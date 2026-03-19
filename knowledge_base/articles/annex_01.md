# Annex I: High-Risk AI Systems Categories

## Overview
This document provides practical guidance on Annex I categories - the classifications that determine if an AI system is high-risk under Article 6 of the EU AI Act.

## Category 1: Biometric Identification and Categorization

### Definition
AI systems used for the purpose of identification, authentication, and categorization of natural persons based on physical or behavioral characteristics.

### Sub-Categories

#### 1.1: Real-Time Facial Recognition
**Scope**: Live identification/authentication of individuals from video/camera feeds

**HIGH-RISK Examples**:
- Border control systems scanning arrivals in real-time
- Law enforcement facial recognition at protests
- Airport biometric gates matching live faces
- Street surveillance matching to wanted persons database

**NOT HIGH-RISK Examples**:
- Post-recognition identification (analyzing footage after incident)
- Consensual airport security gates (travelers knowingly use)
- Photo ID matching using static images

**Requirements if HIGH-RISK**:
- Explicit human authorization before identification
- Accuracy testing and bias evaluation
- Audit trails and logging
- Clear data retention limits
- Right to refuse consent

#### 1.2: Emotion Recognition
**Scope**: AI analyzing facial expressions or vocal patterns to infer emotions/mental states

**HIGH-RISK Examples**:
- HR systems assessing employee engagement from video
- Customer service monitoring satisfaction from facial expressions
- Security systems flagging "suspicious" emotional states

**NOT HIGH-RISK Examples**:
- Voluntary emotion rating in entertainment apps
- Animated character responding to user expressions (no decision)

#### 1.3: Biometric Categorization
**Scope**: Classification into demographic or behavioral groups using biometric data

**HIGH-RISK Examples**:
- Gender classification for targeted policing
- Age estimation used for benefit eligibility
- "Threat assessment" based on facial features

---

## Category 2: Critical Infrastructure Management

### Definition
AI systems controlling or managing infrastructure essential to society.

### Key Systems

- **Electricity Grids**: AI managing power distribution, load balancing, pricing
- **Water Systems**: Treatment plant control, quality monitoring, distribution
- **Gas Infrastructure**: Supply management, leak detection, safety systems
- **Transportation**: Autonomous train systems, traffic signal control
- **Telecommunications**: Network management affecting service continuity

### Decision Factors

HIGH-RISK if:
- Loss of system could cause public harm
- Affects availability of essential services
- Makes autonomous or safety-critical decisions
- Cannot be manually overridden in reasonable time

---

## Category 3: Education and Training Systems

### Definition
AI systems making determinations about educational access, progression, or outcomes.

### HIGH-RISK Examples
1. **Admissions**: AI ranking applications, determining who gets admitted
2. **Placement**: Assigning students to schools or educational tracks (streaming)
3. **Assessment**: Evaluating student performance with legal consequences
4. **Content Recommendation**: Suggesting educational programs with enrollment effects

### NOT HIGH-RISK Examples
- Personalized tutoring systems students choose voluntarily
- Vocabulary learning apps
- Administrative automation (scheduling, grade recording)

### Legal Basis
Educational decisions affect access to opportunities and social mobility - therefore legally significant effects.

---

## Category 4: Employment and Workers

### Definition
AI systems making determinations about employment decisions affecting individuals.

### HIGH-RISK Examples

#### 4.1: Recruitment & Screening
- Resume screening removing candidates from consideration
- Assessment tests determining merit/fit
- Video interview analysis ranking candidates
- Background screening for employment eligibility

#### 4.2: Performance Management
- Systems evaluating employee performance/productivity
- Algorithms determining promotions/advancement
- Systems recommending termination
- Remote work monitoring systems with employment consequences

#### 4.3: Compensation
- AI determining salary or pay bands
- Systems recommending bonuses/raises
- Algorithms for shift assignment (affecting hours)

### Key Requirement: **Meaningful Human Oversight**
All high-risk employment AI must have human review that can override recommendations before implementation.

---

## Category 5: Law Enforcement

### Definition
AI systems used by police, prosecutors, or law enforcement for operational decisions.

### HIGH-RISK Examples

#### 5.1: Risk Assessment
- Predicting criminal recidivism for parole decisions
- Risk scoring for bail/release recommendations
- Threat assessment determining investigation priority

#### 5.2: Crime Prediction & Profiling
- Predictive policing determining patrol areas
- Crime hotspot prediction systems
- Gang/criminal network identification

#### 5.3: Suspect Identification
- Facial recognition for suspect matching
- Gait recognition matching suspects
- Behavioral pattern matching

#### 5.4: Evidence Analysis
- Forensic analysis automation (DNA, fingerprints)
- Evidence correlation systems
- Crime pattern analysis recommending investigations

### Critical Safeguard: **Narrow Exceptions**
Real-time biometric identification by law enforcement is **PROHIBITED** except:
1. Searching for a specifically identified known person (wanted criminal, missing person)
2. Preventing imminent threat to public safety

**NOT Permitted**: General surveillance, mass identification of crowds, or predictive searches.

---

## Category 6: Administration of Justice and Democratic Processes

### Definition
AI systems assisting in judicial decisions or affecting democratic processes.

### HIGH-RISK Examples

#### 6.1: Judicial Decisions
- Systems predicting case outcomes
- Bail decision recommendations
- Sentencing recommendations
- Appeals assessment

#### 6.2: Democratic Processes
- Voter eligibility determination
- Redistricting/boundary drawing
- Candidate ballot access determination

### Special Concern
These systems affect the right to fair trial and democratic participation - fundamental constitutional rights.

---

## Category 7: Access to Essential Services

### Definition
AI systems determining access to goods, services, or benefits essential to human dignity.

### HIGH-RISK Examples

#### 7.1: Financial Services (MOST COMMON)
- **Credit Scoring**: Loan, mortgage, credit card eligibility
- **Insurance**: Underwriting and pricing decisions
- **Banking**: Account opening, transaction reviews

#### 7.2: Healthcare Services
- Triage and priority determination
- Transplant recipient selection
- Treatment eligibility decisions
- Denial of coverage recommendations

#### 7.3: Social Welfare & Benefits
- Unemployment benefit eligibility
- Disability assessment
- Housing assistance determination
- Food assistance eligibility

#### 7.4: Housing & Accommodation
- Rental application screening
- Mortgage approval decisions
- Eviction risk prediction

### Rationale
These services are deemed "essential" because without them, people cannot meet basic human needs or achieve social participation.

---

## Category 8: Migration and Asylum

### Definition
AI systems managing immigration, asylum, or border processes.

### HIGH-RISK Examples

1. **Document Authenticity**: Assessing whether travel documents are genuine
2. **Risk Assessment**: Evaluating asylum/migration risk profiles
3. **Border Decisions**: Determining entry/exit authorization
4. **Asylum Determination**: Recommending adoption/rejection of asylum claims

### Rationale
Migration decisions affect:
- Right to movement (freedom of residence)
- Protection from persecution
- Family unity
- Access to employment and services

---

## Decision Framework for Each Category

### Quick Assessment

```
For any AI system, ask:

1. Does it involve biometric identification/categorization? → Art.6 Category 1
2. Does it control critical infrastructure? → Art.6 Category 2
3. Does it affect educational access/progression? → Art.6 Category 3
4. Does it make employment decisions? → Art.6 Category 4
5. Does law enforcement use it for decisions? → Art.6 Category 5
6. Does it affect judicial/democratic processes? → Art.6 Category 6
7. Does it determine access to essential services? → Art.6 Category 7
8. Does it affect migration/asylum decisions? → Art.6 Category 8

If YES to ANY: → HIGH-RISK (requires full compliance)
If NO to ALL: → Check LIMITED-RISK or MINIMAL-RISK
```

---

## Compliance Pathway for High-Risk Systems

Once classified as HIGH-RISK under any Annex I category:

1. **Immediate**: Conduct risk assessment (Article 9)
2. **Within 30 days**: Engage compliance team
3. **Within 90 days**: Implement human oversight (Article 14)
4. **Within 6 months**: Complete technical documentation (Article 11)
5. **Ongoing**: Monitor performance, maintain audit logs (Article 15)
6. **Periodically**: Reassess risk and effectiveness (Article 9)

---

## References
- EU AI Act Regulation 2024/1689, Article 6
- Recitals 32-45 (explaining high-risk rationale)
- Annex III (Final high-risk list, developing)
