# Microsoft Forms Questionnaire Guide
## EU AI Act Compliance Assessment

### Overview

This guide explains the mandatory, conditional, and optional questions for your EU AI Act compliance questionnaire in Microsoft Forms.

---

## Question Structure

### **MANDATORY Questions (Core Classification) - All systems must answer**

These 5 questions map directly to EU AI Act Annex I explicit high-risk categories and MUST be answered by every organization.

| Question | Category | Why Mandatory | Risk If Not Answered |
|----------|----------|---------------|----------------------|
| **Q5** | Recruitment/Selection | Employment decisions are explicit Annex I high-risk | Cannot classify employment systems |
| **Q6** | Employment Conditions | Employment-related AI is explicit Annex I high-risk | Cannot assess employment impact |
| **Q7** | Biometric Identification | Determines if PROHIBITED or HIGH_RISK | Cannot identify prohibited systems |
| **Q9** | Critical Infrastructure | Critical infrastructure is explicit Annex I high-risk | Cannot identify safety-critical systems |
| **Q10** | Credit Scoring | Credit decisions are explicit Annex I high-risk | Cannot assess financial system risk |

**Estimated time to complete Core 5 questions: 5-10 minutes**

---

### **CONDITIONAL Mandatory Questions (Education systems only)**

If the system operates in **education/training**, these 4 questions become mandatory:

| Question | Applies When | Why Mandatory | Compliant Alternative |
|----------|--------------|---------------|----------------------|
| **Q1** | Education/training admission system | Access to education is a protected right | Not applicable - must answer if education system |
| **Q2** | System predicts/determines learning outcomes | Affects educational opportunity | Must answer if education system |
| **Q3** | System evaluates qualifications/skills | Educational qualifications affect life opportunities | Must answer if education system |
| **Q4** | System monitors exams or detects cheating | Affects assessment integrity and fairness | Must answer if education system |

**Implementation Logic:**
```
IF q1_education_admissions IS "education/training system" 
THEN Q1, Q2, Q3, Q4 become required
ELSE Q1, Q2, Q3, Q4 are skipped and not required
```

**Estimated time if education system: +5 minutes**

---

### **OPTIONAL Questions (Recommended)**

These questions provide additional context and are highly recommended but not strictly required for EU AI Act classification:

| Question | Why Recommended | Value |
|----------|-----------------|-------|
| **Q8** | Sensitive Attributes | Identifies fairness/discrimination risks not covered by other questions |
| **Human Oversight Level** | Mitigation factor | Demonstrates compliance measures and reduces risk classification |
| **Transparency/Explainability** | Required obligation | Identifies if system meets transparency compliance requirements |

---

## Implementation in Microsoft Forms

### **Step 1: Create Required Fields**
- System Name (required text field)
- System Purpose (required text field)  
- Data Types (required text field)
- Autonomous (required choice)
- Affects Rights (required choice)
- Organization Sector (required choice)

### **Step 2: Add Education Detection**
- Add: "Is this an education/training system?" (optional choice)
- Set up conditional branching for Q1-Q4

### **Step 3: Mandatory Core 5 Questions**
Make these 5 questions **required** in your form:
1. Q5 - Recruitment/Selection
2. Q6 - Employment Conditions
3. Q7 - Biometric Identification
4. Q9 - Critical Infrastructure
5. Q10 - Credit Scoring

### **Step 4: Conditional Education Questions**
Create a branching rule:
```
IF (Is this an education/training system?) = YES
THEN Show Q1, Q2, Q3, Q4 as REQUIRED questions
ELSE Skip these questions
```

### **Step 5: Optional Section**
Add as optional (not required):
- Q8 - Sensitive Attributes
- Human Oversight Level
- Transparency/Explainability

---

## Response Analysis Guide

### **Minimum Sufficient Information**

Your compliance agent can make a valid classification with:
- ✅ All Core 5 mandatory questions answered
- ✅ If education system: All 4 conditional questions answered
- ⚠️ Missing optional questions: Classification will be valid but may miss nuances

### **Recommended Complete Information**

For most comprehensive assessment, also collect:
- ✅ System Information (name, purpose, data types, autonomy, rights impact)
- ✅ All mandatory + conditional questions
- ✅ Optional questions (Q8, oversight level, transparency)
- ✅ Additional notes providing context

---

## Question-by-Question Guidance for Respondents

### **Q5: Recruitment/Selection**
**When to answer YES:**
- CV screening, resume filtering, candidate ranking
- Skill assessment tests
- Job suitability scoring
- Candidate shortlisting

**When to answer NO:**
- System only displays job postings
- System administers test but doesn't score it
- Human only looks at results without system ranking

---

### **Q6: Employment Conditions**
**When to answer YES:**
- Bonus/salary calculations
- Promotion eligibility determination
- Training program assignment
- Work task allocation
- Performance monitoring and ratings
- Scheduling decisions

**When to answer NO:**
- System only tracks hours worked (for payment) with no automation
- System displays employee data without making decisions

---

### **Q7: Biometric Identification**
**When to answer YES - Real-time remote (⚠️ PROHIBITED):**
- Facial recognition for identity verification at a distance
- Iris scanning for remote authentication
- Voice recognition for identity verification

**When to answer YES - Other biometric (HIGH_RISK):**
- Fingerprint scanning at physical location
- Palm vein scanning
- Biometric data stored for matching

**When to answer NO:**
- System doesn't use biometric data
- System uses password/PIN only

---

### **Q9: Critical Infrastructure**
**When to answer YES:**
- Electricity grid management/optimization
- Water treatment or distribution system
- Transportation network management (rail, air, road)
- Telecommunications network
- Gas supply system
- Medical care infrastructure
- Emergency services systems

**When to answer NO:**
- Most business systems
- Consumer services
- Content management

---

### **Q10: Credit Scoring**
**When to answer YES:**
- Loan approval/rejection decisions
- Credit score calculation
- Credit limit determination
- Loan terms/interest rate setting
- Creditworthiness assessment
- Financial risk scoring

**When to answer NO:**
- Banking services with no AI scoring
- Payment processing
- Invoice management

---

### **Q1-Q4: Education Questions**
**When to answer YES (any of Q1-Q4):**
- University admission processing
- Student course/program assignment
- Exam proctoring or cheating detection
- Learning effectiveness assessment
- Skill level evaluation
- Recommendation for educational placement

**When to answer NO:**
- General educational content delivery
- Online learning platforms without assessment AI
- Administrative systems without AI decision-making

---

### **Q8: Sensitive Attributes**
**When to answer YES:**
- System makes inferences about race, ethnicity, gender, disability, etc.
- System profiles based on protected characteristics
- System's decisions correlate with protected attributes

**When to answer NO:**
- System doesn't use or infer sensitive attributes
- Explicit measures prevent proxy discrimination

---

## Scoring & Classification Logic

Once responses are collected, the compliance agent uses this logic:

```
1. Check Q7 (Biometric):
   IF real-time remote biometric → PROHIBITED (95% confidence)

2. Check Q5, Q6, Q9, Q10:
   IF any = YES → At least HIGH_RISK
   
3. Check Q1-Q4 (if education system):
   IF any = YES → At least HIGH_RISK

4. If none of above → LIMITED_RISK or MINIMAL_RISK
   (based on autonomous + affects_rights combination)
```

---

## Expected Response Patterns

### **Pattern 1: Employment System**
```
Mandatory:
- Q5: Yes (recruitment)
- Q6: Yes (employment conditions)
- Q7: No
- Q9: No
- Q10: No

Expected Classification: HIGH_RISK
Reason: Employment decisions are Annex I high-risk
```

### **Pattern 2: Education System**
```
Mandatory:
- Q5-Q10: Mostly No

Conditional (because is_education_system=Yes):
- Q1: Yes (admission)
- Q2-Q4: No

Expected Classification: HIGH_RISK
Reason: Education access decisions are high-risk
```

### **Pattern 3: Minimal Risk**
```
Mandatory:
- Q5-Q10: All No

Education: No
Autonomous: No
Affects Rights: No

Expected Classification: MINIMAL_RISK
Reason: No high-risk indicators
```

---

## Microsoft Forms Configuration Checklist

- [ ] Create form with title "EU AI Act Compliance Assessment"
- [ ] Add System Information section (all required)
- [ ] Add MANDATORY section with 5 required questions
- [ ] Add CONDITIONAL section with branching logic for education questions
- [ ] Add OPTIONAL section (not required)
- [ ] Set up branching: If education_system=Yes → show Q1-Q4 as required
- [ ] Configure submission confirmation message
- [ ] Test with sample responses
- [ ] Set form permissions (who can submit)
- [ ] Configure automated response collection

---

## Integration with Compliance Agent

Once responses are submitted:

1. **Extract responses** from Microsoft Forms
2. **Map to Questionnaire schema** (use the updated schemas.py)
3. **Validate mandatory fields** are answered
4. **Call compliance agent** with questionnaire data
5. **Generate classification report** with applicable EU AI Act articles
6. **Provide recommendations** based on identified risks

---

## FAQ

**Q: Can respondents skip mandatory questions?**
A: No. Set these as required in Microsoft Forms:
- Core 5 (Q5, Q6, Q7, Q9, Q10) - always required
- Q1-Q4 - only required if education_system=Yes

**Q: What if a respondent doesn't know the answer?**
A: Provide "Unsure/Not Applicable" as an option, but guidance should encourage best-effort answers. Uncertain responses may trigger recommendations for system documentation review.

**Q: How long should the questionnaire take?**
A: Core questions: 5-10 minutes; Education systems: +5 minutes; Full questionnaire with optional: 15 minutes total.

**Q: Can organizations skip optional questions?**
A: Yes, optional questions won't affect classification. But highly recommend for completeness.

**Q: Who should fill this out?**
A: AI system owners, data protection officers, or compliance managers who understand the system's technical and operational details.

---

## Document Version
- **Created**: March 12, 2026
- **Status**: Ready for Microsoft Forms implementation
- **Mandatory Questions**: 5 core + up to 4 conditional
- **Optional Questions**: 3 recommended
