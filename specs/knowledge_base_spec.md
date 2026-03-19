# EU AI Act Knowledge Base - Specification

**Status**: Draft for MVP v1.0  
**Purpose**: Define structure and content for the AI Compliance Sherpa's knowledge base

---

## 1. Overview

The knowledge base is the foundation of the AI Compliance Sherpa agent. It contains:
- Structured information about EU AI Act articles and requirements
- Risk classification decision trees
- Use case examples
- Remediation guidance

This specification ensures the knowledge base is:
- **Accurate**: Reflects official EU AI Act text
- **Structured**: Organized for LLM retrieval
- **Complete**: Covers all relevant sections for MVP
- **Maintainable**: Easy to update as regulations evolve

---

## 2. Knowledge Base Structure

### 2.1 File Organization

```
knowledge_base/
├── eu_ai_act_articles/
│   ├── article_05_prohibited_practices.md
│   ├── article_06_high_risk_identification.md
│   ├── article_07_high_risk_requirements.md
│   ├── article_08-52_high_risk_detailed.md
│   ├── limited_risk_articles.md
│   └── minimal_risk_guidance.md
├── decision_trees/
│   ├── risk_classification_tree.md
│   ├── data_sensitivity_tree.md
│   └── decision_impact_tree.md
├── use_cases/
│   ├── high_risk_examples.md
│   ├── limited_risk_examples.md
│   └── compliant_systems.md
├── glossary.md
└── update_log.md
```

### 2.2 Article Content Structure

Each article file follows this template:

```markdown
# Article [NUMBER]: [TITLE]

**Source**: Regulation (EU) 2024/1689  
**Version**: EUR-Lex reference [xxx]  
**Last Updated**: YYYY-MM-DD

## Official Text

[Exact or summarized legal text from EU AI Act]

## Key Provisions

- Provision 1: [What it requires]
- Provision 2: [What it requires]

## Applicability

**Applies to**: [List of AI system types]  
**Does NOT apply to**: [Exclusions]

## Compliance Obligations

1. **Requirement A**
   - Who: [Developers/Providers/Users]
   - When: [Development/Deployment/Operation]
   - How: [Implementation approach]
   - Evidence needed: [Documentation/Tests/Certifications]

## Related Articles

Cross-references to related articles and requirements

## Questions for Classification

Questions that help determine if this article applies:
- Question 1?
- Question 2?
- Question 3?

## Examples

### Scenario A ✅ COMPLIANT
[Description of compliant system]

### Scenario B ❌ NON-COMPLIANT  
[Description of non-compliant system + remediation]

## Resources

- Link to official guidance
- Link to impact assessment templates
- Link to technical documentation
```

---

## 3. Article Coverage for MVP

### 3.1 Prohibited AI Practices (Article 5)

**Content Must Include**:
- List of all prohibited practices
- Context for why each is prohibited
- Exception cases (if any)
- Consequences of violation

**Trigger Questions**:
- Does your system engage in subliminal manipulation?
- Does it exploit vulnerabilities of vulnerable groups?
- Does it perform real-time facial recognition in public spaces for law enforcement? (specific contexts)

### 3.2 High-Risk AI Systems (Articles 6-52)

**Content Must Include**:
- Criteria for identifying high-risk systems
- List of high-risk use cases (Annex I & III)
- Mandatory requirements (technical, governance, operational)
- Documentation obligations
- Human oversight requirements
- Conformity assessment procedures

**Key Areas**:
1. **Risk Assessment & Management** (Article 9)
2. **Transparency & Information** (Article 13)
3. **Human Oversight** (Article 14)
4. **Accuracy, Robustness & Cybersecurity** (Article 15)
5. **Documentation** (Article 11)
6. **Logging** (Article 12)
7. **Biometric Identification Systems** (Article 10)
8. **Data & AI Governance** (Articles 10, 16-20)

### 3.3 Limited-Risk AI Systems (Articles 50-52)

**Content Must Include**:
- Definition of limited-risk systems
- Transparency obligations ("know you're talking to AI")
- Use cases: Chatbots, deepfakes, AI-generated content labels
- Implementation approaches

### 3.4 Minimal Risk

**Content Must Include**:
- Definition: All other AI systems
- Proportionate risk management approach recommendation
- Enterprise best practices (not mandatory but advisable)

---

## 4. Decision Tree Content

### 4.1 Risk Classification Decision Tree

```
START: Analyze AI System
│
├─→ Q1: Does it perform ANY of these?
│   ├─ Subliminal manipulation
│   ├─ Exploit vulnerabilities
│   ├─ Real-time facial recognition (law enforcement, public spaces)
│   ├─ Biometric categorization by sensitive attributes
│   ├─ Emotion recognition (law enforcement, workplace contexts)
│   ├─ Social scoring
│   └─ Derived rights (restricting fundamental rights based on inference)
│      └─→ YES → PROHIBITED ❌
│      └─→ NO → Continue to Q2
│
├─→ Q2: Does it match ANY high-risk use case?
│   ├─ Employment/HR decisions
│   ├─ Law enforcement investigations
│   ├─ Critical infrastructure control
│   ├─ Education/training access
│   ├─ Credit/financial services
│   ├─ Citizenship/migration
│   ├─ Biometric identification/verification
│   ├─ Safety-critical systems
│   └─ Healthcare decisions
│      └─→ YES → Continue to Q3
│      └─→ NO → Continue to Q4
│
├─→ Q3: Does it produce AUTONOMOUS decisions affecting fundamental rights?
│   └─→ YES → HIGH-RISK ⚠️
│   └─→ NO → Consider LIMITED-RISK
│
├─→ Q4: Is it a LIMITED-RISK system?
│   ├─ Chatbot/conversational AI
│   ├─ Deepfake detection
│   ├─ AI-generated content system
│   └─→ YES → LIMITED-RISK ℹ️
│   └─→ NO → Continue
│
└─→ DEFAULT: MINIMAL-RISK ✅
```

### 4.2 Data Sensitivity Decision Tree

Helps classify whether system processes sensitive data:

```
Personal Data?
├─ YES → Special Categories? (Race, health, biometrics, etc.)
│        ├─ YES → SENSITIVE ⚠️
│        └─ NO → Continue
├─ Scope: How many individuals?
│   ├─ Large Scale (100K+) → HIGH sensitivity
│   └─ Limited scope → MODERATE sensitivity
└─ NO → Check derived data (inferred attributes)
```

---

## 5. Use Case Examples

Each section must contain realistic, company-relatable examples:

### 5.1 High-Risk Examples

**Example 1: Resume Screening System**
- **System**: CV filtering for job candidates
- **Risk Level**: HIGH-RISK
- **Why**: Employment decision, affects fundamental right (to work), autonomous decision-making
- **Applicable Articles**: 6(1), 9 (Risk Management), 13 (Transparency), 14 (Human Oversight)
- **Requirements**:
  1. Risk assessment document
  2. Human review of borderline cases
  3. Clear communication to candidates
  4. Testing for bias (gender, age, ethnicity)
  5. Documentation of training data

**Remediation**: [Steps to make compliant]

### 5.2 Limited-Risk Examples

**Example 2: Customer Service Chatbot**
- **System**: LLM-based support bot
- **Risk Level**: LIMITED-RISK
- **Why**: Transparency obligation (users must know they're talking to AI)
- **Applicable Articles**: 50, 52 (Transparency)
- **Requirements**:
  1. Clear disclosure that interaction is with AI
  2. Escalation path to human agents
  3. Content policy compliance

---

## 6. Glossary of Key Terms

Include definitions for:
- **AI System**: As per EU AI Act definition
- **High-Risk AI System**: Formal definition
- **Provider**: Entity developing/releasing the AI system
- **Deployer**: Entity using the AI system
- **Fundamental Rights**: ECHR and Charter rights
- **Autonomous Decision-Making**: System decides without human input
- **Biometric Data**: Face, fingerprint, iris, voice
- **Sensitive Data**: Special categories under GDPR
- **Impact Assessment**: Documentation of system design and risk mitigation
- **Conformity Assessment**: Verification that system meets requirements
- **Human Oversight**: Human review and intervention capability

---

## 7. Knowledge Base Content Checklist

### Must-Have Content
- [ ] Article 5 (Prohibited): Complete list + context
- [ ] Article 6 (High-Risk Definition): All criteria
- [ ] Annex I (High-Risk Use Cases): All categories
- [ ] Annex III (Additional High-Risk): All categories  
- [ ] Articles 7-15 (High-Risk Requirements): Technical summary
- [ ] Articles 50-52 (Limited-Risk): Transparency requirements
- [ ] Decision trees for classification
- [ ] 15+ realistic use case examples
- [ ] Glossary of key terms

### Nice-to-Have Content (Future)
- [ ] GDPR cross-references
- [ ] DSA integration
- [ ] Case law / regulatory guidance documents
- [ ] Industry-specific guidance
- [ ] Frequently Asked Questions

---

## 8. LLM Retrieval Optimization

To ensure Sherpa agent can effectively use this KB:

### 8.1 Chunking Strategy
- Articles broken into sections <1500 words each (optimal for RAG)
- Clear section headers (Article X, Section Y)
- Bullet points for key requirements
- Use case examples separated for retrieval

### 8.2 Embedding & Indexing
- All articles embedded once (stored in vector DB or embedding cache)
- Metadata tags: `article_number`, `article_title`, `risk_category`, `use_case_type`
- Enable semantic search: "What are requirements for employment decisions?"

### 8.3 Prompt Engineering Notes
When agent retrieves KB articles, it should:
1. Cite article numbers in reasoning
2. Extract exact regulatory language
3. Map questionnaire responses to articles
4. Explain gaps vs. requirements

---

## 9. Maintenance & Updates

### 9.1 Change Log

Track all updates:

```markdown
## Update Log

### Version 1.0 (2026-03-15)
- Initial MVP knowledge base
- Articles 5-15 fully documented
- Articles 50-52 documented
- 20 use case examples included

### [Future Updates Go Here]
```

### 9.2 Review Triggers

Update knowledge base when:
- EU AI Act regulation is amended
- EDPB/regulatory body issues guidance
- Company legal team flags new interpretation
- Quarterly legal review (even if no changes)

### 9.3 Version Control

- Store in Git with date-based versioning
- Tag releases: `kb_v1.0`, `kb_v1.1`, etc.
- Maintain change log in each article

---

## 10. Source Document References

### EU AI Act Sources
- **Official Text**: [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- **Recitals**: Full contextual explanations
- **Annexes**: 
  - Annex I: High-Risk Categories
  - Annex III: Additional High-Risk Cases
  - Annex IV: Technical Documentation Requirements

### Regulatory Guidance (To Be Collected)
- EU Commission implementation guidance (when published)
- EDPB AI guidelines
- National regulatory authority guidance

---

## 11. Knowledge Base Integration with Agent Prompt

The agent's system prompt will include:

```
You are the AI Compliance Sherpa, an expert in EU AI Act compliance.

Knowledge Base Available:
- EU AI Act Articles 5-52 with full provision text
- Decision trees for risk classification
- 50+ use case examples
- Best practice remediation guidance

Your Role:
1. Analyze user's AI system description via questionnaire
2. Search knowledge base for relevant articles and use cases
3. Classify risk level using decision trees
4. Explain classification with direct references to articles
5. Provide remediation guidance for non-compliant systems

Requirements:
- Always cite article numbers when explaining requirements
- Review ALL applicable articles before finalizing classification
- Assess both system characteristics AND use context
- Recommend expert legal review for edge cases or novel systems
- Explain in clear language, providing article excerpts
```

---

**Next Steps**:
1. Create detailed article markdown files (Article 5, 6, etc.)
2. Develop decision tree implementations (logic/code)
3. Collect 50+ use case examples from company's AI projects
4. Create agent system prompt and retrieval configuration
5. Implement vector DB / embedding-based retrieval

