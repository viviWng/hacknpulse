# Article 5: Prohibited AI Practices

## Title
Prohibited practices (EU Regulation 2024/1689)

## Full Text
The following AI practices shall be prohibited:

(a) the placing on the market, putting into service or use of an AI system that deploys subliminal techniques beyond a person's consciousness in order to materially distort a person's behaviour in a manner that causes or is likely to cause harm;

(b) the placing on the market, putting into service or use of an AI system that exploits any of the vulnerabilities of a specific group of persons due to their age, physical or mental disability, in order to materially distort the behaviour of a person belonging to that group in a manner that causes or is likely to cause harm to that person or another person;

(c) the social credit system placing on the market, putting into service or use of an AI system for the purpose of social scoring by natural or legal persons acting on behalf of an official authority or on behalf of a body vested with public authority, resulting in the exclusion or disadvantaging of natural persons in a way that affects their access to education, employment, essential goods and services, or the ability to exercise a right;

(d) the real-time remote biometric identification of natural persons by law enforcement authorities except where strictly necessary for the purposes of:
   1. searching for a specific identified natural person;
   2. preventing a substantial and imminent threat to public safety, and with appropriate safeguards;

## Key Requirements
- **Complete Prohibition**: These practices cannot be used in any context under EU AI Act
- **No Exceptions**: Even with guardrails, these systems cannot be deployed
- **Immediate Action**: Any system identified as using prohibited practices must cease operation

## Enforcement
- National authorities may impose fines up to 10% of annual global turnover
- Immediate market removal orders
- Criminal penalties possible for serious violations

## Related Articles
- Article 6: Definition of high-risk AI systems
- Article 76: Administrative fines

---

## Classification Indicators

A system violates Article 5 if it:
1. Uses subliminal techniques to distort behavior without awareness
2. Targets vulnerable groups (children, disabled persons) to manipulate
3. Implements social credit scoring that excludes people from essential services
4. Uses real-time facial recognition by law enforcement (except narrow exceptions)

## Decision Tree
```
Does the system use:
  ├─ Subliminal manipulation? → PROHIBITED
  ├─ Target vulnerable groups to distort behavior? → PROHIBITED
  ├─ Implement social scoring for exclusion? → PROHIBITED
  ├─ Real-time biometric ID (law enforcement, without narrow exception)? → PROHIBITED
  └─ None of above → Check Article 6
```

## Examples
- **PROHIBITED**: Manipulative notification system that bypasses user awareness to influence behavior
- **PROHIBITED**: Credit system that excludes based on ethnic background or protected characteristics
- **PROHIBITED**: Biometric surveillance system identifying protesters in real-time
- **NOT PROHIBITED**: Spam filter removing unsolicited emails
- **NOT PROHIBITED**: Search functionality finding specific known person in database
