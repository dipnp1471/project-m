# -*- coding: utf-8 -*-
"""
Professional Dilemmas (4 Questions: 2 Ranking, 2 Selection)
Concise, high-yield GMC Good Medical Practice scenarios tailored for online publishing.
"""

ADDITIONAL_QUESTIONS = [
    # ==========================================
    # PROFESSIONAL DILEMMAS - RANKING (2 Questions)
    # ==========================================
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a GP. A mature 15-year-old girl asks for the contraceptive pill without telling her parents. She understands your advice, refuses to inform them, will continue having sex with her 16-year-old boyfriend regardless, and there are no safeguarding concerns.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Assess her against the Fraser guidelines, prescribe contraception confidentially, and encourage her gently to talk to her parents when ready.",
            "Explore her sexual health risks, offer STI screening, and document her Fraser competence clearly in the notes.",
            "Arrange a confidential follow-up appointment to review side effects and support.",
            "Refuse to prescribe contraception unless she brings a parent to her next appointment.",
            "Phone her mother after she leaves to inform her that her daughter is sexually active."
        ],
        "correct_answer": [
            "Assess her against the Fraser guidelines, prescribe contraception confidentially, and encourage her gently to talk to her parents when ready.",
            "Explore her sexual health risks, offer STI screening, and document her Fraser competence clearly in the notes.",
            "Arrange a confidential follow-up appointment to review side effects and support.",
            "Refuse to prescribe contraception unless she brings a parent to her next appointment.",
            "Phone her mother after she leaves to inform her that her daughter is sexually active."
        ],
        "explanation": "Under the Fraser guidelines (Gillick competence), a doctor may lawfully provide confidential contraception to an under-16 if she understands the advice, cannot be persuaded to tell her parents, is likely to continue having sex, her health would suffer without it, and it is in her best interests. Phoning her mother breaches confidentiality."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "Before an afternoon outpatient clinic, you smell alcohol on your registrar's breath and notice her speech is slightly slurred. When you speak to her privately, she insists she only had one glass at lunch and is fine to see patients.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Express your concern calmly in private, advise her not to see patients, and escalate immediately to the clinic consultant or clinical director.",
            "Ensure patients booked into her clinic are safely reviewed by other clinicians or appropriately rescheduled.",
            "Document your objective observations factually and confidentially.",
            "Allow her to run the clinic alone as long as she drinks black coffee first.",
            "Gossip about her drinking to the nursing staff in the clinic corridor."
        ],
        "correct_answer": [
            "Express your concern calmly in private, advise her not to see patients, and escalate immediately to the clinic consultant or clinical director.",
            "Ensure patients booked into her clinic are safely reviewed by other clinicians or appropriately rescheduled.",
            "Document your objective observations factually and confidentially.",
            "Allow her to run the clinic alone as long as she drinks black coffee first.",
            "Gossip about her drinking to the nursing staff in the clinic corridor."
        ],
        "explanation": "GMC Good Medical Practice requires doctors to act promptly if a colleague's health or performance puts patients at risk. Speak privately, escalate immediately to a senior clinician to protect patients, ensure safe clinic cover, and keep factual records rather than ignoring the risk or gossiping."
    },

    # ==========================================
    # PROFESSIONAL DILEMMAS - SELECTION (2 Questions)
    # ==========================================
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A 79-year-old man with terminal metastatic lung cancer and full capacity asks you about CPR if his heart stops. Before you answer, his daughter pulls you aside and demands you sign a DNACPR form without telling him.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Explain empathetically to the daughter that a capacitous patient must be involved in discussions about his own resuscitation status.",
            "Hold a sensitive, honest conversation with the patient about his prognosis, the realistic outcomes of CPR, and his wishes.",
            "Document the discussion, his preferences, and any DNACPR decision clearly in the notes and inform the consultant.",
            "Sign the DNACPR form secretly without telling the patient to spare his feelings.",
            "Allow the daughter to sign the DNACPR form on her father's behalf.",
            "Promise the patient that CPR will definitely restart his heart and cure him.",
            "Avoid discussing resuscitation altogether and leave it for the night on-call team.",
            "Order the daughter to leave the hospital immediately."
        ],
        "correct_answer": [
            "Explain empathetically to the daughter that a capacitous patient must be involved in discussions about his own resuscitation status.",
            "Hold a sensitive, honest conversation with the patient about his prognosis, the realistic outcomes of CPR, and his wishes.",
            "Document the discussion, his preferences, and any DNACPR decision clearly in the notes and inform the consultant."
        ],
        "explanation": "Following the Tracey judgement and GMC end-of-life guidance, clinicians have a legal and ethical duty to involve a capacitous patient when making a DNACPR decision—and relatives cannot override a capacitous patient's autonomy. Hold an empathetic, honest conversation with the patient and document it clearly."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "Three times this week, your acute medical ward has been left dangerously understaffed overnight, directly contributing to delayed sepsis antibiotics and an unwitnessed patient fall.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Submit clinical incident reports (Datix) documenting the unsafe staffing levels and resulting patient safety incidents.",
            "Escalate your concerns formally to the ward consultant, clinical director, and Freedom to Speak Up Guardian.",
            "Prioritise sickest patients safely on shift and escalate immediately to the night site manager whenever staffing becomes unsafe.",
            "Post details of the understaffed ward and patient fall publicly on social media to force change.",
            "Say nothing because understaffing is normal across the NHS.",
            "Walk off the ward mid-shift without handing over your patients.",
            "Falsify antibiotic administration times so the sepsis audit looks compliant.",
            "Tell relatives to sue the hospital trust."
        ],
        "correct_answer": [
            "Submit clinical incident reports (Datix) documenting the unsafe staffing levels and resulting patient safety incidents.",
            "Escalate your concerns formally to the ward consultant, clinical director, and Freedom to Speak Up Guardian.",
            "Prioritise sickest patients safely on shift and escalate immediately to the night site manager whenever staffing becomes unsafe."
        ],
        "explanation": "Under GMC *Raising and acting on concerns about patient safety* guidance, you have a duty to report unsafe staffing through proper governance channels (Datix, senior clinical leaders, Freedom to Speak Up Guardian) while maintaining immediate patient safety on shift—never falsifying records or breaching confidentiality online."
    }
]
