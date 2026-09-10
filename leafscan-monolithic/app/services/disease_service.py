import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

try:
    from app.services.disease_database import DISEASE_DATABASE
except (ImportError, ModuleNotFoundError) as e:
    DISEASE_DATABASE = {}

def parse_disease_class(disease_full: str) -> tuple:
    
    if "___" in disease_full:
        parts = disease_full.split("___")
        if len(parts) == 2:
            plant_part = parts[0]
            
            if "(" in plant_part:
                plant_type = plant_part.split("(")[0].strip()
            else:
                plant_type = plant_part.strip()
            
            plant_type = plant_type.rstrip("_")
            
            disease_name_raw = parts[1]
            disease_name = disease_name_raw.replace("_", " ")
            
            return (plant_type, disease_name)
    
    if "|" in disease_full:
        parts = disease_full.split("|")
        if len(parts) == 2:
            plant_type = parts[0].strip().rstrip("_")
            disease_name = parts[1].replace("_", " ")
            return (plant_type, disease_name)
    
    plant_type = disease_full.replace("_", " ").title()
    disease_name = "Unknown"
    logger.warning(f"⚠️  Could not parse disease_full={disease_full}, using fallback")
    
    return (plant_type, disease_name)


def format_disease_response(disease_name: str, plant_type: str) -> Dict:
    plant_clean = plant_type.strip()
    disease_clean = disease_name.strip()
    
    possible_keys = []
    
    disease_words = disease_clean.split()
    if disease_words:
        if disease_words[0].lower() == plant_clean.lower() and len(disease_words) > 1:
            remaining_words = disease_words[1:]
            concatenated_no_dup = plant_clean + "".join(w.capitalize() for w in remaining_words)
            possible_keys.append(concatenated_no_dup)
            
            concatenated_no_dup_lower = plant_clean + "".join(remaining_words).lower()
            possible_keys.append(concatenated_no_dup_lower)
        
        concatenated = plant_clean + "".join(w.capitalize() for w in disease_words)
        possible_keys.append(concatenated)
        
        concatenated_mixed = plant_clean + disease_words[0] + "".join(w.lower() for w in disease_words[1:])
        possible_keys.append(concatenated_mixed)
        
        concatenated_lower = plant_clean + disease_clean.lower().replace(" ", "")
        possible_keys.append(concatenated_lower)
    
    possible_keys.extend([
        f"{plant_clean}|{disease_clean.lower().replace(' ', '_')}",
        f"{plant_clean}|{disease_clean}",
        f"{plant_clean}|{disease_clean.replace(' ', '_')}",
        f"{plant_clean} {disease_clean}",
    ])
    
    for key in possible_keys:
        if key in DISEASE_DATABASE:
            disease_data = DISEASE_DATABASE[key]
            
            care_advices_list = disease_data.get("careAdvices", [])
            
            if isinstance(care_advices_list, list) and len(care_advices_list) > 0:
                if isinstance(care_advices_list[0], dict) and 'title' in care_advices_list[0]:
                    care_advices = care_advices_list
                else:
                    care_advices = []
            else:
                care_advices = []
            
            response = {
                "plant_type": plant_type,
                "disease_name": disease_name,
                "description": disease_data.get("description", ""),
                "symptoms": disease_data.get("symptoms", []),
                "causes": disease_data.get("causes", []),
                "spread_mechanisms": disease_data.get("spreadmechanisms", []),
                "care_advices": care_advices,
            }
            
            return response
    
    db_keys_lower = {k.lower(): k for k in DISEASE_DATABASE.keys()}
    
    for key in possible_keys:
        key_lower = key.lower()
        if key_lower in db_keys_lower:
            actual_key = db_keys_lower[key_lower]
            disease_data = DISEASE_DATABASE[actual_key]
            
            care_advices_list = disease_data.get("careAdvices", [])
            
            if isinstance(care_advices_list, list) and len(care_advices_list) > 0:
                if isinstance(care_advices_list[0], dict) and 'title' in care_advices_list[0]:
                    care_advices = care_advices_list
                else:
                    care_advices = []
            else:
                care_advices = []
            
            response = {
                "plant_type": plant_type,
                "disease_name": disease_name,
                "description": disease_data.get("description", ""),
                "symptoms": disease_data.get("symptoms", []),
                "causes": disease_data.get("causes", []),
                "spread_mechanisms": disease_data.get("spreadmechanisms", []),
                "care_advices": care_advices,
            }
            
            return response
    
    logger.warning(f"Disease NOT found in database!")
    logger.warning(f"Plant: '{plant_type}', Disease: '{disease_name}'")
    logger.warning(f"Tried {len(possible_keys)} keys:")
    for i, key in enumerate(possible_keys[:5], 1):
        logger.warning(f"{i}. '{key}'")
    
    if DISEASE_DATABASE:
        all_plants = set()
        for k in DISEASE_DATABASE.keys():
            if "|" in k:
                all_plants.add(k.split("|")[0])
            else:
                for i, char in enumerate(k):
                    if i > 0 and char.isupper():
                        all_plants.add(k[:i])
                        break
        
        sample_keys = [k for k in DISEASE_DATABASE.keys() if k.startswith(plant_clean) or ("|" in k and k.split("|")[0] == plant_clean)]
        if sample_keys:
            logger.warning(f"Sample keys for {plant_clean}: {sample_keys[:3]}")
    else:
        logger.error(f"DATABASE IS EMPTY!")
    
    error_msg = (
        f"Disease '{disease_name}' for plant '{plant_type}' not found in database. "
        f"Please check the /api/diseases endpoint for available diseases."
    )
    raise ValueError(error_msg)


def get_all_diseases() -> Dict:
    diseases_by_plant = {}
    
    for key in DISEASE_DATABASE.keys():
        if "|" in key:
            plant = key.split("|", 1)[0]
            disease = key.split("|", 1)[1].replace("_", " ")
        else:
            data = DISEASE_DATABASE[key]
            plant = data.get("plantname", key.split()[0])
            disease = data.get("diseasename", key)
        
        if plant not in diseases_by_plant:
            diseases_by_plant[plant] = []
        
        diseases_by_plant[plant].append({
            "name": disease,
            "key": key
        })
    
    total = sum(len(v) for v in diseases_by_plant.values())
    return diseases_by_plant


def get_disease_by_key(disease_key: str) -> Optional[Dict]:
    """
    Get disease information by exact database key.
    
    Args:
        disease_key: Database key (e.g., "AppleApplesscab")
    
    Returns:
        Disease data dict or None if not found
    """
    return DISEASE_DATABASE.get(disease_key)


def debug_database_status() -> Dict:
    plants = set()
    for k in DISEASE_DATABASE.keys():
        if "|" in k:
            plants.add(k.split("|")[0])
        else:
            data = DISEASE_DATABASE.get(k, {})
            plants.add(data.get("plantname", k.split()[0]))
    
    return {
        "total_entries": len(DISEASE_DATABASE),
        "plants": sorted(list(plants)),
        "sample_keys": list(DISEASE_DATABASE.keys())[:10],
        "database_loaded": len(DISEASE_DATABASE) > 0,
        "status": "Ready" if DISEASE_DATABASE else "Empty - Import Failed"
    }