"""
EU AI Act Compliance Report Generator
Generates detailed compliance assessment in structured table format
Maps questionnaire responses to specific EU AI Act categories and obligations
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum


class ComplianceStatus(str, Enum):
    """Compliance status indicators"""
    PROHIBITED = "PROHIBITED"  # Violates EU AI Act Article 5
    HIGH_RISK = "HIGH_RISK"    # Fails to meet Annex I high-risk requirements
    LIMITED_RISK = "LIMITED_RISK"  # Some compliance concerns
    COMPLIANT = "COMPLIANT"    # Meets applicable requirements
    NOT_APPLICABLE = "NOT_APPLICABLE"  # Category doesn't apply to this system


@dataclass
class ComplianceCriterion:
    """Single compliance assessment criterion"""
    criterion: str
    category: str  # EU AI Act section (e.g., "Article 5", "Annex I", "General")
    status: ComplianceStatus
    explanation: str
    applicable: bool  # True if this criterion applies to the system
    risk_level: Optional[str] = None  # PROHIBITED, HIGH_RISK, LIMITED_RISK, MINIMAL_RISK
    applicable_articles: List[int] = None  # Article numbers that apply


class ComplianceReportGenerator:
    """Generates structured compliance reports based on EU AI Act criteria"""
    
    @staticmethod
    def _normalize_response(response):
        """
        Convert response to boolean value
        Handles both simple boolean and detailed object responses
        """
        if response is None:
            return None
        if isinstance(response, bool):
            return response
        if isinstance(response, dict):
            answer = response.get('answer')
            if answer in ['yes', 'Yes', True]:
                return True
            elif answer in ['no', 'No', False]:
                return False
            elif answer in ['potential', 'Potential']:
                return 'potential'
        if isinstance(response, str):
            if response.lower() in ['yes']:
                return True
            elif response.lower() in ['no']:
                return False
            elif response.lower() in ['potential']:
                return 'potential'
        return response
    
    @staticmethod
    def generate_criteria_table(questionnaire_data: dict) -> List[ComplianceCriterion]:
        """
        Generate compliance criteria assessment table based on questionnaire responses
        
        Returns a list of ComplianceCriterion objects representing the assessment matrix
        """
        criteria = []
        
        # Extract and normalize key responses
        q5_recruitment = ComplianceReportGenerator._normalize_response(questionnaire_data.get('q5_recruitment_selection'))
        q6_employment = ComplianceReportGenerator._normalize_response(questionnaire_data.get('q6_employment_conditions'))
        q7_biometric = ComplianceReportGenerator._normalize_response(questionnaire_data.get('q7_biometric_identification'))
        q8_sensitive = ComplianceReportGenerator._normalize_response(questionnaire_data.get('q8_categorization_sensitive'))
        q9_infrastructure = ComplianceReportGenerator._normalize_response(questionnaire_data.get('q9_critical_infrastructure'))
        q10_credit = ComplianceReportGenerator._normalize_response(questionnaire_data.get('q10_credit_scoring'))
        
        # ============ ARTICLE 5: PROHIBITED AI SYSTEMS ============
        
        # Biometric Identification - Real-time remote
        status = ComplianceStatus.PROHIBITED if q7_biometric == "Yes - real-time remote biometric identification (face, iris, fingerprint live matching)" else ComplianceStatus.COMPLIANT
        criteria.append(ComplianceCriterion(
            criterion="Remote biometric identification systems (real-time, at distance)",
            category="Article 5 - Prohibited AI",
            status=status,
            explanation="Real-time remote biometric identification is prohibited under Article 5, except for narrow law enforcement exceptions" if status == ComplianceStatus.PROHIBITED else "System does not utilize real-time remote biometric identification",
            applicable=(q7_biometric is not None and "real-time" in str(q7_biometric).lower()),
            risk_level="PROHIBITED" if status == ComplianceStatus.PROHIBITED else None,
            applicable_articles=[5] if status == ComplianceStatus.PROHIBITED else []
        ))
        
        # ============ ANNEX I: HIGH-RISK AI SYSTEMS ============
        
        # 1. Employment - Recruitment/Selection
        if q5_recruitment:
            applicable = q5_recruitment != "No"
            status = ComplianceStatus.HIGH_RISK if applicable else ComplianceStatus.NOT_APPLICABLE
            criteria.append(ComplianceCriterion(
                criterion="AI systems used for recruitment or selection of personnel, including deep learning and targeted job offers",
                category="Annex I - Employment",
                status=status,
                explanation="AI recruitment systems are classified as high-risk under Annex I(4). Requires risk assessment, human oversight, and compliance with Articles 9-14" if applicable else "System does not make recruitment or selection decisions",
                applicable=applicable,
                risk_level="HIGH_RISK" if applicable else None,
                applicable_articles=[6, 9, 10, 13, 14] if applicable else []
            ))
        
        # 2. Employment - Performance Evaluation/Management
        if q6_employment:
            applicable = q6_employment != "No"
            status = ComplianceStatus.HIGH_RISK if applicable else ComplianceStatus.NOT_APPLICABLE
            criteria.append(ComplianceCriterion(
                criterion="AI systems evaluating employment conditions, work performance, or tasks, including monitoring and evaluation of workers",
                category="Annex I - Employment",
                status=status,
                explanation="Employment monitoring and performance evaluation are classified as high-risk under Annex I(4). Requires risk assessment, human oversight, and worker information" if applicable else "System does not evaluate employment conditions or performance",
                applicable=applicable,
                risk_level="HIGH_RISK" if applicable else None,
                applicable_articles=[6, 9, 10, 13, 14] if applicable else []
            ))
        

        
        # 7. Biometric - Identification Systems (non-real-time)
        if q7_biometric and q7_biometric != "No - does not use biometric data at all":
            if q7_biometric != "Yes - real-time remote biometric identification (face, iris, fingerprint live matching)":
                applicable = True
                status = ComplianceStatus.HIGH_RISK
                criteria.append(ComplianceCriterion(
                    criterion="Biometric identification systems (non-real-time or at-location)",
                    category="Annex I - Biometric",
                    status=status,
                    explanation="Non-real-time biometric identification systems are classified as high-risk under Annex I(1). Requires strict data protection and accuracy measures",
                    applicable=applicable,
                    risk_level="HIGH_RISK",
                    applicable_articles=[6, 9, 10, 13, 14]
                ))
        
        # 8. Credit/Financial Risk Assessment
        if q10_credit:
            applicable = q10_credit != "No - not involved in credit or financial decisions"
            status = ComplianceStatus.HIGH_RISK if applicable else ComplianceStatus.NOT_APPLICABLE
            criteria.append(ComplianceCriterion(
                criterion="AI systems assessing credit scoring, creditworthiness, or loan eligibility",
                category="Annex I - Finance",
                status=status,
                explanation="Credit and financial risk assessment are classified as high-risk under Annex I(2). Affects access to essential financial services" if applicable else "System does not assess credit or financial risk",
                applicable=applicable,
                risk_level="HIGH_RISK" if applicable else None,
                applicable_articles=[6, 9, 10, 13, 14] if applicable else []
            ))
        
        # 9. Critical Infrastructure
        if q9_infrastructure:
            applicable = q9_infrastructure in ["Yes - manages critical infrastructure (power grid, water, transport, communications)"]
            status = ComplianceStatus.HIGH_RISK if applicable else ComplianceStatus.NOT_APPLICABLE if q9_infrastructure != "Yes - important but not critical infrastructure" else ComplianceStatus.LIMITED_RISK
            criteria.append(ComplianceCriterion(
                criterion="AI systems managing critical infrastructure (power, water, transport, communications)",
                category="Annex I - Critical Infrastructure",
                status=status,
                explanation="Critical infrastructure management systems are high-risk under Annex I(5) due to safety and availability impact" if applicable else "System does not manage critical infrastructure" if q9_infrastructure != "Yes - important but not critical infrastructure" else "System manages important but non-critical infrastructure",
                applicable=applicable or (q9_infrastructure == "Yes - important but not critical infrastructure"),
                risk_level="HIGH_RISK" if applicable else "LIMITED_RISK" if (q9_infrastructure == "Yes - important but not critical infrastructure") else None,
                applicable_articles=[6, 9, 10, 13, 14] if applicable else []
            ))
        
        # ============ FAIRNESS & DISCRIMINATION ============
        
        # Sensitive Attribute Categorization
        if q8_sensitive:
            applicable = q8_sensitive != "No - does not make such categorizations"
            status = ComplianceStatus.LIMITED_RISK if applicable else ComplianceStatus.COMPLIANT
            criteria.append(ComplianceCriterion(
                criterion="AI systems categorizing or profiling individuals based on sensitive attributes (race, gender, disability, etc.)",
                category="General - Fairness",
                status=status,
                explanation="Systems making sensitive attribute inferences raise fairness and discrimination concerns. Requires fairness assessment and safeguards even if not explicitly high-risk" if applicable else "System does not categorize based on sensitive attributes",
                applicable=applicable,
                risk_level="LIMITED_RISK" if applicable else None,
                applicable_articles=[9, 10] if applicable else []
            ))
        
        # ============ GENERAL OBLIGATIONS ============
        
        # Risk Assessment & Documentation
        has_high_risk = any(c.risk_level == "HIGH_RISK" and c.applicable for c in criteria)
        status = ComplianceStatus.HIGH_RISK if has_high_risk else ComplianceStatus.COMPLIANT
        criteria.append(ComplianceCriterion(
            criterion="Comprehensive risk assessment and documentation (per Article 9)",
            category="General - Documentation",
            status=status,
            explanation="High-risk systems require documented risk assessments covering technical accuracy, robustness, cybersecurity, and compliance measures" if has_high_risk else "Not required for non-high-risk systems, though recommended",
            applicable=has_high_risk,
            risk_level="HIGH_RISK" if has_high_risk else None,
            applicable_articles=[9] if has_high_risk else []
        ))
        
        # Human Oversight
        status = ComplianceStatus.HIGH_RISK if has_high_risk else ComplianceStatus.COMPLIANT
        criteria.append(ComplianceCriterion(
            criterion="Human oversight and intervention capabilities (per Article 14)",
            category="General - Human Oversight",
            status=status,
            explanation="High-risk systems must enable human oversight: monitoring inputs, understanding outputs, and overriding decisions when needed" if has_high_risk else "Not required for non-high-risk systems",
            applicable=has_high_risk,
            risk_level="HIGH_RISK" if has_high_risk else None,
            applicable_articles=[14] if has_high_risk else []
        ))
        
        # Transparency & Information
        status = ComplianceStatus.HIGH_RISK if has_high_risk else ComplianceStatus.COMPLIANT
        criteria.append(ComplianceCriterion(
            criterion="Transparency and information provision (per Article 13)",
            category="General - Transparency",
            status=status,
            explanation="High-risk systems must inform affected individuals of AI involvement, provide explanations for decisions, and enable contestation" if has_high_risk else "Not required for non-high-risk systems",
            applicable=has_high_risk,
            risk_level="HIGH_RISK" if has_high_risk else None,
            applicable_articles=[13] if has_high_risk else []
        ))
        
        return criteria
    
    @staticmethod
    def format_for_display(criteria: List[ComplianceCriterion]) -> List[Dict]:
        """Format criteria for table display in Streamlit"""
        formatted = []
        for criterion in criteria:
            formatted.append({
                "Category": criterion.category,
                "Criterion": criterion.criterion,
                "Status": criterion.status.value if criterion.status != ComplianceStatus.NOT_APPLICABLE else "NOT APPLICABLE",
                "Explanation": criterion.explanation,
                "Risk Level": criterion.risk_level or "-",
                "Applicable": "✓" if criterion.applicable else "✗"
            })
        return formatted
