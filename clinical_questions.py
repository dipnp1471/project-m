# -*- coding: utf-8 -*-
"""
High-Yield Clinical Problem Solving Questions
60 challenging clinical questions focusing on classic diagnostic signs, core pathophysiology, and high-yield findings.
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
        "explanation": "A 'boot-shaped' cardiac silhouette (coeur en sabot) on chest radiography is a hallmark radiological feature of Tetralogy of Fallot (TOF). The characteristic contour is produced by right ventricular hypertrophy elevating the cardiac apex alongside hypoplasia of the pulmonary artery trunk. The presentation of cyanosis exacerbated by crying or feeding represents hypercyanotic 'tet spells', which occur due to acute infundibular spasm worsening the right-to-left shunt."
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
        "explanation": "This patient presents with acute cardiac tamponade, evidenced by Beck's triad (hypotension, elevated jugular venous pressure, and muffled heart sounds) alongside electrical alternans on ECG (beat-to-beat variation in QRS amplitude caused by the heart swinging within a fluid-filled pericardial sac). Urgent pericardiocentesis under echocardiographic guidance is the definitive life-saving intervention to relieve intrapericardial pressure."
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
        "explanation": "Radio-femoral delay, blood pressure discrepancy between the upper and lower extremities, and inferior rib notching on chest radiography strongly point to coarctation of the aorta. Rib notching results from pressure erosion by dilated, tortuous intercostal collateral arteries bypassing the aortic narrowing (typically involving ribs 3 to 8). It is commonly associated with a bicuspid aortic valve and Turner syndrome."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 60-year-old man presents with sharp pleuritic chest pain. He had a myocardial infarction 4 weeks ago. An echocardiogram shows a large accumulation of fluid in the pericardial sac. A chest X-ray demonstrates an enlarged globular cardiac silhouette, often described as a 'water bottle' heart. What is the underlying immunological process?",
        "options": [
            "Dressler's syndrome",
            "Acute viral pericarditis",
            "Ventricular pseudoaneurysm",
            "Left ventricular rupture",
            "Uraemic pericarditis"
        ],
        "correct_answer": "Dressler's syndrome",
        "explanation": "Dressler's syndrome (post-myocardial infarction pericarditis) is an immune-mediated pericarditis that characteristically develops 2 to 10 weeks after a myocardial infarction, triggered by autoimmune response against damaged myocardial antigens. The globular 'water bottle' cardiac contour on chest radiography reflects a substantial pericardial effusion. Management typically involves high-dose NSAIDs or colchicine; corticosteroids are reserved for refractory cases."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 35-year-old woman from South America presents with progressive dysphagia and constipation. She recently developed right bundle branch block on ECG and signs of dilated cardiomyopathy. She reports being bitten by a 'kissing bug' in childhood. What is the most likely causative organism?",
        "options": [
            "Trypanosoma cruzi",
            "Trypanosoma brucei",
            "Leishmania donovani",
            "Toxoplasma gondii",
            "Schistosoma mansoni"
        ],
        "correct_answer": "Trypanosoma cruzi",
        "explanation": "Chagas disease is caused by the protozoan parasite Trypanosoma cruzi, transmitted by the triatomine ('kissing') bug in endemic regions of Central and South America. Chronic infection manifests decades later with destructive parasympathetic denervation, leading to dilated cardiomyopathy (frequently featuring right bundle branch block or left ventricular apical aneurysms), megaoesophagus (achalasia-like dysphagia), and megacolon (severe chronic constipation)."
    },

    # =========================================================================
    # 2. DERMATOLOGY / OPHTHALMOLOGY / ENT
    # =========================================================================
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 25-year-old man presents with a mild pruritic rash. It began 10 days ago as a single 3 cm oval, salmon-coloured scaly patch on his chest. Yesterday, a widespread eruption of smaller scaly macules appeared on his trunk along the lines of cleavage, giving a 'Christmas tree' distribution. What is the most likely diagnosis?",
        "options": [
            "Pityriasis rosea",
            "Psoriasis vulgaris",
            "Tinea versicolor",
            "Secondary syphilis",
            "Guttate psoriasis"
        ],
        "correct_answer": "Pityriasis rosea",
        "explanation": "The appearance of an initial solitary, salmon-pink 'herald patch' followed days later by a generalised eruption of smaller oval plaques orientated along Langer's cleavage lines (the classic 'Christmas tree' distribution) is characteristic of pityriasis rosea. Likely associated with reactivation of HHV-6 or HHV-7, the condition is benign and self-limiting, typically resolving spontaneously over 6 to 12 weeks without requiring treatment beyond topical emollients or mild antipruritics."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 70-year-old man presents with sudden, painless, profound loss of vision in his right eye. Examination of the fundus reveals a pale, opaque retina with a distinct 'cherry-red spot' at the macula. What is the most likely diagnosis?",
        "options": [
            "Central retinal artery occlusion",
            "Central retinal vein occlusion",
            "Rhegmatogenous retinal detachment",
            "Acute angle-closure glaucoma",
            "Wet age-related macular degeneration"
        ],
        "correct_answer": "Central retinal artery occlusion",
        "explanation": "Sudden, profound, painless monocular visual loss accompanied by diffuse retinal pallor and a prominent macular 'cherry-red spot' is the hallmark clinical presentation of central retinal artery occlusion (CRAO). The cherry-red appearance occurs because the thin fovea allows visualization of the underlying, well-vascularised choroid, while the surrounding oedematous, ischaemic retina appears pale. It represents an ophthalmic emergency analogous to an acute stroke and requires urgent specialist intervention to attempt preservation of vision."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 4-year-old unimmunised boy is brought to the GP with a 3-day history of high fever, coryza, cough, and conjunctivitis. On examination of the oral mucosa, tiny white spots resembling grains of salt on a red background are seen on the buccal mucosa opposite the molars. What are these spots called?",
        "options": [
            "Koplik spots",
            "Fordyce spots",
            "Aphthous ulcers",
            "Leukoplakia",
            "Brushfield spots"
        ],
        "correct_answer": "Koplik spots",
        "explanation": "Koplik spots are tiny, bluish-white granular papules situated on an erythematous base upon the buccal mucosa (characteristically opposite the second molars). They are highly distinctive of the prodromal stage of measles (rubeola), emerging 1 to 2 days prior to the characteristic cephalocaudal maculopapular exanthem and typically fading within 48 hours. The clinical triad of the 'three Cs'—cough, coryza, and conjunctivitis—further confirms measles."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 65-year-old man with long-standing poorly controlled hypertension attends for a routine eye check. Fundoscopy shows thickening of the retinal arterioles causing compression of the venules where they cross. What is this specific finding known as?",
        "options": [
            "AV nipping (nipping/nicking)",
            "Cotton wool spots",
            "Flame haemorrhages",
            "Roth spots",
            "Drusen"
        ],
        "correct_answer": "AV nipping (nipping/nicking)",
        "explanation": "Arteriovenous (AV) nipping, or nicking, is a recognized feature of moderate (Grade II) hypertensive retinopathy. It develops because chronic arterial wall thickening and sclerosis compress and taper the underlying, thinner-walled venule where they share a common adventitial sheath at vascular crossings. Left unchecked, this can predispose to branch retinal vein occlusion (BRVO)."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 55-year-old farmer presents with a slowly growing nodule on his upper lip. On examination, it is a 1 cm nodule with a 'pearly, rolled edge' and visible fine telangiectasia across its surface. The centre is slightly ulcerated. What is the most likely diagnosis?",
        "options": [
            "Basal cell carcinoma",
            "Squamous cell carcinoma",
            "Malignant melanoma",
            "Actinic keratosis",
            "Keratoacanthoma"
        ],
        "correct_answer": "Basal cell carcinoma",
        "explanation": "A pearly translucent nodule with rolled borders, arborising telangiectasias, and central ulceration (a 'rodent ulcer') is the signature clinical presentation of nodular basal cell carcinoma (BCC). BCC is the most common non-melanoma cutaneous malignancy, primarily driven by cumulative ultraviolet radiation exposure. While locally invasive and destructive if neglected, distant metastases are exceptionally rare, and surgical excision with margins is typically curative."
    },

    # =========================================================================
    # 3. ENDOCRINOLOGY / METABOLIC
    # =========================================================================
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 42-year-old woman is found to have an incidental thyroid nodule. Fine needle aspiration (FNA) is inconclusive, but histological analysis following hemithyroidectomy demonstrates cells with ground-glass nuclei, nuclear grooving, and psammoma bodies. What is the diagnosis?",
        "options": [
            "Papillary thyroid carcinoma",
            "Follicular thyroid carcinoma",
            "Medullary thyroid carcinoma",
            "Anaplastic thyroid carcinoma",
            "Hashimoto thyroiditis"
        ],
        "correct_answer": "Papillary thyroid carcinoma",
        "explanation": "Ground-glass, optically clear nuclei with prominent grooves (classically described as 'Orphan Annie eyes') and concentric, laminated calcospherites known as psammoma bodies are definitive histological hallmarks of papillary thyroid carcinoma. It accounts for over 70–80% of all thyroid cancers, generally carries an excellent overall prognosis, and primarily metastasises via lymphatic drainage to regional cervical nodes."
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
            "Stasis dermatitis"
        ],
        "correct_answer": "Pretibial myxoedema",
        "explanation": "Pretibial myxoedema (thyroid dermopathy) is a localized, mucinous non-pitting cutaneous infiltration virtually unique to Graves' disease. It arises from thyroid-stimulating hormone (TSH) receptor antibody activation of dermal fibroblasts, leading to marked glycosaminoglycan accumulation. It almost invariably develops in patients with preexisting Graves' ophthalmopathy and indicates high circulating autoantibody titres."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 55-year-old man presents with fatigue, joint pains, and erectile dysfunction. On examination, he has a slate-grey hyperpigmentation of his skin. Blood tests show significantly elevated ferritin and fasting blood glucose is 14 mmol/L. This presentation is classically referred to as 'bronze diabetes'. What is the underlying condition?",
        "options": [
            "Haemochromatosis",
            "Wilson's disease",
            "Addison's disease",
            "Cushing's disease",
            "Porphyria cutanea tarda"
        ],
        "correct_answer": "Haemochromatosis",
        "explanation": "The combination of slate-grey skin hyperpigmentation, newly diagnosed diabetes mellitus, and signs of chronic organ damage (such as chondrocalcinosis, hypogonadotropic hypogonadism, or hepatomegaly) represents the historical triad of 'bronze diabetes' in hereditary haemochromatosis. Caused by an autosomal recessive mutation in the HFE gene (most commonly C282Y homozygous), uncontrolled intestinal iron absorption causes parenchymal iron overload. Regular venesection is the cornerstone of therapy to prevent progression to cirrhosis and hepatocellular carcinoma."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 28-year-old woman undergoes a total thyroidectomy. On post-operative day 2, she complains of tingling around her mouth and in her fingers. When taking her blood pressure, inflation of the cuff above systolic pressure causes carpal spasm. What is this sign called?",
        "options": [
            "Trousseau's sign",
            "Chvostek's sign",
            "Kernig's sign",
            "Brudzinski's sign",
            "Homans' sign"
        ],
        "correct_answer": "Trousseau's sign",
        "explanation": "Trousseau's sign of latent tetany—carpopedal spasm elicited by inflating a sphygmomanometer cuff above systolic pressure for 3 minutes—is considerably more sensitive and specific for hypocalcaemia than Chvostek's sign. Post-thyroidectomy hypocalcaemia is caused by transient ischaemia or inadvertent devascularisation/resection of the parathyroid glands. Prompt intravenous or oral calcium replacement alongside active vitamin D (calcitriol/alfacalcidol) is indicated."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 60-year-old woman presents with bone pain, renal colic, and constipation. She reports feeling increasingly depressed and lethargic. Serum biochemistry shows hypercalcaemia. Her constellation of symptoms is historically described as 'moans, groans, stones, and bones'. What is the most likely diagnosis?",
        "options": [
            "Primary hyperparathyroidism",
            "Hypoparathyroidism",
            "Paget's disease of bone",
            "Osteomalacia",
            "Multiple myeloma"
        ],
        "correct_answer": "Primary hyperparathyroidism",
        "explanation": "The traditional mnemonic 'painful bones, renal stones, abdominal groans, and psychiatric moans' summarises the clinical sequelae of symptomatic hypercalcaemia. In ambulatory outpatients, primary hyperparathyroidism (usually secondary to a solitary benign parathyroid adenoma in ~85% of cases) is by far the leading cause, characterized by elevated serum calcium with inappropriately normal or raised PTH. In hospitalised inpatients, malignancy-related hypercalcaemia (PTHrP secretion or osteolytic metastases) predominates."
    },

    # =========================================================================
    # 4. GASTROENTEROLOGY / CLINICAL NUTRITION
    # =========================================================================
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 24-year-old man presents with chronic bloody diarrhoea. A barium enema reveals complete loss of haustral markings throughout the descending and sigmoid colon, giving it the appearance of a smooth, rigid tube. What is the classical name for this radiological finding?",
        "options": [
            "Lead pipe colon",
            "Apple core lesion",
            "String sign of Kantor",
            "Cobblestone appearance",
            "Thumbprinting"
        ],
        "correct_answer": "Lead pipe colon",
        "explanation": "A 'lead pipe' colon describes the radiological appearance of a featureless, foreshortened, and rigid colon lacking normal haustral mucosal folds on contrast imaging. It is a defining chronic feature of long-standing ulcerative colitis, caused by recurrent mucosal inflammation, mural hypertrophy, and submucosal fibrosis. Patients with extensive colitis exceeding 8–10 years duration require regular surveillance colonoscopy due to an elevated risk of colorectal dysplasia."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 28-year-old woman presents with abdominal pain and weight loss. Colonoscopy reveals transmural inflammation with deep fissuring ulcers interspersed with normal mucosa, giving a 'cobblestone' appearance. A barium follow-through shows severe stricturing of the terminal ileum. What is the stricture known as?",
        "options": [
            "String sign of Kantor",
            "Bird's beak sign",
            "Coffee bean sign",
            "Pauchet's sign",
            "Whirl sign"
        ],
        "correct_answer": "String sign of Kantor",
        "explanation": "The 'string sign of Kantor' is a radiological sign on small bowel follow-through where severe narrowing of the terminal ileum resembles a frayed piece of string. This luminal stenosis results from persistent transmural inflammation, muscular spasm, and fibrotic stricturing characteristic of Crohn's disease. The interspersed 'skip lesions' and deep mucosal fissures producing cobblestoning clearly differentiate Crohn's from ulcerative colitis."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 68-year-old man presents with iron deficiency anaemia and altered bowel habit. A barium enema demonstrates a short segment of severe, circumferential irregular narrowing in the descending colon with overhanging edges. What is the classic term for this appearance?",
        "options": [
            "Apple core lesion",
            "Lead pipe sign",
            "Thumbprinting",
            "Accordion sign",
            "Target sign"
        ],
        "correct_answer": "Apple core lesion",
        "explanation": "An 'apple core' (or napkin-ring) sign on fluoroscopic barium enema describes annular, circumferential constriction of the colonic lumen with abrupt shelf-like or overhanging margins. It strongly suggests an infiltrating colorectal adenocarcinoma until proven otherwise. In contemporary practice, suspected lesions are investigated directly with colonoscopy or CT colonography to allow tissue biopsy and formal staging."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 19-year-old man presents with tremors and signs of chronic liver disease. Slit-lamp examination of the eyes reveals golden-brown rings at the periphery of the cornea in Descemet's membrane. What are these rings called?",
        "options": [
            "Kayser-Fleischer rings",
            "Fleischer rings",
            "Corneal arcus",
            "Lisch nodules",
            "Kayser-Roth rings"
        ],
        "correct_answer": "Kayser-Fleischer rings",
        "explanation": "Kayser-Fleischer (KF) rings are greenish-brown or golden pigmented bands formed by abnormal copper deposition within Descemet's membrane of the peripheral corneal limbus. They are strongly indicative of Wilson's disease (hepatolenticular degeneration) and are present in nearly all patients presenting with neurological or psychiatric features. Wilson's disease results from mutations in the ATP7B gene, causing impaired biliary copper excretion; diagnostic findings include low serum caeruloplasmin and elevated 24-hour urinary copper."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 45-year-old woman presents with intermittent dysphagia for both solids and liquids, along with retrosternal chest pain. A barium swallow reveals multiple uncoordinated contractions, giving the oesophagus a 'corkscrew' or 'rosary bead' appearance. What is the diagnosis?",
        "options": [
            "Diffuse oesophageal spasm",
            "Achalasia",
            "Oesophageal adenocarcinoma",
            "Systemic sclerosis",
            "Schatzki ring"
        ],
        "correct_answer": "Diffuse oesophageal spasm",
        "explanation": "A 'corkscrew' or 'rosary bead' oesophagus on barium swallow is a distinctive finding of diffuse oesophageal spasm (distal oesophageal spasm). It is caused by uncoordinated, simultaneous non-peristaltic tertiary contractions in the smooth muscle portion of the oesophagus. High-resolution manometry is the gold standard diagnostic modality, revealing premature, repetitive contractions with normal lower oesophageal sphincter relaxation."
    },

    # =========================================================================
    # 5. INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 65-year-old man presents with fatigue and bleeding gums. A full blood count shows a low haemoglobin, thrombocytopenia, and leukocytosis. A blood film reveals large blast cells with prominent nucleoli and distinct, needle-like eosinophilic inclusions in the cytoplasm. What are these inclusions called?",
        "options": [
            "Auer rods",
            "Döhle bodies",
            "Howell-Jolly bodies",
            "Heinz bodies",
            "Pappenheimer bodies"
        ],
        "correct_answer": "Auer rods",
        "explanation": "Auer rods are linear, needle-like reddish-purple inclusions formed by coalesced azurophilic lysosomes and myeloperoxidase within the cytoplasm of blast cells. Their detection confirms myeloid lineage and is diagnostic of Acute Myeloid Leukaemia (AML) (or high-grade myelodysplastic syndrome with excess blasts), conclusively distinguishing AML from Acute Lymphoblastic Leukaemia (ALL). Multiple Auer rods stacked together ('faggot cells') are especially prominent in acute promyelocytic leukaemia (APML)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 25-year-old woman presents with a painless, enlarged cervical lymph node and night sweats. A lymph node biopsy demonstrates large, binucleate cells with prominent eosinophilic nucleoli giving an 'owl-eye' appearance. What is the specific name of these cells?",
        "options": [
            "Reed-Sternberg cells",
            "Gaucher cells",
            "Langhans giant cells",
            "Touton giant cells",
            "Mott cells"
        ],
        "correct_answer": "Reed-Sternberg cells",
        "explanation": "Reed-Sternberg cells are giant, morphologically distinctive binucleated or multinucleated B-cells featuring prominent eosinophilic nucleoli surrounded by a clear halo, creating an 'owl-eye' appearance. They are the defining neoplastic component of classic Hodgkin's lymphoma, characteristically staining positive for CD30 and CD15 on immunohistochemistry. Typically, they comprise only 1–2% of the tumour mass, embedded within a dense reactive inflammatory background of lymphocytes, eosinophils, and histiocytes."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "An asymptomatic 70-year-old man is found to have a significantly elevated lymphocyte count on a routine blood test. A peripheral blood smear shows many mature-appearing small lymphocytes alongside fragile, disrupted lymphocytes. What is the term for these disrupted cells?",
        "options": [
            "Smudge cells",
            "Schistocytes",
            "Target cells",
            "Tear drop cells",
            "Acanthocytes"
        ],
        "correct_answer": "Smudge cells",
        "explanation": "Smudge cells (or Gumprecht shadow cells) are fragile, mechanically disrupted leucocytes that disintegrate during the preparation of a peripheral blood smear due to cytoskeletal defects (specifically vimentin deficiency). While non-specific in isolation, their presence in large numbers alongside an isolated, persistent mature lymphocytosis (>5 x 10^9/L) is strongly characteristic of Chronic Lymphocytic Leukaemia (CLL). Diagnosis is confirmed with flow cytometry demonstrating a clonal B-cell population expressing CD5, CD19, and CD23."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 68-year-old man presents with severe back pain and lethargy. Investigations reveal hypercalcaemia and impaired renal function. Urine electrophoresis identifies monoclonal free light chains. What is the eponymous name for these light chains?",
        "options": [
            "Bence Jones proteins",
            "Russell bodies",
            "Cryoglobulins",
            "Waldenström macroglobulins",
            "Amyloid light chains"
        ],
        "correct_answer": "Bence Jones proteins",
        "explanation": "Bence Jones proteins are monoclonal free immunoglobulin light chains (either kappa or lambda) filtered by the glomeruli and detected in the urine via protein electrophoresis or immunofixation. They are strongly associated with multiple myeloma and light chain amyloidosis, where excessive light chain production overwhelms proximal tubular reabsorption and causes cast nephropathy (myeloma kidney). The classic 'CRAB' features—HyperCalcaemia, Renal impairment, Anaemia, and Bone lesions—further support the diagnosis."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 22-year-old man of Mediterranean descent develops jaundice and dark urine after starting nitrofurantoin for a UTI. A peripheral blood smear shows 'bite cells' and special staining reveals denatured haemoglobin aggregates within red blood cells. What are these aggregates called?",
        "options": [
            "Heinz bodies",
            "Howell-Jolly bodies",
            "Basophilic stippling",
            "Pappenheimer bodies",
            "Cabot rings"
        ],
        "correct_answer": "Heinz bodies",
        "explanation": "Heinz bodies are insoluble clumps of oxidised, denatured haemoglobin that precipitate onto red cell membranes following oxidative insults (such as nitrofurantoin, primaquine, fava beans, or acute infection) in Glucose-6-Phosphate Dehydrogenase (G6PD) deficiency. As these damaged erythrocytes transit through the splenic cords, macrophages pluck out the Heinz bodies, leaving behind characteristic 'bite cells' (degmacytes) and blister cells on the peripheral blood film. G6PD enzyme assays should only be measured once the acute haemolytic crisis has resolved, as surviving younger reticulocytes can yield false-normal levels."
    },

    # =========================================================================
    # 6. MUSCULOSKELETAL
    # =========================================================================
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 28-year-old man presents with chronic lower back pain and morning stiffness lasting over an hour that improves with exercise. A plain pelvic radiograph shows complete fusion of the sacroiliac joints, and spinal X-rays reveal extensive syndesmophyte formation and calcification of the spinal ligaments. What is the classic term for this spinal appearance?",
        "options": [
            "Bamboo spine",
            "Rugger-jersey spine",
            "Picture frame spine",
            "Scaffold spine",
            "Codfish vertebrae"
        ],
        "correct_answer": "Bamboo spine",
        "explanation": "'Bamboo spine' is the definitive radiographic appearance of end-stage ankylosing spondylitis (axial spondyloarthritis). It results from progressive ossification of the annulus fibrosus, syndesmophyte bridging between adjacent vertebral bodies, and calcification of the anterior longitudinal ligament and interspinous ligaments, creating a continuous, rigid column. Patients are usually HLA-B27 positive and have a heightened risk of spinal fractures following even minor trauma."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 50-year-old woman with a 15-year history of rheumatoid arthritis presents with hand deformities. On examination, the PIP joint of her middle finger is permanently flexed, and the DIP joint is hyperextended. What is the name of this deformity?",
        "options": [
            "Boutonniere deformity",
            "Swan neck deformity",
            "Mallet finger",
            "Z-deformity of the thumb",
            "Dupuytren contracture"
        ],
        "correct_answer": "Boutonniere deformity",
        "explanation": "A Boutonnière (buttonhole) deformity consists of persistent flexion of the proximal interphalangeal (PIP) joint combined with hyperextension of the distal interphalangeal (DIP) joint. It develops in rheumatoid arthritis when chronic synovitis ruptures or attenuates the central slip of the extensor digitorum tendon, causing the lateral bands to slip volarward and act as PIP flexors. In contrast, a swan-neck deformity represents the exact opposite configuration: PIP hyperextension with DIP flexion."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 62-year-old woman presents with persistent, aching pain and morning stiffness lasting 15 minutes in her hands, worsened by knitting. Examination shows prominent, hard, non-tender bony enlargements over the distal interphalangeal (DIP) joints of both hands. What are these bony enlargements called?",
        "options": [
            "Heberden's nodes",
            "Bouchard's nodes",
            "Rheumatoid nodules",
            "Tophi",
            "Osler's nodes"
        ],
        "correct_answer": "Heberden's nodes",
        "explanation": "Heberden's nodes are hard, palpable bony outgrowths (osteophytes) located at the distal interphalangeal (DIP) joints of the hands, characteristic of primary nodal osteoarthritis. Bouchard's nodes similarly represent osteophytic hypertrophy but affect the proximal interphalangeal (PIP) joints. The brief duration of morning stiffness (<30 minutes), absence of systemic symptoms, and specific involvement of the DIPs help differentiate nodal osteoarthritis from inflammatory arthritides like rheumatoid arthritis, which typically spares the DIP joints."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 52-year-old man presents with acute, excruciating pain, swelling, and redness in his first metatarsophalangeal (MTP) joint that started overnight. Arthrocentesis is performed. Polarised light microscopy demonstrates needle-shaped crystals with strong negative birefringence. What is the diagnosis?",
        "options": [
            "Gout",
            "Pseudogout",
            "Septic arthritis",
            "Reactive arthritis",
            "Hydroxyapatite arthropathy"
        ],
        "correct_answer": "Gout",
        "explanation": "Synovial fluid analysis showing needle-shaped monosodium urate crystals displaying strong negative birefringence under polarized light microscopy confirms acute gout (podagra). 'Negative birefringence' means the crystals appear yellow when aligned parallel to the polarizing axis and blue when perpendicular. In contrast, pseudogout features calcium pyrophosphate dihydrate (CPPD) crystals, which are rhomboid-shaped and demonstrate weak positive birefringence."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 75-year-old woman presents with an acutely swollen and painful right knee. A radiograph shows a thin layer of calcification within the articular cartilage. Joint aspiration reveals weakly positive birefringent, rhomboid-shaped crystals. What is the diagnosis?",
        "options": [
            "Pseudogout",
            "Gout",
            "Basic calcium phosphate crystal disease",
            "Osteoarthritis flare",
            "Avascular necrosis"
        ],
        "correct_answer": "Pseudogout",
        "explanation": "The presence of rhomboid-shaped calcium pyrophosphate dihydrate (CPPD) crystals with weak positive birefringence on polarized microscopy establishes the diagnosis of pseudogout (acute CPPD crystal arthritis). Under compensated polarized light, these crystals turn blue when parallel to the slow axis of the compensator. Plain radiographs commonly demonstrate chondrocalcinosis (linear calcification within hyaline or fibrocartilage, frequently in the menisci or triangular fibrocartilage of the wrist)."
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
            "Bird's beak sign"
        ],
        "correct_answer": "Double bubble sign",
        "explanation": "The 'double bubble' sign on an erect abdominal radiograph indicates duodenal atresia. The two prominent gas fluid levels represent air distending the stomach and the blind-ending dilated first part of the duodenum, with a complete absence of distal bowel gas. Duodenal atresia results from failure of recanalisation of the embryonic duodenum at weeks 8–10 of gestation and is strongly associated with Trisomy 21 (Down's syndrome), occurring in approximately one-third of affected infants."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 2-year-old boy presents with a barking cough and stridor. An AP neck radiograph is performed to rule out other conditions, and it shows subglottic narrowing. What is the name of this radiological sign?",
        "options": [
            "Steeple sign",
            "Thumbprint sign",
            "Omega sign",
            "Spinnaker sail sign",
            "Deep sulcus sign"
        ],
        "correct_answer": "Steeple sign",
        "explanation": "The 'steeple sign' (or wine-bottle sign) describes symmetrical subglottic tracheal narrowing on an anteroposterior (AP) soft-tissue neck radiograph, resembling a church steeple. It is a recognized radiological feature of acute laryngotracheobronchitis (croup), typically caused by parainfluenza virus. While croup is primarily a clinical diagnosis diagnosed by a barking cough, hoarseness, and inspiratory stridor, imaging is occasionally obtained to exclude foreign body inhalation or acute epiglottitis. First-line medical therapy is oral dexamethasone."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 4-year-old unimmunised girl presents with a high fever, drooling, and leaning forward in a 'tripod' position. She looks toxic. A lateral neck radiograph is taken cautiously and shows an enlarged epiglottis. What is the name of this sign?",
        "options": [
            "Thumbprint sign",
            "Steeple sign",
            "Silhouette sign",
            "Sail sign",
            "Pencil tip sign"
        ],
        "correct_answer": "Thumbprint sign",
        "explanation": "The 'thumbprint sign' on a lateral cervical soft-tissue radiograph represents a thickened, rounded, edematous epiglottis projecting into the hypopharynx, resembling an adult thumb. It indicates acute epiglottitis, historically caused by Haemophilus influenzae type b (Hib) and now occasionally caused by Streptococcus pyogenes or Staphylococcus aureus in unimmunised children. This is a critical airway emergency: direct inspection of the pharynx must be avoided until an experienced anaesthetist or ENT surgeon is present in theatre with emergency airway equipment ready."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 7-month-old infant presents with episodic inconsolable crying, drawing his legs up to his chest, followed by lethargy. He has passed stool that looks like 'red currant jelly'. An abdominal ultrasound shows a 'target' or 'doughnut' sign. What is the diagnosis?",
        "options": [
            "Intussusception",
            "Pyloric stenosis",
            "Meckel's diverticulitis",
            "Hirschsprung disease",
            "Midgut volvulus"
        ],
        "correct_answer": "Intussusception",
        "explanation": "The 'target' (or 'doughnut') sign on ultrasound—demonstrating concentric alternating rings of hypoechoic and hyperechoic bowel wall—confirms ileocolic intussusception, where a proximal segment of bowel telescopes into a distal segment. Passage of 'red currant jelly' stools (a mixture of shed mucosa, sloughed bowel, and blood) is a late clinical finding denoting intestinal ischaemia. Ultrasound has >95% sensitivity and specificity; first-line definitive management in hemodynamically stable children without peritonitis or perforation is radiological pneumatic (air) reduction."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old girl is brought in with mild fever and a bright red macular rash on both cheeks. Two days later, a lacy, reticular rash appears on her arms and trunk. What is the name of the appearance on her face?",
        "options": [
            "Slapped cheek appearance",
            "Butterfly rash",
            "Strawberry mark",
            "Port-wine stain",
            "Erythema marginatum"
        ],
        "correct_answer": "Slapped cheek appearance",
        "explanation": "The confluent, intense erythema over both cheeks giving a 'slapped cheek' appearance followed several days later by a reticular, lace-like erythematous rash on the trunk and limbs is distinctive of erythema infectiosum (fifth disease). It is caused by Parvovirus B19 infection. By the time the facial rash erupts, the child is no longer infectious. Crucially, Parvovirus B19 can precipitate aplastic crises in individuals with underlying haemoglobinopathies (e.g. sickle cell disease) and hydrops fetalis in pregnant women."
    },

    # =========================================================================
    # 8. PHARMACOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 78-year-old woman with atrial fibrillation is admitted with nausea, vomiting, and visual disturbances, specifically yellow-green halos around objects. Her ECG shows scooped, 'reverse tick' ST-segment depression. What drug toxicity is most likely?",
        "options": [
            "Digoxin",
            "Amiodarone",
            "Flecainide",
            "Verapamil",
            "Bisoprolol"
        ],
        "correct_answer": "Digoxin",
        "explanation": "Xanthopsia (yellow-green vision or halos), gastrointestinal upset, and scooped, down-sloping 'reverse tick' (Salvador Dalí's moustache) ST depressions are characteristic features of digoxin toxicity. The therapeutic window for digoxin is narrow, and toxicity is frequently triggered by hypokalaemia, hypomagnesaemia, or renal dysfunction, as hypokalaemia increases myocardial sensitivity to digoxin. Life-threatening arrhythmias or severe hyperkalaemia are treated with digoxin-specific antibody fragments (DigiFab)."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 40-year-old man with bipolar disorder is admitted with confusion, ataxia, and a severe coarse tremor. He recently developed a diarrhoeal illness and became dehydrated. Which medication is most likely responsible for his symptoms?",
        "options": [
            "Lithium",
            "Sodium valproate",
            "Lamotrigine",
            "Quetiapine",
            "Olanzapine"
        ],
        "correct_answer": "Lithium",
        "explanation": "A coarse tremor, ataxia, hyperreflexia, and altered mental status are hallmark signs of lithium toxicity. While a fine postural tremor is a common benign therapeutic side effect, the emergence of a coarse tremor alongside cerebellar or neurological signs signals dangerously elevated serum lithium levels (>1.5–2.0 mmol/L). Volume depletion (from gastroenteritis, ACE inhibitors, NSAIDs, or thiazide diuretics) reduces renal lithium clearance, triggering toxicity. Management includes aggressive IV 0.9% saline rehydration, with hemodialysis indicated for severe toxicity."
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
        "explanation": "Gingival hypertrophy (overgrowth of the gums), coarsening of facial features, acne, and hirsutism are well-documented long-term adverse effects of chronic phenytoin therapy. Gingival hyperplasia occurs in up to 50% of patients due to drug-induced alteration of collagen catabolism by gingival fibroblasts; strict oral hygiene and chlorhexidine rinses can limit severity. In acute toxicity, nystagmus, ataxia, and dysarthria predominate."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 65-year-old man presents with worsening breathlessness. He has a history of ventricular arrhythmias. Examination reveals a slate-grey discoloration of his skin in sun-exposed areas. A slit-lamp eye examination shows corneal microdeposits. Which medication is he taking?",
        "options": [
            "Amiodarone",
            "Sotalol",
            "Diltiazem",
            "Mexiletine",
            "Propafenone"
        ],
        "correct_answer": "Amiodarone",
        "explanation": "Slate-grey or blue-grey skin pigmentation (ceruloderma) on sun-exposed surfaces, asymptomatic corneal microdeposits (cornea verticillata), and pulmonary toxicity (pulmonary fibrosis/organising pneumonia) are distinctive adverse effects of long-term amiodarone therapy. Because of its high iodine content and extensive tissue accumulation, baseline and regular monitoring of pulmonary function, thyroid status (hypo- or hyperthyroidism), and liver enzymes is mandatory."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 55-year-old diabetic man is started on a new antihypertensive medication. Two weeks later, he develops a persistent, dry, tickly cough that is worse at night. What is the mechanism behind this side effect?",
        "options": [
            "Accumulation of bradykinin",
            "Inhibition of angiotensin II type 1 receptors",
            "Direct histamine release",
            "Excessive aldosterone degradation",
            "Bronchoconstriction via beta-2 antagonism"
        ],
        "correct_answer": "Accumulation of bradykinin",
        "explanation": "A persistent, non-productive nocturnal cough is a well-recognised class effect of Angiotensin-Converting Enzyme (ACE) inhibitors, affecting roughly 10–15% of patients. ACE (kininase II) is responsible for hydrolysing bradykinin and substance P in the respiratory tract. When ACE is inhibited, circulating and tissue levels of bradykinin accumulate, irritating pulmonary C-fibres and provoking cough. The cough typically resolves within 1 to 4 weeks of switching the patient to an Angiotensin Receptor Blocker (ARB), which does not affect bradykinin metabolism."
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
            "Marked lymphocytic pleocytosis",
            "Significantly decreased glucose with high neutrophils",
            "Normal protein and elevated red blood cells",
            "Oligoclonal bands with low protein"
        ],
        "correct_answer": "Albuminocytologic dissociation",
        "explanation": "Albuminocytological dissociation—characterized by a markedly elevated CSF protein concentration (>0.55 g/L) in the presence of a normal cerebrospinal fluid white cell count (<10 cells/uL)—is a defining diagnostic hallmark of Guillain-Barré syndrome (GBS). This dissociation reflects severe immune-mediated inflammation and demyelination of the spinal nerve roots without intrathecal cellular infiltration. Treatment involves intravenous immunoglobulin (IVIG) or plasma exchange, alongside close spirometric monitoring of forced vital capacity (FVC)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 28-year-old woman presents with sudden unilateral visual loss and pain on eye movement. She had a similar episode of right leg weakness 2 years ago that resolved. A lumbar puncture and serum protein electrophoresis are performed. Which finding on cerebrospinal fluid (CSF) analysis supports this diagnosis?",
        "options": [
            "Oligoclonal bands in CSF but not in serum",
            "Elevated opening pressure only",
            "Marked neutrophilic pleocytosis",
            "Markedly low CSF glucose",
            "Normal protein and normal white cell count"
        ],
        "correct_answer": "Oligoclonal bands in CSF but not in serum",
        "explanation": "The detection of two or more unique IgG oligoclonal bands in the CSF that are absent in matched paired serum samples demonstrates intrathecal immunoglobin synthesis, serving as a key supportive diagnostic feature of Multiple Sclerosis (under the McDonald criteria). The clinical history of optic neuritis and previous resolved myelopathy demonstrates neurological lesions disseminated in both time and space. Brain MRI with gadolinium contrast remains the primary investigation to assess for active and prior demyelinating plaques."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "An autopsy is performed on a 75-year-old man who had a history of resting tremor, rigidity, bradykinesia, and visual hallucinations. Histology of the substantia nigra reveals eosinophilic intracytoplasmic inclusions within neurons. What are these inclusions called?",
        "options": [
            "Lewy bodies",
            "Neurofibrillary tangles",
            "Pick bodies",
            "Hirano bodies",
            "Bunina bodies"
        ],
        "correct_answer": "Lewy bodies",
        "explanation": "Lewy bodies are round, eosinophilic, concentric intracytoplasmic inclusion bodies with a halo, composed predominantly of abnormally aggregated, misfolded alpha-synuclein protein. They represent the primary histological hallmark of both Parkinson's disease (where loss of dopaminergic neurons in the substantia nigra pars compacta is prominent) and Dementia with Lewy Bodies (DLB), where widespread cortical Lewy bodies cause fluctuating cognition, Parkinsonism, and early visual hallucinations."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 45-year-old patient with severe depression is admitted to the psychiatric ward. They are mute, immobile, and hold unusual, awkward postures for hours without showing fatigue. When the doctor lifts the patient's arm, it remains exactly where it was placed. What is this sign called?",
        "options": [
            "Waxy flexibility (Catalepsy)",
            "Gegenhalten (Paratonia)",
            "Cogwheel rigidity",
            "Lead-pipe rigidity",
            "Mitgehen"
        ],
        "correct_answer": "Waxy flexibility (Catalepsy)",
        "explanation": "Waxy flexibility (flexibilitas cerea) is a classic motor sign of catatonia, characterized by initial slight resistance when moving the patient's limbs followed by the patient remaining in whatever position or posture they have been placed in, akin to bending a wax candle. Catatonia can occur in schizophrenia, severe affective disorders (depression or mania), and medical conditions (such as encephalitis). First-line pharmacological management is intravenous or oral lorazepam, with electroconvulsive therapy (ECT) indicated for refractory or malignant cases."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A patient dies from progressive encephalitis characterized by hydrophobia, hypersalivation, and pharyngeal spasms after an animal bite in a developing country. Brain biopsy shows eosinophilic cytoplasmic inclusions in the Purkinje cells of the cerebellum and hippocampal neurons. What are they?",
        "options": [
            "Negri bodies",
            "Cowdry A inclusions",
            "Guarnieri bodies",
            "Babes-Ernst granules",
            "Councilman bodies"
        ],
        "correct_answer": "Negri bodies",
        "explanation": "Negri bodies are sharply defined, eosinophilic, round or oval intracytoplasmic viral inclusion bodies found within the Purkinje cells of the cerebellum and pyramidal cells of the hippocampus. Their histological presence confirms rabies virus encephalitis (a Lyssavirus). Rabies causes a fatal encephalomyelitis characterized by aerophobia, hydrophobia (violent laryngeal spasms when attempting to swallow liquids), and autonomic instability, emphasizing the necessity of prompt post-exposure prophylaxis (rabies vaccine and rabies immunoglobulin) prior to symptom onset."
    },

    # =========================================================================
    # 10. RENAL / UROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 60-year-old man undergoes major abdominal surgery complicated by severe hypotension. Three days later, his creatinine rises from 80 to 450 umol/L. Urine microscopy is performed. Which characteristic finding on urine microscopy confirms Acute Tubular Necrosis (ATN)?",
        "options": [
            "Muddy brown casts",
            "Hyaline casts",
            "Broad waxy casts",
            "White blood cell casts",
            "Fatty casts"
        ],
        "correct_answer": "Muddy brown casts",
        "explanation": "'Muddy brown' coarse granular casts (composed of sloughed, necrotic tubular epithelial cells and Tamm-Horsfall mucoprotein) in the urinary sediment are a diagnostic hallmark of Acute Tubular Necrosis (ATN). ATN is the most frequent intrinsic cause of acute kidney injury in hospitalized patients, typically resulting from prolonged renal hypoperfusion (ischaemic ATN) or nephrotoxic agents like aminoglycosides, radiocontrast, or NSAIDs."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 25-year-old man presents with macroscopic haematuria and hypertension 2 weeks after a severe sore throat. Urine microscopy reveals distorted erythrocytes and cylindrical structures. Which type of urinary casts is characteristic of acute glomerulonephritis (nephritic syndrome)?",
        "options": [
            "Red blood cell casts",
            "Muddy brown casts",
            "White blood cell casts",
            "Hyaline casts",
            "Eosinophil casts"
        ],
        "correct_answer": "Red blood cell casts",
        "explanation": "Red blood cell (RBC) casts are formed when erythrocytes pass through a damaged glomerular basement membrane and become entrapped in a matrix of Tamm-Horsfall protein within the distal nephron. Finding RBC casts confirms intrinsic glomerular bleeding, strongly indicating an active proliferative glomerulonephritis (nephritic syndrome), such as post-streptococcal glomerulonephritis, IgA nephropathy, or ANCA-associated vasculitis."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 45-year-old woman with nephrotic syndrome undergoes a renal biopsy. Silver staining and electron microscopy show thickening of the glomerular basement membrane with subepithelial immune complex deposits, forming a characteristic 'spike and dome' appearance. What is the diagnosis?",
        "options": [
            "Membranous nephropathy",
            "Minimal change disease",
            "Focal segmental glomerulosclerosis",
            "IgA nephropathy",
            "Diabetic nephropathy"
        ],
        "correct_answer": "Membranous nephropathy",
        "explanation": "A 'spike and dome' pattern on silver staining and electron microscopy is the diagnostic hallmark of membranous nephropathy. The 'spikes' represent projections of newly formed glomerular basement membrane matrix protruding between subepithelial IgG and C3 immune complex deposits ('domes'). In approximately 70–80% of primary cases in adults, it is mediated by autoantibodies against the M-type phospholipase A2 receptor (anti-PLA2R); secondary causes include malignancies, hepatitis B, SLE, and medications."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 30-year-old man with Hepatitis C presents with mixed nephritic/nephrotic syndrome. A renal biopsy shows mesangial interposition into the capillary wall, causing a 'tram-track' or double-contour appearance of the glomerular basement membrane on light microscopy. What is the diagnosis?",
        "options": [
            "Membranoproliferative glomerulonephritis (MPGN)",
            "Post-streptococcal glomerulonephritis",
            "Alport syndrome",
            "Rapidly progressive glomerulonephritis",
            "Lupus nephritis class IV"
        ],
        "correct_answer": "Membranoproliferative glomerulonephritis (MPGN)",
        "explanation": "A 'tram-track' (or double-contour) appearance on light microscopy—caused by mesangial cell proliferation and matrix interposition splitting the glomerular capillary basement membrane—is the classic histological signature of membranoproliferative glomerulonephritis (MPGN). It frequently presents as a combined nephritic and nephrotic syndrome with low complement levels, and is strongly associated with chronic hepatitis C virus infection and cryoglobulinaemia."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 65-year-old man with a 25-year history of poorly controlled type 2 diabetes presents with proteinuria. A renal biopsy reveals nodular glomerulosclerosis with eosinophilic nodules at the periphery of the glomerulus. What are these classic nodules called?",
        "options": [
            "Kimmelstiel-Wilson nodules",
            "Aschoff bodies",
            "Mallory-Denk bodies",
            "Psammoma bodies",
            "Ferruginous bodies"
        ],
        "correct_answer": "Kimmelstiel-Wilson nodules",
        "explanation": "Kimmelstiel-Wilson nodules (intercapillary glomerulosclerosis) are rounded, acellular, eosinophilic PAS-positive nodules formed within the mesangium of the renal glomeruli. They represent advanced, irreversible diabetic nephropathy (diabetic glomerulosclerosis). Early diabetic renal disease begins with glomerular hyperfiltration and microalbuminuria; finding Kimmelstiel-Wilson nodules signifies severe chronic microvascular damage, typically accompanied by diabetic retinopathy."
    },

    # =========================================================================
    # 11. REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 28-year-old pregnant woman presents at 10 weeks gestation with severe hyperemesis, a uterus large for dates, and vaginal bleeding. Transvaginal ultrasound demonstrates a heterogeneous mass with multiple cystic spaces, and an absence of fetal parts. What is the classic term for this ultrasound appearance?",
        "options": [
            "Snowstorm appearance",
            "Ground glass appearance",
            "Wheel spoke pattern",
            "Honeycomb pattern",
            "Whirlpool sign"
        ],
        "correct_answer": "Snowstorm appearance",
        "explanation": "A 'snowstorm' (or 'granular') ultrasound appearance—featuring an enlarged uterine cavity filled with a heterogeneous, echogenic mass and numerous small cystic vesicles without an identifiable fetus or amniotic sac—is characteristic of a complete hydatidiform mole. This molar pregnancy results from fertilization of an enucleated ovum by one or two sperm (typically 46,XX diploid). Serum beta-hCG levels are markedly elevated, accounting for prominent theca lutein cysts and pronounced hyperemesis gravidarum. Treatment is suction evacuation followed by serial hCG monitoring."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 32-year-old woman presents with severe secondary dysmenorrhoea and deep dyspareunia. A laparoscopy is performed, revealing an ovarian cyst filled with thick, dark, old blood. What is the common clinical term for this finding in endometriosis?",
        "options": [
            "Chocolate cyst",
            "Dermoid cyst",
            "Corpus luteum cyst",
            "Theca lutein cyst",
            "Simple follicular cyst"
        ],
        "correct_answer": "Chocolate cyst",
        "explanation": "An ovarian endometrioma is colloquially termed a 'chocolate cyst' because repeated cyclic haemorrhage from ectopic endometrial glandular tissue inside the ovary produces thick, dark, syrupy fluid resembling melted chocolate. Endometriomas are strongly indicative of moderate-to-severe endometriosis. Definitive diagnosis requires laparoscopy, and management encompasses hormonal suppression (e.g. combined oral contraceptives, progestogens, or GnRH analogues) or laparoscopic cystectomy to alleviate dysmenorrhoea and preserve fertility."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 24-year-old woman presents with an offensive, thin, grey-white vaginal discharge. The pH is >4.5 and a 'whiff test' with potassium hydroxide produces a fishy odour. Microscopy of the discharge reveals vaginal squamous epithelial cells covered in bacteria, obscuring their borders. What are these cells called?",
        "options": [
            "Clue cells",
            "Koilocytes",
            "Parabasal cells",
            "Navicular cells",
            "Donovan bodies"
        ],
        "correct_answer": "Clue cells",
        "explanation": "Clue cells are vaginal squamous epithelial cells whose borders are studded and obscured by adherent coccobacilli (predominantly Gardnerella vaginalis). Their presence on wet mount microscopy is a cornerstone of the Amsel criteria for diagnosing Bacterial Vaginosis (BV), which also requires three of: a homogeneous grey-white discharge, vaginal pH >4.5, and a positive amine 'whiff test' upon adding 10% KOH. BV represents a dysbiosis where protective hydrogen peroxide-producing lactobacilli are displaced by anaerobic overgrowth; oral metronidazole is first-line treatment."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 27-year-old woman presents with a frothy, yellow-green vaginal discharge and vulval itch. On speculum examination, the cervix has multiple punctate haemorrhages. What is this classic clinical sign called?",
        "options": [
            "Strawberry cervix",
            "Cobblestone cervix",
            "Ectropion",
            "Nabothian cyst",
            "Cervical leukoplakia"
        ],
        "correct_answer": "Strawberry cervix",
        "explanation": "A 'strawberry cervix' (colpitis macularis) describes punctate micro-haemorrhages scattered across the ectocervix, giving it the appearance of a ripe strawberry. It is a highly specific physical sign of Trichomonas vaginalis infection, an STI caused by a flagellated protozoan. Patients typically present with a copious, frothy, malodorous yellow-green discharge, dysuria, and vulval irritation. Both the patient and sexual partners should be treated with oral metronidazole."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 29-year-old woman presents with oligomenorrhoea, hirsutism, and infertility. A pelvic ultrasound shows enlarged ovaries with multiple small peripherally arranged follicles (typically 12 or more per ovary). What is the classic term for this ultrasound appearance?",
        "options": [
            "String of pearls sign",
            "Snowstorm sign",
            "Cogwheel sign",
            "Tip of the iceberg sign",
            "Whirlpool sign"
        ],
        "correct_answer": "String of pearls sign",
        "explanation": "The 'string of pearls' (or 'necklace') sign on pelvic ultrasound describes the peripheral distribution of 12 or more subcentimeter antral follicles (typically 2–9 mm in diameter) encircling an increased hyperechoic central ovarian stroma. This is the characteristic sonographic morphology of Polycystic Ovary Syndrome (PCOS). Under the Rotterdam diagnostic criteria, PCOS requires at least two of: oligo/anovulation, clinical or biochemical hyperandrogenism, and polycystic ovarian morphology on ultrasound."
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
            "Tree-in-bud pattern",
            "Crazy paving pattern",
            "Halo sign",
            "Reverse halo sign"
        ],
        "correct_answer": "Signet ring sign",
        "explanation": "The 'signet ring' sign on high-resolution chest CT (HRCT) is the radiographic hallmark of bronchiectasis. In normal lungs, a bronchus has roughly the same calibre as its accompanying pulmonary artery (bronchoarterial ratio = 1). In bronchiectasis, chronic inflammation causes irreversible bronchial dilatation, making the cross-sectional airway significantly larger than the adjacent artery and resembling a signet ring. Cylindrical bronchiectasis viewed longitudinally also produces thickened parallel 'tram-track' opacities."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 70-year-old man presents with progressive exertional dyspnoea and a dry cough. Auscultation reveals fine, end-inspiratory 'Velcro-like' crackles at the lung bases. HRCT demonstrates subpleural, basal predominant reticular opacities with clustered cystic air spaces. What is the term for this advanced cystic change?",
        "options": [
            "Honeycomb lung",
            "Ground glass opacities",
            "Emphysema",
            "Pneumatocele",
            "Bronchiolectasis"
        ],
        "correct_answer": "Honeycomb lung",
        "explanation": "Honeycombing describes clustered, thick-walled cystic spaces (typically 3–10 mm in diameter) arranged in rows beneath the pleura, accompanied by traction bronchiectasis and architectural distortion. On high-resolution CT, a subpleural and basilar predominant honeycombing pattern defines the usual interstitial pneumonia (UIP) pattern, which provides definitive confirmation of idiopathic pulmonary fibrosis (IPF) in the appropriate clinical setting, eliminating the need for invasive surgical lung biopsy."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 35-year-old woman of Afro-Caribbean descent presents with erythema nodosum, uveitis, and a dry cough. A chest X-ray shows bilateral hilar lymphadenopathy. A transbronchial biopsy is performed. Which histological feature confirms the diagnosis of sarcoidosis?",
        "options": [
            "Non-caseating granulomas",
            "Caseating granulomas with central necrosis",
            "Reed-Sternberg cells",
            "Atypical lymphoid infiltrates",
            "Cavitating lesions with fungal balls"
        ],
        "correct_answer": "Non-caseating granulomas",
        "explanation": "Non-caseating (non-necrotising) epithelioid granulomas—composed of compact aggregates of epithelioid histiocytes and multinucleated Langhans giant cells without central necrosis—are the defining histological finding in sarcoidosis. This contrasts with tuberculosis, which typically produces caseating (necrotising) granulomas. The presentation with bilateral hilar lymphadenopathy, erythema nodosum, and bilateral ankle arthralgia is specifically known as Löfgren's syndrome, an acute form of sarcoidosis with an excellent spontaneous remission rate."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 12-year-old boy with a known history of severe asthma provides a sputum sample during an exacerbation. Microscopy reveals spiral-shaped mucus plugs and hexagonal, double-pointed crystals derived from eosinophil breakdown. What are these crystals called?",
        "options": [
            "Charcot-Leyden crystals",
            "Curschmann spirals",
            "Ferruginous bodies",
            "Cholesterol crystals",
            "Calcium oxalate crystals"
        ],
        "correct_answer": "Charcot-Leyden crystals",
        "explanation": "Charcot-Leyden crystals are slender, bipyramidal hexagonal structures formed from the crystallisation of galectin-10 (a lysophospholipase protein) derived from the degeneration of eosinophils. Their presence in sputum or bronchoalveolar lavage fluid reflects marked eosinophilic airway inflammation, characteristic of severe bronchial asthma and allergic bronchopulmonary aspergillosis (ABPA). Sputum microscopy in asthmatics may also reveal Curschmann spirals (coiled casts of condensed mucus formed in small bronchioles)."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 45-year-old woman presents with sudden onset pleuritic chest pain, haemoptysis, and shortness of breath following a long-haul flight. A chest X-ray shows a wedge-shaped opacity in the right lower lobe with its base against the pleura. What is this sign known as?",
        "options": [
            "Hampton's hump",
            "Westermark sign",
            "Fleischner sign",
            "Palla's sign",
            "Golden S sign"
        ],
        "correct_answer": "Hampton's hump",
        "explanation": "Hampton's hump is a peripheral, wedge-shaped pulmonary opacity with its broad base abutted against the visceral pleura and its apex directed toward the hilum. It is a classic radiological sign of pulmonary infarction following a pulmonary embolism (PE), typically developing in distal pulmonary arterial occlusions. Another recognized radiological sign of PE on chest radiography is Westermark's sign (focal oligaemia distal to the occluded vessel). CT Pulmonary Angiography (CTPA) is the gold standard diagnostic investigation."
    }
]
