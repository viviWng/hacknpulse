# EU AI Act Knowledge Base - Architecture (SDD Compliant)

## Overview

The EU AI Act Knowledge Base has been redesigned according to Specification-Driven Development (SDD) principles to ensure:

- **Deterministic Classification**: Rules-based logic that is reproducible and auditable
- **Legal Grounding**: All decisions reference official EU AI Act regulation text
- **Versioning & Auditability**: Every classification includes metadata for compliance auditing
- **Separation of Concerns**: LLM used only for explanation, not classification
- **Maintainability**: Regulatory updates can be applied safely via configuration files

---

## Architecture Layers

### Layer 1: Official Legal Corpus
**Location**: `knowledge_base/legal/eu_ai_act/`

Contains the official EU AI Act regulation text:
- `regulation_2024_1689.txt` - Full regulation text
- `annex_I.txt` - Prohibited and high-risk categories
- `annex_II.txt` - High-risk systems list (detailed)
- `annex_III.txt` - AI systems exemptions
- `annex_IV.txt` - Specific obligations
- `legal_version.json` - Version metadata and tracking

**Purpose**: 
- Provide authoritative legal reference
- Enable legal audit trail
- Ground LLM explanations in official text
- Track regulatory updates

### Layer 2: Structured Compliance Rules
**Location**: `knowledge_base/rules/`

Machine-readable YAML rule files:
- `prohibited_practices.yaml` - Article 5 prohibitions
- `high_risk_domains.yaml` - Article 6 high-risk categories (Annex I)
- `risk_mapping.yaml` - Question-to-article mappings and decision logic

**Purpose**:
- Enable DETERMINISTIC classification (reproducible)
- Map questionnaire responses to regulatory articles
- Define compliance obligations and safeguards
- Separate logic from code for maintainability

### Layer 3: Interpretative Guidance
**Location**: `knowledge_base/guidance/`

Markdown documents for LLM explanation context:
- `article_explanations.md` - Detailed article summaries
- `domain_examples.md` - Use case examples per domain
- `compliance_best_practices.md` - Implementation guidance

**Purpose**:
- Help LLM generate human-friendly explanations
- Provide context for recommendations
- Show examples and best practices
- **NOT used for classification logic**

---

## Module Architecture

### Classification Flow

```
User Input (Questionnaire)
    ↓
[Pydantic Validation - schemas.py]
    ↓
classify_system() [classification.py]
    ↓
    ├─→ Rule Engine (rule_engine.py)
    │   ├─ Load YAML rules
    │   ├─ Check PROHIBITED practices (Article 5)
    │   ├─ Check HIGH_RISK systems (Article 6)
    │   └─ Return: risk_classification, articles, confidence
    │
    ├─→ Legal Corpus (legal_corpus_loader.py)
    │   ├─ Load regulation text
    │   ├─ Get article summaries
    │   └─ Create audit log entries
    │
    └─→ Sherpa Agent (sherpa/agent.py) [EXPLANATION ONLY]
        ├─ Generate human-friendly explanation
        └─ Extract recommendations
    ↓
ClassificationResult with versioning
    ├─ risk_classification
    ├─ applicable_articles (from legal_corpus)
    ├─ compliance_obligations (from rule_engine)
    ├─ regulation_version
    ├─ rule_version
    ├─ classification_timestamp
    └─ questionnaire_hash (audit trail)
```

---

## Key Components

### 1. Rule Engine (`src/compliance/rule_engine.py`)

**Responsibility**: Deterministic classification using YAML rules

**Key Methods**:
- `classify(questionnaire_data)` → (risk_level, articles, confidence)
- `_check_prohibited_practices()` → Check Article 5
- `_check_high_risk_systems()` → Check Article 6
- `get_applicable_requirements()` → Get compliance obligations

**Principle**: Classification logic is in YAML rules, not hardcoded Python

```python
# Usage:
engine = get_rule_engine()
risk_level, articles, confidence = engine.classify(questionnaire_dict)
```

### 2. Legal Corpus Loader (`src/legal/legal_corpus_loader.py`)

**Responsibility**: Load and provide access to regulation text

**Key Methods**:
- `get_article_text(article_number)` → Official regulation text
- `get_annex_text(annex_name)` → Annex content
- `get_applicable_articles(questionnaire_data)` → Articles that apply
- `get_article_summary(article_number)` → Article overview
- `create_audit_log_entry()` → Versioned audit trail

**Principle**: All legal references grounded in official corpus

```python
# Usage:
corpus = get_legal_corpus_loader()
article_text = corpus.get_article_text(6)
audit_entry = corpus.create_audit_log_entry(...)
```

### 3. Classification (`src/classification.py`)

**Updated to orchestrate**:
1. Call rule_engine for deterministic classification
2. Call legal_corpus for article grounding
3. Call Sherpa agent for explanation only
4. Build ClassificationResult with versioning

**Key Change**: Uses engines instead of hardcoded logic

```python
def classify_system(questionnaire, agent_explanation):
    rule_engine = get_rule_engine()
    legal_corpus = get_legal_corpus_loader()
    
    # Step 1: Deterministic classification via rules
    risk_level, articles, confidence = rule_engine.classify(
        questionnaire.dict()
    )
    
    # Step 2: Get legal grounding
    applicable_articles = [
        ApplicableArticle(
            article_number=num,
            article_title=legal_corpus.get_article_summary(num)['title'],
            ...
        )
        for num in articles
    ]
    
    # Step 3: Agent explanation (supplementary)
    recommendations = parse_agent_recommendations(agent_explanation)
    
    # Step 4: Return versioned result
    return ClassificationResult(
        ...,
        regulation_version=legal_corpus.get_version_info()['regulation'],
        rule_version=rule_engine.get_rule_version_info()['rules_version'],
        classification_timestamp=datetime.now().isoformat(),
        questionnaire_hash=_generate_questionnaire_hash(...)
    )
```

### 4. Schemas (`src/schemas.py`)

**Updated ClassificationResult** with versioning:
```python
regulation_version: Optional[str]        # "EU 2024/1689"
regulation_date: Optional[str]           # "2024-05-22"
rule_version: Optional[str]              # "2.0"
rule_version_date: Optional[str]         # "2026-03-12"
classification_timestamp: Optional[str]  # ISO format
questionnaire_hash: Optional[str]        # SHA256 (audit trail)
```

---

## YAML Rule Structure Example

### `high_risk_domains.yaml`

```yaml
high_risk_domains:
  
  recruitment_selection:
    name: "AI systems intended to be used for recruitment and selection"
    annex_reference: "Annex I(4)(a)"
    articles: [6, 9, 10, 13, 14]
    questions_trigger:
      - q5_recruitment_selection
    affected_rights:
      - "Access to employment"
      - "Non-discrimination"
    requirements:
      - Article 6: Classification as high-risk
      - Article 9: Risk assessment required
      - Article 10: Data quality and governance
      - Article 13: Transparency to affected persons
      - Article 14: Human oversight mandatory
    safeguards_needed:
      - Human review of all flagged candidates
      - Documentation of training data sources
      - Bias testing before deployment
```

---

## Regulatory Update Process

### Monthly (15 minutes)
- Check EUR-Lex for new amendments
- Review EU AI Office guidance (launches Feb 2025)
- Update `legal_version.json` if changes detected

### Quarterly (30-60 minutes)
- Review EDPB opinions and guidance
- Update article text files if interpretations change
- Add test cases for new guidance

### Annual (2-4 hours)
- Comprehensive audit against latest guidance
- Update rule files if decision trees change
- Review for any amendments to regulation

### Git Workflow
```bash
# Update legal corpus
git add knowledge_base/legal/
git commit -m "Update EU AI Act regulation based on EUR-Lex guidance (2026-Q1)"

# Update rules
git add knowledge_base/rules/
git commit -m "Update risk_mapping.yaml per EDPB opinion on Article 6"

# Track version
git tag -a v1.1 -m "Support for new EU AI Office guidance"
```

---

## Governance & Compliance

### System Classification
The Compliance Sherpa tool itself is:
**Minimal Risk AI** (internal decision support, not automated enforcement)

### Output Disclaimer
Every classification report includes:
```
⚠️ DISCLAIMER
This automated assessment provides guidance on EU AI Act classification 
based on the provided questionnaire and should not replace legal advice. 
Classification is based on rule version [VERSION] and regulation 
[EU 2024/1689] as of [DATE].
```

### Audit Trail
Every classification produces:
```json
{
  "timestamp": "2026-03-12T15:30:45.123Z",
  "questionnaire_hash": "a1b2c3d4e5f6g7h8",
  "regulation_version": "EU 2024/1689",
  "rule_version": "2.0",
  "risk_classification": "HIGH_RISK",
  "applicable_articles": [6, 9, 10, 13, 14],
  "confidence_score": 0.92
}
```

---

## Testing & Validation

### Unit Tests
- Test prohibited practices detection (Article 5)
- Test high-risk classification (Article 6)
- Test confidence scoring
- Test YAML rule loading

### Integration Tests
- End-to-end: questionnaire → classification → report
- Verify version information included
- Verify legal grounding via corpus

### Regression Tests
- 10+ pre-built test systems with expected classifications
- Test against rule updates
- Verify backward compatibility

---

## Migration Guide (From Old System)

### What Changed
1. **Classification logic** moved from Python → YAML rules
2. **Article mapping** centralized in `risk_mapping.yaml`
3. **Legal grounding** added via `legal_corpus_loader.py`
4. **Versioning** added to all results

### What Stayed the Same
- Questionnaire format (Q5-Q10)
- Risk classification levels (PROHIBITED, HIGH_RISK, LIMITED_RISK, MINIMAL_RISK)
- Streamlit UI functionality
- FastAPI API contract (new versioning fields added)

### For Developers
```python
# OLD - Hardcoded logic (DEPRECATED)
from src.classification import is_high_risk
if is_high_risk(questionnaire):
    ...

# NEW - Rule engine (CORRECT)
from src.compliance.rule_engine import get_rule_engine
engine = get_rule_engine()
risk_level, articles, confidence = engine.classify(questionnaire.dict())
if risk_level == "HIGH_RISK":
    ...
```

---

## Performance & Scalability

| Operation | Latency | Notes |
|-----------|---------|-------|
| Load rule engine | ~50ms | Cached after first load |
| Classify (deterministic) | ~100ms | YAML parsing + rule evaluation |
| Load legal corpus text | ~200ms | Cached; only once per session |
| Sherpa explanation (LLM) | 1-3 sec | Azure OpenAI API call |
| Audit log generation | <10ms | JSON serialization |
| **Total per classification** | **1.5-3.5 sec** | LLM is bottleneck |

---

## Future Enhancements

### Phase 2: Multi-Language Support
- Translate rule files and guidance to EU languages
- Maintain version control for translations

### Phase 3: Dynamic Compliance Monitoring
- Automatic monitoring of EU AI Office guidance
- Alerting for regulatory changes
- Automatic rule updates (with human review)

### Phase 4: Enterprise Features
- Organizational rule customization
- Custom compliance frameworks
- Integration with CI/CD governance gates

---

## References

- **EU AI Act**: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **EU AI Office** (launches Feb 2025): https://artificial-intelligence-act.ec.europa.eu
- **Architecture Design**: `/ARCHITECTURE_SUMMARY.md`
- **SDD Specification**: Provided as design input

---

**Document Version**: 1.0  
**Last Updated**: March 12, 2026  
**Regulation Version**: EU 2024/1689  
**Rule Version**: 2.0
