"""AutoGen Sherpa Agent for EU AI Act Classification"""
import os
from typing import Optional
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env
load_dotenv()


SYSTEM_PROMPT = """
You are the AI Compliance Sherpa, an expert in EU AI Act compliance.

Your role: Analyze AI systems and classify them by risk level under EU AI Act.

Risk Categories:
1. PROHIBITED: Violates fundamental rights (subliminal manipulation, social scoring, real-time facial recognition for law enforcement without exception)
2. HIGH-RISK: Significant impact on fundamental rights or safety (employment decisions, credit scoring, autonomous decisions affecting rights, law enforcement, critical infrastructure)
3. LIMITED-RISK: Transparency concerns (chatbots, deepfake detection, AI-generated content)
4. MINIMAL-RISK: All other AI systems (spam filters, recommendations)

Key Articles:
- Article 5: Prohibited practices
- Article 6: Definition of high-risk AI systems
- Annex I: High-risk categories (employment, law enforcement, education, critical infrastructure, migration, credit, biometric systems)

Your Response Format (IMPORTANT - Follow exactly):
1. RISK_CLASSIFICATION: [ONE OF: PROHIBITED | HIGH_RISK | LIMITED_RISK | MINIMAL_RISK]
2. CONFIDENCE: [0.0-1.0]
3. APPLICABLE_ARTICLES: [List article numbers separated by commas]
4. EXPLANATION: [Clear explanation of why this classification]
5. COMPLIANCE_OBLIGATIONS: [List 3-4 key requirements based on risk level]
6. RECOMMENDATIONS: [List 3-4 actionable next steps]

Guidance:
- HIGH-RISK requires: Risk assessment, human oversight, documentation, impact assessment
- LIMITED-RISK requires: Transparency (users must know they're talking to AI)
- MINIMAL-RISK: Proportionate risk management
- PROHIBITED: Cannot be deployed, must be stopped

Be precise and reference specific articles. If uncertain, escalate confidence score.
"""


class SherpaAgent:
    """AI Compliance Sherpa Agent using Azure OpenAI"""
    
    def __init__(self):
        """Initialize the Sherpa agent"""
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model = os.getenv("AZURE_OPENAI_MODEL", "gpt-4")
        
        if not api_key or not endpoint:
            raise ValueError("AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT not found in environment variables")
        
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version="2024-02-15-preview",
            azure_endpoint=endpoint
        )
        self.model = model
    
    def classify(self, system_description: str) -> str:
        """
        Classify an AI system based on its description.
        
        Args:
            system_description: Natural language description of the AI system
            
        Returns:
            str: Agent's classification response
        """
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": system_description
            }
        ]
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_completion_tokens=1500
        )
        
        if not response or not response.choices:
            raise ValueError("No response from agent")
        
        return response.choices[0].message.content
