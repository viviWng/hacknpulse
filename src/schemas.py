"""Pydantic schemas for questionnaire and classification output"""
from pydantic import BaseModel, Field
from typing import Optional, List


class Questionnaire(BaseModel):
    """AI System Questionnaire Input - Supports both simple and detailed formats"""
    
    name: str = Field(..., description="Name of the AI system")
    purpose: str = Field(..., description="Purpose and use case of the system")
    data_types: str = Field(..., description="Types of data processed")
    autonomous: bool = Field(..., description="Does it make autonomous decisions?")
    affects_rights: bool = Field(..., description="Does it affect fundamental rights?")
    use_case: str = Field(..., description="Use case category")
    
    # MANDATORY EU AI Act Questions - Required for all systems
    # Focused on: Employment, Finance, Critical Infrastructure, General Fairness
    q5_recruitment_selection: Optional[bool] = Field(None, description="[MANDATORY] Q5: Does the system make recruitment or selection decisions?")
    q6_employment_conditions: Optional[bool] = Field(None, description="[MANDATORY] Q6: Does the system evaluate employment conditions, tasks, or performance?")
    q7_biometric_identification: Optional[bool] = Field(None, description="[MANDATORY] Q7: Does the system perform biometric identification?")
    q8_categorization_sensitive: Optional[bool] = Field(None, description="[MANDATORY] Q8: Does the system categorize individuals based on sensitive attributes (race, gender, disability)?")
    q9_critical_infrastructure: Optional[bool] = Field(None, description="[MANDATORY] Q9: Is this system a critical infrastructure component?")
    q10_credit_scoring: Optional[bool] = Field(None, description="[MANDATORY] Q10: Does the system assess credit scoring or creditworthiness?")
    
    # Additional details (optional)
    is_education_system: Optional[bool] = Field(None, description="Does the system operate in education/training sector?")
    additional_notes: Optional[str] = Field(None, description="Additional context about the system")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Resume Screening System",
                "purpose": "Filter job candidates based on qualifications",
                "data_types": "Names, education, work history",
                "autonomous": True,
                "affects_rights": True,
                "use_case": "Employment",
                "q5_recruitment_selection": True,
                "q8_categorization_sensitive": False
            }
        }


class ApplicableArticle(BaseModel):
    """Article that applies to the system"""
    
    article_number: int
    article_title: str
    is_violated: bool
    explanation: str


class ComplianceObligation(BaseModel):
    """What the system must do"""
    
    requirement: str
    affected: bool
    action: str


class ClassificationResult(BaseModel):
    """Classification output with regulatory traceability"""
    
    system_name: str
    risk_classification: str  # PROHIBITED, HIGH_RISK, LIMITED_RISK, MINIMAL_RISK
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    applicable_articles: List[ApplicableArticle]
    compliance_obligations: List[str]
    recommendations: List[str]
    explanation: str
    
    # VERSIONING & AUDITABILITY (SDD Requirement)
    regulation_version: Optional[str] = Field(None, description="EU AI Act regulation version (e.g., 'EU 2024/1689')")
    regulation_date: Optional[str] = Field(None, description="Regulation effective date")
    rule_version: Optional[str] = Field(None, description="Rule engine version used for classification")
    rule_version_date: Optional[str] = Field(None, description="Rule version date")
    classification_timestamp: Optional[str] = Field(None, description="When classification was performed")
    questionnaire_hash: Optional[str] = Field(None, description="Hash of questionnaire input for audit trail")
    
    class Config:
        json_schema_extra = {
            "example": {
                "system_name": "Resume Screening System",
                "risk_classification": "HIGH_RISK",
                "confidence_score": 0.92,
                "applicable_articles": [
                    {
                        "article_number": 6,
                        "article_title": "High-Risk AI Systems",
                        "is_violated": False,
                        "explanation": "System qualifies as high-risk due to employment decisions affecting fundamental rights"
                    }
                ],
                "compliance_obligations": [
                    "Conduct risk assessment",
                    "Implement human oversight",
                    "Maintain documentation"
                ],
                "recommendations": [
                    "Have HR manager review flagged candidates",
                    "Document training data sources",
                    "Test for bias before deployment"
                ],
                "explanation": "This is a HIGH-RISK system because it makes autonomous employment decisions that affect fundamental rights (right to work)."
            }
        }
