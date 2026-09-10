import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
from app.config import settings
import logging


logger = logging.getLogger(__name__)


HTML_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeafScan Disease Report</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 650px;
            margin: 0 auto;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
            border-radius: 12px;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #2d6a4f 0%, #40916c 100%);
            color: #ffffff;
            padding: 40px 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 32px;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        .header p {
            margin: 8px 0 0 0;
            font-size: 14px;
            opacity: 0.95;
        }
        .content {
            padding: 40px 30px;
        }
        .section {
            margin-bottom: 30px;
        }
        .section-title {
            font-size: 18px;
            font-weight: 600;
            color: #2d6a4f;
            margin: 0 0 16px 0;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .detection-box {
            background-color: #f0f8f5;
            border-left: 4px solid #2d6a4f;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 24px;
        }
        .detection-row {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #e0e0e0;
        }
        .detection-row:last-child {
            border-bottom: none;
        }
        .detection-label {
            font-weight: 600;
            color: #2d6a4f;
            font-size: 14px;
        }
        .detection-value {
            color: #333;
            font-size: 14px;
            font-weight: 500;
        }
        .severity-badge {
            display: inline-block;
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .severity-none {
            background-color: #d4edda;
            color: #155724;
        }
        .severity-mild {
            background-color: #d4edda;
            color: #155724;
        }
        .severity-moderate {
            background-color: #fff3cd;
            color: #856404;
        }
        .severity-severe {
            background-color: #f8d7da;
            color: #721c24;
        }
        .disease-description {
            background-color: #f8f9fa;
            padding: 18px;
            border-radius: 6px;
            font-size: 14px;
            line-height: 1.7;
            color: #444;
            margin-bottom: 20px;
        }
        .symptoms-list, .causes-list {
            background-color: #fafafa;
            padding: 16px;
            border-radius: 6px;
            margin-bottom: 16px;
        }
        .symptoms-list ul, .causes-list ul {
            margin: 0;
            padding-left: 20px;
            list-style: none;
        }
        .symptoms-list li, .causes-list li {
            padding: 6px 0;
            font-size: 13px;
            color: #555;
            position: relative;
            padding-left: 20px;
        }
        .symptoms-list li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #2d6a4f;
            font-weight: bold;
        }
        .causes-list li:before {
            content: "•";
            position: absolute;
            left: 3px;
            color: #40916c;
            font-weight: bold;
        }
        .care-advice-section {
            background-color: #f0f8f5;
            border-left: 4px solid #40916c;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 20px;
        }
        .advice-item {
            background-color: #ffffff;
            padding: 16px;
            margin-bottom: 12px;
            border-radius: 6px;
            border-left: 3px solid #40916c;
        }
        .advice-item:last-child {
            margin-bottom: 0;
        }
        .advice-title {
            font-weight: 600;
            color: #2d6a4f;
            font-size: 14px;
            margin: 0 0 6px 0;
        }
        .advice-reason {
            font-size: 13px;
            color: #666;
            margin: 0;
            font-style: italic;
            line-height: 1.5;
        }
        .tip-box {
            background-color: #fff8e1;
            border-left: 4px solid #ffc107;
            padding: 16px;
            border-radius: 6px;
            margin-bottom: 24px;
        }
        .tip-box p {
            margin: 0;
            font-size: 13px;
            color: #856404;
            line-height: 1.6;
        }
        .tip-icon {
            font-size: 18px;
            margin-right: 8px;
        }
        .footer {
            background-color: #f8f9fa;
            padding: 24px 30px;
            text-align: center;
            border-top: 1px solid #e0e0e0;
        }
        .footer p {
            margin: 4px 0;
            font-size: 12px;
            color: #999;
        }
        .footer-brand {
            font-weight: 600;
            color: #2d6a4f;
            font-size: 13px;
        }
        .confidence-bar {
            width: 100%;
            height: 8px;
            background-color: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }
        .confidence-fill {
            height: 100%;
            background-color: #40916c;
            transition: width 0.3s ease;
        }
        @media (max-width: 600px) {
            .container {
                border-radius: 0;
            }
            .content {
                padding: 24px 16px;
            }
            .header {
                padding: 30px 16px;
            }
            .header h1 {
                font-size: 24px;
            }
            .detection-row {
                flex-direction: column;
            }
            .detection-value {
                margin-top: 4px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>🌿 LeafScan Disease Report</h1>
            <p>AI-Powered Plant Disease Detection & Care Guidance</p>
        </div>

        <!-- Main Content -->
        <div class="content">
            <!-- Detection Results -->
            <div class="section">
                <div class="section-title">📊 Detection Results</div>
                <div class="detection-box">
                    <div class="detection-row">
                        <span class="detection-label">Plant Type</span>
                        <span class="detection-value">{{ plant_type }}</span>
                    </div>
                    <div class="detection-row">
                        <span class="detection-label">Disease Detected</span>
                        <span class="detection-value">{{ disease_name }}</span>
                    </div>
                    <div class="detection-row">
                        <span class="detection-label">Detection Confidence</span>
                        <span class="detection-value">{{ confidence }}%</span>
                    </div>
                    <div style="margin-top: 8px;">
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {{ confidence }}%"></div>
                        </div>
                    </div>
                    <div class="detection-row" style="border-bottom: none; margin-top: 12px;">
                        <span class="detection-label">Severity Level</span>
                        <span class="severity-badge severity-{{ severity }}">{{ severity }}</span>
                    </div>
                </div>
            </div>

            <!-- Disease Description -->
            {% if description %}
            <div class="section">
                <div class="section-title">📖 Disease Overview</div>
                <div class="disease-description">{{ description }}</div>
            </div>
            {% endif %}

            <!-- Symptoms -->
            {% if symptoms and symptoms|length > 0 %}
            <div class="section">
                <div class="section-title">🔍 Symptoms</div>
                <div class="symptoms-list">
                    <ul>
                        {% for symptom in symptoms %}
                        <li>{{ symptom }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            {% endif %}

            <!-- Causes -->
            {% if causes and causes|length > 0 %}
            <div class="section">
                <div class="section-title">⚠️ Causes</div>
                <div class="causes-list">
                    <ul>
                        {% for cause in causes %}
                        <li>{{ cause }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            {% endif %}

            <!-- Care & Treatment Advice -->
            {% if care_advices and care_advices|length > 0 %}
            <div class="section">
                <div class="section-title">💊 Care & Treatment Advice</div>
                <div class="care-advice-section">
                    {% for advice in care_advices %}
                    <div class="advice-item">
                        <p class="advice-title">{{ advice.title }}</p>
                        <p class="advice-reason">Why: {{ advice.why }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endif %}

            <!-- Tip Box -->
            <div class="tip-box">
                <p>
                    <span class="tip-icon">💡</span>
                    <strong>Pro Tip:</strong> Monitor your plant closely and follow the recommended care steps. Early intervention is key to preventing disease spread. If symptoms persist after two weeks, consult a local agricultural expert.
                </p>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p class="footer-brand">LeafScan - AI-Powered Plant Disease Detection</p>
            <p>Helping farmers and gardeners protect their crops with precision disease identification</p>
        </div>
    </div>
</body>
</html>
"""


async def send_prediction_email(
    to_email: str,
    disease_name: str,
    confidence: float,
    plant_type: str,
    severity: str = "moderate",
    disease_data: dict = None
):
    subject = f"🌿 LeafScan: {disease_name} Detected in Your {plant_type}"
    template = Template(HTML_EMAIL_TEMPLATE)
    
    conf_pct = round(confidence * 100, 1) if confidence <= 1 else round(confidence, 1)
    
    if disease_data and isinstance(disease_data, dict):
        description = disease_data.get("description", "")
        symptoms = disease_data.get("symptoms", [])
        causes = disease_data.get("causes", [])
        care_advices = disease_data.get("care_advices", [])
        
        if isinstance(symptoms, str):
            symptoms = [s.strip() for s in symptoms.split(",") if s.strip()]
        if isinstance(causes, str):
            causes = [c.strip() for c in causes.split(",") if c.strip()]
        if not isinstance(care_advices, list):
            care_advices = []    
    else:
        description = ""
        symptoms = []
        causes = []
        care_advices = []
    
    html_content = template.render(
        plant_type=plant_type,
        disease_name=disease_name,
        confidence=conf_pct,
        severity=severity.lower(),
        description=description,
        symptoms=symptoms,
        causes=causes,
        care_advices=care_advices
    )
    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f"{settings.EMAIL_FROM_NAME} <{settings.EMAIL_FROM}>"
    message["To"] = to_email
    
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)
    
    try:
        async with aiosmtplib.SMTP(hostname=settings.SMTP_HOST, port=settings.SMTP_PORT) as smtp:
            await smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            await smtp.sendmail(settings.EMAIL_FROM, to_email, message.as_string())
    except Exception as e:
        logger.error(f"Email failed: {e}", exc_info=True)
