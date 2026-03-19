# Article 6: Classification of High-Risk AI Systems

## Title
Classification of high-risk AI systems (EU Regulation 2024/1689)

## Overview
Article 6 defines which AI systems are classified as "high-risk" and therefore subject to stringent compliance requirements. This is the central provision for determining if a system triggers high-risk obligations.

## Definition
An AI system is classified as high-risk where both:
1. The AI system is intended to be used as a safety component or in a safety-related system, **OR**
2. The AI system is listed in Annex III (before implementation, this means Annex I examples)

**AND** the AI system produces legal or similarly significant effects on natural persons

## Annex I: High-Risk AI Categories (Key Examples)

### 1. **Biometric identification and categorization**
- Real-time facial recognition
- Emotion recognition systems
- Biometric analysis for classification

### 2. **Critical infrastructure**
- Management of electricity grids
- Water supply systems
- Gas infrastructure
- Autonomous railway systems

### 3. **Education and training**
- AI systems determining school placement
- Recommending educational content
- Assessing student performance
- Admissions decisions

### 4. **Employment and workers**
- Recruitment and screening
- Performance management decisions
- Contract termination recommendations
- Salary determination

### 5. **Law enforcement**
- Crime predication
- Assessment of criminal risk
- Suspect identification
- Border control processing

### 6. **Administration of justice and democratic processes**
- Legal rule interpretation
- Case outcome prediction
- Bail decisions
- Sentencing recommendations

### 7. **Access to and enjoyment of essential services and benefits**
- **Credit scoring** for loans, mortgages
- Access to healthcare services
- Social welfare benefits determination
- Housing determination

### 8. **Migration and asylum**
- Authenticity of travel documents
- Asylum application assessment
- Risk profiling of migrants

## Key Legal Test

A system is HIGH-RISK if:

```
┌─ Is it a safety component? → HIGH-RISK
│
├─ Is it in Annex I list? 
│  ├─ Employment decisions? → HIGH-RISK
│  ├─ Education access? → HIGH-RISK
│  ├─ Credit/essential services? → HIGH-RISK
│  ├─ Law enforcement? → HIGH-RISK
│  ├─ Biometric categorization? → HIGH-RISK
│  └─ Critical infrastructure? → HIGH-RISK
│
└─ Does it produce legal or similarly significant effects?
   └─ Yes → HIGH-RISK
   └─ No → Check LIMITED-RISK or MINIMAL-RISK
```

## "Legally Significant Effects" Definition

Effects include:
- Determining eligibility for employment
- Determining creditworthiness
- Access to education
- Determining criminal risk
- Affecting constitutional/human rights
- Determining benefit eligibility
- Creating legal liability

## High-Risk Compliance Obligations (Article 8-17)

When classified as HIGH-RISK, systems must:

### 1. **Risk Assessment (Article 9)**
- Document potential risks before deployment
- Assess technical and organizational measures
- Evaluate effectiveness of risk mitigation

### 2. **Human Oversight (Article 14)**
- Ensure qualified humans can understand and intervene
- Provide meaningful oversight capability
- Implement intervention mechanisms

### 3. **Documentation (Article 11)**
- Technical documentation and risk register
- Quality assurance procedures
- Data handling and governance records

### 4. **Transparency (Article 13)**
- Users must know they're interacting with AI
- Explain AI decision-making
- Document AI recommendations clearly

### 5. **Data Governance (Article 10)**
- High-quality training data standards
- Bias and discrimination testing
- Ongoing monitoring and auditing

### 6. **Monitoring (Article 15)**
- Continuous performance monitoring
- Incident reporting mechanisms
- Log retention and analysis

## Examples by Category

### ✅ HIGH-RISK Examples
1. **Resume Screening**: Autonomous recruiting decision based on resume analysis, education history
2. **Credit Scoring**: Determining loan eligibility automatically
3. **Student Assessment**: AI determining school placement or educational advancement
4. **Crime Prediction**: Using AI to predict criminal risk for bail/parole decisions
5. **Benefits Determination**: Assessing disability benefits eligibility

### ❌ NOT HIGH-RISK (Minimal or Limited Risk)
1. **Spam Filter**: Automated filtering doesn't affect fundamental rights
2. **Content Recommendation**: Suggesting posts/products doesn't create legal effects
3. **Virtual Assistant**: Scheduling assistant doesn't affect rights
4. **Chatbot**: Customer service bot providing information only

## Decision Tree for Classification

```
Step 1: Does it affect fundamental rights, safety, or legal outcomes?
  NO → Check Limited-Risk / Minimal-Risk
  YES → Continue

Step 2: Is it in one of the Annex I categories?
  NO → Check limited safety components
  YES → HIGH-RISK

Step 3: Does it make autonomous decisions affecting people?
  NO → Perhaps not high-risk if only advisory
  YES → HIGH-RISK

Conclusion → HIGH-RISK
```

## Non-High-Risk Safety Components (Limited)

Some safety systems are not high-risk if they:
- Provide information support only (advisory, not autonomous)
- Require human review before implementation
- Cannot override human decision-making
- Are transparent about AI involvement

---

## Transitional Provisions (Important)

Applications cannot classify systems as high-risk "in isolation." Regulators will provide:
- Guidance on Annex III final list
- Safe harbor provisions for compliance efforts
- Conformity assessment procedures (CE mark equivalent)

## Related Articles
- Article 5: Prohibited practices
- Articles 8-17: Technical requirements for high-risk systems
- Article 76: Enforcement and fines
- Annex III: Final high-risk list (evolving over time)
