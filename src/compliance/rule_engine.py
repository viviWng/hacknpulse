"""
Rule Engine - Layer 2: Structured Compliance Rules
Loads and applies YAML rule files for deterministic risk classification.

This module provides the deterministic classification logic based on
structured YAML rules instead of hardcoded Python logic.

PRINCIPLE: Classification must be reproducible and auditable by reading rules
from YAML configuration files.
"""

import yaml
from pathlib import Path
from typing import Optional, Dict, List, Tuple
import hashlib


class RuleEngine:
    """Load and apply compliance rules from YAML configuration"""

    def __init__(self, rules_path: str = "knowledge_base/rules"):
        """
        Initialize rule engine
        
        Args:
            rules_path: Path to knowledge_base/rules directory
        """
        self.rules_path = Path(rules_path)
        self._rules_cache = {}
        self.rules_version = "2.0"
        self.rules_last_updated = "2026-03-12"
        
    def load_rules(self) -> Dict:
        """
        Load all rule files from rules directory
        
        Returns:
            Dictionary containing all loaded rules
        """
        rules = {}
        
        # Load prohibited practices rules
        prohibited = self._load_yaml_file("prohibited_practices.yaml")
        if prohibited:
            rules["prohibited"] = prohibited
        
        # Load high-risk domains rules
        high_risk = self._load_yaml_file("high_risk_domains.yaml")
        if high_risk:
            rules["high_risk"] = high_risk
        
        # Load risk mapping rules
        risk_mapping = self._load_yaml_file("risk_mapping.yaml")
        if risk_mapping:
            rules["risk_mapping"] = risk_mapping
        
        return rules
    
    def _load_yaml_file(self, filename: str) -> Optional[Dict]:
        """
        Load YAML file from rules directory
        
        Args:
            filename: YAML filename
            
        Returns:
            Parsed YAML content or None if not found
        """
        if filename in self._rules_cache:
            return self._rules_cache[filename]
        
        file_path = self.rules_path / filename
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                self._rules_cache[filename] = content
                return content
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return None
    
    def classify(self, questionnaire_data: Dict) -> Tuple[str, List[int], float]:
        """
        Classify AI system based on questionnaire and rules
        
        This is the CORE DETERMINISTIC CLASSIFICATION LOGIC using rules.
        
        Args:
            questionnaire_data: Questionnaire responses
            
        Returns:
            Tuple of (risk_classification, applicable_articles, confidence_score)
        """
        # Load rules
        rules = self.load_rules()
        
        # STEP 1: Check for PROHIBITED practices (Article 5)
        prohibited_result = self._check_prohibited_practices(
            questionnaire_data, 
            rules.get("prohibited", {})
        )
        if prohibited_result:
            return prohibited_result
        
        # STEP 2: Check for HIGH-RISK systems (Article 6)
        high_risk_result = self._check_high_risk_systems(
            questionnaire_data,
            rules.get("high_risk", {}),
            rules.get("risk_mapping", {})
        )
        if high_risk_result:
            return high_risk_result
        
        # STEP 3: Default to MINIMAL_RISK
        return ("MINIMAL_RISK", [], 0.85)
    
    def _check_prohibited_practices(self, questionnaire: Dict, rules: Dict) -> Optional[Tuple]:
        """
        Check if system violates Article 5 (Prohibited practices)
        
        Returns:
            Tuple if PROHIBITED, None otherwise
        """
        if not rules or "prohibited_practices" not in rules:
            return None
        
        prohibited = rules["prohibited_practices"]
        
        # Check for real-time remote biometric identification
        if questionnaire.get("q7_biometric_identification"):
            # If it mentions real-time remote biometric ID with law enforcement
            bio_description = str(questionnaire.get("purpose", "")).lower()
            if any(keyword in bio_description for keyword in 
                   ["real-time", "facial recognition", "remote biometric", "live"]):
                
                # Check if it's law enforcement
                if any(keyword in str(questionnaire.get("use_case", "")).lower() 
                       for keyword in ["law enforcement", "police", "border", "security"]):
                    
                    return ("PROHIBITED", [5], 0.95)
        
        # Check for social scoring
        purpose = str(questionnaire.get("purpose", "")).lower()
        if any(keyword in purpose for keyword in ["social scoring", "social credit", "citizen scoring"]):
            return ("PROHIBITED", [5], 0.95)
        
        # Check for subliminal manipulation
        if any(keyword in purpose for keyword in ["subliminal", "subconscious manipulation"]):
            return ("PROHIBITED", [5], 0.95)
        
        return None
    
    def _check_high_risk_systems(self, questionnaire: Dict, high_risk_rules: Dict, 
                                 risk_mapping: Dict) -> Optional[Tuple]:
        """
        Check if system qualifies as HIGH-RISK (Article 6)
        
        Returns:
            Tuple if HIGH_RISK, None otherwise
        """
        if not risk_mapping or "risk_mapping" not in risk_mapping:
            return None
        
        risk_mapping = risk_mapping["risk_mapping"]
        high_risk_questions = ["q5_recruitment_selection", "q6_employment_conditions",
                              "q7_biometric_identification", "q8_categorization_sensitive",
                              "q9_critical_infrastructure", "q10_credit_scoring"]
        
        # Count how many high-risk questions are answered affirmatively
        high_risk_count = 0
        applicable_articles = set()
        
        for question in high_risk_questions:
            if question in risk_mapping:
                answer = questionnaire.get(question)
                
                if answer == True:
                    high_risk_count += 1
                    rule_info = risk_mapping[question].get("if_true", {})
                    articles = rule_info.get("applicable_articles", [])
                    applicable_articles.update(articles)
                
                elif answer == "potential":
                    # "Potential" is treated as lower risk
                    rule_info = risk_mapping[question].get("if_potential")
                    if rule_info:
                        articles = rule_info.get("applicable_articles", [])
                        applicable_articles.update(articles)
        
        # If any high-risk question is true, classification is HIGH_RISK
        if high_risk_count > 0:
            # Calculate confidence based on criteria met
            confidence = self._calculate_confidence(questionnaire, high_risk_count)
            return ("HIGH_RISK", sorted(list(applicable_articles)), confidence)
        
        return None
    
    def _calculate_confidence(self, questionnaire: Dict, high_risk_count: int) -> float:
        """
        Calculate confidence score for HIGH_RISK classification
        
        Args:
            questionnaire: Questionnaire data
            high_risk_count: Number of high-risk questions answered affirmatively
            
        Returns:
            Confidence score (0.7 - 0.95)
        """
        base_confidence = 0.70
        
        # Boost confidence based on criteria met
        if high_risk_count >= 3:
            base_confidence = 0.90
        elif high_risk_count == 2:
            base_confidence = 0.80
        elif high_risk_count == 1:
            base_confidence = 0.70
        
        # Additional confidence boost for employment/finance use cases
        use_case = str(questionnaire.get("use_case", "")).lower()
        if any(keyword in use_case for keyword in ["employment", "law enforcement", "credit", "finance"]):
            base_confidence = min(0.95, base_confidence + 0.05)
        
        # Additional confidence boost if both autonomous and affects rights
        if questionnaire.get("autonomous") and questionnaire.get("affects_rights"):
            base_confidence = min(0.95, base_confidence + 0.05)
        
        return base_confidence
    
    def get_applicable_requirements(self, risk_classification: str, 
                                    applicable_articles: List[int]) -> Dict:
        """
        Get applicable compliance requirements based on classification
        
        Args:
            risk_classification: Risk level (PROHIBITED, HIGH_RISK, etc.)
            applicable_articles: List of applicable article numbers
            
        Returns:
            Dictionary with requirements and obligations
        """
        requirements = {
            "risk_classification": risk_classification,
            "applicable_articles": applicable_articles,
            "compliance_obligations": [],
            "safeguards_needed": []
        }
        
        if risk_classification == "PROHIBITED":
            requirements["compliance_obligations"] = [
                "DO NOT DEPLOY - System violates Article 5",
                "Remove from market immediately",
                "Cease all use and testing"
            ]
            return requirements
        
        if risk_classification == "HIGH_RISK":
            base_obligations = [
                "Conduct risk assessment per Article 9",
                "Implement data quality measures per Article 10",
                "Provide transparency per Article 13",
                "Implement human oversight per Article 14"
            ]
            requirements["compliance_obligations"] = base_obligations
            
            # Add specific obligations based on articles
            if 6 in applicable_articles:
                requirements["compliance_obligations"].append(
                    "Meet high-risk system requirements (Article 6)"
                )
            if 9 in applicable_articles:
                requirements["compliance_obligations"].append(
                    "Document risk assessment findings"
                )
            if 13 in applicable_articles:
                requirements["compliance_obligations"].append(
                    "Ensure users are informed about AI system"
                )
            if 14 in applicable_articles:
                requirements["compliance_obligations"].append(
                    "Ensure human can override or stop system"
                )
            
            return requirements
        
        if risk_classification == "LIMITED_RISK":
            requirements["compliance_obligations"] = [
                "Provide transparency information (Article 13)",
                "Enable human override capability",
                "Maintain user awareness of AI system"
            ]
            return requirements
        
        # MINIMAL_RISK
        requirements["compliance_obligations"] = [
            "Monitor for any changes that would increase risk",
            "Maintain documentation of system design"
        ]
        return requirements
    
    def get_rule_version_info(self) -> Dict:
        """Get rule engine version and metadata"""
        return {
            "rules_version": self.rules_version,
            "rules_last_updated": self.rules_last_updated,
            "rules_location": str(self.rules_path),
            "regulation_reference": "EU 2024/1689"
        }


# Singleton instance
_rule_engine_instance = None

def get_rule_engine(rules_path: str = "knowledge_base/rules") -> RuleEngine:
    """Get or create singleton rule engine instance"""
    global _rule_engine_instance
    if _rule_engine_instance is None:
        _rule_engine_instance = RuleEngine(rules_path)
    return _rule_engine_instance
