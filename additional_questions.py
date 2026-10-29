# additional_questions.py
# Contains the remaining 24 Clinical SBAs (2 per domain) and 16 Professional Dilemmas (8 ranking, 8 selection).

ADDITIONAL_QUESTIONS = [
    # ==========================================
    # CARDIOVASCULAR (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 66-year-old hypertensive man develops sudden, severe tearing interscapular pain. His BP is 188/104 mmHg in the right arm and 146/86 mmHg in the left arm. ECG shows LVH with lateral ST-T changes, and the nurse asks whether to give loading aspirin and ticagrelor. What is the immediate action?",
        "options": [
            "Withhold antiplatelets and arrange an urgent CT aortogram",
            "Give aspirin 300 mg and ticagrelor 180 mg and repeat ECG",
            "Administer intravenous alteplase thrombolysis",
            "Request a serum D-dimer before arranging imaging",
            "Start an intravenous dobutamine infusion"
        ],
        "correct_answer": "Withhold antiplatelets and arrange an urgent CT aortogram",
        "explanation": "Sudden tearing interscapular pain with a >20 mmHg inter-arm systolic BP discrepancy indicates acute aortic dissection. Giving ACS antiplatelets or anticoagulants can trigger fatal haemorrhage; immediate CT aortography (and IV beta-blockade with labetalol) is the priority."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 79-year-old woman on digoxin, ramipril, and furosemide presents with 4 days of nausea, anorexia, and yellow-green visual disturbance, 2 weeks after her furosemide dose was doubled. ECG shows AF at 52 bpm with down-sloping ST depression. Which electrolyte abnormality precipitated this?",
        "options": [
            "Hypokalaemia",
            "Hyperkalaemia",
            "Hypocalcaemia",
            "Hyponatraemia",
            "Hypermagnesaemia"
        ],
        "correct_answer": "Hypokalaemia",
        "explanation": "Nausea, xanthopsia (yellow-green vision), and bradyarrhythmia indicate digoxin toxicity (whereas reverse-tick ST depression shows digoxin effect). Digoxin competes with potassium ions at the myocardial Na+/K+-ATPase pump; loop diuretic-induced hypokalaemia reduces potassium competition, markedly potentiating digoxin toxicity."
    },

    # ==========================================
    # DERMATOLOGY / OPHTHALMOLOGY / ENT (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 44-year-old man with mild plaque psoriasis becomes febrile (38.6°C) and tachycardic (114 bpm) 5 days after finishing a 5-day course of oral prednisolone for sinusitis. His skin is diffusely fiery red, tender, and covered in sheets of tiny sterile pinpoint yellow pustules. What is the diagnosis?",
        "options": [
            "Generalised pustular psoriasis triggered by steroid withdrawal",
            "Staphylococcal scalded skin syndrome",
            "Stevens-Johnson syndrome secondary to prednisolone",
            "Eczema herpeticum",
            "Cellulitis with secondary impetiginisation"
        ],
        "correct_answer": "Generalised pustular psoriasis triggered by steroid withdrawal",
        "explanation": "Abrupt withdrawal of systemic corticosteroids in psoriasis can precipitate a life-threatening rebound flare of generalised pustular (von Zumbusch) or erythrodermic psoriasis. Urgent hospital admission is required due to the risk of sepsis, hypothermia, and high-output cardiac failure."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 36-year-old woman wakes with right facial weakness, drooling, and right hyperacusis. She cannot wrinkle her right forehead or fully close her right eye. Otoscopy and limb neurology are normal. Presenting within 72 hours of onset, what is the appropriate management?",
        "options": [
            "Oral prednisolone and lubricating eye drops with night-time eye taping",
            "Urgent non-contrast CT head and stroke thrombolysis call",
            "Oral aciclovir monotherapy for 7 days",
            "Oral amoxicillin for presumed acute otitis media",
            "Immediate surgical decompression of the facial nerve"
        ],
        "correct_answer": "Oral prednisolone and lubricating eye drops with night-time eye taping",
        "explanation": "Forehead involvement confirms a lower motor neuron CN VII lesion (unlike stroke, which spares the forehead), and normal otoscopy excludes Ramsay Hunt syndrome. NICE recommends oral prednisolone within 72 hours of Bell's palsy onset plus corneal protection (lubricating drops and night taping); antivirals alone are ineffective."
    },

    # ==========================================
    # ENDOCRINOLOGY / METABOLIC (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 52-year-old man with hereditary spherocytosis presents with polyuria and polydipsia. Two fasting venous glucose readings are 9.8 mmol/L and 10.4 mmol/L, but his HbA1c is 34 mmol/mol (normal <42). What explains this discrepancy?",
        "options": [
            "Shortened red cell lifespan in spherocytosis causes a falsely low HbA1c",
            "Hereditary spherocytosis increases glycation, falsely elevating HbA1c",
            "Fasting venous glucose is unreliable in haemolytic anaemia",
            "He has benign renal glycosuria rather than diabetes",
            "HbA1c only detects post-prandial hyperglycaemia"
        ],
        "correct_answer": "Shortened red cell lifespan in spherocytosis causes a falsely low HbA1c",
        "explanation": "HbA1c reflects glucose exposure over the normal 120-day red cell lifespan. Conditions that shorten red cell survival—such as haemolytic anaemias (hereditary spherocytosis, sickle cell, G6PD deficiency) or blood loss—produce a falsely low HbA1c that can mask diabetes."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "An asymptomatic 29-year-old man has persistent mild hypercalcaemia (2.81 mmol/L), mildly low phosphate (0.76 mmol/L), normal renal function and vitamin D, and an unsuppressed PTH of 6.8 pmol/L (1.6–6.9). His 24-hour urinary calcium-to-creatinine clearance ratio is 0.006. What is the diagnosis?",
        "options": [
            "Familial hypocalciuric hypercalcaemia",
            "Primary hyperparathyroidism (parathyroid adenoma)",
            "Tertiary hyperparathyroidism",
            "Humoral hypercalcaemia of malignancy",
            "Vitamin D toxicity"
        ],
        "correct_answer": "Familial hypocalciuric hypercalcaemia",
        "explanation": "Both primary hyperparathyroidism and familial hypocalciuric hypercalcaemia (FHH) cause hypercalcaemia with elevated or unsuppressed PTH. FHH (an inactivating CaSR mutation) causes avid renal calcium reabsorption, giving a urinary calcium-to-creatinine clearance ratio <0.01 and sparing the patient unnecessary parathyroidectomy."
    },

    # ==========================================
    # GASTROENTEROLOGY / CLINICAL NUTRITION (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 76-year-old woman with atrial fibrillation who stopped apixaban 3 weeks ago presents with 3 hours of sudden, agonising central abdominal pain. She is writhing in pain (HR 118 bpm, AF), yet her abdomen is soft with minimal tenderness. ABG shows pH 7.26 and lactate 6.4 mmol/L. What is the definitive diagnostic test?",
        "options": [
            "Urgent CT angiography of the abdomen",
            "Erect chest X-ray and plain abdominal X-ray",
            "Urgent upper GI endoscopy",
            "Abdominal ultrasound of the biliary tree",
            "Serum amylase and conservative fluid therapy"
        ],
        "correct_answer": "Urgent CT angiography of the abdomen",
        "explanation": "Severe abdominal pain out of proportion to examination findings in a patient with unanticoagulated AF and lactic acidosis is classic for acute mesenteric ischaemia (typically superior mesenteric artery embolism). Triphasic CT angiography is the definitive investigation."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 23-year-old student develops mild scleral icterus while recovering from a viral cold and skipping meals. He has normal-coloured urine and stools. Bloods show: total bilirubin 54 µmol/L, conjugated bilirubin 6 µmol/L, normal ALT/ALP, Hb 152 g/L, and reticulocytes 1.1%. What is the next step?",
        "options": [
            "Reassure him that this is benign Gilbert's syndrome requiring no treatment",
            "Arrange an urgent MRCP to exclude bile duct stones",
            "Request a direct antiglobulin (Coombs) test",
            "Perform an outpatient liver biopsy",
            "Start oral ursodeoxycholic acid"
        ],
        "correct_answer": "Reassure him that this is benign Gilbert's syndrome requiring no treatment",
        "explanation": "Isolated unconjugated hyperbilirubinaemia with normal liver enzymes and no haemolysis (normal Hb and reticulocytes) triggered by fasting or viral illness is classic for Gilbert's syndrome (reduced hepatic UGT1A1 activity). Reassurance is all that is needed."
    },

    # ==========================================
    # INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 38-year-old woman presents with a painless, expanding 8 cm annular red rash with central clearing behind her knee, 12 days after a tick bite in the New Forest. She has mild myalgia and no neurological or cardiac features. Under NICE guidelines, what is the management?",
        "options": [
            "Diagnose Lyme disease clinically and start oral doxycycline for 21 days without waiting for serology",
            "Request Borrelia ELISA serology and withhold antibiotics until confirmed",
            "Prescribe topical terbinafine cream for 2 weeks",
            "Prescribe oral flucloxacillin for 7 days",
            "Give a single prophylactic 200 mg dose of doxycycline"
        ],
        "correct_answer": "Diagnose Lyme disease clinically and start oral doxycycline for 21 days without waiting for serology",
        "explanation": "Erythema migrans is a clinical diagnosis of Lyme disease (*Borrelia burgdorferi*). NICE advises starting oral doxycycline (100 mg twice daily for 21 days) immediately without waiting for serology, as early antibody tests have a high false-negative rate."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 63-year-old man has intense generalized itching after hot showers, burning red toes relieved by aspirin, facial plethora, and splenomegaly (SpO2 98%). Bloods show: Hb 196 g/L, Hct 0.58, WCC 13.4 × 10⁹/L, platelets 540 × 10⁹/L, and low serum EPO. Which mutation is present in >95% of cases?",
        "options": [
            "JAK2 V617F mutation",
            "BCR-ABL1 fusion gene",
            "CALR exon 9 mutation",
            "HFE C282Y homozygosity",
            "Factor V Leiden mutation"
        ],
        "correct_answer": "JAK2 V617F mutation",
        "explanation": "Aquagenic pruritus, erythromelalgia, splenomegaly, pancytosis (raised Hb, WCC, and platelets), and suppressed serum EPO indicate polycythaemia vera (PV). Over 95% of PV cases are driven by an activating *JAK2* V617F mutation causing EPO-independent erythroid proliferation."
    },

    # ==========================================
    # MUSCULOSKELETAL (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 26-year-old man has 8 months of lower back and alternating buttock pain that wakes him in the second half of the night, with 60 minutes of morning stiffness that improves with cycling. He had anterior uveitis last year. Pelvic and lumbar X-rays are normal. What is the next step?",
        "options": [
            "Refer to rheumatology for suspected axial spondyloarthritis (and MRI of sacroiliac joints)",
            "Reassure him that normal X-rays exclude ankylosing spondylitis and refer for physiotherapy",
            "Arrange an emergency lumbar MRI to exclude cauda equina syndrome",
            "Request rheumatoid factor and anti-CCP antibodies",
            "Advise bed rest and prescribe modified-release morphine"
        ],
        "correct_answer": "Refer to rheumatology for suspected axial spondyloarthritis (and MRI of sacroiliac joints)",
        "explanation": "Inflammatory back pain (<45 years, >3 months, night pain, morning stiffness >30 min easing with exercise) plus anterior uveitis strongly suggests axial spondyloarthritis. Plain X-rays are often normal for years; NICE advises rheumatology referral for sacroiliac/spinal MRI."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 68-year-old man with type 2 diabetes presents with 24 hours of a hot, swollen, agonising native right knee, fever (38.8°C), and inability to tolerate any passive joint movement. What is the most important investigation before starting empirical IV antibiotics?",
        "options": [
            "Urgent synovial fluid aspiration for microscopy, Gram stain, crystals, and culture",
            "Plain AP and lateral radiographs of the right knee",
            "Serum uric acid level",
            "MRI of the right knee to exclude osteomyelitis",
            "C-reactive protein and ESR"
        ],
        "correct_answer": "Urgent synovial fluid aspiration for microscopy, Gram stain, crystals, and culture",
        "explanation": "An acutely hot, swollen monoarthritis with restricted passive movement is septic arthritis until proven otherwise. In a native joint, urgent needle aspiration (arthrocentesis) must be performed *before* starting empirical IV antibiotics so synovial fluid cultures are not sterilised."
    },

    # ==========================================
    # PAEDIATRICS (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old boy presents 10 days after a cold with symmetrical palpable purpura over his buttocks and legs, ankle arthralgia, and colicky abdominal pain. BP is 96/60 mmHg, platelets are 310 × 10⁹/L, and urine dipstick is negative. What follow-up is essential?",
        "options": [
            "Regular urine dipstick and blood pressure monitoring for at least 6 months",
            "Urgent bone marrow biopsy to exclude leukaemia",
            "A 14-day course of oral prednisolone to prevent nephritis",
            "Immediate intramuscular benzylpenicillin",
            "Prophylactic platelet transfusion"
        ],
        "correct_answer": "Regular urine dipstick and blood pressure monitoring for at least 6 months",
        "explanation": "Palpable purpura on the buttocks/legs with normal platelets, arthralgia, and abdominal pain indicates Henoch-Schönlein purpura (IgA vasculitis). Because HSP nephritis can develop weeks to months later, all children require urine dipstick and BP monitoring for 6–12 months."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 5-month-old infant presents in November with 3 days of coryza, dry wheezy cough, RR 46/min, SpO2 96% in air, mild subcostal recession, and widespread fine crackles and wheeze. He is alert and taking 75% of his normal feeds. Under NICE guidelines, what is the management?",
        "options": [
            "Supportive home care with smaller, more frequent feeds and red-flag safety-netting",
            "Inhaled salbutamol via a spacer",
            "Oral amoxicillin for 5 days",
            "Single dose of oral dexamethasone",
            "Immediate hospital admission for NG feeding and oxygen"
        ],
        "correct_answer": "Supportive home care with smaller, more frequent feeds and red-flag safety-netting",
        "explanation": "Coryza followed by cough, fine crackles, and wheeze in an infant <1 year indicates viral bronchiolitis. With SpO2 >=92%, feeds >=50–75% of normal, and no apnoea or severe distress, management is supportive at home (smaller, frequent feeds). Salbutamol, steroids, and antibiotics are not recommended."
    },

    # ==========================================
    # PSYCHIATRY / NEUROLOGY (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 54-year-old man with alcohol dependence is brought in confused with an ataxic gait, horizontal nystagmus, and bilateral sixth nerve palsies. His capillary blood glucose is 2.9 mmol/L. What is the correct immediate IV treatment sequence?",
        "options": [
            "Give high-dose IV thiamine (Pabrinex) before or concurrently with IV glucose",
            "Give 20% IV dextrose immediately, then oral thiamine tomorrow",
            "Give IV chlordiazepoxide alone and withhold glucose",
            "Give IV naloxone followed by 0.9% sodium chloride",
            "Give IV phenytoin and arrange an urgent CT head"
        ],
        "correct_answer": "Give high-dose IV thiamine (Pabrinex) before or concurrently with IV glucose",
        "explanation": "Confusion, ataxia, and ophthalmoplegia/nystagmus form the triad of Wernicke's encephalopathy (thiamine deficiency). Thiamine is a cofactor for glucose metabolism; giving IV glucose before thiamine exhausts remaining B1 stores and precipitates irreversible Korsakoff's psychosis."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 27-year-old man presents with 5 weeks of depression requesting an antidepressant. Collateral history reveals a 9-day episode 8 months ago of sleeping 2 hours/night with boundless energy, pressured speech, reckless spending, and grandiose delusions. What is the appropriate management?",
        "options": [
            "Avoid antidepressant monotherapy and refer to secondary care mental health for suspected bipolar disorder",
            "Start oral sertraline 50 mg daily and review in 2 weeks",
            "Start oral amitriptyline 75 mg nightly for insomnia",
            "Start lithium carbonate immediately in primary care without referral",
            "Reassure him and refer for low-intensity CBT only"
        ],
        "correct_answer": "Avoid antidepressant monotherapy and refer to secondary care mental health for suspected bipolar disorder",
        "explanation": "A past 9-day episode of reduced sleep need, pressured speech, reckless spending, and grandiose delusions indicates prior mania (Bipolar I disorder). Unopposed antidepressant monotherapy risks triggering a manic switch or rapid cycling; NICE advises specialist referral."
    },

    # ==========================================
    # RENAL / UROLOGY (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 71-year-old man with AKI on ramipril and spironolactone has a serum potassium of 7.1 mmol/L. His ECG shows absent P waves, tall tented T waves, and QRS widening to 156 ms. Which IV medication must be given first?",
        "options": [
            "10 mL of 10% calcium gluconate",
            "10 units soluble insulin in 50 mL 20% glucose",
            "Nebulised salbutamol 10 mg",
            "Oral sodium zirconium cyclosilicate",
            "Intravenous furosemide 80 mg"
        ],
        "correct_answer": "10 mL of 10% calcium gluconate",
        "explanation": "In severe hyperkalaemia (K+ >=6.5 mmol/L) with toxic ECG changes (absent P waves, tented T waves, QRS widening), the immediate life-saving step is myocardial membrane stabilisation with IV 10% calcium gluconate (or calcium chloride), followed by insulin-dextrose to shift K+ intracellularly."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 48-year-old ex-smoker presents after passing painless, frankly blood-stained urine twice this week. She has no UTI symptoms, and urine culture shows red cells with no bacterial growth. Under NICE NG12 guidelines, what is the next step?",
        "options": [
            "Urgent 2-week wait urological cancer referral",
            "Prescribe 3 days of nitrofurantoin and repeat dipstick",
            "Reassure and repeat urine microscopy in 6 months",
            "Routine referral to nephrology",
            "Request serum CA-125 and pelvic ultrasound"
        ],
        "correct_answer": "Urgent 2-week wait urological cancer referral",
        "explanation": "Under NICE NG12, patients aged >=45 with unexplained visible haematuria without UTI (or visible haematuria persisting/recurring after UTI treatment) require an urgent 2-week wait urological cancer referral to exclude bladder or renal malignancy."
    },

    # ==========================================
    # REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A healthy, non-smoking 24-year-old woman (BP 112/70 mmHg, BMI 22) requests the combined oral contraceptive pill (COCP). Twice a year, she gets unilateral headaches preceded by 25 minutes of shimmering zig-zag visual lines. How does UKMEC classify the COCP for her?",
        "options": [
            "UKMEC Category 4 (absolute contraindication)",
            "UKMEC Category 3 (risks generally outweigh benefits)",
            "UKMEC Category 2 (benefits generally outweigh risks)",
            "UKMEC Category 1 (no restriction)",
            "Safe if a 20 mcg low-oestrogen pill is used"
        ],
        "correct_answer": "UKMEC Category 4 (absolute contraindication)",
        "explanation": "Migraine *with aura* at any age is a UKMEC Category 4 (absolute contraindication) for all combined hormonal contraception due to the synergistically increased risk of ischaemic stroke from ethinylestradiol. Progestogen-only methods remain safe."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 31-year-old woman at 33 weeks gestation presents with intense nocturnal itching of her palms and soles. Fetal movements, BP (118/72 mmHg), and urine dipstick are normal, and examination shows only scratch excoriations with no primary rash. What is the key diagnostic test?",
        "options": [
            "Serum bile acids and liver function tests",
            "Skin scraping for microscopy in potassium hydroxide",
            "24-hour urinary protein and serum uric acid",
            "Fasting venous plasma glucose",
            "Cutaneous patch testing"
        ],
        "correct_answer": "Serum bile acids and liver function tests",
        "explanation": "Third-trimester palmar and plantar nocturnal pruritus without a primary rash indicates intrahepatic cholestasis of pregnancy (ICP). Serum total bile acids (>=19 µmol/L) and LFTs confirm the diagnosis; severe elevation (>=100 µmol/L) increases stillbirth risk and guides planned delivery."
    },

    # ==========================================
    # RESPIRATORY (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 28-year-old woman with childhood eczema presents with 4 months of episodic nocturnal cough and wheeze after cold-air exercise. Her chest is clear in clinic. Under NICE guidelines, how should suspected asthma be diagnosed?",
        "options": [
            "Objective testing (blood eosinophils or FeNO, and bronchodilator reversibility spirometry)",
            "A 6-week empirical trial of an inhaled corticosteroid",
            "Clinical history alone and a salbutamol inhaler",
            "High-resolution CT scan of the thorax",
            "Clinic room-air arterial blood gas"
        ],
        "correct_answer": "Objective testing (blood eosinophils or FeNO, and bronchodilator reversibility spirometry)",
        "explanation": "Under joint BTS/NICE/SIGN asthma guidelines, asthma should not be diagnosed on history alone or via an inhaler 'trial of treatment'. Objective testing of airway inflammation (eosinophils or FeNO) and airflow variability (bronchodilator reversibility spirometry or PEF) is required."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 64-year-old heavy smoker presents with 2 weeks of breathlessness, morning facial and periorbital swelling, headaches worse on stooping, dilated chest wall veins, and a fixed, non-pulsatile JVP raised at 9 cm. What is the underlying cause?",
        "options": [
            "Superior vena cava obstruction from lung cancer or mediastinal lymphadenopathy",
            "Cardiac tamponade from a malignant pericardial effusion",
            "Acute right ventricular infarction",
            "Pancoast tumour invading the sympathetic chain",
            "Tension pneumothorax"
        ],
        "correct_answer": "Superior vena cava obstruction from lung cancer or mediastinal lymphadenopathy",
        "explanation": "Morning facial/periorbital oedema, plethora, stooping headaches, chest wall collateral veins, and a **fixed, non-pulsatile** raised JVP indicate superior vena cava obstruction (SVCO)—most commonly caused by bronchogenic carcinoma or lymphoma."
    },

    # ==========================================
    # PHARMACOLOGY (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A sexually active 22-year-old woman has juvenile myoclonic epilepsy controlled only on sodium valproate after other antiepileptics failed. Under MHRA safety regulations, what is mandatory if valproate is continued?",
        "options": [
            "Enrolment in the Pregnancy Prevention Programme (LARC contraception and Annual Risk Acknowledgement Form)",
            "Immediate switch to phenytoin in primary care",
            "Low-dose folic acid 400 mcg daily instead of contraception",
            "Monthly serum valproate trough levels",
            "Stopping valproate only after a positive pregnancy test"
        ],
        "correct_answer": "Enrolment in the Pregnancy Prevention Programme (LARC contraception and Annual Risk Acknowledgement Form)",
        "explanation": "Valproate carries a ~10% congenital malformation risk and a 30–40% neurodevelopmental disorder risk. MHRA mandates enrolment in the Pregnancy Prevention Programme (PPP), requiring highly effective contraception (ideally LARC) and a signed Annual Risk Acknowledgement Form."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 74-year-old woman on once-daily IV gentamicin for urosepsis has a pre-dose trough level of 2.4 mg/L (target <1.0 mg/L) at 20 hours, with creatinine rising from 88 to 124 µmol/L. How should her gentamicin regimen be adjusted?",
        "options": [
            "Withhold the next dose and extend the dosing interval until the trough is <1.0 mg/L",
            "Give the next dose on time but halve the milligram dose",
            "Double the infusion rate to increase peak concentration",
            "Continue the same 24-hourly dose as high troughs aid killing",
            "Add IV furosemide to flush gentamicin renally"
        ],
        "correct_answer": "Withhold the next dose and extend the dosing interval until the trough is <1.0 mg/L",
        "explanation": "Aminoglycosides use peak concentration for bacterial killing, whereas nephrotoxicity and irreversible ototoxicity correlate with persistently raised trough levels. When the trough is high (>1.0 mg/L), withhold the next dose and extend the dosing interval."
    },

    # ==========================================
    # PROFESSIONAL DILEMMAS - RANKING (8 Questions)
    # ==========================================
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a GP. A self-employed delivery driver who had a first unprovoked tonic-clonic seizure 2 weeks ago admits he has ignored hospital advice to stop driving and notify the DVLA because he cannot afford to lose income. Despite your explanation of the risks, he refuses to stop driving.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Inform him that if he continues driving, you must disclose his condition to the DVLA, and urge him one final time to self-report.",
            "Explore whether non-driving work or financial support is available and document the discussion thoroughly.",
            "Seek prompt advice from your Caldicott Guardian or defence union on making a public-interest disclosure.",
            "Call 999 immediately to have him arrested in the waiting room.",
            "Take no further action to avoid breaching patient confidentiality."
        ],
        "correct_answer": [
            "Inform him that if he continues driving, you must disclose his condition to the DVLA, and urge him one final time to self-report.",
            "Explore whether non-driving work or financial support is available and document the discussion thoroughly.",
            "Seek prompt advice from your Caldicott Guardian or defence union on making a public-interest disclosure.",
            "Call 999 immediately to have him arrested in the waiting room.",
            "Take no further action to avoid breaching patient confidentiality."
        ],
        "explanation": "Under GMC DVLA guidance: (1) Explain clearly that you will have to notify the DVLA if he does not stop driving and self-report. (2) Explore practical/financial support and document fully. (3) Consult your Caldicott Guardian/defence union regarding disclosure. (4) Calling 999 for waiting-room arrest is disproportionate unless there is an acute crisis. (5) Doing nothing is least appropriate, as public safety overrides confidentiality."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 on an elderly care ward. An 84-year-old man recovering from pneumonia with mild resolving delirium becomes agitated and refuses his routine morning blood tests. Yesterday's results showed falling inflammatory markers and stable renal function.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Check if today's blood test is clinically necessary and speak calmly with the patient to understand his refusal.",
            "If the test is needed, assess decision-specific capacity and re-offer it later with a familiar nurse or relative present.",
            "Discuss stepping down daily routine bloods to every 48–72 hours with the registrar.",
            "Tell the patient his oral antibiotics will be stopped unless he allows the blood test.",
            "Ask two staff members to hold his arm down to take the sample quickly."
        ],
        "correct_answer": [
            "Check if today's blood test is clinically necessary and speak calmly with the patient to understand his refusal.",
            "If the test is needed, assess decision-specific capacity and re-offer it later with a familiar nurse or relative present.",
            "Discuss stepping down daily routine bloods to every 48–72 hours with the registrar.",
            "Tell the patient his oral antibiotics will be stopped unless he allows the blood test.",
            "Ask two staff members to hold his arm down to take the sample quickly."
        ],
        "explanation": "(1) First verify whether today's routine blood test is even necessary and speak respectfully with the patient. (2) If needed, assess capacity and use the least restrictive approach (calmer timing/familiar staff). (3) Rationalise ongoing blood frequency with your senior. (4) Threatening to withhold antibiotics is coercive. (5) Restraining an agitated patient for routine bloods is disproportionate and unlawful."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a ward FY2. A distressed nurse tells you she gave a 78-year-old woman 320 mg of gliclazide instead of 80 mg 30 minutes ago because your handwritten drug chart entry was unclear.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Assess the patient immediately, check her capillary glucose, and start serial glucose monitoring with carbohydrate/IV dextrose cover.",
            "Rewrite the drug chart clearly and inform your medical registrar of the error and monitoring plan.",
            "Apologise openly to the patient, explain the error and monitoring plan (Duty of Candour), and submit a Datix.",
            "Advise the nurse not to mention the error to the patient unless hypoglycaemia develops.",
            "Scrub out the original prescription heavily in black ink so your handwriting cannot be identified."
        ],
        "correct_answer": [
            "Assess the patient immediately, check her capillary glucose, and start serial glucose monitoring with carbohydrate/IV dextrose cover.",
            "Rewrite the drug chart clearly and inform your medical registrar of the error and monitoring plan.",
            "Apologise openly to the patient, explain the error and monitoring plan (Duty of Candour), and submit a Datix.",
            "Advise the nurse not to mention the error to the patient unless hypoglycaemia develops.",
            "Scrub out the original prescription heavily in black ink so your handwriting cannot be identified."
        ],
        "explanation": "(1) Patient safety comes first: sulfonylurea overdose causes prolonged hypoglycaemia, requiring immediate bedside assessment and serial glucose monitoring. (2) Correct the chart and escalate to your senior. (3) Fulfil the Duty of Candour and submit a Datix. (4) Concealing errors breaches honesty. (5) Falsifying/obliterating records is a severe probity breach."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "At 03:00 on a night shift, you stop an FY1 colleague from drawing up undiluted concentrated potassium chloride (KCl) as an IV bolus. He breaks down crying, revealing his father died 3 days ago, he has barely slept, and he cannot concentrate.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Support the FY1, ask him to step down from clinical duties immediately, and contact the night registrar and site manager for cover.",
            "Review the other prescriptions and clinical tasks the FY1 completed earlier on the shift.",
            "Arrange safe transport home (e.g. a taxi) and encourage him to contact his Educational Supervisor and GP.",
            "Tell him to take a 20-minute coffee break and only clerk stable patients for the rest of the night.",
            "Refer the FY1 to the GMC tonight for nearly administering a Never Event bolus."
        ],
        "correct_answer": [
            "Support the FY1, ask him to step down from clinical duties immediately, and contact the night registrar and site manager for cover.",
            "Review the other prescriptions and clinical tasks the FY1 completed earlier on the shift.",
            "Arrange safe transport home (e.g. a taxi) and encourage him to contact his Educational Supervisor and GP.",
            "Tell him to take a 20-minute coffee break and only clerk stable patients for the rest of the night.",
            "Refer the FY1 to the GMC tonight for nearly administering a Never Event bolus."
        ],
        "explanation": "(1) An acutely bereaved, exhausted doctor who just had a Never Event near-miss is unsafe to work: relieve him immediately and arrange night cover. (2) Check his earlier shift tasks to protect patients. (3) Ensure safe travel home and pastoral support. (4) Keeping him working after a brief break leaves patients at risk. (5) Immediate punitive GMC referral is inappropriate."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a male GP trainee. A 32-year-old woman requests a chaperone for a speculum examination, but all trained chaperones are busy for the next 30 minutes. She says, 'Just go ahead without one so I don't miss my bus.'\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Explain that for mutual safety and comfort, it is best to either wait 30 minutes for a chaperone or rebook a priority slot.",
            "Complete the history, STI risk assessment, and any blood/ultrasound requests now so the visit remains productive.",
            "Speak to the practice manager after clinic about improving chaperone availability.",
            "Proceed with the intimate examination alone after asking her to sign a waiver in the notes.",
            "Ask another patient in the waiting room to step in as an informal chaperone."
        ],
        "correct_answer": [
            "Explain that for mutual safety and comfort, it is best to either wait 30 minutes for a chaperone or rebook a priority slot.",
            "Complete the history, STI risk assessment, and any blood/ultrasound requests now so the visit remains productive.",
            "Speak to the practice manager after clinic about improving chaperone availability.",
            "Proceed with the intimate examination alone after asking her to sign a waiver in the notes.",
            "Ask another patient in the waiting room to step in as an informal chaperone."
        ],
        "explanation": "Under GMC chaperone guidance: (1) For a non-urgent intimate exam where a chaperone was requested, wait for a trained chaperone or rebook rather than letting time pressure force an unchaperoned exam. (2) Complete non-intimate elements of care now. (3) Address the staffing gap with management. (4) Proceeding alone with a 'waiver' is unsafe. (5) Using a stranger from the waiting room breaches confidentiality."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "At 16:30 on Friday, a bed manager pressures you to sign the discharge for a 72-year-old man with COPD to free a bed. On reviewing him, you find his RR is 26/min, SpO2 has dropped to 85% on air (baseline 91%), and he is acutely breathless.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Cancel the discharge, start controlled oxygen (88–92%) and acute medical reassessment, and inform the bed manager he is unsafe to go.",
            "Inform your respiratory registrar or consultant of his deterioration and cancelled discharge.",
            "Update the patient and his family on why he must stay in hospital.",
            "Sign the discharge summary as requested, but tell the patient to call 999 if breathless at home.",
            "Argue loudly with the bed manager in the ward bay about hospital targets."
        ],
        "correct_answer": [
            "Cancel the discharge, start controlled oxygen (88–92%) and acute medical reassessment, and inform the bed manager he is unsafe to go.",
            "Inform your respiratory registrar or consultant of his deterioration and cancelled discharge.",
            "Update the patient and his family on why he must stay in hospital.",
            "Sign the discharge summary as requested, but tell the patient to call 999 if breathless at home.",
            "Argue loudly with the bed manager in the ward bay about hospital targets."
        ],
        "explanation": "(1) Patient safety overrides bed pressures: treat the acute hypoxia (controlled oxygen 88–92%, ABG, review) and cancel the unsafe discharge. (2) Escalate to your senior team. (3) Keep the patient and family informed. (4) Discharging an acutely hypoxic patient is negligent. (5) Publicly arguing in the ward bay is unprofessional."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "A 74-year-old woman with full capacity has a CT scan showing metastatic pancreatic cancer. Outside her room, her son begs you not to tell her it is cancer and asks you to tell him the results instead while telling her it is gallstones.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Acknowledge the son's distress empathetically, but explain you cannot deceive a capacitous patient or share her results without her consent.",
            "Speak sensitively with the patient, check how much detail she wants to know, and ask if she wants her son present.",
            "Arrange support from the hepatobiliary clinical nurse specialist for the patient and family.",
            "Give the son the full CT report in the corridor first to calm him down.",
            "Agree to the son's request and tell the patient she only has benign gallstones."
        ],
        "correct_answer": [
            "Acknowledge the son's distress empathetically, but explain you cannot deceive a capacitous patient or share her results without her consent.",
            "Speak sensitively with the patient, check how much detail she wants to know, and ask if she wants her son present.",
            "Arrange support from the hepatobiliary clinical nurse specialist for the patient and family.",
            "Give the son the full CT report in the corridor first to calm him down.",
            "Agree to the son's request and tell the patient she only has benign gallstones."
        ],
        "explanation": "(1) Respond empathetically to the son while maintaining clear ethical boundaries: a capacitous patient has a right to honesty and confidentiality. (2) Explore the patient's wishes on information and family presence. (3) Involve the specialist nurse. (4) Disclosing results in the corridor without consent breaches confidentiality. (5) Lying to a capacitous patient breaches autonomy and probity."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a vascular FY1. Ten minutes before theatre, your consultant asks you to take written consent from a patient for a complex fenestrated endovascular aneurysm repair (fEVAR), a procedure you have never seen and do not understand.\n\nRank the appropriateness of the following actions (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Explain to the consultant that you are not trained to take valid consent for fEVAR and ask the consultant or registrar to consent him.",
            "Offer to accompany the consultant or registrar during the consent discussion so you can learn.",
            "Check that the patient's admissions paperwork, observations, group & save, and bloods are ready for theatre.",
            "Look up fEVAR on your phone and take written consent yourself.",
            "Ask the patient to sign a blank consent form for the consultant to fill in later."
        ],
        "correct_answer": [
            "Explain to the consultant that you are not trained to take valid consent for fEVAR and ask the consultant or registrar to consent him.",
            "Offer to accompany the consultant or registrar during the consent discussion so you can learn.",
            "Check that the patient's admissions paperwork, observations, group & save, and bloods are ready for theatre.",
            "Look up fEVAR on your phone and take written consent yourself.",
            "Ask the patient to sign a blank consent form for the consultant to fill in later."
        ],
        "explanation": "Under GMC consent guidance: (1) Delegated consent may only be taken by someone suitably trained who understands the procedure's risks and alternatives—decline politely outside your competence. (2) Offer to shadow the consent discussion. (3) Expedite pre-op checks within your competence. (4) Guessing risks from a phone search invalidates consent. (5) Signing a blank form is unlawful."
    },

    # ==========================================
    # PROFESSIONAL DILEMMAS - SELECTION (8 Questions)
    # ==========================================
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A 14-month-old boy presents with a spiral humerus fracture. His mother and her partner give conflicting accounts of how it happened 2 days ago, and full examination reveals three oval bruises over his lumbar spine and lower ribs.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Escalate immediately to the paediatric registrar/consultant and the hospital safeguarding team.",
            "Admit the child to the paediatric ward as a place of safety for child protection assessment.",
            "Document both histories verbatim and map the exact size, colour, and site of all bruises in the notes.",
            "Accuse the partner directly of child abuse and demand a confession.",
            "Discharge the child home in a sling with fracture clinic follow-up in 1 week.",
            "Examine only the arm and avoid undressing the toddler.",
            "Promise the mother you will not involve Children's Social Care.",
            "Wait 6 weeks until the fracture heals before raising safeguarding concerns."
        ],
        "correct_answer": [
            "Escalate immediately to the paediatric registrar/consultant and the hospital safeguarding team.",
            "Admit the child to the paediatric ward as a place of safety for child protection assessment.",
            "Document both histories verbatim and map the exact size, colour, and site of all bruises in the notes."
        ],
        "explanation": "A spiral humeral fracture in a toddler with delayed presentation, conflicting histories, and torso bruising strongly suggests non-accidental injury (NAI). You must: (1) escalate immediately to senior paediatrics and safeguarding, (2) admit to a place of safety, and (3) record verbatim histories and a detailed body map."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "While taking an arterial blood gas from a capacitous 34-year-old man with a history of intravenous drug use, your finger is punctured deeply by the used hollow-bore needle.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Encourage gentle bleeding under running warm water and wash with soap without scrubbing.",
            "Report immediately to Occupational Health (or ED out of hours) for BBV risk assessment and PEP.",
            "Ask another clinician to approach the patient for informed consent to test his blood for HIV, HBV, and HCV.",
            "Send blood from the patient's arterial line for HIV testing without telling him.",
            "Wait 3 months to see if symptoms develop before reporting.",
            "Scrub the puncture wound vigorously with neat bleach.",
            "Test the blood already in the ABG syringe for HIV without consent.",
            "Refuse to treat any further patients with substance misuse."
        ],
        "correct_answer": [
            "Encourage gentle bleeding under running warm water and wash with soap without scrubbing.",
            "Report immediately to Occupational Health (or ED out of hours) for BBV risk assessment and PEP.",
            "Ask another clinician to approach the patient for informed consent to test his blood for HIV, HBV, and HCV."
        ],
        "explanation": "After a needle-stick injury: (1) encourage gentle bleeding under running water and wash with soap, (2) contact Occupational Health/ED immediately (HIV PEP is best started within 1 hour), and (3) ask a colleague (not yourself) to seek the source patient's explicit consent for HIV/HBV/HCV serology."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "Halfway through a GP consultation with a 58-year-old man discussing newly diagnosed heart failure, you notice his smartphone on the desk is covertly audio-recording the conversation.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Acknowledge the recording calmly and ask what prompted him to record the consultation.",
            "Reassure him that personal recording is welcome to help remember advice, and offer a written summary.",
            "Continue the consultation professionally and note in the medical record that it was audio-recorded.",
            "Demand he delete the recording before you prescribe his heart failure medication.",
            "Terminate the appointment immediately and remove him from the practice list.",
            "Call security to confiscate his phone under the Data Protection Act.",
            "Communicate only by typing on your screen for the rest of the consultation.",
            "Threaten legal action for recording without permission."
        ],
        "correct_answer": [
            "Acknowledge the recording calmly and ask what prompted him to record the consultation.",
            "Reassure him that personal recording is welcome to help remember advice, and offer a written summary.",
            "Continue the consultation professionally and note in the medical record that it was audio-recorded."
        ],
        "explanation": "Consultation information is the patient's own personal data, and patients usually record out of anxiety or fear of forgetting complex advice. You should: (1) address it calmly and explore why, (2) reassure him open recording is fine and offer written leaflets, and (3) continue care professionally while documenting the recording."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A police officer in the Emergency Department asks for the names, addresses, and notes of all patients treated for a dog bite in the last 48 hours after a local resident was bitten in a park. The officer has no court order or patient consent.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Politely decline to release patient details or records without patient consent or a court order.",
            "Explain that disclosure without consent only applies to prevent or detect very serious crime (risk of death or serious harm).",
            "Consult the ED consultant or Caldicott Guardian and document the police request.",
            "Print the last 48 hours of ED attendances and hand it to the officer.",
            "Give the names and phone numbers verbally so there is no paper trail.",
            "Leave the computer screen unlocked showing the dog-bite records while you get coffee.",
            "Tell the officer doctors can never speak to police even with a court order.",
            "Phone the patients and threaten them with arrest if they do not contact police."
        ],
        "correct_answer": [
            "Politely decline to release patient details or records without patient consent or a court order.",
            "Explain that disclosure without consent only applies to prevent or detect very serious crime (risk of death or serious harm).",
            "Consult the ED consultant or Caldicott Guardian and document the police request."
        ],
        "explanation": "Police have no automatic right to patient records without consent or a court order unless public-interest disclosure is justified by a risk of death or very serious harm (e.g. gun/knife crime). You should: (1) politely decline disclosure, (2) explain the threshold, and (3) consult your consultant/Caldicott Guardian and document."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "On Instagram, you see a public story posted 20 minutes ago by a medical student on your firm. Behind him at the nurses' station, the ward whiteboard is legible, showing patients' full names and diagnoses.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Contact the student privately right away, explain that patient details are visible, and ask him to delete the post immediately.",
            "Inform your clinical supervisor and log the data breach via the hospital incident system (Datix).",
            "Discuss GMC social media and confidentiality guidance with the student.",
            "Comment publicly on the post listing which patients' names are visible.",
            "Screenshot the post and share it in the junior doctors' WhatsApp group.",
            "Ignore it because Instagram stories expire after 24 hours.",
            "Tell the ward sister that you took the photo to protect the student.",
            "Wipe the names off the physical ward whiteboard so they no longer match."
        ],
        "correct_answer": [
            "Contact the student privately right away, explain that patient details are visible, and ask him to delete the post immediately.",
            "Inform your clinical supervisor and log the data breach via the hospital incident system (Datix).",
            "Discuss GMC social media and confidentiality guidance with the student."
        ],
        "explanation": "Visible patient data on social media is a serious confidentiality breach. You must: (1) contact the student privately to delete the post immediately, (2) escalate to your supervisor and file an information governance Datix, and (3) educate the student on GMC social media rules."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "In pre-op clinic for an elective hip replacement in 2 weeks, a capacitous 62-year-old Jehovah's Witness presents a valid Advance Decision (ADRT) refusing all blood products even if her life is at risk. Her Hb is 108 g/L with MCV 74 fL and low ferritin.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Respect her refusal, place her ADRT in the notes, and clarify which blood-conservation methods (e.g. cell salvage, tranexamic acid) she accepts.",
            "Optimise her preoperative haemoglobin by treating her iron-deficiency anaemia.",
            "Alert the consultant surgeon and anaesthetist early to agree a bloodless-surgery perioperative plan.",
            "Tell her the anaesthetist will override her ADRT if life-threatening bleeding occurs in theatre.",
            "Ask her husband to consent to transfusion once she is anaesthetised.",
            "Section her under the Mental Health Act so she can be transfused.",
            "Cancel her operation permanently without consultant discussion.",
            "Transfuse red cells in an opaque bag labelled as saline."
        ],
        "correct_answer": [
            "Respect her refusal, place her ADRT in the notes, and clarify which blood-conservation methods (e.g. cell salvage, tranexamic acid) she accepts.",
            "Optimise her preoperative haemoglobin by treating her iron-deficiency anaemia.",
            "Alert the consultant surgeon and anaesthetist early to agree a bloodless-surgery perioperative plan."
        ],
        "explanation": "A valid ADRT in a capacitous adult is legally binding. You should: (1) respect and document her ADRT and check acceptable blood-sparing techniques (cell salvage, tranexamic acid), (2) treat her preoperative iron-deficiency anaemia, and (3) involve the consultant surgeon and anaesthetist early."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "On discharge after an acute MI, a grateful businessman hands you an envelope containing £500 in cash and insists you use it for a holiday.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Thank him warmly, but politely decline the cash gift, explaining GMC and trust rules on personal gifts.",
            "Explain that he is welcome to donate to the official hospital charity or ward fund if he wishes.",
            "Inform your clinical supervisor and document the offered gift and refusal in the notes/gift register.",
            "Accept the £500 quietly so you do not offend him.",
            "Accept the cash in exchange for giving him your personal mobile number.",
            "Keep £100 and put £400 in the staff room biscuit tin.",
            "Withhold his discharge medications until he takes the envelope back.",
            "Ask him to send the £500 by bank transfer instead."
        ],
        "correct_answer": [
            "Thank him warmly, but politely decline the cash gift, explaining GMC and trust rules on personal gifts.",
            "Explain that he is welcome to donate to the official hospital charity or ward fund if he wishes.",
            "Inform your clinical supervisor and document the offered gift and refusal in the notes/gift register."
        ],
        "explanation": "Under GMC guidance, doctors must not accept cash or high-value personal gifts from patients. You should: (1) thank him graciously while declining the cash, (2) signpost official hospital charity/ward fund channels, and (3) inform your supervisor and document the refusal."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "A pharmaceutical representative offers you an all-expenses-paid luxury golf and spa weekend if you switch your GP practice's atrial fibrillation patients from generic apixaban to their expensive new branded DOAC.\n\nSelect the THREE most appropriate actions.",
        "options": [
            "Decline the luxury hotel weekend and refuse any link between hospitality and prescribing.",
            "Explain that practice prescribing is based strictly on clinical evidence and NICE/local formulary guidance.",
            "Inform your fellow GP partners and governance lead about the inappropriate inducement.",
            "Accept the weekend and switch 50 patients to the new drug on Monday.",
            "Ask the representative to transfer the cash value to your bank account instead.",
            "Switch all patients to the branded drug without informing them.",
            "Accept the trip and omit it from the practice conflict-of-interest register.",
            "Agree to switch patients only if the company buys new reception laptops."
        ],
        "correct_answer": [
            "Decline the luxury hotel weekend and refuse any link between hospitality and prescribing.",
            "Explain that practice prescribing is based strictly on clinical evidence and NICE/local formulary guidance.",
            "Inform your fellow GP partners and governance lead about the inappropriate inducement."
        ],
        "explanation": "GMC guidance and the ABPI Code strictly prohibit accepting inducements or excessive hospitality linked to prescribing decisions. You must: (1) decline the hospitality and quid-pro-quo offer, (2) reiterate that prescribing follows clinical evidence and local formulary rules, and (3) alert your GP partners."
    }
]
