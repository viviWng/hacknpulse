# AI Compliance Sherpa MVP

## Overview

**AI Compliance Sherpa** is a multi-agentic compliance system helping R&D teams assess AI systems against the EU AI Act during development. By embedding governance and compliance as a *speed enabler* (not a blocker), we help teams move faster while building responsibly.

This MVP focuses on a single agent that classifies AI systems by risk level (Prohibited, High-Risk, Limited-Risk, Minimal-Risk) based on questionnaire responses and EU AI Act knowledge.

### Key Philosophy

> **Governance and compliance is not here to slow projects down. It helps teams move faster without breaking what cannot be repaired yet.** 
> 
> Compliance issues shouldn't be an afterthought but a preliminary criterion to be weighed upon from the beginning of the development process.

---

## 📋 Getting Started

### Quick Start (5 minutes)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourorg/hacknpulse.git
   cd hacknpulse
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or: venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key
   nano .env
   ```

5. **Verify setup**
   ```bash
   pytest tests/unit/ -v
   ```

See [Development Setup Guide](specs/IMPLEMENTATION_GUIDE.md#4-local-development-setup) for detailed instructions.

---

## 📚 Documentation

### Comprehensive Specifications

This project uses **specification-driven development**. Start here:

#### 1. **[Main System Specification](specs/spec.en.md)** - START HERE
   - Problem statement & motivation
   - System goals & non-goals
   - High-level architecture  
   - Data schemas & API contracts
   - Success metrics
   - **Best for**: Understanding the full vision and requirements

#### 2. **[Knowledge Base Specification](specs/knowledge_base_spec.md)**
   - EU AI Act knowledge organization
   - Article structure and coverage
   - Decision trees for classification
   - Use case examples
   - **Best for**: Understanding how the agent knows about compliance

#### 3. **[Agent Architecture Specification](specs/agent_spec.md)**
   - AutoGen agent configuration
   - System prompt (with EU AI Act context)
   - Input/output validation
   - Error handling & edge cases
   - Testing strategy
   - **Best for**: Technical implementation details

#### 4. **[MS Forms Integration Specification](specs/ms_forms_spec.md)**
   - Questionnaire design (all questions)
   - Form validation rules
   - JSON schema and data collection
   - Integration with Agent API
   - **Best for**: Understanding user input flow

#### 5. **[Implementation Guide](specs/IMPLEMENTATION_GUIDE.md)**
   - Development setup instructions
   - Repository structure
   - Development phases (5 weeks)
   - Code standards & quality gates
   - Git workflow & collaboration
   - **Best for**: Day-to-day development reference

#### 6. **[Quick Reference](specs/QUICK_REFERENCE.md)**
   - One-page overview of key decisions
   - Decision trees (visual)
   - API endpoints & schemas (abbreviated)
   - Success metrics
   - **Best for**: Quick lookup while coding

### User & Operational Docs

- [API Documentation](docs/API.md) *(to be created)*
- [Architecture Diagrams](docs/ARCHITECTURE.md) *(to be created)*
- [Deployment Guide](docs/DEPLOYMENT.md) *(to be created)*
- [User Guide](docs/USER_GUIDE.md) *(to be created)*

---

## 🏗️ Project Structure

```
hacknpulse/
├── specs/                          # 📖 Specification-Driven Development
│   ├── spec.en.md                 # Main system specification
│   ├── knowledge_base_spec.md     # EU AI Act knowledge base structure
│   ├── agent_spec.md              # Agent architecture & design
│   ├── ms_forms_spec.md           # MS Forms questionnaire integration
│   ├── IMPLEMENTATION_GUIDE.md    # Development guide & setup
│   └── QUICK_REFERENCE.md         # One-page quick reference
│
├── src/                            # 🔧 Source Code (to be created)
│   ├── sherpa/                    # Agent initialization & core logic
│   ├── api/                       # FastAPI application & routes
│   ├── extraction/                # Questionnaire validation & preprocessing
│   ├── output/                    # Classification output & report generation
│   ├── knowledge_base/            # EU AI Act knowledge (data + loader)
│   └── utils/                     # Utilities, logging, errors
│
├── knowledge_base/                 # 📚 EU AI Act Knowledge (data files)
│   ├── articles/                  # Article markdown files (to be created)
│   ├── decision_trees/            # Classification logic
│   ├── use_cases/                 # Real-world examples
│   └── glossary.md
│
├── tests/                          # ✅ Test Suite (to be created)
│   ├── unit/                      # Unit tests
│   ├── integration/               # End-to-end tests
│   └── fixtures/                  # Test data
│
├── docs/                           # 📖 User Documentation (to be created)
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   └── USER_GUIDE.md
│
├── config/                         # ⚙️ Configuration
│   ├── settings.yml
│   ├── agent_config.json
│   └── .env.example
│
├── scripts/                        # 🔨 Utility Scripts (to be created)
│   ├── setup.sh
│   ├── validate_kb.py
│   └── train_agent.py
│
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── pytest.ini                      # Test configuration
├── .gitignore
├── README.md                       # This file
└── LICENSE
```

---

## 🚀 How It Works

### 1. User Submits Questionnaire

Users (PM, Architect, Engineer) answer questions about their AI system via **MS Forms**, including:
- System name & purpose
- Data types processed
- Decision-making scope & autonomy
- Use case category (employment, law enforcement, etc.)
- Governance & oversight mechanisms

### 2. Questionnaire → Classification Agent

The questionnaire response is sent to the **AI Compliance Sherpa agent** which:
1. **Validates** the questionnaire
2. **Analyzes** system characteristics against EU AI Act articles
3. **Classifies** into one of 4 risk categories
4. **Explains** with article references and requirements
5. **Recommends** next steps & remediation (if needed)

### 3. Classification Report

User receives a detailed report including:
- **Risk Classification**: PROHIBITED | HIGH-RISK | LIMITED-RISK | MINIMAL-RISK
- **Confidence Score**: 0.0-1.0 (how confident is the classification)
- **Applicable Articles**: EU AI Act articles that apply with explanations
- **Compliance Obligations**: What must be done (based on risk level)
- **Remediation Roadmap**: Steps to address gaps (for high-risk systems)
- **Next Actions**: Immediate steps recommended

---

## 📖 Risk Classification at a Glance

| Classification | Definition | Examples | Required Actions |
|---|---|---|---|
| **🚫 PROHIBITED** | Violates fundamental rights | Subliminal manipulation, real-time facial recognition for law enforcement in public | Must not be deployed |
| **⚠️ HIGH-RISK** | Significant impact on rights/safety | HR screening, credit scoring, autonomous decisions | Impact assessment, human oversight, testing, documentation |
| **ℹ️ LIMITED-RISK** | Transparency concerns | Chatbots, deepfake detection | User disclosure of AI |
| **✅ MINIMAL-RISK** | All other AI systems | Recommendations, spam filtering | Proportionate approach |

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | OpenAI GPT-4 | Intelligent classification & reasoning |
| **LLM** | Azure OpenAI (GPT-4) | Intelligent classification & reasoning |
| **LLM Setup** | Azure OpenAI credentials | API key, endpoint, deployment name |
| **Agent Framework** | Microsoft AutoGen | Multi-turn agent orchestration |
| **Web Framework** | FastAPI | REST API for classification |
| **Validation** | Pydantic | Data validation & serialization |
| **Knowledge Management** | Markdown + in-memory context | EU AI Act knowledge base |
| **Testing** | pytest | Comprehensive test coverage |
| **Language** | Python 3.10+ | Development language |

---

## 📅 Development Timeline

| Phase | Duration | Focus | Deliverable |
|-------|----------|-------|-------------|
| **Phase 1: Foundation** | Weeks 1-2 | Project setup, KB, Agent initialization | Repository ready, first articles documented, agent callable |
| **Phase 2: Integration** | Week 3 | API, output formatting, MS Forms integration | End-to-end classification, reports working |
| **Phase 3: Refinement** | Week 4 | Testing, optimization, documentation | 95%+ accuracy, <20s latency, full docs |
| **Phase 4: Deployment** | Week 5 | Production setup, monitoring, launch | Live, monitored, team trained |

See [Implementation Guide - Section 6](specs/IMPLEMENTATION_GUIDE.md#6-implementation-phases) for detailed tasks.

---

## ✅ Success Metrics

| Metric | Target | Rationale |
|--------|--------|-----------|
| **Classification Accuracy** | 95%+ vs. expert review | Core reliability & trustworthiness |
| **Response Latency** | <30 seconds | User experience threshold |
| **False Negative Rate** | <2% (don't miss high-risk) | Safety-critical—miss high-risk = compliance risk |
| **Code Coverage** | >80% | Quality & maintainability |
| **User Satisfaction** | 4.0+/5.0 NPS | Adoption indicator |
| **Team Adoption** | 70%+ of new AI projects | Business impact within 3 months |

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Code style & standards
- Git workflow & PR process
- Testing requirements
- Documentation expectations

In brief:
- Branch: `feature/feature-name` from `develop`
- Commits: `[TYPE] Short description` (e.g., `[FEAT] Add risk classification`)
- Tests: Required before merge; >80% coverage
- Review: 2 approvals required

---

## 🔒 Security & Compliance

- All sensitive data encrypted (in transit: TLS; at rest: AES-256)
- No PII in logs; questionnaire responses anonymized
- API authentication via bearer tokens
- Audit trail of all classifications (for compliance)
- GDPR-compliant data retention (3 years)

See [Implementation Guide - Section 11](specs/IMPLEMENTATION_GUIDE.md#11-monitoring--observability) for observability details.

---

## 📞 Support & Escalation

| Issue Type | Channel | Response Time |
|---|---|---|
| **Technical Question** | Slack #ai-compliance-sherpa | 4 hours |
| **Bug Report** | GitHub Issue + Slack | 24 hours |
| **Legal/Compliance Question** | Legal Team Email | 2 business days |
| **Critical Production Issue** | On-call Engineer | 30 minutes |

---

## 📝 Key Documents at a Glance

### For Product/Business Stakeholders
1. Start: [Main Specification - Sections 1-3](specs/spec.en.md#1-problem-statement)
2. Then: [Quick Reference](specs/QUICK_REFERENCE.md)
3. Deep dive: [MS Forms Spec](specs/ms_forms_spec.md) (user requirements)

### For Architects/Tech Leads
1. Start: [Quick Reference](specs/QUICK_REFERENCE.md)
2. Then: [Agent Spec](specs/agent_spec.md) + [KB Spec](specs/knowledge_base_spec.md)
3. Build: [Implementation Guide - Section 2](specs/IMPLEMENTATION_GUIDE.md#2-repository-structure) (repo setup)

### For Engineers
1. Start: [Implementation Guide](specs/IMPLEMENTATION_GUIDE.md)
2. Code: Reference [Agent Spec](specs/agent_spec.md) & [KB Spec](specs/knowledge_base_spec.md)
3. Test: [IMPLEMENTATION_GUIDE - Section 7](specs/IMPLEMENTATION_GUIDE.md#7-code-standards--quality) (standards)

### For Legal/Compliance
1. **Legal Reference**: [EU AI Act Reference Framework](EU_AI_ACT_REFERENCE.md) - Comprehensive guide to articles, mapping, obligations, and how to keep current
2. Start: [Main Spec - Section 1 & 9](specs/spec.en.md#1-problem-statement)
3. KB Details: [Knowledge Base Spec](specs/knowledge_base_spec.md)
4. Accuracy: [Implementation Guide - Section 6](specs/IMPLEMENTATION_GUIDE.md#6-implementation-phases)

---

## 🎯 Next Steps

### Immediate (This Week)
- [ ] **Read specifications**: Team members review relevant specs above
- [ ] **Create branches**: Legal reviews compliance language
- [ ] **Schedule kickoff**: Team alignment meeting
- [ ] **Provision credentials**: OpenAI API key, Azure access

### Phase 1 (Weeks 1-2)
- [ ] Initialize repository structure
- [ ] Set up CI/CD pipeline
- [ ] Begin EU AI Act knowledge base documentation
- [ ] Implement AutoGen agent skeleton

See [IMPLEMENTATION_GUIDE - Section 13](specs/IMPLEMENTATION_GUIDE.md#13-next-immediate-actions) for detailed tasks.

---

## 📚 References

### EU AI Act & Regulatory
- **Official Regulation**: [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- **Commission Guidance**: [To be collected in knowledge_base/]

### Technology
- **AutoGen**: [microsoft/autogen](https://github.com/microsoft/autogen)
- **FastAPI**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **Pydantic**: [docs.pydantic.dev](https://docs.pydantic.dev)

---

## 📄 License

[Specify your license - e.g., MIT, Apache 2.0, etc.]

---

## 👥 Team

| Role | Name | Contact |
|------|------|---------|
| **Project Lead** | [Name] | [Email/Slack] |
| **Lead Engineer** | [Name] | [Email/Slack] |
| **AI/ML Engineer** | [Name] | [Email/Slack] |
| **Product Manager** | [Name] | [Email/Slack] |
| **Legal Advisor** | [Name] | [Email/Slack] |

---

## 📈 Status Board

**MVP Development Status**: 🟡 **IN PLANNING** (Phase 1 starts [date])

| Phase | Status | Progress | ETA |
|-------|--------|----------|-----|
| Phase 1: Foundation | 🟡 Planning | 0% | Week 1-2 |
| Phase 2: Integration | ⚪ Waiting | 0% | Week 3 |
| Phase 3: Refinement | ⚪ Waiting | 0% | Week 4 |
| Phase 4: Deployment | ⚪ Waiting | 0% | Week 5 |

---

## 🙏 Questions?

👉 **Start here**: Read [Quick Reference](specs/QUICK_REFERENCE.md) (5 min)

👉 **Still unclear**: Check [Specification Index](#📚-documentation) for detailed docs

👉 **Need help**: Post in Slack or create GitHub issue with `[QUESTION]` tag

---

**Document Version**: 1.0  
**Last Updated**: March 9, 2026
**Status**: DRAFT - Ready for team review  
**Next Review**: After team kickoff meeting