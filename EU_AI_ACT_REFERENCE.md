# EU AI Act - Legal Reference Framework

**Last Updated:** March 12, 2026  
**Document Version:** 1.0  
**Regulation:** Regulation (EU) 2024/1689 on Artificial Intelligence (AI Act)  
**Official Entry into Force:** August 1, 2024  
**Current Implementation Status:** Phased rollout through 2026

---

## Executive Summary

This document provides the legal foundation for the AI Compliance Sherpa's assessment framework. It maps:

1. **Which EU AI Act articles are referenced** in our compliance criteria
2. **How each article applies** to the six mandatory compliance questions (Q5-Q10)
3. **What obligations** systems in each category must meet
4. **How to keep this framework current** as EU AI regulations evolve

Our system focuses on **Business-to-Business (B2B) software products** covering Finance, Accounting, HR, and related business functions. We have removed Education-specific criteria as they are not applicable to your product portfolio.

---

## Table of Contents

1. [Articles Referenced](#articles-referenced)
2. [Article-to-Question Mapping](#article-to-question-mapping)
3. [Risk Classification Framework](#risk-classification-framework)
4. [Compliance Obligations by Category](#compliance-obligations-by-category)
5. [Current Implementation Timeline](#current-implementation-timeline)
6. [Keeping This Document Current](#keeping-this-document-current)
7. [Additional Resources](#additional-resources)

---

## Articles Referenced

### Core Prohibition Articles

#### **Article 5: Prohibited AI Practices**

**Scope:** Practices that violate fundamental rights and freedoms.

**Specific Prohibitions:**
- Placing on the market, putting into service, or use of AI systems intended to:
  - Deploy subliminal or manipulative techniques beyond a person's consciousness to distort behavior/decision-making
  - Exploit vulnerable groups or their vulnerabilities
  - Create social scores based on social behavior or personal characteristics predicting future conduct (social credit scoring)
  - Use real-time remote biometric identification in public spaces for law enforcement (with narrow exceptions)

**Applicability to Your Systems:**
- ✅ **Q7 (Biometric Identification):** If you develop real-time remote facial recognition or similar biometric systems for law enforcement use, Article 5 applies → **PROHIBITED**
- ⚠️ **Q5, Q6, Q10:** If employment, finance, or HR systems use subliminal manipulation or vulnerable group targeting → **PROHIBITED**

**Current Status:** Article 5 prohibitions entered into force August 1, 2024

---

### High-Risk AI Systems (Annex I)

#### **Article 6: Classification of High-Risk AI Systems**

**Scope:** Systems that pose significant risks to fundamental rights and safety.

**Applicability:** High-risk classification applies when:
1. System falls under one of the Annex I categories, AND
2. System makes or significantly influences autonomous decisions affecting fundamental rights

**Annex I Categories (Relevant for B2B Software):**

| Category | Applies to | Your Questions |
|----------|-----------|---|
| **1. Biometric Systems** | Real-time biometric identification and emotion/behavior detection systems at a distance | Q7 |
| **2. Critical Infrastructure** | AI controlling or managing critical infrastructure (power, water, transport, digital infrastructure) | Q9 |
| **3. (Removed - Education)** | Educational systems admission/assignment | NOT APPLICABLE |
| **(Implied) 4. Employment** | Recruitment, selection, promotion, termination; performance monitoring; worker tasks | Q5, Q6 |
| **(Implied) 5. Finance** | Credit scoring, credit eligibility assessment, access to essential financial and insurance services | Q10 |

**High-Risk Requirements (Articles 6, 4, 9-14):**

Systems classified as high-risk must:
- ✅ Conduct and document risk assessments (Article 9)
- ✅ Implement and maintain quality management systems
- ✅ Maintain technical documentation
- ✅ Implement human oversight capabilities (Article 14)
- ✅ Provide transparency to users (Article 13)
- ✅ Maintain logs and audit trails
- ✅ Conduct accuracy, robustness, cybersecurity assessments
- ✅ Provide clear information when system is in use

**Implementation Deadline:** February 2, 2025 (for systems already deployed January 1, 2025)

---

### General Transparency Articles

#### **Article 13: Transparency and Information to Users**

**Applies to:**
- Users of high-risk AI systems
- Natural persons interacting with emotion detection or biometric categorization systems
- Any person affected by AI decisions from high-risk systems

**Obligations:**
- Inform users that an AI system is being used
- Inform users about the system's capabilities and limitations
- Provide meaningful information about decisions that significantly affect the person
- Enable contestation and remedy mechanisms

**Relevance to Your Systems:** If any of Q5-Q10 answer "Yes," Article 13 applies.

---

#### **Article 14: Human Oversight**

**Definition:** Meaningful human operation and oversight that ensures humans can understand, monitor, and interrupt AI decisions.

**Requirements for High-Risk Systems:**
- Humans must be involved in important decisions
- Systems must be designed to enable human oversight
- Humans must have ability to understand outputs and override decisions
- Humans must be trained on system use and limitations
- Monitoring must not be pure post-hoc review; it must enable intervention

**Your Question Relevance:**
- Q5 (Recruitment): Recruiters must review system recommendations before decisions
- Q6 (Employment): HR must be able to monitor and override performance evaluations
- Q10 (Credit): Credit officers must review and confirm AI recommendations

---

## Article-to-Question Mapping

### Summary Table

| Question | Topic | Articles | Classification |
|----------|-------|----------|---|
| **Q5** | Recruitment/Selection Decisions | 6, 9, 13, 14 | HIGH_RISK |
| **Q6** | Employment Conditions/Performance | 6, 9, 13, 14 | HIGH_RISK |
| **Q7** | Biometric Identification | 5 (prohibited), 6, 9, 13, 14 | HIGH_RISK or PROHIBITED |
| **Q8** | Sensitive Attribute Categorization | 9, 10 (fairness) | LIMITED_RISK |
| **Q9** | Critical Infrastructure | 6, 9, 13, 14 | HIGH_RISK |
| **Q10** | Credit/Finance Decisions | 6, 9, 13, 14 | HIGH_RISK |

### Detailed Mappings

#### **Q5: Recruitment/Selection Decisions**

**Legal Basis:**
- EU AI Act Annex I (4): "AI systems used by employment services to match job applicants with job offers or to filter candidates"
- Same article: "AI systems intended to be used for other employment decisions that significantly affect workers' working conditions"

**Applicable Articles:**
- **Article 6:** Classification as high-risk
- **Article 9:** Risk management and assessment requirements
- **Article 13:** Transparency obligations to job applicants
- **Article 14:** Human oversight - recruiters must review before hiring decisions

**What This Means:**
If your HR or recruitment software uses AI to screen resumes, match candidates, or rank applicants:
- ✅ Classification: **HIGH_RISK**
- ✅ You must conduct a risk assessment documenting how the system could bias outcomes
- ✅ Provide job applicants with information that an AI system was used in their evaluation
- ✅ Ensure recruiters can review and override system recommendations
- ✅ Document that discriminatory outcomes (unequal impact) do not occur

**Compliance Actions Required:**
1. Document training data sources and composition
2. Conduct bias and accuracy testing
3. Test for protected Class A discrimination concerns
4. Implement recruiter review process before any reject decisions
5. Maintain audit logs of all recruiting decisions
6. Provide "explainability" of why candidates ranked differently

---

#### **Q6: Employment Conditions/Performance**

**Legal Basis:**
- EU AI Act Annex I (4): "AI systems to monitor and evaluate workers' performance..."
- Same: "Systems intended to monitor, detect, or report behavior of workers..."

**Applicable Articles:**
- **Article 6:** High-risk classification
- **Article 9:** Risk assessment and management
- **Article 14:** Human oversight - workers/managers must be able to override/contest
- **Article 13:** Transparency obligations to workers

**What This Means:**
If your product monitors, evaluates, or makes recommendations about employee performance, attendance, productivity, or work allocation:
- ✅ Classification: **HIGH_RISK**
- ✅ Workers have the right to know they're being monitored
- ✅ Managers must retain ability to override AI recommendations
- ✅ System must not use opaque "black box" metrics
- ✅ Non-discrimination requirements apply

**Compliance Actions Required:**
1. Notify employees that performance monitoring AI is in use
2. Explain what metrics are being assessed
3. Ensure transparency in how performance scores are calculated
4. Verify system doesn't discriminate across protected groups
5. Allow employees to contest and request review
6. Provide managers with ability to adjust recommendations
7. Maintain audit trails of all decisions/overrides

---

#### **Q7: Biometric Identification**

**Legal Basis:**
- **Article 5:** "Real-time remote biometric identification" (live facial recognition) is **PROHIBITED** for law enforcement with narrow exceptions
- **Article 6, Annex I(1):** Non-real-time biometric identification (physical verification at location, stored comparison) is HIGH_RISK

**Applicable Articles:**
- **Article 5:** Prohibition (if real-time remote)
- **Articles 6, 9, 10, 13, 14:** High-risk requirements (if non-real-time)

**What This Means:**

**If your system does real-time remote biometric ID (e.g., live facial recognition for building access control):**
- ❌ You likely **CANNOT** deploy it in law enforcement contexts
- ⚠️ Review narrow exceptions for very specific use cases
- ⚠️ Non-law-enforcement uses may face increasing restrictions

**If your system does non-real-time biometric ID (e.g., fingerprint verification for building entry, employee authentication):**
- ✅ Classification: **HIGH_RISK**
- ✅ Must include accuracy/robustness testing
- ✅ Must comply with data protection (GDPR) requirements
- ✅ Users must be informed biometric data is being collected
- ✅ Must maintain extensive technical documentation

**Compliance Actions Required:**
1. Verify whether system is real-time remote (prohibited) or non-real-time (high-risk)
2. If real-time remote: Document narrow law enforcement exceptions or discontinue use
3. If non-real-time: Ensure GDPR biometric data processing compliance
4. Conduct accuracy/false positive rate testing
5. Document security measures protecting biometric data
6. Test for demographic bias (e.g., facial recognition accuracy rates by ethnicity)
7. Maintain logs of all biometric authentication events

---

#### **Q8: Sensitive Attribute Categorization**

**Legal Basis:**
- **Article 9(1):** Risk assessment must cover "risks of unlawful discrimination" occurring as a result of the AI system not functioning as intended
- **Article 10:** Specific obligations for AI systems not classified as high-risk but that process sensitive attributes

**Applicable Articles:**
- **Article 9:** Risk assessment including discrimination risks
- **Article 10:** Fairness and non-discrimination standards

**What This Means:**
If your system (even if not explicitly high-risk) infers or uses protected characteristics (race, religion, gender, disability, etc.):
- ✅ Classification: **LIMITED_RISK** or higher
- ✅ Must conduct fairness/anti-discrimination assessment
- ✅ Must test for disparate impact on protected groups
- ✅ Must monitor for proxy discrimination (using non-protected attributes that correlate with protected attributes)

**Examples:**
- HR system that infers gender from name/profile picture
- Finance system that uses postal codes (proxy for race/origin)
- Recruitment system that uses educational background as proxy for gender

**Compliance Actions Required:**
1. Identify any protected characteristics in training data
2. Test system outputs for disparate impact by protected group
3. Implement fairness metrics (demographic parity, equalized odds)
4. Document proxy variables that could correlate to protected characteristics
5. Implement monitoring for fairness after deployment
6. Conduct periodic fairness audits

---

#### **Q9: Critical Infrastructure**

**Legal Basis:**
- **EU AI Act Annex I (5):** "AI systems intended to be used as safety components of machinery or in critical infrastructure"
- Critical infrastructure definition covers: power, water supply, wastewater, transportation, health, digital infrastructure

**Applicable Articles:**
- **Article 6, Annex I(5):** High-risk classification
- **Article 9:** Risk assessment and management
- **Article 14:** Human oversight for safety-critical decisions
- **Article 13:** Transparency about AI involvement

**What This Means:**
If your product controls, monitors, or makes safety-critical decisions in:
- ⚡ Power grid management, renewable energy distribution
- 💧 Water/wastewater treatment control systems
- 🚗 Transportation routing, traffic management, rail systems
- 📡 Digital infrastructure (cloud, DNS, network management)
- 🏥 Hospital IT infrastructure

Then:
- ✅ Classification: **HIGH_RISK**
- ✅ Failures could affect safety, availability, or security of essential services
- ✅ Extensive testing required before deployment
- ✅ Continuous monitoring and update mechanisms required
- ✅ Human override capabilities mandatory

**Compliance Actions Required:**
1. Conduct FMEA (Failure Mode and Effects Analysis) or similar
2. Define failure modes and safety impact
3. Test system under normal, degraded, and failure conditions
4. Document rollback/recovery procedures
5. Implement 24/7 monitoring and alerting
6. Ensure humans can immediately take control if needed
7. Document all patches/updates and their safety implications
8. Conduct regular safety audits and penetration testing

---

#### **Q10: Credit/Finance Decisions**

**Legal Basis:**
- **EU AI Act Annex I (2):** "AI systems intended to evaluate the creditworthiness of natural persons or establish their credit score, except for AI systems whose failure or malfunction does not pose any risk of material damage to financial interests"
- Also covers: access to banking services, mortgages, insurance underwriting for essential coverage

**Applicable Articles:**
- **Article 6, Annex I(2):** High-risk classification
- **Article 9:** Risk assessment (including non-discrimination)
- **Article 13:** Transparency to applicants (must disclose AI involvement)
- **Article 14:** Human oversight (credit officers review recommendations)

**What This Means:**
If your finance/accounting product uses AI to:
- 💳 Score creditworthiness or determine credit limits
- 🏦 Assess loan/mortgage eligibility
- 📊 Determine insurance rates or coverage
- 💰 Make financial access decisions

Then:
- ✅ Classification: **HIGH_RISK**
- ✅ Applicants must be informed an AI system was used
- ✅ System must provide explainability (why was application denied/approved?)
- ✅ Credit officers must be able to override decisions
- ✅ Must test for demographic disparate impact
- ✅ Must comply with financial services regulations (EU Consumer Credit Directive, etc.)

**Compliance Actions Required:**
1. Document which features drive credit approval/denial decisions
2. Test for lending discrimination by protected characteristics
3. Implement decision explanations ("explainability")
4. Provide applicants with information about AI involvement and right to contest
5. Maintain audit logs of all credit decisions
6. Test for feedback loops that could create discrimination (e.g., if denying credit to certain groups reduces their future credit history)
7. Conduct periodic bias/fairness audits
8. Document accuracy testing and performance metrics

---

## Risk Classification Framework

### How Answers Map to Risk Levels

```
IF ANY QUESTION (Q5-Q10) Answered "YES" →
    AND System makes autonomous decisions affecting fundamental rights →
        THEN Classification = HIGH_RISK
        OBLIGATIONS: Articles 6, 9, 13, 14 (full high-risk regime)
    ELSE IF Limited autonomy or strong human oversight →
        THEN Classification = LIMITED_RISK
        OBLIGATIONS: Article 10 (fairness), monitoring requirements
ELSE IF System categorizes sensitive attributes (Q8) →
    AND Makes inferences about protected characteristics →
        THEN Classification = LIMITED_RISK
        OBLIGATIONS: Anti-discrimination testing, fairness monitoring
ELSE →
    Classification = MINIMAL_RISK
    OBLIGATIONS: Transparency, general AI ethics best practices
```

### Article 5 Override (Prohibition)

If Q7 = real-time remote biometric identification used for law enforcement:
```
    CLASSIFICATION = PROHIBITED (regardless of other answers)
    PROHIBITION: Cannot be deployed for law enforcement
    EXCEPTION: Only in narrow circumstances (EU Member State exceptions)
```

---

## Compliance Obligations by Category

### HIGH-RISK Systems (Any Q5, Q6, Q7, Q9, Q10 = "Yes")

**Article 9: Risk Management**

Obligation: Establish and implement risk management system covering:

1. **Assessment Phase:**
   - Likelihood of harm (moderate, high, critical)
   - Magnitude of potential impact
   - Vulnerability of affected groups
   - System failure hazards

2. **Mitigation Phase:**
   - Technical measures (validation, accuracy testing)
   - Operational measures (human oversight, monitoring)
   - Governance measures (documentation, policies)

3. **Monitoring Phase:**
   - Continuous monitoring after deployment
   - Real-world performance tracking
   - Incident reporting and escalation

**Your Action:** Create a risk management plan document for your product

---

**Article 10: Data Quality and Governance**

Obligation: Ensure training data is:
- Relevant and representative
- Free from documented bias and errors
- Properly labeled and validated
- Documented with provenance

**Your Action:** Audit training data sources for your models

---

**Article 13: Transparency Requirements**

Obligation: Inform affected persons:
- That an AI system is being used
- What the system is designed to do
- What factors influenced the decision
- Limitations and expected accuracy
- How to seek human review or appeal

**Your Action:** Update product UX to clearly disclose AI involvement with affected users

---

**Article 14: Human Oversight**

Obligation: Enable meaningful human oversight:
- Humans can understand system outputs
- Humans can access explanation/reasoning
- Humans can override and reverse decisions
- Humans receive training and clear procedures
- Decisions cannot be fully automated for high-impact outcomes

**Your Action:** Ensure product allows HR managers, credit officers, etc. to review and override AI recommendations

---

### LIMITED-RISK Systems (Q8 = "Yes" or soft dependencies)

**Article 10: Fairness and Non-Discrimination**

Obligation:
- Assess risk of unlawful discrimination
- Test for disparate impact
- Monitor for proxy discrimination
- Implement fairness metrics

**Your Action:** Add fairness testing to QA procedures

---

## Current Implementation Timeline

### Dates Critical to Compliance

| Date | Event | Impact |
|------|-------|--------|
| **Aug 1, 2024** | ✅ Article 5 prohibitions enter into force | Real-time remote biometric ID ban effective |
| **Feb 2, 2025** | Deadline for high-risk systems already deployed | Compliance deadline for existing systems |
| **May 2, 2025** | Transitional period for classification ends | All systems must be reclassified under new definitions |
| **May 2, 2026** | Downstream requirements fully effective | Human oversight, transparency, documentation fully required |
| **Nov 2, 2026** | Prohibited practices ban fully enforced | No new prohibited systems can be placed on market |

---

## Keeping This Document Current

### How EU AI Regulations Evolve

The EU AI Act is a **living regulation** with:
- Annual review requirements (Article 75)
- Commission power to issue delegated acts clarifying definitions
- Regular guidance publication by the AI Office (new EU agency)
- Court decisions continuously interpreting obligations

### Your Responsibility: Monitoring Changes

To keep the compliance system current, you should:

#### **1. Monthly Review** (15 minutes)
- Subscribe to **EU AI Office newsletter** (launches 2025)
- Monitor **European Commission AI news** (ec.europa.eu/newsroom)
- Check **Digital Services Box** compliance news (EUR-Lex)

**Action:** Set calendar reminder to check these sources 1st Friday of each month

---

#### **2. Quarterly Review** (30-60 minutes)
- Review **EDPB guidance** on AI and GDPR (edpb.europa.eu)
- Check **Industry association guidance**:
  - TechUK AI Working Group
  - CCIA Europe position papers
  - Your industry body's AI publications
- Review **Case law** affecting your sector

**Action:** Quarterly meeting agenda: "EU AI Act Regulatory Update"

---

#### **3. Annual Review** (2-4 hours)
- Complete assessment of regulation changes
- Review EU AI Office guidance updates
- Assess impact on your product compliance
- Update this document and questionnaire if needed
- Report recommendations to leadership

**Action Structure:**
- Audit this document version against official EU AI Act text
- Identify any criteria/articles no longer current
- Propose messaging updates to comply with newest guidance
- Train compliance officer on updates

---

### Official Sources for Updates

**Primary Sources:**
1. **EUR-Lex** (eur-lex.europa.eu) - Official EU legal database
   - Search: "Regulation (EU) 2024/1689"
   - Subscribe to amendments/corrigenda

2. **European AI Office** (sera.ai)
   - Launches February 2025
   - Will publish guidance documents and clarifications

3. **EDPB** (edpb.europa.eu) - Data Protection Board
   - Guidance on AI + GDPR intersection

4. **National DPA Websites**
   - Each Member State's Data Protection Authority publishes AI guidance
   - Example: UK ICO (ico.org.uk) posts AI guidance

**Secondary Sources:**
5. **LSE AI Society Policy Research** (lse.ac.uk/granthaminstitute)
6. **Stanford AI Index** (aiindex.stanford.edu) - tracks EU developments
7. **MIT - Center for Civic Media** - AI regulation tracking
8. **Brookings AI Governance tracker** (brookings.edu)

---

### What to Reassess When Regulations Change

Whenever new EU AI guidance or court decisions emerge, reassess:

**Yellow Flag Changes** (Update documentation, no product change):
- Clarifications about article interpretations
- New guidance that aligns with your current practices
- Helpful case law supporting your compliance approach

**Orange Flag Changes** (May require product updates):
- New requirements for existing high-risk categories
- Expanded definition of "fundamental rights" affecting your use cases
- New transparency or human oversight requirements

**Red Flag Changes** (Immediate escalation):
- New article prohibiting your current system type
- Enforcement actions against similar products
- New data protection or fairness requirements making current approach non-compliant

---

## Additional Resources

### Official EU Documentation
- **Full EU AI Act Text:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **Executive Summary:** https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- **Consumer Rights Portal:** https://digital-strategy.ec.europa.eu/en/policies/artificial-intelligence

### Guidance Documents (When Published)
- EU AI Office Implementation Guidelines (Feb 2025+)
- Commission delegated acts on high-risk categories
- National implementation guidance from your country's DPA

### Industry Guidance
- Your industry body's AI compliance guidance
- Legal counsel specializing in EU AI Act
- Compliance consultants with EU AI expertise
- Audit firms' AI governance frameworks

---

## Document Management

| Element | Details |
|---------|---------|
| **Current Version** | 1.0 - Published March 12, 2026 |
| **Next Review Date** | June 12, 2026 (Quarterly) |
| **Maintained By** | Legal/Compliance Officer |
| **Approval Authority** | Chief Legal Officer |
| **Distribution** | All product teams, QA, Legal, Customer Success |

### Change History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| Mar 12, 2026 | 1.0 | Initial document created, focused on B2B software (Finance, HR, Accounting). Removed education-specific criteria. | Compliance Team |
| | | | |

---

## Questions or Clarifications?

If product teams have questions about:
- Whether a feature falls under high-risk categories
- How to implement Article 13 transparency requirements
- What documentation is needed for Article 9 risk assessments
- How to test for Article 10 fairness requirements

→ **Contact:** Legal/Compliance Officer or Product Counsel

---

**DISCLAIMER:** This document provides educational information about the EU AI Act. It is not legal advice. For binding interpretation and legal obligations, consult with qualified legal counsel specializing in EU AI regulations.

