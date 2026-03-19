# AI Compliance Sherpa - Development Setup Guide

**Status**: MVP Project Initialization  
**Last Updated**: March 2026

---

## 1. Project Overview

**Project Name**: AI Compliance Sherpa MVP  
**Objective**: Build a single agentic system that classifies AI systems based on EU AI Act risk criteria  
**Methodology**: Specification-Driven Development (using GitHub Spec Kit)  
**Timeline**: 5 weeks (Phase 1-4)  
**Team Roles**: 
- 1 Lead Engineer
- 1 ML/AI Engineer  
- 1 Product Manager
- 1 Legal Advisor (part-time)

---

## 2. Repository Structure

```
hacknpulse/
├── specs/                          # Specification-driven development
│   ├── spec.en.md                 # Main system specification
│   ├── knowledge_base_spec.md     # EU AI Act KB structure
│   ├── agent_spec.md              # Agent architecture
│   ├── ms_forms_spec.md           # MS Forms integration
│   └── IMPLEMENTATION_GUIDE.md    # This file
│
├── src/                            # Source code
│   ├── sherpa/                    # Main agent module
│   │   ├── __init__.py
│   │   ├── agent.py               # AutoGen agent initialization
│   │   ├── config.py              # Configuration management
│   │   └── schemas.py             # Pydantic models for I/O
│   │
│   ├── api/                        # API layer
│   │   ├── __init__.py
│   │   ├── app.py                 # FastAPI application
│   │   ├── routes.py              # API endpoints
│   │   └── middleware.py          # Auth, logging, error handling
│   │
│   ├── extraction/                 # Input processing
│   │   ├── __init__.py
│   │   ├── validation.py          # Questionnaire validation
│   │   └── preprocessing.py       # JSON → agent input
│   │
│   ├── output/                     # Output generation
│   │   ├── __init__.py
│   │   ├── parser.py              # Parse agent response
│   │   ├── formatter.py           # JSON + Markdown formatting
│   │   └── report.py              # Report generation
│   │
│   ├── knowledge_base/             # EU AI Act knowledge
│   │   ├── __init__.py
│   │   ├── articles/              # Article markdown files
│   │   ├── use_cases/             # Use case examples
│   │   ├── decision_trees/        # Classification logic
│   │   └── loader.py              # KB initialization
│   │
│   ├── utils/                      # Utilities
│   │   ├── __init__.py
│   │   ├── logging.py             # Structured logging
│   │   ├── errors.py              # Custom exceptions
│   │   └── helpers.py             # Common functions
│   │
│   └── main.py                     # Entry point
│
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures
│   ├── unit/
│   │   ├── test_validation.py
│   │   ├── test_agent.py
│   │   ├── test_preprocessing.py
│   │   └── test_formatting.py
│   ├── integration/
│   │   ├── test_end_to_end.py
│   │   └── test_api.py
│   └── fixtures/                  # Test data
│       ├── sample_questionnaires.json
│       └── expected_outputs.json
│
├── docs/                           # Documentation
│   ├── API.md                     # API documentation
│   ├── ARCHITECTURE.md            # Architecture diagrams
│   ├── DEPLOYMENT.md              # Deployment guide
│   └── USER_GUIDE.md              # User documentation
│
├── knowledge_base/                 # EU AI Act knowledge (data)
│   ├── articles/
│   │   ├── article_05.md
│   │   ├── article_06.md
│   │   ├── [...articles 7-52...]
│   │   └── limited_risk_articles.md
│   ├── decision_trees/
│   │   └── risk_classification.md
│   ├── use_cases/
│   │   ├── high_risk_examples.md
│   │   ├── limited_risk_examples.md
│   │   └── compliant_systems.md
│   └── glossary.md
│
├── config/                         # Configuration files
│   ├── settings.yml               # App settings
│   ├── agent_config.json          # Agent configuration
│   └── .env.example               # Environment variables template
│
├── scripts/                        # Utility scripts
│   ├── setup.sh                   # Project initialization
│   ├── train_agent.py             # KB embedding (future)
│   └── validate_kb.py             # KB integrity check
│
├── docker/                         # Containerization
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .github/                        # GitHub configuration
│   ├── workflows/
│   │   ├── tests.yml
│   │   ├── lint.yml
│   │   └── deploy.yml
│   └── ISSUE_TEMPLATE/
│
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── pytest.ini                      # Pytest configuration
├── .gitignore
├── .env.example
├── README.md                       # Project README
├── CONTRIBUTING.md                 # Contribution guidelines
└── LICENSE

```

---

## 3. Prerequisites

### 3.1 System Requirements

- **Python**: 3.10+
- **OS**: Linux, macOS, or Windows with WSL2
- **RAM**: 8GB minimum (16GB recommended)
- **Disk**: 2GB free space

### 3.2 Software Requirements

- **Git**: version control
- **Docker**: containerization (optional but recommended)
- **VS Code** or **PyCharm**: code editor
- **Postman** or **curl**: API testing

### 3.3 API Keys & Credentials

- **OpenAI API Key**: GPT-4 access
- **Azure Tenant ID**: for MS Forms integration
- **Microsoft Graph API**: for Forms data retrieval
- **Environment**: `.env` file (see section 4)

---

## 4. Local Development Setup

### 4.1 Clone Repository

```bash
git clone https://github.com/yourorg/hacknpulse.git
cd hacknpulse
```

### 4.2 Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip
```

### 4.3 Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Install dev dependencies (for testing, linting)
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .
```

### 4.4 Configure Environment

```bash
# Copy template to .env
cp .env.example .env

# Edit .env with your credentials
nano .env
# Or in VS Code: code .env
```

**Required `.env` variables**:
```env
# OpenAI Configuration
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.2
OPENAI_MAX_TOKENS=2000

# Azure / MS Forms (if using)
AZURE_TENANT_ID=...
AZURE_CLIENT_ID=...
AZURE_CLIENT_SECRET=...

# Application Configuration
LOG_LEVEL=INFO
DEBUG=False
ENVIRONMENT=development

# Knowledge Base
KB_VERSION=1.0
KB_PATH=./knowledge_base/

# Security
API_SECRET_KEY=... (generate with: openssl rand -hex 32)

# Optional: Database
DATABASE_URL=sqlite:///./test.db
```

### 4.5 Verify Installation

```bash
# Test Python environment
python -c "import autogen; print(autogen.__version__)"

# Test OpenAI API connection
python -c "from openai import OpenAI; print('OpenAI available')"

# Run basic tests
pytest tests/unit/ -v
```

---

## 5. Development Dependencies

### 5.1 Core Dependencies (requirements.txt)

```txt
# LLM & Agent Framework
autogen-agentchat>=0.2.0
openai>=1.0.0

# Web Framework (if using API)
fastapi>=0.104.0
uvicorn>=0.24.0

# Data Validation & Serialization
pydantic>=2.0.0
pydantic-settings>=2.0.0
fastapi-azure-auth>=0.13.0  # For B2B auth (future)

# File & Data Processing
python-dotenv>=1.0.0
pyyaml>=6.0
json5>=0.9.0

# Utilities
tenacity>=8.0.0  # Retry logic
loguru>=0.7.0    # Structured logging

# Development & Testing
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-asyncio>=0.21.0
black>=23.0.0    # Code formatting
flake8>=6.0.0    # Linting
mypy>=1.0.0      # Type checking
```

### 5.2 Development Dependencies (requirements-dev.txt)

```txt
-r requirements.txt

# Testing
pytest-mock>=3.12.0
responses>=0.24.0

# Code Quality
pylint>=3.0.0
isort>=5.12.0
autopep8>=2.0.0

# Documentation
sphinx>=7.0.0
sphinx-rtd-theme>=1.3.0

# Debugging
ipython>=8.0.0
ipdb>=0.13.0

# Pre-commit hooks
pre-commit>=3.5.0
```

---

## 6. Implementation Phases

### Phase 1: Foundation (Weeks 1-2)

#### Week 1: Project Setup & Knowledge Base

**Tasks**:
- [x] Create project specifications (already done!)
- [ ] Set up GitHub repository with issue templates
- [ ] Initialize Python project structure
- [ ] Create knowledge base directory structure
- [ ] Begin documenting EU AI Act Articles (5-15)
- [ ] Set up CI/CD pipeline (GitHub Actions)

**Deliverables**:
- Repository with structure from section 2
- KB skeleton with Article 5 and 6 documented
- CI pipeline running tests on push

**Success Criteria**:
- All team members can clone and run `python -m pytest` successfully
- First set of articles added to KB  
- GitHub Actions pipeline validates code

---

#### Week 2: Agent & API Foundation

**Tasks**:
- [ ] Create AutoGen agent initialization code
- [ ] Implement questionnaire schema (Pydantic models)
- [ ] Create input validation module
- [ ] Set up basic FastAPI application
- [ ] Create agent system prompt with KB context
- [ ] Unit tests for validation & preprocessing

**Deliverables**:
- `src/sherpa/agent.py` - working AutoGen agent
- `src/extraction/validation.py` - questionnaire validator
- `src/api/app.py` - basic FastAPI app with POST endpoint
- Unit test coverage >80%

**Success Criteria**:
- Agent initializes without errors
- API endpoint accepts sample questionnaire
- Agent returns classification (any classification, bare minimum)

---

### Phase 2: Integration (Week 3)

**Tasks**:
- [ ] Complete EU AI Act knowledge base (all articles)
- [ ] Implement output parsing & formatting
- [ ] Create classification output schema
- [ ] Generate markdown reports
- [ ] Integrate MS Forms JSON export
- [ ] Write integration tests

**Deliverables**:
- Complete KB with all articles 5-52
- `src/output/formatter.py` - output formatting
- `src/output/parser.py` - agent response parsing
- Full integration test suite
- API returns JSON + markdown reports

**Success Criteria**:
- Agent classifies 10 test systems correctly
- Output format matches specification
- Reports are readable and match legal requirements
- Integration tests pass with >90% coverage

---

### Phase 3: Refinement & Testing (Week 4)

**Tasks**:
- [ ] Accuracy validation against expert classifications
- [ ] Performance optimization (response time <30s)
- [ ] Error handling & edge cases
- [ ] Comprehensive documentation
- [ ] UAT with sample AI projects
- [ ] Security review (API keys, logging, PII handling)

**Deliverables**:
- Accuracy report (95%+ agreement with experts)
- Performance benchmarks
- API documentation (OpenAPI/Swagger)
- User guide and troubleshooting
- Security audit results

**Success Criteria**:
- 95%+ classification accuracy vs. expert review
- Average response time <20 seconds
- All critical bugs resolved
- Zero security vulnerabilities found

---

### Phase 4: Deployment & Go-Live (Week 5)

**Tasks**:
- [ ] Set up production environments (dev, staging, prod)
- [ ] Configure CI/CD for releases
- [ ] Set up monitoring & alerting
- [ ] Create runbooks & operational procedures
- [ ] Team training & documentation
- [ ] Prepare launch communication

**Deliverables**:
- Production deployment ready
- Monitoring dashboard
- On-call runbooks
- Team training materials
- Launch communication to stakeholder teams

**Success Criteria**:
- Zero downtime deployment
- 99.5% uptime in first week  
- <5% of users report issues
- Adoption by >70% of new AI projects (target within 3 months)

---

## 7. Code Standards & Quality

### 7.1 Code Style

- **Language**: Python 3.10+ with type hints
- **Formatter**: Black (line length: 100)
- **Linter**: Flake8
- **Type Checker**: Mypy (strict mode)
- **Import Sorter**: isort

Setup pre-commit hook:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Manual run
pre-commit run --all-files
```

### 7.2 Code Organization

- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Functions**: Max 50 lines; single responsibility
- **Classes**: Cohesive, with clear interfaces
- **Docstrings**: Google style for all public functions
- **Comments**: Explain WHY, not WHAT

Example:

```python
def classify_system(
    questionnaire: Dict[str, Any],
    agent: AutogenAgent
) -> ClassificationResult:
    """
    Classify an AI system based on questionnaire responses.
    
    Args:
        questionnaire: Validated questionnaire data
        agent: Initialized AutoGen agent instance
    
    Returns:
        ClassificationResult with risk level and explanation
    
    Raises:
        ValidationError: If questionnaire is invalid
        AgentError: If agent fails to classify
    """
    # Preprocess questionnaire to natural language
    # (Agent works better with prose vs. JSON)
    narrative = preprocess_questionnaire(questionnaire)
    
    # Invoke agent
    response = agent.generate_reply(
        messages=[{"role": "user", "content": narrative}]
    )
    
    # Parse response to structured output
    result = parse_classification_output(response)
    
    return result
```

### 7.3 Error Handling

- **Custom Exceptions**: Define in `src/utils/errors.py`
- **Validation**: Use Pydantic models, not manual checks
- **Graceful Degradation**: Return detailed error responses
- **Logging**: All errors logged with context

```python
from src.utils.errors import QuestionnaireValidationError

try:
    result = validate_questionnaire(data)
except QuestionnaireValidationError as e:
    logger.error("Validation failed", extra={"errors": e.errors})
    raise HTTPException(status_code=400, detail={"errors": e.errors})
```

### 7.4 Testing Requirements

- **Unit Tests**: >80% code coverage (critical paths >95%)
- **Integration Tests**: All APIs tested end-to-end
- **Test Data**: Use fixtures (conftest.py)
- **Mocking**: Mock OpenAI API calls to avoid costs

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_questionnaire():
    return {
        "system_info": {"name": "Test System", ...},
        "data_processing": {"personal_data_processed": True, ...},
        ...
    }

@pytest.fixture
def mock_openai_agent(monkeypatch):
    def mock_generate_reply(messages):
        return {"content": "CLASSIFIED: HIGH_RISK"}
    
    monkeypatch.setattr(
        "src.sherpa.agent.AutogenAgent.generate_reply",
        mock_generate_reply
    )
```

---

## 8. Git Workflow

### 8.1 Branching Strategy

- **main**: Production-ready code; protected branch
- **develop**: Integration branch; staging environment
- **feature/{feature-name}**: Individual feature branches
- **bugfix/{bug-name}**: Bug fix branches
- **docs/{title}**: Documentation updates

### 8.2 Commit Messages

Format: `[TYPE] Short description`

Types:
- `[FEAT]` - New feature
- `[FIX]` - Bug fix
- `[DOCS]` - Documentation
- `[REFACTOR]` - Code restructuring
- `[TEST]` - Test additions/changes
- `[SPEC]` - Specification updates

Example:
```
[FEAT] Implement agent system prompt with EU AI Act knowledge base
[FIX] Handle ambiguous use case classification
[DOCS] Add API documentation
[TEST] Add unit tests for output parser
```

### 8.3 Pull Request Process

1. Create feature branch from `develop`
2. Make commits with descriptive messages
3. Push and create PR with description of changes
4. Link to specification/issue
5. Request review from at least 2 team members
6. Pass CI checks (tests, linting, type checking)
7. Squash merge to `develop` or `main`

### 8.4 Code Review Checklist

Reviewers verify:
- [ ] Code matches specification
- [ ] Tests included and passing
- [ ] Type hints present
- [ ] Documentation updated
- [ ] No hard-coded credentials
- [ ] Error handling appropriate
- [ ] Performance acceptable (for critical paths)

---

## 9. Documentation

### 9.1 Code Documentation

Every module should have:

```python
"""Module docstring explaining purpose and main exports."""

from src.extraction.validation import validate_questionnaire
from src.output.formatter import format_classification_result

__all__ = ["validate_questionnaire", "format_classification_result"]
```

### 9.2 Architecture Documentation

Create `docs/ARCHITECTURE.md` with diagrams:

```
[Questionnaire Input] 
        ↓
[Validation Layer]
        ↓
[Agent (AutoGen + LLM)]
        ↓
[Output Parser]
        ↓
[Report Generator]
        ↓
[API Response / Markdown Report]
```

### 9.3 API Documentation

Use FastAPI's auto-generated OpenAPI:
- Endpoint: `/docs` (Swagger UI)
- Endpoint: `/redoc` (ReDoc)
- Export: OpenAPI JSON at `/openapi.json`

### 9.4 User Documentation

Create `docs/USER_GUIDE.md` covering:
- How to fill out MS Forms questionnaire
- What each question means
- How to interpret results
- Next steps based on classification

---

## 10. Collaboration & Communication

### 10.1 Team Sync

- **Daily Standup**: 15 min (async in Slack or sync)
  - What done yesterday
  - What doing today  
  - Blockers

- **Weekly Planning**: 1 hour (Monday)
  - Review spec updates
  - Prioritize tasks for week
  - Discuss blockers

- **Bi-weekly Demo**: 30 min
  - Show progress to stakeholders
  - Gather feedback
  - Adjust plan as needed

### 10.2 Issue Tracking

Use GitHub Issues for:
- **Spec Issues**: Link to specific spec sections
- **Implementation Tasks**: Break into sprints
- **Bugs**: Title, reproduction steps, expected behavior
- **Documentation**: Content to add/update

Label system:
- `spec` - Specification updates
- `frontend` - UI/Forms
- `backend` - Core agent logic
- `testing` - Test additions
- `documentation` - Docs
- `high-priority` - Critical path
- `blocked` - Waiting on something
- `good-first-issue` - Onboarding tasks

### 10.3 Knowledge Sharing

- **Spec Review Sessions**: Weekly, review one spec document
- **Code Examples**: Document patterns (input validation, error handling)
- **Decision Log**: Record architectural decisions in [docs/ADR/](docs/ADR/)
- **FAQ**: Collect common questions in [docs/FAQ.md](docs/FAQ.md)

---

## 11. Monitoring & Observability

### 11.1 Structured Logging

Use `loguru` for structured logs:

```python
from loguru import logger

logger.info(
    "Classification completed",
    submission_id=submission_id,
    risk_classification=result.risk_classification,
    confidence_score=result.confidence_score,
    processing_time_ms=elapsed_time
)
```

### 11.2 Metrics to Track

Production metrics:
- **Latency**: P50, P95, P99 response times
- **Availability**: Uptime percentage
- **Accuracy**: Classification agreement rate
- **Cost**: API calls and costs per classification
- **Volume**: Classifications per day

### 11.3 Alerting

Set up alerts for:
- Response time > 30 seconds
- Error rate > 5%
- Failed API calls
- Timeout errors
- Cost spikes

---

## 12. Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: autogen` | Dependency not installed | `pip install -r requirements.txt` |
| `OpenAI API Error 401` | Invalid API key | Check `.env` OPENAI_API_KEY |
| `Agent returns empty response` | System prompt too long | Optimize KB size or use RAG |
| `Classification takes >30s` | Model is slow | Use smaller model or optimize prompts |
| `Test failures with AssertionError` | Output format changed | Check spec updates, update tests |

### Debug Mode

Enable verbose logging:

```bash
# In code
import logging
logging.basicConfig(level=logging.DEBUG)

# Or via environment
export LOG_LEVEL=DEBUG
```

Run with debugger:

```bash
# Using pdb
python -m pdb src/main.py

# Using PyCharm: Run → Debug
```

---

## 13. Next Immediate Actions

**This Week**:

1. [ ] Every team member: Read the 4 specification documents
2. [ ] Create GitHub repository and initialize project structure
3. [ ] Set up CI/CD pipeline (GitHub Actions)
4. [ ] Install dependencies locally and verify setup
5. [ ] Schedule weekly kickoff meeting to discuss questions

**Week 1 Deliverables**:
- [ ] Repository ready with all directories
- [ ] Issue labels and templates configured
- [ ] CI pipeline running (even if just linting)
- [ ] First EU AI Act articles documented in KB
- [ ] Agent initialization code started

**Success Metrics**:
- All team members can run `pytest tests/` successfully
- At least 3 team members familiar with all specs
- First 10 pull requests submitted and reviewed

---

## 14. Resources & References

### Official EU AI Act
- **Text**: [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- **Recitals**: Explanatory preamble
- **Guidance**: EU Commission documents (collected in knowledge_base/)

### AutoGen Documentation
- **GitHub**: [microsoft/autogen](https://github.com/microsoft/autogen)
- **Docs**: [Microsoft AutoGen](https://microsoft.github.io/autogen/)
- **Examples**: [AutoGen cookbook](https://github.com/microsoft/autogen/tree/main/notebook)

### Python & FastAPI
- **Python**: [python.org](https://python.org)
- **FastAPI**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **Pydantic**: [docs.pydantic.dev](https://docs.pydantic.dev)

### Development Tools
- **pytest**: [pytest.org](https://pytest.org)
- **Black Code Formatter**: [psf/black](https://github.com/psf/black)
- **VS Code**: [code.visualstudio.com](https://code.visualstudio.com)

---

## 15. Questions to Resolve with Team

- [ ] Which Azure region for deployment? (compliance, latency)
- [ ] Exact MS Forms questionnaire structure? (confirm section 2.2 of MS Forms spec)
- [ ] Who has access to file classifications? (control access to audit trail)
- [ ] Escalation process for expert legal review? (who, how often)
- [ ] Budget & cost limits for OpenAI API?
- [ ] Preferred observability platform? (DataDog, Prometheus, etc.)

---

**Document Status**: DRAFT - Ready for team review  
**Last Updated**: March 2026  
**Next Review**: After first week of development

