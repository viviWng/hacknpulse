# AI Compliance Sherpa Agent - Architectural Specification

**Status**: Draft for MVP v1.0  
**Purpose**: Define agent architecture, interaction patterns, and state management

---

## 1. Agent Architecture Overview

### 1.1 Agent Type
- **Framework**: Microsoft AutoGen (ConversableAgent)
- **LLM Backbone**: OpenAI GPT-4
- **Interaction Pattern**: Synchronous request-response (one-shot classification)
- **Knowledge Integration**: Knowledge base retrieval via context injection

### 1.2 Agent Goals

```
Primary Goal: Classify an AI system's risk level under EU AI Act 
              and provide detailed, actionable compliance guidance

Success Criteria:
- Accurate risk classification (95%+ agreement with legal experts)
- Explanation grounded in EU AI Act articles
- Clear remediation guidance for high-risk systems
- No hallucinations / staying within knowledge base
- Conversational but authoritative tone
```

---

## 2. Agent Configuration

### 2.1 System Prompt (Core Instructions)

```
You are the AI Compliance Sherpa, an expert AI compliance advisor 
specialized in the EU Artificial Intelligence Act.

Your Purpose:
You help R&D teams, architects, and product managers understand 
the regulatory risk classification of their AI systems under the 
EU AI Act. Your role is to educate, clarify, not to provide legal advice.

Knowledge Base:
You have access to comprehensive documentation of:
- All EU AI Act articles (5-52)
- Risk classification criteria
- High-risk use case categories
- Compliance requirements by risk level
- Real-world implementation examples

Your Methodology:
1. Analyze the AI system's characteristics from the user questionnaire
2. Reference relevant EU AI Act articles based on the system's usage
3. Apply risk classification decision trees systematically
4. Explain classifications with clear article citations
5. Provide actionable remediation steps for high-risk systems

Tone & Communication:
- Authoritative but educational (explain, don't dictate)
- Use plain language while citing legal sources
- Acknowledge uncertainty and recommend expert review when appropriate
- Empathize with compliance challenges while being clear on requirements
- Avoid legal jargon where possible; define technical terms

Critical Guidelines:
1. ALWAYS cite the specific EU AI Act article when explaining requirements
2. ALWAYS include the article number and provision description
3. If uncertain about classification, escalate to expert review recommendation
4. Do NOT make up articles or regulations not in your knowledge base
5. Do NOT provide legal advice; frame as educational guidance
6. Do NOT skip any potentially applicable articles in your analysis
7. Do NOT allow scope creep: Focus only on EU AI Act compliance
8. Acknowledge edge cases and limitations of automated classification

Output Format:
Structure your analysis as:
1. System Summary (reiterate understanding of their system)
2. Applicability Analysis (which articles/categories apply)
3. Risk Classification (PROHIBITED|HIGH-RISK|LIMITED-RISK|MINIMAL-RISK)
4. Detailed Explanation (article-by-article breakdown)
5. Compliance Obligations (what they must do)
6. Remediation Roadmap (for high-risk)
7. Next Steps (immediate actions)
8. Expert Review Recommendation (if applicable)

Risk Classification Definitions:
- PROHIBITED: System violates fundamental rights. Cannot be deployed.
- HIGH-RISK: System has significant impact on rights/safety. Requires 
  comprehensive compliance measures (impact assessment, human oversight, etc.)
- LIMITED-RISK: System has transparency implications. Primary obligation: 
  disclose to users they're interacting with AI.
- MINIMAL-RISK: All other AI systems. Proportionate approach recommended.

When Escalating to Expert Review:
Recommend expert legal review when:
- Novel use case not explicitly covered in guidance
- Complex multi-factor classification (doesn't clearly fit one category)
- High organizational impact (critical infrastructure, sensitive population)
- Rapid regulatory changes / recent amendments
- Risk of fundamental rights violation (erring on side of caution)
```

### 2.2 Agent Configuration Parameters

```python
# AutoGen ConversableAgent Configuration
agent_config = {
    "name": "ai_compliance_sherpa",
    "system_message": [system_prompt_above],
    
    # LLM Parameters
    "llm_config": {
        "config_list": [
            {
                "model": "gpt-4",
                "api_key": os.environ.get("OPENAI_API_KEY"),
                "temperature": 0.2,  # Lower temp for consistency
                "max_tokens": 2000,
                "top_p": 0.9,
            }
        ],
        "seed": 42,  # Reproducibility
    },
    
    # Interaction Parameters
    "human_input_mode": "NEVER",  # No human feedback loops in MVP
    "max_consecutive_auto_reply": 1,  # Single response, no back-and-forth
    
    # Termination
    "is_termination_msg": lambda msg: True,  # Single-turn interaction
}
```

---

## 3. Knowledge Base Integration

### 3.1 Knowledge Injection Strategy

**Option A: In-Context Learning (MVP Approach)**
- Load EU AI Act articles at agent initialization
- Inject full knowledge base into system prompt context
- Pros: No external dependencies, fast inference
- Cons: Token usage, limited scalability with larger KB

**Option B: Retrieval-Augmented Generation (RAG) - Future**
- Vector DB (e.g., Pinecone, Weaviate)
- Embeddings for semantic search
- Retrieve relevant articles on-demand based on questionnaire
- Pros: Scalable, efficient token usage
- Cons: Additional infrastructure, latency

**MVP Implementation**: Option A (in-context)
- Full Annex I & III categories in system prompt
- Key Articles (5-15, 50-52) as context
- Use case examples embedded in prompt
- Decision trees as structured rules

### 3.2 Context Injection in System Prompt

Structure:
```
[Base System Prompt - Section 2.1]

---

## EU AI ACT REFERENCE MATERIAL

### PROHIBITED PRACTICES (Article 5)
[Full text or summary]

### HIGH-RISK IDENTIFICATION (Article 6)
[Full text or summary]

### HIGH-RISK ANNEX I CATEGORIES
[Complete list with explanations]

### HIGH-RISK ANNEX III ADDITIONAL CATEGORIES
[Complete list]

### KEY COMPLIANCE REQUIREMENTS
- Article 7: Risk Management
- Article 9: Risk Assessment  
- Article 11: Documentation
- Article 13: Transparency
- Article 14: Human Oversight
[...]

### USE CASE EXAMPLES
[10-15 real examples showing classification reasoning]

### DECISION TREES
[Classification logic in pseudo code or flowchart format]
```

### 3.3 Version Control & Updates

- Knowledge base version tagged in prompt
- Format: `KB_VERSION: 1.0 (2026-03-15)`
- On updates: Update version, tests, deployment configs

---

## 4. Input Processing & Validation

### 4.1 Questionnaire Validation

Before passing to agent, validate:

```python
def validate_questionnaire(questionnaire: dict) -> Tuple[bool, List[str]]:
    """
    Validates questionnaire against schema.
    Returns (is_valid, error_messages)
    """
    errors = []
    required_fields = [
        "metadata.submission_id",
        "system_info.name",
        "system_info.purpose",
        "data_processing.personal_data_processed",
        "decision_making.produces_legal_decisions",
        "decision_making.produces_individual_decisions",
        "use_case_category",
    ]
    
    for field in required_fields:
        if not _get_nested_value(questionnaire, field):
            errors.append(f"Missing required field: {field}")
    
    # Type validation
    if not isinstance(questionnaire.get("metadata", {}).get("timestamp"), str):
        errors.append("metadata.timestamp must be ISO 8601 format")
    
    # Enum validation
    valid_categories = ["EMPLOYMENT", "LAW_ENFORCEMENT", "EDUCATION", ...]
    if questionnaire["use_case_category"] not in valid_categories:
        errors.append(f"Invalid use_case_category: {questionnaire['use_case_category']}")
    
    return len(errors) == 0, errors
```

### 4.2 Questionnaire Preprocessing

Transform questionnaire into  agent-friendly format:

```python
def preprocess_questionnaire(questionnaire: dict) -> str:
    """
    Convert questionnaire JSON to natural language summary for agent.
    """
    summary = f"""
    AI System Under Review: {questionnaire['system_info']['name']}
    
    PURPOSE:
    {questionnaire['system_info']['purpose']}
    
    DATA PROCESSING:
    - Processes personal data: {questionnaire['data_processing']['personal_data_processed']}
    - Processes sensitive data: {questionnaire['data_processing']['sensitive_data_processed']}
    - Uses special category data: {questionnaire['data_processing']['special_category_data']}
    
    DECISION-MAKING:
    - Produces legal/regulatory decisions: {questionnaire['decision_making']['produces_legal_decisions']}
    - Makes individual decisions: {questionnaire['decision_making']['produces_individual_decisions']}
    - Affects fundamental rights: {questionnaire['decision_making']['affects_fundamental_rights']}
    - Fully autonomous: {questionnaire['decision_making']['autonomous_decision_making']}
    - Has human appeal process: {questionnaire['decision_making']['human_appeal_process']}
    
    USE CASE CATEGORY: {questionnaire['use_case_category']}
    
    STAKEHOLDERS:
    - Involves minors: {questionnaire['stakeholders']['minors_involved']}
    - Involves vulnerable groups: {questionnaire['stakeholders']['vulnerable_groups']}
    - Affected population size: {questionnaire['stakeholders']['data_subject_count']}
    - EU countries affected: {', '.join(questionnaire['stakeholders']['countries_affected'])}
    
    GOVERNANCE:
    - Data Protection Officer involved: {questionnaire['governance']['data_protection_officer_involved']}
    - Human oversight: {questionnaire['governance']['human_oversight_mechanism']}
    - Monitoring capability: {questionnaire['governance']['monitoring_capability']}
    - Explainability requirement: {questionnaire['governance']['explainability_requirement']}
    """
    return summary.strip()
```

---

## 5. Agent Interaction Flow

### 5.1 Single-Turn Classification Flow

```
INPUT: Questionnaire JSON
   ↓
[Validation]
   ↓ (valid)
[Preprocessing: JSON → Natural Language Summary]
   ↓
[Agent Receives Message]
   ├─ System Prompt (with knowledge base)
   └─ User Message (questionnaire summary)
   ↓
[LLM Processing - GPT-4]
   ├─ Analyzes system characteristics
   ├─ References knowledge base articles
   ├─ Applies decision trees
   └─ Generates classification + explanation
   ↓
[Output Parsing]
   ├─ Extract risk classification
   ├─ Extract article citations
   ├─ Extract compliance obligations
   └─ Extract remediation suggestions
   ↓
[Response Formatting]
   ├─ JSON structure (per spec)
   └─ Markdown report for humans
   ↓
[Logging]
   ├─ Store classification + reasoning
   ├─ Log questionnaire hash (privacy)
   └─ Record timestamp
   ↓
OUTPUT: Classification JSON + Report
```

### 5.2 Error Handling & Edge Cases

| Scenario | Handling |
|----------|----------|
| Invalid questionnaire | Return 400 with validation errors; don't invoke agent |
| Ambiguous classification | Agent recommends expert review; confidence score < 0.85 |
| Knowledge base knowledge gap | Agent flags as "novel scenario"; recommends legal review |
| API rate limit | Graceful backoff; return 429 with retry-after header |
| Agent hallucination | Monitor via confidence scores; flag for manual review |
| Timeout (>30s) | Return 504; don't queue for retry |

---

## 6. Output Generation

### 6.1 Response Structure

The agent generates output following this structure:

```markdown
# AI Compliance Classification Report

**System**: {system_name}
**Submission ID**: {submission_id}
**Classification Date**: {timestamp}

## Executive Summary

**Risk Classification: [PROHIBITED|HIGH-RISK|LIMITED-RISK|MINIMAL-RISK]**
**Confidence Score**: [0.0-1.0]
**Expert Review Recommended**: [YES|NO]

{Brief one-paragraph summary of classification rationale}

## System Analysis

### System Understanding
{Restatement of system characteristics from questionnaire}

### Applicability Assessment
{Which articles/categories apply and why}

## Detailed Risk Analysis

### Article 5: Prohibited Practices
**Applies**: YES|NO
{If yes: check against each practice; explain if any match}

### Article 6: High-Risk Identification
**Applies**: YES|NO  
{If yes: evaluate against high-risk criteria}

### Annex I: High-Risk Use Cases
**Matching Categories**: [List any matches]

### Annex III: Additional High-Risk Cases
**Matching Categories**: [List any matches]

### [Additional articles as applicable]

## Compliance Obligations

For [RISK LEVEL] systems, you must:

1. **Required Action 1** (Article X)
   - Description
   - Timeline
   - Evidence/Deliverable

2. **Required Action 2** (Article Y)
   - Description
   - Timeline  
   - Evidence/Deliverable

## Remediation Roadmap (if HIGH-RISK)

### Critical (Immediate - <1 month)
1. Action item with estimate

### High Priority (1-3 months)  
1. Action item with estimate

### Medium Priority (3-6 months)
1. Action item with estimate

## Next Steps

1. [Immediate action]
2. [Phase 2 action]
3. [Ongoing action]

## Disclaimer

This analysis is based on the EU AI Act and information provided in the questionnaire. 
This is educational guidance, not legal advice. For final compliance determinations and 
legal implications, consult your organization's legal team.

---

**Report Generated By**: AI Compliance Sherpa v1.0
**Knowledge Base Version**: EU AI Act KB v1.0 (2026-03-15)
```

### 6.2 JSON Transformation

Parse agent output → JSON structure (per main spec, section 6.2)

---

## 7. Confidence Scoring

### 7.1 Confidence Mechanisms

Agent assigns confidence based on:

- **Clarity of questionnaire** (ambiguous answers → lower confidence)
- **Novelty of use case** (not in examples → lower confidence)
- **Certainty of classification** (clear match vs. borderline → lower confidence)
- **Presence of contradictions** (mixed risk signals → lower confidence)

Scoring:
- **0.95-1.0**: Clear classification, strong KB support, no ambiguity
- **0.85-0.94**: Confident, minor edge cases noted  
- **0.75-0.84**: Applicable but some uncertainty; expert review recommended
- **<0.75**: Significant uncertainty; expert legal review required

### 7.2 Recommending Expert Review

Agent recommends expert review when:
- Classification confidence < 0.85
- Novel use case not in guidance
- System affects high-risk population (minors, vulnerable groups)
- Potential fundamental rights violation (err on side of caution)
- Rapid regulatory changes / recent amendments

---

## 8. Testing Strategy

### 8.1 Agent Testing Approach

**Unit Tests**: Agent system prompt & knowledge base integrity
- Verify agent references correct articles
- Verify decision trees are followed
- Verify hallucination detection

**Integration Tests**: End-to-end questionnaire → classification
- Test with pre-classified benchmark systems
- Verify output JSON against schema
- Test error cases (malformed input, ambiguous cases)

**Accuracy Tests**: Comparison with legal experts
- Have legal experts classify 50+ systems
- Run agent on same systems  
- Measure agreement rate (target: 95%+)

**Stress Tests**: LLM cost & latency
- Measure tokens/response
- Measure wall-clock latency
- Identify optimization opportunities

### 8.2 Benchmark Test Cases

Maintain a dataset of pre-classified systems:

```json
{
  "test_case_id": "HC_001",
  "name": "Resume Screening - HR Department",
  "expected_classification": "HIGH_RISK",
  "expected_articles": [6, 9, 13, 14],
  "questionnaire": {...},
  "expert_notes": "Clear high-risk: employment decision, fundamental right to work"
}
```

---

## 9. Deployment Configuration

### 9.1 Environment Variables

```bash
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
KB_VERSION=1.0
LOG_LEVEL=INFO
MAX_REQUEST_TOKENS=2000
REQUEST_TIMEOUT_SECONDS=30
KNOWLEDGE_BASE_PATH=./kb/
```

### 9.2 Monitoring & Observability

Log structure:
```json
{
  "timestamp": "2026-03-15T10:35:00Z",
  "submission_id": "uuid",
  "event": "classification_complete",
  "risk_classification": "HIGH_RISK",
  "confidence_score": 0.92,
  "processing_time_ms": 8500,
  "tokens_used": {"prompt": 3200, "completion": 1100},
  "cost_usd": 0.18
}
```

---

## 10. Future Enhancements (Post-MVP)

- [ ] Multi-turn dialogue (ask clarifying questions)
- [ ] RAG-based KB retrieval (vector embeddings)
- [ ] Integration with MS Forms via webhook
- [ ] Audit logging to compliance database
- [ ] Regulatory update alerts
- [ ] Integration with GDPR/DSA compliance agents
- [ ] Uncertainty quantification
- [ ] Few-shot learning from user feedback

---

**Next Steps**:
1. Code the agent initialization (autogen.ConversableAgent)
2. Write comprehensive system prompt with full KB context
3. Create input validation & preprocessing functions
4. Implement output parsing & formatting
5. Set up test suite with benchmark cases  
6. Deploy and measure accuracy vs. legal experts

