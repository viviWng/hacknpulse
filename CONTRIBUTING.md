# Contributing to AI Compliance Sherpa

Thank you for contributing to the AI Compliance Sherpa project! This guide ensures consistency and quality across the codebase.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Submitting Changes](#submitting-changes)
- [Testing](#testing)
- [Documentation](#documentation)

---

## Code of Conduct

- **Respect**: Treat all team members with respect
- **Inclusivity**: Assume good intent and communicate clearly
- **Quality**: Raise standards through constructive feedback
- **Compliance**: Remember our mission: compliance is a speed enabler, not a blocker

---

## Getting Started

### 1. Fork & Clone

```bash
git clone https://github.com/yourorg/hacknpulse.git
cd hacknpulse
```

### 2. Set Up Environment

Follow [Development Setup Guide](specs/IMPLEMENTATION_GUIDE.md#4-local-development-setup):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming:
- `feature/feature-name` - New features
- `bugfix/bug-name` - Bug fixes
- `docs/documentation-title` - Documentation updates
- `spec/spec-update` - Specification changes

### 4. Make Changes & Commit

Commit message format: `[TYPE] Short description`

Types:
- `[FEAT]` - New feature
- `[FIX]` - Bug fix
- `[DOCS]` - Documentation
- `[TEST]` - Test additions
- `[REFACTOR]` - Code restructuring
- `[SPEC]` - Specification updates

Examples:
```bash
git commit -m "[FEAT] Implement questionnaire validation"
git commit -m "[FIX] Handle ambiguous use case classification"
git commit -m "[TEST] Add unit tests for output parser"
```

---

## Development Workflow

### 1. Pre-Commit Checks

Run these before committing:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint
flake8 src/ tests/

# Type check
mypy src/ --strict

# Run tests
pytest tests/ -v --cov=src
```

Or use pre-commit hook:

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### 2. Push to Remote

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

1. Go to GitHub and create PR
2. Link to specification section relevant to your work
3. Link to GitHub issue(s) being addressed
4. Describe what changed and why
5. Add screenshots/examples if applicable
6. Ensure CI checks pass

PR template:

```markdown
## Description
Brief description of changes

## Specification Reference
Links to relevant specification sections

## Related Issues
Closes #123

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Code refactor

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Tests pass locally
```

### 4. Code Review

- At least 2 approvals required
- Address all comments before merging
- Ping reviewers if blocked

### 5. Merge

- Squash commits for cleaner history
- Merge to `develop` (or `main` if hotfix)
- Delete feature branch

---

## Code Standards

### Python Style

Follow [PEP 8](https://pep8.org/) with Black formatting:

```python
# ✅ Good
def validate_questionnaire(
    questionnaire: Dict[str, Any],
    strict_mode: bool = True
) -> Tuple[bool, List[str]]:
    """
    Validate questionnaire against schema.
    
    Args:
        questionnaire: Questionnaire data to validate
        strict_mode: If True, enforce all requirements
    
    Returns:
        Tuple of (is_valid, error_messages)
    
    Raises:
        ValidationError: If critical fields missing
    """
    errors = []
    
    # Validate required fields
    for field in REQUIRED_FIELDS:
        if field not in questionnaire:
            errors.append(f"Missing required field: {field}")
    
    return len(errors) == 0, errors


# ❌ Bad
def validate(q):
    """Validates questionnaire."""
    e = []
    for f in ["name", "purpose"]:
        if f not in q:
            e.append(f"Missing {f}")
    return len(e) == 0, e
```

### Type Hints

Always include type hints:

```python
# ✅ Good
from typing import Dict, List, Tuple, Optional

def process_data(
    data: Dict[str, Any],
    verbose: bool = False
) -> Optional[Dict[str, Any]]:
    """Process data and return result."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def classify_system(
    questionnaire: Dict[str, Any],
    agent: AutogenAgent
) -> ClassificationResult:
    """
    Classify an AI system based on questionnaire.
    
    This function analyzes system characteristics and returns
    a risk classification (PROHIBITED, HIGH-RISK, etc.) with
    detailed explanations referencing EU AI Act articles.
    
    Args:
        questionnaire: Validated questionnaire from MS Forms
        agent: Initialized Sherpa agent instance
    
    Returns:
        ClassificationResult containing:
            - risk_classification: One of 4 categories
            - confidence_score: 0.0-1.0
            - applicable_articles: List of article IDs
            - compliance_obligations: Required actions
    
    Raises:
        ValidationError: If questionnaire is invalid
        AgentError: If classification fails
    
    Example:
        >>> result = classify_system(questionnaire, agent)
        >>> print(f"Risk: {result.risk_classification}")
        >>> print(f"Confidence: {result.confidence_score}")
    """
    ...
```

### Comments

Explain *why*, not *what*:

```python
# ✅ Good - explains why
# Use confidence <0.85 as threshold because legal review 
# becomes necessary at higher risk levels
if confidence_score < 0.85:
    result['expert_review_recommended'] = True

# ❌ Bad - just restates code
# Check if confidence is less than 0.85
if confidence_score < 0.85:
    result['expert_review_recommended'] = True
```

---

## Testing

### Test Organization

```
tests/
├── unit/
│   ├── test_validation.py
│   ├── test_agent.py
│   ├── test_preprocessing.py
│   └── test_formatting.py
├── integration/
│   ├── test_end_to_end.py
│   └── test_api.py
└── fixtures/
    └── sample_questionnaires.json
```

### Writing Tests

```python
# tests/unit/test_validation.py
import pytest
from src.extraction.validation import validate_questionnaire

class TestQuestionnaireValidation:
    """Test questionnaire validation logic."""
    
    def test_valid_questionnaire_returns_true(self):
        """Valid questionnaire should pass validation."""
        valid_q = {
            "system_info": {"name": "Test System", "purpose": "Test"},
            "data_processing": {"personal_data_processed": True},
            # ... other required fields
        }
        is_valid, errors = validate_questionnaire(valid_q)
        assert is_valid is True
        assert len(errors) == 0
    
    def test_missing_required_field_returns_false(self):
        """Questionnaire missing required field should fail."""
        invalid_q = {"system_info": {"name": "Test System"}}
        # Missing 'purpose' field
        is_valid, errors = validate_questionnaire(invalid_q)
        assert is_valid is False
        assert any("purpose" in error for error in errors)
    
    def test_invalid_enum_value(self):
        """Invalid enum value should be caught."""
        invalid_q = {
            "use_case_category": "INVALID_CATEGORY",
            # ... other fields
        }
        is_valid, errors = validate_questionnaire(invalid_q)
        assert is_valid is False
        assert any("use_case_category" in error for error in errors)


# Use fixtures for common test data
@pytest.fixture
def sample_hr_questionnaire():
    """Sample HR system questionnaire."""
    return {
        "system_info": {
            "name": "Resume Screening System",
            "purpose": "Screen resumes for hiring"
        },
        "use_case_category": "EMPLOYMENT",
        # ... full questionnaire
    }


def test_hr_system_classified_as_high_risk(sample_hr_questionnaire):
    """HR system should be classified as HIGH-RISK."""
    result = classify_system(sample_hr_questionnaire, mock_agent)
    assert result.risk_classification == "HIGH_RISK"
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_validation.py

# Run specific test function
pytest tests/unit/test_validation.py::TestQuestionnaireValidation::test_valid_questionnaire_returns_true

# Run tests matching pattern
pytest tests/ -k "validation"

# Show print statements during tests
pytest tests/ -s
```

### Coverage Requirements

- **Minimum**: 80% overall
- **Critical paths**: 95%+ (validation, classification logic)
- **Utils**: 70%+ acceptable

Check coverage:

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

---

## Documentation

### Update Specification If Necessary

If changes affect requirements:
1. Update relevant specification file in `specs/`
2. Include in PR description
3. Get legal review if compliance-related

### Update API Documentation

If adding/modifying API endpoints:

```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/api/v1/classify-ai-system")
async def classify_ai_system(questionnaire: QuestionnaireRequest):
    """
    Classify an AI system based on EU AI Act criteria.
    
    ## Request
    
    JSON questionnaire with system characteristics
    
    ## Response
    
    Classification result with risk level and compliance guidance
    
    ## Example
    
    ```bash
    curl -X POST https://api.company.com/v1/classify-ai-system \\
      -H "Content-Type: application/json" \\
      -d @questionnaire.json
    ```
    
    ## Status Codes
    
    - 200: Classification successful
    - 400: Invalid questionnaire
    - 429: Rate limit exceeded
    """
    ...
```

### Update README/Code Comments

- Update [README.md](README.md) if project-level changes
- Keep specification references current
- Update [IMPLEMENTATION_GUIDE.md](specs/IMPLEMENTATION_GUIDE.md) for process changes

---

## Common Patterns

### Input Validation Pattern

```python
from pydantic import BaseModel, Field, validator

class QuestionnaireRequest(BaseModel):
    """Request model for classification API."""
    
    system_name: str = Field(..., min_length=3, max_length=100)
    purpose: str = Field(..., min_length=20)
    use_case: str
    
    @validator('use_case')
    def validate_use_case(cls, v):
        valid_cases = ["EMPLOYMENT", "LAW_ENFORCEMENT", ...]
        if v not in valid_cases:
            raise ValueError(f"Invalid use case: {v}")
        return v
```

### Error Handling Pattern

```python
from src.utils.errors import QuestionnaireValidationError

try:
    result = validate_questionnaire(data)
except QuestionnaireValidationError as e:
    logger.error("Validation failed", extra={"errors": e.errors})
    raise HTTPException(
        status_code=400,
        detail={"error_code": "VALIDATION_FAILED", "errors": e.errors}
    )
except Exception as e:
    logger.exception("Unexpected error during validation")
    raise HTTPException(status_code=500, detail="Internal server error")
```

### Logging Pattern

```python
from loguru import logger

def classify_system(questionnaire):
    logger.info(
        "Classification started",
        submission_id=submission_id,
        system_name=questionnaire['system_info']['name']
    )
    
    try:
        result = agent.classify(questionnaire)
        logger.info(
            "Classification completed",
            submission_id=submission_id,
            risk_classification=result.risk_classification,
            confidence_score=result.confidence_score
        )
        return result
    except Exception as e:
        logger.error(
            "Classification failed",
            submission_id=submission_id,
            error=str(e),
            exc_info=True
        )
        raise
```

---

## Checklist Before Submitting PR

- [ ] Code passes `black`, `flake8`, `mypy`
- [ ] All tests pass: `pytest tests/ --cov`
- [ ] Coverage >80% (or >95% for critical paths)
- [ ] Type hints on all functions
- [ ] Docstrings written (Google style)
- [ ] No hardcoded secrets/API keys
- [ ] Comments explain *why*, not *what*
- [ ] No unnecessary imports
- [ ] Variable names are descriptive
- [ ] Functions are <50 lines
- [ ] Specification updated (if needed)
- [ ] Related GitHub issue linked
- [ ] PR description is clear and detailed

---

## Getting Help

- **Questions**: Post in Slack #ai-compliance-sherpa
- **Blocked on spec**: Comment in GitHub issue
- **Code review feedback**: Ask for clarification
- **Unsure about approach**: Discuss before coding

---

## Code Review Feedback Examples

### Giving Feedback

```markdown
## Comment: Input Validation
I noticed the validation function doesn't check for null values. 
Can we add that? Reference: [spec.en.md Section 5.1](specs/spec.en.md#51-functional-requirements)

Suggested fix:
```python
if questionnaire is None:
    raise ValidationError("Questionnaire cannot be null")
```
```

### Receiving Feedback

```markdown
Good point! I'll add null check. I see this is important because
the spec requires handling edge cases gracefully.

Updated in commit [hash]: Added null value validation
```

---

## Questions?

1. Check [IMPLEMENTATION_GUIDE.md](specs/IMPLEMENTATION_GUIDE.md) - Development Setup
2. Check specifications - Design decisions
3. Ask in Slack - Team will help
4. Create GitHub Issue - Document for future reference

Thank you for contributing! 🚀

---

**Last Updated**: March 9, 2026  
**Status**: DRAFT - Ready for team review
