# AI Compliance Sherpa MVP - System Specification

**Status**: Draft for MVP v1.0
**Author**: R&D Governance Team
**Date**: March 2026

---

## 1. Problem Statement

AI development teams within the company often approach compliance and governance as an afterthought, leading to:
- Projects requiring late-stage redesign to meet regulatory requirements
- Increased time-to-market due to compliance rework
- Risk of building non-compliant systems that cannot be deployed
- Lack of early visibility into compliance risks during the design phase

The EU AI Act introduces regulatory requirements for risk classification (Prohibited, High-Risk, Limited Risk, Minimal Risk), but R&D teams lack a structured, accessible tool to understand the implications during development planning.

**Desired Outcome**: Enable teams (PMs, architects, R&D) to understand the risk classification of their AI system early in development, using a conversational agent that translates EU AI Act requirements into actionable guidance.

---

## 2. Motivation

**Why Now?**
- EU AI Act is now in force; compliance is not optional
- Hackathon POC demonstrated feasibility of agentic approach
- Early-stage compliance assessment prevents costly late-stage pivots
- A "speed enabler" mindset: compliance helps teams move faster by clarifying constraints upfront

**Business Value**
- Reduce time-to-compliance for new AI initiatives
- Democratize compliance knowledge across technical teams
- Create audit trail of risk classification decisions
- Support risk management and board reporting

---

## 3. Goals & Non-Goals

### Goals
1. **Risk Classification**: Accurately classify AI systems into EU AI Act risk categories (Prohibited, High-Risk, Limited Risk, Minimal Risk)
2. **Explainability**: Provide detailed, article-referenced explanations for each classification decision
3. **User-Friendly Questionnaire**: Accept structured input from Microsoft Forms questionnaire about AI system characteristics
4. **Conversational Guidance**: Guide users through next steps and remediation suggestions for high-risk systems
5. **Knowledge-Grounded**: Ground responses in actual EU AI Act text and articles
6. **Audit Trail**: Log all classifications with reasoning for governance/compliance records

### Non-Goals (For MVP)
- Real-time compliance monitoring of deployed systems
- Integration with model training pipelines
- Multinational compliance (focus: EU AI Act only for MVP)
- Support for custom organizational policies (only EU AI Act v1.0)
- AI system performance validation or technical testing

---

## 4. Proposed Solution

### 4.1 High-Level Architecture

```
┌─────────────────────┐
│  User Questionnaire │ (MS Form Input)
│   JSON Response    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│   Input Processing & Validation Layer   │
│   - Parse questionnaire                 │
│   - Extract key system characteristics  │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  AI Compliance Sherpa Agent (AutoGen)   │
│  - System Prompt (EU AI Act)            │
│  - Knowledge Base (Act articles)        │
│  - Risk Classification Logic            │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│   Output Generation & Explanation       │
│   - Risk category decision              │
│   - Article-by-article breakdown       │
│   - Remediation suggestions             │
│   - JSON + Human-readable report       │
└─────────────────────────────────────────┘
```

### 4.2 Core Components

#### 4.2.1 Knowledge Base
- **Source**: EU AI Act (Regulation (EU) 2024/1689)
- **Content**: 
  - Articles defining risk categories
  - Use case examples from each risk tier
  - Technical requirements per article
  - Compliance checklist items
- **Format**: Structured markdown with article references

#### 4.2.2 Questionnaire Schema
Input from Microsoft Form capturing:
- AI System Name & Purpose
- Data Types (personal, sensitive, special categories)
- Decision-Making Scope (individual vs. group, consequences)
- Autonomous Decision-Making (yes/no, appeals process)
- Use Case Category (employment, law enforcement, education, etc.)
- Key Stakeholders (data subjects, minors involved)
- Monitoring & Auditing Capabilities
- Human Oversight Mechanisms

#### 4.2.3 Risk Classification Engine
Input: Questionnaire responses  
Process: 
1. Check for Prohibited AI (article 5 violations) → Output: PROHIBITED
2. If not prohibited, check High-Risk indicators → Output: HIGH-RISK (if matched)
3. Otherwise, check Limited-Risk indicators → Output: LIMITED-RISK
4. Otherwise → OUTPUT: MINIMAL-RISK

#### 4.2.4 Explanation Generator
For each classification:
- List applicable articles with article numbers
- Extract relevant requirements from EU AI Act
- Explain how system characteristics trigger compliance obligations
- Suggest remediation steps if deficiencies found

### 4.3 Technology Stack

| Component | Technology |
|-----------|-----------|
| LLM Backbone | OpenAI GPT-4 (via AutoGen) |
| Agent Framework | AutoGen 0.2.x |
| Input Interface | Microsoft Forms (JSON API) |
| Knowledge Management | Markdown-based knowledge base |
| Output Format | JSON + Markdown report |
| Language | Python 3.10+ |
| Dependencies | autogen-agentchat, openai, pydantic |

---

## 5. Requirements

### 5.1 Functional Requirements

| ID | Requirement | Acceptance Criteria |
|----|-----------|-------------------|
| FR1 | Accept questionnaire input | Agent receives questionnaire JSON, validates required fields |
| FR2 | Classify system risk level | Output includes one of: PROHIBITED, HIGH-RISK, LIMITED-RISK, MINIMAL-RISK |
| FR3 | Explain classification | For each article applied, provide extracted text & explanation |
| FR4 | Reference EU AI Act | All explanations cite article numbers & sections |
| FR5 | Suggest remediation | For HIGH-RISK systems, provide concrete next steps to address gaps |
| FR6 | Log decision | All classifications logged with timestamp, questionnaire hash, and reasoning |
| FR7 | Handle edge cases | Agent gracefully handles ambiguous/incomplete questionnaires |

### 5.2 Non-Functional Requirements

| ID | Requirement | Target |
|----|-----------|--------|
| NFR1 | Response latency | < 30 seconds for classification (incl. API calls) |
| NFR2 | Availability | 99.5% uptime (standard cloud SLA) |
| NFR3 | Accuracy | Classification matches expert review in 95%+ of test cases |
| NFR4 | Knowledge currency | EU AI Act knowledge updated within 1 month of amendments |
| NFR5 | Audit trail | 100% of classifications logged with full reasoning |
| NFR6 | Security | API keys secured via environment variables; no sensitive data in logs |

### 5.3 Constraints

- MVP scope: EU AI Act only (no other regulatory frameworks)
- Single agent architecture (no multi-agent collaboration)
- Synchronous request-response model (no async workflows)
- English language output only

---

## 6. Data Structures

### 6.1 Questionnaire Schema (Input)

```json
{
  "metadata": {
    "form_submission_id": "uuid",
    "timestamp": "2026-03-09T10:30:00Z",
    "submitter_role": "PM|ARCHITECT|ENGINEER",
    "organization_unit": "string"
  },
  "system_info": {
    "name": "string",
    "description": "string",
    "purpose": "string",
    "expected_deployment_date": "2026-06-01",
    "deployment_scope": "INTERNAL|EXTERNAL|PUBLIC"
  },
  "data_processing": {
    "personal_data_processed": boolean,
    "sensitive_data_processed": boolean,
    "special_category_data": boolean,
    "data_source_description": "string"
  },
  "decision_making": {
    "produces_legal_decisions": boolean,
    "produces_individual_decisions": boolean,
    "affects_fundamental_rights": boolean,
    "autonomous_decision_making": boolean,
    "human_appeal_process": boolean
  },
  "use_case_category": "EMPLOYMENT|LAW_ENFORCEMENT|EDUCATION|CRITICAL_INFRASTRUCTURE|MIGRATION|CREDIT|OTHER",
  "stakeholders": {
    "minors_involved": boolean,
    "vulnerable_groups": boolean,
    "data_subject_count": "integer",
    "countries_affected": ["ISO-3166-ALPHA-2"]
  },
  "governance": {
    "data_protection_officer_involved": boolean,
    "human_oversight_mechanism": "FULL|PARTIAL|NONE",
    "monitoring_capability": "REAL_TIME|PERIODIC|POST_DEPLOYMENT|NONE",
    "explainability_requirement": "COMPREHENSIVE|BASIC|NONE"
  }
}
```

### 6.2 Classification Output Schema

```json
{
  "classification_id": "uuid",
  "timestamp": "2026-03-09T10:35:00Z",
  "questionnaire_id": "uuid",
  "risk_classification": "PROHIBITED|HIGH_RISK|LIMITED_RISK|MINIMAL_RISK",
  "confidence_score": 0.95,
  "applicable_articles": [
    {
      "article_number": 5,
      "article_title": "Prohibited AI Practices",
      "is_violated": true,
      "explanation": "string",
      "extracted_legal_text": "string"
    }
  ],
  "compliance_obligations": [
    {
      "article_number": 6,
      "requirement": "string",
      "affected_by_system": boolean,
      "recommended_action": "string"
    }
  ],
  "remediation_suggestions": [
    {
      "priority": "CRITICAL|HIGH|MEDIUM|LOW",
      "action": "string",
      "rationale": "string",
      "estimated_effort": "DAYS|WEEKS|MONTHS"
    }
  ],
  "next_steps": [
    "string"
  ],
  "expert_review_recommended": boolean,
  "expert_review_rationale": "string"
}
```

---

## 7. API Contract

### Endpoint: POST /api/v1/classify-ai-system

**Request**
```
POST /api/v1/classify-ai-system
Content-Type: application/json
Authorization: Bearer <api-key>

{
  "questionnaire": {...}, // Questionnaire Schema as defined in 6.1
  "user_context": {
    "user_id": "string",
    "organization": "string"
  }
}
```

**Response (200 OK)**
```
{
  "status": "success",
  "data": {...} // Classification Output Schema as defined in 6.2
}
```

**Response (400 Bad Request)**
```
{
  "status": "error",
  "error_code": "INVALID_QUESTIONNAIRE",
  "message": "Required field 'system_info.name' is missing",
  "details": {"missing_fields": ["system_info.name"]}
}
```

**Response (429 Too Many Requests)**
```
{
  "status": "error",
  "error_code": "RATE_LIMIT_EXCEEDED",
  "message": "Rate limit exceeded. Try again in 60 seconds."
}
```

---

## 8. Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Set up EU AI Act knowledge base (markdown files with articles)
- [ ] Define and test questionnaire schema
- [ ] Create AutoGen Sherpa agent with system prompt
- [ ] Unit tests for risk classification logic

### Phase 2: Integration (Week 3)
- [ ] MS Forms connector for questionnaire ingestion
- [ ] API wrapper for agent interaction
- [ ] Output formatting (JSON + markdown report generation)
- [ ] Integration tests

### Phase 3: Refinement (Week 4)
- [ ] User acceptance testing with sample systems
- [ ] Accuracy validation against expert classifications
- [ ] Documentation & runbooks
- [ ] Performance optimization + caching

### Phase 4: Deployment (Week 5)
- [ ] Environment setup (dev, staging, prod)
- [ ] Audit logging & monitoring
- [ ] Team training
- [ ] Go-live

---

## 9. Success Metrics

| Metric | Target | Rationale |
|--------|--------|-----------|
| Classification accuracy | 95%+ agreement with expert review | Core reliability requirement |
| User satisfaction | 4.0+/5.0 NPS | Usability & value |
| Adoption rate | 70%+ of new AI projects use tool | Business impact |
| Response time | <30 seconds per classification | User experience threshold |
| False negative rate (missing high-risk systems) | <2% | Safety critical—don't miss risks |

---

## 10. Testing Strategy

### Unit Tests
- Risk classification logic for each category
- Error handling for malformed inputs
- EU AI Act knowledge base search

### Integration Tests
- End-to-end: questionnaire → classification → report
- MS Forms input parsing
- API error responses

### User Acceptance Tests
- Sample AI systems (real cases from company)
- Expert review of classifications
- Feedback loop on explanations

### Performance Tests
- Latency under normal load
- Response time with large knowledge base
- Concurrent request handling

---

## 11. Open Questions & Risks

### Open Questions
1. **MS Forms Integration**: What's the exact MS Forms questionnaire structure? (To be finalized with team)
2. **Knowledge Base Scope**: Should we include guidance for other EU regulations (GDPR, DSA)? Scope creep risk.
3. **Update Frequency**: How will we keep up with EU AI Act amendments/guidance post-launch?
4. **Escalation Process**: When should systems be escalated to legal for expert review?

### Risks & Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| LLM misclassifies due to ambiguous prompt | Medium | High | Extensive system prompt engineering + expert validation in testing |
| EU AI Act text changes/updates | Low-Medium | Medium | Establish knowledge base update SLA; version tracking |
| Low adoption due to organizational friction | Medium | High | Early engagement with stakeholder teams; show quick wins |
| Knowledge base becomes outdated | Low | Medium | Quarterly reviews; alert system for regulatory updates |

---

## 12. References

- **EU AI Act**: [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- **Implementation Guidance**: Official EU AI Act guidance documents (to be collected)
- **AutoGen Documentation**: [Microsoft AutoGen](https://microsoft.github.io/autogen/)

---

## Appendix A: Risk Classification Framework Summary

Quick reference for risk categories:

| Category | Definition | Examples | Key Requirements |
|----------|-----------|----------|------------------|
| **Prohibited** | AI systems that violate fundamental rights | Subliminal manipulation, banned facial recognition use cases | Must not be deployed |
| **High-Risk** | AI systems with significant impact on fundamental rights or safety | Biometric identification, employment decisions, credit scoring | Mandatory impact assessments, human oversight, transparency, documentation |
| **Limited-Risk** | AI systems with transparency concerns | Chatbots, deepfakes detection | Transparency obligations; users must know they're interacting with AI |
| **Minimal-Risk** | All other AI systems | Spam detection, game AI | Proportionate risk management |

---

**Next Step**: Review this specification with stakeholders and proceed to detailed design specifications for each component.
