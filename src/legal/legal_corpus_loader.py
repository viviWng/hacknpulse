"""
Legal Corpus Loader - Layer 1: Official Legal Corpus
Provides access to EU AI Act regulation text and annexes.

This module loads the official regulation text from knowledge_base/legal/eu_ai_act/
and provides methods to retrieve articles, annexes, and full regulation text.

PRINCIPLE: All explanations and context provided by the LLM must be grounded
in official regulation text loaded by this module.
"""

import json
import os
from pathlib import Path
from typing import Optional, Dict, List
from datetime import datetime


class LegalCorpusLoader:
    """Load and retrieve EU AI Act regulation text and metadata"""

    def __init__(self, base_path: str = "knowledge_base/legal"):
        """
        Initialize legal corpus loader
        
        Args:
            base_path: Path to knowledge_base/legal directory
        """
        self.base_path = Path(base_path)
        self.eu_ai_act_path = self.base_path / "eu_ai_act"
        self.version_metadata = self._load_version_metadata()
        self._corpus_cache = {}  # Cache loaded documents
        
    def _load_version_metadata(self) -> Dict:
        """Load legal version metadata"""
        version_file = self.base_path / "legal_version.json"
        if version_file.exists():
            with open(version_file, 'r') as f:
                return json.load(f)
        return {
            "regulation": "EU 2024/1689",
            "version_date": "2024-05-22",
            "checksum": "unknown"
        }
    
    def get_version_info(self) -> Dict:
        """Get regulation version and metadata"""
        return self.version_metadata
    
    def get_regulation_text(self) -> Optional[str]:
        """
        Get full EU AI Act regulation text
        
        Returns:
            Full regulation text or None if not found
        """
        return self._load_document("regulation_summary.txt")
    
    def get_article_text(self, article_number: int) -> Optional[str]:
        """
        Get full text of a specific article
        
        Args:
            article_number: Article number (5, 6, 9, 10, 13, 14)
            
        Returns:
            Article text or None if not found
        """
        # Map article numbers to content sections
        article_map = {
            5: "ARTICLE_5_PROHIBITED",
            6: "ARTICLE_6_HIGH_RISK",
            9: "ARTICLE_9_RISK_ASSESSMENT",
            10: "ARTICLE_10_DATA_QUALITY",
            13: "ARTICLE_13_TRANSPARENCY",
            14: "ARTICLE_14_HUMAN_OVERSIGHT"
        }
        
        if article_number not in article_map:
            return None
        
        # Get regulation text
        regulation_text = self.get_regulation_text()
        if not regulation_text:
            return None
        
        # Extract article section (simplified)
        article_label = article_map[article_number]
        if article_label in regulation_text:
            start = regulation_text.find(f"# {article_label}")
            if start == -1:
                start = regulation_text.find(article_label)
            if start != -1:
                # Find next article or end of text
                end = regulation_text.find("# ARTICLE_", start + 1)
                if end == -1:
                    end = len(regulation_text)
                return regulation_text[start:end].strip()
        
        return None
    
    def get_annex_text(self, annex_name: str) -> Optional[str]:
        """
        Get full text of a specific annex
        
        Args:
            annex_name: Annex name ("Annex I", "Annex II", "Annex III", "Annex IV")
            
        Returns:
            Annex text or None if not found
        """
        return self._load_document(f"annex_{annex_name.replace(' ', '_').lower()}.txt")
    
    def _load_document(self, filename: str) -> Optional[str]:
        """
        Load document from knowledge base
        
        Args:
            filename: Document filename
            
        Returns:
            Document content or None if not found
        """
        if filename in self._corpus_cache:
            return self._corpus_cache[filename]
        
        file_path = self.eu_ai_act_path / filename
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self._corpus_cache[filename] = content
                return content
        
        return None
    
    def get_applicable_articles(self, questionnaire_data: Dict) -> List[int]:
        """
        Get applicable article numbers based on questionnaire
        
        Args:
            questionnaire_data: Questionnaire responses
            
        Returns:
            List of applicable article numbers
        """
        articles = []
        
        # Check each question and map to articles
        if questionnaire_data.get("q5_recruitment_selection"):
            articles.extend([6, 9, 10, 13, 14])
        
        if questionnaire_data.get("q6_employment_conditions"):
            articles.extend([6, 9, 10, 13, 14])
        
        if questionnaire_data.get("q7_biometric_identification"):
            articles.extend([6, 9, 10, 13, 14])
        
        if questionnaire_data.get("q8_categorization_sensitive"):
            articles.extend([6, 9, 10, 13, 14])
        
        if questionnaire_data.get("q9_critical_infrastructure"):
            articles.extend([6, 9, 10, 13, 14])
        
        if questionnaire_data.get("q10_credit_scoring"):
            articles.extend([6, 9, 10, 13, 14])
        
        # Remove duplicates and sort
        return sorted(list(set(articles)))
    
    def get_article_summary(self, article_number: int) -> Dict:
        """
        Get summary information about an article
        
        Args:
            article_number: Article number
            
        Returns:
            Dictionary with article summary
        """
        summaries = {
            5: {
                "number": 5,
                "title": "Prohibited AI Practices",
                "description": "Defines AI systems that are absolutely prohibited under EU AI Act",
                "key_prohibitions": [
                    "Subliminal manipulation beyond consciousness",
                    "Social scoring based on behavior or characteristics",
                    "Real-time remote biometric identification (law enforcement with narrow exceptions)"
                ]
            },
            6: {
                "number": 6,
                "title": "Classification of High-Risk AI Systems",
                "description": "Defines what constitutes high-risk AI systems requiring compliance measures",
                "annex_reference": "Annex I",
                "applies_to": [
                    "Recruitment and selection systems",
                    "Employment evaluation systems",
                    "Education assessment systems",
                    "Credit and financial access systems",
                    "Law enforcement applications",
                    "Critical infrastructure systems"
                ]
            },
            9: {
                "number": 9,
                "title": "Risk Assessment",
                "description": "Requires risk assessment for high-risk AI systems before deployment",
                "requirements": [
                    "Identify and analyze reasonably foreseeable risks",
                    "Assess severity of risks",
                    "Evaluate existing and proposed mitigations",
                    "Document risk assessment process",
                    "Update when significant changes occur"
                ]
            },
            10: {
                "number": 10,
                "title": "Data Quality and Governance",
                "description": "Data must be relevant, representative, error-free, and complete",
                "requirements": [
                    "Training, validation, test data: relevant and representative",
                    "Data governance practices documented and effective",
                    "Data management subject to monitoring",
                    "Audit trail maintained"
                ]
            },
            13: {
                "number": 13,
                "title": "Transparency and Information to Users",
                "description": "Users must be informed about AI systems affecting them",
                "requirements": [
                    "Inform when interacting with AI system",
                    "Provide meaningful information about system",
                    "Enable understanding of how system works",
                    "Inform about right to human intervention",
                    "For generated content: disclose AI generation"
                ]
            },
            14: {
                "number": 14,
                "title": "Human Oversight",
                "description": "High-risk AI systems must be designed for effective human oversight",
                "requirements": [
                    "Ability to stop execution of tasks",
                    "Ability to override or reverse AI decisions",
                    "Human intervention during design, development, deployment",
                    "Meaningful and proportionate oversight"
                ]
            }
        }
        
        return summaries.get(article_number, {
            "number": article_number,
            "title": f"Article {article_number}",
            "description": "See official EU AI Act regulation text"
        })
    
    def create_audit_log_entry(self, 
                              classification_result: str,
                              applicable_articles: List[int],
                              questionnaire_hash: str) -> Dict:
        """
        Create audit log entry with version information
        
        Args:
            classification_result: Risk classification (PROHIBITED, HIGH_RISK, etc.)
            applicable_articles: Article numbers that apply
            questionnaire_hash: Hash of questionnaire input
            
        Returns:
            Audit log entry dictionary
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "regulation_version": self.version_metadata.get("regulation", "unknown"),
            "regulation_date": self.version_metadata.get("version_date", "unknown"),
            "regulation_checksum": self.version_metadata.get("checksum", "unknown"),
            "classification_result": classification_result,
            "applicable_articles": applicable_articles,
            "questionnaire_hash": questionnaire_hash,
            "audit_trail_version": "1.0"
        }


# Singleton instance for application
_legal_corpus_instance = None

def get_legal_corpus_loader(base_path: str = "knowledge_base/legal") -> LegalCorpusLoader:
    """Get or create singleton legal corpus loader instance"""
    global _legal_corpus_instance
    if _legal_corpus_instance is None:
        _legal_corpus_instance = LegalCorpusLoader(base_path)
    return _legal_corpus_instance
