DISEASE_DATABASE = {
    # ========== APPLE (5 DISEASES) ==========
    "AppleApplescab": {
        "plantname": "Apple",
        "diseasename": "Apple Scab",
        "description": "Apple scab is caused by the ascomycete fungus Venturia inaequalis. This is the most economically important disease of apples in temperate regions. The fungus overwinters in fallen leaves and produces ascospores in spring that infect new foliage. Infected fruit becomes unmarketable, and severe defoliation reduces tree vigor and next year's fruit production.",
        "symptoms": [
            "Dark olive-green to black velvety lesions on leaves with indefinite margins",
            "Similar scab lesions on fruit surfaces causing russetting or cork-like appearance",
            "Premature yellowing and abscission of infected leaves",
            "Distorted, cracked, or russeted fruit with reduced market value",
            "Lesions may appear on petioles, twigs, and flower clusters"
        ],
        "causes": [
            "Venturia inaequalis fungal pathogen with ascospores and conidia",
            "Cool, wet spring weather 15-21°C during budbreak and leaf emergence",
            "High humidity and prolonged leaf wetness (12+ hours required)",
            "Poor air circulation and canopy density",
            "Infected leaf residue from previous seasons"
        ],
        "spreadmechanisms": [
            "Ascospores released from overwintering leaf debris in spring",
            "Conidia spread via rain splash to uninfected foliage",
            "Wind-borne spores during wet weather",
            "Contaminated pruning tools spreading fungal mycelium",
            "Pseudothecia in fallen leaves ensuring persistence"
        ],
        "careAdvices": [
            {"title": "Rake and remove fallen leaves; do not compost diseased material", "why": "Eliminates overwintering structures; burying 6 inches deep also works"},
            {"title": "Prune branches to thin canopy allowing sunlight penetration", "why": "Faster leaf drying reduces wetness period below infection threshold"},
            {"title": "Apply sulfur spray from green tip through petal fall stage", "why": "Cost-effective preventive for susceptible varieties; repeat every 10-14 days"},
            {"title": "Water early morning via drip system at soil level only", "why": "Avoids overhead wetting; rain exposure still presents risk regardless"},
            {"title": "Plant resistant cultivars like Liberty, Priscilla, or Enterprise", "why": "Best long-term solution; eliminates fungicide need for new orchards"}
        ]
    },
    "AppleBlackrot": {
        "plantname": "Apple",
        "diseasename": "Black Rot",
        "description": "Black rot is caused by Botryosphaeria obtusa, a necrotrophic fungus in the Botryosphaeriaceae family. While primarily a fruit rot pathogen, it causes cankers on branches and trunk. The fungus survives as spores in infected bark cankers and mummified fruit.",
        "symptoms": [
            "Circular black lesions with concentric rings (target pattern) on fruit",
            "Brown to black spots with yellow halos on leaves, often at margins",
            "Sunken cankers on twigs and branches that enlarge annually",
            "Mummified fruit persisting on branches through winter",
            "Weeping lesions on cankers during wet weather"
        ],
        "causes": [
            "Botryosphaeria obtusa with ascospores and pycnidial spores",
            "Mechanical tree injury from pruning, sunscald, or freeze damage",
            "Tree stress from poor irrigation or nutrition",
            "Warm, humid conditions (25-30°C) favoring fungal growth",
            "Infected wood or fruit material providing inoculum"
        ],
        "spreadmechanisms": [
            "Rain splash from cankers spreading pycnidial spores",
            "Wind-borne ascospores and conidia during warm weather",
            "Contaminated pruning tools between trees",
            "Mummified fruit providing year-round spore production",
            "Infected nursery stock establishing disease in new orchards"
        ],
        "careAdvices": [
            {"title": "Remove cankers and mummified fruit by hand pruning", "why": "Direct removal reduces inoculum source; sterilize tools between cuts"},
            {"title": "Avoid unnecessary pruning; prune only in dry weather", "why": "Pruning wounds are primary entry points; timing is critical"},
            {"title": "Apply copper fungicide post-harvest if disease history exists", "why": "Copper is preventive only; apply when disease conditions likely"},
            {"title": "Maintain consistent irrigation avoiding tree stress", "why": "Stressed trees more susceptible; water during dry periods only"},
            {"title": "Avoid planting in frost-prone, low areas", "why": "Site selection prevents injury predisposing trees to infection"}
        ]
    },
    "AppleCedarapplerust": {
        "plantname": "Apple",
        "diseasename": "Cedar Apple Rust",
        "description": "Cedar apple rust is caused by Gymnosporangium juniperi-virginianae, a macrocyclic rust fungus. The disease requires two hosts to complete its life cycle—cedar/juniper trees and apple/crabapple. The fungus causes significant fruit damage and cosmetic leaf lesions.",
        "symptoms": [
            "Distinctive yellow-orange blisters and pustules on leaf undersides",
            "Bright orange aecia on fruit with prominent tube-like projections",
            "Yellow halos surrounding fruit lesions, expanding into tissues",
            "Distorted, malformed fruit that cracks and develops secondary infections",
            "Affected leaves yellow and eventually abscise prematurely"
        ],
        "causes": [
            "Gymnosporangium juniperi-virginianae requires both apple and juniper hosts",
            "Spores overwintering on cedar/juniper galls, releasing in spring",
            "Wet weather during pink bud to petal fall stage favoring infection",
            "Presence of juniper or cedar trees within 2-3 km of apple orchard",
            "Susceptible apple varieties including Jonathan and Winesap"
        ],
        "spreadmechanisms": [
            "Basidiospores from cedar/juniper galls blown to apple foliage and fruit",
            "Wind-borne basidiospores traveling up to 3 km during wet springs",
            "Primary infection occurring from budbreak through petal fall",
            "Secondary spread limited as apple is alternate host only"
        ],
        "careAdvices": [
            {"title": "Remove junipers and cedars within 2 km of orchard if possible", "why": "Eliminates disease cycle; complete removal preferred but costly"},
            {"title": "Plant resistant varieties (Granny Smith, Liberty, and others)", "why": "Varietal resistance most economical long-term solution"},
            {"title": "Apply ferbam or sulfur spray at pink bud through petal fall", "why": "Timing critical; applications after petal fall ineffective"},
            {"title": "Scout junipers for galls; prune infected twigs in dormant season", "why": "Reduces spore source; repeat annually for management"},
            {"title": "Thin fruit to remove infected specimens immediately", "why": "Prevents secondary infections and spore production"}
        ]
    },
    "ApplePowderymildew": {
        "plantname": "Apple",
        "diseasename": "Powdery Mildew",
        "description": "Apple powdery mildew is caused by Podosphaera leucotricha, an obligate parasite that infects only above-ground tissues. The fungus causes white powdery coating on leaves, shoots, and fruit.",
        "symptoms": [
            "White powdery coating on leaf surfaces, petioles, and young shoots",
            "Infected leaves become curled, distorted, and reddish-purple",
            "New shoot growth stunted with reduced lateral branch development",
            "Fruit develops russet spots and russetting of entire surface",
            "Brown crusty patches on fruit that crack and become corky"
        ],
        "causes": [
            "Podosphaera leucotricha fungus overwinters in flower buds and shoot tips",
            "Warm, dry conditions (18-24°C) with high relative humidity favoring infection",
            "Spring infection beginning at bloom stage and continuing through summer",
            "Lack of air circulation within dense canopies",
            "Susceptible varieties including Red Delicious and Jonagold"
        ],
        "spreadmechanisms": [
            "Conidia produced on infected leaves dispersed by air currents",
            "Wind-borne spores capable of traveling several hundred meters",
            "Continuous sporulation on infected tissues throughout growing season",
            "No water required for spore dispersal, unlike other fungal pathogens",
            "Overwintering in flower buds ensuring perpetual supply"
        ],
        "careAdvices": [
            {"title": "Prune severely to remove infected shoots and open canopy", "why": "Removes primary inoculum; improved air circulation reduces humidity"},
            {"title": "Apply sulfur starting at tight cluster stage through early summer", "why": "Effective and organic; apply weekly when conditions favorable"},
            {"title": "Use resistant varieties like Liberty, Priscilla, or Golden Delicious", "why": "Most economical long-term solution; avoiding fungicide need"},
            {"title": "Avoid high nitrogen fertilization promoting lush susceptible growth", "why": "Mature tissues more resistant; balanced nutrition preferred"},
            {"title": "Monitor new shoot tips weekly during spring for early signs", "why": "Early detection enables control before disease becomes established"}
        ]
    },
    "AppleHealthy": {
        "plantname": "Apple",
        "diseasename": "Healthy",
        "description": "Healthy apple foliage and fruit show no signs of disease or pest damage. Leaves are uniformly colored green, turgid, and free of lesions, spots, or abnormal markings.",
        "symptoms": [
            "Uniform green coloration on all leaves without spots or lesions",
            "Firm, turgid leaf and fruit tissues",
            "Normal growth patterns and fruit development",
            "No visible signs of pathogenic infection or pest damage",
            "Clean fruit surface without russetting, scabbing, or rot"
        ],
        "causes": [
            "Proper cultural practices including adequate irrigation and nutrition",
            "Effective pest and disease management programs",
            "Favorable environmental conditions for plant growth",
            "Resistant or tolerant varieties selected for growing region",
            "Good sanitation practices preventing pathogen establishment"
        ],
        "spreadmechanisms": [
            "No disease or pest spread when plants are healthy",
            "Maintenance of health through continued proper management",
            "Regular monitoring to detect early signs of problems"
        ],
        "careAdvices": [
            {"title": "Maintain consistent irrigation providing 1-2 inches water weekly", "why": "Adequate water supports vigor and disease resistance"},
            {"title": "Apply balanced fertilizer maintaining nitrogen, phosphorus, potassium", "why": "Proper nutrition supports immune function and growth"},
            {"title": "Prune to maintain open canopy allowing air circulation", "why": "Reduces humidity and conditions favoring fungal diseases"},
            {"title": "Monitor weekly for early pest and disease signs", "why": "Early detection enables rapid management before problems worsen"},
            {"title": "Apply dormant oil spray in late winter for pest suppression", "why": "Preventive approach reduces need for growing season applications"}
        ]
    },

    # ========== BLUEBERRY (1 DISEASE) ==========
    "BlueberryHealthy": {
        "plantname": "Blueberry",
        "diseasename": "Healthy",
        "description": "Healthy blueberry plants exhibit vigorous growth with deep green foliage, proper flowering, and normal fruit development. Plants are free of disease symptoms, pest damage, and nutrient deficiencies.",
        "symptoms": [
            "Deep green, glossy leaves without spots or discoloration",
            "Abundant flower production with normal fruit set",
            "Blue or purple fruit depending on variety with waxy bloom",
            "Firm fruit with typical size for cultivar",
            "Healthy branch structure without cankers or dieback"
        ],
        "causes": [
            "Proper pH management (4.0-5.5 soil pH suited to blueberries)",
            "Well-draining sandy or amended soil with high organic matter",
            "Consistent moisture through drip irrigation or mulching",
            "Adequate spacing for air circulation and sunlight penetration",
            "Effective pest and disease prevention programs"
        ],
        "spreadmechanisms": [
            "No disease development when plants maintain health",
            "Healthy plants establish strong canopies resisting pest colonization"
        ],
        "careAdvices": [
            {"title": "Maintain acidic soil pH between 4.0-5.5 with peat moss amendments", "why": "Blueberries require acid conditions; higher pH causes chlorosis"},
            {"title": "Mulch with pine needles or bark maintaining 2-3 inch depth", "why": "Conserves moisture, maintains cool roots, and reduces soil pH"},
            {"title": "Water deeply 1-2 times weekly during growing season", "why": "Shallow roots require consistent moisture; mulch helps retention"},
            {"title": "Thin fruit clusters early in season to increase berry size", "why": "Hand thinning improves marketability and consumer appeal"},
            {"title": "Prune to maintain open bush structure removing old canes", "why": "Rejuvenation pruning maintains vigor and productivity"}
        ]
    },

    # ========== CHERRY (2 DISEASES) ==========
    "CherryHealthy": {
        "plantname": "Cherry",
        "diseasename": "Healthy",
        "description": "Healthy cherry trees exhibit dark green glossy foliage, normal bud development, and characteristic cherry fruit. Leaves are free of lesions, spots, or abnormal coloration.",
        "symptoms": [
            "Uniform dark green foliage with glossy appearance",
            "Normal growth patterns and lateral branching",
            "Proper flower development and fruit set",
            "Cherry fruit with unmarred skin and proper coloring",
            "No evidence of pest galleries or disease symptoms"
        ],
        "causes": [
            "Well-draining soil with moderate fertility",
            "Adequate water during fruit development (June-July)",
            "Proper pruning to maintain tree structure and light penetration",
            "Effective sanitation removing mummified fruit and diseased wood",
            "Variety selection appropriate for regional climate"
        ],
        "spreadmechanisms": [
            "Healthy trees provide poor environment for pathogen establishment",
            "Strong plant vigor resists pest colonization"
        ],
        "careAdvices": [
            {"title": "Water deeply during June-July when fruit developing", "why": "Adequate water at fruit enlargement prevents small, poor quality fruit"},
            {"title": "Remove mummified fruit and dead wood annually", "why": "Eliminates disease and pest overwintering sites"},
            {"title": "Prune to maintain open vase-shaped structure", "why": "Sunlight penetration improves fruit color; air flow prevents disease"},
            {"title": "Thin fruit to 4-6 inches apart for large sweet cherries", "why": "Hand thinning improves size and market value of remaining fruit"},
            {"title": "Use bird netting or scare tactics if birds damaging fruit", "why": "Physical barriers more effective than scaring methods alone"}
        ]
    },
    "CherryPowderymildew": {
        "plantname": "Cherry",
        "diseasename": "Powdery Mildew",
        "description": "Cherry powdery mildew is caused by Podosphaera clandestina, an obligate fungal pathogen. The disease appears as white powdery coating on leaves and fruits. Young fruit may be completely covered in white mycelium.",
        "symptoms": [
            "White powdery coating on leaf surfaces and undersides",
            "Infected leaves curl upward and become thick and rigid",
            "White coverage of entire young fruit early in season",
            "Fruit russetting and cracking when infected early",
            "Premature leaf senescence and defoliation in severe cases"
        ],
        "causes": [
            "Podosphaera clandestina fungus overwintering on infected tissue",
            "Warm days (20-24°C) and cool nights (10-15°C) favoring infection",
            "High humidity and poor air circulation within canopy",
            "Late spring and early summer being peak infection periods",
            "Continued sporulation on infected tissues throughout season"
        ],
        "spreadmechanisms": [
            "Airborne conidia spreading rapidly in favorable conditions",
            "No water required for spore germination or infection",
            "Continuous sporulation providing persistent inoculum",
            "Spores capable of traveling significant distances on air currents"
        ],
        "careAdvices": [
            {"title": "Apply sulfur starting at late pink bud stage weekly through July", "why": "Most effective organic option; apply when no rain forecast within 48 hours"},
            {"title": "Prune to thin canopy improving air circulation", "why": "Reduced humidity suppresses fungal development and sporulation"},
            {"title": "Avoid high nitrogen applications promoting lush susceptible growth", "why": "Moderate nutrition favors more resistant mature tissues"},
            {"title": "Remove and destroy early infected shoots and fruit", "why": "Early season management prevents mid-season epidemic development"},
            {"title": "Select resistant varieties when establishing new plantings", "why": "Resistance most effective long-term solution for disease-prone areas"}
        ]
    },
 #Cercosporaleafspotgrayleafspot
    # ========== CORN (4 DISEASES) ==========
    "CornCercosporaleafspotgrayleafspot": {
        "plantname": "Corn",
        "diseasename": "Cercospora Leaf Spot",
        "description": "Corn Cercospora leaf spot is caused by Cercospora zeae-maydis, a fungal leaf pathogen. The disease produces numerous small necrotic lesions on leaves and sheaths. Severe infections reduce photosynthetic area.",
        "symptoms": [
            "Small elliptical lesions with tan centers and dark purple margins on lower leaves",
            "Lesions gradually expand and coalesce in severe infections",
            "Infected leaves appear scorched with brown necrotic tissue",
            "Lesions primarily on older leaves moving upward as season progresses",
            "Premature leaf senescence when disease severe"
        ],
        "causes": [
            "Cercospora zeae-maydis fungal spores overwintering on crop residue",
            "Warm, wet weather (25-28°C) with high humidity favoring infection",
            "Extended leaf wetness (12+ hours) required for infection",
            "Susceptible hybrid and open-pollinated corn varieties",
            "Continuous cropping favoring pathogen survival"
        ],
        "spreadmechanisms": [
            "Rain splash spreading spores from infected to healthy leaves",
            "Wind-borne spores during wet weather periods",
            "Contaminated farm equipment moving spores between fields",
            "Residue-borne spores surviving winter in temperate regions"
        ],
        "careAdvices": [
            {"title": "Plant resistant or tolerant hybrids suited to your region", "why": "Genetic resistance is most economical control method"},
            {"title": "Remove or plow under corn residue after harvest", "why": "Breaks disease cycle by eliminating overwintering inoculum"},
            {"title": "Rotate corn with non-host crops; avoid planting 2 years consecutively", "why": "Reduces pathogen inoculum level in soil and residue"},
            {"title": "Apply fungicide at first sign of disease on lower leaves", "why": "Protects upper leaves during critical grain fill period if spray timing right"},
            {"title": "Provide adequate nitrogen supporting plant vigor and recovery", "why": "Well-nourished plants better tolerate foliar disease"}
        ]
    },
    "CornCommonrust": {
        "plantname": "Corn",
        "diseasename": "Common Rust",
        "description": "Corn common rust is caused by Puccinia sorghi, a macrocyclic rust fungus. The disease produces rusty-colored pustules on leaf surfaces. While generally not as damaging as southern leaf blight, severe infections can reduce grain yield and quality.",
        "symptoms": [
            "Reddish-brown to rust-colored pustules erupting through leaf cuticle",
            "Pustules elongated along leaf veins in distinctive linear patterns",
            "Both leaf surfaces affected with heavier infection on upper side",
            "Pustules eventually darken to chocolate brown as season progresses",
            "Severe infections causing partial premature desiccation of leaves"
        ],
        "causes": [
            "Puccinia sorghi fungus requiring alternate barberry host for sexual stage",
            "Moderate temperatures (15-25°C) and high humidity favoring infection",
            "Continuous cloud cover and frequent rainfall favoring spore spread",
            "Rust-susceptible corn hybrids without resistance genes",
            "Presence of barberry species (alternate host) in some regions"
        ],
        "spreadmechanisms": [
            "Uredospores produced in pustules spreading via wind and rain",
            "Spores capable of traveling long distances on atmospheric currents",
            "Aecial stage on barberry (minor role in most corn-growing areas)",
            "Primary inoculum from previous year's residue in southern regions"
        ],
        "careAdvices": [
            {"title": "Plant rust-resistant or tolerant corn hybrids for your area", "why": "Varietal resistance most economical and environmentally sound"},
            {"title": "Monitor fields weekly during mid-season noting pustule development", "why": "Early detection enables timely fungicide application if needed"},
            {"title": "Remove barberry hedges if present within 1 mile of corn field", "why": "Eliminates alternate host; reducing but not eliminating disease risk"},
            {"title": "Apply fungicide when 5-10% of leaf area infected at silking stage", "why": "Timing critical; applications too late ineffective for yield protection"},
            {"title": "Plow under corn residue after harvest", "why": "Reduces inoculum for next season in some regions"}
        ]
    },
    "CornHealthy": {
        "plantname": "Corn",
        "diseasename": "Healthy",
        "description": "Healthy corn plants display vigorous upright growth with dark green leaves. Leaves are free of spots, streaks, or discoloration. Ear development is normal for growth stage with proper kernel formation.",
        "symptoms": [
            "Uniform dark green foliage with waxy coating",
            "Strong upright plant architecture without lodging",
            "Normal leaf expansion and development progression",
            "Straight rows with consistent plant heights",
            "Proper ear development at appropriate nodes"
        ],
        "causes": [
            "Well-drained soil with adequate fertility and organic matter",
            "Proper seeding rates and plant spacing",
            "Timely rainfall or irrigation providing consistent moisture",
            "Effective pest management preventing economic damage",
            "Absence of disease-causing pathogens"
        ],
        "spreadmechanisms": [
            "Healthy plants resist pathogen and pest colonization",
            "Strong vigor enables quick recovery from environmental stress"
        ],
        "careAdvices": [
            {"title": "Provide 20-25 inches rainfall or irrigation during season", "why": "Moisture-stress periods reduce final yield significantly"},
            {"title": "Apply nitrogen side-dress at V4-V6 growth stage", "why": "Timing ensures nutrient availability during critical growth periods"},
            {"title": "Scout fields weekly for pest and disease symptoms", "why": "Early detection enables rapid management of developing problems"},
            {"title": "Maintain equipment cleanliness between fields preventing disease spread", "why": "Contaminated equipment major vector for seed-borne pathogens"},
            {"title": "Select hybrids adapted to your climate and soil conditions", "why": "Proper variety selection foundation for healthy crops"}
        ]
    },
    "CornNorthernleafblight": {
        "plantname": "Corn",
        "diseasename": "Northern Leaf Blight",
        "description": "Corn northern leaf blight is caused by Exserohilum turcicum, a fungal leaf pathogen. The disease produces large elliptical lesions on corn leaves. Severe infections can cause significant defoliation and grain yield reductions of 25-30%.",
        "symptoms": [
            "Large elliptical lesions (1-3 inches) with tan centers and dark margins",
            "Lesions initially appear on lower leaves spreading upward",
            "Grayish-brown lesions with smoke-like appearance at high humidity",
            "Lesions eventually coalesce causing large areas of necrotic tissue",
            "Severe defoliation from bottom upward in highly susceptible varieties"
        ],
        "causes": [
            "Exserohilum turcicum fungus overwintering on corn residue",
            "Cool to moderate temperatures (18-27°C) and high humidity",
            "Leaf wetness (12-24 hours) required for infection",
            "Susceptible corn hybrids lacking Ht resistance genes",
            "Continuous corn or inadequate residue management"
        ],
        "spreadmechanisms": [
            "Conidia dispersed by wind and rain from infected leaves",
            "Splash from rain spreading spores to lower leaf surfaces",
            "Wind-borne spores capable of moving several miles",
            "Residue-borne spores surviving winter in infected tissue"
        ],
        "careAdvices": [
            {"title": "Plant Ht1, Ht2, or Ht3 resistance gene hybrids for high-risk areas", "why": "Genetic resistance most reliable and economical control"},
            {"title": "Plow under or compost corn residue after harvest", "why": "Eliminates primary inoculum for next season"},
            {"title": "Avoid continuous corn; rotate with non-susceptible crops", "why": "Breaks disease cycle through diversity and pathogen starvation"},
            {"title": "Apply fungicide at first sign when lesions visible on lower leaves", "why": "Timing critical; applications after grain fill ineffective"},
            {"title": "Monitor weather patterns; apply fungicide during high-risk periods", "why": "Cool, wet weather indicates need for preventive applications"}
        ]
    },

    # ========== GRAPE (4 DISEASES) ==========
    "GrapeBlackrot": {
        "plantname": "Grape",
        "diseasename": "Black Rot",
        "description": "Grape black rot is caused by Guignardia bidwellii, an ascomycete fungus. The disease infects leaves, flowers, and fruit. Infected fruit becomes mummified and remains on vine providing overwintering inoculum.",
        "symptoms": [
            "Small round brown spots on grape leaves with concentric rings",
            "Black circular lesions on young grape berries (early infection)",
            "Diseased berries shrivel and mummify becoming hard and black",
            "Gray sporulation evident on mummified fruit during wet weather",
            "Flower cluster infection causing complete blossom blast"
        ],
        "causes": [
            "Guignardia bidwellii fungus overwintering in mummified fruit and cane lesions",
            "Wet weather (rain or high humidity) during budbreak through fruit development",
            "Temperatures (22-27°C) optimal for infection and sporulation",
            "High moisture availability extending infection period",
            "Young developing tissues (shoots, flowers, berries) most susceptible"
        ],
        "spreadmechanisms": [
            "Ascospores discharged from infected canes during spring rain periods",
            "Wind and rain-borne ascospores landing on young susceptible tissues",
            "Conidia produced on infected leaves and fruit spreading disease",
            "Mummified fruit providing continuous inoculum throughout season"
        ],
        "careAdvices": [
            {"title": "Remove mummified fruit from vines and surrounding area in dormant season", "why": "Eliminates primary inoculum source for spring infection"},
            {"title": "Prune to maintain open canopy ensuring rapid leaf drying", "why": "Reduced humidity and faster drying suppresses infection"},
            {"title": "Apply sulfur or copper fungicide from budbreak through fruit development", "why": "Preventive timing critical; cure is difficult once infection established"},
            {"title": "Thin fruit clusters early in season to improve air circulation", "why": "Better penetration of fungicides and faster drying of wet canopy"},
            {"title": "Select resistant rootstocks and scion varieties when replanting", "why": "Eliminates disease through genetics in future vineyard operations"}
        ]
    },
    "GrapeEsca": {
        "plantname": "Grape",
        "diseasename": "Esca",
        "description": "Esca is a complex disease caused by multiple fungal pathogens including Phaeoacremonium minimum, Phaeomoniella chlamydospora, and Fomitiporia species. The disease causes vascular discoloration and wood decay within the vine.",
        "symptoms": [
            "Unilateral wilting and drying of shoots despite adequate soil moisture",
            "Striped or striations of discolored wood when cane cut longitudinally",
            "Brown to black discolored wood tissue spreading through cross-sections",
            "Gradual decline of affected vines over 3-5 years",
            "Complete vine death once symptoms become severe"
        ],
        "causes": [
            "Multiple fungal pathogens entering through pruning wounds",
            "Infection occurs when conditions warm (spring-early summer)",
            "Pathogens colonize wood tissues causing vascular discoloration",
            "Disease progression slow with symptoms appearing years after infection",
            "Warm climates favoring fungal development and disease expression"
        ],
        "spreadmechanisms": [
            "Conidia from infected wood spreading through pruning wounds",
            "Contaminated pruning tools transmitting fungal inoculum"
        ],
        "careAdvices": [
            {"title": "Sterilize pruning tools with 10% bleach between cuts", "why": "Prevents mechanical spread of fungal inoculum between vines"},
            {"title": "Prune only during dry season; seal large wounds with dressing", "why": "Reduces infection courts and fungal colonization of wounds"},
            {"title": "Remove and destroy infected vines showing symptoms", "why": "Eliminates disease source; do not replant on same spot"},
            {"title": "Maintain vine vigor through proper irrigation and nutrition", "why": "Stressed vines more susceptible; vigorous vines resist disease better"},
            {"title": "Apply fungicide to pruning wounds immediately after cutting", "why": "Preventive treatment only effective when applied immediately"}
        ]
    },
    "GrapePowderymildew": {
        "plantname": "Grape",
        "diseasename": "Powdery Mildew",
        "description": "Powdery mildew of grape is caused by Uncinula necator, an obligate fungal parasite. This disease thrives in warm, dry conditions and is prevalent in many grape-growing regions worldwide.",
        "symptoms": [
            "White to grayish powdery coating on upper and lower leaf surfaces",
            "Similar coating on shoots, flower buds, and berries in spring and summer",
            "Infected leaves curl with reddish discoloration along margins",
            "Severely infected berries develop russetting; shot berries fail to mature",
            "Distinctive musty odor from infected tissues"
        ],
        "causes": [
            "Uncinula necator fungal parasite requiring living grape tissue",
            "Warm daytime temperatures (20-26°C) with cool nights",
            "Moderate humidity (40-70%) with dry leaf surfaces",
            "Dense canopy reducing air circulation",
            "Susceptible grape varieties"
        ],
        "spreadmechanisms": [
            "Wind-dispersed conidia produced abundantly on infected tissues",
            "Does not require rainfall or leaf wetness for infection",
            "Ascospores from overwintering structures",
            "Aerial dispersal extremely efficient"
        ],
        "careAdvices": [
            {"title": "Prune aggressively to open canopy and improve air circulation", "why": "Dry conditions and air movement inhibit spore germination"},
            {"title": "Apply sulfur dust every 14 days from pre-bloom through bunch closure", "why": "Sulfur is cost-effective preventive; only effective before infection"},
            {"title": "Avoid high-nitrogen fertilization promoting tender shoot growth", "why": "Reduces susceptible tissue; balanced nutrition better"},
            {"title": "Do not apply sulfur if temperatures exceed 32°C within 48 hours", "why": "Sulfur burn risk high in heat; skip applications during hot weather"},
            {"title": "Plant powdery-mildew-resistant rootstock/scion combinations", "why": "Eliminates fungicide need; best long-term economics"}
        ]
    },
    "GrapeHealthy": {
        "plantname": "Grape",
        "diseasename": "Healthy",
        "description": "Healthy grape vines appear healthy with vigorous growth and normal fruit development. Continue proper care practices.",
        "symptoms": [
            "Healthy green foliage with no visible disease",
            "Normal flowering and fruit set",
            "Strong vine growth and canopy",
            "Good berry size and color development"
        ],
        "causes": [
            "Excellent growing conditions with proper temperature and moisture",
            "Effective disease prevention practices",
            "Good variety selection with disease resistance",
            "Proper irrigation, nutrition, and canopy management"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Continue preventive practices"
        ],
        "careAdvices": [
            {"title": "Scout vines every 2 weeks during growing season for disease or pest symptoms", "why": "Early detection prevents economic loss"},
            {"title": "Prune for open canopy allowing light and air penetration into fruit zone", "why": "Improves fruit quality and reduces disease pressure"},
            {"title": "Water deeply but infrequently; drip irrigation best applied early morning", "why": "Encourages deep rooting and avoids creating wet canopy conditions"},
            {"title": "Apply balanced fertilizer in spring; adjust based on leaf/petiole analysis", "why": "Proper nutrition supports vine health and grape quality"}
        ]
    },

    # ========== ORANGE (1 DISEASE) ==========
    "OrangeHealthy": {
        "plantname": "Orange",
        "diseasename": "Healthy",
        "description": "Healthy orange trees display vigorous growth with dark green foliage and normal fruit development. Leaves are free of spots or discoloration and fruit is unblemished.",
        "symptoms": [
            "Vibrant green foliage with no visible disease",
            "Normal fruit size and coloring",
            "Vigorous tree growth and structure",
            "No visible pest damage or lesions"
        ],
        "causes": [
            "Proper irrigation and nutrition",
            "Effective disease prevention",
            "Good variety selection",
            "Proper environmental conditions"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Healthy trees resist infection"
        ],
        "careAdvices": [
            {"title": "Maintain consistent irrigation during fruit development", "why": "Ensures proper fruit size and quality"},
            {"title": "Apply balanced fertilizer based on soil test", "why": "Supports tree vigor and productivity"},
            {"title": "Scout trees regularly for disease or pest signs", "why": "Early detection prevents economic loss"},
            {"title": "Maintain proper tree canopy through selective pruning", "why": "Improves air circulation and light penetration"}
        ]
    },

    # ========== PEACH (1 DISEASE) ==========
    "PeachHealthy": {
        "plantname": "Peach",
        "diseasename": "Healthy",
        "description": "Healthy peach trees display vigorous growth with normal fruit development. Leaves are green and free of spots or lesions. Fruit develops proper size and color.",
        "symptoms": [
            "Deep green foliage without spots or lesions",
            "Normal flowering and fruit set",
            "Good fruit size with proper coloring",
            "Vigorous tree growth"
        ],
        "causes": [
            "Proper irrigation during fruit development",
            "Well-balanced nutrition",
            "Effective disease management",
            "Good variety selection"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Healthy tree vigor resists infection"
        ],
        "careAdvices": [
            {"title": "Water deeply during fruit development (June-August)", "why": "Adequate moisture ensures proper fruit size and sweetness"},
            {"title": "Apply balanced fertilizer in early spring", "why": "Supports tree vigor and fruit production"},
            {"title": "Prune to maintain open vase-shaped tree structure", "why": "Improves sunlight penetration and air circulation"},
            {"title": "Thin fruit to 4-6 inches apart early in season", "why": "Improves fruit size and quality"}
        ]
    },
    "PeachBacterialSpot": {
        "plantname": "Peach",
        "diseasename": "Bacterial Spot",
        "description": "Bacterial spot is a serious disease of peach trees caused by bacterial infection, leading to lesions on leaves, fruit, and twigs. It can significantly reduce fruit quality and yield if not properly managed.",
        "symptoms": [
            "Small, dark, water-soaked spots on leaves that may turn angular",
            "Lesions on leaves that dry and fall out, giving a shot-hole appearance",
            "Dark, sunken spots on fruit that may crack as they enlarge",
            "Premature leaf drop in severe infections"
        ],
        "causes": [
            "Infection by the bacterium Xanthomonas arboricola pv. pruni",
            "Warm, wet, and humid weather conditions",
            "Overhead irrigation that keeps foliage wet",
            "Poor air circulation within dense tree canopies"
        ],
        "spreadmechanisms": [
            "Rain splash spreading bacteria between leaves and fruits",
            "Wind-driven rain carrying bacteria over short distances",
            "Contaminated pruning tools",
            "Infected plant debris left in the orchard"
        ],
        "careAdvices": [
            {"title": "Apply copper-based bactericides during early season","why": "Helps reduce bacterial population and prevents early infection"},
            {"title": "Prune trees to improve air circulation","why": "Reduces humidity and leaf wetness, limiting bacterial growth"},
            {"title": "Avoid overhead irrigation","why": "Prevents prolonged leaf wetness which favors disease spread"},
            {"title": "Remove and destroy infected leaves and fruit","why": "Reduces sources of bacterial inoculum"},
            {"title": "Plant resistant or tolerant peach varieties","why": "Minimizes susceptibility to bacterial spot infection"}
        ]
    },

    # ========== PEPPER (2 DISEASES) ==========
    "PepperBacterialspot": {
        "plantname": "Pepper",
        "diseasename": "Bacterial Spot",
        "description": "Pepper bacterial spot is caused by several Xanthomonas species. The disease produces water-soaked lesions on leaves and fruit that become necrotic and corky.",
        "symptoms": [
            "Water-soaked circular lesions with yellow halos on leaves",
            "Lesions enlarge becoming brown with concentric rings",
            "Fruit develops raised pustules with brown centers",
            "Fruit lesions eventually become corky and sunken",
            "Severe leaf drop from bottom upward in infection"
        ],
        "causes": [
            "Xanthomonas campestris or related Xanthomonas species",
            "Warm (25-28°C) wet conditions favoring infection",
            "Overhead irrigation and frequent rainfall",
            "Extended leaf wetness (12+ hours) required",
            "Contaminated seed or transplant material"
        ],
        "spreadmechanisms": [
            "Water splash from rain or overhead irrigation",
            "Wind-driven rain spreading bacteria within canopy",
            "Contaminated tools and hands during pruning/harvest",
            "Infected plant residue in compost or field"
        ],
        "careAdvices": [
            {"title": "Use disease-free certified seed and transplants", "why": "Eliminates seed-borne bacteria at crop establishment"},
            {"title": "Avoid overhead irrigation; use drip systems at soil level", "why": "Wet foliage creates conditions favoring bacterial growth"},
            {"title": "Apply copper bactericide from transplanting through season", "why": "Preventive applications more effective than curative"},
            {"title": "Disinfect pruning tools with 10% bleach between plants", "why": "Prevents mechanical transmission during pruning"},
            {"title": "Remove and destroy infected plants and surrounding residue", "why": "Stops disease spread to nearby healthy pepper plants"}
        ]
    },
    "PepperHealthy": {
        "plantname": "Pepper",
        "diseasename": "Healthy",
        "description": "Healthy pepper plants appear healthy with normal growth and fruit development. Continue proper care practices.",
        "symptoms": [
            "Healthy green foliage with no visible disease",
            "Vigorous flowering and fruit development",
            "No wilting or discoloration",
            "Good fruit size and ripening"
        ],
        "causes": [
            "Excellent growing conditions with proper temperature and moisture",
            "Effective disease prevention practices",
            "Good plant nutrition",
            "Strong plant immunity"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Continue preventive monitoring"
        ],
        "careAdvices": [
            {"title": "Scout plants 2-3 times weekly for early disease or pest symptoms", "why": "Early detection prevents economic loss"},
            {"title": "Water at soil level early morning; provide 1-2 inches water weekly", "why": "Consistent moisture maintains plant vigor"},
            {"title": "Apply balanced fertilizer at planting; side-dress at first flowering", "why": "Proper nutrition supports fruit production"},
            {"title": "Support fruit with stakes or cages to prevent fruit contact with soil", "why": "Prevents soil-borne disease contact on fruit"}
        ]
    },

    # ========== POTATO (1 DISEASE) ==========
    "PotatoHealthy": {
        "plantname": "Potato",
        "diseasename": "Healthy",
        "description": "Healthy potato plants display vigorous growth with dense green foliage and normal tuber development. Plants are free of disease symptoms.",
        "symptoms": [
            "Vigorous upright green foliage",
            "Normal flowering for variety",
            "No spots, lesions, or discoloration",
            "Good tuber development underground"
        ],
        "causes": [
            "Proper irrigation and nutrition",
            "Effective disease prevention",
            "Good seed quality",
            "Favorable growing conditions"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Healthy plants resist infection"
        ],
        "careAdvices": [
            {"title": "Provide consistent moisture (20-25 inches total during season)", "why": "Critical for tuber development and sizing"},
            {"title": "Apply fertilizer at planting and at emergence", "why": "Supports vigorous growth and tuber production"},
            {"title": "Hill soil around developing plants", "why": "Protects developing tubers from light exposure"},
            {"title": "Scout plants weekly for disease or pest symptoms", "why": "Early detection enables rapid management"}
        ]
    },

    # ========== SOYBEAN (1 DISEASE) ==========
    "SoybeanHealthy": {
        "plantname": "Soybean",
        "diseasename": "Healthy",
        "description": "Healthy soybean plants display vigorous growth with normal leaf development and reproductive structure. Plants are free of disease symptoms and pest damage.",
        "symptoms": [
            "Vigorous upright growth with full green canopy",
            "Normal flowering and pod development",
            "No leaf spots, lesions, or discoloration",
            "Good pod and seed development"
        ],
        "causes": [
            "Proper soil moisture and drainage",
            "Adequate nutrition",
            "Effective pest and disease management",
            "Good variety selection"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Healthy plants resist pathogen colonization"
        ],
        "careAdvices": [
            {"title": "Provide adequate moisture during pod-fill stage (R4-R6)", "why": "Critical for seed development and yield"},
            {"title": "Monitor fields weekly for disease or pest symptoms", "why": "Early detection enables timely management"},
            {"title": "Use certified seed free from seed-borne pathogens", "why": "Prevents disease introduction at planting"},
            {"title": "Rotate crops to break disease cycles", "why": "Reduces pathogen inoculum in soil and residue"}
        ]
    },

    # ========== SQUASH (1 DISEASE) ==========
    "SquashPowderymildew": {
        "plantname": "Squash",
        "diseasename": "Powdery Mildew",
        "description": "Squash powdery mildew is caused by Erysiphe cichoracearum and Sphaerotheca fuliginea. The disease produces white powdery coating on leaves. Severe infections reduce photosynthetic area and fruit quality.",
        "symptoms": [
            "White powdery coating on upper and lower leaf surfaces",
            "Infected leaves gradually yellow and die",
            "Powdery growth also appearing on stems and petioles",
            "Fruits becoming sunburned when leaves removed by severe defoliation",
            "Disease typically appearing in mid-season during warm periods"
        ],
        "causes": [
            "Erysiphe cichoracearum or Sphaerotheca fuliginea fungal pathogens",
            "Warm (21-27°C) dry conditions with moderate humidity",
            "High nitrogen fertilization promoting lush susceptible growth",
            "Poor air circulation within dense plant canopy",
            "Susceptible squash and melon varieties"
        ],
        "spreadmechanisms": [
            "Conidia produced on infected leaves dispersed by air currents",
            "No water required for infection (unlike most other fungal pathogens)",
            "Continuous sporulation providing perpetual disease pressure",
            "Airborne spores capable of traveling considerable distances"
        ],
        "careAdvices": [
            {"title": "Apply sulfur spray at first sign of white powder on leaves", "why": "Most effective organic option; begin applications preventively"},
            {"title": "Use drip irrigation at soil level avoiding overhead wetting", "why": "Dry foliage less favorable for fungal development"},
            {"title": "Space plants widely for good air circulation", "why": "Better air flow reduces humidity favoring disease"},
            {"title": "Avoid excess nitrogen promoting lush susceptible growth", "why": "Moderate nutrition favors more resistant mature tissues"},
            {"title": "Select resistant varieties when available for your region", "why": "Genetic resistance most economical long-term solution"}
        ]
    },

    # ========== STRAWBERRY (1 DISEASE) ==========
    "StrawberryHealthy": {
        "plantname": "Strawberry",
        "diseasename": "Healthy",
        "description": "Healthy strawberry plants display vigorous growth with lush green foliage and normal fruit development. Plants are free of disease symptoms.",
        "symptoms": [
            "Vibrant green foliage with no spots or lesions",
            "Normal flowering with abundant fruit development",
            "Red ripening berries with normal size and color",
            "Vigorous runner and crown development"
        ],
        "causes": [
            "Proper soil drainage and fertility",
            "Consistent moisture during growing season",
            "Effective disease and pest prevention",
            "Good variety selection"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Healthy plants resist pathogen colonization"
        ],
        "careAdvices": [
            {"title": "Provide consistent moisture (1-2 inches per week)", "why": "Critical for fruit quality and development"},
            {"title": "Mulch around plants maintaining 2-3 inch depth", "why": "Conserves moisture and prevents soil splash"},
            {"title": "Remove runners except on mother plants for propagation", "why": "Directs energy to fruit production"},
            {"title": "Scout plants regularly for disease or pest symptoms", "why": "Early detection prevents economic loss"}
        ]
    },

    # ========== TOMATO (11 DISEASES) ==========
    "TomatoBacterialspot": {
        "plantname": "Tomato",
        "diseasename": "Bacterial Spot",
        "description": "Tomato bacterial spot is caused by several Xanthomonas species. The disease produces water-soaked lesions on leaves and fruit. Infected fruit becomes unmarketable.",
        "symptoms": [
            "Water-soaked circular lesions with yellow halos on leaves",
            "Lesions enlarge becoming brown with concentric rings",
            "Fruit develops raised pustules with brown centers",
            "Fruit lesions eventually become corky and sunken",
            "Severe leaf drop from bottom upward in infection"
        ],
        "causes": [
            "Xanthomonas campestris or related Xanthomonas species",
            "Warm (25-28°C) wet conditions favoring infection",
            "Overhead irrigation and frequent rainfall",
            "Extended leaf wetness (12+ hours) required",
            "Contaminated seed or transplant material"
        ],
        "spreadmechanisms": [
            "Water splash from rain or overhead irrigation",
            "Wind-driven rain spreading bacteria within canopy",
            "Contaminated tools and hands during pruning/harvest",
            "Infected plant residue in compost or field"
        ],
        "careAdvices": [
            {"title": "Use disease-free certified seed and transplants", "why": "Eliminates seed-borne bacteria at crop establishment (most important)"},
            {"title": "Avoid overhead irrigation; use drip systems at soil level", "why": "Wet foliage creates conditions favoring bacterial growth (most effective)"},
            {"title": "Apply copper bactericide from transplanting through season", "why": "Preventive applications more effective than curative"},
            {"title": "Disinfect pruning tools with 10% bleach between plants", "why": "Prevents mechanical transmission during pruning"},
            {"title": "Remove and destroy infected plants and surrounding residue", "why": "Stops disease spread to nearby healthy tomato plants"}
        ]
    },
    "TomatoEarlyblight": {
        "plantname": "Tomato",
        "diseasename": "Early Blight",
        "description": "Tomato early blight is caused by Alternaria solani. The disease produces target-like lesions on lower leaves. Severe infections cause complete defoliation.",
        "symptoms": [
            "Circular lesions with concentric rings (target pattern) on lower leaves",
            "Lesions start on oldest leaves progressing upward",
            "Brown-gray tissue within lesions surrounded by yellow halo",
            "Lesions eventually coalesce causing extensive necrosis",
            "Premature defoliation starting from plant base"
        ],
        "causes": [
            "Alternaria solani fungus overwintering on soil and plant debris",
            "Warm (21-27°C) humid conditions with frequent rainfall",
            "Extended leaf wetness (12+ hours) required for infection",
            "Overhead irrigation and dense canopy",
            "Mechanical injury creating infection courts"
        ],
        "spreadmechanisms": [
            "Conidia dispersed by wind and rain splash",
            "Spores capable of traveling considerable distances",
            "Direct contact spreading spores",
            "Residue-borne spores surviving in soil"
        ],
        "careAdvices": [
            {"title": "Destroy plant residue after harvest; avoid composting", "why": "Breaks disease cycle by eliminating overwintering inoculum"},
            {"title": "Apply mancozeb or chlorothalonil at first leaf lesions", "why": "Protects healthy foliage if timed properly"},
            {"title": "Remove lower leaves early preventing infection of unaffected tissue", "why": "Reduces primary infection site and inoculum production"},
            {"title": "Space plants for air circulation and rapid drying", "why": "Reduced humidity suppresses fungal sporulation"},
            {"title": "Avoid overhead irrigation; use drip at soil level", "why": "Wet foliage creates conditions favoring fungal growth"}
        ]
    },
    "TomatoHealthy": {
        "plantname": "Tomato",
        "diseasename": "Healthy",
        "description": "Healthy tomato plants exhibit vigorous growth with lush green compound leaves. Plants develop abundant yellow flowers followed by proper fruit development. Leaves are free of spots or discoloration.",
        "symptoms": [
            "Vigorous upright growth with lush green compound leaves",
            "Normal leaf expansion and development",
            "Abundant yellow flowers developing into fruit",
            "Proper fruit development and ripening for variety",
            "No visible disease symptoms or pest damage"
        ],
        "causes": [
            "Fertile well-draining soil with good organic matter",
            "Proper spacing for light penetration and air circulation",
            "Consistent water throughout season (20-25 inches)",
            "Adequate nutrition supporting vigorous growth",
            "Effective pest and disease management programs"
        ],
        "spreadmechanisms": [
            "No disease development in healthy plants",
            "Strong vigor resists pathogen colonization"
        ],
        "careAdvices": [
            {"title": "Water deeply early morning providing 1-2 inches weekly", "why": "Consistent moisture essential for fruit development"},
            {"title": "Apply balanced fertilizer every 2-3 weeks during growing season", "why": "Proper nutrition supports continuous flowering and fruiting"},
            {"title": "Prune suckers to 1-2 main stems for large indeterminate varieties", "why": "Improves air circulation and directs energy to fruit production"},
            {"title": "Scout plants weekly for pest insects and hornworms", "why": "Early detection prevents significant damage"},
            {"title": "Mulch around plants maintaining 2-3 inch depth", "why": "Conserves moisture and suppresses soil-borne pathogens"}
        ]
    },
    "TomatoLateblight": {
        "plantname": "Tomato",
        "diseasename": "Late Blight",
        "description": "Tomato late blight is caused by Phytophthora infestans. The disease causes water-soaked lesions on leaves and fruit. It is the same pathogen as potato late blight.",
        "symptoms": [
            "Water-soaked irregular lesions on leaves starting at margins",
            "Rapid lesion expansion during wet weather",
            "White moldy growth (sporangia) on leaf undersides in morning",
            "Tan-brown greasy rot on fruit with white mold inside",
            "Rapid plant collapse during wet extended periods"
        ],
        "causes": [
            "Phytophthora infestans oomycete favoring cool wet (13-18°C) periods",
            "Extended leaf wetness (12+ hours) required for infection",
            "High humidity and poor air circulation",
            "Overhead irrigation and frequent rainfall",
            "Infected volunteer potatoes and wild solanaceous hosts nearby"
        ],
        "spreadmechanisms": [
            "Sporangia produced on infected foliage dispersed by wind/rain",
            "Water splash spreading sporangia within field",
            "Zoospores swimming in water",
            "Infected fruit providing inoculum for next season"
        ],
        "careAdvices": [
            {"title": "Eliminate potato volunteers and wild solanaceous plants nearby", "why": "Removes alternate disease hosts providing inoculum"},
            {"title": "Apply mancozeb or copper fungicide weekly during cool wet periods", "why": "Preventive applications most effective; curative treatments ineffective"},
            {"title": "Avoid overhead irrigation; use drip systems at soil level", "why": "Wet foliage creates ideal conditions for disease"},
            {"title": "Destroy plant residue immediately after harvest", "why": "Eliminates diseased fruit and vegetative structures"},
            {"title": "Space plants for excellent air circulation", "why": "Good air flow reduces humidity and promotes leaf drying"}
        ]
    },
    "TomatoLeafmold": {
        "plantname": "Tomato",
        "diseasename": "Leaf Mold",
        "description": "Tomato leaf mold is caused by Passalora fulva. The disease produces yellow spots on upper leaf surfaces with olive-green moldy growth on undersides. It is primarily a greenhouse disease.",
        "symptoms": [
            "Circular yellow spots on upper leaf surfaces",
            "Corresponding velvety olive-green to brown sporulation on undersides",
            "Spots gradually enlarge and coalesce covering much of leaf",
            "Severely affected leaves eventually yellow and drop",
            "Disease typically starting on lower leaves progressing upward"
        ],
        "causes": [
            "Passalora fulva fungus favoring high humidity (85-90%) and warmth",
            "Poor air circulation within greenhouse or dense canopy",
            "Overhead watering and high ambient humidity",
            "Susceptible tomato varieties without resistance",
            "Cool nights (15-18°C) with warm days (20-25°C) ideal"
        ],
        "spreadmechanisms": [
            "Conidia produced abundantly on infected undersides",
            "Spores dispersed by air currents and direct contact",
            "No water required for spore germination",
            "Spores viable for extended periods"
        ],
        "careAdvices": [
            {"title": "Lower humidity by improving greenhouse ventilation and air circulation", "why": "Disease favors 85% humidity; reduced humidity suppresses growth"},
            {"title": "Remove infected leaves and destroy; do not compost", "why": "Eliminates primary inoculum source"},
            {"title": "Apply sulfur dust or chlorothalonil at first sign of disease", "why": "Controls fungal growth on foliage"},
            {"title": "Space plants for excellent air circulation", "why": "Good air flow reduces humidity favoring disease"},
            {"title": "Use resistant varieties with Cf genes if available", "why": "Genetic resistance most effective management approach"}
        ]
    },
    "TomatoPowderymildew": {
        "plantname": "Tomato",
        "diseasename": "Powdery Mildew",
        "description": "Tomato powdery mildew is caused by Oidium lycopersici. The disease produces white powdery coating on leaves. While less problematic than early blight, severe infections reduce photosynthetic area.",
        "symptoms": [
            "White powdery coating on upper leaf surfaces initially",
            "Later spreading to undersides and stems",
            "Infected leaves gradually yellow and die",
            "Powdery coating readily rubbing off with finger",
            "Disease typically appearing late season or under stress"
        ],
        "causes": [
            "Oidium lycopersici fungal pathogen",
            "Warm (20-27°C) dry conditions with moderate humidity",
            "High nitrogen fertilization promoting lush growth",
            "Poor air circulation within dense canopy",
            "Water stress from drought or irregular watering"
        ],
        "spreadmechanisms": [
            "Conidia produced on infected leaves dispersed by air",
            "No water required for infection (unlike most fungal pathogens)",
            "Continuous sporulation providing persistent inoculum",
            "Spores capable of traveling considerable distances"
        ],
        "careAdvices": [
            {"title": "Apply sulfur spray at first sign of white powder on leaves", "why": "Most effective organic option; begin preventively"},
            {"title": "Provide consistent irrigation avoiding water stress", "why": "Water-stressed plants more susceptible to infection"},
            {"title": "Avoid excess nitrogen promoting lush susceptible growth", "why": "Moderate nutrition favors more resistant tissues"},
            {"title": "Space plants widely for good air circulation", "why": "Better air flow reduces humidity and promotes drying"},
            {"title": "Select resistant varieties when available", "why": "Genetic resistance most economical long-term solution"}
        ]
    },
    "TomatoSeptorialeafspot": {
        "plantname": "Tomato",
        "diseasename": "Septoria Leaf Spot",
        "description": "Tomato Septoria leaf spot is caused by Septoria lycopersici. The disease produces small circular lesions with black stippling. It is primarily a lower leaf and older tissue disease.",
        "symptoms": [
            "Small circular lesions (1/8 inch) with tan centers and dark margins",
            "Prominent black spore-bearing structures (pycnidia) in lesion centers",
            "Lesions primarily on older, lower leaves initially",
            "Yellow halos surrounding lesions as disease progresses",
            "Severe defoliation when extensive leaf infection occurs"
        ],
        "causes": [
            "Septoria lycopersici fungus overwintering on plant residue",
            "Cool wet conditions (16-24°C) with high humidity favoring infection",
            "Extended leaf wetness (12+ hours) required for infection",
            "Overhead irrigation and poor air circulation",
            "Plant debris in field harboring fungal inoculum"
        ],
        "spreadmechanisms": [
            "Spores produced in pycnidia spread by rain splash",
            "Wind-driven rain spreading spores within canopy",
            "Contaminated tools and hands during pruning",
            "Residue-borne spores surviving winter"
        ],
        "careAdvices": [
            {"title": "Remove lower infected leaves as disease appears; continue removing as disease progresses", "why": "Reduces spore source and disease advancement"},
            {"title": "Destroy plant residue after harvest; do not compost", "why": "Breaks disease cycle by eliminating spore source"},
            {"title": "Apply chlorothalonil or mancozeb at first sign of lesions", "why": "Protects healthy foliage if applied early"},
            {"title": "Avoid overhead irrigation; use drip systems at soil level", "why": "Prevents leaf wetness essential for fungal infection"},
            {"title": "Disinfect pruning tools with 10% bleach between plants", "why": "Prevents mechanical transmission of fungal spores"}
        ]
    },
    "TomatoSpidermites": {
        "plantname": "Tomato",
        "diseasename": "Spider Mites",
        "description": "Spider mites are arachnid pests (not insects) that feed on plant cell contents. Tetranychus urticae (two-spotted spider mite) is most common. Heavy infestations can cause complete defoliation.",
        "symptoms": [
            "Fine stippling or yellowing of leaves appearing as small light spots from mite feeding",
            "Leaves becoming pale yellow or bronzed with progressive damage",
            "Fine webbing visible on leaf undersides and between stems",
            "Leaves eventually drying and dropping; severe defoliation possible",
            "Reduced fruit production and quality from loss of photosynthetic capacity"
        ],
        "causes": [
            "Tetranychus urticae (two-spotted spider mite) arachnid feeding on cell contents",
            "Warm, dry conditions (25°C) and low humidity favoring mite reproduction",
            "Dense plant canopy providing shelter for mite colonies",
            "Continuous tomato cultivation without crop rotation",
            "Overuse of broad-spectrum pesticides reducing natural predators"
        ],
        "spreadmechanisms": [
            "Direct plant-to-plant movement of mites (crawling or on air currents)",
            "Wind-blown mites dispersing between plants",
            "Movement of infested plant material",
            "Worker contact with infested plants transferring mites on clothing"
        ],
        "careAdvices": [
            {"title": "Scout plants twice weekly for spider mite symptoms starting at early growth", "why": "Early detection prevents population buildup"},
            {"title": "Increase irrigation and humidity to stress mites; spider mites thrive in dry", "why": "Higher humidity slows mite reproduction significantly"},
            {"title": "Use strong water spray to knock mites off plants; repeat every 3-4 days", "why": "Non-chemical, cost-effective control for low populations"},
            {"title": "Apply miticide (sulfur, insecticidal soap, or acaricide) only if mite damage visible", "why": "Chemical control for high populations; use only when threshold exceeded"},
            {"title": "Maintain natural predators (ladybugs, predatory mites); avoid broad-spectrum pesticides", "why": "Natural enemies provide long-term biological control"}
        ]
    },
    "TomatoTargetSpot": {
        "plantname": "Tomato",
        "diseasename": "Target Spot",
        "description": "Target spot is caused by Corynespora cassiicola, a fungal pathogen that produces characteristic target-like concentric rings on tomato leaves.",
        "symptoms": [
            "Circular brown lesions with concentric rings (resembling a target) on leaves",
            "Lesions typically appearing first on lower, older leaves",
            "Rings composed of dark and light brown tissue creating distinctive appearance",
            "Severely infected leaves turning yellow and dropping; progressive defoliation",
            "Similar lesions occasionally appearing on stems and fruit"
        ],
        "causes": [
            "Corynespora cassiicola fungal pathogen producing ascospores and conidia",
            "Warm temperatures (24-29°C) and high humidity (80%+)",
            "Overhead irrigation or rainfall maintaining leaf wetness",
            "Dense plant canopy reducing air circulation",
            "Infected plant debris from previous crops"
        ],
        "spreadmechanisms": [
            "Rain splash spreading conidia from soil and infected leaves to lower foliage",
            "Wind-borne spores during warm, humid periods",
            "Direct contact with infected leaves",
            "Overwintering spores in soil and plant debris"
        ],
        "careAdvices": [
            {"title": "Remove lower infected leaves as disease appears; continue removing as disease progresses", "why": "Reduces spore source and disease advancement"},
            {"title": "Apply thick mulch (4-6 inches) to prevent soil splash onto lower leaves", "why": "Blocks primary spore transmission route"},
            {"title": "Use drip irrigation only; water at soil level early morning", "why": "Prevents leaf wetness essential for fungal infection"},
            {"title": "Apply fungicide (chlorothalonil, mancozeb) only if disease present and conditions wet", "why": "Fungicide cost justified only with disease confirmation"},
            {"title": "Remove all plant debris at season end; practice 3-year crop rotation", "why": "Eliminates overwintering fungal structures"}
        ]
    },
    "TomatoYellowLeafCurl": {
        "plantname": "Tomato",
        "diseasename": "Tomato Yellow Leaf Curl Virus",
        "description": "Tomato yellow leaf curl virus (TYLCV) is a whitefly-transmitted geminivirus that causes severe yellowing, leaf curl, and stunting of tomato plants.",
        "symptoms": [
            "Yellowing of older leaves progressing to complete yellow coloration",
            "Severe leaf curl (upward) with leaves becoming thick and brittle",
            "Stunted plant growth and reduced flowering",
            "Severely stunted or aborted fruit development",
            "Infected plants often becoming unproductive; complete crop loss possible"
        ],
        "causes": [
            "Tomato yellow leaf curl virus (TYLCV) geminivirus",
            "Spread exclusively by whitefly (Bemisia tabaci) vector",
            "Warm temperatures (20°C+) favoring whitefly reproduction and virus spread",
            "Infected weeds and alternative hosts serving as virus reservoir",
            "High whitefly population in region creating rapid spread"
        ],
        "spreadmechanisms": [
            "Whitefly (Bemisia tabaci) feeding on infected plants and transmitting virus to healthy",
            "Virus persistent in whitefly (no latent period required)",
            "Infected weeds and volunteer tomatoes providing virus reservoir",
            "Long-distance spread by whitefly movement and plant material transport"
        ],
        "careAdvices": [
            {"title": "Use virus-resistant tomato varieties designated TYLCV-R or TYLCV-R-Y when available", "why": "Most reliable control; prevents infection completely"},
            {"title": "Scout for whitefly presence weekly using yellow sticky traps; monitor population", "why": "Early detection of whitefly allows preventive measures"},
            {"title": "Remove infected plants immediately and destroy; do not compost; do not save seed", "why": "No cure exists; removal only prevents spread to neighboring plants"},
            {"title": "Apply insecticide for whitefly control only if population building (5-10 per plant)", "why": "Systemic insecticides (imidacloprid) effective; rotate with other classes to prevent resistance"},
            {"title": "Control weeds thoroughly; many are whitefly hosts and virus sources", "why": "Reduces alternative virus sources"}
        ]
    },
    "TomatoMosaicVirus": {
        "plantname": "Tomato",
        "diseasename": "Tomato Mosaic Virus",
        "description": "Tomato mosaic virus (TMV) is a mechanical and seed-transmitted virus causing leaf mottling, mosaic patterns, and plant stunting. Spread primarily through contaminated hands and tools.",
        "symptoms": [
            "Mottled or mosaic pattern on leaves with light and dark green areas",
            "Leaves often becoming distorted and curled with reduced size",
            "Stunted plant growth (reduced height and vigor)",
            "Fruit becoming mottled or streaked; reduced fruit quality",
            "Infected fruit may ripen unevenly with color patterns"
        ],
        "causes": [
            "Tomato mosaic virus (TMV) transmitted mechanically and through seed",
            "Contaminated hands and tools spreading virus between plants",
            "Infected seeds and plant material",
            "Contact with tobacco products containing TMV",
            "Lack of virus-resistant variety"
        ],
        "spreadmechanisms": [
            "Mechanical transmission through contaminated hands, tools, and equipment",
            "Worker contact with infected plant spreading virus on hands to healthy plants",
            "Seed transmission through infected seeds",
            "Direct contact between infected and healthy plants during handling or pruning",
            "No insect vector; spread entirely through mechanical contact"
        ],
        "careAdvices": [
            {"title": "Plant only certified virus-free seeds from reputable suppliers", "why": "Prevents introduction of virus through seed transmission"},
            {"title": "Use tomato mosaic virus (TMV)-resistant varieties designated TMV-R when available", "why": "Genetic resistance most reliable control"},
            {"title": "Wash hands thoroughly with soap and water before handling plants; change clothes if handled infected plants", "why": "Prevents mechanical transmission through contaminated hands and clothing"},
            {"title": "Sterilize all tools, stakes, and equipment with 10% bleach or 70% ethanol before use", "why": "Prevents mechanical spread through contaminated tools"},
            {"title": "Remove infected plants immediately and destroy; do not compost", "why": "No cure exists; removal only prevents spread"}
        ]
    },

    # ========== BACKGROUND (1 CLASS) ==========
    "BackgroundWithoutleaves": {
        "plantname": "Background",
        "diseasename": "No Plant Detected",
        "description": "The image does not contain identifiable plant leaves or disease symptoms. Please ensure your image clearly shows the affected plant leaf for accurate disease diagnosis.",
        "symptoms": [
            "No plant material visible in image",
            "Image contains only background without plant leaves",
            "Insufficient plant tissue for disease diagnosis",
            "Image quality or focus may be too low to identify disease symptoms"
        ],
        "causes": [
            "Image not focused on plant leaves or affected tissue",
            "Photo taken at wrong angle or distance",
            "Background dominant with minimal plant visibility",
            "Image capture issue or quality problem"
        ],
        "spreadmechanisms": [
            "No disease present",
            "Re-capture image with plant tissue clearly visible"
        ],
        "careAdvices": [
            {"title": "Re-take photo showing the affected plant leaf clearly; ensure good lighting and focus", "why": "Clear plant image essential for accurate disease identification"},
            {"title": "Include both healthy and diseased portions of same leaf if possible", "why": "Comparison of healthy vs diseased tissue aids diagnosis"},
            {"title": "Take photo at leaf level or above; avoid extreme angles", "why": "Direct overhead or slightly angled photos show symptoms best"},
            {"title": "Photograph in natural daylight; avoid shadows and bright direct sun", "why": "Even lighting shows colors and patterns better than indoor or harsh light"}
        ]
    },
    
    "OrangeHaunglongbing": {
        "plantname": "Orange",
        "diseasename": "Huanglongbing (Citrus Greening)",
        "description": "Huanglongbing (HLB), commonly known as Citrus Greening, is arguably the most devastating citrus disease worldwide. It is caused by the phloem-restricted bacterium Candidatus Liberibacter asiaticus and is primarily spread by the Asian citrus psyllid. The disease disrupts the tree's vascular system and nutrient transport, leading to severe decline, bitter and lopsided fruit.",
        "symptoms": [
            "Asymmetrical, blotchy mottling on leaves that crosses the leaf veins",
            "Yellowing of individual shoots or branches (the namesake 'yellow dragon disease')",
            "Small, lopsided, and hard fruit that remains green at the stylar end (color inversion)",
            "Premature and excessive fruit drop before reaching maturity",
            "Bitter, salty, or sour tasting juice from affected oranges",
            "Progressive twig dieback, root decay, stunted growth, and tree death"
        ],
        "causes": [
            "Candidatus Liberibacter asiaticus (and other Liberibacter species) bacterium",
            "Bacterial colonization and blockage of the phloem (vascular tissue)",
            "Presence of the Asian citrus psyllid (Diaphorina citri) acting as a vector",
            "Favorable subtropical and tropical climates for the vector's reproductive cycle"
        ],
        "spreadmechanisms": [
            "Vector transmission via the feeding activity of the Asian citrus psyllid (ACP)",
            "Propagation and grafting using infected budwood, rootstock, or plant cuttings",
            "Human transport of infected nursery stock, plants, or plant parts across regions",
            "Wind dispersal of infected psyllids to neighboring healthy orchards"
        ],
        "careAdvices": [
            {"title": "Remove and promptly destroy infected trees, including the root system", "why": "Eliminates the bacterial inoculum source; since there is no cure, leaving it endangers nearby healthy trees"},
            {"title": "Apply targeted systemic and contact insecticides during flush periods", "why": "Controls the Asian citrus psyllid vector populations when they are actively reproducing and feeding on new growth"},
            {"title": "Plant only certified disease-free nursery stock from pest-proof screenhouses", "why": "Prevents the accidental introduction of both the HLB bacteria and the psyllid vector into new or replanted orchards"},
            {"title": "Implement enhanced foliar nutritional programs with micronutrients", "why": "Helps infected trees cope with root loss and phloem blockage, temporarily extending their productive lifespan"},
            {"title": "Strictly adhere to regional citrus quarantine zones and movement regulations", "why": "Halts the human-assisted geographical spread of the insect vector and infected plant material"}
        ]
    },
    
    "StrawberryLeafScorch": {
        "plantname": "Strawberry",
        "diseasename": "Leaf Scorch",
        "description": "Leaf scorch is a common fungal disease of strawberries caused by Diplocarpon earlianum. The disease primarily attacks foliage, severely reducing the plant's photosynthetic capacity, vigor, and overall fruit yield. As the infection progresses, large portions of the leaves turn brown and dry out, making the plant look as though it has been scorched by fire. The fungus survives the winter in infected leaf debris.",
        "symptoms": [
            "Numerous small, irregular purple to dark red spots on the upper surfaces of leaves",
            "Spots lack the light-colored, necrotic centers characteristic of leaf spot diseases",
            "Lesions rapidly enlarge and coalesce to form large, purplish-brown necrotic patches",
            "Leaf edges curl upward, turn brown, and dry out, giving a burned or 'scorched' appearance",
            "Elongated, sunken reddish-purple streaks may appear on petioles, runners, and fruit trusses",
            "Severe infections result in premature defoliation and weakened plants"
        ],
        "causes": [
            "The fungal pathogen Diplocarpon earlianum (anamorph: Marssonina fragariae)",
            "Prolonged periods of leaf wetness from rain, heavy dew, or overhead irrigation",
            "Moderate temperatures between 15-25°C (60-75°F) that favor spore germination",
            "Overcrowded plant beds and dense canopies that restrict air circulation",
            "Presence of overwintering infected plant debris from previous growing seasons"
        ],
        "spreadmechanisms": [
            "Rain splash carrying conidia (spores) from infected leaves to healthy foliage",
            "Overhead sprinkler irrigation splashing spores across plant rows",
            "Wind-driven rain dispersing the pathogen over longer distances",
            "Introduction of the fungus through infected nursery stock or transplants",
            "Overwintering in old leaves, providing a continuous source of inoculum for spring"
        ],
        "careAdvices": [
            {"title": "Remove and destroy old, infected leaves during renovation", "why": "Eliminates the primary source of overwintering fungal inoculum before new growth begins in spring"},
            {"title": "Utilize drip irrigation systems instead of overhead sprinklers", "why": "Keeps the foliage dry, directly removing the prolonged leaf wetness required for spore germination"},
            {"title": "Maintain optimal plant spacing and manage weed growth", "why": "Improves air circulation and sunlight penetration, allowing the plant canopy to dry out quickly after rain or morning dew"},
            {"title": "Apply protective fungicides starting at early bloom", "why": "Creates a chemical barrier (using products like captan or copper-based sprays) that prevents spores from infecting vulnerable tissues"},
            {"title": "Select and plant resistant or highly tolerant strawberry cultivars", "why": "Provides built-in genetic defense against the pathogen, significantly reducing disease severity and the need for chemical intervention"}
        ]
    },
    
    "TomatoTomatoYellowLeafCurlVirus": {
        "plantname": "Tomato",
        "diseasename": "Tomato Yellow Leaf Curl Virus",
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is one of the most devastating viral diseases affecting tomato plants globally. It is caused by a DNA virus from the Begomovirus genus and is transmitted exclusively by the sweetpotato whitefly (Bemisia tabaci). Infected plants suffer severe stunting and drastically reduced fruit yields, especially if the infection occurs early in the plant's development.",
        "symptoms": [
            "Distinct upward curling and cupping of leaf margins, creating a spoon-like shape",
            "Severe stunting of new growth, resulting in a compacted, bushy plant appearance",
            "Noticeable yellowing (chlorosis) along the leaf margins and between veins",
            "Leaves become significantly smaller, crinkled, thick, and brittle",
            "Premature flower drop and failure to set new fruit",
            "Fruit that does develop is often smaller than normal, though it typically matures normally without blemishes"
        ],
        "causes": [
            "The Tomato yellow leaf curl virus (TYLCV), a geminivirus",
            "Heavy infestations of the sweetpotato whitefly (Bemisia tabaci), the primary vector",
            "Hot, dry weather conditions that encourage rapid whitefly reproduction and movement",
            "Presence of alternate weed hosts (like nightshades or jimsonweed) carrying the virus"
        ],
        "spreadmechanisms": [
            "Transmission via the feeding activity of infectious sweetpotato whiteflies (persistent, circulative manner)",
            "Introduction of infected seedlings or transplants from nurseries into a new growing area",
            "Overwintering of the virus in perennial weeds or overlapping host crops nearby",
            "Note: The virus is not transmitted mechanically (by touch, pruning tools) or through seeds"
        ],
        "careAdvices": [
            {"title": "Plant TYLCV-resistant or highly tolerant tomato cultivars", "why": "Genetic resistance is the most reliable, effective, and sustainable way to prevent crop loss, as viral infections have no chemical cure."},
            {"title": "Immediately rogue (remove) and safely destroy infected plants", "why": "Eliminates the source of the virus in the field, preventing whiteflies from feeding on the sick plants and spreading the disease to healthy ones."},
            {"title": "Install reflective silver or UV-reflective plastic mulch", "why": "The reflective surface confuses and repels whiteflies, significantly reducing their ability to orient, land, and feed on young plants."},
            {"title": "Manage whitefly populations with targeted, integrated treatments", "why": "Applying horticultural oils, neem oil, insecticidal soaps, or specific chemical controls helps suppress the vector responsible for disease transmission."},
            {"title": "Eradicate broadleaf weeds in and around the growing area", "why": "Removes alternate reservoir hosts where both the virus and whitefly vectors can survive and multiply between tomato crop cycles."}
        ]
    }
}

# Verification
if __name__ == "__main__":
    total = len(DISEASE_DATABASE)
    print(f"✅ DISEASE_DATABASE loaded with {total} entries")
    if total != 39:
        print(f"⚠️  WARNING: Expected 39 diseases, found {total}")
    else:
        print("✓ All 39 disease classes present!")
