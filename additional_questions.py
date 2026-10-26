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
        "scenario": "A 66-year-old man with poorly controlled hypertension presents to the Emergency Department with a sudden-onset, severe tearing pain between his shoulder blades that started 45 minutes ago while lifting a heavy suitcase. He looks pale and clammy. His heart rate is 96 bpm, blood pressure in his right arm is 188/104 mmHg, and blood pressure in his left arm is 146/86 mmHg. A 12-lead ECG shows left ventricular hypertrophy with non-specific lateral ST-T changes, and the triage nurse asks if you want to administer loading doses of aspirin and ticagrelor for suspected acute coronary syndrome.\n\nWhat is the most appropriate immediate action?",
        "options": [
            "Withhold antiplatelet therapy and arrange an urgent CT aortogram",
            "Administer aspirin 300 mg and ticagrelor 180 mg and repeat the ECG in 15 minutes",
            "Administer intravenous thrombolysis with alteplase",
            "Request a serum D-dimer and await the result before imaging",
            "Start an intravenous dobutamine infusion to equalise limb perfusion"
        ],
        "correct_answer": "Withhold antiplatelet therapy and arrange an urgent CT aortogram",
        "explanation": "Sudden-onset tearing interscapular pain coupled with a systolic blood pressure discrepancy >20 mmHg between arms is classic for acute aortic dissection. Giving dual antiplatelet therapy or anticoagulation for a presumed ACS is a dangerous trap that can trigger catastrophic haemorrhage if emergency surgical repair is required or if the dissection ruptures into the pericardium. Immediate CT angiography of the aorta (alongside intravenous beta-blockade such as labetalol to reduce aortic wall shear stress) is the priority."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 79-year-old woman with permanent atrial fibrillation and chronic heart failure presents to her GP with a 4-day history of nausea, anorexia, fatigue, and noticing a yellowish-green tint to her vision. Her regular medications are digoxin 125 micrograms daily, ramipril 5 mg daily, and furosemide. Two weeks ago, her furosemide dose was doubled from 40 mg to 80 mg daily following an episode of ankle swelling. An ECG shows atrial fibrillation at 52 bpm with widespread down-sloping ST-segment depression.\n\nWhich electrolyte abnormality is most likely to have precipitated her current presentation?",
        "options": [
            "Hypokalaemia",
            "Hyperkalaemia",
            "Hypocalcaemia",
            "Hyponatraemia",
            "Hypermagnesaemia"
        ],
        "correct_answer": "Hypokalaemia",
        "explanation": "Note that the reverse-tick ST depression ('Salvador Dali moustache') on the ECG reflects digoxin effect rather than toxicity itself, whereas the anorexia, nausea, xanthopsia (yellow-green visual disturbance), and bradyarrhythmia indicate true digoxin toxicity. Digoxin inhibits the myocardial Na+/K+-ATPase pump by binding to the same extracellular site as potassium ions. When loop diuretics (furosemide) cause hypokalaemia, there is less potassium competing with digoxin at the binding site, markedly potentiating digoxin toxicity even when serum digoxin levels remain within the normal therapeutic range."
    },

    # ==========================================
    # DERMATOLOGY / OPHTHALMOLOGY / ENT (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 44-year-old man with long-standing mild chronic plaque psoriasis presents to the Urgent Treatment Centre feeling feverish, shivery, and acutely unwell. Ten days ago, he attended a walk-in clinic with severe acute rhinosinusitis and was prescribed a 5-day course of oral prednisolone 40 mg daily, which he finished 5 days ago. Over the last 48 hours, his skin has become diffusely fiery red, hot, and tender, covered in sheets of tiny, sterile, pinpoint yellowish pustules across his trunk and limbs. His temperature is 38.6°C and heart rate is 114 bpm.\n\nWhat is the most likely diagnosis?",
        "options": [
            "Generalised pustular psoriasis triggered by systemic corticosteroid withdrawal",
            "Staphylococcal scalded skin syndrome",
            "Stevens-Johnson syndrome secondary to corticosteroid therapy",
            "Eczema herpeticum",
            "Cellulitis with secondary impetiginisation"
        ],
        "correct_answer": "Generalised pustular psoriasis triggered by systemic corticosteroid withdrawal",
        "explanation": "Systemic corticosteroids are a well-known trap in patients with psoriasis: while they temporarily suppress plaques, abrupt withdrawal can precipitate a life-threatening rebound flare of generalised pustular psoriasis (von Zumbusch variant) or erythrodermic psoriasis. Patients present with systemic toxicity (fever, tachycardia, malaise) and widespread fiery erythema studded with sterile pinpoint pustules, requiring urgent dermatological admission because of the risk of high-output cardiac failure, hypothermia, and sepsis."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 36-year-old woman presents to the Emergency Department after waking up with right-sided facial weakness and drooling when drinking her morning tea. She reports a mild ache behind her right ear over the past 2 days and notes that noises sound unusually loud in her right ear. On examination, she is unable to wrinkle the right side of her forehead, cannot fully close her right eyelid, and the right corner of her mouth droops when she smiles. Otoscopy of the right ear canal and tympanic membrane is completely normal, and limb power, coordination, and sensation are intact.\n\nProvided she has presented within 72 hours of symptom onset, what is the most appropriate management?",
        "options": [
            "Oral prednisolone and lubricating eye drops, with taping of the eyelid at night",
            "Urgent non-contrast CT head and stroke thrombolysis call",
            "Oral aciclovir monotherapy for 7 days",
            "Oral amoxicillin for presumed acute otitis media",
            "Immediate surgical decompression of the facial nerve canal"
        ],
        "correct_answer": "Oral prednisolone and lubricating eye drops, with taping of the eyelid at night",
        "explanation": "Inability to wrinkle the ipsilateral forehead confirms a lower motor neuron facial nerve (CN VII) lesion rather than an upper motor neuron lesion (such as an acute cerebral hemisphere stroke, where forehead movement is spared due to bilateral cortical innervation of the upper facial nucleus). Normal otoscopy excludes Ramsay Hunt syndrome (herpes zoster oticus), making idiopathic Bell's palsy the diagnosis; hyperacusis occurs due to paralysis of the stapedius muscle. NICE recommends starting oral prednisolone within 72 hours of symptom onset alongside meticulous corneal protection (lubricating drops during the day and ointment/taping at night if eye closure is impaired). Antivirals alone are ineffective."
    },

    # ==========================================
    # ENDOCRINOLOGY / METABOLIC (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 52-year-old man attends his GP with a 2-month history of polyuria, nocturia, polydipsia, and recurrent candidal balanitis. A fasting venous plasma glucose is 9.8 mmol/L and a repeat fasting venous plasma glucose a week later is 10.4 mmol/L. However, a routine HbA1c sent at the same time returns at 34 mmol/mol (normal <42 mmol/mol). His past medical history includes hereditary spherocytosis and hypertension.\n\nWhat is the most accurate explanation for the discrepancy between his fasting glucose and his HbA1c?",
        "options": [
            "Shortened red blood cell lifespan in hereditary spherocytosis causes a falsely low HbA1c",
            "Hereditary spherocytosis causes a falsely elevated HbA1c by increasing glycation rates",
            "Fasting venous glucose is unreliable in patients with hypertension",
            "He has renal glycosuria rather than diabetes mellitus",
            "HbA1c only reflects post-prandial glucose peaks and misses fasting hyperglycaemia"
        ],
        "correct_answer": "Shortened red blood cell lifespan in hereditary spherocytosis causes a falsely low HbA1c",
        "explanation": "HbA1c measures the proportion of haemoglobin non-enzymatically glycated over the average 120-day lifespan of an erythrocyte. Conditions that shorten red cell survival—such as haemolytic anaemias (hereditary spherocytosis, sickle cell disease, G6PD deficiency), recent blood loss, or splenomegaly—leave red cells exposed to glucose for a much shorter time, producing a falsely low HbA1c that can mask overt diabetes. Conversely, conditions that prolong red cell age or reduce turnover (such as iron, B12, or folate deficiency, or splenectomy) cause a falsely high HbA1c."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 29-year-old asymptomatic man is found to have an adjusted serum calcium of 2.81 mmol/L (reference range 2.20–2.60) on routine occupational health blood tests. He feels entirely well with no history of renal stones, bone pain, or constipation. Repeat testing confirms persistent mild hypercalcaemia (2.79 mmol/L), a mildly low serum phosphate (0.76 mmol/L), normal renal function, normal vitamin D, and a parathyroid hormone (PTH) level of 6.8 pmol/L (reference range 1.6–6.9). A 24-hour urinary calcium-to-creatinine clearance ratio is calculated at 0.006.\n\nWhat is the most likely diagnosis?",
        "options": [
            "Familial hypocalciuric hypercalcaemia",
            "Primary hyperparathyroidism secondary to a solitary parathyroid adenoma",
            "Tertiary hyperparathyroidism",
            "Humoral hypercalcaemia of malignancy",
            "Vitamin D toxicity"
        ],
        "correct_answer": "Familial hypocalciuric hypercalcaemia",
        "explanation": "Both primary hyperparathyroidism and familial hypocalciuric hypercalcaemia (FHH) present with hypercalcaemia and an elevated or inappropriately normal (unsuppressed) PTH level. The critical distinguisher—and the reason urinary calcium testing is performed before referring for parathyroid surgery—is the 24-hour urinary calcium-to-creatinine clearance ratio. FHH is an autosomal dominant loss-of-function mutation in the calcium-sensing receptor (CaSR) in the parathyroid glands and kidneys, causing the kidneys to avidly reabsorb calcium (clearance ratio <0.01). Recognising FHH spares the patient an unnecessary and ineffective parathyroidectomy."
    },

    # ==========================================
    # GASTROENTEROLOGY / CLINICAL NUTRITION (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 76-year-old woman is brought to the Emergency Department with a 3-hour history of sudden-onset, agonising central abdominal pain and two episodes of vomiting. Her past medical history includes atrial fibrillation, for which she takes bisoprolol, and she admits she stopped taking her apixaban 3 weeks ago because of minor gum bleeding. On examination, she is distressed and writhing in bed, with a heart rate of 118 bpm (irregularly irregular) and blood pressure of 110/68 mmHg, yet palpation of her abdomen reveals it is soft with only mild diffuse tenderness and no guarding. Arterial blood gas shows pH 7.26, HCO3- 14 mmol/L, and lactate 6.4 mmol/L.\n\nWhat is the most appropriate definitive diagnostic investigation?",
        "options": [
            "Urgent CT angiography of the abdomen",
            "Erect chest X-ray and plain abdominal X-ray",
            "Urgent upper gastrointestinal endoscopy",
            "Abdominal ultrasound to assess the biliary tree",
            "Serum amylase and conservative management with intravenous fluids"
        ],
        "correct_answer": "Urgent CT angiography of the abdomen",
        "explanation": "Severe, sudden-onset abdominal pain that is markedly out of proportion to the benign clinical examination findings (soft abdomen without peritonism) is the hallmark of early acute mesenteric ischaemia. Unanticoagulated atrial fibrillation provides a clear cardioembolic source (typically occluding the superior mesenteric artery), and the profound metabolic acidosis with high lactate reflects ischaemic bowel. Peritonism only develops late once full-thickness bowel infarction and perforation have occurred. Triphasic CT angiography of the abdomen is the investigation of choice."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 23-year-old medical student attends his GP after his flatmate noticed a subtle yellow tinge to his sclerae over the past 2 days while he has been recovering from a viral coryzal illness and skipping meals to revise for exams. He denies dark urine, pale stools, pruritus, or abdominal pain. On examination, there is mild scleral icterus, no hepatosplenomegaly, and no stigmata of chronic liver disease. Blood tests show:\n- Total bilirubin: 54 µmol/L (reference range 3–20)\n- Conjugated (direct) bilirubin: 6 µmol/L\n- ALT: 22 U/L (reference range 5–40)\n- ALP: 68 U/L (reference range 30–130)\n- Haemoglobin: 152 g/L, Reticulocyte count: 1.1% (normal)\n\nWhat is the most appropriate next step in management?",
        "options": [
            "Reassure him that this is a benign inherited condition and no treatment is required",
            "Arrange an urgent MRCP to exclude choledocholithiasis",
            "Refer to haematology for a direct antiglobulin (Coombs) test",
            "Advise complete alcohol abstinence and perform a liver biopsy",
            "Start oral ursodeoxycholic acid"
        ],
        "correct_answer": "Reassure him that this is a benign inherited condition and no treatment is required",
        "explanation": "Isolated unconjugated hyperbilirubinaemia with completely normal liver enzymes (ALT, ALP) and no evidence of haemolysis (normal haemoglobin and reticulocytes) triggered by intercurrent viral illness, fasting, dehydration, or stress is classic for Gilbert's syndrome. It is a common autosomal recessive reduction in hepatic UDP-glucuronosyltransferase (UGT1A1) activity affecting ~5% of the population. Because unconjugated bilirubin is water-insoluble, it does not enter the urine (so urine remains normal in colour). Reassurance and explanation of triggers are all that is required."
    },

    # ==========================================
    # INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 38-year-old woman presents to her GP with a painless, expanding red rash behind her left knee. Twelve days ago, she went camping in the New Forest and remembers brushing a tiny dark speck off her leg. On examination, there is an 8 cm erythematous annular lesion with partial central clearing behind the left knee. She feels slightly fatigued with mild generalized myalgia, has no fever, and has no neurological or cardiac symptoms.\n\nAccording to NICE guidelines, what is the most appropriate management?",
        "options": [
            "Diagnose Lyme disease clinically and start oral doxycycline 100 mg twice daily for 21 days without waiting for serology",
            "Request Borrelia burgdorferi ELISA serology and withhold antibiotics until a positive result is confirmed",
            "Prescribe topical terbinafine cream twice daily for 2 weeks",
            "Prescribe oral flucloxacillin 500 mg four times daily for 7 days",
            "Administer a single prophylactic 200 mg dose of oral doxycycline"
        ],
        "correct_answer": "Diagnose Lyme disease clinically and start oral doxycycline 100 mg twice daily for 21 days without waiting for serology",
        "explanation": "Erythema migrans—a painless, slowly expanding 'bull's-eye' rash appearing 1–4 weeks (typically 3–30 days) after a tick bite—is a clinical diagnosis of Lyme disease (*Borrelia burgdorferi*). NICE explicitly advises against waiting for serology when erythema migrans is present, both because the rash is diagnostic in itself and because early antibody tests (ELISA) have a high false-negative rate in the first few weeks of infection. First-line treatment in non-pregnant adults is oral doxycycline 100 mg twice daily (or 200 mg once daily) for 21 days."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 63-year-old man presents to his GP complaining of intense, burning generalized itching that occurs consistently for 20 minutes after he takes a hot shower or bath, despite having no visible rash. He also mentions intermittent throbbing headaches and painful redness and burning in his toes that improves with aspirin. On examination, he has a plethoric facial complexion and a palpable spleen tip 2 cm below the left costal margin. His oxygen saturation is 98% on room air. Blood tests show:\n- Haemoglobin: 196 g/L (reference range 135–175)\n- Haematocrit: 0.58\n- White cell count: 13.4 × 10^9/L\n- Platelets: 540 × 10^9/L\n- Serum erythropoietin (EPO): Low\n\nWhich genetic mutation is present in over 95% of patients with this condition?",
        "options": [
            "JAK2 V617F mutation",
            "BCR-ABL1 fusion gene (Philadelphia chromosome)",
            "CALR exon 9 mutation",
            "HFE C282Y homozygosity",
            "Factor V Leiden mutation"
        ],
        "correct_answer": "JAK2 V617F mutation",
        "explanation": "Aquagenic pruritus (intense itching after contact with warm water), erythromelalgia (burning redness in the digits relieved by aspirin), facial plethora, splenomegaly, pancytosis (raised Hb/Hct, WCC, and platelets), and a suppressed serum erythropoietin level point to polycythaemia vera (PV). Unlike secondary polycythaemia (driven by chronic hypoxia or EPO-secreting tumours, where EPO is elevated), PV is a clonal myeloproliferative neoplasm driven in >95% of cases by an activating *JAK2* V617F mutation, leading to EPO-independent erythroid proliferation."
    },

    # ==========================================
    # MUSCULOSKELETAL (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 26-year-old man presents to his GP with an 8-month history of insidious-onset lower back and alternating buttock pain. The pain wakes him during the second half of the night, forcing him to get out of bed and walk around the room, and is accompanied by 60 minutes of morning stiffness that gradually eases once he cycles to work. He had an episode of acute anterior uveitis treated by ophthalmology last year. Lumbar spine and pelvic X-rays requested by a locum GP 2 weeks ago are reported as normal.\n\nWhat is the most appropriate next step in management?",
        "options": [
            "Refer to rheumatology for suspected axial spondyloarthritis (where MRI of the sacroiliac joints and spine can be arranged)",
            "Reassure him that normal pelvic X-rays exclude ankylosing spondylitis and refer for physiotherapy",
            "Arrange an urgent MRI of the lumbar spine to exclude cauda equina syndrome",
            "Request serum rheumatoid factor and anti-CCP antibodies",
            "Advise strict bed rest during flares and prescribe modified-release morphine"
        ],
        "correct_answer": "Refer to rheumatology for suspected axial spondyloarthritis (where MRI of the sacroiliac joints and spine can be arranged)",
        "explanation": "Chronic back pain (>3 months) starting before age 45 with inflammatory features—insidious onset, waking in the second half of the night, morning stiffness >30 minutes, improvement with exercise but not rest, alternating buttock pain, and extra-articular features like anterior uveitis—strongly points to axial spondyloarthritis. A very common exam trap is ruling out the diagnosis because plain X-rays of the sacroiliac joints are normal: radiographic sacroiliitis often takes years to appear. NICE recommends referring to rheumatology even if plain X-rays are normal, as MRI with STIR sequences detects early bone marrow oedema (non-radiographic axial spondyloarthritis)."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 68-year-old man with type 2 diabetes and osteoarthritis presents to the Emergency Department with a 24-hour history of a severely painful, hot, swollen right knee and rigors. He has not had a joint replacement. On examination, his temperature is 38.8°C, heart rate is 108 bpm, and blood pressure is 128/76 mmHg. The right knee is erythematous, tense, and held in slight flexion; any attempt at passive or active movement causes excruciating pain.\n\nWhat is the single most important investigation to perform before commencing empirical intravenous antibiotics?",
        "options": [
            "Urgent synovial fluid aspiration (arthrocentesis) for microscopy, Gram stain, crystal analysis, and culture",
            "Plain AP and lateral radiographs of the right knee",
            "Serum uric acid concentration",
            "MRI of the right knee to exclude osteomyelitis",
            "C-reactive protein and erythrocyte sedimentation rate"
        ],
        "correct_answer": "Urgent synovial fluid aspiration (arthrocentesis) for microscopy, Gram stain, crystal analysis, and culture",
        "explanation": "An acutely hot, swollen, monoarticular joint with fever and severe restriction of passive movement must be managed as septic arthritis until proven otherwise, as bacterial chondrolysis can irreversibly destroy articular cartilage within 24–48 hours. In a native joint, urgent needle aspiration (arthrocentesis) for synovial fluid WCC, Gram stain, polarised light microscopy (noting that crystals and infection can coexist), and culture must be performed *prior* to starting empirical IV antibiotics so that synovial cultures are not sterilised. (Note: if the joint were prosthetic, aspiration must only be performed by the orthopaedic team in a sterile theatre environment.)"
    },

    # ==========================================
    # PAEDIATRICS (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old boy is brought to his GP by his mother with a 2-day history of a non-blanching rash over his buttocks and the extensor surfaces of both lower legs, accompanied by bilateral ankle swelling and intermittent colicky abdominal pain. He had a mild viral upper respiratory tract infection 10 days ago. On examination, he is afebrile, well-perfused, and alert, with palpable purpura symmetrically distributed over his buttocks and legs. His blood pressure is 96/60 mmHg. A full blood count shows haemoglobin 126 g/L, white cell count 8.9 × 10^9/L, and platelets 310 × 10^9/L. Urine dipstick is currently negative for blood and protein.\n\nWhat is the most important aspect of ongoing follow-up for this child?",
        "options": [
            "Regular monitoring of urine dipstick (for blood and protein) and blood pressure for at least 6 months",
            "Urgent bone marrow biopsy to exclude acute lymphoblastic leukaemia",
            "A 14-day course of oral prednisolone to prevent renal involvement",
            "Immediate administration of intramuscular benzylpenicillin",
            "Platelet transfusion to prevent spontaneous intracranial haemorrhage"
        ],
        "correct_answer": "Regular monitoring of urine dipstick (for blood and protein) and blood pressure for at least 6 months",
        "explanation": "The classic tetrad of palpable purpura (characteristically over the buttocks and lower limb extensor surfaces) with a normal platelet count, arthralgia/arthritis, colicky abdominal pain, and potential IgA nephropathy following a viral URTI is Henoch-Schönlein purpura (IgA vasculitis). While skin, joint, and mild gut symptoms are self-limiting, long-term morbidity depends on renal involvement (HSP nephritis), which can develop weeks to months after the initial rash resolves. All children therefore require regular urinalysis (for haematuria/proteinuria) and blood pressure monitoring for 6–12 months. Prophylactic corticosteroids do not prevent nephritis."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 5-month-old infant is brought to the GP surgery in November with a 3-day history of coryzal symptoms, a dry wheezy cough, and mild breathlessness during feeds. He was born at term with no neonatal complications. On examination, he is alert and interactive, his temperature is 37.6°C, respiratory rate is 46 breaths/min, oxygen saturation is 96% on room air, and there is mild subcostal recession with widespread fine end-inspiratory crackles and expiratory wheeze across both lung fields. His mother reports he is taking roughly 75% of his usual formula milk volumes and has had four wet nappies today.\n\nAccording to NICE guidelines, what is the most appropriate management?",
        "options": [
            "Supportive care at home with smaller, more frequent feeds, nasal saline drops, and red-flag safety-netting advice",
            "Prescribe a salbutamol metered-dose inhaler via a spacer",
            "Prescribe a 5-day course of oral amoxicillin",
            "Administer a single dose of oral dexamethasone",
            "Admit immediately to hospital for nasogastric tube feeding and humidified oxygen"
        ],
        "correct_answer": "Supportive care at home with smaller, more frequent feeds, nasal saline drops, and red-flag safety-netting advice",
        "explanation": "A prodrome of coryza followed by dry cough, tachypnoea, fine crackles, and wheeze in an infant under 1 year old (most commonly <6 months) in winter is classic for acute bronchiolitis (usually caused by RSV). NICE guidelines state that hospital admission is indicated if SpO2 is persistently <92%, feed intake falls below 50–75% of normal (or there is clinical dehydration), or there is apnoea or severe respiratory distress (grunting, marked recession, RR >70/min). Because this infant is alert, maintaining SpO2 96%, and taking 75% of feeds, management is supportive at home (smaller, more frequent feeds to reduce respiratory fatigue). Bronchodilators (salbutamol/ipratropium), systemic or inhaled corticosteroids, and antibiotics are specifically not recommended."
    },

    # ==========================================
    # PSYCHIATRY / NEUROLOGY (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 54-year-old man with a history of alcohol dependence is brought to the Emergency Department after being found confused and unsteady outside a hostel. On examination, he smells strongly of alcohol, is disorientated to time and place, has a broad-based ataxic gait, and exhibits bilateral horizontal nystagmus and a bilateral sixth cranial nerve palsy (abducens paresis). A bedside capillary blood glucose is 2.9 mmol/L.\n\nWhat is the correct sequence of immediate intravenous treatment?",
        "options": [
            "Administer high-dose intravenous thiamine (Pabrinex) before or concurrently with intravenous glucose",
            "Administer 100 mL of 20% intravenous dextrose immediately, followed by oral thiamine the next morning",
            "Administer intravenous chlordiazepoxide alone and withhold glucose",
            "Administer intravenous naloxone followed by 0.9% sodium chloride",
            "Administer intravenous phenytoin and arrange an urgent CT head"
        ],
        "correct_answer": "Administer high-dose intravenous thiamine (Pabrinex) before or concurrently with intravenous glucose",
        "explanation": "The triad of acute confusion, cerebellar ataxia, and ocular signs (nystagmus, lateral rectus palsy/ophthalmoplegia) in a malnourished or alcohol-dependent patient represents Wernicke's encephalopathy, caused by severe thiamine (vitamin B1) deficiency. Thiamine is an essential cofactor for enzymes in carbohydrate metabolism (including pyruvate dehydrogenase and alpha-ketoglutarate dehydrogenase). Giving an intravenous glucose load without replenishing thiamine first (or simultaneously) rapidly consumes any remaining marginal thiamine stores, precipitating irreversible mammillary body damage and Korsakoff's psychosis."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 27-year-old graphic designer presents to his GP with a 5-week history of pervasive low mood, anhedonia, early morning wakening, and poor concentration, requesting an antidepressant. While taking a collateral history, you ask whether he has ever experienced periods of unusually elevated mood. He recalls a 9-day period eight months ago during which he slept only 2 hours a night without feeling tired, spoke so rapidly his friends could not interrupt him, maxxed out three credit cards on a grand business venture, and believed he had been chosen to redesign the global banking system.\n\nWhat is the most appropriate management step?",
        "options": [
            "Avoid starting antidepressant monotherapy and refer urgently to the secondary care mental health team for assessment of suspected bipolar disorder",
            "Start oral sertraline 50 mg once daily and review in 2 weeks",
            "Start oral amitriptyline 75 mg at night to help his early morning wakening",
            "Start lithium carbonate immediately in primary care without specialist referral",
            "Reassure him that his previous episode was normal creative productivity and refer for low-intensity CBT"
        ],
        "correct_answer": "Avoid starting antidepressant monotherapy and refer urgently to the secondary care mental health team for assessment of suspected bipolar disorder",
        "explanation": "Patients with bipolar disorder most commonly present to primary care during a depressive episode rather than during mania or hypomania. Careful screening for past episodes of decreased need for sleep, pressured speech, grandiosity, and reckless spending is essential: here, a 9-day episode with grandiose delusions represents a previous manic episode (Bipolar I disorder). Prescribing unopposed SSRI or tricyclic antidepressant monotherapy in bipolar depression carries a high risk of triggering a manic switch or inducing rapid cycling. NICE advises referring to secondary care where specialist pharmacological treatment (such as fluoxetine combined with olanzapine, quetiapine, or lamotrigine alongside a mood stabiliser) can be initiated."
    },

    # ==========================================
    # RENAL / UROLOGY (2 Questions)
    # ==========================================
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 71-year-old man with stage 4 chronic kidney disease is admitted with acute-on-chronic kidney injury following a diarrhoeal illness during which he continued taking ramipril and spironolactone. His urgent venous blood gas shows a potassium of 7.1 mmol/L. A 12-lead ECG demonstrates absent P waves, tall tented T waves across the precordial leads, and broadening of the QRS complex to 156 ms.\n\nWhich intravenous medication must be administered first?",
        "options": [
            "10 mL of 10% calcium gluconate over 5–10 minutes",
            "10 units of soluble insulin in 50 mL of 20% glucose over 15–30 minutes",
            "Nebulised salbutamol 10 mg",
            "Intravenous sodium zirconium cyclosilicate",
            "Intravenous furosemide 80 mg stat"
        ],
        "correct_answer": "10 mL of 10% calcium gluconate over 5–10 minutes",
        "explanation": "In severe hyperkalaemia (K+ ≥6.5 mmol/L) accompanied by toxic ECG changes (tall tented T waves, loss of P waves, PR prolongation, and especially QRS widening, which heralds imminent sine-wave pattern and ventricular fibrillation/asystole), the immediate life-saving priority is myocardial membrane stabilisation with intravenous calcium (10 mL of 10% calcium gluconate or calcium chloride). Calcium does not lower the serum potassium concentration, so it must be followed immediately by intracellular shift therapy (insulin-dextrose infusion and nebulised salbutamol) and potassium removal from the body."
    },
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 48-year-old female schoolteacher presents to her GP after noticing frankly blood-stained urine without clots on two occasions over the past week. She has no dysuria, urinary frequency, suprapubic pain, or loin pain, and she stopped menstruating 6 months ago following an endometrial ablation. She is an ex-smoker with a 15-pack-year history. Her abdomen is soft and non-tender, blood pressure is 124/78 mmHg, and a mid-stream urine dipstick shows 3+ blood, negative leucocytes, and negative nitrites. Urine microscopy and culture shows red blood cells with no bacterial growth.\n\nAccording to NICE (NG12) guidelines, what is the most appropriate next step?",
        "options": [
            "Refer via the urgent 2-week wait suspected cancer pathway for bladder/renal cancer investigation",
            "Prescribe a 3-day course of oral nitrofurantoin and repeat the urine dipstick in 2 weeks",
            "Reassure her and repeat the urine microscopy in 6 months",
            "Routine referral to nephrology for suspected IgA nephropathy",
            "Request a serum CA-125 and transvaginal ultrasound"
        ],
        "correct_answer": "Refer via the urgent 2-week wait suspected cancer pathway for bladder/renal cancer investigation",
        "explanation": "Under NICE NG12 guidelines, an urgent 2-week wait suspected urological cancer referral (for flexible cystoscopy and upper urinary tract imaging) is indicated for any patient aged **45 years and over** who has either: (1) unexplained visible haematuria without urinary tract infection, or (2) visible haematuria that persists or recurs after successful treatment of a urinary tract infection. (For unexplained *non-visible* haematuria, the age threshold is ≥60 years accompanied by either dysuria or a raised white cell count on a blood test.) Painless visible haematuria is the classic presentation of urothelial bladder carcinoma."
    },

    # ==========================================
    # REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 24-year-old woman attends her GP requesting the combined oral contraceptive pill (COCP) both for contraception and to help regulate her heavy periods. She is a non-smoker with a BMI of 22 kg/m² and a blood pressure of 112/70 mmHg. She mentions that twice a year she gets severe unilateral throbbing headaches preceded by 25 minutes of shimmering zig-zag lines across her visual field, which resolve completely when the headache starts.\n\nAccording to the UK Medical Eligibility Criteria (UKMEC), how is the combined oral contraceptive pill classified for this patient?",
        "options": [
            "UKMEC Category 4 (unacceptable health risk; absolute contraindication)",
            "UKMEC Category 3 (risks generally outweigh theoretical or proven benefits)",
            "UKMEC Category 2 (benefits generally outweigh theoretical or proven risks)",
            "UKMEC Category 1 (no restriction for the use of the contraceptive method)",
            "Safe to prescribe provided a low-dose (20 microgram ethinylestradiol) formulation is used"
        ],
        "correct_answer": "UKMEC Category 4 (unacceptable health risk; absolute contraindication)",
        "explanation": "Migraine *with aura* (at any age, even if attacks are infrequent or occurred in the past) is a UKMEC Category 4 (absolute contraindication) for all combined hormonal contraception (COCP, combined patch, combined vaginal ring) due to a synergistically elevated risk of ischaemic stroke caused by ethinylestradiol. By contrast, migraine *without aura* in a woman under 35 with no other stroke risk factors is UKMEC 2 for initiation. Progestogen-only methods (such as the POP, implant, depot injection, or LNG-IUD, which also treats heavy menstrual bleeding) are safe options here."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 31-year-old primigravida at 33 weeks' gestation presents to her midwife and GP with a 1-week history of intense, generalized itching that is markedly worse on the palms of her hands and the soles of her feet at night, preventing her from sleeping. She feels fetal movements are normal. On examination, her blood pressure is 118/72 mmHg, urine dipstick is negative for protein, and skin inspection reveals linear excoriation marks from scratching on her forearms and calves, with no primary rash.\n\nWhat is the most important diagnostic investigation to arrange?",
        "options": [
            "Serum bile acids and liver function tests",
            "Skin scraping for microscopy in potassium hydroxide",
            "24-hour urinary protein collection and serum uric acid",
            "Fasting venous plasma glucose",
            "Patch testing for allergic contact dermatitis"
        ],
        "correct_answer": "Serum bile acids and liver function tests",
        "explanation": "Pruritus in the third trimester affecting particularly the palms and soles, worse at night, and occurring *without a primary skin rash* (only secondary excoriations from scratching) is the classic presentation of intrahepatic cholestasis of pregnancy (ICP, also called obstetric cholestasis). Serum total bile acids (specifically peak bile acids ≥19 µmol/L) and liver function tests (ALT/AST are often mildly-to-moderately elevated) establish the diagnosis. Identifying ICP is vital because severely elevated bile acids (especially ≥100 µmol/L) carry an increased risk of spontaneous preterm labour, fetal distress, and sudden intrauterine fetal death (stillbirth), guiding timing of planned birth."
    },

    # ==========================================
    # RESPIRATORY (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 28-year-old woman presents to her GP with a 4-month history of episodic dry cough, chest tightness, and wheeze that are worse at night and after running in cold air. She has a childhood history of atopic eczema and seasonal allergic rhinitis. Outside of these episodes, her chest examination is completely normal.\n\nAccording to current NICE guidelines, what is the recommended objective diagnostic pathway for suspected asthma in adults?",
        "options": [
            "Perform objective testing (such as blood eosinophil count or fractional exhaled nitric oxide [FeNO], and spirometry with bronchodilator reversibility) before confirming the diagnosis",
            "Start a 6-week empirical trial of a low-dose inhaled corticosteroid and diagnose asthma if symptoms resolve",
            "Diagnose asthma on clinical history alone and prescribe a salbutamol reliever inhaler",
            "Arrange a high-resolution CT scan of the thorax as the first-line test",
            "Perform an arterial blood gas on room air during a routine clinic visit"
        ],
        "correct_answer": "Perform objective testing (such as blood eosinophil count or fractional exhaled nitric oxide [FeNO], and spirometry with bronchodilator reversibility) before confirming the diagnosis",
        "explanation": "A major shift in NICE asthma guidelines (including the joint BTS/NICE/SIGN guidance) is that a diagnosis of asthma in adults and children aged 5 and over should **not** be made on clinical history alone or via a 'trial of treatment' with inhalers, because symptoms and empirical improvement are non-specific and lead to widespread overdiagnosis. Instead, objective testing—measuring airway inflammation (FeNO or blood eosinophils) and airflow obstruction/variability (spirometry with bronchodilator reversibility, or peak expiratory flow variability)—is required to confirm the diagnosis (unless the patient presents acutely unwell, in which case treatment is given immediately and testing is performed shortly afterwards)."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 64-year-old man with a 45-pack-year smoking history presents to the Emergency Department with a 2-week history of progressive breathlessness, a feeling of fullness in his head that worsens when he bends forward to tie his shoelaces, and morning facial swelling. On examination, his face is plethoric with periorbital oedema, there are dilated collateral veins visible across his upper anterior chest wall, and his jugular venous pressure is markedly elevated at 9 cm above the sternal angle with a fixed, non-pulsatile column.\n\nWhat is the most likely underlying anatomical cause of his presentation?",
        "options": [
            "Superior vena cava obstruction secondary to a right upper lobe bronchogenic carcinoma or mediastinal lymphadenopathy",
            "Cardiac tamponade secondary to a malignant pericardial effusion",
            "Right ventricular infarction",
            "Pancoast tumour invading the inferior cervical sympathetic ganglion",
            "Tension pneumothorax"
        ],
        "correct_answer": "Superior vena cava obstruction secondary to a right upper lobe bronchogenic carcinoma or mediastinal lymphadenopathy",
        "explanation": "Morning facial and periorbital oedema, facial plethora, headache/head fullness aggravated by stooping forward, dilated superficial chest wall collateral veins, and a **fixed, non-pulsatile** raised JVP (Pemberton's sign when lifting the arms causes facial congestion and stridor) form the classic presentation of superior vena cava obstruction (SVCO). Notice how the non-pulsatile JVP distinguishes SVCO from cardiac tamponade or right heart failure (where the JVP remains pulsatile). Lung cancer (particularly small cell lung cancer and right-sided squamous cell carcinoma) and lymphoma are the commonest malignant causes."
    },

    # ==========================================
    # PHARMACOLOGY (2 Questions)
    # ==========================================
    {
        "exam": "MSRA / AKT",
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 22-year-old woman with juvenile myoclonic epilepsy is reviewed in clinic. Her generalised tonic-clonic and myoclonic seizures have only ever been controlled on sodium valproate, after levetiracetam and lamotrigine both failed due to severe side effects and breakthrough status epilepticus. She is sexually active with a male partner.\n\nAccording to MHRA regulatory safety guidance, which of the following is mandatory if sodium valproate is to be continued in this patient?",
        "options": [
            "Enrolment in the Pregnancy Prevention Programme (PPP), including use of highly effective contraception and signing an Annual Risk Acknowledgement Form with a specialist",
            "Switching her to phenytoin immediately without neurology input",
            "Taking low-dose folic acid 400 micrograms daily as a substitute for contraception",
            "Performing monthly serum valproate trough levels to prevent teratogenicity",
            "Withholding sodium valproate only after a positive urine pregnancy test is obtained"
        ],
        "correct_answer": "Enrolment in the Pregnancy Prevention Programme (PPP), including use of highly effective contraception and signing an Annual Risk Acknowledgement Form with a specialist",
        "explanation": "Sodium valproate is highly teratogenic: exposure in utero carries an ~10% risk of major congenital malformations (such as neural tube defects, craniofacial anomalies, and cardiac defects) and a 30–40% risk of permanent neurodevelopmental disorders and lower IQ. MHRA regulations stipulate that valproate must not be used in any woman or girl of childbearing potential unless other treatments are ineffective or not tolerated, and if used, the **Pregnancy Prevention Programme (PPP)** must be strictly followed—requiring highly effective contraception (ideally a user-independent LARC such as an IUD, IUS, or implant) and an Annual Risk Acknowledgement Form signed by both the patient and specialists."
    },
    {
        "exam": "UKMLA / MSRA",
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 74-year-old woman is receiving once-daily (extended-interval) intravenous gentamicin (5 mg/kg) for urosepsis with Gram-negative bacteraemia. A pre-dose (trough) serum gentamicin level is taken 20 hours after the first infusion and returns elevated at 2.4 mg/L (target trough <1.0 mg/L; Hartford nomogram indicates reduced clearance). Her serum creatinine has risen from 88 µmol/L to 124 µmol/L.\n\nWhat is the correct adjustment to her gentamicin regimen?",
        "options": [
            "Withhold the next scheduled dose and extend the dosing interval (e.g. from 24-hourly to 36- or 48-hourly), repeating the trough level before administering a further dose",
            "Administer the next dose on time but halve the milligram dose",
            "Double the infusion rate of the next dose to achieve a higher peak concentration",
            "Continue the same dose at 24-hourly intervals as high troughs are needed for bactericidal efficacy",
            "Add intravenous vancomycin and furosemide to flush gentamicin through the kidneys"
        ],
        "correct_answer": "Withhold the next scheduled dose and extend the dosing interval (e.g. from 24-hourly to 36- or 48-hourly), repeating the trough level before administering a further dose",
        "explanation": "Aminoglycosides (gentamicin, amikacin) exhibit **concentration-dependent killing** (where a high peak concentration relative to the MIC drives bacterial eradication) alongside a prolonged post-antibiotic effect, whereas **nephrotoxicity and irreversible vestibulocochlear ototoxicity** correlate with persistently elevated **trough** levels (failure to clear the drug between doses). Therefore, when the pre-dose trough concentration is too high or renal clearance falls, you extend the dosing interval (or withhold the next dose until the level falls below the safe threshold <1 mg/L) rather than administering frequent small doses."
    },

    # ==========================================
    # PROFESSIONAL DILEMMAS - RANKING (8 Questions)
    # ==========================================
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a GP. A 42-year-old van delivery driver attends a follow-up appointment 2 weeks after being discharged from hospital following a witnessed first unprovoked generalised tonic-clonic seizure. The hospital discharge summary confirms the neurology team advised him that he must stop driving immediately and notify the DVLA. During today's consultation, he tells you that he has not informed the DVLA and is still driving his delivery van every day because he is self-employed and cannot afford to lose his income. You explain the legal requirement and the severe risk to himself and the public, but he remains adamant that he will continue driving.\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Inform the patient that if he continues to drive against medical advice, you have a professional duty to disclose relevant medical information to the DVLA, and encourage him one final time to self-report.",
            "Explore whether there are any alternative non-driving roles at his depot or financial support/benefits he can access while off the road, and document your discussion thoroughly.",
            "Seek prompt advice from your practice Caldicott Guardian or medical defence organisation regarding making a disclosure in the public interest.",
            "Phone the police immediately on 999 to have him arrested in the waiting room before he reaches his van.",
            "Respect his confidentiality unconditionally and take no further action, as disclosing without consent would breach GDPR."
        ],
        "correct_answer": [
            "Inform the patient that if he continues to drive against medical advice, you have a professional duty to disclose relevant medical information to the DVLA, and encourage him one final time to self-report.",
            "Explore whether there are any alternative non-driving roles at his depot or financial support/benefits he can access while off the road, and document your discussion thoroughly.",
            "Seek prompt advice from your practice Caldicott Guardian or medical defence organisation regarding making a disclosure in the public interest.",
            "Phone the police immediately on 999 to have him arrested in the waiting room before he reaches his van.",
            "Respect his confidentiality unconditionally and take no further action, as disclosing without consent would breach GDPR."
        ],
        "explanation": "Under the GMC's *Confidentiality: patients' fitness to drive and reporting concerns to the DVLA or DVA* guidance:\n1. First, if a patient continues to drive when unfit, you should make every reasonable effort to persuade them to stop and explicitly warn them that if they do not inform the DVLA, you will be obligated to disclose their relevant medical information to the DVLA in the public interest (**1st**).\n2. Supporting the patient practically (exploring non-driving duties/sick pay/benefits) and keeping meticulous contemporaneous records addresses the root barrier while protecting safety (**2nd**).\n3. Consulting a senior colleague/Caldicott Guardian/defence union while preparing the DVLA notification is sensible governance (**3rd**).\n4. Calling 999 for immediate arrest in the waiting room is disproportionate compared to the established GMC/DVLA reporting pathway unless there is an acute imminent crisis (e.g. intoxicated or actively seizing at the wheel) (**4th**).\n5. Doing nothing is the least appropriate action (**5th**): protection of the public from serious harm overrides patient confidentiality when a patient refuses to stop driving against medical advice."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a Foundation Year 2 doctor working on a care of the elderly ward. The phlebotomist informs you that an 84-year-old man admitted 3 days ago with a lower respiratory tract infection and mild resolving delirium has refused his routine morning blood tests (full blood count and urea & electrolytes), becoming agitated when approached with a needle. Yesterday's blood results showed his inflammatory markers were falling and his renal function was stable.\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Review the clinical notes and yesterday's results to determine whether a repeat venepuncture is clinically necessary today, and speak calmly with the patient to understand his refusal.",
            "If the blood test is clinically required, assess his decision-specific capacity for venepuncture and attempt to re-offer the test later when a familiar nurse or family member is present.",
            "Discuss with the ward registrar during the morning board round whether routine daily blood tests can be safely stepped down to every 48–72 hours.",
            "Tell the patient that the hospital will stop his oral antibiotics if he does not allow the blood test to be taken today.",
            "Ask two healthcare assistants to hold his arm down so you can take the blood sample quickly while he is distracted."
        ],
        "correct_answer": [
            "Review the clinical notes and yesterday's results to determine whether a repeat venepuncture is clinically necessary today, and speak calmly with the patient to understand his refusal.",
            "If the blood test is clinically required, assess his decision-specific capacity for venepuncture and attempt to re-offer the test later when a familiar nurse or family member is present.",
            "Discuss with the ward registrar during the morning board round whether routine daily blood tests can be safely stepped down to every 48–72 hours.",
            "Tell the patient that the hospital will stop his oral antibiotics if he does not allow the blood test to be taken today.",
            "Ask two healthcare assistants to hold his arm down so you can take the blood sample quickly while he is distracted."
        ],
        "explanation": "1. The most constructive first step is to check whether today's routine blood test is even clinically needed (given his improving trajectory) and speak with the patient respectfully (**1st**).\n2. Under the Mental Capacity Act 2005, if the test is needed, capacity is decision- and time-specific; waiting until fluctuating delirium settles or involving a familiar person applies the 'least restrictive' principle and maximises capacity (**2nd**).\n3. Reviewing blood test frequency with your senior prevents unnecessary distress from reflexive daily phlebotomy (**3rd**).\n4. Threatening to withhold treatment (coercion) is unethical and damages trust (**4th**).\n5. Physically restraining an agitated patient for a non-urgent routine blood test is disproportionate, unethical, and potentially unlawful battery (**5th**)."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor on a medical ward. A staff nurse approaches you looking distressed: she has just realised that 30 minutes ago she administered gliclazide 320 mg (four 80 mg tablets) instead of the intended 80 mg to a 78-year-old woman with type 2 diabetes because your handwritten drug chart entry was unclear and looked like '320 mg'.\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Assess the patient immediately at the bedside, check her capillary blood glucose and observations, and institute frequent blood glucose monitoring with oral carbohydrate or IV dextrose if required.",
            "Rewrite the prescription clearly on the drug chart and inform your medical registrar of the error and your monitoring plan.",
            "Apologise openly to the patient, explain clearly that a higher dose of her diabetes medication was given and how you will monitor her blood sugar closely, and submit a clinical incident form (Datix).",
            "Reassure the nurse that mistakes happen and advise her that there is no need to tell the patient unless her blood sugar actually drops.",
            "Cross out the original prescription heavily with black ink so that the error cannot be traced back to your handwriting."
        ],
        "correct_answer": [
            "Assess the patient immediately at the bedside, check her capillary blood glucose and observations, and institute frequent blood glucose monitoring with oral carbohydrate or IV dextrose if required.",
            "Rewrite the prescription clearly on the drug chart and inform your medical registrar of the error and your monitoring plan.",
            "Apologise openly to the patient, explain clearly that a higher dose of her diabetes medication was given and how you will monitor her blood sugar closely, and submit a clinical incident form (Datix).",
            "Reassure the nurse that mistakes happen and advise her that there is no need to tell the patient unless her blood sugar actually drops.",
            "Cross out the original prescription heavily with black ink so that the error cannot be traced back to your handwriting."
        ],
        "explanation": "1. Patient safety is always the immediate priority: sulfonylurea overdose causes prolonged hypoglycaemia, so immediate bedside assessment, blood glucose check, and a clear serial monitoring/glucose rescue plan come first (**1st**).\n2. Correcting the chart so the error is not repeated at the next drug round and escalating to your senior come next (**2nd**).\n3. Fulfilling the statutory and professional Duty of Candour (open explanation and apology to the patient) and logging a patient safety incident (Datix) for systems learning follow once the patient is safe (**3rd**).\n4. Concealing the error unless harm manifests breaches the GMC principle of honesty and candour (**4th**).\n5. Falsifying or obliterating medical records to cover up an error is serious probity misconduct that puts registration at risk (**5th**)."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor working a night shift on the acute medical unit alongside an FY1 colleague. At 03:00, you walk into the treatment room and see the FY1 about to draw up an ampoule of concentrated potassium chloride (KCl) to give as an undiluted intravenous bolus to a patient with a potassium of 3.1 mmol/L. You immediately stop him and explain that undiluted IV potassium is fatal and must always be given via a pre-mixed infusion bag. The FY1 breaks down in tears, telling you his father died unexpectedly 3 days ago, he has barely slept since, and he cannot concentrate, but came into work because he did not want to leave the night team short-staffed.\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Support the FY1 empathetically, ask him to step away from clinical duties immediately, and contact the night medical registrar and site manager to arrange cover so he can go home safely.",
            "Review any other prescriptions or clinical tasks the FY1 has completed during the shift to ensure patient safety.",
            "Ensure the FY1 has a safe way to get home (such as a hospital-funded taxi rather than driving himself while exhausted) and encourage him to contact his Educational Supervisor and GP.",
            "Tell the FY1 to drink a cup of coffee and take a 20-minute break, then ask him to only clerk stable patients for the rest of the night.",
            "Report the FY1 directly to the GMC tonight for fitness-to-practise concerns after he nearly administered a never-event bolus."
        ],
        "correct_answer": [
            "Support the FY1 empathetically, ask him to step away from clinical duties immediately, and contact the night medical registrar and site manager to arrange cover so he can go home safely.",
            "Review any other prescriptions or clinical tasks the FY1 has completed during the shift to ensure patient safety.",
            "Ensure the FY1 has a safe way to get home (such as a hospital-funded taxi rather than driving himself while exhausted) and encourage him to contact his Educational Supervisor and GP.",
            "Tell the FY1 to drink a cup of coffee and take a 20-minute break, then ask him to only clerk stable patients for the rest of the night.",
            "Report the FY1 directly to the GMC tonight for fitness-to-practise concerns after he nearly administered a never-event bolus."
        ],
        "explanation": "1. The FY1 is acutely bereaved and severely sleep-deprived, and has just had a near-miss involving a Never Event (undiluted IV potassium bolus). Both patient safety and colleague welfare require immediately relieving him of clinical duties and escalating to the night registrar and site manager to redistribute workload (**1st**).\n2. Checking the other tasks/prescriptions he completed earlier on the shift is a crucial safety net to protect patients already seen (**2nd**).\n3. Ensuring he gets home safely without driving exhausted and signposting pastoral support (ES/GP/bereavement leave) looks after colleague welfare (**3rd**).\n4. Keeping him working clinically after a 20-minute break leaves patients and the colleague at serious risk (**4th**).\n5. Punitive immediate GMC referral for an acute bereavement reaction is inappropriate and unhelpful (**5th**)."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a male GP trainee. A 32-year-old woman attends a routine appointment for a cervical screening smear test and bimanual pelvic examination for intermenstrual bleeding. You offer her a chaperone in line with GMC guidance, and she states she would like one present. However, when you call reception, you are told the practice nurses and trained healthcare assistants are all currently busy in minor surgery and phlebotomy clinics, and no trained chaperone will be available for at least 30 minutes. The patient says, 'Honestly doctor, don't worry about it, just go ahead without one so I don't miss my bus.'\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Explain politely that because she initially requested a chaperone and for mutual comfort and safety during an intimate examination, it is best to either wait 30 minutes for a trained chaperone or rebook the examination at a convenient priority slot.",
            "Complete the non-examination parts of the consultation now (full gynaecological history, STI risk assessment, and arranging blood tests or pelvic ultrasound if indicated) so her visit is still productive.",
            "Speak to the practice manager at the end of the clinic about improving chaperone availability during routine GP lists.",
            "Proceed with the speculum and pelvic examination immediately alone after asking her to sign a handwritten waiver in the notes.",
            "Ask the patient parked in the waiting room next door to step in and act as an informal chaperone."
        ],
        "correct_answer": [
            "Explain politely that because she initially requested a chaperone and for mutual comfort and safety during an intimate examination, it is best to either wait 30 minutes for a trained chaperone or rebook the examination at a convenient priority slot.",
            "Complete the non-examination parts of the consultation now (full gynaecological history, STI risk assessment, and arranging blood tests or pelvic ultrasound if indicated) so her visit is still productive.",
            "Speak to the practice manager at the end of the clinic about improving chaperone availability during routine GP lists.",
            "Proceed with the speculum and pelvic examination immediately alone after asking her to sign a handwritten waiver in the notes.",
            "Ask the patient parked in the waiting room next door to step in and act as an informal chaperone."
        ],
        "explanation": "Under GMC *Intimate examinations and chaperones* guidance:\n1. If either the patient or the doctor wishes a chaperone to be present and none is immediately available, and the examination is not a life-threatening emergency, you should delay the examination until a trained chaperone arrives or rearrange it (**1st**). A patient agreeing to waive their request only because they feel pressured by convenience/bus times should not be pushed into an unchaperoned intimate examination.\n2. Using the appointment to complete the history and non-intimate aspects of care ensures her trip is still worthwhile (**2nd**).\n3. Raising the staffing gap with the practice manager prevents recurrence (**3rd**).\n4. Proceeding alone after she already expressed a wish for a chaperone (even with a 'waiver') leaves both patient and doctor vulnerable (**4th**).\n5. Bringing a stranger from the waiting room into an intimate exam is an outrageous breach of confidentiality and dignity (**5th**)."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor on a respiratory ward. At 16:30 on a Friday, the hospital bed manager comes to the ward and strongly pressures you to sign the discharge summary and TTO (to-take-out medications) for a 72-year-old man admitted with an infective exacerbation of COPD, because the Emergency Department has patients waiting on trolleys. When you go to review the patient before signing the TTO, you find he is tachypnoeic (respiratory rate 26 breaths/min), his oxygen saturation has dropped to 85% on room air (baseline 91%), and he is too breathless to walk to the toilet.\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Decline to discharge the patient, start controlled oxygen therapy (target SpO2 88–92%) and acute medical reassessment (including an arterial blood gas), and explain clearly to the bed manager that the patient has clinically deteriorated and is unsafe for discharge.",
            "Inform your respiratory registrar or consultant of the patient's deterioration and the cancelled discharge.",
            "Update the patient and his family on why he needs to stay in hospital longer so any transport or home care arrangements can be paused.",
            "Sign the discharge summary as requested by the bed manager, but tell the patient to call 999 as soon as he gets home if he still feels breathless.",
            "Have a heated argument with the bed manager in the middle of the ward bay about hospital management targets."
        ],
        "correct_answer": [
            "Decline to discharge the patient, start controlled oxygen therapy (target SpO2 88–92%) and acute medical reassessment (including an arterial blood gas), and explain clearly to the bed manager that the patient has clinically deteriorated and is unsafe for discharge.",
            "Inform your respiratory registrar or consultant of the patient's deterioration and the cancelled discharge.",
            "Update the patient and his family on why he needs to stay in hospital longer so any transport or home care arrangements can be paused.",
            "Sign the discharge summary as requested by the bed manager, but tell the patient to call 999 as soon as he gets home if he still feels breathless.",
            "Have a heated argument with the bed manager in the middle of the ward bay about hospital management targets."
        ],
        "explanation": "1. Under GMC *Good Medical Practice*, you must make the care of your patient your first concern and never allow operational or resource pressures to compromise immediate clinical safety. Treating the acute hypoxia (controlled oxygen 88–92%, clinical review) and calmly cancelling the unsafe discharge is the top priority (**1st**).\n2. Escalating the clinical deterioration and bed status to your senior medical team ensures senior oversight (**2nd**).\n3. Communicating clearly with the patient and relatives manages expectations and logistics (**3rd**).\n4. Discharging an acutely hypoxic, tachypnoeic patient to appease bed flow targets is negligent and dangerous (**4th**).\n5. Engaging in a public confrontation in the clinical area is unprofessional (**5th**)."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor on a surgical ward. A 74-year-old woman with full mental capacity has just had an urgent abdominal CT scan for painless jaundice, which demonstrates a pancreatic head mass with multiple liver metastases. Before you go into her side room with the registrar to discuss the scan results, her adult son intercepts you in the corridor and begs you: 'Please don't tell my mum it looks like cancer—it will break her spirit and she'll give up fighting. Tell me the results instead and tell her it's just gallstones.'\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Acknowledge the son's distress empathetically, but explain politely that because his mother has capacity, you cannot withhold information from her or deceive her, nor can you share her results with him without her permission.",
            "Go in to speak with the patient sensitively, check how much detail she wishes to know about her scan results today, and ask if she would like her son present for the discussion.",
            "Offer to arrange support from the hepatobiliary clinical nurse specialist (CNS) for both the patient and her family once the results have been discussed.",
            "Tell the son the full CT report in the corridor first so he feels reassured before you speak to his mother.",
            "Agree to the son's request and tell the patient that the scan only showed benign gallstones."
        ],
        "correct_answer": [
            "Acknowledge the son's distress empathetically, but explain politely that because his mother has capacity, you cannot withhold information from her or deceive her, nor can you share her results with him without her permission.",
            "Go in to speak with the patient sensitively, check how much detail she wishes to know about her scan results today, and ask if she would like her son present for the discussion.",
            "Offer to arrange support from the hepatobiliary clinical nurse specialist (CNS) for both the patient and her family once the results have been discussed.",
            "Tell the son the full CT report in the corridor first so he feels reassured before you speak to his mother.",
            "Agree to the son's request and tell the patient that the scan only showed benign gallstones."
        ],
        "explanation": "1. Relatives frequently ask doctors to withhold bad news ('collusion') out of love and fear, so responding with empathy while maintaining a firm ethical boundary is essential: a capacitous adult has the right to confidentiality and truthful information about their diagnosis (**1st**).\n2. Exploring the patient's own wishes about how much detail she wants to hear and whether she wants her son in the room respects her autonomy (**2nd**).\n3. Involving the specialist nurse provides continuity and emotional support for the whole family (**3rd**).\n4. Disclosing the CT results to the son in the corridor without the patient's consent is a breach of patient confidentiality (**4th**).\n5. Lying to a capacitous patient about their diagnosis is a fundamental breach of honesty, autonomy, and GMC guidance (**5th**)."
    },
    {
        "exam": "MSRA",
        "type": "ranking",
        "category": "Professional Dilemmas",
        "scenario": "You are a Foundation Year 1 doctor on your first rotation in vascular surgery. Ten minutes before the morning theatre list starts, your vascular consultant rings you from the anaesthetic room and asks you to go to the Admissions Lounge and take written consent from a 75-year-old man for a complex fenestrated endovascular aneurysm repair (fEVAR). You have never seen this procedure performed and do not know its specific risks, complication rates, or alternative management options.\n\nRank in order the appropriateness of the following actions in response to this situation (1 = Most appropriate; 5 = Least appropriate).",
        "options": [
            "Explain clearly to the consultant that you have not been trained in this procedure and do not know the specific risks or alternatives required to take valid informed consent, and ask for the consultant or vascular registrar to consent the patient.",
            "Offer to accompany the consultant or vascular registrar when they take consent so you can learn about the procedure and observe the consent process.",
            "Go to the Admissions Lounge to check that the patient's clerk-in paperwork, baseline observations, group and save, and coagulation results are ready so theatre is not delayed for administrative reasons.",
            "Look up fenestrated EVAR on Wikipedia on your phone and take written consent from the patient yourself so you do not annoy the consultant.",
            "Ask the patient to sign the blank consent form now and tell him the consultant will fill in the risks box after he is asleep."
        ],
        "correct_answer": [
            "Explain clearly to the consultant that you have not been trained in this procedure and do not know the specific risks or alternatives required to take valid informed consent, and ask for the consultant or vascular registrar to consent the patient.",
            "Offer to accompany the consultant or vascular registrar when they take consent so you can learn about the procedure and observe the consent process.",
            "Go to the Admissions Lounge to check that the patient's clerk-in paperwork, baseline observations, group and save, and coagulation results are ready so theatre is not delayed for administrative reasons.",
            "Look up fenestrated EVAR on Wikipedia on your phone and take written consent from the patient yourself so you do not annoy the consultant.",
            "Ask the patient to sign the blank consent form now and tell him the consultant will fill in the risks box after he is asleep."
        ],
        "explanation": "Under GMC *Decision making and consent* guidance:\n1. The person who seeks consent should ideally be the clinician performing the procedure; it may only be delegated to someone who is suitably trained and qualified, has sufficient knowledge of the proposed investigation or treatment, and understands the risks and alternatives. Working within the limits of your competence requires politely declining to take consent for a complex procedure you do not understand (**1st**).\n2. Offering to shadow the senior clinician taking consent shows initiative and turns the situation into a constructive learning opportunity (**2nd**).\n3. Proactively ensuring all pre-op bloods, group & save, and admissions paperwork are in place genuinely helps the list run smoothly within your competence (**3rd**).\n4. Guessing risks from an internet search produces legally and ethically invalid consent (**4th**).\n5. Getting a patient to sign an incomplete/blank consent form is fraudulent and unlawful (**5th**)."
    },

    # ==========================================
    # PROFESSIONAL DILEMMAS - SELECTION (8 Questions)
    # ==========================================
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are a Foundation Year 2 doctor in the Paediatric Emergency Department. A 14-month-old boy is brought in by his mother and her new partner because he has stopped using his left arm. An X-ray of the left arm reveals a spiral fracture of the mid-shaft humerus. When taking the history, the partner states the toddler 'must have twisted his arm in the cot bars two days ago', whereas the mother says she thought it happened this morning when he tripped on the rug. On full head-to-toe examination with the child undressed, you also notice three oval yellowish-purple bruises over his lumbar spine and lower ribs.\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Escalate immediately to the on-call paediatric registrar/consultant and the hospital Named Doctor or safeguarding team.",
            "Arrange for the child to be admitted to the paediatric ward (as a place of safety) while a full child protection assessment and skeletal survey are coordinated.",
            "Document the history verbatim from both adults and record the exact size, colour, shape, and site of every bruise on a body map in the clinical notes.",
            "Accuse the mother's partner directly of physically abusing the child and demand a confession.",
            "Discharge the child home in a collar-and-cuff sling with an outpatient fracture clinic appointment in 1 week.",
            "Examine only the left arm and avoid undressing the toddler so you do not upset the parents.",
            "Promise the mother that you will keep your concerns confidential between you and the paediatric team and will not involve Children's Social Care.",
            "Wait until the fracture has healed in 6 weeks before raising any safeguarding concerns."
        ],
        "correct_answer": [
            "Escalate immediately to the on-call paediatric registrar/consultant and the hospital Named Doctor or safeguarding team.",
            "Arrange for the child to be admitted to the paediatric ward (as a place of safety) while a full child protection assessment and skeletal survey are coordinated.",
            "Document the history verbatim from both adults and record the exact size, colour, shape, and site of every bruise on a body map in the clinical notes."
        ],
        "explanation": "A spiral humeral fracture in a toddler combined with delayed presentation, an inconsistent/changing mechanism incompatible with developmental stage, and bruising over non-bony torso sites (lumbar spine/ribs—'TEN-4' bruising regions) are strong red flags for non-accidental injury (NAI). The three essential steps are:\n1. Immediate escalation to the senior paediatric team and safeguarding lead.\n2. Admitting the child to a place of safety (paediatric ward) while statutory child protection investigations (social care referral, strategy discussion, skeletal survey, ophthalmology review, coagulation screen) take place.\n3. Meticulous, objective contemporaneous documentation (verbatim accounts and a body map of all cutaneous injuries) without confronting/accusing the caregivers directly in a way that could endanger the child or compromise a forensic investigation."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor on a trauma ward. While taking arterial blood gas samples from a conscious, capacitous 34-year-old man with a known history of intravenous drug use, your gloved finger is punctured deeply by the hollow-bore needle after removing it from his radial artery.\n\nSelect the THREE most appropriate actions to take in response to this needle-stick injury.",
        "options": [
            "Encourage the puncture site to bleed gently by squeezing around it under running warm water and wash with soap, without scrubbing or sucking the wound.",
            "Report the injury immediately to Occupational Health (or the Emergency Department if out of hours) to have your blood-borne virus risk assessed and start post-exposure prophylaxis (PEP) if indicated.",
            "Ask another member of the clinical team (not yourself) to approach the patient to explain the incident and seek his informed consent for blood-borne virus (HIV, hepatitis B, and hepatitis C) testing.",
            "Take an extra vial of blood from the patient's arterial line yourself and send it for HIV and hepatitis serology without telling him so he does not feel awkward.",
            "Wait 3 months before reporting the injury to see if you develop any viral symptoms first.",
            "Scrub the puncture wound vigorously with a nail brush and neat bleach.",
            "Test the blood already inside the arterial gas syringe for HIV without the patient's consent.",
            "Refuse to treat any further patients with a history of substance misuse for the rest of your rotation."
        ],
        "correct_answer": [
            "Encourage the puncture site to bleed gently by squeezing around it under running warm water and wash with soap, without scrubbing or sucking the wound.",
            "Report the injury immediately to Occupational Health (or the Emergency Department if out of hours) to have your blood-borne virus risk assessed and start post-exposure prophylaxis (PEP) if indicated.",
            "Ask another member of the clinical team (not yourself) to approach the patient to explain the incident and seek his informed consent for blood-borne virus (HIV, hepatitis B, and hepatitis C) testing."
        ],
        "explanation": "Following a sharps injury:\n1. Perform immediate first aid: gently encourage bleeding under running water, wash with soap and water (never scrub or suck the wound), and cover with a waterproof dressing.\n2. Contact Occupational Health (or ED out of hours) immediately—HIV post-exposure prophylaxis (PEP) is most effective when started within 1 hour and must be started within 72 hours.\n3. Source-patient testing for HIV, HBV, and HCV requires explicit informed consent in a capacitous patient (under the Human Tissue Act 2004, testing blood without consent is unlawful), and UK guidance specifically states that **another clinician** (not the injured healthcare worker) should obtain that consent to avoid placing undue emotional pressure on the patient."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are a GP trainee. Halfway through a consultation with a 58-year-old man discussing newly diagnosed heart failure, you notice that his smartphone on the desk has its voice-recorder app actively running and recording your conversation. He did not ask you beforehand.\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Acknowledge the recording calmly and non-defensively, and ask him what prompted him to record the consultation (for example, anxiety about forgetting complex medical information).",
            "Reassure him that he is welcome to record the consultation openly for his personal use to help remember the plan, and offer to also provide a written summary or patient information leaflet.",
            "Continue the consultation professionally and document in the clinical records that the consultation was audio-recorded by the patient.",
            "Demand that he hand over his phone and delete the audio file in front of you before you will prescribe his heart failure medication.",
            "Terminate the consultation immediately and remove him from the practice list for a breach of trust.",
            "Call practice security to confiscate his smartphone under the Data Protection Act.",
            "Refuse to speak for the remainder of the appointment and communicate only by typing on your screen.",
            "Threaten him with legal action for recording you without written permission."
        ],
        "correct_answer": [
            "Acknowledge the recording calmly and non-defensively, and ask him what prompted him to record the consultation (for example, anxiety about forgetting complex medical information).",
            "Reassure him that he is welcome to record the consultation openly for his personal use to help remember the plan, and offer to also provide a written summary or patient information leaflet.",
            "Continue the consultation professionally and document in the clinical records that the consultation was audio-recorded by the patient."
        ],
        "explanation": "Medical defence organisations (MDU/MPS) and the BMA highlight that the clinical information discussed in a consultation belongs to the patient (it is *their* personal data), so a patient recording a consultation for their own personal use does not breach data protection law. Most patients record consultations because they are anxious, hard of hearing, or worried about forgetting complex advice, or want to share the explanation with a relative. The most professional approach is to:\n1. Address it calmly and explore why they felt the need to record covertly.\n2. Reassure them that open recording is fine and offer written summaries/leaflets to support understanding.\n3. Deliver the same high standard of care and note in the medical record that the consultation was recorded."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor working in the Emergency Department. A uniformed police officer approaches the reception desk and asks you for the names, addresses, and clinical notes of all patients who have attended the department over the last 48 hours with a dog bite, because a local resident reported being bitten by an off-lead dog in the park yesterday and the police are trying to trace other potential victims or the owner. The officer does not have a court order or patient consent.\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Politely decline to release the names, addresses, or clinical records of patients without their consent or a court order/statutory requirement.",
            "Explain to the police officer that confidentiality can only be breached without consent in the public interest if there is a risk of death or very serious harm (such as gun or knife wounds or terrorism), and ask if they can provide further details or obtain a court order.",
            "Consult the Emergency Department consultant on call or the hospital Caldicott Guardian/information governance team and document the police request.",
            "Print out the full Emergency Department attendance list for the last 48 hours and hand it to the officer immediately.",
            "Give the officer the names and phone numbers verbally so there is no paper trail of the disclosure.",
            "Access the electronic health records of all dog-bite patients from the last week and leave the computer screen unlocked while you go for a coffee so the officer can read it.",
            "Tell the officer that doctors are never allowed to speak to the police even if there is a court order.",
            "Call the patients yourself and tell them the police will arrest them if they do not go to the police station."
        ],
        "correct_answer": [
            "Politely decline to release the names, addresses, or clinical records of patients without their consent or a court order/statutory requirement.",
            "Explain to the police officer that confidentiality can only be breached without consent in the public interest if there is a risk of death or very serious harm (such as gun or knife wounds or terrorism), and ask if they can provide further details or obtain a court order.",
            "Consult the Emergency Department consultant on call or the hospital Caldicott Guardian/information governance team and document the police request."
        ],
        "explanation": "Under GMC *Confidentiality* guidance, the police have no automatic right to access patient health records without the patient's explicit consent unless disclosure is required by statute, ordered by a judge/court, or justified in the public interest to prevent or detect a *very serious crime* (such as murder, manslaughter, rape, child abuse, or gun/knife attacks—where the GMC has specific gunshot and knife wound reporting guidance). A general fishing enquiry for dog-bite attendees without consent or a court order does not meet that threshold. You should:\n1. Politely decline immediate disclosure.\n2. Explain the threshold for disclosure without consent (consent, court order, or serious risk of death/serious harm).\n3. Seek advice from your senior consultant or Caldicott Guardian and document the interaction."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY1 doctor. While scrolling through Instagram during your lunch break, you see a public story posted 20 minutes ago by a final-year medical student attached to your firm. The photo shows the student smiling in scrubs at the nurses' station with the caption 'Surviving another long ward round!'. In the background behind his shoulder, the ward patient whiteboard is clearly visible and legible, showing several patients' full names, bed numbers, and diagnoses.\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Contact the medical student immediately in private, explain that patient names and diagnoses are visible on the whiteboard in the background, and ask him to delete the post straight away.",
            "Inform your supervising consultant or clinical supervisor and report the inadvertent data breach via the hospital incident reporting system (Datix) in line with information governance policy.",
            "Discuss GMC guidance on social media and patient confidentiality with the student so he understands why taking photographs in clinical areas is unsafe.",
            "Leave a public comment underneath the Instagram post listing which patients' names are visible so his followers know it was an accident.",
            "Screenshot the post and share it in the hospital junior doctors' WhatsApp group to warn everyone about the student.",
            "Ignore the post because the student did not intend to show the whiteboard and stories disappear after 24 hours anyway.",
            "Tell the ward sister that you took the photo yourself so the medical student does not get into trouble with the university.",
            "Delete the patients' names from the physical ward whiteboard so they no longer match the photograph."
        ],
        "correct_answer": [
            "Contact the medical student immediately in private, explain that patient names and diagnoses are visible on the whiteboard in the background, and ask him to delete the post straight away.",
            "Inform your supervising consultant or clinical supervisor and report the inadvertent data breach via the hospital incident reporting system (Datix) in line with information governance policy.",
            "Discuss GMC guidance on social media and patient confidentiality with the student so he understands why taking photographs in clinical areas is unsafe."
        ],
        "explanation": "Accidental visibility of patient-identifiable data (whiteboards, computer screens, notes) in clinical selfies is a common and serious confidentiality and UK GDPR breach covered by GMC social media guidance.\n1. The immediate priority is damage limitation: contact the student privately right away so the public post is removed immediately.\n2. Because patient-identifiable data was published online, you must escalate to the clinical supervisor and log an information governance incident (Datix) as required by trust policy.\n3. Providing constructive educational feedback on GMC social media rules helps prevent future breaches. Sharing screenshots on WhatsApp only propagates the data breach further, and taking false blame is dishonest."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are a surgical FY2 doctor in the pre-operative assessment clinic reviewing a 62-year-old woman scheduled for an elective total hip replacement in 2 weeks. She is a practising Jehovah's Witness with full mental capacity and presents a valid, signed, and witnessed Advance Decision to Refuse Treatment (ADRT) stating that she refuses transfusion of whole blood, red cells, white cells, platelets, and plasma under all circumstances, even if her life is at risk. Her preoperative haemoglobin is 108 g/L with a low mean cell volume (MCV 74 fL) and low serum ferritin.\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Respect her autonomous refusal of blood products, ensure a copy of her valid ADRT is placed prominently in her notes, and discuss specifically which blood-conservation modalities (such as intraoperative cell salvage or tranexamic acid) she does or does not accept.",
            "Optimise her preoperative haemoglobin before surgery by investigating and treating her iron-deficiency anaemia (e.g. with oral or intravenous iron therapy).",
            "Inform the consultant orthopaedic surgeon and consultant anaesthetist early so that a multidisciplinary bloodless-surgery perioperative plan can be agreed in advance.",
            "Tell her that if she suffers life-threatening haemorrhage while under general anaesthesia, the anaesthetist will override her wishes and transfuse red cells to save her life.",
            "Wait until she is unconscious in theatre and then ask her non-Jehovah's Witness husband to consent to a blood transfusion on her behalf.",
            "Apply to the Court of Protection to have her sectioned under the Mental Health Act so she can be transfused.",
            "Cancel her hip replacement permanently and discharge her without discussing the case with the surgical or anaesthetic consultants.",
            "Prescribe a preoperative red blood cell transfusion disguised in an opaque bag and tell her it is intravenous saline."
        ],
        "correct_answer": [
            "Respect her autonomous refusal of blood products, ensure a copy of her valid ADRT is placed prominently in her notes, and discuss specifically which blood-conservation modalities (such as intraoperative cell salvage or tranexamic acid) she does or does not accept.",
            "Optimise her preoperative haemoglobin before surgery by investigating and treating her iron-deficiency anaemia (e.g. with oral or intravenous iron therapy).",
            "Inform the consultant orthopaedic surgeon and consultant anaesthetist early so that a multidisciplinary bloodless-surgery perioperative plan can be agreed in advance."
        ],
        "explanation": "A capacitous adult has an absolute legal and ethical right to refuse any medical treatment—even if that refusal may result in their death—and a valid, applicable Advance Decision to Refuse Treatment (ADRT) is legally binding under the Mental Capacity Act 2005 (transfusing against it constitutes battery). Individual Jehovah's Witnesses differ on whether they accept autologous techniques like continuous-circuit intraoperative cell salvage or pharmacological adjuncts (tranexamic acid, erythropoietin), so:\n1. Document the ADRT and clarify each specific product/modality on an itemised check-list.\n2. Optimise her preoperative iron-deficiency anaemia ahead of elective surgery.\n3. Alert the consultant surgeon and anaesthetist early to plan safe blood-conserving surgery."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are an FY2 doctor on a cardiology ward. A wealthy 69-year-old businessman whom you looked after during his recovery from an acute myocardial infarction is being discharged today. As he shakes your hand to say thank you, he hands you a sealed envelope containing £500 in cash and says, 'You've been brilliant to me all week—treat yourself to a proper holiday, I won't take no for an answer.'\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Thank the patient warmly for his kindness and appreciation, but politely decline the personal cash gift, explaining that hospital policy and GMC guidance do not permit doctors to accept significant personal gifts or cash.",
            "Explain that if he wishes to show his appreciation financially, he is very welcome to make a donation to the hospital charity or the ward staff fund (which benefits the whole team or patient amenities) via the official channels.",
            "Inform your consultant or clinical supervisor of the offered cash gift and record the conversation and your refusal in the clinical notes or gift register in line with trust policy.",
            "Accept the £500 cash quietly and put it in your pocket so you do not offend the patient.",
            "Accept the £500 cash on condition that you give the patient your personal mobile number for private medical advice at home.",
            "Take £100 for yourself and leave the remaining £400 loose in the staff room biscuit tin without telling anyone.",
            "Refuse to give the patient his discharge medications unless he takes the envelope back immediately.",
            "Ask the patient to transfer the £500 via bank transfer instead so it is not physical cash."
        ],
        "correct_answer": [
            "Thank the patient warmly for his kindness and appreciation, but politely decline the personal cash gift, explaining that hospital policy and GMC guidance do not permit doctors to accept significant personal gifts or cash.",
            "Explain that if he wishes to show his appreciation financially, he is very welcome to make a donation to the hospital charity or the ward staff fund (which benefits the whole team or patient amenities) via the official channels.",
            "Inform your consultant or clinical supervisor of the offered cash gift and record the conversation and your refusal in the clinical notes or gift register in line with trust policy."
        ],
        "explanation": "Under GMC *Financial and commercial arrangements and conflicts of interest* guidance and NHS Standards of Business Conduct, while trivial token gifts of low intrinsic value (e.g. a box of chocolates or thank-you card shared with the ward team) are generally acceptable, doctors must decline cash or high-value personal gifts that could affect—or be perceived to affect—the doctor-patient relationship or public trust.\n1. Thank the patient graciously so they do not feel rejected, while politely declining the £500 cash.\n2. Redirect their generosity toward the official hospital charity or ward fund if they wish.\n3. Inform your senior/supervisor and document the interaction transparently to protect your probity."
    },
    {
        "exam": "MSRA",
        "type": "selection",
        "category": "Professional Dilemmas",
        "scenario": "You are a newly qualified GP partner at a large suburban practice. A pharmaceutical company representative books an appointment to see you and offers to pay for an all-expenses-paid weekend at a 5-star golf and spa hotel—described as an 'anticoagulation advisory retreat' with a 30-minute presentation on Saturday morning—if you agree to switch your practice's atrial fibrillation patients from generic apixaban to their newly launched, significantly more expensive branded direct oral anticoagulant.\n\nSelect the THREE most appropriate actions to take in this situation.",
        "options": [
            "Decline the offer of the luxury hotel weekend and refuse to enter into any agreement linking personal hospitality to prescribing changes.",
            "Explain that any prescribing changes in the practice are based strictly on clinical evidence, patient safety, and local ICB/NICE formulary guidance rather than commercial incentives.",
            "Inform your fellow GP partners (and practice governance lead) about the representative's inappropriate inducement.",
            "Accept the luxury spa weekend, attend the 30-minute talk, and switch 50 patients to the new drug on Monday morning.",
            "Ask the representative to pay the value of the hotel trip directly into your personal bank account instead so nobody sees you at the hotel.",
            "Switch all the practice's patients to the branded drug without checking their renal function or informing them.",
            "Accept the trip for yourself and your partner, and omit it from the practice's register of conflicts of interest.",
            "Agree to switch patients only if the pharmaceutical company also buys new laptops for the reception desk."
        ],
        "correct_answer": [
            "Decline the offer of the luxury hotel weekend and refuse to enter into any agreement linking personal hospitality to prescribing changes.",
            "Explain that any prescribing changes in the practice are based strictly on clinical evidence, patient safety, and local ICB/NICE formulary guidance rather than commercial incentives.",
            "Inform your fellow GP partners (and practice governance lead) about the representative's inappropriate inducement."
        ],
        "explanation": "Both GMC guidance (*Financial and commercial arrangements and conflicts of interest*) and the ABPI Code of Practice strictly prohibit doctors from asking for or accepting any inducement, gift, or excessive hospitality that may affect or be seen to affect the way they prescribe for, treat, or refer patients.\n1. Refuse the luxury spa hospitality and any quid-pro-quo prescribing arrangement.\n2. Reiterate that prescribing decisions must be governed solely by clinical need, NICE/local formulary evidence, and best use of NHS resources.\n3. Alert your fellow GP partners/governance lead so the practice is aware of the inappropriate approach."
    }
]
