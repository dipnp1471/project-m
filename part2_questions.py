# -*- coding: utf-8 -*-
"""
Part 2: Infectious Diseases / Haematology / Immunology / Allergies / Genetics, Musculoskeletal, Paediatrics, Psychiatry / Neurology
4 clinical domains x 13 questions (8 SBA + 5 EMQ) = 52 questions.
"""

PART2_QUESTIONS = [
    # =========================================================================
    # 5. INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 54-year-old woman undergoing chemotherapy for breast cancer presents to the Acute Assessment Unit with chills and rigors. Her temperature is 38.6°C, blood pressure is 102/64 mmHg, and heart rate is 114 bpm. An urgent full blood count reveals an absolute neutrophil count of 0.3 x 10^9/L (reference 2.0-7.0). What is the single most urgent therapeutic priority according to NICE guidelines?",
        "options": [
            "Immediate intravenous Piperacillin-Tazobactam (Tazocin) within 1 hour",
            "Awaiting blood and urine culture results before starting targeted antibiotics",
            "Subcutaneous Granulocyte Colony-Stimulating Factor (G-CSF) alone",
            "Intravenous Fluconazole and oral Ciprofloxacin",
            "Oral Co-amoxiclav and outpatient review in 24 hours"
        ],
        "correct_answer": "Immediate intravenous Piperacillin-Tazobactam (Tazocin) within 1 hour",
        "explanation": "Neutropenic sepsis is defined as a temperature >=38°C (or signs of sepsis) with an absolute neutrophil count <0.5 x 10^9/L in a patient who has received chemotherapy. It is an oncological emergency. NICE guidelines mandate immediate administration of intravenous broad-spectrum antipseudomonal beta-lactam monotherapy (usually Piperacillin-Tazobactam) within 1 hour of arrival (the 'Golden Hour') without waiting for culture results."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 34-year-old keen hiker presents with an expanding erythematous macular rash with central clearing ('bull's eye' appearance) on his thigh that appeared 10 days after walking in the New Forest. He has mild malaise and arthralgia. He has no recollection of an insect bite. What is the most appropriate management according to NICE guidelines?",
        "options": [
            "Clinical diagnosis of Lyme disease; prescribe oral Doxycycline for 21 days immediately without serological testing",
            "Order urgent Borrelia burgdorferi ELISA serology and withhold treatment pending results",
            "Prescribe topical Hydrocortisone 1% cream for 2 weeks",
            "Administer a single intramuscular dose of Ceftriaxone",
            "Reassure that this is an exaggerated insect bite reaction"
        ],
        "correct_answer": "Clinical diagnosis of Lyme disease; prescribe oral Doxycycline for 21 days immediately without serological testing",
        "explanation": "Erythema migrans is diagnostic of early localized Lyme disease (Borrelia burgdorferi). NICE guidelines explicitly state that in the presence of classic erythema migrans, treatment (oral Doxycycline 100 mg BD for 21 days, or Amoxicillin if contraindicated) should be started immediately on clinical grounds without performing serological tests, which are frequently false-negative in early disease."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 19-year-old university student is brought to the ED with severe headache, photophobia, fever, and neck stiffness. Examination shows positive Kernig's and Brudzinski's signs and a sparse non-blanching petechial rash on the torso. Blood pressure is 110/70 mmHg, heart rate is 108 bpm. While preparing for blood cultures and emergency hospital treatment, what is the first-line empirical antibiotic regimen?",
        "options": [
            "Intravenous Ceftriaxone 2 g BD plus Dexamethasone 10 mg QDS",
            "Oral Amoxicillin 1 g TDS",
            "Intravenous Vancomycin monotherapy",
            "Intravenous Gentamicin plus Metronidazole",
            "Intramuscular Benzylpenicillin only if LP cannot be performed"
        ],
        "correct_answer": "Intravenous Ceftriaxone 2 g BD plus Dexamethasone 10 mg QDS",
        "explanation": "The clinical presentation is acute meningococcal meningitis. In secondary care, immediate treatment consists of intravenous Ceftriaxone (2 g every 12 hours) and intravenous Dexamethasone (10 mg every 6 hours, started before or with the first dose of antibiotics to reduce neurological sequelae and hearing loss in bacterial meningitis)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 24-year-old man eats a peanut satay meal and within 10 minutes develops generalized urticaria, facial and tongue angioedema, inspiratory stridor, and wheeze. His blood pressure drops to 82/48 mmHg and oxygen saturation is 90% on room air. What is the immediate drug, dose, and route of administration of first choice according to UK Resuscitation Council guidelines?",
        "options": [
            "Intramuscular Adrenaline 500 micrograms (0.5 mL of 1:1,000) in the anterolateral thigh",
            "Intravenous Adrenaline 1 mg (1 mL of 1:1,000) rapid push",
            "Intravenous Chlorphenamine 10 mg plus Hydrocortisone 200 mg",
            "Nebulised Salbutamol 5 mg with high-flow oxygen",
            "Subcutaneous Adrenaline 300 micrograms"
        ],
        "correct_answer": "Intramuscular Adrenaline 500 micrograms (0.5 mL of 1:1,000) in the anterolateral thigh",
        "explanation": "The patient has life-threatening anaphylaxis with airway, breathing, and circulation compromise. Intramuscular Adrenaline (epinephrine) 500 micrograms (0.5 mL of 1:1,000) administered into the anterolateral aspect of the middle third of the thigh is the mandatory first-line treatment, repeated after 5 minutes if there is no response."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 71-year-old man presents with persistent lower back pain, lethargy, and recurrent chest infections. Investigations show: Hb 92 g/L (normocytic), corrected calcium 2.88 mmol/L (2.20-2.60), serum creatinine 188 micromol/L (60-110), ESR 110 mm/hr. A skeletal survey reveals multiple punched-out lytic lesions in the skull and vertebrae. Which investigation is essential to confirm the paraproteinemia?",
        "options": [
            "Serum protein electrophoresis (SPEP) and serum free light chain (SFLC) assay",
            "24-hour urine microscopy for dysmorphic red cells",
            "Abdominal ultrasound",
            "Rheumatoid factor and anti-CCP titre",
            "Technetium-99m bone scintigraphy"
        ],
        "correct_answer": "Serum protein electrophoresis (SPEP) and serum free light chain (SFLC) assay",
        "explanation": "The patient exhibits the classic 'CRAB' features of Multiple Myeloma: Calcium elevation, Renal impairment, Anaemia, and Bone disease (lytic punched-out lesions). Definitive initial screening requires serum protein electrophoresis (to identify monoclonal IgG or IgA M-spikes) and serum free light chain (SFLC) assay (or urine Bence-Jones protein)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 28-year-old woman is noted to have petechiae and ecchymoses on her shins. She is otherwise well and takes no medications. Bloods reveal: platelets 14 x 10^9/L (150-400), Hb 134 g/L, WBC 6.8 x 10^9/L. Blood film shows isolated severe thrombocytopenia with no fragmented red cells (schistocytes). Coagulation screen, renal function, and liver function are normal. What is the most likely diagnosis?",
        "options": [
            "Immune Thrombocytopenia (ITP)",
            "Thrombotic Thrombocytopenic Purpura (TTP)",
            "Disseminated Intravascular Coagulation (DIC)",
            "Haemolytic Uraemic Syndrome (HUS)",
            "Aplastic Anaemia"
        ],
        "correct_answer": "Immune Thrombocytopenia (ITP)",
        "explanation": "Isolated thrombocytopenia in a well patient without systemic features, anaemia, coagulopathy, or red blood cell fragmentation on blood film is the classic presentation of Immune Thrombocytopenia (ITP), caused by autoantibodies directed against platelet surface glycoproteins. First-line therapy when treatment is indicated (e.g. platelets <30 or bleeding) is oral corticosteroids (prednisolone) or IVIG."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 21-year-old man with sickle cell disease (HbSS) is admitted with severe bony pain. On day 2, he becomes acutely short of breath with pleuritic chest pain and a temperature of 38.4°C. Vitals: RR 28 breaths/min, HR 118 bpm, SpO2 89% on room air. Chest X-ray demonstrates new bilateral pulmonary infiltrates. What is the diagnosis and most severe potential complication?",
        "options": [
            "Acute Chest Syndrome; carries significant risk of respiratory failure and mortality",
            "Simple bacterial lobar pneumonia; treated with oral antibiotics alone",
            "Pneumothorax; requires immediate intercostal chest drain insertion",
            "Pulmonary infarction without need for transfusion",
            "Bronchial asthma exacerbation; treat with nebulised bronchodilators"
        ],
        "correct_answer": "Acute Chest Syndrome; carries significant risk of respiratory failure and mortality",
        "explanation": "Acute Chest Syndrome (ACS) is defined in sickle cell disease by a new pulmonary infiltrate on chest radiography combined with fever and/or respiratory symptoms. It is the leading cause of death in SCD. Management includes high-flow oxygen, analgesia, broad-spectrum antibiotics, fluid balance monitoring, and early blood transfusion (or automated red cell exchange transfusion if severe/hypoxic)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 32-year-old woman returns from rural Nigeria 8 days ago and presents with spiking fevers, rigors, headache, and jaundice. Blood film microscopy confirms Plasmodium falciparum malaria with a parasitaemia of 8% (severe malaria definition >2%). She is somnolent with a blood glucose of 2.9 mmol/L. What is the first-line treatment for severe malaria according to UK and WHO guidelines?",
        "options": [
            "Intravenous Artesunate",
            "Oral Artemether-Lumefantrine (Riamet)",
            "Intravenous Chloroquine",
            "Oral Atovaquone-Proguanil (Malarone)",
            "Intravenous Primaquine"
        ],
        "correct_answer": "Intravenous Artesunate",
        "explanation": "Intravenous Artesunate is the first-line treatment of choice for severe falciparum malaria (parasitaemia >2%, impaired consciousness, jaundice, severe anaemia, or hypoglycaemia), having demonstrated significantly lower mortality compared to intravenous quinine. Hypoglycaemia must also be promptly corrected."
    },
    # Infectious / Haematology EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "Theme: Investigation of Anaemia. Match each clinical scenario with the most likely diagnosis.\n\nVignette 1: A 52-year-old woman with menorrhagia presents with fatigue and pica (craving ice). Investigations reveal: Hb 86 g/L, MCV 71 fL (80-100), serum ferritin 8 mcg/L (reference >30), and Total Iron Binding Capacity (TIBC) is markedly increased.",
        "options": [
            "Iron Deficiency Anaemia",
            "Anaemia of Chronic Disease",
            "Beta-Thalassaemia Trait",
            "Vitamin B12 Deficiency",
            "Autoimmune Haemolytic Anaemia (AIHA)",
            "Aplastic Anaemia",
            "Sideroblastic Anaemia",
            "Folate Deficiency"
        ],
        "correct_answer": "Iron Deficiency Anaemia",
        "explanation": "Microcytic anaemia with profoundly low serum ferritin and elevated TIBC (reflecting increased transferrin production) is diagnostic of iron deficiency anaemia."
    },
    {
        "type": "emq",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "Theme: Investigation of Anaemia. Match each clinical scenario with the most likely diagnosis.\n\nVignette 2: A 62-year-old man with severe active rheumatoid arthritis presents with chronic fatigue. Bloods show: Hb 98 g/L, MCV 84 fL (normocytic), serum ferritin 480 mcg/L (elevated), serum iron low, and Total Iron Binding Capacity (TIBC) is reduced.",
        "options": [
            "Iron Deficiency Anaemia",
            "Anaemia of Chronic Disease",
            "Beta-Thalassaemia Trait",
            "Vitamin B12 Deficiency",
            "Autoimmune Haemolytic Anaemia (AIHA)",
            "Aplastic Anaemia",
            "Sideroblastic Anaemia",
            "Folate Deficiency"
        ],
        "correct_answer": "Anaemia of Chronic Disease",
        "explanation": "Normocytic (or mildly microcytic) anaemia in chronic inflammation, mediated by hepcidin which sequesters iron in macrophages, resulting in low serum iron, high ferritin (acute phase reactant), and low TIBC."
    },
    {
        "type": "emq",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "Theme: Investigation of Anaemia. Match each clinical scenario with the most likely diagnosis.\n\nVignette 3: An asymptomatic 24-year-old pregnant woman of Mediterranean origin is screened at booking. Bloods show: Hb 108 g/L, MCV 62 fL (disproportionately profound microcytosis with normal red cell count), serum ferritin 95 mcg/L (normal). Haemoglobin electrophoresis demonstrates an elevated HbA2 of 5.2% (reference <3.5%).",
        "options": [
            "Iron Deficiency Anaemia",
            "Anaemia of Chronic Disease",
            "Beta-Thalassaemia Trait",
            "Vitamin B12 Deficiency",
            "Autoimmune Haemolytic Anaemia (AIHA)",
            "Aplastic Anaemia",
            "Sideroblastic Anaemia",
            "Folate Deficiency"
        ],
        "correct_answer": "Beta-Thalassaemia Trait",
        "explanation": "Disproportionate severe microcytosis with mild anaemia, normal ferritin, and an elevated HbA2 level (>3.5%) confirms beta-thalassaemia trait (minor)."
    },
    {
        "type": "emq",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "Theme: Investigation of Anaemia. Match each clinical scenario with the most likely diagnosis.\n\nVignette 4: A 68-year-old woman presents with fatigue, lemon-yellow skin tint, painful glossitis, and numbness in her feet with loss of proprioception and vibration sense. Bloods show: Hb 78 g/L, MCV 118 fL (macrocytic), and blood film displays hypersegmented neutrophils. Anti-intrinsic factor antibodies are positive.",
        "options": [
            "Iron Deficiency Anaemia",
            "Anaemia of Chronic Disease",
            "Beta-Thalassaemia Trait",
            "Vitamin B12 Deficiency",
            "Autoimmune Haemolytic Anaemia (AIHA)",
            "Aplastic Anaemia",
            "Sideroblastic Anaemia",
            "Folate Deficiency"
        ],
        "correct_answer": "Vitamin B12 Deficiency",
        "explanation": "Macrocytic megaloblastic anaemia with hypersegmented neutrophils and neurological signs of subacute combined degeneration of the cord (SCDC) caused by pernicious anaemia (anti-intrinsic factor positive) and severe B12 deficiency."
    },
    {
        "type": "emq",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "Theme: Investigation of Anaemia. Match each clinical scenario with the most likely diagnosis.\n\nVignette 5: A 38-year-old woman with systemic lupus erythematosus presents with jaundice and dark urine. Bloods reveal: Hb 82 g/L, MCV 94 fL, reticulocytes 7.8% (elevated), unconjugated bilirubin 54 micromol/L, undetectable haptoglobin, and spherocytes on blood film. The Direct Antiglobulin (Coombs) test is strongly positive for IgG.",
        "options": [
            "Iron Deficiency Anaemia",
            "Anaemia of Chronic Disease",
            "Beta-Thalassaemia Trait",
            "Vitamin B12 Deficiency",
            "Autoimmune Haemolytic Anaemia (AIHA)",
            "Aplastic Anaemia",
            "Sideroblastic Anaemia",
            "Folate Deficiency"
        ],
        "correct_answer": "Autoimmune Haemolytic Anaemia (AIHA)",
        "explanation": "Extravascular haemolysis (elevated unconjugated bilirubin, high reticulocytes, low haptoglobin, spherocytes) with a positive direct antiglobulin (Coombs) test confirming warm IgG autoantibodies indicates Autoimmune Haemolytic Anaemia (AIHA)."
    },

    # =========================================================================
    # 6. MUSCULOSKELETAL (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 56-year-old man with diabetes presents with acute severe pain, erythema, and massive swelling of his right knee that developed over 18 hours. He is unable to weight-bear. Vitals: temperature 38.8°C, HR 102 bpm. On examination, the joint is warm, tense, and held in 30 degrees of flexion with active and passive range of motion restricted by excruciating pain. What is the single most important diagnostic procedure that must be performed before initiating antibiotics?",
        "options": [
            "Urgent diagnostic synovial fluid aspiration (arthrocentesis)",
            "Plain radiograph of the right knee",
            "MRI of the right knee",
            "Serum uric acid level measurement",
            "Ultrasound-guided intra-articular steroid injection"
        ],
        "correct_answer": "Urgent diagnostic synovial fluid aspiration (arthrocentesis)",
        "explanation": "Any acute warm, swollen monoarthritis with systemic fever and inability to weight-bear is suspected septic arthritis until proven otherwise. Urgent synovial fluid aspiration for microscopy (Gram stain, white cell count, and crystal analysis) and culture must be performed immediately prior to commencing empirical intravenous antibiotics (e.g. Flucloxacillin)."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 44-year-old builder presents with severe low back pain radiating down both legs into his calves and feet. Over the past 6 hours, he has noticed numbness in his perineal area and experienced two episodes of urinary incontinence without the sensation of a full bladder. Examination reveals absent ankle reflexes bilaterally, decreased perianal sensation, and lax anal sphincter tone on digital rectal examination. What is the immediate mandatory management?",
        "options": [
            "Emergency MRI of the whole spine and urgent neurosurgical/orthopaedic spinal referral",
            "Prescribe oral Naproxen and arrange outpatient physiotherapy",
            "Perform a diagnostic lumbar puncture",
            "Order a plain lumbar spine radiograph and discharge with a urinary catheter",
            "Arrange an urgent outpatient electromyography (EMG)"
        ],
        "correct_answer": "Emergency MRI of the whole spine and urgent neurosurgical/orthopaedic spinal referral",
        "explanation": "Bilateral radicular leg pain, saddle anaesthesia, bladder dysfunction (incontinence/retention), and lax anal tone are red flag symptoms of Cauda Equina Syndrome (CES). This is a surgical emergency. Immediate whole-spine MRI must be performed without delay to confirm compression (usually massive central disc herniation) followed by emergency surgical decompression within 24-48 hours to avoid irreversible neurological disability."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 69-year-old woman presents with a 2-month history of severe aching and morning stiffness lasting over an hour in both shoulders and hip girdles, making it difficult to raise her arms to brush her hair or rise from a low chair. She has no muscle weakness on testing. Investigations reveal: ESR 76 mm/hr, CRP 42 mg/L, and normal creatine kinase (CK). What is the first-line therapeutic management for polymyalgia rheumatica (PMR)?",
        "options": [
            "Oral Prednisolone 15 mg daily",
            "Oral Methotrexate 15 mg weekly",
            "High-dose intravenous Methylprednisolone 500 mg",
            "Oral Naproxen 500 mg twice daily",
            "Intramuscular Gold injections"
        ],
        "correct_answer": "Oral Prednisolone 15 mg daily",
        "explanation": "Bilateral shoulder and pelvic girdle aching, morning stiffness >45 minutes, elevated inflammatory markers, and age >50 with normal CK is diagnostic of Polymyalgia Rheumatica (PMR). The cornerstone of treatment according to BSR guidelines is low-to-moderate dose oral prednisolone (typically 15 mg daily), which characteristically produces rapid, dramatic clinical improvement within 48-72 hours."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 24-year-old man presents with chronic lower back pain and stiffness for 9 months. The stiffness is worst in the early morning, lasting 90 minutes, and improves significantly with exercise but not with rest. He has developed pain and swelling in his left Achilles tendon. Pelvic radiograph reveals bilateral subchondral sclerosis and erosions of the sacroiliac joints. HLA-B27 is positive. What is the recommended first-line pharmacological treatment?",
        "options": [
            "Continuous full-dose Non-Steroidal Anti-Inflammatory Drugs (NSAIDs) plus structured physiotherapy",
            "Oral Prednisolone 30 mg daily",
            "Immediate Infliximab (anti-TNF) biologic therapy",
            "Oral Paracetamol 1 g four times daily",
            "Spinal surgical fusion"
        ],
        "correct_answer": "Continuous full-dose Non-Steroidal Anti-Inflammatory Drugs (NSAIDs) plus structured physiotherapy",
        "explanation": "The patient has Ankylosing Spondylitis (radiographic axial spondyloarthritis). First-line treatment according to ASAS/EULAR guidelines is continuous full-dose NSAIDs (e.g. naproxen or celecoxib) along with regular structured physical therapy. Anti-TNF biologics (e.g., Adalimumab) are indicated only if disease remains active despite trying at least two different NSAIDs."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 68-year-old man with Chronic Kidney Disease (stage 4, baseline eGFR 22 mL/min/1.73m2) presents with an acute, exquisitely painful, swollen first metatarsophalangeal (MTP) joint. Polarised light microscopy of joint aspirate confirms negatively birefringent needle-shaped monosodium urate crystals. Which treatment is most appropriate for this acute gout flare?",
        "options": [
            "Intra-articular corticosteroid injection (or short-course low-dose oral steroid)",
            "High-dose oral Ibuprofen 800 mg TDS",
            "Immediate initiation of Allopurinol 300 mg daily",
            "High-dose Colchicine 500 mcg four times daily",
            "Intravenous Ketorolac"
        ],
        "correct_answer": "Intra-articular corticosteroid injection (or short-course low-dose oral steroid)",
        "explanation": "In patients with severe renal impairment (eGFR <30), NSAIDs are strictly contraindicated due to nephrotoxicity risk, and colchicine should be avoided or used with extreme caution at drastically reduced doses due to neuromuscular toxicity. Intra-articular corticosteroid injection (or a short course of oral prednisolone) is the safest and most effective choice. Allopurinol is never initiated during an acute flare."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 22-year-old motorcyclist sustains a closed mid-shaft tibial fracture. Four hours after cast application, he develops severe, crescendo calf pain that is completely unresponsive to intravenous morphine. On examination, the anterior and deep posterior compartments are tense and 'woody'. Passive stretching of the toes reproduces excruciating pain. Distal dorsalis pedis pulses are still palpable. What is the definitive emergency management?",
        "options": [
            "Emergency decompressive fasciotomy of all four compartments",
            "Increase intravenous morphine dosage and elevate the limb above heart level",
            "Immediate closed reduction and re-casting",
            "Therapeutic low molecular weight heparin",
            "Application of an external ice pack"
        ],
        "correct_answer": "Emergency decompressive fasciotomy of all four compartments",
        "explanation": "This patient has acute compartment syndrome, a limb-threatening surgical emergency. Pain out of proportion to injury and pain upon passive stretching of the affected muscle groups are the earliest and most reliable clinical indicators. Palpable distal pulses do NOT exclude compartment syndrome. Urgent emergency decompressive four-compartment fasciotomy is required to prevent muscle ischaemic necrosis and Volkmann's contracture."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 36-year-old woman presents with symmetrical pain, swelling, and morning stiffness lasting 2 hours affecting the MCP and PIP joints of both hands and both wrists for 8 weeks. Examination confirms active synovitis. Bloods show: anti-cyclic citrullinated peptide (anti-CCP) antibodies strongly positive, rheumatoid factor positive, CRP 38 mg/L. According to NICE guidelines, what is the recommended first-line disease-modifying antirheumatic drug (DMARD) strategy?",
        "options": [
            "Combination conventional synthetic DMARDs including Methotrexate plus short-term bridging corticosteroid",
            "Rituximab monotherapy",
            "Oral Prednisolone monotherapy for 12 months",
            "Hydroxychloroquine monotherapy only",
            "Adalimumab anti-TNF biologic therapy first-line"
        ],
        "correct_answer": "Combination conventional synthetic DMARDs including Methotrexate plus short-term bridging corticosteroid",
        "explanation": "NICE guideline NG100 recommends offering first-line conventional synthetic DMARD monotherapy or combination therapy (with Methotrexate as the core anchor drug, alongside sulfasalazine or leflunomide) ideally within 3 months of symptom onset, combined with a short-course bridging corticosteroid (oral, IM, or intra-articular) to achieve rapid symptom relief while the DMARD takes effect."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 76-year-old woman presents with sudden-onset sharp mid-thoracic back pain after lifting a bag of compost. She has lost 4 cm in height over the past 3 years. Neurological examination is completely normal. Thoracic spine X-ray reveals an acute anterior wedge compression fracture of T8 with generalized osteopenia. What is the recommended first-line pharmacological therapy to prevent future fractures?",
        "options": [
            "Oral Bisphosphonate (e.g., Alendronic acid) with Calcium and Vitamin D supplementation",
            "Continuous intravenous calcitonin infusion",
            "Oral high-dose Dexamethasone",
            "Hormone replacement therapy (HRT)",
            "Teriparatide subcutaneous injections first-line"
        ],
        "correct_answer": "Oral Bisphosphonate (e.g., Alendronic acid) with Calcium and Vitamin D supplementation",
        "explanation": "Fragility fracture in an elderly woman with height loss indicates severe osteoporosis. NICE guidelines recommend oral bisphosphonates (alendronic acid 70 mg once weekly or risedronate 35 mg once weekly) combined with calcium and vitamin D optimization as first-line secondary fracture prevention."
    },
    # Musculoskeletal EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Musculoskeletal",
        "scenario": "Theme: Knee and Shoulder Pathology. Match each clinical vignette with the most likely diagnosis.\n\nVignette 1: An 18-year-old football player decelerates and twists rapidly on a planted foot, hearing an audible 'pop' inside the knee. Within 2 hours, the knee is tensely swollen from acute haemarthrosis. On examination, the Lachman test is strongly positive with anterior tibial translation.",
        "options": [
            "Anterior Cruciate Ligament (ACL) Tear",
            "Meniscal Tear",
            "Rotator Cuff Tear",
            "Adhesive Capsulitis (Frozen Shoulder)",
            "Ruptured Baker's (Popliteal) Cyst",
            "Patellar Tendinopathy",
            "Subacromial Impingement Syndrome",
            "Posterior Cruciate Ligament (PCL) Tear"
        ],
        "correct_answer": "Anterior Cruciate Ligament (ACL) Tear",
        "explanation": "A twisting knee injury with an audible pop, rapid-onset haemarthrosis (<4 hours), and positive anterior translation on the Lachman or anterior drawer test is classic for an acute ACL rupture."
    },
    {
        "type": "emq",
        "category": "Musculoskeletal",
        "scenario": "Theme: Knee and Shoulder Pathology. Match each clinical vignette with the most likely diagnosis.\n\nVignette 2: A 34-year-old rugby player sustains a twisting injury to his knee. Over the next 24-48 hours, he notices gradual mild effusion. He complains of recurrent mechanical 'locking' where the knee gets stuck in flexion, and localized tenderness along the medial joint line.",
        "options": [
            "Anterior Cruciate Ligament (ACL) Tear",
            "Meniscal Tear",
            "Rotator Cuff Tear",
            "Adhesive Capsulitis (Frozen Shoulder)",
            "Ruptured Baker's (Popliteal) Cyst",
            "Patellar Tendinopathy",
            "Subacromial Impingement Syndrome",
            "Posterior Cruciate Ligament (PCL) Tear"
        ],
        "correct_answer": "Meniscal Tear",
        "explanation": "Delayed joint effusion (24-48 hours), joint-line tenderness, and true mechanical locking (inability to fully extend the knee) strongly point to a bucket-handle meniscal tear."
    },
    {
        "type": "emq",
        "category": "Musculoskeletal",
        "scenario": "Theme: Knee and Shoulder Pathology. Match each clinical vignette with the most likely diagnosis.\n\nVignette 3: A 58-year-old painter falls onto his outstretched arm. He presents with severe shoulder pain and inability to abduct his arm. When the arm is passively abducted to 90 degrees and released, he cannot hold it up and it falls abruptly to his side (positive drop arm sign).",
        "options": [
            "Anterior Cruciate Ligament (ACL) Tear",
            "Meniscal Tear",
            "Rotator Cuff Tear",
            "Adhesive Capsulitis (Frozen Shoulder)",
            "Ruptured Baker's (Popliteal) Cyst",
            "Patellar Tendinopathy",
            "Subacromial Impingement Syndrome",
            "Posterior Cruciate Ligament (PCL) Tear"
        ],
        "correct_answer": "Rotator Cuff Tear",
        "explanation": "Weakness in shoulder abduction and an inability to maintain passive 90-degree abduction (drop arm test) indicates a full-thickness supraspinatus/rotator cuff tear."
    },
    {
        "type": "emq",
        "category": "Musculoskeletal",
        "scenario": "Theme: Knee and Shoulder Pathology. Match each clinical vignette with the most likely diagnosis.\n\nVignette 4: A 53-year-old woman with poorly controlled Type 2 Diabetes presents with a 6-month history of insidious shoulder aching followed by profound stiffness. On examination, she has severe painful restriction of BOTH active and passive movements in all directions, most prominently external rotation.",
        "options": [
            "Anterior Cruciate Ligament (ACL) Tear",
            "Meniscal Tear",
            "Rotator Cuff Tear",
            "Adhesive Capsulitis (Frozen Shoulder)",
            "Ruptured Baker's (Popliteal) Cyst",
            "Patellar Tendinopathy",
            "Subacromial Impingement Syndrome",
            "Posterior Cruciate Ligament (PCL) Tear"
        ],
        "correct_answer": "Adhesive Capsulitis (Frozen Shoulder)",
        "explanation": "Adhesive capsulitis causes global restriction of both active and passive glenohumeral motion with profound loss of external rotation, highly prevalent in patients with diabetes mellitus."
    },
    {
        "type": "emq",
        "category": "Musculoskeletal",
        "scenario": "Theme: Knee and Shoulder Pathology. Match each clinical vignette with the most likely diagnosis.\n\nVignette 5: A 62-year-old man with osteoarthritis of the knee experiences a sudden tearing sensation behind his knee followed by painful calf swelling and erythema mimicking a deep vein thrombosis. Examination reveals a crescent of ecchymosis below the medial malleolus. Doppler ultrasound excludes DVT.",
        "options": [
            "Anterior Cruciate Ligament (ACL) Tear",
            "Meniscal Tear",
            "Rotator Cuff Tear",
            "Adhesive Capsulitis (Frozen Shoulder)",
            "Ruptured Baker's (Popliteal) Cyst",
            "Patellar Tendinopathy",
            "Subacromial Impingement Syndrome",
            "Posterior Cruciate Ligament (PCL) Tear"
        ],
        "correct_answer": "Ruptured Baker's (Popliteal) Cyst",
        "explanation": "Rupture of a Baker's (popliteal) cyst releases synovial fluid into the calf tissues, creating acute pain, erythema, and oedema that closely mimics DVT; bruising around the malleolus (crescent sign) is characteristic."
    },

    # =========================================================================
    # 7. PAEDIATRICS (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 4-month-old infant is brought to the ED in December with a 3-day history of clear rhinorrhoea and low-grade fever, progressing to persistent paroxysmal coughing and breathlessness. On examination: RR 66 breaths/min, subcostal and intercostal recessions, nasal flaring, oxygen saturation 90% on room air. Auscultation reveals fine inspiratory crackles and high-pitched expiratory wheezing throughout both lung fields. According to NICE guideline NG9, what is the core management?",
        "options": [
            "Humidified supplemental oxygen via nasal cannula and feeding support; bronchodilators and steroids are NOT recommended",
            "Inhaled Salbutamol via spacer 10 puffs every 2 hours",
            "Oral Dexamethasone 0.15 mg/kg once daily for 3 days",
            "Intravenous Amoxicillin-Clavulanate for 7 days",
            "Nebulised Hypertonic Saline and Ipratropium bromide"
        ],
        "correct_answer": "Humidified supplemental oxygen via nasal cannula and feeding support; bronchodilators and steroids are NOT recommended",
        "explanation": "The infant has acute bronchiolitis (most commonly RSV). NICE guideline NG9 clearly states that management is supportive: humidified supplemental oxygen to maintain SpO2 >=92% and nasogastric/IV fluid support if feeding <50% of normal volume. Bronchodilators (salbutamol), systemic corticosteroids, and antibiotics have no evidence of benefit and are explicitly not recommended."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 2-year-old boy is brought to the GP by his mother with a harsh 'seal-like' barking cough, hoarse cry, and inspiratory stridor that worsens when he is agitated. He is alert and pink, comfortable at rest with no chest wall indrawing. Temperature is 37.8°C. What is the single most appropriate initial pharmacological treatment?",
        "options": [
            "A single dose of oral Dexamethasone (0.15 mg/kg)",
            "Nebulised Salbutamol 2.5 mg",
            "Oral Amoxicillin 125 mg TDS for 5 days",
            "Steam inhalation therapy in a closed bathroom",
            "Reassurance and discharge with paracetamol only"
        ],
        "correct_answer": "A single dose of oral Dexamethasone (0.15 mg/kg)",
        "explanation": "The child has acute laryngotracheobronchitis (croup), usually caused by Parainfluenza virus. NICE guidelines state that all children with croup (even mild) should receive a single dose of oral dexamethasone (0.15 mg/kg) or oral prednisolone, which reduces the severity, duration, and need for hospital admission. Steam inhalation is ineffective and carries a scald risk."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "An 8-month-old boy presents with sudden, episodic screaming spasms during which he draws his legs up to his abdomen and appears pale. Between episodes, he is lethargic. On the second day, he passes a stool described as resembling 'red currant jelly' containing blood and mucus. A sausage-shaped mass is palpable in the right hypochondrium. What is the initial diagnostic imaging investigation of choice?",
        "options": [
            "Abdominal ultrasound",
            "Plain abdominal radiograph (AXR)",
            "Contrast CT abdomen",
            "Diagnostic laparoscopy",
            "Faecal occult blood test"
        ],
        "correct_answer": "Abdominal ultrasound",
        "explanation": "The presentation is classic for ileocolic intussusception (episodic colicky pain, leg drawing, red currant jelly stool, sausage-shaped mass, Dance's sign). Abdominal ultrasound is the non-invasive investigation of choice with >98% sensitivity, classically demonstrating a 'target' or 'doughnut' sign in transverse section. Therapeutic air/contrast enema reduction follows if there are no signs of peritonitis."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 4-week-old first-born male infant presents with non-bilious projectile vomiting immediately after feeds for 5 days. He remains ravenously hungry after vomiting. On examination, he is mildly dehydrated, and a small, firm, mobile olive-sized mass is palpable in the right upper quadrant during a test feed. Which metabolic and electrolyte derangement is classically present on blood gas?",
        "options": [
            "Hypochloraemic, hypokalaemic metabolic alkalosis",
            "Hyperchloraemic metabolic acidosis with high anion gap",
            "Normal anion gap metabolic acidosis",
            "Hypokalaemic respiratory alkalosis",
            "Hyperkalaemic metabolic acidosis"
        ],
        "correct_answer": "Hypochloraemic, hypokalaemic metabolic alkalosis",
        "explanation": "Hypertrophic pyloric stenosis causes recurrent vomiting of gastric hydrochloric acid (HCl), leading to loss of hydrogen and chloride ions. As the kidneys attempt to preserve hydrogen ions in exchange for potassium, hypokalaemia ensues, producing the classic hypochloraemic, hypokalaemic metabolic alkalosis. Fluid and electrolyte abnormalities must be fully corrected before Ramstedt's pyloromyotomy."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 3-year-old girl is admitted with a 6-day history of high spiking remittent fever unresponsive to antipyretics. On examination: bilateral non-purulent bulbar conjunctival injection, bright red cracked lips with a 'strawberry tongue', a polymorphous erythematous macular rash over the trunk, and tender unilateral cervical lymphadenopathy measuring 2.5 cm. What is the most critical complication that prompt treatment aims to prevent?",
        "options": [
            "Coronary artery aneurysms and thrombosis",
            "Acute glomerulonephritis",
            "Rheumatic valvular disease",
            "Bacterial endocarditis",
            "Permanent sensorineural deafness"
        ],
        "correct_answer": "Coronary artery aneurysms and thrombosis",
        "explanation": "This child meets the diagnostic criteria for Kawasaki disease (fever >=5 days plus at least 4 of 5 features: bilateral conjunctivitis, mucosal changes/strawberry tongue, polymorphous rash, peripheral extremity changes, and cervical lymphadenopathy). Untreated, up to 25% develop coronary artery aneurysms. Early treatment with high-dose intravenous immunoglobulin (IVIG 2 g/kg) and aspirin within the first 10 days significantly reduces this risk to <5%."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old boy presents with symmetrical non-blanching palpable purpuric lesions distributed over his buttocks, thighs, and posterior legs. He also reports crampy peri-umbilical abdominal pain and swollen, painful ankles. His platelet count is 280 x 10^9/L (normal). Urinalysis demonstrates microscopic haematuria and 2+ proteinuria. What is the underlying diagnosis and what regular monitoring is mandatory?",
        "options": [
            "Henoch-Schönlein Purpura (IgA vasculitis); regular blood pressure and urinalysis monitoring for 6-12 months",
            "Immune Thrombocytopenia (ITP); serial weekly platelet counts",
            "Meningococcal septicaemia; immediate lumbar puncture",
            "Post-streptococcal glomerulonephritis; daily renal biopsies",
            "Thrombotic thrombocytopenic purpura; urgent plasma exchange"
        ],
        "correct_answer": "Henoch-Schönlein Purpura (IgA vasculitis); regular blood pressure and urinalysis monitoring for 6-12 months",
        "explanation": "Henoch-Schönlein Purpura (HSP / IgA vasculitis) is a small-vessel leukocytoclastic vasculitis characterized by palpable purpura (with normal platelets), arthralgia, abdominal pain, and renal involvement (haematuria/proteinuria). While most cases are self-limiting, long-term renal impairment can develop; regular blood pressure and urinalysis screening must continue for at least 6-12 months."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "An 18-month-old girl has a generalized tonic-clonic seizure lasting 2 minutes during an acute viral febrile illness (temperature 39.1°C). She has had no prior seizures. On arrival 20 minutes later, she is afebrile after paracetamol, alert, making eye contact, and interacting happily with toys. Neurological examination is entirely normal. How should this seizure be categorized and managed?",
        "options": [
            "Simple febrile convulsion; provide parental reassurance and safety-netting advice without need for EEG or neuroimaging",
            "Complex febrile convulsion; arrange emergency CT head",
            "Epilepsy; commence daily Sodium Valproate",
            "Atypical absence seizure; start Ethosuximide",
            "Status epilepticus; administer intravenous Phenytoin"
        ],
        "correct_answer": "Simple febrile convulsion; provide parental reassurance and safety-netting advice without need for EEG or neuroimaging",
        "explanation": "A simple febrile convulsion is defined as a generalized seizure lasting <15 minutes that does not recur within 24 hours, occurring in a child aged 6 months to 5 years with a febrile illness, followed by complete recovery without focal neurological deficits. No routine investigations (EEG, neuroimaging) are required; parents should be reassured, educated on fever management, and given safety-netting instructions."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "During a routine 18-month child developmental surveillance assessment, the health visitor notes several observations. Which of the following developmental findings represents an absolute 'red flag' requiring urgent paediatric specialist referral?",
        "options": [
            "Inability to walk independently without support",
            "Inability to jump off the ground with both feet",
            "Speaking only 10 recognizable words",
            "Inability to draw a complete circle",
            "Inability to hold and use a small spoon cleanly"
        ],
        "correct_answer": "Inability to walk independently without support",
        "explanation": "In gross motor development, independent walking is expected between 12 and 15 months; failure to walk independently by 18 months is considered a major developmental red flag and warrants urgent referral to paediatrics to exclude underlying neuromotor disorders such as Duchenne muscular dystrophy or cerebral palsy. Jumping and drawing shapes develop much later."
    },
    # Paediatrics EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Paediatrics",
        "scenario": "Theme: Paediatric Exanthems. Match each clinical description with the causative infectious disease.\n\nVignette 1: A 6-year-old boy presents with bright fiery red erythema on both cheeks ('slapped cheek' appearance). Three days later, a fine, pink, lace-like reticular maculopapular rash appears on his arms and trunk. He has had mild coryza.",
        "options": [
            "Erythema Infectiosum (Fifth Disease / Parvovirus B19)",
            "Roseola Infantum (Exanthem Subitum / HHV-6)",
            "Measles (Rubeola)",
            "Scarlet Fever (Group A Streptococcus)",
            "Hand, Foot, and Mouth Disease (Coxsackievirus A16)",
            "Rubella (German Measles)",
            "Varicella (Chickenpox)",
            "Kawasaki Disease"
        ],
        "correct_answer": "Erythema Infectiosum (Fifth Disease / Parvovirus B19)",
        "explanation": "Erythema infectiosum (Fifth disease), caused by Parvovirus B19, classically manifests as bright erythematous cheeks followed by a reticular 'lace-like' rash on the trunk and extremities."
    },
    {
        "type": "emq",
        "category": "Paediatrics",
        "scenario": "Theme: Paediatric Exanthems. Match each clinical description with the causative infectious disease.\n\nVignette 2: An 11-month-old girl has 4 days of high fever (39.5°C) but appears relatively well. As the fever abruptly resolves on day 5, a generalized rose-pink maculopapular rash suddenly erupts on her trunk and spreads to her neck and limbs.",
        "options": [
            "Erythema Infectiosum (Fifth Disease / Parvovirus B19)",
            "Roseola Infantum (Exanthem Subitum / HHV-6)",
            "Measles (Rubeola)",
            "Scarlet Fever (Group A Streptococcus)",
            "Hand, Foot, and Mouth Disease (Coxsackievirus A16)",
            "Rubella (German Measles)",
            "Varicella (Chickenpox)",
            "Kawasaki Disease"
        ],
        "correct_answer": "Roseola Infantum (Exanthem Subitum / HHV-6)",
        "explanation": "Roseola infantum (Sixth disease), caused by human herpesvirus 6 (HHV-6), is characterized by high fever for 3-5 days that resolves abruptly (defervescence) just as a discrete maculopapular rash appears."
    },
    {
        "type": "emq",
        "category": "Paediatrics",
        "scenario": "Theme: Paediatric Exanthems. Match each clinical description with the causative infectious disease.\n\nVignette 3: An unimmunised 4-year-old boy presents with high fever, cough, coryza, and conjunctivitis (the '3 Cs'). Tiny white spots resembling grains of salt on a red base (Koplik spots) are seen on the buccal mucosa. A dark red blotchy maculopapular rash then starts behind the ears and spreads downwards.",
        "options": [
            "Erythema Infectiosum (Fifth Disease / Parvovirus B19)",
            "Roseola Infantum (Exanthem Subitum / HHV-6)",
            "Measles (Rubeola)",
            "Scarlet Fever (Group A Streptococcus)",
            "Hand, Foot, and Mouth Disease (Coxsackievirus A16)",
            "Rubella (German Measles)",
            "Varicella (Chickenpox)",
            "Kawasaki Disease"
        ],
        "correct_answer": "Measles (Rubeola)",
        "explanation": "Cough, coryza, conjunctivitis, pathognomonic Koplik spots on buccal mucosa, and a descending cephalocaudal maculopapular exanthem in an unvaccinated child confirm measles."
    },
    {
        "type": "emq",
        "category": "Paediatrics",
        "scenario": "Theme: Paediatric Exanthems. Match each clinical description with the causative infectious disease.\n\nVignette 4: A 5-year-old girl presents with sore throat, fever, and a widespread fine, punctate erythematous rash that feels rough like 'sandpaper'. She has flushed cheeks with circumoral pallor and a red strawberry tongue. Oral Phenoxymethylpenicillin is prescribed for 10 days.",
        "options": [
            "Erythema Infectiosum (Fifth Disease / Parvovirus B19)",
            "Roseola Infantum (Exanthem Subitum / HHV-6)",
            "Measles (Rubeola)",
            "Scarlet Fever (Group A Streptococcus)",
            "Hand, Foot, and Mouth Disease (Coxsackievirus A16)",
            "Rubella (German Measles)",
            "Varicella (Chickenpox)",
            "Kawasaki Disease"
        ],
        "correct_answer": "Scarlet Fever (Group A Streptococcus)",
        "explanation": "Scarlet fever, caused by erythrogenic exotoxin-producing Streptococcus pyogenes (Group A Strep), presents with sore throat, sandpaper-textured rash, strawberry tongue, and circumoral pallor."
    },
    {
        "type": "emq",
        "category": "Paediatrics",
        "scenario": "Theme: Paediatric Exanthems. Match each clinical description with the causative infectious disease.\n\nVignette 5: A 3-year-old toddler presents with painful shallow ulcers on his tongue and buccal mucosa, accompanied by small erythematous macules and oval vesicles on the palms of both hands and soles of both feet. He is drinking fluids comfortably.",
        "options": [
            "Erythema Infectiosum (Fifth Disease / Parvovirus B19)",
            "Roseola Infantum (Exanthem Subitum / HHV-6)",
            "Measles (Rubeola)",
            "Scarlet Fever (Group A Streptococcus)",
            "Hand, Foot, and Mouth Disease (Coxsackievirus A16)",
            "Rubella (German Measles)",
            "Varicella (Chickenpox)",
            "Kawasaki Disease"
        ],
        "correct_answer": "Hand, Foot, and Mouth Disease (Coxsackievirus A16)",
        "explanation": "Hand, foot, and mouth disease (caused by Coxsackievirus A16 or Enterovirus 71) presents with oral vesicles/ulcerations and typical papulovesicular lesions on the palms and soles. Management is supportive."
    },

    # =========================================================================
    # 8. PSYCHIATRY / NEUROLOGY (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 68-year-old man presents to the ED with sudden-onset right arm and leg weakness and expressive aphasia that started 90 minutes ago. Non-contrast CT brain scan excludes intracerebral haemorrhage. Blood pressure is 162/92 mmHg, blood glucose is 6.4 mmol/L, and INR is 1.0. What is the most appropriate next step in acute management according to NICE guidelines?",
        "options": [
            "Intravenous thrombolysis with Alteplase (or Tenecteplase) within 4.5 hours of symptom onset",
            "Immediate oral Aspirin 300 mg dispersible",
            "Intravenous Heparin infusion",
            "Urgent carotid endarterectomy within 24 hours",
            "Lower blood pressure to <120/80 mmHg with IV Labetalol"
        ],
        "correct_answer": "Intravenous thrombolysis with Alteplase (or Tenecteplase) within 4.5 hours of symptom onset",
        "explanation": "In acute ischaemic stroke presenting within 4.5 hours of symptom onset where intracranial haemorrhage has been ruled out by CT head, intravenous thrombolysis (Alteplase) is the first-line reperfusion therapy, provided there are no contraindications. In large vessel occlusions, mechanical thrombectomy within 6 hours should also be evaluated."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 48-year-old woman presents with sudden, excruciating occipital headache described as being 'hit on the back of the head with a cricket bat', reaching peak intensity within seconds. A non-contrast CT head performed 4 hours after symptom onset is reported as normal. What is the mandatory next investigation to exclude a subarachnoid haemorrhage?",
        "options": [
            "Lumbar puncture performed at least 12 hours after symptom onset to assess for CSF xanthochromia",
            "Lumbar puncture immediately in the ED",
            "MRI brain scan at 2 weeks",
            "Discharge home with reassurance and simple analgesia",
            "CT brain venogram"
        ],
        "correct_answer": "Lumbar puncture performed at least 12 hours after symptom onset to assess for CSF xanthochromia",
        "explanation": "In suspected subarachnoid haemorrhage (SAH) where an initial high-resolution non-contrast CT head is negative, a lumbar puncture must be performed at least 12 hours post-symptom onset. This 12-hour window allows sufficient lysis of red blood cells into bilirubin, which produces spectrophotometric xanthochromia in the CSF."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 28-year-old man with known epilepsy is brought to resuscitation actively convulsing with continuous generalized tonic-clonic activity for 8 minutes. High-flow oxygen is applied and IV access is secured. What is the recommended first-line emergency pharmacological intervention for status epilepticus?",
        "options": [
            "Intravenous Lorazepam 4 mg (or buccal Midazolam 10 mg)",
            "Intravenous Phenytoin infusion 20 mg/kg over 60 minutes",
            "Intravenous Propofol bolus and general anaesthesia",
            "Intramuscular Paraldehyde 10 mL",
            "Oral Levetiracetam 1000 mg"
        ],
        "correct_answer": "Intravenous Lorazepam 4 mg (or buccal Midazolam 10 mg)",
        "explanation": "Convulsive status epilepticus (continuous seizure activity >=5 minutes) requires immediate termination to prevent neurological damage. First-line treatment is intravenous Lorazepam (4 mg in adults) or buccal Midazolam (10 mg), repeated once after 10-15 minutes if seizures continue. If seizures persist past 25 minutes, second-line IV anticonvulsants (Levetiracetam, Sodium Valproate, or Phenytoin) are initiated."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 62-year-old man with Parkinson's disease is commenced on Ropinirole. Three months later, his wife reports that he has secretly depleted their life savings by gambling tens of thousands of pounds online and has developed impulsive hypersexual behaviour. Which pharmacological mechanism is responsible for this side effect?",
        "options": [
            "Dopamine agonist-induced impulse control disorder",
            "Levodopa wearing-off phenomenon",
            "Anticholinergic delirium",
            "MAO-B inhibitor hypertensive crisis",
            "COMT inhibitor hepatotoxicity"
        ],
        "correct_answer": "Dopamine agonist-induced impulse control disorder",
        "explanation": "Non-ergot dopamine receptor agonists (such as Ropinirole and Pramipexole) stimulate mesolimbic D3 receptors and are strongly associated with impulse control disorders (ICDs), including pathological gambling, compulsive shopping, binge eating, and hypersexuality. Patients and carers must be pre-warned, and the dose should be tapered under specialist guidance."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 36-year-old man with schizophrenia is commenced on Haloperidol. Five days later, he is found in a stuporous state with extreme 'lead-pipe' generalised muscle rigidity, temperature of 39.8°C, blood pressure of 184/110 mmHg, and heart rate of 128 bpm. Blood tests reveal a serum Creatine Kinase (CK) of 18,500 U/L (reference <200). What is the diagnosis and the most appropriate specific medical therapy?",
        "options": [
            "Neuroleptic Malignant Syndrome (NMS); discontinue antipsychotic and administer Bromocriptine or Dantrolene",
            "Serotonin syndrome; administer intravenous Flumazenil",
            "Malignant hyperthermia; administer high-dose Haloperidol",
            "Catatonia; treat with high-dose intravenous Phenytoin",
            "Acute dystonic reaction; administer oral Procyclidine"
        ],
        "correct_answer": "Neuroleptic Malignant Syndrome (NMS); discontinue antipsychotic and administer Bromocriptine or Dantrolene",
        "explanation": "The tetrad of severe muscle rigidity ('lead-pipe'), hyperthermia, autonomic dysregulation, and markedly elevated CK following antipsychotic therapy confirms Neuroleptic Malignant Syndrome (NMS). Management requires immediate cessation of the offending neuroleptic, aggressive IV hydration, ICU admission, and specific medical therapy with Dantrolene (muscle relaxant) or Bromocriptine (dopamine agonist)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 26-year-old woman taking Citalopram for depression is prescribed Tramadol for a severe ankle sprain. Twelve hours later, she is brought to the ED agitated and diaphoretic with ocular clonus, hyperreflexia, bilateral inducible ankle clonus, and coarse tremor. Her temperature is 38.3°C. Which syndrome has she developed?",
        "options": [
            "Serotonin Syndrome",
            "Neuroleptic Malignant Syndrome",
            "Anticholinergic toxidrome",
            "Tardive dyskinesia",
            "Lithium toxicity"
        ],
        "correct_answer": "Serotonin Syndrome",
        "explanation": "The Hunter Toxicity Criteria for Serotonin Syndrome include clonus (spontaneous, inducible, or ocular), agitation, diaphoresis, tremor, and hyperreflexia in the presence of serotonergic agents (Citalopram plus Tramadol, a weak serotonin reuptake inhibitor). Management includes stopping serotonergic drugs, supportive care, and Cyproheptadine (a 5-HT2A antagonist) in moderate-to-severe cases."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 52-year-old man with chronic severe alcohol dependence is brought to hospital by ambulance. On examination, he is acutely confused, exhibits horizontal nystagmus with bilateral lateral rectus palsy (sixth nerve palsy), and has marked cerebellar truncal ataxia. What is the immediate mandatory treatment to prevent irreversible Korsakoff psychosis?",
        "options": [
            "Intravenous high-dose Thiamine (Pabrinex) prior to administering any glucose infusions",
            "Intravenous 10% Dextrose infusion stat",
            "Oral Chlordiazepoxide 50 mg alone",
            "Intravenous Haloperidol 5 mg",
            "Intramuscular Vitamin B12 injection"
        ],
        "correct_answer": "Intravenous high-dose Thiamine (Pabrinex) prior to administering any glucose infusions",
        "explanation": "The classic triad of Wernicke's encephalopathy is acute confusion, ophthalmoplegia/nystagmus, and cerebellar ataxia, caused by thiamine (Vitamin B1) deficiency. Immediate intravenous Pabrinex (thiamine) must be given BEFORE any carbohydrate/glucose solutions, because glucose oxidation consumes remaining thiamine and precipitates acute irreversible hypothalamic and mamillary body necrosis (Korsakoff psychosis)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 45-year-old woman with bipolar affective disorder is maintained on Lithium carbonate. She develops gastroenteritis with dehydration and takes over-the-counter Ibuprofen for headache. She presents with coarse hand tremor, slurred speech, ataxia, and confusion. Her serum lithium level is 2.4 mmol/L (therapeutic range 0.4-1.0). What is the underlying cause of this toxicity?",
        "options": [
            "Dehydration and NSAID co-prescription reducing renal clearance of lithium",
            "Direct hepatic metabolism failure induced by ibuprofen",
            "Conversion of lithium to active toxic metabolites",
            "Synergistic CNS sedation from ibuprofen",
            "Decreased gastrointestinal absorption of lithium"
        ],
        "correct_answer": "Dehydration and NSAID co-prescription reducing renal clearance of lithium",
        "explanation": "Lithium is excreted almost entirely by the kidneys. Both volume depletion (dehydration) and NSAIDs (which inhibit renal prostaglandins, reducing renal blood flow and GFR) decrease renal clearance of lithium, leading to acute toxicity (coarse tremor, ataxia, confusion, seizures). ACE inhibitors and thiazide diuretics cause similar toxic drug interactions."
    },
    # Psych/Neuro EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Psychiatry / Neurology",
        "scenario": "Theme: Cranial Neuropathies and Primary Headaches. Match each scenario with the most likely diagnosis.\n\nVignette 1: A 32-year-old woman wakes up with unilateral facial weakness, inability to close her right eye, and inability to wrinkle her right forehead. Taste is impaired on the anterior two-thirds of her tongue. She has no limb weakness. Oral Prednisolone is started within 72 hours.",
        "options": [
            "Bell's Palsy (Idiopathic Facial Nerve Palsy)",
            "Trigeminal Neuralgia",
            "Cluster Headache",
            "Migraine with Aura",
            "Idiopathic Intracranial Hypertension (IIH)",
            "Tension-Type Headache",
            "Vestibular Schwannoma",
            "Multiple Sclerosis"
        ],
        "correct_answer": "Bell's Palsy (Idiopathic Facial Nerve Palsy)",
        "explanation": "Lower motor neuron facial nerve palsy involves both the upper and lower face (including the forehead, distinguishing it from an upper motor neuron stroke). Oral prednisolone within 72 hours significantly improves recovery."
    },
    {
        "type": "emq",
        "category": "Psychiatry / Neurology",
        "scenario": "Theme: Cranial Neuropathies and Primary Headaches. Match each scenario with the most likely diagnosis.\n\nVignette 2: A 58-year-old man experiences paroxysms of severe, sharp, electric shock-like shooting pain in his right cheek and jaw that last 15 seconds. The pain is triggered by light touch, shaving, brushing teeth, or a cold gust of wind. First-line therapy is Carbamazepine.",
        "options": [
            "Bell's Palsy (Idiopathic Facial Nerve Palsy)",
            "Trigeminal Neuralgia",
            "Cluster Headache",
            "Migraine with Aura",
            "Idiopathic Intracranial Hypertension (IIH)",
            "Tension-Type Headache",
            "Vestibular Schwannoma",
            "Multiple Sclerosis"
        ],
        "correct_answer": "Trigeminal Neuralgia",
        "explanation": "Unilateral, lancinating, electric shock-like pain in the distribution of CN V2/V3 triggered by innocuous sensory stimuli is classic trigeminal neuralgia; Carbamazepine is the first-line medication."
    },
    {
        "type": "emq",
        "category": "Psychiatry / Neurology",
        "scenario": "Theme: Cranial Neuropathies and Primary Headaches. Match each scenario with the most likely diagnosis.\n\nVignette 3: A 35-year-old male smoker experiences excruciating unilateral retro-orbital pain occurring at 2 AM every night for the past 3 weeks. During attacks, he is agitated and paces the floor. The pain is accompanied by ipsilateral eye redness, lacrimation, ptosis, and nasal rhinorrhoea. Treatment of choice is 100% high-flow oxygen and subcutaneous Sumatriptan.",
        "options": [
            "Bell's Palsy (Idiopathic Facial Nerve Palsy)",
            "Trigeminal Neuralgia",
            "Cluster Headache",
            "Migraine with Aura",
            "Idiopathic Intracranial Hypertension (IIH)",
            "Tension-Type Headache",
            "Vestibular Schwannoma",
            "Multiple Sclerosis"
        ],
        "correct_answer": "Cluster Headache",
        "explanation": "Severe unilateral periorbital pain occurring in nocturnal clusters with ipsilateral autonomic features (Horner-like ptosis, lacrimation, rhinorrhoea) and restlessness describes cluster headache. High-flow oxygen and SC triptans are first-line acute treatments."
    },
    {
        "type": "emq",
        "category": "Psychiatry / Neurology",
        "scenario": "Theme: Cranial Neuropathies and Primary Headaches. Match each scenario with the most likely diagnosis.\n\nVignette 4: A 27-year-old woman experiences episodic unilateral pulsating headaches lasting 12-24 hours, preceded by an expanding zigzag visual shimmering pattern (scintillating scotoma) lasting 30 minutes. She has severe photophobia and nausea.",
        "options": [
            "Bell's Palsy (Idiopathic Facial Nerve Palsy)",
            "Trigeminal Neuralgia",
            "Cluster Headache",
            "Migraine with Aura",
            "Idiopathic Intracranial Hypertension (IIH)",
            "Tension-Type Headache",
            "Vestibular Schwannoma",
            "Multiple Sclerosis"
        ],
        "correct_answer": "Migraine with Aura",
        "explanation": "Reversible visual aura (scintillating scotoma) followed by unilateral throbbing headache, photophobia, and nausea fulfills diagnostic criteria for migraine with aura."
    },
    {
        "type": "emq",
        "category": "Psychiatry / Neurology",
        "scenario": "Theme: Cranial Neuropathies and Primary Headaches. Match each scenario with the most likely diagnosis.\n\nVignette 5: A 29-year-old obese woman (BMI 36 kg/m2) presents with generalized headaches worse upon bending forward, pulsatile tinnitus, and transient visual obscurations. Fundoscopy demonstrates bilateral high-grade papilloedema. MRI brain is normal and lumbar puncture shows an elevated opening pressure of 34 cm H2O with normal CSF composition.",
        "options": [
            "Bell's Palsy (Idiopathic Facial Nerve Palsy)",
            "Trigeminal Neuralgia",
            "Cluster Headache",
            "Migraine with Aura",
            "Idiopathic Intracranial Hypertension (IIH)",
            "Tension-Type Headache",
            "Vestibular Schwannoma",
            "Multiple Sclerosis"
        ],
        "correct_answer": "Idiopathic Intracranial Hypertension (IIH)",
        "explanation": "Raised intracranial pressure (headache, pulsatile tinnitus, papilloedema, elevated LP opening pressure >25 cm H2O) with normal neuroimaging in an overweight young female confirms Idiopathic Intracranial Hypertension (IIH / pseudotumour cerebri). Weight loss and Acetazolamide are first-line."
    }
]
