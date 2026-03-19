# 📖 Documentation Index & Navigation Map

**Purpose**: Help you find the right information quickly  
**Last Updated**: March 9, 2026

---

## 🚀 Start Here Based on Your Role

### If You're a **Product Manager**
```
START: README.md → (10 min overview)
   ↓
READ: QUICK_REFERENCE.md → (Understand risk framework)
   ↓
DEEP-DIVE: spec.en.md Sections 1-3 → (Problem, goals, vision)
   ↓
IMPLEMENT: ms_forms_spec.md Sections 1-4 → (Questionnaire design)
   ↓
REFERENCE: project_kickstart_summary.md Section "For Product Manager"
```
**Total Time**: ~60 minutes

---

### If You're an **Architect**
```
START: README.md → (10 min overview)
   ↓
READ: QUICK_REFERENCE.md → (Design decisions)
   ↓
DEEP-DIVE: spec.en.md Sections 4-7 → (Architecture, API contracts)
   ↓
DETAIL: agent_spec.md + knowledge_base_spec.md → (Component design)
   ↓
PLAN: IMPLEMENTATION_GUIDE.md Section 2 → (Repository structure)
   ↓
REFERENCE: IMPLEMENTATION_GUIDE.md Sections 8-10 → (Code standards)
```
**Total Time**: ~120 minutes

---

### If You're an **Engineer** (Backend/ML)
```
START: README.md → (10 min overview)
   ↓
READ: QUICK_REFERENCE.md → (Quick lookup)
   ↓
SETUP: IMPLEMENTATION_GUIDE.md Sections 3-5 → (Environment setup)
   ↓
UNDERSTAND: agent_spec.md → (Agent architecture)
   ↓
IMPLEMENT: agent_spec.md Section 5-6 → (Agent code patterns)
   ↓
TEST: IMPLEMENTING_GUIDE.md Section 7 → (Code standards & testing)
   ↓
CODE: CONTRIBUTING.md → (Workflow & standards)
   ↓
REFERENCE: spec.en.md Sections 6-7 → (Schemas & API)
```
**Total Time**: ~150 minutes over 3 days

---

### If You're **Legal / Compliance**
```
START: README.md → (Philosophy & overview)
   ↓
READ: QUICK_REFERENCE.md (Risk framework section)
   ↓
REVIEW: spec.en.md Sections 1 & 9 → (Problem & metrics)
   ↓
DEEP-DIVE: knowledge_base_spec.md → (EU AI Act structure & coverage)
   ↓
VALIDATE: Section 3 of knowledge_base_spec.md → (Article coverage checklist)
   ↓
REFERENCE: agent_spec.md Section 7 → (Confidence & escalation)
```
**Total Time**: ~90 minutes

---

### If You're an **Executive / Stakeholder**
```
START: README.md → (Project overview)
   ↓
READ: PROJECT_KICKSTART_SUMMARY.md → (What was created, timeline, ROI)
   ↓
SKIM: QUICK_REFERENCE.md → (Risk classification basics)
   ↓
UNDERSTAND: spec.en.md Section 9 → (Success metrics)
   ↓
REFERENCE: IMPLEMENTATION_GUIDE.md Section 6 → (Timeline & phases)
```
**Total Time**: ~30 minutes

---

## 📚 Document Map (How They Connect)

```
┌─────────────────────────────────────────────────────────────┐
│                    README.md (ENTRY POINT)                  │
│         Project overview, quick start, doc index             │
└──────────────────┬──────────────────────────────────────────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    ┌─────────┐ ┌──────────────┐ ┌──────────────────┐
    │ QUICK   │ │    MAIN      │ │  PROJECT         │
    │REFERENCE│ │ SPECIFICATION│ │ KICKSTART SUMMARY│
    │ (5min)  │ │  (30 min)    │ │  (20 min)        │
    └────┬────┘ └──────┬───────┘ └────────┬─────────┘
         │             │                   │
         │             │          (Explains what's created,
         │             │           timeline, next steps)
         │      ┌──────┴────┬──────────┬──────────────┐
         │      │           │          │              │
         ▼      ▼           ▼          ▼              ▼
    ┌─────────────────────────────────────────────────────────┐
    │          ROLE-SPECIFIC SPECIFICATIONS                    │
    ├──────────────────────────────────────────────────────────┤
    │                                                           │
    │  KNOWLEDGE_BASE_SPEC.md      ← For Legal, KB design      │
    │      ├─ Article structure                                │
    │      ├─ Decision trees                                   │
    │      └─ Use case examples                                │
    │                                                           │
    │  AGENT_SPEC.md               ← For Architecture, Engineers│
    │      ├─ Agent configuration                              │
    │      ├─ System prompt                                    │
    │      ├─ Input processing                                 │
    │      └─ Output generation                                │
    │                                                           │
    │  MS_FORMS_SPEC.md            ← For PM, Forms users       │
    │      ├─ Questionnaire design (all questions)             │
    │      ├─ Form validation                                  │
    │      └─ Integration API                                  │
    │                                                           │
    │  IMPLEMENTATION_GUIDE.md      ← For Engineers (main ref)  │
    │      ├─ Setup instructions                               │
    │      ├─ Repository structure                             │
    │      ├─ Development phases                               │
    │      ├─ Code standards                                   │
    │      └─ Collaboration workflow                           │
    │                                                           │
    │  CONTRIBUTING.md             ← For All developers         │
    │      ├─ Git workflow                                     │
    │      ├─ Code style                                       │
    │      ├─ Testing requirements                             │
    │      └─ PR process                                       │
    │                                                           │
    └─────────────────────────────────────────────────────────┘
             │                                        │
             │                                        │
             ▼                                        ▼
    ┌──────────────────────────────────────────────────────────┐
    │              IMPLEMENTATION (Code to be written)          │
    ├──────────────────────────────────────────────────────────┤
    │                                                           │
    │  src/sherpa/agent.py         ← Guided by: agent_spec     │
    │  src/extraction/validation.py ← Guided by: spec schemas  │
    │  src/output/formatter.py      ← Guided by: spec schemas  │
    │  knowledge_base/*.md          ← Guided by: kb_spec       │
    │  tests/**/*.py                ← Guided by: all specs     │
    │                                                           │
    └──────────────────────────────────────────────────────────┘
```

---

## 🔄 Information Flow During Development

```
SPECIFICATION PHASE (Week 0 - DONE ✅)
│
├─ spec.en.md ──────────────────────────────────┐
├─ knowledge_base_spec.md ──────────────────────┤
├─ agent_spec.md ───────────────────────────────├─→ Team Alignment
├─ ms_forms_spec.md ────────────────────────────┤
├─ IMPLEMENTATION_GUIDE.md ─────────────────────┤
└─ CONTRIBUTING.md ─────────────────────────────┘


DEVELOPMENT PHASE (Weeks 1-4)
│
├─ Spec → Code Mapping
│  ├─ spec.en.md Schemas → Pydantic models (source code)
│  ├─ agent_spec.md → src/sherpa/agent.py
│  ├─ knowledge_base_spec.md → knowledge_base/ files
│  └─ ms_forms_spec.md → API endpoint design
│
├─ Code Reviews Check Specs
│  ├─ PR references spec sections
│  ├─ Code matches spec requirements
│  ├─ Tests cover spec-defined scenarios
│  └─ Output matches spec schemas
│
└─ Specs Updated If Needed
   ├─ New discoveries → Spec update
   ├─ Design changes → Spec update
   ├─ Requirements drift → Spec update (not code change)
   └─ PR includes spec update


DEPLOYMENT & OPERATIONS (Week 5+)
│
├─ Specs as Runbooks
│  ├─ IMPLEMENTATION_GUIDE → Scaling hints
│  ├─ agent_spec → Monitoring points
│  └─ spec.en.md → Success metrics
│
├─ Maintenance
│  ├─ EU AI Act changes → Update knowledge_base_spec
│  ├─ Form changes → Update ms_forms_spec
│  └─ Architecture evolves → Update specs
│
└─ Continuous Improvement
   ├─ Post-mortems reference specs
   ├─ Performance issues → Check agent_spec optimization ideas
   └─ Legal requests → Escalate via agent_spec confidence rules
```

---

## 📋 Quick Lookup Index (By Topic)

### Questions About Requirements

| Question | Document | Section |
|----------|----------|---------|
| "What are we building?" | README.md | Overview |
| "What are the goals?" | spec.en.md | Sections 2-3 |
| "What's success?" | spec.en.md | Section 9 |
| "What are non-goals?" | spec.en.md | Section 3 |
| "What are constraints?" | spec.en.md | Section 3 & 5 |

### Questions About Design

| Question | Document | Section |
|----------|----------|---------|
| "How does it work?" | README.md | "How It Works" |
| "Architecture overview?" | spec.en.md | Section 4 |
| "Component design?" | agent_spec.md + kb_spec.md | Sections 1-3 |
| "Data flow?" | agent_spec.md | Section 5 |
| "API design?" | spec.en.md | Section 7 |

### Questions About EU AI Act

| Question | Document | Section |
|----------|----------|---------|
| "Risk categories?" | QUICK_REFERENCE.md | Risk Classification |
| "Article coverage?" | knowledge_base_spec.md | Section 3 & 4 |
| "Decision logic?" | knowledge_base_spec.md | Section 4 |
| "Use case examples?" | knowledge_base_spec.md | Section 5 |
| "Which articles apply?" | agent_spec.md | Section 2 (system prompt) |

### Questions About Implementation

| Question | Document | Section |
|----------|----------|---------|
| "How to set up?" | IMPLEMENTATION_GUIDE.md | Sections 3-5 |
| "Repository structure?" | IMPLEMENTATION_GUIDE.md | Section 2 |
| "Development phases?" | IMPLEMENTATION_GUIDE.md | Section 6 |
| "How to code?" | CONTRIBUTING.md | Sections on code standards |
| "How to test?" | IMPLEMENTATION_GUIDE.md | Section 7 |
| "How to collaborate?" | CONTRIBUTING.md | Development workflow |

### Questions About MS Forms

| Question | Document | Section |
|----------|----------|---------|
| "What questions?" | ms_forms_spec.md | Section 2 |
| "JSON schema?" | ms_forms_spec.md | Section 4 |
| "How to set up form?" | ms_forms_spec.md | Section 5 |
| "How is it integrated?" | ms_forms_spec.md | Section 7 |
| "What data is collected?" | ms_forms_spec.md | Section 6 |

### Questions About Agent

| Question | Document | Section |
|----------|----------|---------|
| "Agent design?" | agent_spec.md | Sections 1-2 |
| "System prompt?" | agent_spec.md | Section 2 |
| "Configuration?" | agent_spec.md | Section 2 |
| "How is KB integrated?" | agent_spec.md | Section 3 |
| "Input/output flow?" | agent_spec.md | Sections 5-6 |
| "Error handling?" | agent_spec.md | Section 5.2 |
| "Testing?" | agent_spec.md | Section 8 |

### Questions About Quality

| Question | Document | Section |
|----------|----------|---------|
| "Code standards?" | CONTRIBUTING.md | Code Standards |
| "Testing requirements?" | IMPLEMENTATION_GUIDE.md | Section 7.4 |
| "Coverage target?" | IMPLEMENTATION_GUIDE.md | Section 7.4 |
| "Success metrics?" | spec.en.md | Section 9 |
| "Accuracy target?" | IMPLEMENTATION_GUIDE.md | Section 6.3 |

---

## 🎯 Common Scenarios

### Scenario 1: "I'm New to the Project"
```
1. Read README.md (15 min)
2. Read QUICK_REFERENCE.md (10 min)
3. Read your role-specific spec (25 min)
4. Clone repo and follow IMPLEMENTATION_GUIDE setup (30 min)
→ Total: 80 minutes
```

### Scenario 2: "I'm Implementing a Feature"
```
1. Check QUICK_REFERENCE.md for overview
2. Read relevant spec section for detailed requirements
3. Check CONTRIBUTING.md for code standards
4. Reference spec schemas during implementation
5. Write tests per IMPLEMENTATION_GUIDE Section 7
6. Reference spec in PR description
→ Cycle time: 2-4 hours per feature
```

### Scenario 3: "I'm Reviewing a PR"
```
1. Check if PR references spec sections
2. Read those spec sections (5-10 min)
3. Verify implementation matches spec requirements
4. Check code follows CONTRIBUTING.md standards
5. Ensure tests cover spec-defined scenarios
6. Approve or request changes with spec references
→ Review time: 15-30 minutes per PR
```

### Scenario 4: "We Need to Update a Spec"
```
1. Create issue: [SPEC] Brief description
2. Create branch: spec/change-description
3. Edit specification with clear changes
4. Create PR with rationale
5. Get approvals from relevant experts
6. Merge and update version history in spec
7. Update related code if needed
→ Spec update cycle: 1-2 days
```

### Scenario 5: "Classification Accuracy is Low"
```
1. Check agent_spec.md Section 7 (Confidence scoring)
2. Check knowledge_base_spec.md (Is KB comprehensive?)
3. Run benchmark tests from agent_spec.md Section 8.2
4. Consider prompting improvements (agent_spec Section 2)
5. Consider KB updates (knowledge_base_spec Section 3)
6. Document improvements in specs
→ Investigation: 4-8 hours
```

---

## 📞 How to Use These Specs

### When Asking Questions

Instead of asking: "What are we building?"  
Ask with reference: "I'm confused about [spec.en.md Section 4.2](spec.en.md#42-core-components) - can you clarify?"

This helps because:
- ✅ Others can see exact confusion
- ✅ Prevents repeated questions
- ✅ Creates documented answers
- ✅ Improves specs for others

### When Giving Feedback

Instead of: "I don't like the design"  
Say: "The design in [agent_spec.md Section 4](agent_spec.md#4-knowledge-base-integration) doesn't match our use case because [reason]. Suggest [alternative] instead."

This helps because:
- ✅ Specific & actionable
- ✅ Others understand concern
- ✅ Easier to discuss alternatives
- ✅ Can be documented in spec update

### When Writing Code

Instead of guessing: "How should I structure this?"  
Reference spec: "Per [IMPLEMENTATION_GUIDE.md Section 2](specs/IMPLEMENTATION_GUIDE.md#2-repository-structure), validation goes in src/extraction/validation.py"

This ensures:
- ✅ Consistency across codebase
- ✅ Easier code reviews
- ✅ Clear rationale for decisions
- ✅ Easier refactoring later

---

## 🔍 Search Tips

### Finding Article Coverage

**Q**: "Where should I document Article 14 (Human Oversight)?"
**A**: 
1. Open knowledge_base_spec.md
2. Find Section 3 (Article Coverage)
3. Section 3.2 lists High-Risk articles
4. Follow template in Section 2.2

### Finding Code Location

**Q**: "Where does risk classification logic go?"
**A**:
1. Check IMPLEMENTATION_GUIDE.md Section 2 (structure)
2. Look for "classification logic" → check risk classification folder
3. Or search CONTRIBUTING.md for code patterns
4. Reference agent_spec.md Section 5 for interaction flow

### Finding API Details

**Q**: "What's the exact API request/response format?"
**A**:
1. Open spec.en.md
2. Go to Section 7 (API Contract)
3. Find exact JSON examples
4. Cross-reference with input/output schemas in Section 6

### Finding Risk Classification Rules

**Q**: "How do I determine if something is HIGH-RISK?"
**A**:
1. Start: QUICK_REFERENCE.md - Risk Classification Framework
2. Detailed: knowledge_base_spec.md Section 4.1 (Decision Tree)
3. Implementation: agent_spec.md Section 2.1 (System Prompt)

---

## 📊 Document Statistics

| Document | Size | Reading Time | Purpose |
|----------|------|--------------|---------|
| README.md | ~400 lines | 10 min | Entry point & overview |
| QUICK_REFERENCE.md | ~400 lines | 10 min | Quick lookup |
| spec.en.md | ~600 lines | 30 min | Main requirements |
| knowledge_base_spec.md | ~500 lines | 20 min | KB structure & coverage |
| agent_spec.md | ~700 lines | 25 min | Agent architecture |
| ms_forms_spec.md | ~800 lines | 25 min | Forms & integration |
| IMPLEMENTATION_GUIDE.md | ~900 lines | 35 min | Development guide |
| CONTRIBUTING.md | ~600 lines | 20 min | Code collaboration |
| PROJECT_KICKSTART_SUMMARY.md | ~650 lines | 15 min | What's been created |

**Total documentation**: ~5,550 lines  
**Total reading time**: ~3-4 hours for complete understanding  
**Total reading time**: ~30-60 minutes per role-specific path

---

## ✅ Verification Checklist

Use this to verify you have all documentation:

- [ ] README.md (in root directory)
- [ ] PROJECT_KICKSTART_SUMMARY.md (in root directory)
- [ ] CONTRIBUTING.md (in root directory)
- [ ] specs/spec.en.md (main specification)
- [ ] specs/knowledge_base_spec.md (KB structure)
- [ ] specs/agent_spec.md (agent design)
- [ ] specs/ms_forms_spec.md (forms integration)
- [ ] specs/IMPLEMENTATION_GUIDE.md (development guide)
- [ ] specs/QUICK_REFERENCE.md (quick lookup)
- [ ] specs/DOCUMENTATION_INDEX.md (this file)

**If any missing**: Reach out; all should be provided.

---

## 🎓 Training Path

### Day 1: Foundation (1 hour)
- [ ] Read README.md
- [ ] Read QUICK_REFERENCE.md

### Day 2: Role-Specific (1 hour)
- [ ] Read spec relevant to your role
- [ ] Skim CONTRIBUTING.md if you'll code

### Day 3: Deep Dive (1 hour)
- [ ] Read full spec.en.md
- [ ] Read IMPLEMENTATION_GUIDE.md for engineers

### By End of Week
- [ ] Attend team kickoff
- [ ] Set up development environment
- [ ] Ready to start Phase 1

---

## 🤝 Getting Help

**"Where's [information]?"**
1. Check Search Tips section above
2. Check Quick Lookup Index
3. Search document title in this index
4. Ask teammate or in Slack

**"Is there a document for [topic]?"**
1. Check Document Index
2. Check Table of Contents in README.md
3. If not found, create GitHub issue: `[DOCS] Missing documentation for [topic]`

**"This spec is unclear"**
1. Create GitHub issue: `[SPEC] Clarification needed on [topic]`
2. Reference specific section & line if possible
3. Frame as question: "What does this mean?"
4. Team will clarify in issue comments

---

## 📈 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-09 | Initial specifications & documentation |

---

**Last Updated**: March 9, 2026  
**Status**: ✅ COMPLETE - Ready for team review  
**Next Update**: After first team kickoff meeting

🎯 **Use this index to navigate documentation like a pro!**
