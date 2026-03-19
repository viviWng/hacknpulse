# EU AI Act Articles - Detailed Explanations

## Article 5: Prohibited AI Practices

**Official Designation**: Prohibited artificial intelligence practices

### Overview
Article 5 establishes absolute prohibitions on certain AI systems regardless of their deployment context. These are practices that fundamentally violate rights and cannot be made compliant through additional safeguards or oversight.

### Prohibited Categories

#### 1. Subliminal Manipulation
**What's Prohibited**: AI systems that deploy techniques beyond a person's consciousness to materially distort behavior causing harm.

**Examples**:
- Audio/visual techniques that bypass rational processing
- Subliminal messaging embedded in content
- Neuro-manipulation techniques

**Why**: Violates human dignity and autonomy. Cannot be remedied by transparency since target cannot consciously perceive the technique.

#### 2. Social Scoring
**What's Prohibited**: AI systems that score individuals based on social behavior or personal characteristics with potential to unfairly categorize or impact civic activities.

**Examples**:
- Government citizen scoring systems
- Systems that lower social status based on political opinions
- Systems that restrict civic participation (voting, public services) based on algorithm scores

**Why**: Creates chilling effect on fundamental freedoms. Incompatible with democratic societies.

#### 3. Real-Time Remote Biometric Identification
**What's Prohibited**: Real-time biometric identification at distance by law enforcement UNLESS narrow exceptions apply.

**Examples of Prohibited Use**:
- Mass surveillance with facial recognition
- Ongoing monitoring at public spaces
- Automated identification workflows

**Allowed Exceptions** (must have legal authorization):
- Searching for specifically identified person
- Preventing imminent threat to life
- National law explicitly authorizes

**Why**: Privacy risks are extreme. Remote biometric ID enables mass surveillance incompatible with human rights.

### Enforcement
- **Consequence**: System must be removed from market immediately
- **Responsibility**: National AI authorities
- **Compliance**: Zero tolerance; no mitigation possible

---

## Article 6: Classification of High-Risk AI Systems

**Official Designation**: Classification of high-risk AI systems

### Overview
Article 6 defines what constitutes high-risk AI systems. These are systems that, while not prohibited, require substantial compliance measures including risk assessment, data governance, human oversight, and transparency.

### High-Risk Categories (Annex I)

Systems are HIGH-RISK if they fall into specific domains AND make autonomous decisions affecting fundamental rights:

#### Domain 1: Employment
**Systems that make decisions about**:
- Recruitment and selection of personnel
- Job applicant evaluation
- Employee performance assessment
- Promotion and salary decisions
- Disciplinary actions

**Affected Rights**:
- Right to work
- Fair employment conditions
- Non-discrimination

**Annex Reference**: Annex I(4)(a)-(b)

#### Domain 2: Credit and Finance
**Systems that make decisions about**:
- Loan approval/rejection
- Credit limit determination
- Interest rate setting
- Insurance underwriting
- Creditworthiness assessment
- Access to financial services

**Affected Rights**:
- Access to essential financial services
- Non-discrimination
- Right to explanation

**Annex Reference**: Annex I(5)(a)-(b)

#### Domain 3: Biometric Identification
**Systems that**:
- Perform automatic identification of individuals
- Use facial recognition, iris scanning, fingerprint matching
- Create/update biometric databases

**Affected Rights**:
- Privacy and data protection
- Right to identity
- Protection from surveillance

**Annex Reference**: Annex I(1)

#### Domain 4: Critical Infrastructure
**Systems controlling**:
- Energy distribution (electricity, gas, oil)
- Water supply and treatment
- Transportation networks
- Emergency services
- Digital infrastructure

**Affected Rights**:
- Public safety
- Continuity of essential services
- Life and health protection

**Annex Reference**: Annex I(2)

#### Domain 5: Sensitive Attribute Categorization
**Systems that infer or categorize based on**:
- Race or ethnicity
- Gender or gender identity
- Disability or health status
- Religion or belief
- Sexual orientation
- Political opinion
- Union membership
- Genetic or biometric data

**Affected Rights**:
- Protection from discrimination
- Dignity and equality
- Freedom of conscience

**Annex Reference**: Article 10

### Compliance Requirements for High-Risk Systems

#### Article 9: Risk Assessment
- Identify and analyze reasonably foreseeable risks
- Assess severity of each risk
- Evaluate existing and proposed mitigation measures
- Document findings and justifications
- Update assessment when significant changes occur

#### Article 10: Data and Governance
- Training data must be relevant, representative, error-free, complete
- Validation and testing data must meet quality standards
- Data governance procedures must be documented
- Regular monitoring and auditing of data quality
- Data management subject to oversight and control

#### Article 13: Transparency
- Individuals must be informed they're interacting with AI
- Meaningful information about AI system must be provided
- Users must understand how decisions are made
- Clear information about rights and possibilities
- For AI-generated content: disclose AI generation

#### Article 14: Human Oversight
- Design system so humans can effectively supervise
- Provide ability to stop or override AI decisions
- Enable human intervention in design/deployment/use
- Meaningful and proportionate to risk level
- Users must have clear information to exercise oversight

---

## Article 9: Risk Assessment

**Official Designation**: Risk assessment and mitigation

### Purpose
Before deploying high-risk systems, organizations must systematically identify, analyze, and mitigate risks to fundamental rights and safety.

### Required Elements

#### 1. Risk Identification
Identify all reasonably foreseeable risks including:
- Risks to fundamental rights (discrimination, privacy)
- Safety-critical failures
- Accuracy and reliability failures
- Data quality issues
- Model drift and degradation
- Adversarial attacks

#### 2. Risk Severity Assessment
For each identified risk:
- Scope: How many people affected?
- Magnitude: How serious is the harm?
- Probability: How likely is it to occur?
- Reversibility: Can the harm be remedied?

#### 3. Mitigation Evaluation
For each significant risk:
- What existing safeguards mitigate it?
- What additional measures are needed?
- How will you monitor that mitigations work?
- What's the residual risk after mitigation?

#### 4. Documentation
Record:
- Risk identification methodology
- All identified risks and assessments
- Mitigation measures and their effectiveness
- Rationale for accepting any residual risks
- Timeline for risk assessment updates

### When Assessment is Needed
- Before first deployment
- When significant changes occur
- When incidents reveal new risks
- Periodically (at least annually)

---

## Article 10: Data Quality and Governance

**Official Designation**: Data and algorithmic governance

### Purpose
High-risk systems must ensure high data quality and effective governance to prevent discrimination, inaccuracy, and bias.

### Data Quality Requirements

#### Training Data
Must be:
- **Relevant**: Appropriate for intended use case
- **Representative**: Not systematically biased toward certain groups
- **Error-free**: Quality checks and cleaning done
- **Complete**: Not missing significant data classes or populations
- **Adequate frequency**: Regular updates to remain representative

#### Validation & Testing Data
Must meet same quality standards as training data.

#### Data Governance
Must include:
- Documented procedures for data collection
- Quality assessment processes
- Data cleaning and error correction
- Version control and provenance tracking
- Access controls and security

### Fairness & Non-Discrimination

#### Bias Testing
Before deployment and during monitoring:
- Test performance across protected characteristic groups
- Identify disparate impact in outcomes
- Analyze for proxy discrimination (using non-protected attributes)
- Document findings and corrective actions

#### Specific High-Risk Considerations
- Employment systems: test across gender, age, ethnicity
- Credit systems: test across protected financial characteristic groups
- Biometric systems: test accuracy across demographics
- Critical infrastructure: test resilience for diverse operating conditions

---

## Article 13: Transparency and Information

**Official Designation**: Transparency and information obligations

### Purpose
Individuals affected by high-risk AI systems must have sufficient information to understand and exercise their rights.

### Transparency Requirements

#### 1. Notification Requirement
Users must be informed:
- They are interacting with an AI system (not a human)
- OR they are subject to decisions made by an AI system

#### 2. Meaningful Information
Users must receive:
- Explanation of system purpose and decision logic
- Information about their rights
- How to request human intervention
- Contact for questions and complaints
- How their data will be used

#### 3. Right to Human Intervention
Users must know:
- They can request human review of automated decision
- There is a process to contest the decision
- They can request explanation of the decision
- Timeline for human decision

#### 4. Record Keeping
For AI-generated content, maintain:
- Record that content was created by AI
- Record of authenticity assessments
- Ability to retrieve generated content records
- Audit trail of generation parameters

### Use-Case Specific Examples

#### Employment Systems
Notify candidates:
- Resume screening uses AI
- How candidates can appeal
- What factors are reviewed
- How to request human review

#### Credit Systems
Notify applicants:
- AI assessed creditworthiness
- Main factors in decision
- How to request explanation
- How to appeal the decision

#### Biometric Systems
Notify individuals:
- Biometric identification is in use
- What biometric data is collected
- How long data is retained
- Rights regarding their data

---

## Article 14: Human Oversight

**Official Designation**: Human oversight requirements

### Purpose
High-risk systems must be designed so humans can effectively supervise, understand, and override AI decisions.

### Design Principles

#### 1. Meaningful Oversight Mechanism
System must enable humans to:
- Understand AI recommendation/decision
- Assess appropriateness in context
- Decide whether to act on, modify, or reject decision
- Intervene and override when necessary

#### 2. Information for Oversight
Provide decision-makers with:
- Clear explanation of AI reasoning
- Confidence/uncertainty metrics
- Input data that influenced decision
- Historical accuracy information
- Relevant external context

#### 3. Override Capability
Users must have ability to:
- Stop execution of AI decision before implementation
- Reverse decisions already made
- Modify or adjust AI recommendations
- Escalate to higher authority

#### 4. Well-Designed Process
Human oversight must be:
- Integrated into actual workflows
- Not a "rubber stamp" (meaningful review)
- Proportionate to risk level
- Monitored for effectiveness

### Operationalization Examples

#### Employment Recruitment
- Hiring manager reviews AI-flagged candidates
- Can reject AI recommendations
- Can add candidates AI didn't flag
- Documents reasons for overrides

#### Credit Decisions
- Reviewer explains decision  logic to applicant
- Reviews for unintended discrimination
- Can approve exceptions to automated rules
- Logs override rationale

#### Critical Infrastructure
- Operator monitors AI control recommendations
- Can override at any time
- Manual controls always available
- 24/7 human oversight capability

---

## Key Principles Across All Articles

### 1. Proportionality
Compliance measures must be proportionate to:
- Risk level and severity
- Likelihood of harmful outcomes
- Number of people affected
- Sensitivity of decisions

### 2. Context
Risk assessment and controls must consider:
- Actual deployment context
- Stakeholder capabilities
- Available technology
- Organizational maturity

### 3. Human-Centered
All safeguards must:
- Protect human dignity and autonomy
- Enable meaningful human decision-making
- Respect rights and freedoms
- Account for diverse needs

### 4. Practical Implementation
Requirements must be:
- Implementable with existing technology
- Scalable across organization
- Monitorable and auditable
- Continuously improved

---

**Last Updated**: March 12, 2026  
**Regulation Reference**: EU 2024/1689  
**For Official Text**: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
