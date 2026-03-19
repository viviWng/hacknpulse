"""Output formatting for classification results"""
from src.schemas import ClassificationResult
from datetime import datetime


def format_markdown_report(result: ClassificationResult) -> str:
    """
    Format classification result as a markdown report.
    
    Args:
        result: ClassificationResult object
        
    Returns:
        str: Formatted markdown report
    """
    
    # Color coding by risk level
    risk_emoji = {
        "PROHIBITED": "🚫",
        "HIGH_RISK": "⚠️",
        "LIMITED_RISK": "ℹ️",
        "MINIMAL_RISK": "✅"
    }
    
    emoji = risk_emoji.get(result.risk_classification, "❓")
    
    report = f"""# AI Compliance Assessment Report

**System**: {result.system_name}  
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Assessment ID**: {hash(result.system_name) % 100000}

---

## Risk Classification

{emoji} **{result.risk_classification}**

**Confidence Score**: {result.confidence_score:.0%}

---

## Executive Summary

{result.explanation}

---

## Applicable EU AI Act Articles

"""
    
    for article in result.applicable_articles:
        report += f"\n### Article {article.article_number}: {article.article_title}\n"
        report += f"{article.explanation}\n"
    
    report += f"""
---

## Compliance Obligations

Your system must comply with the following requirements:

"""
    
    for i, obligation in enumerate(result.compliance_obligations, 1):
        report += f"{i}. {obligation}\n"
    
    report += f"""
---

## Recommended Actions

To ensure compliance, we recommend:

"""
    
    for i, rec in enumerate(result.recommendations, 1):
        report += f"{i}. {rec}\n"
    
    report += f"""
---

## Next Steps

1. Review this assessment with your legal and compliance team
2. If classified as HIGH-RISK, conduct a formal risk assessment
3. Document all design and implementation decisions
4. Plan necessary compliance measures based on classification
5. Implement human oversight if required

---

**Disclaimer**: This assessment is based on information provided and EU AI Act requirements. 
For final compliance determinations, consult your organization's legal team.

"""
    
    return report


def format_json_response(result: ClassificationResult) -> dict:
    """
    Format classification result as JSON.
    
    Args:
        result: ClassificationResult object
        
    Returns:
        dict: JSON-serializable result
    """
    
    return {
        "status": "success",
        "data": {
            "system_name": result.system_name,
            "risk_classification": result.risk_classification,
            "confidence_score": result.confidence_score,
            "applicable_articles": [
                {
                    "article_number": a.article_number,
                    "article_title": a.article_title,
                    "is_violated": a.is_violated,
                    "explanation": a.explanation
                }
                for a in result.applicable_articles
            ],
            "compliance_obligations": result.compliance_obligations,
            "recommendations": result.recommendations,
            "explanation": result.explanation
        }
    }


def format_summary(result: ClassificationResult) -> str:
    """
    Format a one-line summary for quick reference.
    
    Args:
        result: ClassificationResult object
        
    Returns:
        str: One-line summary
    """
    
    emoji_map = {
        "PROHIBITED": "🚫",
        "HIGH_RISK": "⚠️",
        "LIMITED_RISK": "ℹ️",
        "MINIMAL_RISK": "✅"
    }
    
    emoji = emoji_map.get(result.risk_classification, "❓")
    
    return f"{emoji} {result.system_name}: {result.risk_classification} (Confidence: {result.confidence_score:.0%})"
