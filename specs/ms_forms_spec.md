# MS Forms Integration Specification

**Status**: Draft for MVP v1.0  
**Purpose**: Define MS Forms questionnaire structure and API integration

---

## 1. Overview

MS Forms serves as the user-facing questionnaire interface for the AI Compliance Sherpa. This specification defines:
- Questionnaire structure and question design
- Form validation and data submission
- JSON export schema
- Integration with the classification agent

---

## 2. MS Forms Questionnaire Design

### 2.1 Role-Based Form Variants

The questionnaire is designed for three roles with slightly different UX:
- **Product Manager**: Focus on business intent and stakeholders
- **Architect**: Focus on technical design and governance
- **Engineer**: Focus on implementation details and data handling

All roles answer core questions, but the form flow may differ.

### 2.2 Questionnaire Sections

#### Section 1: System Identification (All roles)

**Q1.1**: What is the name of your AI system?
- Type: Text input (short)
- Required: Yes
- Field: `system_info.name`

**Q1.2**: What is the primary purpose of this system?
- Type: Text area (long)
- Required: Yes  
- Placeholder: "e.g., Recommend products to customers, screen job candidates, detect anomalies..."
- Field: `system_info.purpose`

**Q1.3**: Describe how the system works in 2-3 sentences
- Type: Text area
- Required: Yes
- Field: `system_info.description`

**Q1.4**: When do you plan to deploy this system?
- Type: Date picker
- Required: Yes
- Field: `system_info.expected_deployment_date`

**Q1.5**: What is the scope of deployment?
- Type: Multiple choice (radio)
- Options:
  - Internal use only (within company)
  - External use (customers/partners)
  - Public (general internet)
- Required: Yes
- Field: `system_info.deployment_scope`

#### Section 2: Data Processing (All roles)

**Q2.1**: Does your system process personal data? (data about identifiable individuals)
- Type: Yes/No
- Required: Yes
- Field: `data_processing.personal_data_processed`
- Note: "If unsure, select YES"

**Q2.2**: If YES to Q2.1, describe the types of data (check all that apply):
- Type: Checkboxes
- Options:
  - Name, contact info
  - Location/GPS data
  - Financial/payment info
  - Health or medical data
  - Biometric data (face, fingerprint, voice, etc.)
  - Education/training records
  - Employment/HR records
  - Ethnic origin, race, religion
  - Political views or affiliations
  - Union membership
  - Genetic data
  - Other: [text field]
- Required: Yes if Q2.1 = Yes
- Field: `data_processing.data_types[]`

**Q2.3**: Does your system process special category data (sensitive data like health, biometrics, race, etc.)?
- Type: Yes/No
- Required: Yes
- Field: `data_processing.sensitive_data_processed`
- Help text: "See list in Q2.2 for examples"

**Q2.4**: Approximately how many individuals' data will be processed?
- Type: Radio
- Options:
  - Fewer than 100
  - 100-1,000
  - 1,000-10,000
  - 10,000-100,000
  - Over 100,000
- Required: Yes if Q2.1 = Yes
- Field: `data_processing.data_subject_count`

**Q2.5**: Where does the data come from? (check all that apply)
- Type: Checkboxes
- Options:
  - Directly from the individual
  - From company operations (logs, transactions, etc.)
  - From third-party data providers
  - From public sources
  - Inferred/derived from other data
- Required: Yes if Q2.1 = Yes
- Field: `data_processing.data_source_types[]`

#### Section 3: Decision-Making (All roles)

**Q3.1**: Does your system make decisions that have legal or regulatory consequences for individuals?
- Type: Yes/No
- Required: Yes
- Field: `decision_making.produces_legal_decisions`

**Q3.2**: Does your system make individual-level decisions affecting specific people? (vs. aggregate/statistical decisions)
- Type: Yes/No
- Required: Yes  
- Field: `decision_making.produces_individual_decisions`

**Q3.3**: If YES to Q3.2, describe the decision (e.g., approve/reject, score, classify):
- Type: Text area
- Required: Yes if Q3.2 = Yes
- Field: `decision_making.decision_description`

**Q3.4**: Can the decision materially affect fundamental rights of individuals? (e.g., rights to work, education, fair trial, privacy)
- Type: Yes/No
- Required: Yes
- Field: `decision_making.affects_fundamental_rights`
- Help text: "If unsure, select YES"

**Q3.5**: Is the decision fully autonomous (AI decides without human involvement)?
- Type: Yes/No
- Required: Yes
- Field: `decision_making.autonomous_decision_making`

**Q3.6**: If NOT fully autonomous (Q3.5 = No), describe the human involvement:
- Type: Text area
- Required: Yes if Q3.5 = No
- Field: `decision_making.human_involvement_description`

**Q3.7**: Do individuals have the right to appeal or request human review of the decision?
- Type: Yes/No
- Required: Yes
- Field: `decision_making.human_appeal_process`

#### Section 4: Use Case Classification (All roles)

**Q4.1**: Which of these best describes your AI system? (select one)
- Type: Radio
- Options with descriptions:
  1. **Employment & Recruitment**
     - Hiring, firing, promotion, task allocation, performance monitoring
  2. **Education & Training**  
     - Admission, exam evaluation, curriculum recommendations
  3. **Critical Infrastructure**
     - Power grids, water, transport, gas systems, digital infrastructure
  4. **Law Enforcement**
     - Investigations, risk assessment, evidence analysis
  5. **Migration, Asylum & Border Control**
     - Visa processing, asylum decisions, border screening
  6. **Credit Scoring & Financial Services**
     - Loan approvals, credit lines, insurance decisions
  7. **Biometric Identification**
     - Face recognition, fingerprint matching, iris scanning, (identification purposes)
  8. **Biometric Categorization**
     - Inferring sensitive attributes from biometrics (e.g., age, gender, emotion from face)
  9. **Other High-Risk**: [text field]
  10. **Chatbot / Conversational AI**
      - Customer service, Q&A, dialogue system
  11. **Deepfake Detection**
      - Identifying synthetic media
  12. **Content Generation (AI-Created)**
      - Text generation, image generation, media synthesis
  13. **Other Non-High-Risk**: [text field]

- Required: Yes
- Field: `use_case_category`

**Q4.2**: Are there any use cases involving law enforcement facial recognition in public spaces?
- Type: Yes/No
- Required: Yes
- Field: `special_case.law_enforcement_facial_recognition`
- Help text: "Real-time or post-event facial recognition by law enforcement in public areas"

#### Section 5: Stakeholders (Primarily PM/Architect)

**Q5.1**: Will the system affect or involve minors (under 18)?
- Type: Yes/No
- Required: Yes
- Field: `stakeholders.minors_involved`

**Q5.2**: Does the system affect vulnerable groups? (e.g., elderly, disabled, low-income, asylum seekers)
- Type: Yes/No
- Required: Yes
- Field: `stakeholders.vulnerable_groups`

**Q5.3**: Which countries' individuals will be affected by this system? (select all that apply)
- Type: Checkboxes
- Options: All EU member states + UK, US, etc.
- Required: Yes
- Field: `stakeholders.countries_affected[]`

#### Section 6: Governance & Oversight (Primarily Architect/Engineer)

**Q6.1**: Is a Data Protection Officer (DPO) or compliance team involved in the design?
- Type: Yes/No
- Required: Yes
- Field: `governance.data_protection_officer_involved`

**Q6.2**: What level of human oversight will be in place?
- Type: Radio
- Options:
  - Full oversight: Humans review and approve all decisions
  - Partial oversight: Humans review certain decisions (high-risk, edge cases)
  - Minimal oversight: Humans monitor but don't pre-approve decisions
  - None: System operates autonomously
- Required: Yes
- Field: `governance.human_oversight_mechanism`

**Q6.3**: How will you monitor the system's performance and behavior in production?
- Type: Radio
- Options:
  - Real-time monitoring (continuous, automated alerts)
  - Periodic review (weekly, monthly)
  - Post-incident review (only when issues arise)
  - No monitoring planned
- Required: Yes
- Field: `governance.monitoring_capability`

**Q6.4**: Is the system required to explain its decisions to affected individuals?
- Type: Radio
- Options:
  - Full explainability required (detailed reasoning)
  - Basic explanation (how decision was made, not AI-specific)
  - None required
- Required: Yes
- Field: `governance.explainability_requirement`

**Q6.5**: What measures will you take to ensure fairness and prevent bias?
- Type: Checkboxes
- Options:
  - Testing for bias before deployment
  - Regular bias audits during operation
  - Diverse training data
  - Fairness metrics monitoring  
  - Stakeholder consultation
  - Other: [text field]
  - None planned
- Required: Yes
- Field: `governance.fairness_measures[]`

#### Section 7: Confirmation & Submission (All roles)

**Q7.1**: I confirm that the information provided is accurate to the best of my knowledge.
- Type: Checkbox
- Required: Yes
- Field: `confirmation.accuracy`

**Q7.2**: My organization authorizes this compliance classification assessment.
- Type: Checkbox
- Required: Yes
- Field: `confirmation.authorization`

**Q7.3**: (Optional) Email for follow-up questions
- Type: Email input
- Required: No
- Field: `contact.email`

---

## 3. Form Validation Rules

| Question | Validation | Error Message |
|----------|-----------|---------------|
| Q1.1 | Min 3, max 100 chars | "System name must be 3-100 characters" |
| Q1.2 | Min 20, max 1000 chars | "Description must be 20-1000 characters" |
| Q1.4 | After today's date | "Deployment date must be in future" |
| Q2.1 | If No, Q2.2-2.5 disabled | Automatic (conditional) |
| Q3.1-3.7 | Logical consistency (see below) | "Responses are contradictory..." |
| Q7.1-7.2 | Must be checked | "Required to proceed" |

### Form Logic Rules

```
If Q2.1 (personal_data_processed) = No:
  → Disable Q2.2, Q2.3, Q2.4, Q2.5

If Q3.2 (produces_individual_decisions) = No:
  → Disable Q3.3, Q3.4, Q3.5, Q3.6, Q3.7
  → Q3.4, Q3.5 auto-set to No

If Q3.5 (autonomous_decision_making) = Yes:
  → Disable Q3.6, Q3.7
  → Q3.7 auto-set to No

If Q4.1 uses "Other" option:
  → Require user to fill text field
```

---

## 4. JSON Export Schema

When form is submitted, MS Forms API returns JSON in this structure:

```json
{
  "metadata": {
    "form_submission_id": "uuid",
    "timestamp": "2026-03-09T10:30:00Z",
    "ms_forms_id": "ms-form-abc123",
    "submitter_role": "PM",
    "submitter_email": "user@company.com",
    "organization_unit": "Product"
  },
  "system_info": {
    "name": "Candidate Resume Screening System",
    "description": "AI system that screens resumes and recommends top candidates to recruiters",
    "purpose": "Automate initial resume filtering to reduce recruiter workload",
    "expected_deployment_date": "2026-06-15",
    "deployment_scope": "INTERNAL"
  },
  "data_processing": {
    "personal_data_processed": true,
    "data_types": ["name_contact", "employment_records", "education_records"],
    "sensitive_data_processed": false,
    "data_subject_count": "RANGE_10K_100K",
    "data_source_types": ["directly_from_individual", "company_operations"]
  },
  "decision_making": {
    "produces_legal_decisions": false,
    "produces_individual_decisions": true,
    "decision_description": "System scores each resume and ranks candidates. Recruiters review top-10 recommended candidates before scheduling interviews.",
    "affects_fundamental_rights": true,
    "autonomous_decision_making": false,
    "human_involvement_description": "Recruiters review all system recommendations and make final decision on who to interview",
    "human_appeal_process": true
  },
  "use_case_category": "EMPLOYMENT",
  "special_cases": {
    "law_enforcement_facial_recognition": false
  },
  "stakeholders": {
    "minors_involved": false,
    "vulnerable_groups": false,
    "countries_affected": ["DE", "FR", "IT", "ES"]
  },
  "governance": {
    "data_protection_officer_involved": true,
    "human_oversight_mechanism": "PARTIAL",
    "monitoring_capability": "PERIODIC",
    "explainability_requirement": "BASIC",
    "fairness_measures": ["testing_for_bias", "diverse_training_data", "fairness_metrics_monitoring"]
  },
  "confirmation": {
    "accuracy": true,
    "authorization": true
  },
  "contact": {
    "email": "user@company.com"
  }
}
```

---

## 5. MS Forms Setup Instructions

### 5.1 Creating the Form

1. Go to **forms.office.com**
2. Create new form titled: "AI Compliance Assessment - EU AI Act"
3. Add form description:
   ```
   This questionnaire helps us understand your AI system and its 
   compliance with the EU Artificial Intelligence Act. It will take 
   ~10 minutes to complete.
   
   All information is confidential and used only for compliance 
   assessment purposes within [Company Name].
   ```

4. Set sharing to "People in [Organization] can respond"

5. Add each question following Section 2.2 above

6. At the end, add:
   ```
   Thank you for completing this assessment!
   
   Your responses have been submitted for AI compliance analysis.
   
   You will receive a detailed compliance report within 2 business days.
   Contact [compliance-team@company.com] with questions.
   ```

### 5.2 Form Configuration

- **Shuffle question order**: No (keep consistent)
- **Show progress bar**: Yes (encourages completion)
- **Show score**: No
- **Collect respondent names**: No (privacy)
- **One response per person**: Yes (prevent duplicates)
- **Show results summary**: No (not needed)
- **Require sign-in**: Yes (to organizational account only)

---

## 6. Data Collection & Storage

### 6.1 Form Response Export

Responses are automatically exported.

**Export Frequency**: Daily (automated job)

**Export Format**: 
- CSV (for Excel/analytics)
- JSON (for Agent API integration)

**Storage Location**: 
- Primary: Azure Blob Storage (secure, compliant)
- Backup: SharePoint document library

### 6.2 Data Privacy & Retention

- **Retention Period**: 3 years (for audit trail)
- **Encryption**: AES-256 at rest, TLS in transit
- **Access Control**: Only compliance team & AI agent service account
- **Redaction**: Personally identifiable information anonymized in logs
- **GDPR Compliance**: Data deleted upon request; privacy notice in form

---

## 7. Integration with Classification Agent

### 7.1 Data Flow

```
MS Forms Submission
    ↓
[Form validation in Microsoft Forms]
    ↓
[Response exported to JSON]
    ↓
[Azure Function / Webhook triggers]
    ↓
[Classification Agent API endpoint]
    ↓
[Agent processes questionnaire]
    ↓
[Classification result stored]
    ↓
[Report generated & emailed to submitter]
```

### 7.2 Integration API Call

```
POST https://api.company.com/v1/classify-ai-system

Headers:
  Content-Type: application/json
  Authorization: Bearer {service_account_token}
  X-MS-Forms-Submission-ID: {form_submission_id}

Body: {questionnaire_json_from_form}

Response:
  {
    "classification_id": "uuid",
    "risk_classification": "HIGH_RISK",
    "confidence_score": 0.92,
    "report_markdown": "...",
    "report_json": {...}
  }
```

### 7.3 Automated Workflow (Future)

```
Power Automate Workflow:
1. Trigger: MS Forms response submitted
2. Action: Parse form response to JSON
3. Action: Call Classification Agent API
4. Action: Generate markdown report
5. Action: Create document in SharePoint
6. Action: Send email to submitter with report
7. Action: Log to audit table
```

---

## 8. Testing the Form

### 8.1 Test Scenarios

| Scenario | Purpose | Expected Outcome |
|----------|---------|------------------|
| High-Risk System | Verify detection of clear HR use case with autonomous decisions | Classification = HIGH_RISK |
| Low-Risk Chatbot | Verify correct classification of obvious limited-risk system | Classification = LIMITED_RISK |
| Incomplete Form | Ensure required field validation works | Form not submittable |
| Edge Case: Salary Prediction | Borderline high-risk for HR | Agent recommends expert review |

### 8.2 UAT Checklist

- [ ] All questions display correctly
- [ ] Conditional logic works (hide/show questions based on answers)
- [ ] Validation prevents submission of incomplete forms
- [ ] JSON export includes all responses
- [ ] Email with form link works for external testing
- [ ] Accessibility: screen reader compatible, keyboard navigable
- [ ] Mobile UX: form usable on smartphone
- [ ] Submission confirmation email sent successfully

---

## 9. User Training & Documentation

### 9.1 Help Text in Form

Include contextual help for each section:

```text
SECTION 1 HELP:
"Help your team provide accurate information about your AI system. 
Be specific about the purpose and intended use."

SECTION 2 HELP:  
"Data processing is central to EU AI Act compliance. If you process 
any information identifiable to people, select YES."

SECTION 3 HELP:
"This section focuses on how the system makes decisions and whether 
those decisions affect individuals' fundamental rights."

SECTION 4 HELP:
"The EU AI Act categorizes AI systems by use case and risk level. 
Select the category that best matches your system."
```

### 9.2 FAQ Page (Linked in Form)

Document common questions:
- "What counts as personal data?"
- "What are fundamental rights?"
- "Is my system high-risk?"
- "What happens after I submit?"

---

## 10. Success Metrics

| Metric | Target |
|--------|--------|
| Form completion rate | >80% of started forms completed |
| Average completion time | 8-12 minutes |
| Re-submission rate | <5% (if data quality issues) |
| Submission volume | >70% of new AI projects |
| User satisfaction (NPS) | >4.0/5.0 |

---

## 11. Future Enhancements

- [ ] Progressive disclosure (show only relevant questions for role)
- [ ] Pre-fill from project management system (Jira, Azure DevOps)
- [ ] Mobile app version with offline capability
- [ ] Multilingual support (EU languages)
- [ ] Integration with architecture decision records (ADRs)
- [ ] Video tutorials for complex questions
- [ ] Real-time risk assessment preview (show preliminary classification as user completes form)

---

**Next Steps**:
1. Create MS Forms by following Section 5.1 above
2. Test form with 5-10 internal users (UAT)
3. Collect feedback and refine questions
4. Set up Azure automation for response export
5. Implement API endpoint for agent integration
6. Create user communication materials

