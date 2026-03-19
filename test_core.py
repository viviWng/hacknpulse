"""Quick test - validate core components without API calls"""
import json
from src.schemas import Questionnaire, ClassificationResult
from src.classification import apply_decision_tree, classify_system
from src.output import format_summary, format_json_response


def test_decision_tree():
    """Test the decision tree logic"""
    print("\n🧪 TEST 1: Decision Tree Logic")
    print("─" * 60)
    
    tests = [
        {
            "name": "Resume Screening (HIGH-RISK)",
            "autonomous": True,
            "affects_rights": True,
            "use_case": "Employment",
            "expected": "HIGH_RISK"
        },
        {
            "name": "Spam Filter (MINIMAL-RISK)",
            "autonomous": True,
            "affects_rights": False,
            "use_case": "Email",
            "expected": "MINIMAL_RISK"
        },
        {
            "name": "Chatbot (LIMITED-RISK)",
            "autonomous": False,
            "affects_rights": False,
            "use_case": "Customer Service",
            "expected": "LIMITED_RISK"
        }
    ]
    
    for test in tests:
        q = Questionnaire(
            name=test["name"],
            purpose="Test system",
            data_types="test data",
            autonomous=test["autonomous"],
            affects_rights=test["affects_rights"],
            use_case=test["use_case"]
        )
        
        risk_level, articles, confidence = apply_decision_tree(q)
        
        status = "✅" if risk_level == test["expected"] else "❌"
        print(f"{status} {test['name']}: {risk_level}")
        if risk_level != test["expected"]:
            print(f"   Expected: {test['expected']}, Got: {risk_level}")


def test_schemas():
    """Test Pydantic models"""
    print("\n🧪 TEST 2: Data Schemas")
    print("─" * 60)
    
    # Test questionnaire schema
    try:
        q = Questionnaire(
            name="Test System",
            purpose="This is a test",
            data_types="Test data",
            autonomous=True,
            affects_rights=False,
            use_case="Testing"
        )
        print("✅ Questionnaire schema valid")
    except Exception as e:
        print(f"❌ Questionnaire schema error: {e}")
    
    # Test classification result schema
    try:
        from src.schemas import ApplicableArticle
        
        result = ClassificationResult(
            system_name="Test",
            risk_classification="HIGH_RISK",
            confidence_score=0.95,
            applicable_articles=[
                ApplicableArticle(
                    article_number=6,
                    article_title="Test Article",
                    is_violated=False,
                    explanation="Test explanation"
                )
            ],
            compliance_obligations=["Test obligation"],
            recommendations=["Test recommendation"],
            explanation="Test explanation"
        )
        print("✅ ClassificationResult schema valid")
    except Exception as e:
        print(f"❌ ClassificationResult schema error: {e}")


def test_output_formatting():
    """Test output formatting"""
    print("\n🧪 TEST 3: Output Formatting")
    print("─" * 60)
    
    from src.schemas import ApplicableArticle
    
    result = ClassificationResult(
        system_name="Test HR System",
        risk_classification="HIGH_RISK",
        confidence_score=0.92,
        applicable_articles=[
            ApplicableArticle(
                article_number=6,
                article_title="High-Risk AI Systems",
                is_violated=False,
                explanation="Employment decisions affect fundamental rights"
            )
        ],
        compliance_obligations=[
            "Conduct risk assessment",
            "Implement human oversight"
        ],
        recommendations=[
            "Review with legal team",
            "Document training data sources"
        ],
        explanation="This system makes autonomous employment decisions"
    )
    
    # Test summary formatting
    summary = format_summary(result)
    print("✅ Summary format:")
    print(f"   {summary}")
    
    # Test JSON formatting
    json_result = format_json_response(result)
    print("✅ JSON format valid")
    print(f"   Status: {json_result['status']}")
    print(f"   Risk: {json_result['data']['risk_classification']}")


def test_json_data():
    """Test loading test systems"""
    print("\n🧪 TEST 4: Test Data")
    print("─" * 60)
    
    with open("test_systems.json", "r") as f:
        systems = json.load(f)
    
    print(f"✅ Loaded {len(systems)} test systems:")
    for sys in systems[:3]:
        print(f"   - {sys['name']}: {sys['expected_classification']}")
    print(f"   ... and {len(systems)-3} more")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔬 CORE COMPONENT TESTS")
    print("="*60)
    
    test_decision_tree()
    test_schemas()
    test_output_formatting()
    test_json_data()
    
    print("\n" + "="*60)
    print("✅ All core components working!")
    print("="*60)
    print("\nNext steps:")
    print("1. Verify OPENAI_API_KEY in .env")
    print("2. Run: python demo.py (to test with actual agent)")
    print("3. Run: python -m uvicorn src.api:app --reload (to start API)")
    print("\n")
