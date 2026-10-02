# -*- coding: utf-8 -*-
"""
40 Additional High-Yield Questions
24 Clinical (2 per domain) + 16 Professional Dilemmas
"""

ADDITIONAL_QUESTIONS = [
    # 1. Cardiovascular
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 25-year-old man presents with sharp, tearing chest pain radiating to his back. He is tall with long, thin fingers and a pectus excavatum. Echocardiogram reveals an aortic root aneurysm. What genetic mutation is most likely responsible?",
        "options": [
            "FBN1 (Fibrillin-1)",
            "COL5A1 (Collagen type V)",
            "NF1 (Neurofibromin)",
            "LDLR (Low-density lipoprotein receptor)",
            "CFTR (Cystic fibrosis transmembrane conductance regulator)"
        ],
        "correct_answer": "FBN1 (Fibrillin-1)",
        "explanation": "The patient has Marfan syndrome, characterised by a tall stature, arachnodactyly, pectus excavatum, and aortic root dilation/dissection. It is caused by an autosomal dominant mutation in the FBN1 gene."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "An 80-year-old man presents with syncope on exertion. On examination, he has a slow-rising pulse, a narrow pulse pressure, and a harsh ejection systolic murmur radiating to the carotids. What is the most likely diagnosis?",
        "options": [
            "Aortic stenosis",
            "Aortic regurgitation",
            "Mitral stenosis",
            "Mitral regurgitation",
            "Hypertrophic obstructive cardiomyopathy"
        ],
        "correct_answer": "Aortic stenosis",
        "explanation": "A slow-rising pulse (pulsus parvus et tardus), narrow pulse pressure, and an ejection systolic murmur radiating to the carotids are classic pathognomonic signs of Aortic Stenosis."
    },

    # 2. Dermatology / Ophthalmology / ENT
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 40-year-old woman presents with intensely itchy, grouped blisters on her elbows and knees. She also complains of chronic diarrhoea and weight loss. Skin biopsy shows granular IgA deposits in the dermal papillae. What is the most appropriate management?",
        "options": [
            "Gluten-free diet and Dapsone",
            "Topical corticosteroids",
            "Oral Aciclovir",
            "Oral Prednisolone",
            "Avoidance of sunlight"
        ],
        "correct_answer": "Gluten-free diet and Dapsone",
        "explanation": "Grouped vesicles on extensor surfaces with granular IgA in the dermal papillae is pathognomonic for Dermatitis Herpetiformis, which is strongly associated with Coeliac disease. Treatment is a gluten-free diet and Dapsone for symptom relief."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 35-year-old woman with multiple sclerosis presents with sudden onset pain on eye movement and reduced vision in her left eye. She has a relative afferent pupillary defect (RAPD). What is this sign called?",
        "options": [
            "Marcus Gunn pupil",
            "Argyll Robertson pupil",
            "Adie's tonic pupil",
            "Horner's syndrome",
            "Holmes-Adie pupil"
        ],
        "correct_answer": "Marcus Gunn pupil",
        "explanation": "A relative afferent pupillary defect (RAPD) is also known as a Marcus Gunn pupil. In the swinging flashlight test, the affected pupil appears to dilate when light is shone directly into it, classic for Optic Neuritis."
    },

    # 3. Endocrinology / Metabolic
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 45-year-old woman presents with weight gain, easy bruising, and proximal muscle weakness. Examination reveals purple striae on her abdomen and a 'buffalo hump'. A high-dose dexamethasone suppression test suppresses her cortisol levels by 60%. What is the most likely source of her condition?",
        "options": [
            "Pituitary adenoma",
            "Adrenal adenoma",
            "Small cell lung cancer",
            "Exogenous steroid use",
            "Thyroid adenoma"
        ],
        "correct_answer": "Pituitary adenoma",
        "explanation": "Purple striae and buffalo hump indicate Cushing's syndrome. Suppression of cortisol on a high-dose (but not low-dose) dexamethasone test is pathognomonic for Cushing's disease (a pituitary adenoma secreting ACTH). Ectopic ACTH and adrenal sources do not suppress."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 30-year-old woman presents with severe episodic headaches, sweating, and palpitations. Her blood pressure is 180/110 mmHg. A 24-hour urine collection shows significantly elevated metanephrines. Before surgical resection, what pharmacological blockade must be initiated first?",
        "options": [
            "Alpha-blocker (e.g., Phenoxybenzamine)",
            "Beta-blocker (e.g., Propranolol)",
            "Calcium channel blocker",
            "ACE inhibitor",
            "Thiazide diuretic"
        ],
        "correct_answer": "Alpha-blocker (e.g., Phenoxybenzamine)",
        "explanation": "The patient has a Phaeochromocytoma. Alpha-blockade MUST be initiated before beta-blockade to prevent an unopposed alpha-adrenergic crisis, which could cause a catastrophic hypertensive emergency."
    },

    # 4. Gastroenterology / Clinical Nutrition
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 55-year-old man presents with chronic epigastric pain radiating to his back, steatorrhoea, and new-onset diabetes mellitus. A plain abdominal radiograph shows diffuse calcification in the epigastric region. What is the diagnosis?",
        "options": [
            "Chronic pancreatitis",
            "Pancreatic adenocarcinoma",
            "Peptic ulcer disease",
            "Choledocholithiasis",
            "Haemochromatosis"
        ],
        "correct_answer": "Chronic pancreatitis",
        "explanation": "The classic triad of steatorrhoea, diabetes mellitus, and pancreatic calcification on X-ray is pathognomonic for late-stage Chronic Pancreatitis."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 40-year-old woman presents with fatigue and pruritus. Blood tests show an isolated raised Alkaline Phosphatase (ALP). Antimitochondrial antibodies (AMA) are positive at a high titre. What is the most likely diagnosis?",
        "options": [
            "Primary Biliary Cholangitis (PBC)",
            "Primary Sclerosing Cholangitis (PSC)",
            "Autoimmune hepatitis",
            "Wilson's disease",
            "Alpha-1 antitrypsin deficiency"
        ],
        "correct_answer": "Primary Biliary Cholangitis (PBC)",
        "explanation": "Positive antimitochondrial antibodies (AMA) in the context of cholestasis (raised ALP, pruritus) in a middle-aged woman is pathognomonic for Primary Biliary Cholangitis (PBC)."
    },

    # 5. Infectious Diseases / Haematology / Immunology / Allergies / Genetics
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 15-year-old boy presents with severe pain in his legs and chest. He has a history of a chronic haemolytic anaemia. A peripheral blood smear reveals red blood cells shaped like sickles and the presence of Howell-Jolly bodies. What does the presence of Howell-Jolly bodies signify?",
        "options": [
            "Hyposplenism / Autosplenectomy",
            "Acute myeloid leukaemia",
            "Lead poisoning",
            "Megaloblastic anaemia",
            "G6PD deficiency"
        ],
        "correct_answer": "Hyposplenism / Autosplenectomy",
        "explanation": "Howell-Jolly bodies are nuclear remnants normally removed by the spleen. Their presence in Sickle Cell Disease is a pathognomonic sign of functional hyposplenism (autosplenectomy) due to repeated splenic infarctions."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 25-year-old woman presents with a 'butterfly' rash across her cheeks and nose, which worsens in the sun. She also complains of joint pains. Blood tests reveal a positive ANA and anti-dsDNA. What is the most likely diagnosis?",
        "options": [
            "Systemic Lupus Erythematosus (SLE)",
            "Rosacea",
            "Dermatomyositis",
            "Rheumatoid arthritis",
            "Systemic sclerosis"
        ],
        "correct_answer": "Systemic Lupus Erythematosus (SLE)",
        "explanation": "A malar 'butterfly' rash sparing the nasolabial folds, along with anti-dsDNA and anti-Smith antibodies, is highly specific and pathognomonic for Systemic Lupus Erythematosus (SLE)."
    },

    # 6. Musculoskeletal
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 45-year-old woman presents with dry eyes, a dry mouth, and bilateral parotid gland enlargement. She has positive anti-Ro (SSA) and anti-La (SSB) antibodies. Schirmer's test reveals less than 5mm of wetting in 5 minutes. What is the diagnosis?",
        "options": [
            "Sjögren's syndrome",
            "Systemic Lupus Erythematosus",
            "Rheumatoid arthritis",
            "Systemic sclerosis",
            "Mumps"
        ],
        "correct_answer": "Sjögren's syndrome",
        "explanation": "The triad of keratoconjunctivitis sicca (dry eyes), xerostomia (dry mouth), and positive anti-Ro/La antibodies is the classic presentation of Sjögren's syndrome."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 55-year-old woman complains of thickened, tight skin on her fingers and face. She also experiences colour changes in her fingers in the cold. Blood tests reveal anti-centromere antibodies. She is at particular risk of developing which complication?",
        "options": [
            "Pulmonary arterial hypertension",
            "Renal crisis",
            "Interstitial lung disease",
            "Myocarditis",
            "Aortic root dilation"
        ],
        "correct_answer": "Pulmonary arterial hypertension",
        "explanation": "The patient has Limited Cutaneous Systemic Sclerosis (CREST syndrome), marked by anti-centromere antibodies. This specific subtype is strongly associated with a high risk of developing Pulmonary Arterial Hypertension."
    },

    # 7. Paediatrics
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 3-week-old male infant presents with projectile, non-bilious vomiting immediately after feeds. He is hungry and eager to feed again. On palpation, an 'olive-sized' mass is felt in the right upper quadrant. What acid-base disturbance is most expected?",
        "options": [
            "Hypochloraemic, hypokalaemic metabolic alkalosis",
            "Hyperchloraemic metabolic acidosis",
            "Respiratory alkalosis",
            "Hyponatraemic metabolic acidosis",
            "Normal acid-base balance"
        ],
        "correct_answer": "Hypochloraemic, hypokalaemic metabolic alkalosis",
        "explanation": "An 'olive' mass and projectile non-bilious vomiting are pathognomonic for Pyloric Stenosis. The loss of gastric hydrochloric acid leads to the classic hypochloraemic, hypokalaemic metabolic alkalosis."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 5-year-old boy presents with a high fever for 6 days, bilateral non-purulent conjunctivitis, cracked red lips, a 'strawberry tongue', and a desquamating rash on his hands. He is diagnosed with Kawasaki disease. What is the most critical investigation?",
        "options": [
            "Echocardiogram",
            "Lumbar puncture",
            "Blood cultures",
            "CT brain",
            "Renal ultrasound"
        ],
        "correct_answer": "Echocardiogram",
        "explanation": "A 'strawberry tongue' and prolonged fever with these mucocutaneous signs is classic for Kawasaki disease. An echocardiogram is critical to check for the pathognomonic and dangerous complication: coronary artery aneurysms."
    },

    # 8. Psychiatry / Neurology
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 30-year-old woman complains of double vision and drooping eyelids that worsen towards the end of the day. A Tensilon (edrophonium) test results in marked, temporary improvement of her ptosis. Antibodies against which receptor are most likely present?",
        "options": [
            "Acetylcholine receptor (AChR)",
            "Voltage-gated calcium channel (VGCC)",
            "NMDA receptor",
            "Dopamine receptor",
            "Serotonin receptor"
        ],
        "correct_answer": "Acetylcholine receptor (AChR)",
        "explanation": "Fatigable weakness (worse at the end of the day) that improves with an acetylcholinesterase inhibitor is classic for Myasthenia Gravis, driven by anti-AChR antibodies (or MuSK antibodies)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 40-year-old man presents with sudden-onset 'thunderclap' headache, the worst he has ever experienced. A non-contrast CT brain performed 4 hours later is normal. What is the next most appropriate investigation to confirm the suspected diagnosis?",
        "options": [
            "Lumbar puncture for xanthochromia",
            "MRI Brain",
            "EEG",
            "Carotid doppler",
            "Temporal artery biopsy"
        ],
        "correct_answer": "Lumbar puncture for xanthochromia",
        "explanation": "A thunderclap headache is highly suspicious for a Subarachnoid Haemorrhage (SAH). If the initial CT is negative, a lumbar puncture performed >12 hours post-onset looking for xanthochromia (bilirubin from broken-down RBCs) is the classic diagnostic step."
    },

    # 9. Renal / Urology
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 50-year-old man presents with visible haematuria, flank pain, and a palpable abdominal mass. He also has a left-sided varicocele that does not empty when lying flat. What is the most likely diagnosis?",
        "options": [
            "Renal cell carcinoma",
            "Transitional cell carcinoma of the bladder",
            "Polycystic kidney disease",
            "Nephrolithiasis",
            "Prostate cancer"
        ],
        "correct_answer": "Renal cell carcinoma",
        "explanation": "The classic triad of haematuria, flank pain, and a palpable mass, along with a left-sided varicocele (due to tumour invasion into the left renal vein blocking the left gonadal vein), is highly suggestive of Renal Cell Carcinoma."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 6-year-old boy presents with generalized oedema. Urine dipstick shows ++++ protein. Bloods reveal hypoalbuminaemia. He is treated with high-dose oral prednisolone and fully recovers. What would a renal biopsy most likely have shown on electron microscopy?",
        "options": [
            "Effacement of podocyte foot processes",
            "Subepithelial immune complex 'spikes'",
            "IgA deposition in the mesangium",
            "Linear IgG deposition on the basement membrane",
            "Tram-track appearance of the basement membrane"
        ],
        "correct_answer": "Effacement of podocyte foot processes",
        "explanation": "This is Minimal Change Disease, the most common cause of nephrotic syndrome in children. It responds well to steroids, and electron microscopy characteristically shows effacement of podocyte foot processes."
    },

    # 10. Reproductive / Obstetrics & Gynaecology
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 60-year-old postmenopausal woman presents with a 4-week history of vaginal bleeding. Her BMI is 35 and she has type 2 diabetes. What is the most appropriate initial investigation to exclude malignancy?",
        "options": [
            "Transvaginal ultrasound scan (TVUS)",
            "Cervical smear",
            "Colposcopy",
            "CA-125 level",
            "Pelvic MRI"
        ],
        "correct_answer": "Transvaginal ultrasound scan (TVUS)",
        "explanation": "Postmenopausal bleeding must be assumed to be endometrial cancer until proven otherwise. The classic first-line investigation is a TVUS to measure endometrial thickness (>4mm warrants biopsy)."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 28-year-old pregnant woman at 34 weeks gestation presents with painless, bright red vaginal bleeding. Her abdomen is soft and non-tender on palpation. What is the most likely diagnosis?",
        "options": [
            "Placenta praevia",
            "Placental abruption",
            "Vasa praevia",
            "Uterine rupture",
            "Cervical ectropion"
        ],
        "correct_answer": "Placenta praevia",
        "explanation": "Painless, bright red vaginal bleeding in the third trimester with a soft, non-tender uterus is the classic clinical presentation of Placenta Praevia."
    },

    # 11. Respiratory
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 50-year-old man presents with chronic cough, progressive breathlessness, and significant weight loss. He is a heavy smoker. On examination, he has ptosis and miosis of the right eye, and anhidrosis on the right side of his face. What is the diagnosis?",
        "options": [
            "Pancoast tumour",
            "Mesothelioma",
            "Small cell lung carcinoma",
            "Carcinoid tumour",
            "Tuberculosis"
        ],
        "correct_answer": "Pancoast tumour",
        "explanation": "A lung apex tumour (Pancoast tumour) compressing the sympathetic chain causes the classic triad of ptosis, miosis, and anhidrosis, known as Horner's syndrome."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 40-year-old woman is recovering in the ICU after severe sepsis. She rapidly develops profound hypoxaemia and bilateral pulmonary infiltrates on chest X-ray. Her pulmonary capillary wedge pressure is normal. What is the diagnosis?",
        "options": [
            "Acute Respiratory Distress Syndrome (ARDS)",
            "Cardiogenic pulmonary oedema",
            "Pulmonary embolism",
            "Hospital-acquired pneumonia",
            "Idiopathic pulmonary fibrosis"
        ],
        "correct_answer": "Acute Respiratory Distress Syndrome (ARDS)",
        "explanation": "Bilateral infiltrates ('white out') with severe hypoxaemia and a normal PCWP (indicating non-cardiogenic pulmonary oedema) following a systemic insult like sepsis is the classic picture of ARDS."
    },

    # 12. Pharmacology
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 70-year-old man on tuberculosis treatment presents with numbness and 'pins and needles' in his hands and feet. Which anti-tuberculosis medication is the most likely cause, and what could have prevented this?",
        "options": [
            "Isoniazid; Pyridoxine (Vitamin B6)",
            "Rifampicin; Vitamin C",
            "Ethambutol; Vitamin A",
            "Pyrazinamide; Vitamin D",
            "Streptomycin; Thiamine (Vitamin B1)"
        ],
        "correct_answer": "Isoniazid; Pyridoxine (Vitamin B6)",
        "explanation": "Isoniazid classically causes peripheral neuropathy by depleting Vitamin B6. It is routinely co-prescribed with pyridoxine (Vitamin B6) to prevent this complication."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 25-year-old man is brought to the emergency department agitated, tachycardic, and hyperthermic. His pupils are widely dilated. He tells you he took an overdose of amitriptyline. An ECG shows a widened QRS complex. What is the specific antidote for this cardiotoxicity?",
        "options": [
            "Intravenous Sodium Bicarbonate",
            "Intravenous Glucagon",
            "Intravenous Naloxone",
            "Intravenous Flumazenil",
            "Intravenous Atropine"
        ],
        "correct_answer": "Intravenous Sodium Bicarbonate",
        "explanation": "Amitriptyline is a tricyclic antidepressant (TCA). TCA overdose classically causes anticholinergic toxidrome and QRS widening due to sodium channel blockade. The specific antidote for the cardiotoxicity is IV Sodium Bicarbonate."
    },

    # 13. Professional Dilemmas (8 Ranking, 8 Selection)
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a Foundation Year 1 (FY1) doctor on a busy surgical ward. A nurse asks you to prescribe a fluid bolus for a patient who has become hypotensive. You have not assessed this patient yet, but the nurse says the registrar previously mentioned they might need fluids. \n\nRank the following actions in order of appropriateness from most (1) to least (5) appropriate.",
        "options": [
            "Immediately attend the patient to perform an ABCDE assessment before prescribing.",
            "Ask the nurse to read the registrar's exact plan in the notes before you decide.",
            "Bleep the registrar to ask them to review the patient instead.",
            "Prescribe a small 250ml fluid bolus immediately to be safe, then review the patient.",
            "Refuse to prescribe the fluids and tell the nurse it is not your responsibility."
        ],
        "correct_answer": [
            "Immediately attend the patient to perform an ABCDE assessment before prescribing.",
            "Ask the nurse to read the registrar's exact plan in the notes before you decide.",
            "Bleep the registrar to ask them to review the patient instead.",
            "Prescribe a small 250ml fluid bolus immediately to be safe, then review the patient.",
            "Refuse to prescribe the fluids and tell the nurse it is not your responsibility."
        ],
        "explanation": "Patient safety is paramount. You must not prescribe blindly; an ABCDE assessment is required first (1). Checking notes provides context but delays care slightly (2). Escalating to the registrar is safe but shifts your own responsibility unnecessarily (3). Prescribing blindly is dangerous (4). Refusing and walking away neglects patient care (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You notice a senior consultant consistently arriving late for the morning ward round, smelling faintly of alcohol, and appearing disorganized. This is beginning to affect patient care and ward efficiency. \n\nRank the following actions in order of appropriateness.",
        "options": [
            "Discuss your concerns confidentially with your educational supervisor or clinical lead.",
            "Speak to the consultant directly and privately about your observations.",
            "Raise a formal Datix/incident report detailing the patient care delays.",
            "Discuss the situation with your FY1 peers to see if they have noticed the same.",
            "Ignore the situation as they are much senior to you and it is not your place."
        ],
        "correct_answer": [
            "Discuss your concerns confidentially with your educational supervisor or clinical lead.",
            "Speak to the consultant directly and privately about your observations.",
            "Raise a formal Datix/incident report detailing the patient care delays.",
            "Discuss the situation with your FY1 peers to see if they have noticed the same.",
            "Ignore the situation as they are much senior to you and it is not your place."
        ],
        "explanation": "Escalating concerns about a senior colleague's fitness to practice (especially involving alcohol) to a senior leader (Clinical Lead) is the most appropriate action (1). Confronting them directly is very difficult and may not be effective, but is better than gossiping (2). Formal reports are useful but immediate senior intervention is needed for acute safety (3). Gossiping is unprofessional (4). Ignoring patient safety risks is a breach of GMC guidance (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are covering the night shift. You are paged by three different wards simultaneously:\n1. A patient with a National Early Warning Score (NEWS) of 8 due to hypoxia.\n2. A nurse requesting a routine cannula for IV antibiotics due in 1 hour.\n3. A patient demanding sleeping tablets, keeping the bay awake.\n\nRank the order in which you should prioritize these tasks.",
        "options": [
            "Attend the patient with NEWS 8 immediately.",
            "Delegate the cannula to the night nurse practitioner if available.",
            "Attend to the routine cannula yourself.",
            "Prescribe the sleeping tablets via the electronic prescribing system remotely.",
            "Tell the nurse on the phone that sleeping tablets are not an emergency and to wait."
        ],
        "correct_answer": [
            "Attend the patient with NEWS 8 immediately.",
            "Delegate the cannula to the night nurse practitioner if available.",
            "Attend to the routine cannula yourself.",
            "Prescribe the sleeping tablets via the electronic prescribing system remotely.",
            "Tell the nurse on the phone that sleeping tablets are not an emergency and to wait."
        ],
        "explanation": "Clinical prioritization must be based on clinical urgency (ABCDE). The NEWS 8 patient is critically unwell (1). Delegating appropriate tasks helps manage workload (2). Doing the cannula is a clinical task but non-urgent (3). Remote prescribing for a non-urgent issue is low priority but helpful (4). Being dismissive to colleagues is unprofessional (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A patient's relative aggressively approaches you in the corridor, demanding to know why their mother's scan has been delayed. They are shouting and blocking your path. \n\nRank the following actions in order of appropriateness.",
        "options": [
            "Maintain a calm demeanor, step back to ensure personal safety, and ask them to move to a private room to discuss.",
            "Call security immediately for assistance.",
            "Explain that you are very busy and will come find them later.",
            "Tell them firmly to stop shouting or you will refuse to speak with them.",
            "Walk away quickly without saying anything."
        ],
        "correct_answer": [
            "Maintain a calm demeanor, step back to ensure personal safety, and ask them to move to a private room to discuss.",
            "Call security immediately for assistance.",
            "Explain that you are very busy and will come find them later.",
            "Tell them firmly to stop shouting or you will refuse to speak with them.",
            "Walk away quickly without saying anything."
        ],
        "explanation": "De-escalation and communication are key. Moving to a private, safe space is best (1). If you feel actively threatened, security is the correct next step (2). Delaying the conversation may anger them further but removes you from danger (3). Being confrontational escalates the situation (4). Ignoring them completely is highly unprofessional and inflammatory (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You realize you have just prescribed Penicillin to a patient who has a documented severe Penicillin allergy. The nurse has just administered the drug. \n\nRank the following actions in order of appropriateness.",
        "options": [
            "Immediately attend the patient, assess ABCDE, and prepare anaphylaxis treatment.",
            "Inform the nurse to stop the infusion immediately.",
            "Inform your senior and document the error clearly in the notes.",
            "Submit a Datix/incident report.",
            "Apologize to the patient once they are medically stable."
        ],
        "correct_answer": [
            "Inform the nurse to stop the infusion immediately.",
            "Immediately attend the patient, assess ABCDE, and prepare anaphylaxis treatment.",
            "Inform your senior and document the error clearly in the notes.",
            "Submit a Datix/incident report.",
            "Apologize to the patient once they are medically stable."
        ],
        "explanation": "Stopping further harm is the absolute first step (1). Resuscitating and assessing the patient is the immediate clinical priority (2). Escalating to seniors and documenting is next (3). Formal incident reporting is required but done after the patient is safe (4). Duty of candour applies, but must wait until clinical safety is assured (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are updating a patient's family about their terminal prognosis, but the patient explicitly asked you yesterday not to tell their family they are dying. The family is pushing you for a timeframe. \n\nRank the following actions in order of appropriateness.",
        "options": [
            "Politely explain that you must respect the patient's confidentiality and cannot share that information.",
            "Encourage the family to speak directly with the patient about their concerns.",
            "Discuss the situation with the patient again, explaining their family's distress.",
            "Give the family a vague timeframe to pacify them without giving medical details.",
            "Tell the family the prognosis because it is in their best interest to prepare."
        ],
        "correct_answer": [
            "Politely explain that you must respect the patient's confidentiality and cannot share that information.",
            "Encourage the family to speak directly with the patient about their concerns.",
            "Discuss the situation with the patient again, explaining their family's distress.",
            "Give the family a vague timeframe to pacify them without giving medical details.",
            "Tell the family the prognosis because it is in their best interest to prepare."
        ],
        "explanation": "Patient confidentiality is absolute unless there is a legal exception. You must refuse (1). Facilitating communication is helpful (2). Re-evaluating the patient's consent is good practice (3). Giving vague hints breaches confidentiality subtly (4). Direct disclosure is a major GMC breach (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You post a frustrated comment on social media about how 'incompetent' the management team is at your current NHS trust. A colleague sees it and advises you to delete it. \n\nRank the following actions in order of appropriateness.",
        "options": [
            "Delete the post immediately and reflect on GMC social media guidelines.",
            "Thank the colleague but leave the post up as it is your private account.",
            "Edit the post to remove the name of the specific hospital.",
            "Argue with the colleague that you have a right to free speech.",
            "Post a follow-up rant about colleagues spying on you."
        ],
        "correct_answer": [
            "Delete the post immediately and reflect on GMC social media guidelines.",
            "Edit the post to remove the name of the specific hospital.",
            "Thank the colleague but leave the post up as it is your private account.",
            "Argue with the colleague that you have a right to free speech.",
            "Post a follow-up rant about colleagues spying on you."
        ],
        "explanation": "Doctors are held to high professional standards online. Deleting it is the only fully appropriate action (1). Editing it reduces identifying harm but remains unprofessional (2). Ignoring the advice risks your registration (3). Arguing shows lack of insight (4). Doubling down is highly unprofessional (5)."
    },
    {
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You see an FY1 colleague taking hospital supplies (boxes of gloves and hand sanitizer) and putting them in their bag to take home. \n\nRank the following actions in order of appropriateness.",
        "options": [
            "Approach the colleague privately and ask them why they are taking the supplies.",
            "Report the theft directly to your clinical supervisor.",
            "Inform hospital security.",
            "Take the supplies out of their bag when they are not looking.",
            "Ignore it, as the hospital has plenty of supplies."
        ],
        "correct_answer": [
            "Approach the colleague privately and ask them why they are taking the supplies.",
            "Report the theft directly to your clinical supervisor.",
            "Inform hospital security.",
            "Take the supplies out of their bag when they are not looking.",
            "Ignore it, as the hospital has plenty of supplies."
        ],
        "explanation": "Addressing the issue directly gives them a chance to explain or return items (1). If unsatisfied, escalating to a clinical senior is appropriate for a doctor (2). Security is an escalation if theft is confirmed (3). Stealing it back is unprofessional (4). Ignoring theft breaches probity (5)."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A nurse tells you that the patient in Bed 4 is refusing to have their blood drawn, despite it being urgently needed to check their potassium levels before giving IV fluids. The patient is fully conscious and capacitous. \n\nChoose the THREE most appropriate immediate actions to take.",
        "options": [
            "Go and talk to the patient to explore their reasons for refusing.",
            "Explain the clinical risks of not having the blood test (e.g., cardiac arrhythmias).",
            "Document the refusal clearly in the patient's medical notes.",
            "Ask the nurse to hold the patient's arm still while you take the blood quickly.",
            "Prescribe oral potassium blindly just in case.",
            "Discharge the patient against medical advice.",
            "Refer the patient for a psychiatric capacity assessment.",
            "Tell the patient they will be forcibly treated under the Mental Capacity Act."
        ],
        "correct_answer": [
            "Go and talk to the patient to explore their reasons for refusing.",
            "Explain the clinical risks of not having the blood test (e.g., cardiac arrhythmias).",
            "Document the refusal clearly in the patient's medical notes."
        ],
        "explanation": "A capacitous patient has the absolute right to refuse treatment. You must explore their ideas, concerns, and expectations (ICE), explain the risks so their refusal is informed, and document the event carefully to protect yourself medico-legally. Forcing treatment is assault."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are a GP trainee. A 16-year-old girl requests the oral contraceptive pill. She asks you not to tell her parents. \n\nChoose the THREE criteria (Fraser Guidelines) that MUST be met for you to prescribe without parental consent.",
        "options": [
            "The young person understands the advice and implications of the treatment.",
            "She cannot be persuaded to inform her parents.",
            "She is likely to begin or continue having sexual intercourse with or without the treatment.",
            "She is legally married.",
            "She is accompanied by an older sibling.",
            "Her physical or mental health will suffer if she does not receive the advice or treatment.",
            "She pays a prescription charge.",
            "She has previously been pregnant."
        ],
        "correct_answer": [
            "The young person understands the advice and implications of the treatment.",
            "She cannot be persuaded to inform her parents.",
            "She is likely to begin or continue having sexual intercourse with or without the treatment."
        ],
        "explanation": "Fraser guidelines state you can prescribe to under-16s if: they understand the advice, cannot be persuaded to tell parents, are likely to have sex anyway, their physical/mental health will suffer without it, and it is in their best interests."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "During a handover, you notice that a fellow doctor smells strongly of cannabis. They are about to start a 12-hour shift in the Emergency Department. \n\nChoose the THREE most appropriate immediate actions.",
        "options": [
            "Take the colleague aside and express your concern about their fitness to work.",
            "Inform the ED Consultant in charge immediately.",
            "Ensure the colleague does not see any patients.",
            "Call the police to arrest the colleague.",
            "Search the colleague's locker for drugs.",
            "Send the colleague home in a taxi without telling anyone.",
            "Ask the nurses to double-check all of the colleague's prescriptions.",
            "Post about it anonymously on a medical forum for advice."
        ],
        "correct_answer": [
            "Take the colleague aside and express your concern about their fitness to work.",
            "Inform the ED Consultant in charge immediately.",
            "Ensure the colleague does not see any patients."
        ],
        "explanation": "Patient safety is compromised by an intoxicated doctor. You must confront them, immediately escalate to the clinical lead to arrange cover, and prevent them from seeing patients. Police and searches are not your immediate clinical responsibility."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A 75-year-old patient who has just been diagnosed with metastatic lung cancer tells you, 'I'm going to beat this and run a marathon next year.' You know the prognosis is less than 6 months. \n\nChoose the THREE most appropriate ways to respond.",
        "options": [
            "Acknowledge and validate their emotional reaction.",
            "Gently explore their understanding of the diagnosis you just gave.",
            "Offer to involve palliative care and specialist nurses for support.",
            "Immediately correct them and state bluntly that they will die soon.",
            "Agree enthusiastically and offer them a training plan to keep their hopes up.",
            "Leave the room to give them time to realize their mistake.",
            "Prescribe antidepressants immediately.",
            "Ask their family to explain it to them instead."
        ],
        "correct_answer": [
            "Acknowledge and validate their emotional reaction.",
            "Gently explore their understanding of the diagnosis you just gave.",
            "Offer to involve palliative care and specialist nurses for support."
        ],
        "explanation": "Denial is a common early grief reaction. You should not crush their hope brutally, but neither should you collude in a lie. Exploring their understanding, showing empathy, and providing structural support (MDT/palliative) are the best approaches."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You discover you have accidentally breached data protection by leaving a printed patient handover sheet on a bus. \n\nChoose the THREE most appropriate actions.",
        "options": [
            "Inform your clinical supervisor or line manager immediately.",
            "Report the incident to the hospital's Information Governance team (Caldicott Guardian).",
            "Document the incident via the trust's incident reporting system (Datix).",
            "Try to find the bus and search it yourself before telling anyone.",
            "Keep quiet, as it's unlikely anyone will know it was you.",
            "Call the police to report stolen property.",
            "Personally call all the patients on the list to apologize immediately.",
            "Resign from your post."
        ],
        "correct_answer": [
            "Inform your clinical supervisor or line manager immediately.",
            "Report the incident to the hospital's Information Governance team (Caldicott Guardian).",
            "Document the incident via the trust's incident reporting system (Datix)."
        ],
        "explanation": "Data breaches must be formally reported so the trust can take mitigating action (Information Governance/Caldicott Guardian). You must escalate via seniors and Datix. Covering it up breaches probity."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are struggling to cope with the workload on your ward. You are staying 2 hours late every day and feeling exhausted and tearful. \n\nChoose the THREE most appropriate actions to take to manage this.",
        "options": [
            "Discuss your workload with your clinical supervisor to find strategies for prioritizing.",
            "Speak to your colleagues to see if tasks can be distributed more fairly.",
            "Ensure you take your mandatory breaks, even if it means handing over non-urgent tasks.",
            "Start ignoring your pager for the last hour of your shift.",
            "Pre-prescribe medications for tomorrow to save time, even if unsafe.",
            "Complain to the patients about how understaffed the hospital is.",
            "Stop doing ward rounds.",
            "Hand in your notice immediately."
        ],
        "correct_answer": [
            "Discuss your workload with your clinical supervisor to find strategies for prioritizing.",
            "Speak to your colleagues to see if tasks can be distributed more fairly.",
            "Ensure you take your mandatory breaks, even if it means handing over non-urgent tasks."
        ],
        "explanation": "Burnout and overworking are dangerous for both the doctor and patients. Communicating with seniors for support, delegating, and protecting your own health (taking breaks) are professional and sustainable solutions."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You witness a surgeon breaking sterile field protocol during a minor procedure. When you mention it, they dismiss you, saying 'it doesn't matter for this type of case'. \n\nChoose the THREE most appropriate actions.",
        "options": [
            "Document the breach of protocol in the patient's operative notes.",
            "Discuss the incident with your educational supervisor or the surgical lead.",
            "Submit an incident report (Datix) highlighting the infection risk.",
            "Scrub in and physically stop the surgeon from continuing.",
            "Tell the patient after the surgery that the surgeon was unhygienic.",
            "Refuse to work with that surgeon ever again.",
            "Call the General Medical Council immediately.",
            "Shout at the surgeon in front of the theater team."
        ],
        "correct_answer": [
            "Document the breach of protocol in the patient's operative notes.",
            "Discuss the incident with your educational supervisor or the surgical lead.",
            "Submit an incident report (Datix) highlighting the infection risk."
        ],
        "explanation": "Infection control is a major safety issue. The breach must be documented, escalated to a senior (as the surgeon was dismissive), and logged formally via Datix. Confrontation or causing a scene in theatre is unprofessional."
    },
    {
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A pharmaceutical representative offers you an all-expenses-paid trip to a medical conference in exchange for promoting their new drug to your colleagues. \n\nChoose the THREE most appropriate actions in response to this offer.",
        "options": [
            "Politely decline the offer.",
            "Explain that accepting such gifts violates GMC probity guidelines.",
            "Report the interaction to your clinical lead or trust management.",
            "Accept the trip but secretly don't promote the drug.",
            "Ask if they can just pay you the cash equivalent instead.",
            "Promote the drug only to patients, not colleagues.",
            "Accept the offer as a reward for your hard work.",
            "Threaten the representative with physical violence."
        ],
        "correct_answer": [
            "Politely decline the offer.",
            "Explain that accepting such gifts violates GMC probity guidelines.",
            "Report the interaction to your clinical lead or trust management."
        ],
        "explanation": "Accepting gifts that could influence prescribing is a severe breach of GMC probity guidelines (bribery/conflict of interest). You must decline, state why, and inform management to ensure transparency."
    }
]
