"""FastAPI application for AI Compliance Sherpa"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging
from src.schemas import Questionnaire, ClassificationResult
from src.sherpa.agent import SherpaAgent
from src.classification import classify_system
from src.output import format_json_response, format_markdown_report

# Load environment variables from .env
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Compliance Sherpa",
    description="Classify AI systems by EU AI Act risk level",
    version="0.1.0"
)

# Allow CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent
try:
    agent = SherpaAgent()
    logger.info("✅ Sherpa Agent initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Sherpa Agent: {e}")
    logger.error("Ensure AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT are configured in .env")
    agent = None


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AI Compliance Sherpa API",
        "endpoints": {
            "classify": "/classify",
            "health": "/health"
        }
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "agent_initialized": agent is not None
    }


@app.post("/classify", response_model=dict)
async def classify_ai_system(questionnaire: Questionnaire):
    """
    Classify an AI system by EU AI Act risk level.
    
    Args:
        questionnaire: AI system questionnaire
        
    Returns:
        dict: Classification result with explanation and obligations
    """
    
    try:
        if not agent:
            raise HTTPException(
                status_code=500,
                detail="Agent not initialized. Check AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT in .env"
            )
        
        # Build system description from questionnaire
        system_description = f"""
Please classify this AI system under the EU AI Act:

System Name: {questionnaire.name}
Purpose: {questionnaire.purpose}
Data Types: {questionnaire.data_types}
Makes autonomous decisions: {questionnaire.autonomous}
Affects fundamental rights: {questionnaire.affects_rights}
Use Case: {questionnaire.use_case}

Analyze this system and provide:
1. RISK_CLASSIFICATION
2. CONFIDENCE score
3. APPLICABLE_ARTICLES 
4. EXPLANATION
5. COMPLIANCE_OBLIGATIONS
6. RECOMMENDATIONS
"""
        
        logger.info(f"Classifying system: {questionnaire.name}")
        
        # Get agent classification
        agent_response = agent.classify(system_description)
        logger.info(f"Agent response: {agent_response[:100]}...")
        
        # Build classification result
        result = classify_system(questionnaire, agent_response)
        
        logger.info(f"Classification result: {result.risk_classification}")
        
        # Return JSON formatted response
        return format_json_response(result)
        
    except Exception as e:
        logger.error(f"Classification error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Classification failed: {str(e)}"
        )


@app.post("/report")
async def generate_report(questionnaire: Questionnaire):
    """
    Generate a markdown report for a system classification.
    
    Args:
        questionnaire: AI system questionnaire
        
    Returns:
        str: Markdown formatted report
    """
    
    try:
        if not agent:
            raise HTTPException(
                status_code=500,
                detail="Agent not initialized"
            )
        
        system_description = f"""
Please classify this AI system under the EU AI Act:

System Name: {questionnaire.name}
Purpose: {questionnaire.purpose}
Data Types: {questionnaire.data_types}
Makes autonomous decisions: {questionnaire.autonomous}
Affects fundamental rights: {questionnaire.affects_rights}
Use Case: {questionnaire.use_case}
"""
        
        # Get classification
        agent_response = agent.classify(system_description)
        result = classify_system(questionnaire, agent_response)
        
        # Return markdown report
        return {
            "status": "success",
            "report": format_markdown_report(result)
        }
        
    except Exception as e:
        logger.error(f"Report generation error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Report generation failed: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
