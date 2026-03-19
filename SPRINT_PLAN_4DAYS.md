# 4-Day MVP Sprint Plan (March 9-13, 2026)

**Goal**: Demonstrate working AI Compliance Sherpa agent with EU AI Act classification  
**Timeline**: Monday (now) → Thursday demo  
**Scope**: Minimum viable for impressive demo

---

## ⚡ MVP Scope (Phase 1 Only)

### ✅ MUST HAVE (For Demo)
- [x] 3-5 pre-classified test AI systems (for validation)
- [ ] AutoGen agent initialized with system prompt
- [ ] EU AI Act Articles 5, 6 documented in knowledge base
- [ ] Risk classification logic (decision tree)
- [ ] Basic Python API (FastAPI or Flask)
- [ ] Single API endpoint: `/classify` (accepts questionnaire JSON)
- [ ] Classification output (JSON + markdown report)
- [ ] Demo notebook or script showing end-to-end flow

### 🎯 NICE TO HAVE (If time allows)
- [ ] All Articles 7-15, 50-52 documented
- [ ] Comprehensive questionnaire validation
- [ ] Confidence scoring
- [ ] Full error handling
- [ ] Unit tests

### ❌ SKIP FOR NOW (Post-MVP)
- [ ] MS Forms integration (use JSON files for now)
- [ ] Database/persistence
- [ ] Production deployment
- [ ] Monitoring/alerting
- [ ] Full documentation

---

## 📅 4-Day Sprint Breakdown

### MONDAY (TODAY) - Setup & Core Agent (8 hours)

#### Morning (9am-12pm)
```
□ 30 min: Team sync on prioritized scope
          - Confirm what demo should show
          - Assign tasks
          - Identify blockers

□ 30 min: Create GitHub repo (if not done)
          - Clone to local
          - Create basic structure: src/, tests/, knowledge_base/
          - Push initial commit

□ 2 hours: Set up Python environment
          - Virtual environment
          - Install: autogen, openai, fastapi, uvicorn, pydantic
          - Create requirements.txt
```

#### Afternoon (1pm-5pm)
```
□ 1 hour: Create AutoGen agent skeleton
          File: src/sherpa/agent.py
          - Initialize ConversableAgent
          - Basic system prompt (use from spec.en.md)
          - LLM configuration
          - Single function: classify_system()

□ 2 hours: Create test data
          File: knowledge_base/articles/
          - Article 5 (Prohibited): 1-2 paragraphs
          - Article 6 (High-Risk): 1-2 paragraphs
          - Quick examples for each

□ 1 hour: Create input schema
          File: src/schemas.py
          - Pydantic models for questionnaire
          - Minimal required fields only
          - Keep it simple (10-15 fields max)
```

#### End of Day
```
✅ Agent initializes & can be called
✅ Knowledge base skeleton in place
✅ Input schema defined
```

---

### TUESDAY - API & Classification Logic (8 hours)

#### Morning (9am-12pm)
```
□ 1.5 hours: Create FastAPI app
          File: src/api.py
          - Simple POST endpoint: /classify
          - Input: questionnaire JSON
          - Output: classification result
          - Just a shell, logic comes next

□ 1 hour: Create classification logic
          File: src/classification.py
          - Decision tree for PROHIBITED check
          - Decision tree for HIGH-RISK check
          - Return risk category + articles that apply
          - Keep it rule-based for now (no LLM for classification)

□ 30 min: Integrate agent into API
          - Call agent to generate explanation
          - Format output
```

#### Afternoon (1pm-5pm)
```
□ 1.5 hours: Create output formatter
          File: src/output.py
          - Format classification as markdown report
          - Include articles referenced
          - Include recommendations
          - Keep it concise

□ 1.5 hours: Test manually
          - Run agent with 3 test systems
          - Verify outputs make sense
          - Debug/fix issues

□ 1 hour: Create demo script
          File: demo.py
          - Load test questionnaires
          - Call API endpoint
          - Display results
```

#### End of Day
```
✅ API endpoint functional
✅ Can classify simple systems
✅ Outputs reasonable explanations
✅ Demo script runs
```

---

### WEDNESDAY - Refinement & Knowledge Base (8 hours)

#### Morning (9am-12pm)
```
□ 2 hours: Expand knowledge base
          - Add all Articles 5-15 (summaries, not full)
          - Annex I: High-risk use cases (20 bullet points)
          - Decision tree logic in article docs
          - Real-world examples (employment, healthcare, etc.)

□ 1 hour: Improve system prompt
          - Use knowledge base in context
          - Better article references
          - Cleaner output formatting
```

#### Afternoon (1pm-5pm)
```
□ 2 hours: Test with 5-10 sample systems
          - HR screening system (HIGH-RISK expected)
          - Chatbot (LIMITED-RISK expected)
          - Spam filter (MINIMAL-RISK expected)
          - Facial recognition law enforcement (PROHIBITED)
          - Credit scoring (HIGH-RISK)

□ 1.5 hours: Improve accuracy
          - Adjust system prompt if classifications wrong
          - Add more decision tree rules
          - Test again

□ 1.5 hours: Polish outputs
          - Better markdown formatting
          - Clearer explanations
          - Remove jargon where possible
```

#### End of Day
```
✅ Knowledge base comprehensive enough for demo
✅ Agent classifies accurately on test systems
✅ Outputs are polished & readable
✅ Demo showcases different risk levels
```

---

### THURSDAY (DEMO DAY) - Final Polish & Presentation (4 hours)

#### Morning (9am-12pm)
```
□ 30 min: Final testing
          - Run demo script end-to-end
          - All 10 test systems pass
          - No errors or warnings

□ 1 hour: Create demo presentation
          - Show 1 example of each risk level (4 examples total)
          - Walk through: Input → Classification → Output
          - Show knowledge base / articles referenced
          - Show confidence/reasoning

□ 1.5 hours: Document for team
          - Quick start guide (5 steps to run demo)
          - test_systems.json (all 10 test cases)
          - README with results
```

#### Presentation (2pm)
```
DEMO FLOW (15-20 minutes):

1. (2 min) Show the problem
   - "AI systems need compliance assessment"
   
2. (2 min) Show how it works
   - "Questionnaire → Agent → Classification"

3. (10 min) LIVE DEMO - Classify 4 systems
   - System 1: HR Screening → HIGH-RISK ✅
   - System 2: Chatbot → LIMITED-RISK ✅
   - System 3: Spam Filter → MINIMAL-RISK ✅
   - System 4: Facial Recognition LEA → PROHIBITED ✅

4. (3 min) Show output quality
   - Markdown report with articles cited
   - Clear compliance obligations listed
   - Actionable recommendations

5. (3 min) Ask for Feedback
   - "How should we refine this?"
   - "What's missing?"
   - "Next steps?"
```

---

## 🎯 Success Criteria for Thursday Demo

Your team will be impressed if:

✅ **Agent works** - Can classify systems without errors  
✅ **Accurate** - Gets expected classification for test systems  
✅ **Explainable** - Shows which articles apply & why  
✅ **Polished** - Outputs are readable, professional  
✅ **Live** - Demo runs in front of them (not a video)  
✅ **Understandable** - Team can see the value immediately  

---

## 📋 Task Assignments (Suggest to Team)

If team can help with parallel work:

| Task | Owner | Deadline | Notes |
|------|-------|----------|-------|
| AutoGen agent setup & system prompt | Lead Engineer | EOD Monday | Critical path |
| FastAPI endpoint | Backend Engineer | EOD Monday | Blocked by agent |
| EU AI Act knowledge base (Articles 5-6) | Legal/Tech Lead | EOD Tuesday | Can run in parallel |
| Classification logic & decision trees | ML/Tech Lead | EOD Tuesday | Can run in parallel |
| Test systems & validation | PM + Engineer | EOD Wednesday | 10 realistic examples |
| Demo presentation & polish | Lead | Thursday AM | Final touch |

---

## 🔧 Technology Choices (For Speed)

Keep it simple for 4 days:

| Component | Choice | Why | Complexity |
|-----------|--------|-----|-----------|
| **LLM** | GPT-4 | Best accuracy for legal reasoning | Low (API key) |
| **Agent** | AutoGen | Easy setup, good control | Low |
| **API** | FastAPI | Fast to code, auto docs | Low |
| **Knowledge** | Markdown files | No DB, version control friendly | Low |
| **Testing** | Manual + JSON | No pytest setup needed yet | Low |
| **Deployment** | Local/Colab | Demo only, not prod | Extra low |

**Total setup time**: ~30 minutes

---

## 📂 Minimal File Structure

```
hacknpulse/
├── src/
│   ├── __init__.py
│   ├── agent.py              # AutoGen agent
│   ├── api.py                # FastAPI app
│   ├── classification.py      # Decision logic
│   ├── output.py             # Formatting
│   └── schemas.py            # Pydantic models
│
├── knowledge_base/
│   ├── articles/
│   │   ├── article_05.md     # Prohibited
│   │   ├── article_06.md     # High-Risk definition
│   │   ├── article_09.md     # Risk assessment
│   │   └── [...more articles...]
│   └── annex_i.md            # High-risk use cases
│
├── demo.py                    # Demo script (run this Thursday)
├── test_systems.json          # 10 test questionnaires
├── requirements.txt           # Dependencies
└── README.md                  # Quick start guide
```

---

## 💻 Exact Code to Start (Copy-Paste Ready)

### File: requirements.txt
```
autogen-agentchat>=0.2.0
openai>=1.0.0
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0
python-dotenv>=1.0.0
```

### File: src/agent.py
```python
"""AutoGen Sherpa Agent"""
import os
from autogen import ConversableAgent

SYSTEM_PROMPT = """
You are the AI Compliance Sherpa, an expert in EU AI Act compliance.

Your role: Classify AI systems by risk level (PROHIBITED, HIGH-RISK, LIMITED-RISK, MINIMAL-RISK)

Key Knowledge:
- Article 5: Prohibited practices (subliminal manipulation, social scoring, etc.)
- Article 6: High-Risk definition (affects fundamental rights, autonomous decisions)
- Annex I: High-risk use cases (HR, law enforcement, education, credit, etc.)

Your Output Format:
1. Risk Classification: [ONE OF ABOVE]
2. Confidence: [0.0-1.0]
3. Applicable Articles: [List article numbers]
4. Explanation: [Why this classification]
5. Required Actions: [What they must do]
"""

class SherpaAgent:
    def __init__(self):
        self.agent = ConversableAgent(
            name="sherpa",
            system_message=SYSTEM_PROMPT,
            llm_config={
                "config_list": [{
                    "model": "gpt-4",
                    "api_key": os.getenv("OPENAI_API_KEY")
                }],
                "temperature": 0.2,
                "max_tokens": 2000
            },
            human_input_mode="NEVER"
        )
    
    def classify(self, system_description: str) -> str:
        """Classify an AI system"""
        message = {
            "role": "user",
            "content": system_description
        }
        response = self.agent.generate_reply(messages=[message])
        return response
```

### File: src/api.py
```python
"""FastAPI Application"""
from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import SherpaAgent

app = FastAPI(title="AI Compliance Sherpa")
agent = SherpaAgent()

class Questionnaire(BaseModel):
    name: str
    purpose: str
    data_types: str
    autonomous: bool
    affects_rights: bool
    use_case: str

@app.post("/classify")
async def classify_system(questionnaire: Questionnaire):
    """Classify an AI system"""
    
    # Convert to natural language
    prompt = f"""
    AI System: {questionnaire.name}
    Purpose: {questionnaire.purpose}
    Data: {questionnaire.data_types}
    Autonomous: {questionnaire.autonomous}
    Affects Rights: {questionnaire.affects_rights}
    Use Case: {questionnaire.use_case}
    
    Classify this system under EU AI Act.
    """
    
    # Get classification
    result = agent.classify(prompt)
    
    return {
        "system_name": questionnaire.name,
        "classification": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### File: test_systems.json
```json
[
  {
    "name": "Resume Screening for HR",
    "purpose": "Filter job candidates based on qualifications",
    "data_types": "Names, education, work history",
    "autonomous": true,
    "affects_rights": true,
    "use_case": "Employment",
    "expected_classification": "HIGH-RISK"
  },
  {
    "name": "Customer Service Chatbot",
    "purpose": "Answer customer questions automatically",
    "data_types": "Chat transcripts",
    "autonomous": true,
    "affects_rights": false,
    "use_case": "Conversational AI",
    "expected_classification": "LIMITED-RISK"
  },
  {
    "name": "Email Spam Detector",
    "purpose": "Filter spam emails automatically",
    "data_types": "Email content",
    "autonomous": true,
    "affects_rights": false,
    "use_case": "Content filtering",
    "expected_classification": "MINIMAL-RISK"
  },
  {
    "name": "Facial Recognition for Border Control",
    "purpose": "Identify individuals at borders",
    "data_types": "Biometric data (faces)",
    "autonomous": true,
    "affects_rights": true,
    "use_case": "Law enforcement",
    "expected_classification": "PROHIBITED (or HIGH-RISK if approval process in place)"
  },
  {
    "name": "Credit Scoring Algorithm",
    "purpose": "Determine creditworthiness",
    "data_types": "Financial history, income, debt",
    "autonomous": false,
    "affects_rights": true,
    "use_case": "Financial services",
    "expected_classification": "HIGH-RISK"
  }
]
```

### File: demo.py
```python
"""Demo script - Run this Thursday"""
import json
import requests
from src.api import app
from fastapi.testclient import TestClient

# Test with direct API
client = TestClient(app)

# Load test systems
with open("test_systems.json") as f:
    test_systems = json.load(f)

print("=" * 60)
print("AI COMPLIANCE SHERPA - MVP DEMO")
print("=" * 60)

for system in test_systems[:4]:  # Show 4 for demo
    print(f"\n📋 System: {system['name']}")
    print(f"Expected: {system['expected_classification']}")
    print("-" * 60)
    
    # Call API
    response = client.post("/classify", json=system)
    result = response.json()
    
    print(f"✅ Classification: {result['classification']}")
    print("-" * 60)

print("\n🎉 Demo complete!")
```

---

## ⚡ Speed Hacks (To Save Time)

1. **Use GPT-4 for explanations** - Don't write them manually
2. **Hardcode decision logic** - Use if/elif rules, not ML
3. **Test with 10 examples** - Not 100+ (good enough for MVP demo)
4. **Skip error handling** - Demo happy path only
5. **Keep UI minimal** - JSON input/output is fine
6. **Use OpenAI API directly** - Faster than building full pipeline
7. **Markdown reports manually** - Template + format strings
8. **Skip tests** - Manual testing ok for demo

---

## 📞 Questions to Answer Before You Start

Ask your team:

1. **LLM Access**: Do you have OpenAI API key + quota?
2. **Scope**: "Can we just show 4-5 classified systems?" (not full form)
3. **Knowledge**: "Should we include all articles or focus on 5-6?" (5-6 for speed)
4. **Accuracy**: "What confidence level do we target?" (70%+ is ok for MVP)
5. **Demo style**: "Live coding or pre-recorded?" (Live is more impressive)

---

## 🎬 Thursday Demo Script (Read This)

```
"Hi team, thank you for supporting this project. 
Today I want to show you a working MVP of the AI Compliance Sherpa.

[SHOW PROBLEM]
Currently, our AI teams struggle to understand whether their systems 
comply with EU AI Act. We want to help them get answers in minutes, not weeks.

[SHOW SOLUTION]
Here's a simple agent that takes a description of an AI system and 
classifies it by risk level: PROHIBITED, HIGH-RISK, LIMITED-RISK, or MINIMAL-RISK.

[LIVE DEMO - Run demo.py]
Let me show you 4 examples:

Example 1: HR Resume Screening
→ System classifies as HIGH-RISK ✅
→ Why? Affects fundamental right to work, autonomous decision-making
→ What to do? Conduct risk assessment, implement human oversight

Example 2: Customer Service Chatbot  
→ System classifies as LIMITED-RISK ✅
→ Why? Transparency only - user needs to know they're talking to AI
→ What to do? Add disclosure and escalation path to humans

Example 3: Spam Filter
→ System classifies as MINIMAL-RISK ✅
→ Why? Low impact, no decisions affecting individuals
→ What to do? Proportionate risk management

Example 4: Border Facial Recognition
→ System classifies as HIGH-RISK/PROHIBITED ⚠️
→ Why? Real-time facial recognition by law enforcement is prohibited/heavily restricted
→ What to do? Legal review required, may need exemptions

[ASK FOR FEEDBACK]
This is an MVP - what would make it more useful?
- More detailed explanations?
- Integration with MS Forms?
- Specific articles we're missing?
- Better UI?

Next steps:
- [If positive] Let's refine and integrate with MS Forms
- [If concerned] Let's gather feedback and iterate
"
```

---

## ✅ Final Checklist (Thursday 10am)

Before presenting:

```
□ Agent files created & importable (no syntax errors)
□ API endpoint responds to requests
□ 4 demo systems classified (correct categories)
□ Knowledge base visible (can show article references)
□ demo.py runs without errors
□ Team contacted with time/location
□ Have slides or notes for talking points
□ Backup: Have screen recording just in case
□ Know fallback demo (show code, not just results)
```

---

## 🚀 After Thursday Demo

**If positive feedback**: Proceed with Phase 2 (Week 1-5 from main spec)  
**If concerns**: Address them, iterate for 1-2 days  
**If blockers**: Document and plan Phase 1 improvements

---

**Start NOW**: Copy code above, create files, get OpenAI key working.  
**By EOD Monday**: Agent initialized + API responds  
**By EOD Tuesday**: Can classify 5+ systems  
**By EOD Wednesday**: Outputs polished & demo-ready  
**Thursday 2pm**: wow your team!

Good luck! 🎯
