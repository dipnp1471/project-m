# -*- coding: utf-8 -*-
"""
Part 4: High-Yield Pathognomonic Questions
60 challenging questions focusing on classic pathognomonic signs and high-yield findings.
5 questions for each of the 12 clinical domains.
"""

CLINICAL_QUESTIONS = [
    # =========================================================================
    # 1. CARDIOVASCULAR
    # =========================================================================
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 3-week-old infant is brought in with poor feeding, sweating during feeds, and cyanosis that worsens with crying. A chest X-ray reveals a 'boot-shaped heart' with upturned cardiac apex and decreased pulmonary vascular markings. What is the most likely diagnosis?",
        "options": [
            "Tetralogy of Fallot",
            "Transposition of the Great Arteries",
            "Truncus Arteriosus",
            "Coarctation of the Aorta",
            "Atrial Septal Defect"
        ],
        "correct_answer": "Tetralogy of Fallot",
        "explanation": "A 'boot-shaped heart' (coeur en sabot) on a chest X-ray is classic for Tetralogy of Fallot, caused by right ventricular hypertrophy and a small main pulmonary artery segment. Symptoms of 'tet spells' (cyanosis during crying/feeding) support this."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 45-year-old woman presents with severe dyspnoea. She recently had a viral upper respiratory infection. Her blood pressure is 85/55 mmHg, heart rate is 120 bpm, and neck veins are distended. An ECG shows sinus tachycardia with alternating amplitude of the QRS complexes in consecutive beats. What is the most definitive immediate treatment?",
        "options": [
            "Pericardiocentesis",
            "Intravenous Furosemide",
            "Intravenous Amiodarone",
            "Synchronised DC Cardioversion",
            "High-dose oral Ibuprofen"
        ],
        "correct_answer": "Pericardiocentesis",
        "explanation": "The patient has Beck's triad (hypotension, distended neck veins, muffled heart sounds—implied) and 'electrical alternans' on ECG, which is pathognomonic for cardiac tamponade. The immediate definitive treatment is pericardiocentesis."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 22-year-old man presents with headaches and leg cramps after running. Examination reveals a blood pressure of 170/100 mmHg in the right arm and 110/70 mmHg in the left leg. Palpation of pulses reveals radio-femoral delay. Chest X-ray shows 'notching' of the inferior aspect of the posterior ribs. What is the diagnosis?",
        "options": [
            "Coarctation of the Aorta",
            "Aortic Dissection",
            "Takayasu Arteritis",
            "Fibromuscular Dysplasia",
            "Patent Ductus Arteriosus"
        ],
        "correct_answer": "Coarctation of the Aorta",
        "explanation": "Radio-femoral delay, upper limb hypertension with lower limb hypotension, and rib notching on CXR (due to collateral flow through dilated intercostal arteries) are classic pathognomonic signs of coarctation of the aorta."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 60-year-old man presents with sharp pleuritic chest pain. He had a myocardial infarction 4 weeks ago. An echocardiogram shows a large accumulation of fluid in the pericardial sac. A chest X-ray demonstrates an enlarged globular cardiac silhouette, often described as a 'water bottle' heart. What is the underlying immunological process?",
        "options": [
            "Dressler's syndrome",
            "Acute viral pericarditis",
            "Rheumatic fever",
            "Systemic lupus erythematosus",
            "Uraemic pericarditis"
        ],
        "correct_answer": "Dressler's syndrome",
        "explanation": "Post-myocardial infarction syndrome (Dressler's syndrome) is an autoimmune fibrinous pericarditis that typically occurs 2-10 weeks post-MI. A 'water bottle' heart on CXR indicates a large pericardial effusion."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 35-year-old woman from South America presents with progressive dysphagia and constipation. She recently developed right bundle branch block on ECG and signs of dilated cardiomyopathy. She reports being bitten by a 'kissing bug' in childhood. What is the most likely causative organism?",
        "options": [
            "Trypanosoma cruzi",
            "Borrelia burgdorferi",
            "Plasmodium falciparum",
            "Leishmania donovani",
            "Toxoplasma gondii"
        ],
        "correct_answer": "Trypanosoma cruzi",
        "explanation": "Trypanosoma cruzi causes Chagas disease. It presents years after infection with dilated cardiomyopathy (often with RBBB or apical aneurysm), megaoesophagus, and megacolon."
    },

    # =========================================================================
    # 2. DERMATOLOGY / ENT / OPHTHALMOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 25-year-old man presents with a mild pruritic rash. It began 10 days ago as a single 3 cm oval, salmon-coloured scaly patch on his chest. Yesterday, a widespread eruption of smaller scaly macules appeared on his trunk along the lines of cleavage, giving a 'Christmas tree' distribution. What is the most likely diagnosis?",
        "options": [
            "Pityriasis rosea",
            "Guttate psoriasis",
            "Tinea corporis",
            "Secondary syphilis",
            "Nummular eczema"
        ],
        "correct_answer": "Pityriasis rosea",
        "explanation": "A 'herald patch' followed by a 'Christmas tree' distribution of oval, scaly plaques is pathognomonic for Pityriasis rosea. It is self-limiting."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 70-year-old man presents with sudden, painless, profound loss of vision in his right eye. Examination of the fundus reveals a pale, opaque retina with a distinct 'cherry-red spot' at the macula. What is the most likely diagnosis?",
        "options": [
            "Central retinal artery occlusion",
            "Central retinal vein occlusion",
            "Retinal detachment",
            "Macular degeneration",
            "Amaurosis fugax"
        ],
        "correct_answer": "Central retinal artery occlusion",
        "explanation": "A pale, infarcted retina with a 'cherry-red spot' (the fovea receiving its blood supply from the underlying choroid) is the classic pathognomonic finding of Central Retinal Artery Occlusion (CRAO)."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 4-year-old unimmunised boy is brought to the GP with a 3-day history of high fever, coryza, cough, and conjunctivitis. On examination of the oral mucosa, tiny white spots resembling grains of salt on a red background are seen on the buccal mucosa opposite the molars. What are these spots called?",
        "options": [
            "Koplik spots",
            "Forchheimer spots",
            "Pastia's lines",
            "Slapped cheek",
            "Strawberry tongue"
        ],
        "correct_answer": "Koplik spots",
        "explanation": "Koplik spots are pathognomonic for the prodromal phase of Measles. They appear 1-2 days before the onset of the maculopapular rash."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 65-year-old man with long-standing poorly controlled hypertension attends for a routine eye check. Fundoscopy shows thickening of the retinal arterioles causing compression of the venules where they cross. What is this specific finding known as?",
        "options": [
            "AV nipping (nipping/nicking)",
            "Cotton wool spots",
            "Hard exudates",
            "Flame haemorrhages",
            "Drusen"
        ],
        "correct_answer": "AV nipping (nipping/nicking)",
        "explanation": "Arteriovenous (AV) nipping is a classic sign of hypertensive retinopathy. It occurs because the thickened arteriole compresses the underlying venule."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 55-year-old farmer presents with a slowly growing nodule on his upper lip. On examination, it is a 1 cm nodule with a 'pearly, rolled edge' and visible fine telangiectasia across its surface. The centre is slightly ulcerated. What is the most likely diagnosis?",
        "options": [
            "Basal cell carcinoma",
            "Squamous cell carcinoma",
            "Malignant melanoma",
            "Keratoacanthoma",
            "Actinic keratosis"
        ],
        "correct_answer": "Basal cell carcinoma",
        "explanation": "A nodule with a 'pearly, rolled edge' and arborising telangiectasia, typically on sun-exposed areas, is the classic pathognomonic description of a nodular Basal Cell Carcinoma."
    },

    # =========================================================================
    # 3. ENDOCRINOLOGY / METABOLIC
    # =========================================================================
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 42-year-old woman undergoes a fine needle aspiration (FNA) of a solitary thyroid nodule. Histology reports large cells with 'empty' appearing nuclei, described as 'Orphan Annie eye' nuclei, and calcified structures known as psammoma bodies. What is the diagnosis?",
        "options": [
            "Papillary thyroid carcinoma",
            "Follicular thyroid carcinoma",
            "Medullary thyroid carcinoma",
            "Anaplastic thyroid carcinoma",
            "Hashimoto's thyroiditis"
        ],
        "correct_answer": "Papillary thyroid carcinoma",
        "explanation": "'Orphan Annie eye' nuclei (optically clear nuclei) and psammoma bodies (concentrically calcified structures) are pathognomonic histological features of Papillary thyroid carcinoma, the most common type of thyroid cancer."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 35-year-old woman presents with palpitations, weight loss, and heat intolerance. On examination, she has bilateral exophthalmos and a raised, thickened, non-pitting, red plaque on her shins. What is the specific term for the finding on her shins?",
        "options": [
            "Pretibial myxoedema",
            "Erythema nodosum",
            "Necrobiosis lipoidica",
            "Pyoderma gangrenosum",
            "Acanthosis nigricans"
        ],
        "correct_answer": "Pretibial myxoedema",
        "explanation": "Pretibial myxoedema (thyroid dermopathy) is an infiltrative dermopathy pathognomonic for Graves' disease, almost always occurring in association with Graves' ophthalmopathy."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 55-year-old man presents with fatigue, joint pains, and erectile dysfunction. On examination, he has a slate-grey hyperpigmentation of his skin. Blood tests show significantly elevated ferritin and fasting blood glucose is 14 mmol/L. This presentation is classically referred to as 'bronze diabetes'. What is the underlying condition?",
        "options": [
            "Haemochromatosis",
            "Addison's disease",
            "Cushing's syndrome",
            "Wilson's disease",
            "Acromegaly"
        ],
        "correct_answer": "Haemochromatosis",
        "explanation": "The triad of skin hyperpigmentation, diabetes mellitus ('bronze diabetes'), and liver cirrhosis (or other end-organ damage like arthropathy or hypogonadism) is classic for late-stage Haemochromatosis due to iron deposition."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 28-year-old woman undergoes a total thyroidectomy. On post-operative day 2, she complains of tingling around her mouth and in her fingers. When taking her blood pressure, inflation of the cuff above systolic pressure causes carpal spasm. What is this sign called?",
        "options": [
            "Trousseau's sign",
            "Chvostek's sign",
            "Homan's sign",
            "Phalen's sign",
            "Tinel's sign"
        ],
        "correct_answer": "Trousseau's sign",
        "explanation": "Trousseau's sign is carpopedal spasm induced by ischaemia (inflating a BP cuff), and is a highly specific, classic sign of latent hypocalcaemia, which here is likely due to inadvertent parathyroid injury during thyroidectomy."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 60-year-old woman presents with bone pain, renal colic, and constipation. She reports feeling increasingly depressed and lethargic. Serum biochemistry shows hypercalcaemia. Her constellation of symptoms is historically described as 'moans, groans, stones, and bones'. What is the most likely diagnosis?",
        "options": [
            "Primary hyperparathyroidism",
            "Multiple myeloma",
            "Vitamin D deficiency",
            "Paget's disease",
            "Osteoporosis"
        ],
        "correct_answer": "Primary hyperparathyroidism",
        "explanation": "The mnemonic 'bones, stones, abdominal groans, and psychiatric moans' is classic for hypercalcaemia. In a community setting, the most common cause is Primary hyperparathyroidism."
    },

    # =========================================================================
    # 4. GASTROENTEROLOGY / NUTRITION
    # =========================================================================
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 24-year-old man presents with chronic bloody diarrhoea. A barium enema reveals complete loss of haustral markings throughout the descending and sigmoid colon, giving it the appearance of a smooth, rigid tube. What is the classical name for this radiological finding?",
        "options": [
            "Lead pipe colon",
            "String sign",
            "Thumbprinting",
            "Apple core lesion",
            "Bird's beak sign"
        ],
        "correct_answer": "Lead pipe colon",
        "explanation": "A 'lead pipe' appearance on contrast enema is pathognomonic for chronic Ulcerative Colitis, resulting from long-standing inflammation causing fibrosis and loss of haustra."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 28-year-old woman presents with abdominal pain and weight loss. Colonoscopy reveals transmural inflammation with deep fissuring ulcers interspersed with normal mucosa, giving a 'cobblestone' appearance. A barium follow-through shows severe stricturing of the terminal ileum. What is the stricture known as?",
        "options": [
            "String sign of Kantor",
            "Lead pipe sign",
            "Whirlpool sign",
            "Rigler's sign",
            "Coffee bean sign"
        ],
        "correct_answer": "String sign of Kantor",
        "explanation": "The 'string sign' on a barium series indicates severe narrowing of a bowel loop, classically seen in the terminal ileum in Crohn's disease due to spasm and transmural fibrosis. 'Cobblestoning' is also classic."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 68-year-old man presents with iron deficiency anaemia and altered bowel habit. A barium enema demonstrates a short segment of severe, circumferential irregular narrowing in the descending colon with overhanging edges. What is the classic term for this appearance?",
        "options": [
            "Apple core lesion",
            "Bird's beak deformity",
            "Corkscrew appearance",
            "Stack of coins sign",
            "Target sign"
        ],
        "correct_answer": "Apple core lesion",
        "explanation": "An 'apple core' lesion on a barium enema is a pathognomonic sign of a circumferential, stenosing colorectal carcinoma."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 19-year-old man presents with tremors and signs of chronic liver disease. Slit-lamp examination of the eyes reveals golden-brown rings at the periphery of the cornea in Descemet's membrane. What are these rings called?",
        "options": [
            "Kayser-Fleischer rings",
            "Lisch nodules",
            "Arcus senilis",
            "Brushfield spots",
            "Band keratopathy"
        ],
        "correct_answer": "Kayser-Fleischer rings",
        "explanation": "Kayser-Fleischer rings are a pathognomonic sign of Wilson's disease, caused by copper deposition in Descemet's membrane of the cornea."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 45-year-old woman presents with intermittent dysphagia for both solids and liquids, along with retrosternal chest pain. A barium swallow reveals multiple uncoordinated contractions, giving the oesophagus a 'corkscrew' or 'rosary bead' appearance. What is the diagnosis?",
        "options": [
            "Diffuse oesophageal spasm",
            "Achalasia",
            "Oesophageal web",
            "Systemic sclerosis",
            "Myasthenia gravis"
        ],
        "correct_answer": "Diffuse oesophageal spasm",
        "explanation": "A 'corkscrew' or 'rosary bead' oesophagus on barium swallow is pathognomonic for Diffuse Oesophageal Spasm (DOS), caused by uncoordinated, simultaneous contractions."
    },

    # =========================================================================
    # 5. INFECTIOUS DISEASE / HAEMATOLOGY / IMMUNOLOGY / GENETICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 65-year-old man presents with fatigue and bleeding gums. A full blood count shows a low haemoglobin, thrombocytopenia, and leukocytosis. A blood film reveals large blast cells with prominent nucleoli and distinct, needle-like eosinophilic inclusions in the cytoplasm. What are these inclusions called?",
        "options": [
            "Auer rods",
            "Howell-Jolly bodies",
            "Heinz bodies",
            "Döhle bodies",
            "Basophilic stippling"
        ],
        "correct_answer": "Auer rods",
        "explanation": "Auer rods are needle-like crystallised azurophilic granules found in the cytoplasm of myeloblasts, pathognomonic for Acute Myeloid Leukaemia (AML)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 25-year-old woman presents with a painless, enlarged cervical lymph node and night sweats. A lymph node biopsy demonstrates large, binucleate cells with prominent eosinophilic nucleoli giving an 'owl-eye' appearance. What is the specific name of these cells?",
        "options": [
            "Reed-Sternberg cells",
            "Langhans giant cells",
            "Aschoff cells",
            "Kupffer cells",
            "Gaucher cells"
        ],
        "correct_answer": "Reed-Sternberg cells",
        "explanation": "Reed-Sternberg cells ('owl-eye' cells) are the hallmark, pathognomonic malignant cells found in Hodgkin's lymphoma."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "An asymptomatic 70-year-old man is found to have a significantly elevated lymphocyte count on a routine blood test. A peripheral blood smear shows many mature-appearing small lymphocytes alongside fragile, disrupted lymphocytes. What is the term for these disrupted cells?",
        "options": [
            "Smudge cells",
            "Bite cells",
            "Target cells",
            "Teardrop cells",
            "Schistocytes"
        ],
        "correct_answer": "Smudge cells",
        "explanation": "Smudge cells (or smear cells) are fragile lymphocytes disrupted during the making of the blood film. They are classically associated with Chronic Lymphocytic Leukaemia (CLL)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 68-year-old man presents with severe back pain and lethargy. Investigations reveal hypercalcaemia and impaired renal function. Urine electrophoresis identifies monoclonal free light chains. What is the eponymous name for these light chains?",
        "options": [
            "Bence Jones proteins",
            "Tamm-Horsfall proteins",
            "Cryoglobulins",
            "B2-microglobulin",
            "Alpha-fetoprotein"
        ],
        "correct_answer": "Bence Jones proteins",
        "explanation": "Bence Jones proteins are monoclonal free light chains found in the urine, classic for Multiple Myeloma."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 22-year-old man of Mediterranean descent develops jaundice and dark urine after starting nitrofurantoin for a UTI. A peripheral blood smear shows 'bite cells' and special staining reveals denatured haemoglobin aggregates within red blood cells. What are these aggregates called?",
        "options": [
            "Heinz bodies",
            "Howell-Jolly bodies",
            "Pappenheimer bodies",
            "Cabot rings",
            "Schüffner's dots"
        ],
        "correct_answer": "Heinz bodies",
        "explanation": "Heinz bodies (oxidised, denatured haemoglobin) and 'bite cells' (where the spleen has taken a 'bite' to remove the Heinz body) are pathognomonic for G6PD deficiency undergoing oxidative stress."
    },

    # =========================================================================
    # 6. MUSCULOSKELETAL
    # =========================================================================
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 30-year-old man presents with chronic lower back pain that is worse in the morning and improves with exercise. A radiograph of his lumbar spine reveals fusion of the vertebral bodies, ossification of the longitudinal ligaments, and squaring of the vertebrae. What is the classic term for this appearance?",
        "options": [
            "Bamboo spine",
            "Rugger jersey spine",
            "Picture frame vertebra",
            "Ivory vertebra",
            "Codfish vertebrae"
        ],
        "correct_answer": "Bamboo spine",
        "explanation": "'Bamboo spine' is the pathognomonic radiographic sign of advanced Ankylosing Spondylitis, due to syndesmophyte formation and fusion of the spine."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 55-year-old woman with chronic joint pain presents for a review. Examination of her hands reveals flexion of the proximal interphalangeal (PIP) joints and hyperextension of the distal interphalangeal (DIP) joints. What is this deformity called?",
        "options": [
            "Boutonniere deformity",
            "Swan neck deformity",
            "Mallet finger",
            "Z-thumb deformity",
            "Heberden's nodes"
        ],
        "correct_answer": "Boutonniere deformity",
        "explanation": "A Boutonniere (buttonhole) deformity is flexion at the PIP and hyperextension at the DIP, a classic advanced sign of Rheumatoid Arthritis. (Swan neck is the reverse: hyperextension at PIP, flexion at DIP)."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 70-year-old woman complains of pain at the base of her thumbs. Examination shows hard, bony swellings on the distal interphalangeal (DIP) joints. What are these specific swellings called?",
        "options": [
            "Heberden's nodes",
            "Bouchard's nodes",
            "Osler's nodes",
            "Rheumatoid nodules",
            "Tophi"
        ],
        "correct_answer": "Heberden's nodes",
        "explanation": "Heberden's nodes are osteophytes at the DIP joints, classic for Osteoarthritis. Bouchard's nodes occur at the PIP joints."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 60-year-old man presents with an exquisitely painful, red, swollen first metatarsophalangeal joint. Aspiration of the joint reveals fluid that, under polarised light microscopy, shows strongly negatively birefringent, needle-shaped crystals. What is the diagnosis?",
        "options": [
            "Gout",
            "Pseudogout",
            "Septic arthritis",
            "Rheumatoid arthritis",
            "Osteoarthritis"
        ],
        "correct_answer": "Gout",
        "explanation": "Negatively birefringent, needle-shaped monosodium urate crystals are pathognomonic for Gout. Pseudogout features positively birefringent, rhomboid-shaped CPPD crystals."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 75-year-old woman presents with an acutely swollen and painful right knee. A radiograph shows a thin layer of calcification within the articular cartilage. Joint aspiration reveals weakly positive birefringent, rhomboid-shaped crystals. What is the diagnosis?",
        "options": [
            "Pseudogout",
            "Gout",
            "Septic arthritis",
            "Reactive arthritis",
            "Osteoarthritis"
        ],
        "correct_answer": "Pseudogout",
        "explanation": "Weakly positively birefringent, rhomboid-shaped calcium pyrophosphate dihydrate (CPPD) crystals, alongside chondrocalcinosis on X-ray, are pathognomonic for Pseudogout."
    },

    # =========================================================================
    # 7. PAEDIATRICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A newborn with Down's syndrome develops bilious vomiting shortly after birth. An abdominal radiograph reveals two large air-filled spaces in the upper abdomen and an absence of distal bowel gas. What is the classic name for this sign?",
        "options": [
            "Double bubble sign",
            "Target sign",
            "String sign",
            "Coffee bean sign",
            "Rigler's sign"
        ],
        "correct_answer": "Double bubble sign",
        "explanation": "The 'double bubble' sign on an abdominal X-ray indicates Duodenal Atresia. The bubbles represent air in the stomach and the dilated proximal duodenum."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 2-year-old boy presents with a barking cough and stridor. An AP neck radiograph is performed to rule out other conditions, and it shows subglottic narrowing. What is the name of this radiological sign?",
        "options": [
            "Steeple sign",
            "Thumbprint sign",
            "Sail sign",
            "Water bottle sign",
            "Silhouette sign"
        ],
        "correct_answer": "Steeple sign",
        "explanation": "The 'steeple sign' (subglottic tracheal narrowing) on an AP neck X-ray is classic for Croup (laryngotracheobronchitis)."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 4-year-old unimmunised girl presents with a high fever, drooling, and leaning forward in a 'tripod' position. She looks toxic. A lateral neck radiograph is taken cautiously and shows an enlarged epiglottis. What is the name of this sign?",
        "options": [
            "Thumbprint sign",
            "Steeple sign",
            "Sail sign",
            "Double bubble sign",
            "Lead pipe sign"
        ],
        "correct_answer": "Thumbprint sign",
        "explanation": "An enlarged epiglottis protruding into the airway on a lateral neck X-ray is called the 'thumbprint sign', classic for acute Epiglottitis (typically Haemophilus influenzae type B)."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 7-month-old infant presents with episodic inconsolable crying, drawing his legs up to his chest, followed by lethargy. He has passed stool that looks like 'red currant jelly'. An abdominal ultrasound shows a 'target' or 'doughnut' sign. What is the diagnosis?",
        "options": [
            "Intussusception",
            "Volvulus",
            "Meckel's diverticulum",
            "Necrotising enterocolitis",
            "Hirschsprung's disease"
        ],
        "correct_answer": "Intussusception",
        "explanation": "'Red currant jelly' stool (blood mixed with mucus) and a 'target/doughnut/bullseye' sign on ultrasound (representing bowel telescoped into bowel) are pathognomonic for Intussusception."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old girl is brought in with mild fever and a bright red macular rash on both cheeks. Two days later, a lacy, reticular rash appears on her arms and trunk. What is the name of the appearance on her face?",
        "options": [
            "Slapped cheek appearance",
            "Koplik spots",
            "Strawberry tongue",
            "Dewdrops on a rose petal",
            "Pastia's lines"
        ],
        "correct_answer": "Slapped cheek appearance",
        "explanation": "A 'slapped cheek' appearance followed by a lacy, maculopapular rash on the body is classic for Erythema Infectiosum (Fifth disease), caused by Parvovirus B19."
    },

    # =========================================================================
    # 8. PHARMACOLOGY / THERAPEUTICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 78-year-old woman with atrial fibrillation is admitted with nausea, vomiting, and visual disturbances, specifically yellow-green halos around objects. Her ECG shows scooped, 'reverse tick' ST-segment depression. What drug toxicity is most likely?",
        "options": [
            "Digoxin",
            "Amiodarone",
            "Flecainide",
            "Sotalol",
            "Verapamil"
        ],
        "correct_answer": "Digoxin",
        "explanation": "Xanthopsia (yellow-green vision) and the 'reverse tick' (scooped) ST depression on ECG are classic signs of Digoxin toxicity or digoxin effect."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 40-year-old man with bipolar disorder is admitted with confusion, ataxia, and a severe coarse tremor. He recently developed a diarrhoeal illness and became dehydrated. Which medication is most likely responsible for his symptoms?",
        "options": [
            "Lithium",
            "Sodium valproate",
            "Lamotrigine",
            "Olanzapine",
            "Carbamazepine"
        ],
        "correct_answer": "Lithium",
        "explanation": "A coarse tremor (as opposed to fine tremor seen at therapeutic levels), ataxia, and confusion, particularly precipitated by dehydration or renal impairment, are classic for Lithium toxicity."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 30-year-old woman with epilepsy presents for a routine check. On examination, you note significant overgrowth of her gums. She also has coarse facial features and mild hirsutism. Which anti-epileptic drug is the likely cause?",
        "options": [
            "Phenytoin",
            "Carbamazepine",
            "Levetiracetam",
            "Sodium valproate",
            "Ethosuximide"
        ],
        "correct_answer": "Phenytoin",
        "explanation": "Gingival hyperplasia, coarse facial features, hirsutism, and nystagmus (in toxicity) are classic side effects pathognomonic of chronic Phenytoin use."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 65-year-old man presents with worsening breathlessness. He has a history of ventricular arrhythmias. Examination reveals a slate-grey discoloration of his skin in sun-exposed areas. A slit-lamp eye examination shows corneal microdeposits. Which medication is he taking?",
        "options": [
            "Amiodarone",
            "Sotalol",
            "Flecainide",
            "Methotrexate",
            "Bleomycin"
        ],
        "correct_answer": "Amiodarone",
        "explanation": "Slate-grey skin discoloration, corneal microdeposits, and pulmonary fibrosis are highly specific, classic side effects of Amiodarone."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 55-year-old diabetic man is started on a new antihypertensive medication. Two weeks later, he develops a persistent, dry, tickly cough that is worse at night. What is the mechanism behind this side effect?",
        "options": [
            "Accumulation of bradykinin",
            "Blockade of substance P",
            "Bronchoconstriction via beta-2 antagonism",
            "Histamine release",
            "Vagal nerve stimulation"
        ],
        "correct_answer": "Accumulation of bradykinin",
        "explanation": "A dry cough is a classic side effect of ACE inhibitors. ACE normally breaks down bradykinin in the lungs; inhibiting ACE leads to bradykinin accumulation, which stimulates cough receptors."
    },

    # =========================================================================
    # 9. PSYCHIATRY / NEUROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 35-year-old man presents with ascending, symmetrical, flaccid weakness of his legs that developed over 3 days, following a Campylobacter jejuni gastroenteritis. A lumbar puncture is performed. What is the classic cerebrospinal fluid (CSF) finding?",
        "options": [
            "Albuminocytologic dissociation",
            "Oligoclonal bands",
            "Xanthochromia",
            "High neutrophils with low glucose",
            "Presence of 14-3-3 protein"
        ],
        "correct_answer": "Albuminocytologic dissociation",
        "explanation": "Albuminocytologic dissociation (highly elevated protein with a normal or mildly elevated white blood cell count) is the pathognomonic CSF finding in Guillain-Barré Syndrome."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 28-year-old woman presents with sudden unilateral visual loss and pain on eye movement. She had a similar episode of right leg weakness 2 years ago that resolved. A lumbar puncture and serum protein electrophoresis are performed. What is the expected pathognomonic finding?",
        "options": [
            "Oligoclonal bands in CSF but not in serum",
            "Albuminocytologic dissociation",
            "Monoclonal gammopathy in serum",
            "Presence of tau proteins",
            "Acellular fluid with low glucose"
        ],
        "correct_answer": "Oligoclonal bands in CSF but not in serum",
        "explanation": "Oligoclonal bands of IgG present in the CSF but absent in the blood indicate intrathecal antibody synthesis and are a classic immunological hallmark of Multiple Sclerosis."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "An autopsy is performed on a 75-year-old man who had a history of resting tremor, rigidity, bradykinesia, and visual hallucinations. Histology of the substantia nigra reveals eosinophilic intracytoplasmic inclusions within neurons. What are these inclusions called?",
        "options": [
            "Lewy bodies",
            "Negri bodies",
            "Neurofibrillary tangles",
            "Pick bodies",
            "Rosenthal fibres"
        ],
        "correct_answer": "Lewy bodies",
        "explanation": "Lewy bodies (aggregates of alpha-synuclein) are the pathognomonic histological hallmark of Parkinson's disease and Lewy Body Dementia."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 45-year-old patient with severe depression is admitted to the psychiatric ward. They are mute, immobile, and hold unusual, awkward postures for hours without showing fatigue. When the doctor lifts the patient's arm, it remains exactly where it was placed. What is this sign called?",
        "options": [
            "Waxy flexibility (Catalepsy)",
            "Cogwheel rigidity",
            "Lead-pipe rigidity",
            "Echopraxia",
            "Spasticity"
        ],
        "correct_answer": "Waxy flexibility (Catalepsy)",
        "explanation": "Waxy flexibility (catalepsy), where a patient's limbs maintain any posture they are placed in, is a classic pathognomonic sign of Catatonia."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A patient dies from progressive encephalitis characterized by hydrophobia, hypersalivation, and pharyngeal spasms after an animal bite in a developing country. Brain biopsy shows eosinophilic cytoplasmic inclusions in the Purkinje cells of the cerebellum and hippocampal neurons. What are they?",
        "options": [
            "Negri bodies",
            "Lewy bodies",
            "Cowdry type A bodies",
            "Hirano bodies",
            "Bunina bodies"
        ],
        "correct_answer": "Negri bodies",
        "explanation": "Negri bodies are pathognomonic for Rabies virus infection."
    },

    # =========================================================================
    # 10. RENAL / UROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 60-year-old man undergoes major abdominal surgery complicated by severe hypotension. Three days later, his creatinine rises from 80 to 450 umol/L. Urine microscopy is performed. What pathognomonic finding confirms Acute Tubular Necrosis (ATN)?",
        "options": [
            "Muddy brown casts",
            "Red blood cell casts",
            "White blood cell casts",
            "Hyaline casts",
            "Waxy casts"
        ],
        "correct_answer": "Muddy brown casts",
        "explanation": "Muddy brown granular casts in the urine sediment are pathognomonic for Acute Tubular Necrosis (ATN), often caused by ischaemia or nephrotoxins."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 25-year-old man presents with macroscopic haematuria and hypertension 2 weeks after a severe sore throat. Urine microscopy reveals distorted erythrocytes and cylindrical structures. What type of casts are pathognomonic for a nephritic syndrome (glomerulonephritis)?",
        "options": [
            "Red blood cell casts",
            "White blood cell casts",
            "Muddy brown casts",
            "Fatty casts",
            "Hyaline casts"
        ],
        "correct_answer": "Red blood cell casts",
        "explanation": "Red blood cell casts indicate bleeding from the glomerulus and are pathognomonic for glomerulonephritis (nephritic syndrome), such as post-streptococcal glomerulonephritis."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 45-year-old woman with nephrotic syndrome undergoes a renal biopsy. Silver staining and electron microscopy show thickening of the glomerular basement membrane with subepithelial immune complex deposits, forming a characteristic 'spike and dome' appearance. What is the diagnosis?",
        "options": [
            "Membranous nephropathy",
            "Minimal change disease",
            "Membranoproliferative glomerulonephritis",
            "Focal segmental glomerulosclerosis",
            "IgA nephropathy"
        ],
        "correct_answer": "Membranous nephropathy",
        "explanation": "A 'spike and dome' appearance on electron microscopy is pathognomonic for Membranous nephropathy, a common cause of nephrotic syndrome in adults."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 30-year-old man with Hepatitis C presents with mixed nephritic/nephrotic syndrome. A renal biopsy shows mesangial interposition into the capillary wall, causing a 'tram-track' or double-contour appearance of the glomerular basement membrane on light microscopy. What is the diagnosis?",
        "options": [
            "Membranoproliferative glomerulonephritis (MPGN)",
            "Membranous nephropathy",
            "Diabetic nephropathy",
            "Lupus nephritis",
            "Minimal change disease"
        ],
        "correct_answer": "Membranoproliferative glomerulonephritis (MPGN)",
        "explanation": "A 'tram-track' appearance (splitting of the GBM) is pathognomonic for Membranoproliferative glomerulonephritis (MPGN)."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 65-year-old man with a 25-year history of poorly controlled type 2 diabetes presents with proteinuria. A renal biopsy reveals nodular glomerulosclerosis with eosinophilic nodules at the periphery of the glomerulus. What are these classic nodules called?",
        "options": [
            "Kimmelstiel-Wilson nodules",
            "Aschoff bodies",
            "Ghon complexes",
            "Schiller-Duval bodies",
            "Lisch nodules"
        ],
        "correct_answer": "Kimmelstiel-Wilson nodules",
        "explanation": "Kimmelstiel-Wilson nodules (nodular glomerulosclerosis) are pathognomonic histological lesions seen in advanced Diabetic Nephropathy."
    },

    # =========================================================================
    # 11. REPRODUCTIVE / O&G
    # =========================================================================
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 28-year-old pregnant woman presents at 10 weeks gestation with severe hyperemesis, a uterus large for dates, and vaginal bleeding. Transvaginal ultrasound demonstrates a heterogeneous mass with multiple cystic spaces, and an absence of fetal parts. What is the classic term for this ultrasound appearance?",
        "options": [
            "Snowstorm appearance",
            "String of pearls appearance",
            "Lemon sign",
            "Banana sign",
            "Target sign"
        ],
        "correct_answer": "Snowstorm appearance",
        "explanation": "A 'snowstorm' or 'bunch of grapes' appearance on ultrasound is pathognomonic for a complete hydatidiform mole (molar pregnancy)."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 32-year-old woman presents with severe secondary dysmenorrhoea and deep dyspareunia. A laparoscopy is performed, revealing an ovarian cyst filled with thick, dark, old blood. What is the common name for this pathognomonic finding of endometriosis?",
        "options": [
            "Chocolate cyst",
            "Dermoid cyst",
            "Corpus luteum cyst",
            "Follicular cyst",
            "Theca lutein cyst"
        ],
        "correct_answer": "Chocolate cyst",
        "explanation": "An endometrioma containing old, dark brown blood is classically called a 'chocolate cyst'. It is highly indicative of endometriosis involving the ovaries."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 24-year-old woman presents with an offensive, thin, grey-white vaginal discharge. The pH is >4.5 and a 'whiff test' with potassium hydroxide produces a fishy odour. Microscopy of the discharge reveals vaginal squamous epithelial cells covered in bacteria, obscuring their borders. What are these cells called?",
        "options": [
            "Clue cells",
            "Koilocytes",
            "Tzanck cells",
            "Navicular cells",
            "Decidual cells"
        ],
        "correct_answer": "Clue cells",
        "explanation": "Clue cells (epithelial cells stippled with bacteria, obscuring the margins) are a pathognomonic finding on wet mount microscopy for Bacterial Vaginosis."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 27-year-old woman presents with a frothy, yellow-green vaginal discharge and vulval itch. On speculum examination, the cervix has multiple punctate haemorrhages. What is this classic clinical sign called?",
        "options": [
            "Strawberry cervix",
            "Cervical ectropion",
            "Nabothian cyst",
            "Cervical polyp",
            "Blue cervix (Chadwick's sign)"
        ],
        "correct_answer": "Strawberry cervix",
        "explanation": "A 'strawberry cervix' (colpitis macularis)—punctate haemorrhages on the cervix—is a classic sign of Trichomonas vaginalis infection."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 29-year-old woman presents with oligomenorrhoea, hirsutism, and infertility. A pelvic ultrasound shows enlarged ovaries with multiple small peripherally arranged follicles (typically 12 or more per ovary). What is the classic term for this ultrasound appearance?",
        "options": [
            "String of pearls sign",
            "Snowstorm sign",
            "Whirlpool sign",
            "Ground glass appearance",
            "Double decidual sign"
        ],
        "correct_answer": "String of pearls sign",
        "explanation": "The 'string of pearls' appearance on ultrasound describes the peripheral arrangement of multiple small follicles, characteristic of Polycystic Ovary Syndrome (PCOS)."
    },

    # =========================================================================
    # 12. RESPIRATORY
    # =========================================================================
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 60-year-old woman with chronic cough and copious purulent sputum production undergoes a high-resolution CT of the chest. It demonstrates dilated, thick-walled bronchi that are larger than their accompanying pulmonary artery. What is the classic term for this CT finding?",
        "options": [
            "Signet ring sign",
            "Honeycomb lung",
            "Ground glass opacification",
            "Tree-in-bud pattern",
            "Water lily sign"
        ],
        "correct_answer": "Signet ring sign",
        "explanation": "The 'signet ring' sign on HRCT (a dilated airway adjacent to a smaller accompanying pulmonary artery) and 'tram lines' (thickened parallel bronchial walls) are pathognomonic for Bronchiectasis."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 70-year-old man presents with progressive exertional dyspnoea and a dry cough. Auscultation reveals fine, end-inspiratory 'Velcro-like' crackles at the lung bases. HRCT demonstrates subpleural, basal predominant reticular opacities with clustered cystic air spaces. What is the term for this advanced cystic change?",
        "options": [
            "Honeycomb lung",
            "Signet ring sign",
            "Consolidation",
            "Air bronchogram",
            "Crazy paving pattern"
        ],
        "correct_answer": "Honeycomb lung",
        "explanation": "Honeycombing (clustered cystic air spaces with thick walls, predominantly subpleural and basal) is the classic pathognomonic HRCT feature of usual interstitial pneumonia (UIP) / Idiopathic Pulmonary Fibrosis (IPF)."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 35-year-old woman of Afro-Caribbean descent presents with erythema nodosum, uveitis, and a dry cough. A chest X-ray shows bilateral hilar lymphadenopathy. A transbronchial biopsy is performed. What pathognomonic histological feature confirms the diagnosis?",
        "options": [
            "Non-caseating granulomas",
            "Caseating granulomas",
            "Charcot-Leyden crystals",
            "Curschmann spirals",
            "Asbestos bodies"
        ],
        "correct_answer": "Non-caseating granulomas",
        "explanation": "Non-caseating (non-necrotising) epithelioid granulomas are the hallmark histological finding in Sarcoidosis."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 12-year-old boy with a known history of severe asthma provides a sputum sample during an exacerbation. Microscopy reveals spiral-shaped mucus plugs and hexagonal, double-pointed crystals derived from eosinophil breakdown. What are these crystals called?",
        "options": [
            "Charcot-Leyden crystals",
            "Cholesterol crystals",
            "Urate crystals",
            "Birefringent crystals",
            "Struvite crystals"
        ],
        "correct_answer": "Charcot-Leyden crystals",
        "explanation": "Charcot-Leyden crystals (formed from the breakdown of eosinophils) and Curschmann spirals (mucus plugs) are classic pathognomonic sputum findings in bronchial Asthma."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 45-year-old woman presents with sudden onset pleuritic chest pain, haemoptysis, and shortness of breath following a long-haul flight. A chest X-ray shows a wedge-shaped opacity in the right lower lobe with its base against the pleura. What is this sign known as?",
        "options": [
            "Hampton's hump",
            "Westermark sign",
            "Fleischner sign",
            "Golden S sign",
            "Silhouette sign"
        ],
        "correct_answer": "Hampton's hump",
        "explanation": "Hampton's hump is a wedge-shaped pleural-based opacity on a chest X-ray indicative of pulmonary infarction, a classic but rare pathognomonic sign of a Pulmonary Embolism."
    }
]
