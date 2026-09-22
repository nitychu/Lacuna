# ISO 27001:2022 Annex A Gap Assessment

**Subject.** RTI International Information Security Policy (effective November 2020, updated May 2026)
**Reviewer.** Nityasri Chukka
**Date.** September 2026
**Type.** Documentation review

## 1. Executive summary

This is a review of RTI International's published Information Security Policy against 16 controls from ISO 27001:2022 Annex A. The result was **6 controls covered, 10 partial, and 0 outright gaps.**

No control is entirely absent, which is unusual and speaks well of the document's breadth. It is organized around NIST control families, assigns clear ownership to the Office of the CISO, and names specific roles down to risk designation levels for individual IT positions.

The partials cluster around one pattern. A requirement is stated without the process that would make it operate. Encryption is required for devices, but nothing defines key management or approved algorithms. Access controls enforce least privilege, but nothing governs how privileged accounts are granted or reviewed. Authentication uses passwords and tokens, but no multi-factor requirement or strength standard appears. A written control and an operating control are not the same thing, and ISO 27001 certification turns on the second.

Two structural observations follow from that. The policy's own governance is incomplete. It has an owner and a three-year review cycle, but shows no evidence of management approval or personnel acknowledgment, which is what A.5.1 asks for. Cloud is also named in scope without being controlled. The policy covers cloud platforms and defers physical security to the provider, but says nothing about how cloud services are acquired, managed, or exited.

Three priorities follow. Add cloud service controls, add a cryptography and key management section, and record management approval of the policy itself.

## 2. Scope and method

**Document assessed.** RTI International's Information Security Policy, a nine-page public document, effective November 2020 and updated May 2026. Version matters here. An earlier run of this assessment against the December 2022 version produced materially different results, so any finding below applies to the May 2026 text only.

**Controls assessed.** Sixteen ISO 27001:2022 Annex A controls spanning all four themes, which are organizational (A.5), people (A.6), physical (A.7), and technological (A.8). This is a subset of the full 93. The subset was chosen to cover each theme rather than to target weaknesses, and a full assessment would widen it.

**Method.** Each control was assessed in two passes. First, a tool I built (Lacuna) split the policy into sections, retrieved the sections most relevant to each control, and proposed a verdict with cited evidence. Second, I reviewed every verdict against the source document myself, checking whether the cited text supported the verdict and whether relevant text elsewhere in the policy had been missed. Where the two disagreed, my review governs. Section 6 reports how often they disagreed.

**Verdict definitions.**

- **Covered.** The policy addresses the control's intent, with the specifics the control asks for.
- **Partial.** The policy addresses the subject but omits a requirement the control names.
- **Gap.** Nothing in the policy addresses the control.

**What this is not.** This is a documentation review. It assesses what the policy says, not what RTI does. No interviews were conducted, no evidence was sampled, and no control was tested for operating effectiveness. A control marked covered here means the policy addresses it, not that the organization is compliant.

## 3. Summary of findings

**6 covered, 10 partial, 0 gaps**

| Control | Title | Verdict | Rationale |
|---|---|---|---|
| A.5.1 | Policies for information security | Partial | Owner, effective date, and three-year review cycle stated, but no management approval or personnel acknowledgment |
| A.5.7 | Threat intelligence | Partial | Threat assessments and security alerts performed, but no process for collecting or analyzing threat intelligence |
| A.5.10 | Acceptable use of information and assets | Partial | References a separate Acceptable Use Policy and sets clean desk rules, but the use rules themselves are outside this document |
| A.5.15 | Access control | Covered | Authorized access only, account lifecycle, least privilege, separation of duties, and information flow control |
| A.5.17 | Authentication information | Partial | Authenticator and identifier management covered, but no guidance to personnel on handling credentials |
| A.5.23 | Information security for use of cloud services | Partial | Cloud in scope and provider controls assessed annually, but no acquisition, use, or exit process |
| A.5.24 | Incident management planning | Covered | Incident Response Plan, OCISO ownership, role-based training by incident phase, escalation through ticketing |
| A.6.3 | Awareness, education and training | Covered | Training at hire and annually, role-based, records maintained, monthly phishing simulations |
| A.7.2 | Physical entry | Covered | Physical access authorized and monitored, visitor records, escorts, datacenter access by risk designation |
| A.8.2 | Privileged access rights | Partial | Least privilege and risk-designated positions, but no allocation or review process specific to privileged accounts |
| A.8.5 | Secure authentication | Partial | Passwords, tokens, and biometrics named, but no multi-factor requirement or strength standards |
| A.8.8 | Management of technical vulnerabilities | Covered | Regular scans, owners notified with severity and mitigation guidance, prioritized remediation |
| A.8.12 | Data leakage prevention | Partial | Unauthorized data transfers prevented and USB drives prohibited, but no DLP tooling or monitoring |
| A.8.13 | Information backup | Partial | Backup services, alternate sites, and a Backup Administrator role, but no backup frequency, retention, or restore testing |
| A.8.16 | Monitoring activities | Covered | Centralized logging, automated alerts, continuous monitoring, tiered by system impact level |
| A.8.24 | Use of cryptography | Partial | Encryption required for devices and media, but no cryptographic policy or key management |

## 4. Detailed findings

### A.5.1 Policies for information security (Partial)

**Policy evidence.** Documentation Management assigns the OCISO responsibility for the ISMS governing the lifecycle of IT procedures, with annual review, defined ownership, authorization of amendments, and role-based training acknowledgements. The policy states it is subject to review every three years unless circumstances require earlier.

**Assessment.** Ownership and a review cycle are in place, which is more than many published policies show. What is missing is evidence that this policy was approved by management and communicated to and acknowledged by personnel. Role-based training acknowledgements are mentioned for procedures generally, not for this policy. The control asks for a policy that is defined, approved by management, published, communicated, acknowledged, and reviewed. Approval and acknowledgment are the two links absent here.

**To close.** Record management approval on the document itself (approver, role, date), and add an annual acknowledgment requirement for all personnel with records retained.

### A.5.7 Threat intelligence (Partial)

**Policy evidence.** The Security Operations team conducts threat assessments and operates security monitoring tools. The OCISO offers threat assessments as a service. System and Information Integrity includes distributing security alerts and directives. Risk Assessment covers ongoing vulnerability monitoring.

**Assessment.** The pieces of a threat intelligence capability appear across three sections, but the policy never describes collecting information about threats and analyzing it to produce actionable intelligence. Distributing alerts is consumption, not production. The control asks for a defined process with sources, analysis, and use.

**To close.** Define threat intelligence sources, who analyzes them, on what cadence, and how the output feeds risk assessment and monitoring.

### A.5.10 Acceptable use of information and assets (Partial)

**Policy evidence.** Non-Compliance cites RTI-14.1.3 Acceptable Use Policy and its consequences. Clean Desk sets handling rules for sensitive information in the office and remotely. Media Protection restricts non-IT managed devices and prohibits USB drives without an approved exemption.

**Assessment.** Real handling rules exist, and a separate Acceptable Use Policy is referenced by document number. But this document does not state the acceptable use rules themselves, and a reader of this policy alone would not know what is permitted. Referencing another document is legitimate practice. The finding is that the rules cannot be assessed from what is published here.

**To close.** Either summarize the acceptable use rules in this policy or make RTI-14.1.3 available alongside it, with a clear pointer.

### A.5.15 Access control (Covered)

**Policy evidence.** Access Controls state that information may only be accessed by authorized individuals, that privileges are for individual use and must not be shared, and that procedures cover account activation, changes, review, and deactivation, plus information flow control, separation of duties, and least privilege.

**Assessment.** The control asks for rules governing physical and logical access based on business and security requirements. This section covers logical access thoroughly, and Physical and Environmental Security covers the physical side. Account review is explicitly included, which is often the omission in policies like this.

### A.5.17 Authentication information (Partial)

**Policy evidence.** Identification and Authentication requires users and devices to be identified and authenticated before access, using passwords, tokens, or biometrics, with procedures governing identifier management, authenticator controls, protection of authentication feedback, and secure disposal.

**Assessment.** Allocation and management of authentication information are covered. What the control also asks for, and the policy does not address, is guidance to personnel on handling their own credentials, meaning how to keep them confidential, what to do if one is compromised, and rules against reuse. Given that the policy does state credentials must not be shared, the guidance gap is narrow but real.

**To close.** Add a short section on user responsibilities for credentials, including compromise reporting.

### A.5.23 Information security for use of cloud services (Partial)

**Policy evidence.** Scope includes cloud-based platforms, applications, and infrastructure. Physical and Environmental Security assigns datacenter controls to the Cloud Service Provider, with annual compliance assessments by the OCISO. Supply Chain Risk Management requires third-party due diligence and security requirements in contracts. Several IT position risk designations are AWS-specific.

**Assessment.** This is the widest partial in the set. Cloud is plainly central to RTI's environment, since five of fifteen listed IT positions are AWS roles, and provider controls are verified annually. But the control asks for processes covering acquisition, use, management, and exit from cloud services, and none of those appear. Exit in particular is absent. Nothing describes how data is retrieved or deleted when a cloud service is discontinued.

**To close.** Add a cloud services section covering approval before acquisition, security requirements for configuration and use, ongoing management responsibilities split between RTI and the provider, and an exit process covering data retrieval and deletion.

### A.5.24 Information security incident management planning (Covered)

**Policy evidence.** Incident Response describes an Incident Response Plan led by the OCISO, collaboration with departments as needed, role-based training covering preparation, detection, analysis, containment, eradication, and recovery, and event reporting through a ticketing system with escalation to appropriate teams.

**Assessment.** The control asks for planned and prepared incident management with defined processes, roles, and responsibilities. All three are present, and the training explicitly follows the incident lifecycle, which shows the phases are defined rather than assumed.

### A.6.3 Information security awareness, education and training (Covered)

**Policy evidence.** Awareness and Training requires all personnel accessing RTI assets to complete security awareness training. The OCISO delivers basic and role-specific training at hire and annually, maintains training records, conducts monthly phishing simulations, and provides additional instruction as needed. Position Risk Designation adds that staff, contractors, vendors, and interns are all screened and trained, with more for higher-privilege roles.

**Assessment.** Fully covered, including the elements policies most often omit, which are record retention, extension to contractors and vendors, and a recurring cadence rather than onboarding only. Monthly phishing simulations go beyond what the control requires.

### A.7.2 Physical entry (Covered)

**Policy evidence.** Physical and Environmental Security covers authorizing and controlling physical access to facilities, monitoring facility access, keeping visitor access records, and escorting visitors when required. The IT Position Responsibilities table assigns datacenter physical access per role as none, escorted, or full.

**Assessment.** The control asks that secure areas be protected by appropriate entry controls. Authorization, monitoring, visitor records, and escorting are all present, and the per-position access table shows the controls are applied in practice rather than described generally.

### A.8.2 Privileged access rights (Partial)

**Policy evidence.** Access Controls apply least privilege and separation of duties, with account activation, changes, review, and deactivation. Position Risk Designation assigns levels 2 through 5 to IT positions based on duties and impact, with higher-privilege roles receiving additional training.

**Assessment.** The framework for privileged access exists, since risk designations track privilege closely and least privilege is stated. What the control asks for and the policy lacks is a process specific to privileged accounts, meaning how they are requested and approved, whether they are time-limited, and how their use is reviewed separately from standard accounts. Review is mentioned for accounts generally, not for privileged ones in particular.

**To close.** Define approval, periodic review, and logging requirements specific to privileged and administrative accounts.

### A.8.5 Secure authentication (Partial)

**Policy evidence.** Identification and Authentication names passwords, tokens, and biometric verification as authentication mechanisms. Access Controls include enforcement of access and authentication restrictions.

**Assessment.** Mechanisms are named but not required. The policy does not mandate multi-factor authentication anywhere, including for the privileged AWS and domain administrator roles it lists elsewhere, nor does it define password length, complexity, or rotation. The control asks for secure authentication technologies implemented according to access restrictions and the access control policy, which implies a stated standard rather than a menu of options.

**To close.** Require multi-factor authentication for remote access and privileged accounts, and state password standards or reference the procedure that does.

### A.8.8 Management of technical vulnerabilities (Covered)

**Policy evidence.** Vulnerability Disclosure assigns the OCISO responsibility for tracking, communicating, and disclosing vulnerabilities, conducting regular vulnerability scans, notifying system owners and technical SMEs with severity and mitigation guidance, and prioritizing remediation. Risk Assessment adds ongoing vulnerability monitoring and response within defined risk tolerance. IT Operations Management performs continuous monitoring and vulnerability assessments.

**Assessment.** The control asks that information about technical vulnerabilities be obtained, exposure evaluated, and measures taken. All three appear, with named ownership and a route to the people who own the affected systems.

### A.8.12 Data leakage prevention (Partial)

**Policy evidence.** System and Communications Protection prevents unauthorized data transfers and protects transmitted data. Media Protection prohibits USB drives without an approved exemption, restricts non-IT managed devices unless authorized and encrypted, and requires sanitization before disposal or reuse.

**Assessment.** Several leakage paths are closed by rule, including removable media, unmanaged devices, and disposal. What the control asks for and the policy does not describe is data leakage prevention applied to systems, networks, and devices that process sensitive information, meaning monitoring or tooling that detects attempted exfiltration rather than prohibiting a channel outright.

**To close.** State whether DLP tooling is deployed, on what channels (email, endpoint, cloud storage), and who monitors and responds to alerts.

### A.8.13 Information backup (Partial)

**Policy evidence.** Contingency Planning requires a Disaster Recovery Plan with staff training on designated roles, regular testing of response plans, and alternative locations and backup services to ensure continuity. The IT Position Responsibilities table includes a Backup Administrator responsible for systems used for data backup and restores.

**Assessment.** Backup exists as a capability with an owner and a tested recovery plan, which is more than a bare mention. But the control asks for backup copies of information, software, and systems maintained and regularly tested in line with an agreed policy, and the policy states no backup frequency, retention period, storage location requirement, or restore testing separate from DR plan testing. Testing a recovery plan and testing that backups restore are related but not the same.

**To close.** Define backup scope, frequency, retention, and offsite or separate-region storage, and require periodic restore testing with documented results.

### A.8.16 Monitoring activities (Covered)

**Policy evidence.** Assessment, Authorization and Monitoring requires low-impact systems to log key events, protect audit records, perform periodic reviews, and maintain time synchronization, while moderate-impact systems require advanced logging, centralized storage, automated alerts, regular reviews, and extended retention. Security Operations monitors, detects, and responds to threats. System and Information Integrity includes continuous monitoring for potential attacks. Audit and Accountability requires identifying and recording audit events, regular log review, and protection of audit data from unauthorized change.

**Assessment.** The control asks that networks, systems, and applications be monitored for anomalous behaviour with appropriate action taken. Monitoring, automated alerting, and review are present, and the tiering by system impact shows the requirement is calibrated rather than generic. Security Operations provides the response path.

### A.8.24 Use of cryptography (Partial)

**Policy evidence.** Clean Desk requires electronic devices to be encrypted and stored securely. Media Protection permits non-IT managed devices only when authorized and encrypted. System and Communications Protection requires protecting transmitted data.

**Assessment.** Encryption is required in specific situations, so the subject is not absent. But the control asks for rules on the effective use of cryptography, including key management, and the policy contains no cryptographic policy, no approved algorithms or key lengths, and nothing on key generation, storage, rotation, or destruction. Protection of transmitted data is required without specifying that it be encrypted. For an organization handling ePHI and CUI under HIPAA and NIST SP 800-171, this is the most consequential partial in the set.

**To close.** Add a cryptography section defining approved algorithms and key lengths, where encryption is required at rest and in transit, and the full key management lifecycle with assigned ownership.

## 5. Themes

**Written controls outnumber operating ones.** Ten of sixteen controls landed partial, and eight of those ten failed on the same thing. The policy states a requirement without the process that would make it work. Encryption is required with no key management. Least privilege is stated with no privileged access review. Authentication mechanisms are named with no standard for which to use or how strong. Backups exist with no frequency or restore testing.

This is the distinction ISO 27001 certification turns on. A certification audit asks for evidence that a control operates, meaning records, cadences, named owners, and results. A policy that states a requirement and stops gives an auditor nothing to sample. RTI's document is strongest exactly where it specifies process. Awareness and Training says training happens at hire and annually with records kept and monthly phishing simulations, and that control was covered without qualification. The same level of specificity applied to cryptography, backup, and privileged access would move most of the partials.

**The policy does not govern itself.** A.5.1 is a control about the policy, and it landed partial. The document has an owner, an effective date, an update date, and a three-year review cycle, which is genuinely better than most published policies. But nothing shows management approved it or that personnel acknowledged it. That matters more than it looks. If the policy is not formally approved, the authority behind every requirement in it is unstated, and if personnel never acknowledge it, enforcement, including the termination consequence the Non-Compliance section names, rests on a document no one confirmed reading.

**Cloud is in scope but not in the controls.** The scope statement covers cloud platforms and infrastructure. Five of the fifteen IT positions listed are AWS roles. Physical security for cloud is explicitly delegated to the provider and verified annually, which shows real awareness of shared responsibility. Yet no control addresses how cloud services are selected, approved, configured, or exited. The organization has clearly moved to cloud operationally while the policy's control set still reflects an on-premises structure. Exit is the sharpest version of this. For an organization handling protected health information, the absence of any stated process for retrieving and deleting data when a cloud service ends is a real exposure, not a documentation nicety.

## 6. Limitations

**Documentation review only.** No interviews, no evidence sampling, no testing of operating effectiveness. Every verdict describes the policy text, not the organization.

**Partial control set.** Sixteen of 93 Annex A controls. The subset spans all four themes but a full assessment would likely surface findings this one cannot.

**Single reviewer.** All verdicts are mine, with no second opinion. Verdict boundaries, particularly between covered and partial, involve judgment another reviewer might draw differently. A.5.10 and A.8.12 are the two I would expect most disagreement on.

**Public document only.** The policy references other documents by number, including RTI-14.1.3 Acceptable Use Policy and the procedures the ISMS governs. Several partials, notably A.5.10 and A.8.5, might be covered by documents not published. This assessment reflects what a reader of the public policy can verify.

**Tool-assisted, manually reviewed.** Verdicts were proposed by a tool I built and then reviewed by hand against the source. In the tool's first version, that review changed all but three of the 16 verdicts. Retrieval was surfacing the wrong sections, so the model was judging text that did not contain the relevant control. After redesigning chunking and retrieval, tool and reviewer agreed on 13 of 16. The three remaining disagreements are recorded in the tool's repository. Every verdict in this report reflects my review, not the tool's output.

## 7. Recommendations

**1. Add cloud service controls.** Highest priority, because the gap is widest relative to how central cloud is to the environment. Cover approval before acquisition, configuration and use requirements, the split of responsibility with the provider, and an exit process covering data retrieval and deletion.

**2. Add a cryptography and key management section.** Second because of regulatory exposure. With ePHI under HIPAA and CUI under NIST SP 800-171 in scope, encryption requirements without key management leave the most consequential control underspecified. Define approved algorithms and key lengths, where encryption is required at rest and in transit, and the key lifecycle with an assigned owner.

**3. Record management approval and personnel acknowledgment of this policy.** Lowest effort of the four and it closes A.5.1. Add an approval block to the document and an annual acknowledgment requirement with retained records.

**4. Specify backup and privileged access processes.** Backup needs frequency, retention, storage, and restore testing. Privileged access needs an approval and review process distinct from general account management. Both are cases where the capability exists and only the stated process is missing.
