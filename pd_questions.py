# -*- coding: utf-8 -*-
"""
Professional Dilemmas (PD) Question Bank for MedBank Studio.
Contains 25 Ranking questions and 25 Selection questions (Total = 50 questions).
Adheres strictly to GMC Good Medical Practice principles.
"""

PD_QUESTIONS = [
    # =========================================================================
    # RANKING QUESTIONS (1 to 25)
    # 5 options ranked from most appropriate (1) to least appropriate (5).
    # =========================================================================
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor on a busy medical ward. At 09:00, you notice your FY1 colleague slurring their speech, walking unsteadily, and smelling strongly of alcohol. They are about to cannulate a patient and prescribe intravenous fluids. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Immediately intervene to stop the FY1 from carrying out the procedure, explain your concern privately, and escort them away from clinical areas",
            "Urgent escalation to the supervising consultant or clinical lead informing them that the FY1 appears impaired and unfit for duty",
            "Offer to take over the FY1's immediate urgent clinical tasks so that patient care is not compromised",
            "Advise the FY1 to drink some coffee and take a short nap in the doctors' mess before resuming duties",
            "Ignore the situation as it is their personal responsibility and you do not want to damage their career"
        ],
        "correct_answer": [
            "Immediately intervene to stop the FY1 from carrying out the procedure, explain your concern privately, and escort them away from clinical areas",
            "Urgent escalation to the supervising consultant or clinical lead informing them that the FY1 appears impaired and unfit for duty",
            "Offer to take over the FY1's immediate urgent clinical tasks so that patient care is not compromised",
            "Advise the FY1 to drink some coffee and take a short nap in the doctors' mess before resuming duties",
            "Ignore the situation as it is their personal responsibility and you do not want to damage their career"
        ],
        "explanation": "GMC guidance states that patient safety is the paramount priority. The most appropriate immediate step is to prevent the colleague from treating patients and remove them from clinical duties. The consultant must then be notified urgently so formal support and coverage can be arranged. Taking over urgent tasks ensures continuity of care. Advising them to sleep it off and return compromises safety, and ignoring it completely breaches professional duty."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You realize that you inadvertently prescribed a tenfold overdose of intravenous Gentamicin to an elderly patient with sepsis 2 hours ago. The infusion was administered by the nursing staff. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Immediately assess the patient, check vital signs, and liaise with senior medical staff and pharmacy/poisons service for monitoring and management",
            "Explain the error openly and honestly to the patient (and family if appropriate), apologize, and explain what monitoring and treatment will be undertaken (Duty of Candour)",
            "Complete an internal electronic clinical incident report (e.g. Datix) and document the event and management objectively in the patient's medical record",
            "Discuss the incident with your educational supervisor at your end-of-placement review in 3 months",
            "Alter the prescription chart to the correct dose to avoid disciplinary consequences"
        ],
        "correct_answer": [
            "Immediately assess the patient, check vital signs, and liaise with senior medical staff and pharmacy/poisons service for monitoring and management",
            "Explain the error openly and honestly to the patient (and family if appropriate), apologize, and explain what monitoring and treatment will be undertaken (Duty of Candour)",
            "Complete an internal electronic clinical incident report (e.g. Datix) and document the event and management objectively in the patient's medical record",
            "Discuss the incident with your educational supervisor at your end-of-placement review in 3 months",
            "Alter the prescription chart to the correct dose to avoid disciplinary consequences"
        ],
        "explanation": "Immediate clinical assessment and senior involvement to mitigate harm is the top priority. Under the statutory Duty of Candour, the doctor must promptly and openly inform the patient and apologize. Documenting and filing an incident report promotes institutional learning. Delaying discussion for 3 months misses early reflection, and falsifying records is fraudulent, dishonest, and a gross breach of GMC standards."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are assessing a 3-year-old child brought to the ED by their mother's new partner. The child has multiple circular burn marks on their back that resemble cigarette burns, which the partner claims were caused by 'brushing against a hot radiator'. The partner is impatient and demands immediate discharge. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Discuss your safeguarding concerns urgently with the on-duty paediatric registrar or consultant and admit the child to the paediatric ward for a place of safety",
            "Contact the hospital safeguarding children team and initiate a multi-agency safeguarding referral (MASH)",
            "Perform a thorough, documented top-to-toe examination of the child, looking for other injuries or signs of neglect",
            "Accuse the partner directly of child abuse in front of the child and threaten to call the police immediately",
            "Discharge the child as requested by the partner and arrange routine GP follow-up in 2 weeks"
        ],
        "correct_answer": [
            "Discuss your safeguarding concerns urgently with the on-duty paediatric registrar or consultant and admit the child to the paediatric ward for a place of safety",
            "Contact the hospital safeguarding children team and initiate a multi-agency safeguarding referral (MASH)",
            "Perform a thorough, documented top-to-toe examination of the child, looking for other injuries or signs of neglect",
            "Accuse the partner directly of child abuse in front of the child and threaten to call the police immediately",
            "Discharge the child as requested by the partner and arrange routine GP follow-up in 2 weeks"
        ],
        "explanation": "In suspected non-accidental injury, child protection is paramount. Admitting the child under paediatric supervision ensures immediate physical safety. Initiating safeguarding procedures through hospital safeguarding/MASH ensures multi-agency assessment. Full clinical documentation is essential. Confrontational accusations may escalate danger or cause the carer to abscond with the child. Discharging the child places them at extreme risk of serious harm."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 28-year-old man attends your GP clinic and tests positive for acute hepatitis B. He explicitly forbids you from telling his long-term live-in partner, with whom he is sexually active, stating that he fears she will leave him. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Explain the transmission risk to his partner, explore his fears, and counsel him extensively on the ethical and health necessity of notifying and testing his partner",
            "Advise the patient that if he continues to refuse, you have a professional duty to protect third parties from serious communicable harm and may disclose to his partner after seeking Caldicott guidance",
            "Seek confidential advice from your medical defence organisation (MDO) or the trust Caldicott Guardian regarding breaching confidentiality in the public interest",
            "Immediately telephone the partner without warning the patient to inform her of the diagnosis",
            "Agree unconditionally to keep the diagnosis secret and take no further action to protect the partner"
        ],
        "correct_answer": [
            "Explain the transmission risk to his partner, explore his fears, and counsel him extensively on the ethical and health necessity of notifying and testing his partner",
            "Advise the patient that if he continues to refuse, you have a professional duty to protect third parties from serious communicable harm and may disclose to his partner after seeking Caldicott guidance",
            "Seek confidential advice from your medical defence organisation (MDO) or the trust Caldicott Guardian regarding breaching confidentiality in the public interest",
            "Immediately telephone the partner without warning the patient to inform her of the diagnosis",
            "Agree unconditionally to keep the diagnosis secret and take no further action to protect the partner"
        ],
        "explanation": "The initial step is to work with the patient to understand his concerns and encourage voluntary disclosure. If he refuses, GMC guidance allows disclosure to protect individuals from risk of death or serious harm, but the patient must first be informed of your intention to disclose unless doing so creates danger. Seeking MDO/Caldicott advice ensures legal alignment. Immediate unauthorized phone calls breach trust, and doing nothing leaves the partner at severe risk."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A consultant physician instructs you, an FY1, to rewrite an electronic discharge summary to omit a medication error that resulted in a patient staying an extra 3 days in hospital, telling you: 'It will only upset the patient and trigger an unnecessary complaint'. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Politely decline to falsify or omit the information, explaining that discharge summaries must be an accurate clinical record",
            "Seek advice from your clinical supervisor, educational supervisor, or clinical director regarding the consultant's instruction",
            "Document the true clinical events, including the error and its management, objectively in the patient's records",
            "Agree to omit the error from the discharge summary but report the consultant anonymously online",
            "Comply fully with the consultant's instruction without questioning because they are your senior assessor"
        ],
        "correct_answer": [
            "Politely decline to falsify or omit the information, explaining that discharge summaries must be an accurate clinical record",
            "Seek advice from your clinical supervisor, educational supervisor, or clinical director regarding the consultant's instruction",
            "Document the true clinical events, including the error and its management, objectively in the patient's records",
            "Agree to omit the error from the discharge summary but report the consultant anonymously online",
            "Comply fully with the consultant's instruction without questioning because they are your senior assessor"
        ],
        "explanation": "Doctors must maintain integrity and honesty in all medical documentation. Declining to falsify records is the primary professional action. Escalating to educational leadership provides support in dealing with senior pressure. Documenting facts truthfully ensures accurate care. Participating in a cover-up while posting anonymously online breaches GMC standards, and blind compliance in falsification is dishonest and unacceptable."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "The grateful family of an elderly patient whom you cared for during a prolonged admission presents you with an expensive luxury watch valued at approximately £800 as a personal thank-you gift. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Politely decline the watch, thanking the family warmly and explaining that professional standards and hospital policy prohibit accepting high-value personal gifts",
            "Suggest that if they wish to express gratitude, they could write a thank-you letter or make a modest donation to the ward charitable fund",
            "Inform your clinical supervisor or line manager about the offer and your decision to decline it",
            "Accept the watch but only wear it outside of work hours so colleagues do not see it",
            "Accept the watch and offer to provide the family with your personal mobile number for priority medical advice"
        ],
        "correct_answer": [
            "Politely decline the watch, thanking the family warmly and explaining that professional standards and hospital policy prohibit accepting high-value personal gifts",
            "Suggest that if they wish to express gratitude, they could write a thank-you letter or make a modest donation to the ward charitable fund",
            "Inform your clinical supervisor or line manager about the offer and your decision to decline it",
            "Accept the watch but only wear it outside of work hours so colleagues do not see it",
            "Accept the watch and offer to provide the family with your personal mobile number for priority medical advice"
        ],
        "explanation": "GMC Good Medical Practice guidance states that doctors must not accept gifts that could be seen as affecting their professional judgment or exceeding a token value. An £800 watch is high-value and must be declined politely. Redirecting gratitude to the ward team or a charity is constructive. Informing a supervisor provides transparency. Hiding the gift is deceitful, and trading personal access for gifts is a severe conflict of interest."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You see a public post on Instagram by a fellow FY1 doctor containing a photo of an unusual surgical specimen on a theatre tray. The caption mentions the patient's age, hospital name, and specific rare diagnosis, stating: 'Craziest case of my shift!'. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Contact your colleague privately and immediately, advising them that the post contains identifiable patient details and must be taken down at once",
            "Remind your colleague of the GMC guidance on social media and patient confidentiality",
            "If the colleague refuses or fails to remove the post promptly, escalate the matter to their educational supervisor or the hospital Caldicott Guardian",
            "Post a public critical comment under their photo accusing them of violating patient rights",
            "Like and share the post to your own medical followers because the case is educational"
        ],
        "correct_answer": [
            "Contact your colleague privately and immediately, advising them that the post contains identifiable patient details and must be taken down at once",
            "Remind your colleague of the GMC guidance on social media and patient confidentiality",
            "If the colleague refuses or fails to remove the post promptly, escalate the matter to their educational supervisor or the hospital Caldicott Guardian",
            "Post a public critical comment under their photo accusing them of violating patient rights",
            "Like and share the post to your own medical followers because the case is educational"
        ],
        "explanation": "GMC social media guidance warns that combining clinical details can lead to patient identification, breaching confidentiality. Contacting the colleague privately to remove the post immediately mitigates ongoing harm. Pointing to guidance helps them understand the breach. Escalating is necessary if they do not comply. Public shaming is unprofessional and amplifies attention to the breach, and sharing it makes you complicit in the violation."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "While suturing a laceration on an acutely confused intravenous drug user with suspected blood-borne viruses, you accidentally sustain a deep needlestick puncture through your glove. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Immediately encourage free bleeding of the puncture site under warm running water and wash with soap and water without scrubbing",
            "Cover the puncture site with a waterproof dressing and immediately report to Occupational Health or the ED for post-exposure prophylaxis (PEP) assessment",
            "Hand over the patient's care safely to a colleague so that the patient's wound can be completed",
            "Complete an electronic incident report (Datix) once medical management is underway",
            "Squeeze the puncture wound aggressively, apply neat bleach, and finish your 8-hour shift before seeking advice"
        ],
        "correct_answer": [
            "Immediately encourage free bleeding of the puncture site under warm running water and wash with soap and water without scrubbing",
            "Cover the puncture site with a waterproof dressing and immediately report to Occupational Health or the ED for post-exposure prophylaxis (PEP) assessment",
            "Hand over the patient's care safely to a colleague so that the patient's wound can be completed",
            "Complete an electronic incident report (Datix) once medical management is underway",
            "Squeeze the puncture wound aggressively, apply neat bleach, and finish your 8-hour shift before seeking advice"
        ],
        "explanation": "Immediate first aid (washing gently with soap and warm water, encouraging free bleeding) is the proven first step. Prompt assessment for HIV/HBV/HCV PEP (ideally within 1 hour) is critical. Handing over the patient ensures their care is not compromised. Submitting a Datix aids reporting. Caustic chemicals like bleach and aggressive squeezing damage tissue and increase transmission risk, and delaying PEP assessment for hours diminishes its effectiveness."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 42-year-old Jehovah's Witness is admitted with severe bleeding from a duodenal ulcer. His haemoglobin is 48 g/L. He is fully conscious, alert, and demonstrates full mental capacity. He carries a valid, signed Advance Decision refusing all blood and blood products under any circumstances. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Respect the patient's autonomous decision, verify the validity and applicability of the Advance Decision, and document the discussion clearly",
            "Explore alternative non-blood management options such as intravenous iron, tranexamic acid, cell salvage, and endoscopic haemostasis",
            "Discuss the situation urgently with your consultant and involve the hospital transfusion liaison team / hospital legal team",
            "Attempt to persuade the patient by informing them repeatedly that their religious beliefs are irrational",
            "Wait until the patient loses consciousness from hypovolaemia and immediately transfuse blood products against their documented wishes"
        ],
        "correct_answer": [
            "Respect the patient's autonomous decision, verify the validity and applicability of the Advance Decision, and document the discussion clearly",
            "Explore alternative non-blood management options such as intravenous iron, tranexamic acid, cell salvage, and endoscopic haemostasis",
            "Discuss the situation urgently with your consultant and involve the hospital transfusion liaison team / hospital legal team",
            "Attempt to persuade the patient by informing them repeatedly that their religious beliefs are irrational",
            "Wait until the patient loses consciousness from hypovolaemia and immediately transfuse blood products against their documented wishes"
        ],
        "explanation": "Under the Mental Capacity Act 2005, an adult with capacity has the absolute legal and ethical right to refuse any medical treatment, including life-sustaining blood transfusions. Valid Advance Decisions must be respected. Maximizing non-blood medical options is standard. Involving seniors and transfusion specialists ensures safe supportive care. Insulting religious beliefs is coercive and unprofessional, and transfusing an incapacitated patient against a valid advance refusal is battery and unlawful."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are the sole FY1 on a 30-bed surgical ward at 02:00. Two patients are acutely deteriorating with NEWS scores of 7 and 8, three surgical post-op patients require urgent analgesia, and the ward sister informs you that nursing staffing is 50% below safe minimum levels. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Immediately assess and stabilize the two deteriorating patients while calling the surgical registrar and hospital resuscitation / critical care outreach team",
            "Escalate the acute ward staffing crisis and workload to the hospital site coordinator / clinical night lead for emergency redeployment of staff",
            "Briefly triage remaining tasks with the nursing team, ensuring urgent analgesia is delegated or prioritized once acutely unwell patients are stable",
            "Submit a formal clinical incident report (Datix) and exception report at the end of the shift",
            "Leave the ward to sit in the mess because the workload is impossible to manage alone"
        ],
        "correct_answer": [
            "Immediately assess and stabilize the two deteriorating patients while calling the surgical registrar and hospital resuscitation / critical care outreach team",
            "Escalate the acute ward staffing crisis and workload to the hospital site coordinator / clinical night lead for emergency redeployment of staff",
            "Briefly triage remaining tasks with the nursing team, ensuring urgent analgesia is delegated or prioritized once acutely unwell patients are stable",
            "Submit a formal clinical incident report (Datix) and exception report at the end of the shift",
            "Leave the ward to sit in the mess because the workload is impossible to manage alone"
        ],
        "explanation": "Clinical prioritization must put the most critically unwell patients first with immediate outreach/senior help. Escalating staffing to the site coordinator enables hospital-wide resource allocation. Team communication and task triaging ensures urgent patient needs are tracked. Incident reporting flags systemic unsafe conditions for institutional review. Abandoning deteriorating patients is patient abandonment and severe misconduct."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 72-year-old man has just been diagnosed with metastatic pancreatic cancer. His daughter intercepts you in the corridor and tearfully begs you: 'Please do not tell my father he has cancer, the shock will kill him'. The patient is alert, orientated, and currently waiting for his scan results. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Explain empathetically to the daughter that her father has the legal and ethical right to know his diagnosis if he wishes, but you will deliver the news sensitively",
            "Invite the daughter into a private room to understand her fears and explore how the family would like to support him during the consultation",
            "Ask the patient directly in the presence of the daughter how much information he would like to receive about his investigations and condition",
            "Comply with the daughter's request and lie to the patient by telling him his scan showed benign inflammation",
            "Bluntly tell the daughter in the corridor that it is none of her business and dismiss her concerns"
        ],
        "correct_answer": [
            "Explain empathetically to the daughter that her father has the legal and ethical right to know his diagnosis if he wishes, but you will deliver the news sensitively",
            "Invite the daughter into a private room to understand her fears and explore how the family would like to support him during the consultation",
            "Ask the patient directly in the presence of the daughter how much information he would like to receive about his investigations and condition",
            "Comply with the daughter's request and lie to the patient by telling him his scan showed benign inflammation",
            "Bluntly tell the daughter in the corridor that it is none of her business and dismiss her concerns"
        ],
        "explanation": "GMC guidance on confidentiality and consent affirms that patients with capacity have an intrinsic right to information about their condition. Explaining this gently to relatives while validating their distress is essential. Establishing the patient's own preference for information delivery respects autonomy. Lying to the patient violates honesty and duty of care, and dismissive rudeness damages trust and causes unnecessary distress."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "While passing a ward treatment room, you observe a 4th-year medical student about to perform an arterial puncture (ABG) on an elderly confused patient. The student admits they have never performed an ABG before and that the patient has not given informed consent. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Intervene immediately and calmly to prevent the student from proceeding, prioritizing patient safety and dignity",
            "Take the student aside into a private room to explain why performing an invasive procedure without competence or valid consent is unacceptable",
            "Assess the patient yourself, explain the procedure if indicated, and perform the ABG under appropriate supervision with the student observing",
            "Report the medical student to the university medical school dean immediately without speaking to the student",
            "Allow the student to attempt the procedure on their own to see how well they do"
        ],
        "correct_answer": [
            "Intervene immediately and calmly to prevent the student from proceeding, prioritizing patient safety and dignity",
            "Take the student aside into a private room to explain why performing an invasive procedure without competence or valid consent is unacceptable",
            "Assess the patient yourself, explain the procedure if indicated, and perform the ABG under appropriate supervision with the student observing",
            "Report the medical student to the university medical school dean immediately without speaking to the student",
            "Allow the student to attempt the procedure on their own to see how well they do"
        ],
        "explanation": "Patient safety must come first: stopping an unconsented, unsupervised invasive procedure by an untrained student prevents harm. Giving immediate private educational feedback explains the gravity of consent and competence. Demonstrating the procedure correctly turns the event into a safe learning opportunity. Immediate reporting without local discussion bypasses formative learning, and allowing an unsafe procedure to continue is negligence."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You notice that your fellow FY2 colleague has become increasingly withdrawn, exhausted, and tearful over the past month. Today they made two near-miss medication errors and confided in you that they feel completely overwhelmed and 'cannot cope anymore'. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Listen compassionately in private, express your support, and gently encourage them to speak with their educational supervisor or GP",
            "Signpost them to confidential support services such as the BMA Wellbeing Support Service, NHS Practitioner Health, or hospital Occupational Health",
            "Offer to assist them with their immediate clinical workload for the rest of the shift so they are not working in an unsafe state",
            "Inform their clinical supervisor confidentially if they continue to make errors and refuse to seek help",
            "Tell them to 'toughen up' because junior doctor training is naturally stressful for everyone"
        ],
        "correct_answer": [
            "Listen compassionately in private, express your support, and gently encourage them to speak with their educational supervisor or GP",
            "Signpost them to confidential support services such as the BMA Wellbeing Support Service, NHS Practitioner Health, or hospital Occupational Health",
            "Offer to assist them with their immediate clinical workload for the rest of the shift so they are not working in an unsafe state",
            "Inform their clinical supervisor confidentially if they continue to make errors and refuse to seek help",
            "Tell them to 'toughen up' because junior doctor training is naturally stressful for everyone"
        ],
        "explanation": "Supporting a struggling colleague with empathy and encouraging them to seek formal guidance is the best first step. Providing access to professional support services (Practitioner Health, BMA) addresses root causes. Assisting with workload protects immediate patient care. Escalating confidentially is necessary if patient safety is endangered and the colleague does not seek help. Dismissive comments are harmful, unprofessional, and stigmatize mental health."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 68-year-old patient with severe abdominal pain and signs of peritonitis is in the Emergency Department. The medical registrar states the patient has a medical abdomen and should be admitted under surgery. The surgical registrar refuses to admit, stating the patient has diverticulitis which should be managed medically. The patient is clinically deteriorating. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Request an immediate joint bedside review between the medical registrar and surgical registrar to agree on a clinical stabilization and admission plan",
            "If disagreement persists, escalate immediately to the on-call medical and surgical consultants for a definitive consultant-to-consultant decision",
            "Ensure the patient is actively resuscitated, prescribed analgesia, and closely monitored in the ED resuscitation area during the discussion",
            "Advise the patient's family to submit a formal complaint against the surgical team",
            "Discharge the patient home with oral analgesia since neither team will accept them"
        ],
        "correct_answer": [
            "Request an immediate joint bedside review between the medical registrar and surgical registrar to agree on a clinical stabilization and admission plan",
            "If disagreement persists, escalate immediately to the on-call medical and surgical consultants for a definitive consultant-to-consultant decision",
            "Ensure the patient is actively resuscitated, prescribed analgesia, and closely monitored in the ED resuscitation area during the discussion",
            "Advise the patient's family to submit a formal complaint against the surgical team",
            "Discharge the patient home with oral analgesia since neither team will accept them"
        ],
        "explanation": "In inter-specialty admission disputes involving an unstable patient, collaborative joint bedside review is the fastest way to resolve clinical ambiguity. Escalating to duty consultants resolves impasses definitively. Ongoing resuscitation and monitoring in the ED protects the patient. Inciting family complaints detracts from immediate care, and discharging a deteriorating patient with peritonitis is life-threatening malpractice."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 50-year-old lorry driver is admitted with a first unprovoked generalized tonic-clonic seizure. You explain the mandatory DVLA regulations requiring him to cease driving immediately. The patient becomes furious and states: 'I will lose my job and mortgage. I am driving home from hospital and will never tell the DVLA'. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Explain the strict legal obligation not to drive, the medical reasons for this, and warn him that if he continues to drive you have a professional duty to notify the DVLA directly",
            "Explore his social and financial concerns empathetically and involve hospital social work or occupational health support",
            "If he still refuses to stop driving, discuss the case with the trust Caldicott Guardian or MDO, and notify the DVLA medical adviser in the public interest",
            "Call the police immediately without warning the patient while he is still on the ward",
            "Agree not to report him to the DVLA because doctor-patient confidentiality is absolute"
        ],
        "correct_answer": [
            "Explain the strict legal obligation not to drive, the medical reasons for this, and warn him that if he continues to drive you have a professional duty to notify the DVLA directly",
            "Explore his social and financial concerns empathetically and involve hospital social work or occupational health support",
            "If he still refuses to stop driving, discuss the case with the trust Caldicott Guardian or MDO, and notify the DVLA medical adviser in the public interest",
            "Call the police immediately without warning the patient while he is still on the ward",
            "Agree not to report him to the DVLA because doctor-patient confidentiality is absolute"
        ],
        "explanation": "GMC guidance on disclosing information about fitness to drive states that doctors must first explain the legal duty to the patient and warn them of the duty to disclose if they refuse. Exploring concerns helps engagement. If the patient persists in driving, disclosing to the DVLA to protect the public from serious harm is permitted and expected. Calling police without prior discussion is premature unless imminent driving occurs, and ignoring the threat breaches public protection duties."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A staff nurse administers an incorrect antibiotic to a patient because your handwriting on the paper drug chart was unclear. The patient suffers no adverse reaction. The nurse approaches you visibly upset, asking if you can rewrite the chart so that she does not face disciplinary action. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Assess the patient immediately to confirm they remain clinically well and have suffered no harm",
            "Explain kindly to the nurse that you cannot falsify or backdate records, but reassure her that clinical incidents are treated with a learning culture rather than blame",
            "Complete an incident report (Datix) together, noting both the unclear handwriting and the administration error as contributory factors",
            "Rewrite the chart as requested to protect the nurse's career since no harm occurred",
            "Report the nurse immediately to the Nursing and Midwifery Council (NMC) without discussing it with her"
        ],
        "correct_answer": [
            "Assess the patient immediately to confirm they remain clinically well and have suffered no harm",
            "Explain kindly to the nurse that you cannot falsify or backdate records, but reassure her that clinical incidents are treated with a learning culture rather than blame",
            "Complete an incident report (Datix) together, noting both the unclear handwriting and the administration error as contributory factors",
            "Rewrite the chart as requested to protect the nurse's career since no harm occurred",
            "Report the nurse immediately to the Nursing and Midwifery Council (NMC) without discussing it with her"
        ],
        "explanation": "Patient safety check comes first. Honesty in clinical documentation is non-negotiable; explaining why falsification is illegal while offering reassurance supports a just culture. Joint incident reporting addresses systemic factors (poor handwriting, verification checks). Falsifying charts is fraudulent, and reporting a single error directly to the NMC without local process is disproportionate and punitive."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You observe a senior surgical trainee pocketing several ampoules of Morphine from the ward controlled drugs cabinet without entering them in the CD register. When asked, the trainee claims they are for an acute trauma patient in theatre, but you know that theatre has its own separate drug supply. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Immediately inform the ward sister and the duty clinical manager/consultant about the unaccounted controlled drugs",
            "Check the controlled drugs register with the ward sister to confirm the discrepancy and document it formally",
            "Ensure the trainee does not administer uncontrolled medications to patients while the situation is investigated",
            "Confront the trainee aggressively in front of patients and staff on the ward",
            "Do nothing because controlled drugs are the sole responsibility of the nursing staff"
        ],
        "correct_answer": [
            "Immediately inform the ward sister and the duty clinical manager/consultant about the unaccounted controlled drugs",
            "Check the controlled drugs register with the ward sister to confirm the discrepancy and document it formally",
            "Ensure the trainee does not administer uncontrolled medications to patients while the situation is investigated",
            "Confront the trainee aggressively in front of patients and staff on the ward",
            "Do nothing because controlled drugs are the sole responsibility of the nursing staff"
        ],
        "explanation": "Controlled drugs legislation and GMC guidance require strict accountability; immediate senior escalation is essential to protect patients and the trainee. Formal auditing with the ward sister establishes the evidence base. Ensuring patient safety during investigation is vital. Public aggressive confrontation escalates conflict and breaches confidentiality, and ignoring CD diversion compromises patient safety and the law."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 55-year-old male patient admitted with chest pain refuses to be examined by you because of your ethnic background, loudly demanding: 'I only want a white British doctor treating me'. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Remain calm and professional, explain that all hospital doctors are fully qualified, and assess whether the patient has acute life-threatening instability",
            "If the patient is stable, inform the ward sister and supervising consultant of the patient's refusal and discriminatory behaviour",
            "Offer the patient the option to be seen by another team member if clinically feasible and safe, while reinforcing the hospital's zero-tolerance policy on discrimination",
            "Refuse to arrange any medical care for the patient and demand security immediately evict them from the hospital",
            "Engage in a shouting match with the patient to defend your professional honour"
        ],
        "correct_answer": [
            "Remain calm and professional, explain that all hospital doctors are fully qualified, and assess whether the patient has acute life-threatening instability",
            "If the patient is stable, inform the ward sister and supervising consultant of the patient's refusal and discriminatory behaviour",
            "Offer the patient the option to be seen by another team member if clinically feasible and safe, while reinforcing the hospital's zero-tolerance policy on discrimination",
            "Refuse to arrange any medical care for the patient and demand security immediately evict them from the hospital",
            "Engage in a shouting match with the patient to defend your professional honour"
        ],
        "explanation": "Maintaining professional composure while triaging acute clinical stability is primary. Escalating discriminatory behavior to seniors ensures trust support and policy enforcement. Accommodating care while setting boundaries protects the doctor and ensures patient safety. Evicting a potentially unstable chest pain patient risks death, and shouting is completely unprofessional."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "Your brother-in-law calls you on a Sunday evening asking you to write a private prescription for a course of oral Amoxicillin for his recurrent dental abscess, saying his dentist is closed until Tuesday. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Politely decline to prescribe, explaining that GMC guidance strictly advises against prescribing for family members except in life-threatening emergencies",
            "Direct him to contact NHS 111 or the local emergency out-of-hours dental service for proper dental assessment and treatment",
            "Advise him on appropriate over-the-counter analgesia (such as paracetamol or ibuprofen) in the interim",
            "Prescribe the amoxicillin this once on the condition that he promises not to ask again",
            "Take prescription pads from the hospital ward without authorization to write the prescription"
        ],
        "correct_answer": [
            "Politely decline to prescribe, explaining that GMC guidance strictly advises against prescribing for family members except in life-threatening emergencies",
            "Direct him to contact NHS 111 or the local emergency out-of-hours dental service for proper dental assessment and treatment",
            "Advise him on appropriate over-the-counter analgesia (such as paracetamol or ibuprofen) in the interim",
            "Prescribe the amoxicillin this once on the condition that he promises not to ask again",
            "Take prescription pads from the hospital ward without authorization to write the prescription"
        ],
        "explanation": "GMC Good Medical Practice guidance states that doctors must not prescribe for themselves or anyone with whom they have a close personal relationship unless no other doctor is available in an emergency. Directing to emergency dental services (NHS 111) is the safe clinical route. Advising standard OTC pain relief is helpful. Prescribing casually breaches guidelines, and stealing hospital prescription stationery is a criminal offense."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "During a private consultation in the GP surgery, a 35-year-old patient makes repeated romantic comments towards you, holds your hand, and asks you out on a dinner date. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Politely, firmly, and clearly explain that you are their doctor and that professional boundaries prohibit any personal or romantic relationship",
            "Offer to rearrange the consultation with a chaperone present or transfer their care to another doctor in the practice",
            "Document the interaction and the boundary explanation objectively in the patient's medical records immediately afterwards",
            "Agree to the dinner date provided it takes place in a town far away from the surgery",
            "Mock the patient and humiliate them in the waiting room"
        ],
        "correct_answer": [
            "Politely, firmly, and clearly explain that you are their doctor and that professional boundaries prohibit any personal or romantic relationship",
            "Offer to rearrange the consultation with a chaperone present or transfer their care to another doctor in the practice",
            "Document the interaction and the boundary explanation objectively in the patient's medical records immediately afterwards",
            "Agree to the dinner date provided it takes place in a town far away from the surgery",
            "Mock the patient and humiliate them in the waiting room"
        ],
        "explanation": "GMC guidance on maintaining professional boundaries mandates that doctors must establish and maintain clear professional boundaries with patients. Offering a chaperone or transfer of care protects both parties. Contemporaneous factual documentation provides transparency. Accepting romantic advances from a patient is an abuse of professional position that leads to erasure from the medical register, and public humiliation is abusive."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A surgical registrar asks you, an FY1, to insert a central venous line (CVC) in an acutely ill septic patient on the ward. You have observed two CVC insertions previously on a course but have never performed one on a live patient and do not feel competent to do so unsupervised. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Explain clearly and politely to the registrar that you have never performed this procedure on a patient and do not feel competent to do so unsupervised",
            "Offer to prepare the equipment and ultrasound machine and assist the registrar so that they perform it while supervising you",
            "If the registrar refuses to supervise and insists you do it alone, escalate to the duty consultant or critical care team",
            "Attempt the central line insertion independently hoping you will remember the steps from the course",
            "Pretend you have already inserted the line and forge the procedure note"
        ],
        "correct_answer": [
            "Explain clearly and politely to the registrar that you have never performed this procedure on a patient and do not feel competent to do so unsupervised",
            "Offer to prepare the equipment and ultrasound machine and assist the registrar so that they perform it while supervising you",
            "If the registrar refuses to supervise and insists you do it alone, escalate to the duty consultant or critical care team",
            "Attempt the central line insertion independently hoping you will remember the steps from the course",
            "Pretend you have already inserted the line and forge the procedure note"
        ],
        "explanation": "Doctors must recognize and work within the limits of their professional competence (GMC Good Medical Practice). Stating non-competence transparently protects the patient. Assisting and seeking supervision turns it into safe clinical training. Escalating to consultants is essential if seniors pressurize juniors into unsafe practice. Performing high-risk procedures beyond competence risks pneumothorax/arterial puncture, and falsifying procedure notes is fraudulent and dangerous."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "An 18-year-old man presents to the Emergency Department with a stab wound to his forearm. The wound is actively bleeding and requires formal closure. The patient is terrified and begs you not to call the police, claiming he was an innocent bystander. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Immediately control the haemorrhage, provide appropriate analgesia, and treat the physical injury as your primary priority",
            "Explain to the patient that under GMC guidance, doctors are required to notify the police of knife and gun wounds to protect public safety",
            "Inform the on-duty ED consultant and contact the police liaison team as per hospital trust policy",
            "Delay treating the bleeding wound until the police arrive and question the patient",
            "Refuse to treat the patient because knife crime involves criminal activity"
        ],
        "correct_answer": [
            "Immediately control the haemorrhage, provide appropriate analgesia, and treat the physical injury as your primary priority",
            "Explain to the patient that under GMC guidance, doctors are required to notify the police of knife and gun wounds to protect public safety",
            "Inform the on-duty ED consultant and contact the police liaison team as per hospital trust policy",
            "Delay treating the bleeding wound until the police arrive and question the patient",
            "Refuse to treat the patient because knife crime involves criminal activity"
        ],
        "explanation": "Immediate clinical resuscitation and wound care must always take priority over administrative or legal duties. GMC guidance on reporting gunshot and knife wounds states that police must usually be notified in the public interest, and the patient should be informed of this disclosure. Senior consultation ensures compliance with policy. Delaying urgent treatment is unacceptable, and refusing care breaches the fundamental duty of a doctor."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "While having lunch in a busy hospital public restaurant surrounded by visitors and patients, you hear two senior registrars loudly discussing a complex patient on ward 4, mentioning the patient's full name, room number, and sensitive psychiatric diagnosis. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Approach the registrars immediately and discreetly remind them that they are in a public area and their conversation is breaching patient confidentiality",
            "Suggest that they continue their clinical handover or case discussion in a private clinical office",
            "If they ignore you or respond dismissively, report the confidentiality breach to the hospital Caldicott Guardian or clinical director",
            "Loudly berate them in front of the entire cafeteria to make an example of them",
            "Join in the conversation to share your own experience with that patient"
        ],
        "correct_answer": [
            "Approach the registrars immediately and discreetly remind them that they are in a public area and their conversation is breaching patient confidentiality",
            "Suggest that they continue their clinical handover or case discussion in a private clinical office",
            "If they ignore you or respond dismissively, report the confidentiality breach to the hospital Caldicott Guardian or clinical director",
            "Loudly berate them in front of the entire cafeteria to make an example of them",
            "Join in the conversation to share your own experience with that patient"
        ],
        "explanation": "Immediate discreet intervention halts the ongoing breach of patient privacy without creating an unprofessional public scene. Directing colleagues to a private space supports legitimate clinical communication. Escalating to the Caldicott Guardian is appropriate if disregarded. Aggressive public confrontation is unprofessional, and joining in compounds the confidentiality breach."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 45-year-old woman with a significant head injury following a fall is brought to the ED smelling of alcohol. She is confused, disorientated, and has retrograde amnesia. A CT brain scan is strongly indicated. She becomes agitated, states 'I am going home right now', and attempts to walk out into traffic. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Assess her mental capacity specifically regarding her decision to leave hospital against medical advice",
            "Explain in simple terms the serious risks of intracranial haemorrhage and death if she leaves without a scan",
            "If she lacks capacity to refuse urgent treatment, act in her best interests under the Mental Capacity Act 2005 and detain her safely to perform the CT scan",
            "Immediately administer high-dose intravenous Haloperidol without attempting any de-escalation",
            "Allow her to leave immediately because adults are legally allowed to make their own choices"
        ],
        "correct_answer": [
            "Assess her mental capacity specifically regarding her decision to leave hospital against medical advice",
            "Explain in simple terms the serious risks of intracranial haemorrhage and death if she leaves without a scan",
            "If she lacks capacity to refuse urgent treatment, act in her best interests under the Mental Capacity Act 2005 and detain her safely to perform the CT scan",
            "Immediately administer high-dose intravenous Haloperidol without attempting any de-escalation",
            "Allow her to leave immediately because adults are legally allowed to make their own choices"
        ],
        "explanation": "Capacity is decision-specific; assessing whether she can understand, retain, weigh information, and communicate a decision is the essential first step. Providing clear risk explanations supports capacity. If she lacks capacity (due to intoxication/head injury), treating in her best interests under the MCA 2005 to prevent serious harm or death is legal and mandatory. Chemical restraint without verbal de-escalation is excessive, and allowing an incapacitated head injury patient to walk into traffic is gross negligence."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are collaborating on a departmental quality improvement project with a fellow trainee. You discover that your colleague has fabricated 40 data entries on the spreadsheet to make the audit results appear statistically significant for an upcoming national conference presentation. Rank the following actions in order of appropriateness (1 = Most appropriate, 5 = Least appropriate).",
        "options": [
            "Confront your colleague privately, state that fabricating scientific data is scientific fraud, and insist that the falsified data be withdrawn immediately",
            "Inform the project supervising consultant and the departmental audit lead of the data fabrication",
            "Withdraw your name from the abstract and presentation if the falsified data is not removed",
            "Agree to present the poster at the conference anyway because it will boost your portfolio for specialty applications",
            "Help the colleague fabricate additional data to make the conclusions look even more impressive"
        ],
        "correct_answer": [
            "Confront your colleague privately, state that fabricating scientific data is scientific fraud, and insist that the falsified data be withdrawn immediately",
            "Inform the project supervising consultant and the departmental audit lead of the data fabrication",
            "Withdraw your name from the abstract and presentation if the falsified data is not removed",
            "Agree to present the poster at the conference anyway because it will boost your portfolio for specialty applications",
            "Help the colleague fabricate additional data to make the conclusions look even more impressive"
        ],
        "explanation": "Research integrity is an absolute duty under GMC Good Medical Practice. Addressing the colleague directly and demanding withdrawal is the immediate professional course. Escalating to the supervising consultant protects scientific validity and clinical governance. Disassociating yourself prevents complicity. Knowingly presenting fabricated data is professional misconduct, and actively participating in fabrication is fraudulent."
    },

    # =========================================================================
    # SELECTION QUESTIONS (26 to 50)
    # Choose the THREE most appropriate actions from the 8 options provided.
    # =========================================================================
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are called to the hospital outpatient waiting area where an angry, agitated relative of a patient is shouting at the receptionist, slamming fists on the desk, and demanding immediate access to the consultant. Other patients and children are becoming frightened. Choose the THREE most appropriate initial actions.",
        "options": [
            "Ensure your personal safety and that of colleagues by maintaining a safe physical distance and a clear exit route",
            "Invite the relative calmly into a nearby quiet, private room away from other patients to de-escalate the situation",
            "Ask hospital security to attend or be on standby in case the situation turns physically violent",
            "Shout back at the relative to demonstrate authority and establish control",
            "Threaten to cancel the patient's upcoming surgery if the relative does not leave immediately",
            "Physically restrain the relative yourself before they touch the desk again",
            "Advise the receptionist to call the local newspaper to report the disruption",
            "Instruct all clinic staff to abandon the clinic and go home"
        ],
        "correct_answer": [
            "Ensure your personal safety and that of colleagues by maintaining a safe physical distance and a clear exit route",
            "Invite the relative calmly into a nearby quiet, private room away from other patients to de-escalate the situation",
            "Ask hospital security to attend or be on standby in case the situation turns physically violent"
        ],
        "explanation": "When managing agitated individuals, staff safety is paramount (maintaining distance and exit routes). Verbal de-escalation in a quiet, private space protects other patients and helps listen to grievances constructively. Alerting security ensures immediate backup if physical violence threatens. Shouting back, making punitive threats, physical grappling, and abandoning clinical duties are unsafe and unprofessional."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "The daughter of an inpatient who died on your ward 2 days ago submits an urgent formal complaint stating that the medical team communicated poorly, delayed pain relief, and acted insensitively. Choose the THREE most appropriate actions for the ward team.",
        "options": [
            "Acknowledge the complaint promptly and arrange a face-to-face meeting with the consultant and senior nursing staff to listen to their concerns",
            "Review the patient's medical and nursing notes thoroughly prior to the meeting to establish an accurate chronology of events",
            "Offer a sincere apology for the family's distress and explain the findings of the review openly under the Duty of Candour",
            "Refuse to speak with the daughter because formal complaints must only be handled through court proceedings",
            "Blame the junior doctor on night shift directly in the written response",
            "Alter the nursing drug administration records to show timely analgesia delivery",
            "Instruct the family that complaining about NHS staff is unacceptable",
            "Discard the patient's records to prevent further investigation"
        ],
        "correct_answer": [
            "Acknowledge the complaint promptly and arrange a face-to-face meeting with the consultant and senior nursing staff to listen to their concerns",
            "Review the patient's medical and nursing notes thoroughly prior to the meeting to establish an accurate chronology of events",
            "Offer a sincere apology for the family's distress and explain the findings of the review openly under the Duty of Candour"
        ],
        "explanation": "Complaints should be handled constructively and empathetically. Reviewing factual records establishes the clinical reality. A senior face-to-face meeting demonstrates accountability and listening. Acknowledging distress and apologizing under the Duty of Candour is ethical practice. Blaming colleagues, refusing communication, altering charts, and destroying records are unethical and illegal."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "An inpatient with severe penicillin allergy is accidentally administered intravenous Co-amoxiclav due to a failure to check allergy wristbands. Within 3 minutes, the patient develops facial swelling, severe wheeze, and hypotension. Choose the THREE most immediate and appropriate actions.",
        "options": [
            "Stop the antibiotic infusion immediately",
            "Administer intramuscular Adrenaline (500 micrograms 1:1,000) and call the resuscitation emergency team (2222)",
            "Once the patient is stabilized, explain the error openly and apologize to the patient under the statutory Duty of Candour",
            "Wait 30 minutes to see if the wheeze resolves spontaneously before intervening",
            "Administer oral paracetamol and discharge the patient home",
            "Quietly dispose of the infusion bag and deny that any medication was given",
            "Advise the nurse not to log an incident report so that the ward does not get penalized",
            "Tell the patient they must have developed a new allergy that was never documented"
        ],
        "correct_answer": [
            "Stop the antibiotic infusion immediately",
            "Administer intramuscular Adrenaline (500 micrograms 1:1,000) and call the resuscitation emergency team (2222)",
            "Once the patient is stabilized, explain the error openly and apologize to the patient under the statutory Duty of Candour"
        ],
        "explanation": "Immediate cessation of the offending allergen and emergency resuscitation with IM adrenaline are life-saving emergency priorities. Open disclosure, apology, and incident reporting under the Duty of Candour are mandatory once stable. Delaying therapy, covering up errors, and lying to patients are gross violations of medical duty."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are working an intense acute medical rotation. For the third time this week, you have worked 3 hours past your scheduled shift end without a meal or rest break, and your rota coordinator asks you to cover an extra weekend night shift. Choose the THREE most appropriate professional actions.",
        "options": [
            "Submit electronic Exception Reports for the additional hours worked and missed rest breaks according to your junior doctor contract",
            "Discuss your current workload, fatigue, and burnout concerns with your Educational Supervisor or Guardian of Safe Working Hours",
            "Politely decline the additional locum shift, explaining that your current fatigue would compromise safe patient care",
            "Falsify your time sheets to claim double locum rates for your contracted hours",
            "Vent your anger by posting identifying complaints about your hospital rota on social media",
            "Accept the extra shift and take sedatives during the day and stimulants on duty",
            "Walk out halfway through your next shift without handing over to demonstrate your frustration",
            "Instruct all medical students on the ward to take over doctor prescribing tasks"
        ],
        "correct_answer": [
            "Submit electronic Exception Reports for the additional hours worked and missed rest breaks according to your junior doctor contract",
            "Discuss your current workload, fatigue, and burnout concerns with your Educational Supervisor or Guardian of Safe Working Hours",
            "Politely decline the additional locum shift, explaining that your current fatigue would compromise safe patient care"
        ],
        "explanation": "Exception reporting is the contractual mechanism to highlight unsafe hours and trigger rota reviews. Raising concerns with the Guardian of Safe Working Hours ensures systemic governance. Declining voluntary extra shifts when fatigued upholds patient safety. Falsification, unprofessional social media venting, drug misuse, and abandoning shifts without handover are dangerous and unethical."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "Two police officers arrive at the ward reception demanding to view the medical notes and take blood samples from an admitted patient whom they suspect was involved in an assault earlier that evening. The patient is asleep. Choose the THREE most appropriate actions.",
        "options": [
            "Explain politely to the officers that patient medical records are confidential and cannot be disclosed without the patient's informed consent or a formal court warrant",
            "Contact the hospital Caldicott Guardian or on-call trust legal adviser for guidance on disclosure in the public interest",
            "Ask the police officers to explain the statutory legal basis of their request and whether an immediate threat to public safety exists",
            "Hand over the paper notes immediately because police requests always override medical confidentiality",
            "Take the blood sample from the sleeping patient without their knowledge or consent",
            "Order the police officers to leave the hospital premises immediately under threat of arrest",
            "Wake the patient and force them to speak to the police against their will",
            "Delete the patient's electronic records so that the police cannot access them"
        ],
        "correct_answer": [
            "Explain politely to the officers that patient medical records are confidential and cannot be disclosed without the patient's informed consent or a formal court warrant",
            "Contact the hospital Caldicott Guardian or on-call trust legal adviser for guidance on disclosure in the public interest",
            "Ask the police officers to explain the statutory legal basis of their request and whether an immediate threat to public safety exists"
        ],
        "explanation": "Confidentiality is a fundamental legal and ethical principle. Police requests do not automatically override confidentiality unless authorized by statute (e.g., Road Traffic Act, Terrorism Act), a court order, or when disclosure is essential to prevent death or serious crime. Involving the Caldicott Guardian ensures legal compliance. Taking unconsented blood or releasing records without authority is unlawful."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are conducting the morning medical handover at 08:30 following a hectic night shift. Choose the THREE most essential components of a safe, structured clinical handover according to Royal College of Physicians (RCP) guidelines.",
        "options": [
            "Use a standardized communication framework (such as SBAR: Situation, Background, Assessment, Recommendation)",
            "Highlight and prioritize acutely deteriorating patients, outstanding urgent tasks, and results pending review",
            "Ensure a designated, protected quiet environment with minimal interruptions and clear leadership from both day and night teams",
            "Rely exclusively on informal corridor conversations without written or electronic task tracking",
            "Skip the handover if the night shift was busy to allow night staff to leave immediately",
            "Leave handover sheets containing identifiable patient data on the reception desk",
            "Hand over only patients who were admitted during the last 2 hours of the shift",
            "Discuss personal social gossip about colleagues before reviewing sick patients"
        ],
        "correct_answer": [
            "Use a standardized communication framework (such as SBAR: Situation, Background, Assessment, Recommendation)",
            "Highlight and prioritize acutely deteriorating patients, outstanding urgent tasks, and results pending review",
            "Ensure a designated, protected quiet environment with minimal interruptions and clear leadership from both day and night teams"
        ],
        "explanation": "RCP and GMC guidelines emphasize that high-quality clinical handover requires structured frameworks (SBAR), clear prioritization of sick/unstable patients and pending investigations, and a protected environment with minimal distractions. Informal handovers, skipping handover, and leaving patient sheets in public spaces cause clinical errors and breach confidentiality."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "An 82-year-old man with severe vascular dementia presents with a ruptured abdominal aortic aneurysm (AAA) and haemodynamic collapse. He is confused and unable to understand or weigh treatment decisions. His vascular consultant indicates that emergency endovascular repair offers a reasonable chance of survival. Choose the THREE most appropriate actions under the Mental Capacity Act 2005.",
        "options": [
            "Assess and document that the patient lacks mental capacity to consent to or refuse the emergency surgical intervention",
            "Act in the patient's best interests to provide emergency life-saving treatment",
            "Consult the patient's next-of-kin or lasting power of attorney (if available) to ascertain the patient's prior beliefs, values, and wishes",
            "Delay the emergency surgery for 48 hours while awaiting a formal Court of Protection ruling",
            "Assume that all patients with dementia should automatically be made DNR and refused surgery",
            "Require the family to sign an agreement accepting personal financial liability for the surgery",
            "Ignore the emergency and discharge the patient to a care home",
            "Wait for the patient to regain capacity before performing any intervention"
        ],
        "correct_answer": [
            "Assess and document that the patient lacks mental capacity to consent to or refuse the emergency surgical intervention",
            "Act in the patient's best interests to provide emergency life-saving treatment",
            "Consult the patient's next-of-kin or lasting power of attorney (if available) to ascertain the patient's prior beliefs, values, and wishes"
        ],
        "explanation": "Under the Mental Capacity Act 2005, when an incapacitated patient requires emergency life-saving intervention, clinicians have a legal duty to assess and document capacity, consult family/attorneys regarding known prior wishes and values, and proceed with treatment in the patient's best interests. Waiting days for court orders in acute rupture causes death, and blanket discrimination based on dementia is unethical."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You spent 4 months designing, collecting data for, and analyzing a departmental audit on sepsis bundle compliance. At a regional meeting, you discover that your senior colleague has submitted the abstract and presented the work with themselves as sole author, completely omitting your name and contribution. Choose the THREE most constructive and appropriate initial actions.",
        "options": [
            "Arrange a private, professional meeting with the colleague to discuss the omission and review the original project documentation",
            "Gather your dated project proposals, spreadsheets, and communications to establish clear evidence of your contribution",
            "Raise the issue with the departmental audit lead or clinical director if the colleague refuses to acknowledge your contribution",
            "Send an abusive email to all consultants in the hospital denouncing the colleague",
            "Post allegations of intellectual theft on public social media forums",
            "Vandalize the colleague's presentation poster at the conference",
            "Delete all master audit databases from the trust servers to prevent anyone from using them",
            "Drop out of medicine entirely without discussing the issue"
        ],
        "correct_answer": [
            "Arrange a private, professional meeting with the colleague to discuss the omission and review the original project documentation",
            "Gather your dated project proposals, spreadsheets, and communications to establish clear evidence of your contribution",
            "Raise the issue with the departmental audit lead or clinical director if the colleague refuses to acknowledge your contribution"
        ],
        "explanation": "Professional disputes regarding authorship should be handled calmly through direct communication backed by documentary evidence. If informal resolution fails, escalation to departmental leadership (audit lead, clinical director) provides objective mediation. Defamatory emails, public social media attacks, and sabotage of hospital files are unprofessional and actionable misconduct."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You observe a senior orthopaedic consultant repeatedly entering the surgical ward and examining patient wounds without washing their hands, wearing long-sleeved suit jackets, and refusing to adhere to the hospital's 'bare below the elbows' policy. Choose the THREE most appropriate professional actions.",
        "options": [
            "Politely and tactfully remind the consultant of the trust's 'bare below the elbows' and hand hygiene policy prior to them touching a patient",
            "Consistently lead by example by practicing exemplary hand hygiene and infection control yourself",
            "Discuss the persistent infection control breach with the ward sister or hospital infection prevention and control (IPC) lead",
            "Take surreptitious photos of the consultant and post them online to shame them publicly",
            "Stop washing your own hands to fit in with the consultant's practice",
            "Physically push the consultant away from the patient's bedside",
            "Tell the patient that the consultant is dangerous and advise them to self-discharge",
            "Ignore the behavior completely because senior consultants are exempt from infection control rules"
        ],
        "correct_answer": [
            "Politely and tactfully remind the consultant of the trust's 'bare below the elbows' and hand hygiene policy prior to them touching a patient",
            "Consistently lead by example by practicing exemplary hand hygiene and infection control yourself",
            "Discuss the persistent infection control breach with the ward sister or hospital infection prevention and control (IPC) lead"
        ],
        "explanation": "GMC guidance states that all doctors have a duty to challenge unsafe practice regardless of the seniority of the person involved. Tactful direct reminders at the bedside uphold safety. Exemplary personal practice reinforces standards. Escalating to IPC leads addresses recurrent systemic non-compliance. Secret photography, physical aggression, and copying bad practice are unprofessional."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A distressed son contacts the bereavement office demanding immediate access to the complete medical records of his late father who died 3 weeks ago, suspecting medical negligence. Choose the THREE most appropriate actions.",
        "options": [
            "Express sincere condolences and handle the family's request with empathy and professionalism",
            "Explain the formal legal process under the Access to Health Records Act 1990 for accessing deceased patients' records",
            "Direct the son to the hospital's Patient Advice and Liaison Service (PALS) and the Information Governance / Medical Records team",
            "Hand over the original physical medical notes directly across the counter",
            "Refuse all assistance and tell the son that dead patients have no records",
            "Shred the deceased patient's notes to prevent litigation against the hospital",
            "Demand payment in cash directly to yourself before releasing any papers",
            "Tell the son that only a high court judge can ever view medical notes"
        ],
        "correct_answer": [
            "Express sincere condolences and handle the family's request with empathy and professionalism",
            "Explain the formal legal process under the Access to Health Records Act 1990 for accessing deceased patients' records",
            "Direct the son to the hospital's Patient Advice and Liaison Service (PALS) and the Information Governance / Medical Records team"
        ],
        "explanation": "Under the Access to Health Records Act 1990, personal representatives and individuals with a claim arising from a patient's death have a right to apply for access. Compassionate communication and directing relatives through proper legal channels (PALS, Information Governance) is correct practice. Handing over original notes risks loss/tampering, and destroying notes is criminal."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A 22-year-old woman attends the GP practice requesting a referral for an elective termination of pregnancy at 8 weeks gestation. The consulting doctor holds a strong personal conscientious objection to abortion. Choose the THREE most appropriate professional actions according to GMC guidance.",
        "options": [
            "Treat the patient with respect, compassion, and without expressing moral judgment or disapproval",
            "Inform the patient promptly and sensitively of the conscientious objection to providing this service",
            "Ensure the patient is promptly and seamlessly referred to another healthcare professional who can facilitate the service without delay",
            "Attempt to persuade the patient that abortion is morally wrong and show them graphic anti-abortion pictures",
            "Refuse to refer the patient or provide any information about alternative clinics",
            "Inform the patient's parents of her pregnancy without her consent",
            "Prescribe medication designed to induce medical complications",
            "Tell the patient she must wait until 24 weeks before making a decision"
        ],
        "correct_answer": [
            "Treat the patient with respect, compassion, and without expressing moral judgment or disapproval",
            "Inform the patient promptly and sensitively of the conscientious objection to providing this service",
            "Ensure the patient is promptly and seamlessly referred to another healthcare professional who can facilitate the service without delay"
        ],
        "explanation": "GMC guidance on personal beliefs and medical practice permits conscientious objection to abortion, but doctors MUST treat patients with respect, declare their objection promptly without judgment, and ensure immediate referral to another willing clinician so patient care is not delayed. Preaching, refusing referral, and breaching confidentiality are gross misconduct."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "During a routine cervical smear consultation, a 30-year-old woman breaks down in tears and discloses that her partner is physically and emotionally abusive, has isolated her from family, and threatened to kill her if she leaves. Choose the THREE most appropriate initial professional responses.",
        "options": [
            "Validate her disclosure, listen supportively in private, and reassure her that she is not to blame",
            "Assess her immediate physical safety, whether she has children at home, and if she feels safe returning home today",
            "Offer immediate confidential signposting and referral to specialized domestic abuse services (e.g. hospital IDVA, National Domestic Abuse Helpline)",
            "Call the partner immediately to demand an explanation for his abusive behaviour",
            "Instruct the patient to pack her bags and leave her partner this afternoon without a safety plan",
            "Tell the patient that domestic arguments are normal in relationships and dismiss her concerns",
            "Force the patient to report the matter to the police immediately against her will when no children are involved",
            "Document the abuse in a letter sent to the shared home address"
        ],
        "correct_answer": [
            "Validate her disclosure, listen supportively in private, and reassure her that she is not to blame",
            "Assess her immediate physical safety, whether she has children at home, and if she feels safe returning home today",
            "Offer immediate confidential signposting and referral to specialized domestic abuse services (e.g. hospital IDVA, National Domestic Abuse Helpline)"
        ],
        "explanation": "Supportive listening, validating disclosure, assessing immediate safety (and safeguarding of children), and linking with specialist domestic abuse advocates (IDVA) are essential. Contacting the abuser endangers the patient's life, forcing unplanned departures without safety planning is hazardous, and sending written letters home puts victims at extreme risk of violence."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "During an emergency resuscitation of a patient in cardiac arrest, the team leader charges the defibrillator to deliver a shock for ventricular fibrillation, but the device displays a 'battery depleted' error and powers down. Choose the THREE most appropriate immediate actions.",
        "options": [
            "Continue high-quality chest compressions and manual bag-valve-mask ventilation without interruption",
            "Immediately dispatch a team member to fetch the backup defibrillator from the adjacent resuscitation bay or ward",
            "Connect the failed defibrillator to mains power immediately while checking connections",
            "Stop chest compressions and wait for the medical equipment maintenance engineer to arrive",
            "Declare death immediately because equipment failure cannot be overcome",
            "Begin arguing loudly with the ward nurse about who forgot to charge the machine",
            "Hit the defibrillator repeatedly with your fists to restart the battery",
            "Evacuate the resuscitation room"
        ],
        "correct_answer": [
            "Continue high-quality chest compressions and manual bag-valve-mask ventilation without interruption",
            "Immediately dispatch a team member to fetch the backup defibrillator from the adjacent resuscitation bay or ward",
            "Connect the failed defibrillator to mains power immediately while checking connections"
        ],
        "explanation": "In Resuscitation Council guidelines, minimizing interruptions to high-quality chest compressions is paramount for coronary and cerebral perfusion. Rapidly retrieving a secondary defibrillator from nearby clinical areas and connecting the primary unit to mains electricity provides rapid problem resolution. Stopping CPR, arguing, or premature termination of resuscitation costs lives."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "Following the traumatic, unsuccessful resuscitation of an 8-year-old child in the ED, you find your junior FY1 colleague sobbing alone in the staff changing room, visibly distressed and stating: 'I feel like a terrible doctor and can't go on'. Choose the THREE most supportive and professional actions.",
        "options": [
            "Sit with the colleague in private, offer immediate emotional support, and listen without judgment",
            "Ensure they are relieved of clinical duties for the immediate remainder of the shift to recover and debrief",
            "Encourage participation in the multidisciplinary team debrief and signpost to NHS Practitioner Health or staff counselling services",
            "Tell them to stop crying because doctors must never show emotion in front of others",
            "Assign them to clerk the next three waiting room patients to distract them from their feelings",
            "Inform all staff in the handover that the FY1 is emotionally unstable",
            "Record their crying on your phone to show their supervisor as evidence of unfitness to practice",
            "Advise them to drink alcohol heavily when they get home"
        ],
        "correct_answer": [
            "Sit with the colleague in private, offer immediate emotional support, and listen without judgment",
            "Ensure they are relieved of clinical duties for the immediate remainder of the shift to recover and debrief",
            "Encourage participation in the multidisciplinary team debrief and signpost to NHS Practitioner Health or staff counselling services"
        ],
        "explanation": "Critical incident debriefing and compassionate peer support are vital following traumatic deaths. Relieving the colleague from immediate duties prevents compounded distress and protects patient safety. Encouraging structured team debriefs and signposting to wellbeing support facilitates healthy coping. Repressing emotions, forcing immediate work, and shaming are harmful."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A 48-year-old man admitted with acute diverticulitis insists on discharging himself against medical advice (DAMA) at 23:00 because he needs to feed his pets. He has full mental capacity and understands the risks. Choose the THREE most appropriate professional actions.",
        "options": [
            "Clearly explain the specific clinical risks of self-discharge, including risk of perforation, sepsis, and death",
            "Provide appropriate discharge medications (e.g. oral antibiotics), clear safety-netting instructions, and advise him he can return at any time",
            "Document the capacity assessment, discussion of risks, and self-discharge objectively in the medical record",
            "Refuse to let him leave the hospital building and instruct security to lock the ward doors",
            "Withhold his belongings, coat, and wallet to coerce him into staying",
            "Tell him that if he discharges himself, he will be permanently banned from the NHS",
            "Sedate him against his will to prevent him from leaving",
            "Refuse to prescribe any oral antibiotics or provide advice because he is non-compliant"
        ],
        "correct_answer": [
            "Clearly explain the specific clinical risks of self-discharge, including risk of perforation, sepsis, and death",
            "Provide appropriate discharge medications (e.g. oral antibiotics), clear safety-netting instructions, and advise him he can return at any time",
            "Document the capacity assessment, discussion of risks, and self-discharge objectively in the medical record"
        ],
        "explanation": "Competent adults have the legal right to discharge themselves against medical advice. Clinicians must explain risks clearly, mitigate harm by providing discharge medication and safety-netting (harm reduction), reassure them they can return without penalty, and document the encounter thoroughly. Detention, coercion, threats, and withholding treatment are unlawful and punitive."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "While reviewing a patient admitted overnight with pneumonia, you notice on the admission chest X-ray that a prominent 3 cm lung mass was overlooked by the admitting doctor, who only reported consolidation. Choose the THREE most appropriate professional actions.",
        "options": [
            "Discuss the X-ray findings promptly with your supervising consultant or a radiologist for formal review",
            "Commence appropriate investigation pathways (such as an urgent contrast CT chest) and explain the new finding sensitively to the patient",
            "Discuss the missed finding constructively and privately with the admitting doctor as a learning opportunity, completing an incident report (Datix)",
            "Conceal the missed mass in the notes to protect your colleague from criticism",
            "Publicly humiliate the admitting doctor during grand rounds",
            "Tell the patient that the night doctor was incompetent and advise them to sue",
            "Crop the chest X-ray digital image to hide the mass",
            "Discharge the patient without mentioning the mass"
        ],
        "correct_answer": [
            "Discuss the X-ray findings promptly with your supervising consultant or a radiologist for formal review",
            "Commence appropriate investigation pathways (such as an urgent contrast CT chest) and explain the new finding sensitively to the patient",
            "Discuss the missed finding constructively and privately with the admitting doctor as a learning opportunity, completing an incident report (Datix)"
        ],
        "explanation": "Patient care and diagnostic safety come first: getting formal senior/radiological review and initiating appropriate investigation (CT chest) protects the patient. Transparent communication under duty of candour is required. Feeding back constructively to the colleague promotes learning. Concealing diagnostic errors, public shaming, or destroying images is dangerous misconduct."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A patient you treated for an uncomplicated ankle injury in the ED writes you a letter expressing intense romantic feelings towards you and asks to meet for a drink. Choose the THREE most appropriate professional actions according to GMC guidance.",
        "options": [
            "Do not accept the invitation and maintain strictly professional boundaries",
            "Discuss the letter promptly with your educational supervisor or clinical lead for guidance and support",
            "Document the receipt of the letter and your response objectively in the patient's record or discuss with senior staff",
            "Accept the invitation to meet for a drink to see if you are compatible",
            "Send an affectionate reply from your personal email account",
            "Mock the patient on your social media accounts",
            "Threaten the patient with legal action and police arrest",
            "Give the patient's letter to other patients in the waiting room"
        ],
        "correct_answer": [
            "Do not accept the invitation and maintain strictly professional boundaries",
            "Discuss the letter promptly with your educational supervisor or clinical lead for guidance and support",
            "Document the receipt of the letter and your response objectively in the patient's record or discuss with senior staff"
        ],
        "explanation": "GMC guidance on maintaining professional boundaries explicitly prohibits pursuing or accepting romantic relationships with patients. Seeking senior guidance and documenting the event provides transparency and protection. Accepting romantic approaches, sharing personal contact details, or mocking patients breaches professional ethics."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "During an emergency caesarean section, you sustain a sharps injury when a suture needle slips and punctures your glove and skin. The patient's HIV and hepatitis status is unknown. Choose the THREE most appropriate immediate actions.",
        "options": [
            "Stop assisting immediately and step away from the operative field safely to prevent patient contamination",
            "Gently encourage bleeding under warm running water and wash with soap and water without scrubbing",
            "Report immediately to Occupational Health or the ED for risk assessment and consideration of post-exposure prophylaxis (PEP)",
            "Continue operating for another hour until the surgery is completely finished",
            "Scrub the puncture site vigorously with a sterile wire brush and neat iodine",
            "Refuse to report the injury because sharps injuries are embarrassing",
            "Take a confidential blood sample from the patient without consent while they are anaesthetized",
            "Advise the surgical team to ignore the incident"
        ],
        "correct_answer": [
            "Stop assisting immediately and step away from the operative field safely to prevent patient contamination",
            "Gently encourage bleeding under warm running water and wash with soap and water without scrubbing",
            "Report immediately to Occupational Health or the ED for risk assessment and consideration of post-exposure prophylaxis (PEP)"
        ],
        "explanation": "Stepping back safely protects the patient from blood exposure. Immediate wound washing without harsh abrasives reduces viral inoculate. Rapid Occupational Health assessment ensures PEP can be initiated within the 1-hour window if indicated. Continuing to operate risks patient contamination, abrasive scrubbing increases tissue vulnerability, and taking unconsented blood from an anaesthetized patient is unlawful."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "While on a commercial passenger flight, the cabin crew make an urgent announcement asking if there is a doctor on board to assist an acutely unwell passenger who is breathless and clutching their chest. Choose the THREE most appropriate actions.",
        "options": [
            "Identify yourself to the cabin crew, show your medical identification, and volunteer your assistance",
            "Assess the passenger systematically using an ABCDE approach and liaise with the flight crew to access the on-board emergency medical kit",
            "Recognize and work within the limits of your competence in the aviation environment, consulting the airline's ground-based medical support team if available",
            "Pretend to be asleep so that you do not have to get involved",
            "Demand upfront payment in cash from the passenger before providing emergency medical assistance",
            "Perform an emergency thoracotomy in the aircraft aisle with butter knives",
            "Insist the pilot immediately divert the aircraft before you have even assessed the patient",
            "Administer all medications in the aircraft kit simultaneously"
        ],
        "correct_answer": [
            "Identify yourself to the cabin crew, show your medical identification, and volunteer your assistance",
            "Assess the passenger systematically using an ABCDE approach and liaise with the flight crew to access the on-board emergency medical kit",
            "Recognize and work within the limits of your competence in the aviation environment, consulting the airline's ground-based medical support team if available"
        ],
        "explanation": "GMC guidance states that doctors have a professional obligation to offer assistance in emergencies wherever they occur (Good Samaritan principle). Systematic ABCDE evaluation with available aircraft resources is the standard of care. Working within competence and collaborating with ground tele-medical support assists diversion decisions. Feigning sleep, demanding cash, and extreme interventions are dangerous and unethical."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A surgical colleague stops you in the hospital corridor and asks if you can quickly examine a persistent pigmented lesion on their back and write them a prescription for strong topical steroids. Choose the THREE most appropriate professional actions.",
        "options": [
            "Politely explain that corridor consultations are unsafe and that you cannot provide informal medical care or prescriptions for colleagues",
            "Advise your colleague to register with and consult their own General Practitioner for an objective assessment and referral if indicated",
            "Offer support in helping them arrange time off to attend a GP appointment if workload is a barrier",
            "Write the prescription on a hospital scrap paper without taking a history",
            "Examine the lesion in the public corridor in front of visitors",
            "Prescribe oral systemic chemotherapy informally",
            "Inform the colleague's department that they are unfit to work",
            "Ignore the colleague and walk away without responding"
        ],
        "correct_answer": [
            "Politely explain that corridor consultations are unsafe and that you cannot provide informal medical care or prescriptions for colleagues",
            "Advise your colleague to register with and consult their own General Practitioner for an objective assessment and referral if indicated",
            "Offer support in helping them arrange time off to attend a GP appointment if workload is a barrier"
        ],
        "explanation": "GMC guidance explicitly states that doctors must not treat colleagues informally or prescribe outside a formal clinical setting, as objectivity and safety are compromised. Advising them to consult their independent GP ensures proper records and clinical safety. Supporting them to take time for medical appointments encourages wellbeing. Informal prescriptions and public examinations breach standards."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You notice that a new FY1 on your team has been arriving 45 minutes late every day, appears exhausted and unkempt, and has omitted several critical routine blood tests on ward patients. Choose the THREE most constructive and supportive initial actions.",
        "options": [
            "Arrange a private, supportive conversation to ask how they are settling in and whether they are experiencing personal or professional difficulties",
            "Offer practical assistance and guidance on time management, task prioritization, and ward routines",
            "Encourage them to discuss their situation with their educational supervisor or clinical tutor for structured support",
            "Reprimand the FY1 loudly in front of the nursing staff and patients during ward rounds",
            "File a formal complaint to the GMC immediately without speaking to them",
            "Do all their work for them secretly so no one notices their difficulties",
            "Post comments on social media about how incompetent modern FY1 doctors are",
            "Demand that they resign from the training programme immediately"
        ],
        "correct_answer": [
            "Arrange a private, supportive conversation to ask how they are settling in and whether they are experiencing personal or professional difficulties",
            "Offer practical assistance and guidance on time management, task prioritization, and ward routines",
            "Encourage them to discuss their situation with their educational supervisor or clinical tutor for structured support"
        ],
        "explanation": "Approaching a struggling junior colleague with empathy and constructive inquiry identifies underlying struggles early. Practical mentoring and task organization provides immediate workplace support. Involving educational supervisors ensures formal developmental resources. Public shaming, premature GMC referrals, and social media mocking are toxic and unhelpful."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "During a consultation in the outpatient clinic, you notice that the patient has placed their smartphone on the desk and is openly video-recording your conversation. Choose the THREE most appropriate professional actions.",
        "options": [
            "Acknowledge the recording calmly and ask the patient about their reasons for recording the consultation",
            "Reassure the patient that you want them to feel comfortable and that recording can be helpful for remembering complex medical discussions",
            "Ensure that any recording does not breach the privacy or confidentiality of other patients or staff in the clinic",
            "Demand that the patient hand over their smartphone immediately so you can delete the recording",
            "Refuse to provide any medical care and storm out of the consultation room",
            "Call hospital security to have the patient forcefully searched and evicted",
            "Snatch the phone from the desk and smash it on the floor",
            "Pretend you did not notice and deliver substandard care intentionally"
        ],
        "correct_answer": [
            "Acknowledge the recording calmly and ask the patient about their reasons for recording the consultation",
            "Reassure the patient that you want them to feel comfortable and that recording can be helpful for remembering complex medical discussions",
            "Ensure that any recording does not breach the privacy or confidentiality of other patients or staff in the clinic"
        ],
        "explanation": "Patients have a legal right to record their own consultations for personal use. Acknowledging this openly and exploring reasons (e.g. anxiety, memory aid) builds trust and rapport. Ensuring other patients' privacy is protected is reasonable. Confiscating property, physical confrontation, and refusing care are aggressive and completely unlawful."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "An 85-year-old frail woman with polypharmacy is admitted with recurrent falls. On reviewing her chart, you note she is prescribed 12 different regular medications, including sedatives, antihypertensives, and anticholinergics. Choose the THREE most appropriate pharmacological safety actions.",
        "options": [
            "Conduct a structured medication review using validated criteria (such as STOPP/START) to identify inappropriate medications and fall-risk drugs",
            "Deprescribe non-essential medications (e.g. sedatives, anticholinergics) in a planned, gradual, and monitored manner with the patient's agreement",
            "Check for postural hypotension by measuring both lying and standing blood pressure",
            "Double the doses of all sedatives to prevent her from attempting to get out of bed",
            "Stop all 12 medications abruptly without clinical justification or monitoring",
            "Add three new antihypertensive agents simultaneously without checking blood pressure",
            "Advise the family that elderly patients should never take any medications",
            "Refuse to review the medication chart because prescribing was done by her GP"
        ],
        "correct_answer": [
            "Conduct a structured medication review using validated criteria (such as STOPP/START) to identify inappropriate medications and fall-risk drugs",
            "Deprescribe non-essential medications (e.g. sedatives, anticholinergics) in a planned, gradual, and monitored manner with the patient's agreement",
            "Check for postural hypotension by measuring both lying and standing blood pressure"
        ],
        "explanation": "Structured medication review using STOPP/START criteria reduces adverse drug events and fall risk in the frail elderly. Deprescribing sedatives and anticholinergics with patient involvement promotes safety. Measuring lying and standing BP identifies orthostatic hypotension. Over-sedation increases falls, stopping all drugs abruptly causes withdrawal crises, and failing to review charts is negligence."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A 35-year-old man presents to the GP surgery with a 3-day history of clear rhinorrhoea, mild sore throat, and a dry cough. His vitals are normal and chest examination is completely clear. He aggressively demands an immediate prescription for oral Amoxicillin, stating: 'I need antibiotics to get back to work tomorrow'. Choose the THREE most appropriate professional actions.",
        "options": [
            "Explain clearly and empathetically that his symptoms indicate a self-limiting viral infection for which antibiotics are ineffective and cause harm",
            "Offer evidence-based symptomatic advice on self-care, hydration, paracetamol, and honey for cough",
            "Provide clear, documented safety-netting advice on red-flag symptoms that should prompt reassessment (such as high fever, hemoptysis, or severe dyspnoea)",
            "Prescribe a 14-day course of broad-spectrum antibiotics to end the consultation quickly",
            "Give him a course of intravenous antibiotics in the surgery",
            "Shout at the patient for contributing to global antimicrobial resistance",
            "Refuse to speak with the patient ever again",
            "Prescribe oral steroids and strong opioids for mild coryza"
        ],
        "correct_answer": [
            "Explain clearly and empathetically that his symptoms indicate a self-limiting viral infection for which antibiotics are ineffective and cause harm",
            "Offer evidence-based symptomatic advice on self-care, hydration, paracetamol, and honey for cough",
            "Provide clear, documented safety-netting advice on red-flag symptoms that should prompt reassessment (such as high fever, hemoptysis, or severe dyspnoea)"
        ],
        "explanation": "Antimicrobial stewardship guidelines mandate not prescribing antibiotics for uncomplicated viral upper respiratory infections. Patient education explaining viral etiology, recommending symptom relief, and providing robust safety netting empowers patients safely. Inappropriate prescribing fuels resistance and side effects, and verbal aggression is unprofessional."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "In the operating theatre, just as the scrub nurse is about to hand the scalpel to the consultant surgeon to begin an elective right total hip replacement, you notice that the surgical site marked on the skin is the LEFT hip, which contradicts the signed consent form and theatre list. Choose the THREE most immediate and appropriate professional actions.",
        "options": [
            "Speak up immediately and assertively to halt the surgery before the skin incision is made",
            "Instigate an immediate repeat 'Time-Out' safety check with the entire theatre team to verify the correct surgical site against the consent form and imaging",
            "Log a clinical near-miss incident report (Datix) following the procedure to investigate how the incorrect marking occurred",
            "Stay silent because the consultant surgeon has 25 years of experience and knows best",
            "Wait until the surgeon makes the incision before mentioning the discrepancy",
            "Secretly scrub in and mark the other hip without telling anyone",
            "Blame the junior nurse loudly during the operation",
            "Leave the operating theatre quietly without saying anything"
        ],
        "correct_answer": [
            "Speak up immediately and assertively to halt the surgery before the skin incision is made",
            "Instigate an immediate repeat 'Time-Out' safety check with the entire theatre team to verify the correct surgical site against the consent form and imaging",
            "Log a clinical near-miss incident report (Datix) following the procedure to investigate how the incorrect marking occurred"
        ],
        "explanation": "Wrong-site surgery is a NHS 'Never Event'. Every team member has an absolute professional duty to speak up assertively to stop the procedure before harm occurs (human factors / WHO checklist). Repeating the Time-Out verifies records and consent. Incident reporting ensures systemic analysis of how mis-marking occurred. Silence, delayed warning, and abandoning the room risk catastrophic harm to the patient."
    }
]
