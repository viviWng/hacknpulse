"""
Risk Classification Logic - Updated to use Rule Engine (Layer 2)

This module provides the deterministic classification logic using the Rule Engine
instead of hardcoded Python logic. Classification is reproducible and auditable.

ARCHITECTURE PRINCIPLE:
  - Deterministic classification via rule_engine.py
  - LLM explanation only (not used for classification)
  - Legal corpus grounding via legal_corpus_loader.py
  - Full versioning and audit trail
"""

from src.schemas import Questionnaire, ClassificationResult, ApplicableArticle
from src.compliance.rule_engine import get_rule_engine, RuleEngine
from src.legal.legal_corpus_loader import get_legal_corpus_loader, LegalCorpusLoader
from datetime import datetime
import hashlib
import json
from typing import Optional, Tuple, List


def classify_system(questionnaire: Questionnaire, agent_explanation: str) -> ClassificationResult:
    """
    Classify an AI system based on questionnaire and rule engine.
    
    ARCHITECTURE:
      1. Rule engine performs DETERMINISTIC classification (reproducible)
      2. Legal corpus loader provides LEGAL GROUNDING (authoritative)
      3. Agent explanation is SUPPLEMENTARY only (not binding)
      4. Result includes VERSION INFORMATION (auditable)
    
    Args:
        questionnaire: User questionnaire responses
        agent_explanation: Agent's classification explanation (supplementary)
        
    Returns:
        ClassificationResult with version information and audit trail
    """
    
    # Initialize engines
    rule_engine: RuleEngine = get_rule_engine()
    legal_corpus: LegalCorpusLoader = get_legal_corpus_loader()
    
    # Convert questionnaire to dict for rule engine
    questionnaire_dict = questionnaire.dict(exclude_none=True)
    
    # STEP 1: Apply rule engine for DETERMINISTIC classification
    risk_level, articles, confidence = rule_engine.classify(questionnaire_dict)
    
    # STEP 2: Get requirements from rule engine
    requirements = rule_engine.get_applicable_requirements(risk_level, articles)
    obligations = requirements.get("compliance_obligations", [])
    
    # STEP 3: Parse agent response for recommendations
    recommendations = parse_agent_recommendations(agent_explanation)
    
    # STEP 4: Build applicable articles list with legal grounding
    applicable_articles = []
    for article_num in articles:
        article_summary = legal_corpus.get_article_summary(article_num)
        applicable_articles.append(
            ApplicableArticle(
                article_number=article_num,
                article_title=article_summary.get("title", f"Article {article_num}"),
                is_violated=False,
                explanation=article_summary.get("description", f"Article {article_num} applies to this system")
            )
        )
    
    # STEP 5: Generate audit hash
    questionnaire_hash = _generate_questionnaire_hash(questionnaire_dict)
    
    # STEP 6: Get version information
    regulation_version_info = legal_corpus.get_version_info()
    rule_version_info = rule_engine.get_rule_version_info()
    
    # STEP 7: Build classification result with VERSIONING
    return ClassificationResult(
        system_name=questionnaire.name,
        risk_classification=risk_level,
        confidence_score=confidence,
        applicable_articles=applicable_articles,
        compliance_obligations=obligations,
        recommendations=recommendations,
        explanation=agent_explanation,
        # VERSIONING (SDD Requirement)
        regulation_version=regulation_version_info.get("regulation"),
        regulation_date=regulation_version_info.get("version_date"),
        rule_version=rule_version_info.get("rules_version"),
        rule_version_date=rule_version_info.get("rules_last_updated"),
        classification_timestamp=datetime.now().isoformat(),
        questionnaire_hash=questionnaire_hash
    )


def apply_decision_tree(questionnaire: Questionnaire) -> tuple:
    """
    DEPRECATED: Use rule_engine.classify() instead.
    
    This function is kept for backward compatibility but delegates to the rule engine.
    """
    rule_engine = get_rule_engine()
    questionnaire_dict = questionnaire.dict(exclude_none=True)
    return rule_engine.classify(questionnaire_dict)


def get_article_title(article_num: int) -> str:
    """
    Get article title by number (using legal corpus)
    
    Args:
        article_num: Article number
        
    Returns:
        Article title
    """
    legal_corpus = get_legal_corpus_loader()
    summary = legal_corpus.get_article_summary(article_num)
    return summary.get("title", f"Article {article_num}")


def parse_agent_recommendations(response: str) -> List[str]:
    """
    Parse agent response to extract recommendations.
    
    NOTE: Agent response is supplementary only.
    The classification decision comes from the rule engine, not the agent.
    
    Args:
        response: Agent's explanation text
        
    Returns:
        List of recommendations
    """
    
    recommendations = []
    
    if not response:
        return [
            "Consult with your legal and compliance team",
            "Document design and implementation decisions",
            "Conduct a risk assessment before deployment"
        ]
    
    # Extract from agent response
    lines = response.split('\n')
    in_recommendations = False
    
    for line in lines:
        line = line.strip()
        
        if "RECOMMENDATIONS" in line.upper():
            in_recommendations = True
            continue
        elif ":" in line and any(keyword in line.upper() 
             for keyword in ["RISK_CLASSIFICATION", "CONFIDENCE", "ARTICLES", "OBLIGATIONS"]):
            in_recommendations = False
            continue
        
        if line and in_recommendations and len(recommendations) < 5:
            # Clean up bullet points
            clean = line.lstrip("- •*0123456789.)")
            if clean and len(clean) > 10:  # Only include substantial recommendations
                recommendations.append(clean)
    
    # Ensure we have some defaults
    if not recommendations:
        recommendations = [
            "Consult with your legal and compliance team",
            "Document design and implementation decisions",
            "Conduct a risk assessment before deployment"
        ]
    
    return recommendations[:5]  # Limit to 5 recommendations


def _generate_questionnaire_hash(questionnaire_dict: dict) -> str:
    """
    Generate hash of questionnaire for audit trail
    
    Args:
        questionnaire_dict: Questionnaire as dictionary
        
    Returns:
        SHA256 hash of questionnaire
    """
    questionnaire_json = json.dumps(questionnaire_dict, sort_keys=True)
    questionnaire_hash = hashlib.sha256(questionnaire_json.encode()).hexdigest()
    return questionnaire_hash[:16]  # Return first 16 chars


def log_classification_audit(questionnaire: Questionnaire, result: ClassificationResult) -> dict:
    """
    Create audit log entry for classification
    
    This is OPTIONAL but recommended for compliance tracking.
    
    Args:
        questionnaire: Original questionnaire
        result: Classification result
        
    Returns:
        Audit log entry dictionary
    """
    legal_corpus = get_legal_corpus_loader()
    
    audit_entry = {
        "timestamp": result.classification_timestamp,
        "system_name": result.system_name,
        "risk_classification": result.risk_classification,
        "applicable_articles": result.applicable_articles,
        "regulation_version": result.regulation_version,
        "regulation_date": result.regulation_date,
        "rule_version": result.rule_version,
        "rule_version_date": result.rule_version_date,
        "questionnaire_hash": result.questionnaire_hash,
        "confidence_score": result.confidence_score
    }
    
    return audit_entry


# LEGACY FUNCTIONS (Kept for backward compatibility, use rule engine instead)

def is_prohibited(questionnaire: Questionnaire) -> bool:
    """DEPRECATED: Use rule_engine.classify() instead"""
    rule_engine = get_rule_engine()
    questionnaire_dict = questionnaire.dict(exclude_none=True)
    risk_level, _, _ = rule_engine.classify(questionnaire_dict)
    return risk_level == "PROHIBITED"


def is_high_risk(questionnaire: Questionnaire) -> bool:
    """DEPRECATED: Use rule_engine.classify() instead"""
    rule_engine = get_rule_engine()
    questionnaire_dict = questionnaire.dict(exclude_none=True)
    risk_level, _, _ = rule_engine.classify(questionnaire_dict)
    return risk_level == "HIGH_RISK"


def is_limited_risk(questionnaire: Questionnaire) -> bool:
    """DEPRECATED: Use rule_engine.classify() instead"""
    rule_engine = get_rule_engine()
    questionnaire_dict = questionnaire.dict(exclude_none=True)
    risk_level, _, _ = rule_engine.classify(questionnaire_dict)
    return risk_level == "LIMITED_RISK"
