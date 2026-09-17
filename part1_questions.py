# -*- coding: utf-8 -*-
"""
Part 1: Cardiovascular, Dermatology / Ophthalmology / ENT, Endocrinology / Metabolic, Gastroenterology / Clinical Nutrition
4 clinical domains x 13 questions (8 SBA + 5 EMQ) = 52 questions.
"""

PART1_QUESTIONS = [
    # =========================================================================
    # 1. CARDIOVASCULAR (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 62-year-old man presents to the Emergency Department with severe central crushing chest pain radiating to his left arm and jaw for 45 minutes. His blood pressure is 138/84 mmHg, heart rate is 82 bpm, and oxygen saturation is 98% on room air. An immediate 12-lead ECG reveals 3 mm ST elevation in leads II, III, and aVF with reciprocal ST depression in leads I and aVL. The nearest primary PCI facility is 35 minutes away by ambulance. What is the most definitive immediate management?",
        "options": [
            "Primary Percutaneous Coronary Intervention (PCI)",
            "Intravenous thrombolysis with Tenecteplase",
            "Urgent Coronary Artery Bypass Grafting (CABG)",
            "Dual antiplatelet therapy with admission to CCU",
            "CT Coronary Angiogram"
        ],
        "correct_answer": "Primary Percutaneous Coronary Intervention (PCI)",
        "explanation": "This patient has an acute inferior ST-elevation myocardial infarction (STEMI). NICE guidelines recommend primary PCI as the preferred reperfusion strategy if it can be delivered within 120 minutes of the time when fibrinolysis could have been given. As the PCI centre is 35 minutes away, primary PCI is indicated."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 71-year-old woman with a history of ischaemic cardiomyopathy presents with acute shortness of breath and orthopnoea. On examination, she is tachypnoeic at 30 breaths/min, blood pressure is 172/98 mmHg, heart rate is 108 bpm regular, and oxygen saturation is 88% on room air. Auscultation reveals bilateral widespread fine inspiratory crackles and an audible S3 gallop. What is the most appropriate initial pharmacological treatment?",
        "options": [
            "Intravenous Furosemide",
            "Intravenous Digoxin",
            "Oral Bisoprolol",
            "Subcutaneous Enoxaparin",
            "Intravenous Amiodarone"
        ],
        "correct_answer": "Intravenous Furosemide",
        "explanation": "The patient has acute decompensated heart failure with acute pulmonary oedema. First-line medical therapy alongside high-flow oxygen (if hypoxic) is intravenous loop diuretics (e.g., Furosemide 40-80 mg IV bolus) to relieve venous congestion and pulmonary capillary hydrostatic pressure."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 45-year-old intravenous drug user presents with a 2-week history of remittent fever, night sweats, and weight loss. On examination, a new early diastolic murmur is heard along the left sternal border. Splinter haemorrhages are visible beneath the fingernails, and painless erythematous macules are present on the palms. Three sets of blood cultures are drawn. Which initial investigation is most appropriate to evaluate for vegetations?",
        "options": [
            "Transthoracic Echocardiogram (TTE)",
            "CT Pulmonary Angiogram",
            "Cardiac MRI",
            "12-lead Holter monitor",
            "Coronary Angiography"
        ],
        "correct_answer": "Transthoracic Echocardiogram (TTE)",
        "explanation": "The patient presents with classic signs of infective endocarditis (new murmur, fever, Janeway lesions, splinter haemorrhages). Transthoracic echocardiography (TTE) is the initial non-invasive investigation of choice. If TTE is negative or nondiagnostic and suspicion remains high, transoesophageal echocardiography (TOE) should follow."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 58-year-old man presents with sudden-onset severe tearing chest pain radiating straight through to his mid-scapular back. His blood pressure is 184/104 mmHg in the right arm and 142/86 mmHg in the left arm. A chest radiograph demonstrates widening of the superior mediastinum. A CT aortogram confirms a dissection flap involving the ascending aorta extending into the aortic arch. What is the definitive management?",
        "options": [
            "Emergency cardiothoracic surgical repair",
            "Intravenous labetalol infusion alone",
            "Percutaneous thoracic endovascular aortic repair (TEVAR)",
            "Therapeutic anticoagulation with Heparin",
            "Immediate thrombolysis"
        ],
        "correct_answer": "Emergency cardiothoracic surgical repair",
        "explanation": "A Stanford Type A aortic dissection involves the ascending aorta and represents a surgical emergency with a high early mortality rate due to potential aortic rupture, pericardial tamponade, or acute aortic regurgitation. Immediate open surgical repair is required."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 23-year-old man presents with recurrent episodes of rapid palpitations and presyncope. His baseline 12-lead ECG demonstrates a PR interval of 100 ms, a slurred upstroke of the QRS complex (delta wave), and a QRS duration of 130 ms. Which of the following medications is contraindicated if he develops atrial fibrillation with rapid ventricular conduction?",
        "options": [
            "Verapamil",
            "Procainamide",
            "Flecainide",
            "Ibutilide",
            "Amiodarone"
        ],
        "correct_answer": "Verapamil",
        "explanation": "The patient has Wolff-Parkinson-White (WPW) syndrome. In WPW with atrial fibrillation, AV nodal blocking drugs such as verapamil, diltiazem, beta-blockers, digoxin, and adenosine are contraindicated because blocking the AV node preferentially accelerates conduction down the accessory pathway, which can precipitate ventricular fibrillation."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 34-year-old woman presents with sharp pleuritic retrosternal chest pain that is noticeably relieved by sitting forward and worsened when lying flat. An ECG reveals widespread concave ST-segment elevation with PR-segment depression across leads I, II, aVL, and V2-V6. Cardiac troponin is mildly elevated. What is the first-line pharmacological treatment?",
        "options": [
            "High-dose Ibuprofen plus Colchicine",
            "Prednisolone plus Omeprazole",
            "Intravenous Heparin bolus",
            "Sublingual Glyceryl Trinitrate",
            "Oral Bisoprolol"
        ],
        "correct_answer": "High-dose Ibuprofen plus Colchicine",
        "explanation": "The clinical presentation and ECG findings are diagnostic of acute pericarditis (or myopericarditis). First-line treatment according to European Society of Cardiology (ESC) guidelines is high-dose NSAIDs (such as ibuprofen 600 mg TDS) combined with colchicine (500 mcg OD or BD) to speed remission and prevent recurrences."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 65-year-old man with hypertension presents with exertional chest tightness that reliably occurs after walking 200 metres on an incline and completely resolves within 3 minutes of rest. He has never experienced pain at rest. Examination is unremarkable. What is the recommended first-line anti-anginal medication according to NICE guidelines?",
        "options": [
            "Bisoprolol or Amlodipine",
            "Isosorbide mononitrate",
            "Nicorandil",
            "Ivabradine",
            "Ranolazine"
        ],
        "correct_answer": "Bisoprolol or Amlodipine",
        "explanation": "NICE clinical guideline CG95 recommends first-line medical therapy for stable angina consists of a short-acting nitrate for symptom relief plus monotherapy with either a beta-blocker (e.g., Bisoprolol) or a calcium-channel blocker (e.g., Amlodipine)."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 19-year-old amateur athlete collapses during a football match. His brother died suddenly at age 22 while playing basketball. On examination, a harsh ejection systolic murmur is audible at the left sternal border; the murmur increases markedly in intensity with the Valsalva manoeuvre and decreases during passive leg elevation. What is the underlying diagnosis?",
        "options": [
            "Hypertrophic Cardiomyopathy (HCM)",
            "Aortic Valve Stenosis",
            "Mitral Valve Prolapse",
            "Ventricular Septal Defect",
            "Atrial Septal Defect"
        ],
        "correct_answer": "Hypertrophic Cardiomyopathy (HCM)",
        "explanation": "Hypertrophic cardiomyopathy (HCM) causes dynamic left ventricular outflow tract (LVOT) obstruction. Maneuvers that reduce preload or left ventricular cavity size (such as the Valsalva strain or standing) exacerbate the obstruction and increase murmur intensity, whereas increasing preload (passive leg raising) softens the murmur."
    },
    # Cardiovascular EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Cardiovascular",
        "scenario": "Theme: Valvular Heart Disease. Match each clinical vignette with the most likely valvular lesion.\n\nVignette 1: A 78-year-old man presents with syncope on exertion. On examination, he has a slow-rising carotid pulse (pulsus parvus et tardus), a narrow pulse pressure, and a harsh ejection systolic murmur heard loudest in the right 2nd intercostal space that radiates to both carotids.",
        "options": [
            "Aortic Stenosis",
            "Mitral Regurgitation",
            "Aortic Regurgitation",
            "Mitral Stenosis",
            "Tricuspid Regurgitation",
            "Pulmonary Stenosis",
            "Mitral Valve Prolapse",
            "Ventricular Septal Defect"
        ],
        "correct_answer": "Aortic Stenosis",
        "explanation": "Exertional syncope, slow-rising pulse, and an ejection systolic murmur radiating to the carotids are pathognomonic for severe aortic stenosis."
    },
    {
        "type": "emq",
        "category": "Cardiovascular",
        "scenario": "Theme: Valvular Heart Disease. Match each clinical vignette with the most likely valvular lesion.\n\nVignette 2: A 64-year-old woman with a history of myocardial infarction presents with progressive orthopnoea. Examination reveals a displaced, hyperdynamic apex beat and a blowing pansystolic murmur loudest at the apex with radiation to the left axilla.",
        "options": [
            "Aortic Stenosis",
            "Mitral Regurgitation",
            "Aortic Regurgitation",
            "Mitral Stenosis",
            "Tricuspid Regurgitation",
            "Pulmonary Stenosis",
            "Mitral Valve Prolapse",
            "Ventricular Septal Defect"
        ],
        "correct_answer": "Mitral Regurgitation",
        "explanation": "A blowing pansystolic murmur loudest at the apex that radiates to the axilla indicates mitral regurgitation, often secondary to ischaemic papillary muscle dysfunction."
    },
    {
        "type": "emq",
        "category": "Cardiovascular",
        "scenario": "Theme: Valvular Heart Disease. Match each clinical vignette with the most likely valvular lesion.\n\nVignette 3: A 42-year-old man with Marfan syndrome presents with palpitations and dyspnoea. He has a collapsing 'water-hammer' pulse and a wide pulse pressure (160/54 mmHg). A high-pitched early diastolic decrescendo murmur is heard along the left lower sternal border with the patient sitting forward in full expiration.",
        "options": [
            "Aortic Stenosis",
            "Mitral Regurgitation",
            "Aortic Regurgitation",
            "Mitral Stenosis",
            "Tricuspid Regurgitation",
            "Pulmonary Stenosis",
            "Mitral Valve Prolapse",
            "Ventricular Septal Defect"
        ],
        "correct_answer": "Aortic Regurgitation",
        "explanation": "Collapsing pulse, wide pulse pressure, and an early diastolic decrescendo murmur accentuated by leaning forward in expiration are characteristic of aortic regurgitation."
    },
    {
        "type": "emq",
        "category": "Cardiovascular",
        "scenario": "Theme: Valvular Heart Disease. Match each clinical vignette with the most likely valvular lesion.\n\nVignette 4: A 38-year-old immigrant woman presents with hemoptysis and dyspnoea. She has a malar flush on her cheeks, an irregularly irregular pulse, a tapping apex beat, and a low-pitched mid-diastolic rumbling murmur preceded by an opening snap.",
        "options": [
            "Aortic Stenosis",
            "Mitral Regurgitation",
            "Aortic Regurgitation",
            "Mitral Stenosis",
            "Tricuspid Regurgitation",
            "Pulmonary Stenosis",
            "Mitral Valve Prolapse",
            "Ventricular Septal Defect"
        ],
        "correct_answer": "Mitral Stenosis",
        "explanation": "Malar flush, tapping apex beat, opening snap, and a mid-diastolic rumbling murmur are diagnostic of rheumatic mitral stenosis."
    },
    {
        "type": "emq",
        "category": "Cardiovascular",
        "scenario": "Theme: Valvular Heart Disease. Match each clinical vignette with the most likely valvular lesion.\n\nVignette 5: A 52-year-old man with chronic severe pulmonary hypertension secondary to COPD presents with peripheral oedema and ascites. On examination, there is a prominent 'cv' wave in the JVP, hepatomegaly with systolic pulsations, and a pansystolic murmur at the left lower sternal edge that intensifies on inspiration.",
        "options": [
            "Aortic Stenosis",
            "Mitral Regurgitation",
            "Aortic Regurgitation",
            "Mitral Stenosis",
            "Tricuspid Regurgitation",
            "Pulmonary Stenosis",
            "Mitral Valve Prolapse",
            "Ventricular Septal Defect"
        ],
        "correct_answer": "Tricuspid Regurgitation",
        "explanation": "A pansystolic murmur accentuated by inspiration (Carvallo's sign) along with pulsatile hepatomegaly and prominent JVP v waves indicates tricuspid regurgitation."
    },

    # =========================================================================
    # 2. DERMATOLOGY / OPHTHALMOLOGY / ENT (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 68-year-old hypermetropic woman presents to the ED with sudden excruciating right eye pain, headache, nausea, and vomiting. She reports seeing multi-coloured haloes around street lights. On examination, the right eye is red, the cornea is hazy and edematous, and the right pupil is mid-dilated, oval, and non-reactive to light. Palpation reveals a rock-hard globe. What is the immediate medical management?",
        "options": [
            "Intravenous Acetazolamide plus topical Pilocarpine and Timolol",
            "Topical Prednisolone acetate drops hourly",
            "Oral Aciclovir 800 mg five times daily",
            "Topical Chloramphenicol ointment and eye pad",
            "Subcutaneous Sumatriptan injection"
        ],
        "correct_answer": "Intravenous Acetazolamide plus topical Pilocarpine and Timolol",
        "explanation": "This patient has acute angle-closure glaucoma, an ophthalmic emergency. Immediate therapy aims to lower intraocular pressure using systemic carbonic anhydrase inhibitors (IV acetazolamide), topical miotics (pilocarpine 2% to constrict the pupil and reopen the angle), and topical beta-blockers (timolol), followed by urgent ophthalmology review for definitive peripheral iridotomy."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 74-year-old woman presents with a 4-day history of a throbbing right-sided headache, scalp tenderness when brushing her hair, and pain in her jaw muscles while chewing solid food. Blood tests reveal an erythrocyte sedimentation rate (ESR) of 98 mm/hr and C-reactive protein of 64 mg/L. What is the most important immediate step in management?",
        "options": [
            "Commence high-dose oral Prednisolone immediately",
            "Wait for urgent temporal artery biopsy results before treatment",
            "Perform urgent non-contrast CT head",
            "Prescribe oral Sumatriptan and analgesia",
            "Arrange outpatient rheumatology review within 2 weeks"
        ],
        "correct_answer": "Commence high-dose oral Prednisolone immediately",
        "explanation": "The clinical picture of jaw claudication, temporal headache, scalp tenderness, and markedly elevated inflammatory markers strongly indicates giant cell arteritis (temporal arteritis). Treatment with high-dose corticosteroids (Prednisolone 40-60 mg daily) must be started immediately to prevent irreversible bilateral anterior ischemic optic neuropathy and permanent blindness."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 44-year-old man wakes up with complete hearing loss in his right ear accompanied by mild tinnitus. There is no discharge, vertigo, or trauma. Otoscopy is completely normal. On tuning fork testing, the Weber test lateralises to the left ear, and the Rinne test is positive bilaterally (air conduction > bone conduction). What is the recommended management?",
        "options": [
            "Urgent same-day ENT referral and high-dose oral corticosteroids",
            "Prescribe topical Amoxicillin-Clavulanate ear drops",
            "Reassure and advise ear syringing in primary care",
            "Prescribe oral Betahistine for 2 weeks",
            "Order routine non-urgent audiometry within 6 weeks"
        ],
        "correct_answer": "Urgent same-day ENT referral and high-dose oral corticosteroids",
        "explanation": "The patient has sudden sensorineural hearing loss (SSNHL), defined as sensorineural hearing loss of >=30 dB over at least 3 contiguous frequencies within 72 hours. Tuning fork findings confirm right sensorineural loss. SSNHL requires urgent ENT assessment and early initiation of high-dose systemic corticosteroids (prednisolone) within 24-72 hours to maximise the likelihood of hearing recovery."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 21-year-old man presents with severe left-sided sore throat, difficulty swallowing his own saliva, and severe difficulty opening his mouth (trismus). He has a muffled 'hot potato' voice. Examination reveals a markedly swollen left peritonsillar area with deviation of the uvula to the right side. What is the definitive initial intervention?",
        "options": [
            "Needle aspiration or incision and drainage of the abscess plus IV antibiotics",
            "Oral Phenoxymethylpenicillin (Penicillin V) 500 mg QDS",
            "Emergency tracheostomy",
            "Nebulised budesonide and discharge home",
            "Immediate tonsillectomy"
        ],
        "correct_answer": "Needle aspiration or incision and drainage of the abscess plus IV antibiotics",
        "explanation": "The patient has a peritonsillar abscess (Quinsy), characterized by trismus, uvular deviation, and a hot-potato voice. Definitive emergency management requires needle aspiration or incision and drainage under local anaesthesia along with intravenous broad-spectrum antibiotics and analgesia."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 29-year-old woman commenced Lamotrigine for bipolar disorder 3 weeks ago. She presents with fever, malaise, sore throat, and a widespread painful erythematous rash. On examination, there are purpuric macules with central dusky necrosis and flaccid bullae covering approximately 25% of her body surface area. There is painful mucosal sloughing involving the oral cavity and conjunctiva. Nikolsky's sign is positive. What is the diagnosis?",
        "options": [
            "Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis overlap",
            "Staphylococcal Scalded Skin Syndrome",
            "Erythema Multiforme Minor",
            "Bullous Pemphigoid",
            "Generalized Pustular Psoriasis"
        ],
        "correct_answer": "Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis overlap",
        "explanation": "Stevens-Johnson Syndrome (SJS) and Toxic Epidermal Necrolysis (TEN) represent a spectrum of severe adverse cutaneous drug reactions characterized by extensive epidermal detachment and mucosal involvement. SJS involves <10% BSA, SJS/TEN overlap involves 10-30% BSA, and TEN involves >30% BSA. Lamotrigine is a classic culprit medication."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 72-year-old diabetic man presents with deep, severe, unremitting right ear pain that is worse at night. Examination reveals purulent discharge, swelling of the external auditory canal, and granulation tissue at the bone-cartilage junction of the ear canal floor. The tympanic membrane cannot be visualized. What is the underlying condition and its most common causative pathogen?",
        "options": [
            "Malignant (necrotising) otitis externa caused by Pseudomonas aeruginosa",
            "Acute otitis media caused by Streptococcus pneumoniae",
            "Fungal otitis externa caused by Candida albicans",
            "Cholesteatoma caused by anaerobes",
            "Herpes zoster oticus caused by Varicella-zoster virus"
        ],
        "correct_answer": "Malignant (necrotising) otitis externa caused by Pseudomonas aeruginosa",
        "explanation": "Malignant otitis externa is a life-threatening osteomyelitis of the temporal bone and skull base that primarily affects elderly diabetic or immunocompromised individuals. Granulation tissue at the external meatal junction is pathognomonic, and Pseudomonas aeruginosa is the causative organism in >90% of cases. Urgent CT temporal bones and prolonged systemic anti-pseudomonal therapy (e.g., Ciprofloxacin) are required."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 26-year-old university student presents with an intensely pruritic eruption, especially severe at night in bed. Her flatmate has similar symptoms. On examination, there are erythematous papules, excoriations, and linear serpiginous burrows in the finger web spaces, wrists, and axillary folds. What is the recommended treatment regimen?",
        "options": [
            "Permethrin 5% dermal cream applied from neck down, washed off after 8-12 hours, repeated after 7 days; treat all household contacts",
            "Hydrocortisone 1% cream applied twice daily for 2 weeks to affected areas only",
            "Single dose of oral Fluconazole 150 mg",
            "Oral Co-amoxiclav for 7 days",
            "Topical Clotrimazole 1% cream applied for 4 weeks"
        ],
        "correct_answer": "Permethrin 5% dermal cream applied from neck down, washed off after 8-12 hours, repeated after 7 days; treat all household contacts",
        "explanation": "This is scabies (caused by Sarcoptes scabiei). First-line treatment is topical 5% Permethrin dermal cream applied over the whole body from neck down (including scalp/face in infants/elderly), left on for 8-12 hours, and repeated in 7 days to kill newly hatched mites. Crucially, all household contacts and sexual partners must be treated simultaneously."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 66-year-old man presents with sudden, painless, profound visual loss in his left eye upon waking. Visual acuity is reduced to counting fingers in the left eye. Pupillary examination demonstrates a relative afferent pupillary defect in the left eye. Dilated fundoscopy reveals a pale, edematous retina with a prominent 'cherry-red spot' at the fovea. What is the diagnosis?",
        "options": [
            "Central Retinal Artery Occlusion (CRAO)",
            "Central Retinal Vein Occlusion (CRVO)",
            "Rhegmatogenous Retinal Detachment",
            "Vitreous Haemorrhage",
            "Acute Anterior Uveitis"
        ],
        "correct_answer": "Central Retinal Artery Occlusion (CRAO)",
        "explanation": "Sudden, painless loss of vision with a pale retina and a distinctive 'cherry-red spot' at the macula is pathognomonic for Central Retinal Artery Occlusion (CRAO), usually caused by thromboembolism from carotid artery atheroma or cardiac sources."
    },
    # Derm/Eye/ENT EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "Theme: Differential Diagnosis of the Red Eye. Match each scenario with the most likely diagnosis.\n\nVignette 1: A 28-year-old man with ankylosing spondylitis presents with a 2-day history of painful red left eye, severe photophobia, blurred vision, and ciliary injection around the limbus. The pupil is small and irregular. Slit-lamp shows inflammatory cells in the anterior chamber.",
        "options": [
            "Anterior Uveitis (Iritis)",
            "Bacterial Conjunctivitis",
            "Episcleritis",
            "Scleritis",
            "Herpes Simplex Keratitis",
            "Subconjunctival Haemorrhage",
            "Acute Angle-Closure Glaucoma",
            "Corneal Foreign Body"
        ],
        "correct_answer": "Anterior Uveitis (Iritis)",
        "explanation": "Ciliary injection, severe photophobia, a small irregular pupil, and anterior chamber cells in a patient with HLA-B27 spondyloarthropathy confirm acute anterior uveitis."
    },
    {
        "type": "emq",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "Theme: Differential Diagnosis of the Red Eye. Match each scenario with the most likely diagnosis.\n\nVignette 2: A 22-year-old childcare assistant presents with bilateral red, gritty eyes with copious thick yellowish-green discharge. Her eyelids are stuck together every morning. Visual acuity, pupil reflexes, and cornea are completely normal.",
        "options": [
            "Anterior Uveitis (Iritis)",
            "Bacterial Conjunctivitis",
            "Episcleritis",
            "Scleritis",
            "Herpes Simplex Keratitis",
            "Subconjunctival Haemorrhage",
            "Acute Angle-Closure Glaucoma",
            "Corneal Foreign Body"
        ],
        "correct_answer": "Bacterial Conjunctivitis",
        "explanation": "Purulent discharge, morning eyelid sticking, normal visual acuity, and lack of photophobia characterize acute bacterial conjunctivitis."
    },
    {
        "type": "emq",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "Theme: Differential Diagnosis of the Red Eye. Match each scenario with the most likely diagnosis.\n\nVignette 3: A 36-year-old woman presents with localized segmental redness in her right eye. She has mild gritty discomfort but no true eye pain, photophobia, or visual disturbance. Instillation of phenylephrine 2.5% drops produces prompt blanching of the engorged blood vessels.",
        "options": [
            "Anterior Uveitis (Iritis)",
            "Bacterial Conjunctivitis",
            "Episcleritis",
            "Scleritis",
            "Herpes Simplex Keratitis",
            "Subconjunctival Haemorrhage",
            "Acute Angle-Closure Glaucoma",
            "Corneal Foreign Body"
        ],
        "correct_answer": "Episcleritis",
        "explanation": "Episcleritis is a benign self-limiting inflammation of the episclera presenting with localized redness; the superficial vessels blanch when phenylephrine drops are applied."
    },
    {
        "type": "emq",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "Theme: Differential Diagnosis of the Red Eye. Match each scenario with the most likely diagnosis.\n\nVignette 4: A 52-year-old woman with severe rheumatoid arthritis presents with a deep, boring, excruciating left eye ache that awakens her from sleep and radiates to the temple. The eye has a violaceous, deep red hue. Instillation of phenylephrine drops does not blanch the scleral vessels.",
        "options": [
            "Anterior Uveitis (Iritis)",
            "Bacterial Conjunctivitis",
            "Episcleritis",
            "Scleritis",
            "Herpes Simplex Keratitis",
            "Subconjunctival Haemorrhage",
            "Acute Angle-Closure Glaucoma",
            "Corneal Foreign Body"
        ],
        "correct_answer": "Scleritis",
        "explanation": "Scleritis is a destructive, painful ocular condition strongly linked with systemic autoimmune disorders like rheumatoid arthritis. Deep vessels do not blanch with phenylephrine."
    },
    {
        "type": "emq",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "Theme: Differential Diagnosis of the Red Eye. Match each scenario with the most likely diagnosis.\n\nVignette 5: A 40-year-old man presents with foreign body sensation, pain, and photophobia in his left eye. Fluorescein staining reveals a branching, dendritic corneal epithelial ulcer. Topical corticosteroids must be strictly avoided.",
        "options": [
            "Anterior Uveitis (Iritis)",
            "Bacterial Conjunctivitis",
            "Episcleritis",
            "Scleritis",
            "Herpes Simplex Keratitis",
            "Subconjunctival Haemorrhage",
            "Acute Angle-Closure Glaucoma",
            "Corneal Foreign Body"
        ],
        "correct_answer": "Herpes Simplex Keratitis",
        "explanation": "A dendritic ulcer on fluorescein staining is diagnostic of epithelial herpes simplex keratitis. Topical aciclovir is first-line; topical steroids are contraindicated as they cause corneal perforation."
    },

    # =========================================================================
    # 3. ENDOCRINOLOGY / METABOLIC (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 21-year-old man with Type 1 Diabetes is brought to the ED with nausea, vomiting, and abdominal pain. Examination shows Kussmaul respiration with a fruity breath odour. Bloods reveal: venous pH 7.18 (7.35-7.45), bicarbonate 11 mmol/L (22-29), blood ketones 4.8 mmol/L (<0.6), blood glucose 24.2 mmol/L, potassium 4.8 mmol/L (3.5-5.0). Resuscitation with 0.9% sodium chloride and fixed-rate intravenous insulin infusion is started. What is the recommended strategy regarding intravenous potassium replacement?",
        "options": [
            "Add 40 mmol KCl per litre of IV fluid starting with the second fluid bag",
            "Withhold all potassium supplementation until serum potassium drops below 3.5 mmol/L",
            "Administer an immediate IV bolus of 20 mmol KCl over 10 minutes",
            "Give oral potassium chloride effervescent tablets only",
            "Withhold insulin until potassium exceeds 5.5 mmol/L"
        ],
        "correct_answer": "Add 40 mmol KCl per litre of IV fluid starting with the second fluid bag",
        "explanation": "In Diabetic Ketoacidosis (DKA), total body potassium is depleted despite normal or elevated initial serum levels. Joint British Diabetes Societies (JBDS) guidelines recommend adding 40 mmol KCl per litre of fluid if potassium is between 3.5 and 5.5 mmol/L to prevent precipitous hypokalemia once insulin drives potassium back into cells."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 78-year-old man with Type 2 Diabetes is admitted with progressive confusion and lethargy over 10 days. Vitals: BP 94/58 mmHg, HR 112 bpm, capillary refill 4 seconds. Investigations show: blood glucose 48 mmol/L, serum sodium 152 mmol/L, serum potassium 4.2 mmol/L, serum osmolality 360 mOsm/kg (>320), venous blood gas pH 7.37, blood ketones 0.4 mmol/L. What is the primary cornerstone of acute initial management?",
        "options": [
            "Gradual fluid replacement with 0.9% Sodium Chloride alongside prophylactic LMWH",
            "Immediate bolus of high-dose intravenous Actrapid insulin",
            "Rapid administration of 5% Dextrose infusion",
            "Immediate intravenous broad-spectrum Sodium Bicarbonate",
            "Intravenous loop diuretics to lower serum osmolality"
        ],
        "correct_answer": "Gradual fluid replacement with 0.9% Sodium Chloride alongside prophylactic LMWH",
        "explanation": "This patient has Hyperosmolar Hyperglycaemic State (HHS), characterized by marked hyperosmolality (>320), extreme hyperglycemia (>30 mmol/L), and severe dehydration without significant ketoacidosis. The cornerstone of treatment is gradual fluid resuscitation with 0.9% saline (aiming to reduce osmolality by 3-8 mOsm/kg/h to avoid cerebral edema) and prophylactic anticoagulation due to high thromboembolic risk."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 46-year-old woman is investigated for persistent hypertension (168/102 mmHg) refractory to three antihypertensive agents. Routine blood tests reveal a persistent serum potassium of 3.0 mmol/L (3.5-5.0) and serum sodium of 144 mmol/L. She takes no diuretics. Plasma aldosterone concentration is markedly elevated, and plasma renin activity is undetectable. What is the most appropriate first-line medical therapy if surgery is declined or delayed?",
        "options": [
            "Spironolactone",
            "Amlodipine",
            "Ramipril",
            "Furosemide",
            "Bisoprolol"
        ],
        "correct_answer": "Spironolactone",
        "explanation": "The biochemical picture of hypertension with unprovoked hypokalemia, high aldosterone, and suppressed renin indicates primary hyperaldosteronism (Conn's syndrome). Mineralocorticoid receptor antagonists (MRAs) such as spironolactone (or eplerenone) are the medical treatment of choice by competitively antagonizing aldosterone action at the distal nephron."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 38-year-old woman with known autoimmune Addison's disease develops acute gastroenteritis and presents to the ED collapsed. Blood pressure is 78/46 mmHg, heart rate is 120 bpm, and blood glucose is 3.1 mmol/L. Bloods show Na 126 mmol/L and K 6.1 mmol/L. What is the single most urgent therapeutic intervention?",
        "options": [
            "Intravenous Hydrocortisone 100 mg stat plus aggressive 0.9% Sodium Chloride resuscitation",
            "Oral Fludrocortisone 200 mcg stat",
            "Intravenous Dextrose 50% bolus alone",
            "Intravenous Calcium Gluconate 10% bolus",
            "Intramuscular Adrenaline 500 mcg"
        ],
        "correct_answer": "Intravenous Hydrocortisone 100 mg stat plus aggressive 0.9% Sodium Chloride resuscitation",
        "explanation": "This patient is in life-threatening Addisonian (adrenal) crisis, marked by hypotension, shock, hyponatremia, hyperkalemia, and hypoglycemia. Immediate management requires intravenous hydrocortisone 100 mg stat (continued 100 mg 6-8 hourly) and rapid IV volume resuscitation with 0.9% sodium chloride and dextrose."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 50-year-old man presents with progressive coarsening of facial features, enlargement of hands and feet requiring larger shoe and ring sizes, excessive sweating, and mandibular prognathism with teeth spacing. He also has new carpal tunnel syndrome. What is the most appropriate initial biochemical screening test for suspected acromegaly?",
        "options": [
            "Serum Insulin-like Growth Factor-1 (IGF-1)",
            "Random serum Growth Hormone (GH)",
            "Oral Glucose Tolerance Test with GH suppression",
            "24-hour urinary free cortisol",
            "Serum Prolactin"
        ],
        "correct_answer": "Serum Insulin-like Growth Factor-1 (IGF-1)",
        "explanation": "Serum IGF-1 has a stable circulating concentration and is the first-line screening investigation of choice for acromegaly. Random growth hormone (GH) levels fluctuate widely due to pulsatile secretion and are unreliable. If IGF-1 is elevated, an Oral Glucose Tolerance Test (OGTT) with GH measurement is used for definitive confirmation (failure of GH to suppress <1 mcg/L)."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 33-year-old woman presents with severe anterior neck pain radiating to her ears and jaw 3 weeks after recovering from an upper respiratory tract infection. On examination, the thyroid gland is exquisitely tender and firm. Bloods show: TSH <0.02 mU/L, free T4 32 pmol/L (12-22), ESR 85 mm/hr. A technetium-99m thyroid uptake scan shows globally reduced tracer uptake (<1%). What is the diagnosis?",
        "options": [
            "Subacute granulomatous (de Quervain's) thyroiditis",
            "Graves' disease",
            "Toxic multinodular goitre",
            "Hashimoto's thyroiditis",
            "Thyroid abscess (acute suppurative thyroiditis)"
        ],
        "correct_answer": "Subacute granulomatous (de Quervain's) thyroiditis",
        "explanation": "Painful tender goitre following a viral illness with thyrotoxic biochemical features, markedly elevated ESR, and characteristically absent/reduced tracer uptake on radionuclide scan is classic for subacute granulomatous (de Quervain's) thyroiditis. Treatment is supportive with NSAIDs or corticosteroids."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 58-year-old woman presents with fatigue, recurrent kidney stones, constipation, and mild depression. Blood tests show: adjusted serum calcium 2.82 mmol/L (2.20-2.60), serum phosphate 0.71 mmol/L (0.8-1.5), and serum parathyroid hormone (PTH) 9.8 pmol/L (1.6-6.9, inappropriately elevated). Renal function is normal. What is the most likely diagnosis?",
        "options": [
            "Primary hyperparathyroidism",
            "Secondary hyperparathyroidism",
            "Familial hypocalciuric hypercalcaemia",
            "Tertiary hyperparathyroidism",
            "Hypercalcaemia of malignancy"
        ],
        "correct_answer": "Primary hyperparathyroidism",
        "explanation": "Hypercalcemia in the presence of an elevated (or inappropriately non-suppressed) PTH and low-normal phosphate is diagnostic of primary hyperparathyroidism, most commonly caused by a solitary benign parathyroid adenoma (85%). Parathyroidectomy is the definitive curative treatment."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 39-year-old woman presents with central weight gain, facial rounding (moon face), proximal muscle weakness, and purple abdominal striae measuring >1 cm in width. Her blood pressure is 156/94 mmHg and HbA1c is 58 mmol/mol. What is the recommended initial first-line screening investigation for suspected Cushing's syndrome?",
        "options": [
            "Overnight low-dose (1 mg) Dexamethasone Suppression Test",
            "Random morning serum cortisol",
            "High-dose (8 mg) Dexamethasone Suppression Test",
            "Adrenal CT scan",
            "Pituitary MRI scan"
        ],
        "correct_answer": "Overnight low-dose (1 mg) Dexamethasone Suppression Test",
        "explanation": "First-line screening tests for Cushing's syndrome include the overnight 1 mg dexamethasone suppression test (ODST), 24-hour urinary free cortisol (UFC), or late-night salivary cortisol. Normal individuals suppress serum cortisol to <50 nmol/L following 1 mg dexamethasone; failure to suppress confirms hypercortisolemia. Imaging and high-dose suppression tests are second-line localization studies."
    },
    # Endocrinology EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Endocrinology / Metabolic",
        "scenario": "Theme: Thyroid Pathology and Investigations. Match each clinical vignette with the most likely diagnosis.\n\nVignette 1: A 32-year-old woman presents with weight loss, heat intolerance, bilateral proptosis, pretibial myxoedema, and a smooth diffuse goitre with an audible bruit. TSH-receptor antibodies (TRAb) are strongly positive.",
        "options": [
            "Graves' Disease",
            "Toxic Multinodular Goitre",
            "Hashimoto's Thyroiditis",
            "Sick Euthyroid Syndrome",
            "Postpartum Thyroiditis",
            "Thyroid Follicular Adenoma",
            "Riedel's Thyroiditis",
            "Anaplastic Thyroid Carcinoma"
        ],
        "correct_answer": "Graves' Disease",
        "explanation": "Diffuse goitre with bruit, proptosis (thyroid eye disease), pretibial myxedema, and positive TRAb antibodies are definitive for Graves' disease."
    },
    {
        "type": "emq",
        "category": "Endocrinology / Metabolic",
        "scenario": "Theme: Thyroid Pathology and Investigations. Match each clinical vignette with the most likely diagnosis.\n\nVignette 2: A 72-year-old woman presents with palpitations, weight loss, and atrial fibrillation. Examination shows an irregular, nodular enlarged thyroid without eye signs. Scintigraphy demonstrates multiple focal areas of patchy increased tracer uptake with suppression of surrounding tissue.",
        "options": [
            "Graves' Disease",
            "Toxic Multinodular Goitre",
            "Hashimoto's Thyroiditis",
            "Sick Euthyroid Syndrome",
            "Postpartum Thyroiditis",
            "Thyroid Follicular Adenoma",
            "Riedel's Thyroiditis",
            "Anaplastic Thyroid Carcinoma"
        ],
        "correct_answer": "Toxic Multinodular Goitre",
        "explanation": "Irregular nodular goitre in an elderly patient with patchy hyperfunctioning 'hot' nodules on radioiodine scan represents toxic multinodular goitre (Plummer's disease)."
    },
    {
        "type": "emq",
        "category": "Endocrinology / Metabolic",
        "scenario": "Theme: Thyroid Pathology and Investigations. Match each clinical vignette with the most likely diagnosis.\n\nVignette 3: A 46-year-old woman presents with cold intolerance, weight gain, constipation, and dry skin. On examination, she has a firm, non-tender, rubbery goitre. Bloods show high TSH, low free T4, and strongly elevated anti-thyroid peroxidase (anti-TPO) antibodies.",
        "options": [
            "Graves' Disease",
            "Toxic Multinodular Goitre",
            "Hashimoto's Thyroiditis",
            "Sick Euthyroid Syndrome",
            "Postpartum Thyroiditis",
            "Thyroid Follicular Adenoma",
            "Riedel's Thyroiditis",
            "Anaplastic Thyroid Carcinoma"
        ],
        "correct_answer": "Hashimoto's Thyroiditis",
        "explanation": "Goitrous primary hypothyroidism with high anti-TPO antibodies is the hallmark of Hashimoto's autoimmune thyroiditis."
    },
    {
        "type": "emq",
        "category": "Endocrinology / Metabolic",
        "scenario": "Theme: Thyroid Pathology and Investigations. Match each clinical vignette with the most likely diagnosis.\n\nVignette 4: A 65-year-old man admitted to the intensive care unit with severe septic shock from bacterial pneumonia is found on routine blood tests to have a markedly low total T3, low-normal free T4, and a normal TSH. He has no prior history of thyroid disease.",
        "options": [
            "Graves' Disease",
            "Toxic Multinodular Goitre",
            "Hashimoto's Thyroiditis",
            "Sick Euthyroid Syndrome",
            "Postpartum Thyroiditis",
            "Thyroid Follicular Adenoma",
            "Riedel's Thyroiditis",
            "Anaplastic Thyroid Carcinoma"
        ],
        "correct_answer": "Sick Euthyroid Syndrome",
        "explanation": "Sick euthyroid syndrome (non-thyroidal illness syndrome) occurs during critical non-thyroidal systemic illness; low T3 with normal or low TSH and normal T4 is typical. No thyroid hormone therapy is indicated."
    },
    {
        "type": "emq",
        "category": "Endocrinology / Metabolic",
        "scenario": "Theme: Thyroid Pathology and Investigations. Match each clinical vignette with the most likely diagnosis.\n\nVignette 5: A 31-year-old woman presents with palpitations, mild tremor, and anxiety 3 months after delivering her first baby. Blood tests show suppressed TSH and elevated free T4, with weakly positive anti-TPO antibodies. A technetium scan shows very low tracer uptake throughout the thyroid gland.",
        "options": [
            "Graves' Disease",
            "Toxic Multinodular Goitre",
            "Hashimoto's Thyroiditis",
            "Sick Euthyroid Syndrome",
            "Postpartum Thyroiditis",
            "Thyroid Follicular Adenoma",
            "Riedel's Thyroiditis",
            "Anaplastic Thyroid Carcinoma"
        ],
        "correct_answer": "Postpartum Thyroiditis",
        "explanation": "Postpartum thyroiditis typically occurs within 12 months of delivery, exhibiting an initial transient thyrotoxic phase (with low scintigraphy uptake due to release of preformed hormone) often followed by a hypothyroid phase."
    },

    # =========================================================================
    # 4. GASTROENTEROLOGY / CLINICAL NUTRITION (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 54-year-old man with known decompensated alcohol-related liver cirrhosis is brought to the ED with a large volume of haematemesis and melaena. He is pale and clammy. Blood pressure is 86/52 mmHg and heart rate is 124 bpm. Resuscitation with blood products is initiated. In addition to urgent upper GI endoscopy within 24 hours, what is the most appropriate immediate medical management?",
        "options": [
            "Intravenous Terlipressin plus prophylactic IV Ceftriaxone",
            "High-dose oral Omeprazole suspension",
            "Intravenous Tranexamic acid bolus alone",
            "Subcutaneous Octreotide with oral Metronidazole",
            "Placement of a Sengstaken-Blakemore tube immediately"
        ],
        "correct_answer": "Intravenous Terlipressin plus prophylactic IV Ceftriaxone",
        "explanation": "In suspected acute variceal bleeding, NICE guidelines recommend immediate administration of intravenous terlipressin (a splanchnic vasoconstrictor) and prophylactic intravenous broad-spectrum antibiotics (such as ceftriaxone) prior to urgent endoscopy. Balloon tamponade (Sengstaken tube) is reserved for uncontrolled catastrophic bleeding."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 24-year-old woman with known Ulcerative Colitis presents with an acute flare. She reports opening her bowels 8 times a day with visible blood and nocturnal diarrhoea. On examination, temperature is 38.2°C, heart rate is 104 bpm, and ESR is 48 mm/hr. Abdominal X-ray shows no colonic dilatation. According to the Truelove and Witts criteria, how is this flare classified and what is the first-line treatment?",
        "options": [
            "Acute severe flare; treat with intravenous Hydrocortisone",
            "Moderate flare; treat with oral Prednisolone 40 mg",
            "Mild flare; treat with topical 5-ASA enemas",
            "Acute severe flare; proceed directly to emergency subtotal colectomy",
            "Moderate flare; initiate Infliximab monotherapy"
        ],
        "correct_answer": "Acute severe flare; treat with intravenous Hydrocortisone",
        "explanation": "According to Truelove and Witts criteria, >=6 bloody stools per day plus at least one sign of systemic toxicity (pyrexia >37.8°C, tachycardia >90 bpm, anaemia, or ESR >30) defines acute severe ulcerative colitis. This is a medical emergency requiring hospital admission, venous thromboembolism prophylaxis, and intravenous corticosteroids (e.g., Hydrocortisone 100 mg QDS)."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 58-year-old man with cirrhosis and ascites presents with low-grade fever, mild abdominal pain, and new-onset confusion (hepatic encephalopathy). A diagnostic paracentesis yields cloudy ascitic fluid. Ascitic fluid analysis reveals an absolute neutrophil count of 420 cells/mm3 (reference <250). What is the first-line empirical antibiotic therapy?",
        "options": [
            "Intravenous Cefotaxime or Ceftriaxone",
            "Oral Ciprofloxacin",
            "Intravenous Vancomycin",
            "Oral Metronidazole",
            "Intravenous Gentamicin"
        ],
        "correct_answer": "Intravenous Cefotaxime or Ceftriaxone",
        "explanation": "An ascitic neutrophil count >=250 cells/mm3 is diagnostic of Spontaneous Bacterial Peritonitis (SBP). Intravenous third-generation cephalosporins (e.g., Cefotaxime or Ceftriaxone) are the empirical treatment of choice. Intravenous 20% human albumin solution is also co-administered on days 1 and 3 to reduce the incidence of hepatorenal syndrome and mortality."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 28-year-old woman presents with persistent abdominal bloating, loose stools, and unexplained iron deficiency anaemia. Her sister has autoimmune thyroiditis. She has been eating a normal gluten-containing diet. What is the recommended first-line serological screening test for coeliac disease according to NICE guidelines?",
        "options": [
            "IgA tissue transglutaminase (tTG-IgA) antibody plus total IgA level",
            "IgG antigliadin antibody alone",
            "Faecal calprotectin",
            "Endomysial IgA antibody alone",
            "HLA-DQ2 and HLA-DQ8 genotyping"
        ],
        "correct_answer": "IgA tissue transglutaminase (tTG-IgA) antibody plus total IgA level",
        "explanation": "NICE guideline NG20 specifies that the first-line diagnostic investigation for coeliac disease is IgA tissue transglutaminase (tTG-IgA) tested alongside total serum IgA (to exclude selective IgA deficiency, which would cause a false-negative tTG-IgA). If total IgA is deficient, IgG tTG or IgG endomysial antibodies are measured."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 48-year-old woman presents with severe fatigue and unremitting generalised pruritus without a rash. Examination reveals excoriation marks and xanthelasma around her eyes. Blood tests show: bilirubin 18 micromol/L (normal), ALP 420 U/L (30-130), ALT 45 U/L (10-40). Serum Anti-Mitochondrial Antibodies (AMA) are strongly positive (titre >1:160). What is the first-line medical therapy?",
        "options": [
            "Ursodeoxycholic acid (UDCA)",
            "Prednisolone",
            "Azathioprine",
            "Methotrexate",
            "Penicillamine"
        ],
        "correct_answer": "Ursodeoxycholic acid (UDCA)",
        "explanation": "The presentation of pruritus, cholestatic liver enzyme elevation, and positive anti-mitochondrial antibodies (AMA) in a middle-aged woman is classic for Primary Biliary Cholangitis (PBC). Ursodeoxycholic acid (UDCA) improves bile flow, delays histological progression, and prolongs transplant-free survival."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 22-year-old man presents with progressive resting and action tremors, dysarthria, and emotional lability. Examination reveals bilateral copper-coloured rings at the limbus of the cornea (Kayser-Fleischer rings). Liver function tests show chronic transaminitis. Serum caeruloplasmin is markedly reduced and 24-hour urinary copper excretion is elevated. What is the initial pharmacological treatment of choice?",
        "options": [
            "Penicillamine (or Trientine)",
            "Desferrioxamine",
            "N-acetylcysteine",
            "Prednisolone",
            "Levodopa/Carbidopa"
        ],
        "correct_answer": "Penicillamine (or Trientine)",
        "explanation": "Wilson's disease (hepatolenticular degeneration) is an autosomal recessive disorder of copper metabolism resulting in pathological copper accumulation in liver, basal ganglia, and cornea. Copper-chelating agents such as D-penicillamine or trientine are the first-line medical therapies to promote urinary copper excretion."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 46-year-old man is admitted with severe epigastric pain radiating to his back, accompanied by vomiting, following a weekend of heavy alcohol intake. Serum amylase is 1450 U/L. Which clinical scoring system is routinely used within the first 48 hours of admission in the UK to predict the severity and prognosis of acute pancreatitis?",
        "options": [
            "Modified Glasgow criteria (PANCREAS score)",
            "Child-Pugh classification",
            "Rockall scoring system",
            "Maddrey's Discriminant Function",
            "Alvarado score"
        ],
        "correct_answer": "Modified Glasgow criteria (PANCREAS score)",
        "explanation": "The modified Glasgow criteria (mnemonic PANCREAS: PaO2, Age, Neutrophils/WBC, Calcium, Renal/Urea, Enzymes/LDH, Albumin, Sugar/Glucose) assesses the severity of acute pancreatitis within 48 hours of onset. A score of >=3 indicates severe acute pancreatitis and warrants HDU/ICU consideration."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 19-year-old woman with chronic anorexia nervosa (BMI 12.8 kg/m2) is admitted for nutritional rehabilitation. She has eaten virtually no food for 3 weeks. What is the most critical biochemical electrolyte abnormality to monitor and proactively replace to prevent life-threatening complications of refeeding syndrome?",
        "options": [
            "Phosphate",
            "Sodium",
            "Chloride",
            "Bicarbonate",
            "Iron"
        ],
        "correct_answer": "Phosphate",
        "explanation": "In refeeding syndrome, carbohydrate reintroduction stimulates an insulin surge, which drives cellular uptake of glucose, potassium, magnesium, and crucially phosphate for ATP synthesis. Severe hypophosphataemia causes fatal cardiac arrhythmias, respiratory failure, acute heart failure, rhabdomyolysis, and red cell dysfunction. Electrolytes must be checked and replaced prior to and during gradual nutritional reintroduction."
    },
    # Gastroenterology EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "Theme: Chronic Diarrhoea and Malabsorption. Match each scenario with the most likely diagnosis.\n\nVignette 1: A 25-year-old man presents with chronic crampy right lower quadrant pain, weight loss, and non-bloody diarrhoea. Colonoscopy shows patchy aphthous ulceration, discontinuous 'skip lesions', and cobblestoning affecting the terminal ileum and ascending colon. Histology demonstrates non-caseating granulomas.",
        "options": [
            "Crohn's Disease",
            "Ulcerative Colitis",
            "Microscopic Colitis",
            "Irritable Bowel Syndrome",
            "Exocrine Pancreatic Insufficiency",
            "Bile Acid Malabsorption",
            "Small Intestinal Bacterial Overgrowth (SIBO)",
            "Infective Giardiasis"
        ],
        "correct_answer": "Crohn's Disease",
        "explanation": "Discontinuous 'skip lesions', terminal ileal involvement, and transmural non-caseating granulomas are hallmark features of Crohn's disease."
    },
    {
        "type": "emq",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "Theme: Chronic Diarrhoea and Malabsorption. Match each scenario with the most likely diagnosis.\n\nVignette 2: A 64-year-old woman taking Sertraline and Lansoprazole presents with a 6-month history of frequent, watery, nocturnal diarrhoea without bleeding. Colonoscopy reveals macroscopically pristine, normal colonic mucosa. Random mucosal biopsies show thickened subepithelial collagen bands and lymphocytic infiltration.",
        "options": [
            "Crohn's Disease",
            "Ulcerative Colitis",
            "Microscopic Colitis",
            "Irritable Bowel Syndrome",
            "Exocrine Pancreatic Insufficiency",
            "Bile Acid Malabsorption",
            "Small Intestinal Bacterial Overgrowth (SIBO)",
            "Infective Giardiasis"
        ],
        "correct_answer": "Microscopic Colitis",
        "explanation": "Watery diarrhoea with completely normal macroscopy on colonoscopy but diagnostic histological inflammatory changes (collagenous or lymphocytic colitis) confirms microscopic colitis. Budesonide is first-line treatment."
    },
    {
        "type": "emq",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "Theme: Chronic Diarrhoea and Malabsorption. Match each scenario with the most likely diagnosis.\n\nVignette 3: A 31-year-old woman presents with fluctuating abdominal cramps that ease after passing stool, bloating, and alternating bowel habits between loose stools and constipation. Red flag symptoms are absent. Faecal calprotectin, full blood count, CRP, and coeliac serology are completely normal.",
        "options": [
            "Crohn's Disease",
            "Ulcerative Colitis",
            "Microscopic Colitis",
            "Irritable Bowel Syndrome",
            "Exocrine Pancreatic Insufficiency",
            "Bile Acid Malabsorption",
            "Small Intestinal Bacterial Overgrowth (SIBO)",
            "Infective Giardiasis"
        ],
        "correct_answer": "Irritable Bowel Syndrome",
        "explanation": "Recurrent abdominal pain related to defecation, altered stool consistency/frequency, and normal inflammatory/coeliac markers meet the Rome IV diagnostic criteria for Irritable Bowel Syndrome (IBS)."
    },
    {
        "type": "emq",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "Theme: Chronic Diarrhoea and Malabsorption. Match each scenario with the most likely diagnosis.\n\nVignette 4: A 59-year-old man with a long history of chronic pancreatitis presents with weight loss and bulky, pale, foul-smelling stools that float and are difficult to flush. Stool faecal elastase-1 is <50 mcg/g (reference >200 mcg/g).",
        "options": [
            "Crohn's Disease",
            "Ulcerative Colitis",
            "Microscopic Colitis",
            "Irritable Bowel Syndrome",
            "Exocrine Pancreatic Insufficiency",
            "Bile Acid Malabsorption",
            "Small Intestinal Bacterial Overgrowth (SIBO)",
            "Infective Giardiasis"
        ],
        "correct_answer": "Exocrine Pancreatic Insufficiency",
        "explanation": "Steatorrhoea in a patient with chronic pancreatitis and a severely reduced faecal elastase level confirms exocrine pancreatic insufficiency, treated with pancreatic enzyme replacement therapy (Creon)."
    },
    {
        "type": "emq",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "Theme: Chronic Diarrhoea and Malabsorption. Match each scenario with the most likely diagnosis.\n\nVignette 5: A 42-year-old man underwent a cholecystectomy 2 years ago and subsequently developed intractable chronic watery diarrhoea unresponsive to loperamide. A SeHCAT scan demonstrates 7-day retention of 4% (reference >15%). Symptoms resolve completely on Colestyramine.",
        "options": [
            "Crohn's Disease",
            "Ulcerative Colitis",
            "Microscopic Colitis",
            "Irritable Bowel Syndrome",
            "Exocrine Pancreatic Insufficiency",
            "Bile Acid Malabsorption",
            "Small Intestinal Bacterial Overgrowth (SIBO)",
            "Infective Giardiasis"
        ],
        "correct_answer": "Bile Acid Malabsorption",
        "explanation": "Post-cholecystectomy chronic watery diarrhoea with abnormal 7-day SeHCAT retention (<8-15%) and therapeutic response to bile acid sequestrants (colestyramine/colesevelam) confirms bile acid malabsorption (Type 3)."
    }
]
