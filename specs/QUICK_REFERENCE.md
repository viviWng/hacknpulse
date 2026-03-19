# Specification Quick Reference

**Purpose**: One-page overview of key decisions and requirements  
**Audience**: Team members, stakeholders, reviewers

---

## Project Overview

| Aspect | Detail |
|--------|--------|
| **Project Name** | AI Compliance Sherpa MVP |
| **Goal** | Classify AI systems by EU AI Act risk level (Prohibited, High-Risk, Limited-Risk, Minimal-Risk) |
| **Scope** | MVP: Single agent, EU AI Act only, synchronous classification |
| **Method** | Specification-driven development (GitHub Spec Kit) |
| **Timeline** | 5 weeks (Phases 1-4) |
| **Tech Stack** | Python 3.10+, AutoGen, GPT-4, FastAPI |

---

## Key Design Decisions

| Decision | Rationale | Alternative |
|----------|-----------|------------|
| **Single Agent** | Simpler system, faster MVP delivery | Multiple agents (considered but too complex) |
| **In-Context Learning** (KB) | No external dependencies, fast | RAG (deferred to Phase 5) |
| **Synchronous API** | Simpler client integration, <30s latency | Async (for future scaling) |
| **GPT-4 Backbone** | Best accuracy for legal reasoning | GPT-3.5 (cheaper but less accurate) |
| **MS Forms Input** | Native in Microsoft stack, easy adoption | Custom UI (deferred) |
| **JSON + Markdown Output** | Machine-readable + human-friendly | JSON-only (less actionable) |

---

## Risk Classification Framework (Quick Ref)

### Decision Tree Logic

```
1. Check PROHIBITED (Article 5)
   → YES: PROHIBITED ❌
   → NO: Continue to 2

2. Check HIGH-RISK Criteria
   a) Matches Annex I use case? (HR, law enforcement, education, etc.)
   b) Produces autonomous decisions affecting fundamental rights?
   → YES to both: HIGH-RISK ⚠️
   → NO: Continue to 3

3. Check LIMITED-RISK
   a) Chatbot? Deepfake detector? AI-generated content?
   → YES: LIMITED-RISK ℹ️
   → NO: Continue to 4

4. Default
   → MINIMAL-RISK ✅
```

### Classification Definitions

| Category | Definition | Req'd Actions | Example |
|----------|-----------|---------------|---------|
| **PROHIBITED** | Violates fundamental rights | Must not deploy | Subliminal manipulation, real-time facial recognition for law enforcement in public |
| **HIGH-RISK** | Significant impact on rights/safety | Impact assessment, human oversight, testing, documentation | HR screening, credit scoring, biometric ID |
| **LIMITED-RISK** | Transparency concerns | User disclosure | Chatbots, deepfakes |
| **MINIMAL-RISK** | All other AI | Proportionate approach | Recommendation engines, spam filters |

---

## Input/Output Schemas (Abbreviated)

### Key Questionnaire Fields

```json
{
  "system_info": {
    "name": "string",
    "purpose": "string"
  },
  "data_processing": {
    "personal_data_processed": boolean,
    "sensitive_data_processed": boolean  
  },
  "decision_making": {
    "produces_individual_decisions": boolean,
    "affects_fundamental_rights": boolean,
    "autonomous_decision_making": boolean
  },
  "use_case_category": "EMPLOYMENT|LAW_ENFORCEMENT|...",
  "governance": {
    "human_oversight_mechanism": "FULL|PARTIAL|NONE",
    "monitoring_capability": "REAL_TIME|PERIODIC|NONE"
  }
}
```

### Classification Output

```json
{
  "risk_classification": "PROHIBITED|HIGH_RISK|LIMITED_RISK|MINIMAL_RISK",
  "confidence_score": 0.92,
  "applicable_articles": [
    {
      "article_number": 6,
      "is_violated": true
    }
  ],
  "compliance_obligations": [
    {
      "requirement": "string",
      "recommended_action": "string"
    }
  ],
  "next_steps": ["string"]
}
```

---

## Article Coverage by Risk Category

### Prohibited (Article 5)
- Subliminal manipulation
- Exploitation of vulnerabilities
- Social scoring
- Real-time facial recognition (specific law enforcement contexts)
- Biometric categorization by sensitive attributes
- Emotion recognition (specific contexts)
- Derived discrimination (restricting rights based on inference)

### High-Risk (Articles 6-15, Annexes I & III)
- **Annex I Categories**: Employment, HR, critical infrastructure, law enforcement, education, migration, credit, biometric systems, safety-critical
- **Key Requirements**: Risk assessment (Article 9), impact assessment, human oversight (Article 14), documentation, testing, monitoring

### Limited-Risk (Articles 50-52)
- **Categories**: Chatbots, deepfake detection, AI-generated content
- **Requirements**: Transparency (inform users they're interacting with AI)

### Minimal-Risk
- All other systems
- Proportionate risk management (recommended best practices)

---

## API Endpoints (MVP)

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `POST` | `/api/v1/classify-ai-system` | Submit questionnaire, get classification |
| `GET` | `/api/v1/classification/{id}` | Retrieve past classification (future) |
| `GET` | `/docs` | Swagger UI documentation |
| `GET` | `/health` | Health check |

### Example Request

```bash
curl -X POST https://api.company.com/v1/classify-ai-system \
  -H "Content-Type: application/json" \
  -d @questionnaire.json
```

---

## Success Metrics (MVP Target)

| Metric | Target | Why |
|--------|--------|-----|
| Classification Accuracy | 95%+ vs. expert review | Core reliability |
| Response Latency | <30 seconds | User experience |
| False Negative Rate | <2% (miss high-risk) | Safety critical |
| Code Coverage | >80% | Quality threshold |
| User Satisfaction | 4.0+/5.0 NPS | Adoption indicator |
| Team Adoption | 70%+ of new AI projects | Business impact |

---

## Knowledge Base Structure

```
knowledge_base/
├── articles/
│   ├── article_05_prohibited.md      (Required practices)
│   ├── article_06_high_risk.md       (Definition)
│   ├── article_09_risk_assessment.md (Mandatory process)
│   ├── article_14_human_oversight.md (Critical requirement)
│   └── [...articles_7-52...]
├── decision_trees/
│   └── risk_classification.md        (Classification logic)
├── use_cases/
│   ├── high_risk_examples.md
│   └── limited_risk_examples.md
└── glossary.md
```

---

## Development Phases (5 Weeks)

| Phase | Week | Focus | Deliverable |
|-------|------|-------|-------------|
| **1: Foundation** | 1-2 | Setup, KB, Agent | Repo ready, KB skeleton, agent initializes |
| **2: Integration** | 3 | API, Output, MS Forms | API working, classifications complete |
| **3: Refinement** | 4 | Testing, Optimization, Docs | 95%+ accuracy, <20s latency |
| **4: Deployment** | 5 | Production, Monitoring, Training | Live, monitored, documented |

---

## Critical Specs by Role

### For Product Manager
- **Specification**: [spec.en.md](spec.en.md) - Section 1-3 (Problem, Goals)
- **MS Forms**: [ms_forms_spec.md](ms_forms_spec.md) - Questionnaire design
- **Implementation**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Section 10 (Collaboration)

### For Architect
- **All Specifications**: Read in full
- **Key Docs**: [agent_spec.md](agent_spec.md), [knowledge_base_spec.md](knowledge_base_spec.md)
- **Architecture**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Section 2

### For Engineers
- **Core Specs**: [agent_spec.md](agent_spec.md), [knowledge_base_spec.md](knowledge_base_spec.md)
- **API Contract**: [spec.en.md](spec.en.md) - Section 7
- **Development Guide**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)

### For Legal / Compliance
- **Specification**: [spec.en.md](spec.en.md) - Sections 1, 3, 9
- **KB Structure**: [knowledge_base_spec.md](knowledge_base_spec.md)
- **Accuracy**: [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Section 6 (Testing)

---

## Document Map (How They Connect)

```
spec.en.md (System Specification)
├─ Describes problem, goals, overall design
├─ References API contract section 7
└──→ Links to specialized specs below

knowledge_base_spec.md (KB Structure)
├─ Details how EU AI Act knowledge is organized
├─ Templates for articles, use cases, decision trees
└──→ Used by agent_spec.md Section 3

agent_spec.md (Agent Architecture)
├─ Describes AutoGen agent initialization
├─ System prompt with KB context (references knowledge_base_spec)
├─ Input/output processing
└──→ Implementation by engineers (IMPLEMENTATION_GUIDE)

ms_forms_spec.md (MS Forms Integration)
├─ Questionnaire design (input schema from spec.en.md)
├─ Data collection and privacy
├─ Integration with agent API (from agent_spec)
└──→ Setup by PM/full team

IMPLEMENTATION_GUIDE.md (Development Guide)
├─ References all specifications above
├─ Project structure, setup, development workflow
├─ Testing strategy (validates all specs)
└──→ Used by engineers daily
```

---

## Known Limitations & Risk Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| LLM Misclassification | Medium | High | Extensive testing, confidence scores, expert escalation |
| Knowledge base outdates | Low-Medium | Medium | Quarterly reviews, version tracking, update alerts |
| Low adoption | Medium | High | Early stakeholder engagement, quick wins, training |
| Legal liability | Low | Critical | Expert review escalation, clear disclaimers, audit trail |
| API cost overruns | Medium | Medium | Token limits, caching (future), cost monitoring |
| Performance degradation | Low | Medium | Load testing, optimization, scaling strategy |

---

## Implementation Checklists

### Pre-Development
- [ ] All team members read and understand specifications
- [ ] GitHub repository created and configured
- [ ] Development environment set up (Python, dependencies)
- [ ] API keys provisioned (OpenAI, Azure, etc.)
- [ ] Kickoff meeting completed; questions resolved

### Phase 1 Complete
- [ ] Repo structure matches Section 2 of IMPLEMENTATION_GUIDE
- [ ] CI/CD pipeline running (tests, linting)
- [ ] First 3 articles fully documented in KB
- [ ] AutoGen agent initialized and callable
- [ ] Unit tests >80% coverage

### Phase 2 Complete
- [ ] All EU AI Act articles documented
- [ ] API endpoint working end-to-end
- [ ] Output parsing and formatting complete
- [ ] MS Forms integration tested
- [ ] Integration tests passing

### Phase 3 Complete
- [ ] 95%+ classification accuracy vs. experts
- [ ] Response time <20 seconds (P95)
- [ ] All documentation complete
- [ ] UAT passed with sample AI systems
- [ ] Security audit completed

### Phase 4 Complete
- [ ] Deployed to production environment
- [ ] Monitoring and alerting configured
- [ ] On-call runbooks documented
- [ ] Team trained and confident
- [ ] Stakeholder communication sent

---

## FAQ (Quick Answers)

**Q: What if my system doesn't fit any category?**  
A: Default to MINIMAL-RISK; escalate for expert review if affects individuals.

**Q: Can I appeal the classification?**  
A: Yes. Classify again with updated info. recommend expert legal review for edge cases.

**Q: Does this replace legal compliance review?**  
A: No. This is educational guidance. Final legal determinations require legal team review.

**Q: What if the form can't describe my system?**  
A: Escalate for expert review. Alert team so form can be updated.

**Q: How often will the knowledge base be updated?**  
A: Quarterly minimum. More frequently if regulatory changes occur.

---

## Contact & Escalation

- **Technical Questions**: [AI Compliance Sherpa Team Slack]
- **Legal Questions**: [Legal Team Email]
- **Product/Business**: [PM Name/Contact]
- **Urgent Issues**: [On-call Engineer]

---

## Version Control

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-09 | Initial specifications |
| — | — | — |

---

**Last Updated**: March 9, 2026  
**Status**: DRAFT - Ready for team review  
**Next Step**: Kickoff meeting and Q&A
