# -*- coding: utf-8 -*-
"""
High-Yield Clinical Problem Solving Questions (MSRA / UKMLA / AKT Format)
48 concise, satisfying clinical questions (4 per domain across 12 clinical domains)
featuring iconic diagnostic signs and classic clinical reasoning pearls.
"""

CLINICAL_QUESTIONS = [
    # =========================================================================
    # 1. CARDIOVASCULAR (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 24-year-old man with episodic palpitations has a resting ECG showing a short PR interval (<120 ms) and a slurred upstroke of the QRS complex (delta wave). What is the underlying anatomical cause?",
        "options": [
            "Accessory pathway (Bundle of Kent)",
            "Right bundle branch block",
            "Sinoatrial node fibrosis",
            "Mitral valve prolapse",
            "Left ventricular apical aneurysm"
        ],
        "correct_answer": "Accessory pathway (Bundle of Kent)",
        "explanation": "A short PR interval paired with a delta wave is the unmistakable ECG signature of Wolff-Parkinson-White (WPW) syndrome. Pre-excitation of the ventricles occurs via an abnormal congenital accessory conduction tract—the Bundle of Kent—bypassing the normal AV nodal delay."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 68-year-old man presents with sudden palpitations. His ECG shows a regular narrow-complex tachycardia at exactly 150 bpm with a continuous 'sawtooth' baseline in leads II, III, and aVF. What is the rhythm?",
        "options": [
            "Atrial flutter with 2:1 AV block",
            "Atrial fibrillation",
            "Ventricular tachycardia",
            "Complete (third-degree) heart block",
            "Sinus tachycardia"
        ],
        "correct_answer": "Atrial flutter with 2:1 AV block",
        "explanation": "A 'sawtooth' baseline of flutter waves at ~300 bpm in the inferior leads with a regular ventricular rate of 150 bpm points straight to atrial flutter with 2:1 AV conduction. Always suspect atrial flutter whenever you see a regular narrow-complex tachycardia sitting right at 150 bpm."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 45-year-old woman presents with acute dyspnoea, BP 84/50 mmHg, distended neck veins, and muffled heart sounds. Her ECG shows sinus tachycardia with beat-to-beat alternating QRS amplitude (electrical alternans). What is the definitive immediate treatment?",
        "options": [
            "Urgent pericardiocentesis",
            "Intravenous furosemide",
            "Synchronised DC cardioversion",
            "Intravenous amiodarone",
            "High-dose oral ibuprofen"
        ],
        "correct_answer": "Urgent pericardiocentesis",
        "explanation": "Hypotension, raised JVP, and muffled heart sounds form Beck's triad, and electrical alternans occurs as the heart swings rhythmically inside a fluid-filled pericardial sac. Together they confirm acute cardiac tamponade, requiring urgent echo-guided pericardiocentesis."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 56-year-old man has a wide pulse pressure (164/52 mmHg), a collapsing 'water-hammer' pulse, visible nail-bed capillary pulsations (Quincke's sign), and an early diastolic murmur loudest at the left sternal edge when leaning forward. What is the diagnosis?",
        "options": [
            "Aortic regurgitation",
            "Aortic stenosis",
            "Mitral stenosis",
            "Mitral regurgitation",
            "Tricuspid regurgitation"
        ],
        "correct_answer": "Aortic regurgitation",
        "explanation": "Rapid diastolic run-off of blood back into the left ventricle creates a wide pulse pressure and classic hyperdynamic signs—collapsing pulse (Corrigan's), nail-bed pulsations (Quincke's), and head bobbing (de Musset's)—alongside an early diastolic decrescendo murmur."
    },

    # =========================================================================
    # 2. DERMATOLOGY / OPHTHALMOLOGY / ENT (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 71-year-old man with atrial fibrillation suffers sudden, painless, complete loss of vision in his right eye. Fundoscopy shows a pale, oedematous retina with a striking 'cherry-red spot' at the macula. What is the diagnosis?",
        "options": [
            "Central retinal artery occlusion",
            "Central retinal vein occlusion",
            "Retinal detachment",
            "Acute angle-closure glaucoma",
            "Anterior ischaemic optic neuropathy"
        ],
        "correct_answer": "Central retinal artery occlusion",
        "explanation": "Sudden painless monocular blindness with a pale ischaemic retina and a cherry-red spot at the macula confirms central retinal artery occlusion (CRAO). The macula stays red because the thin fovea reveals the intact underlying choroidal blood supply."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 58-year-old man presents with severe right ear pain, vertigo, complete right-sided facial droop (including the forehead), and clustered painful vesicles inside the right external auditory canal and pinna. What is the diagnosis?",
        "options": [
            "Ramsay Hunt syndrome",
            "Bell's palsy",
            "Malignant otitis externa",
            "Acute mastoiditis",
            "Vestibular neuritis"
        ],
        "correct_answer": "Ramsay Hunt syndrome",
        "explanation": "Lower motor neuron facial paralysis accompanied by painful vesicles in the ear canal or pinna is the classic presentation of Ramsay Hunt syndrome (herpes zoster oticus), caused by varicella-zoster virus reactivation in the geniculate ganglion. Early oral aciclovir and prednisolone improve recovery."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 54-year-old woman presents with progressive difficulty climbing stairs, a violaceous 'heliotrope' rash around her eyelids, and flat purple-red scaly papules over the backs of her knuckles (Gottron's papules). What is the diagnosis?",
        "options": [
            "Dermatomyositis",
            "Systemic lupus erythematosus",
            "Polymyositis",
            "Systemic sclerosis",
            "Psoriatic arthritis"
        ],
        "correct_answer": "Dermatomyositis",
        "explanation": "Proximal muscle weakness combined with a purple periorbital heliotrope rash and Gottron's papules over the MCP and PIP joints is the signature presentation of dermatomyositis. Crucially, newly diagnosed adults must be screened for an underlying occult malignancy."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A healthy 21-year-old woman develops a single 4 cm oval pink scaly plaque on her upper back ('herald patch'). Ten days later, smaller oval scaly plaques erupt across her trunk in a 'Christmas tree' distribution. What is the diagnosis?",
        "options": [
            "Pityriasis rosea",
            "Guttate psoriasis",
            "Tinea corporis",
            "Secondary syphilis",
            "Lichen planus"
        ],
        "correct_answer": "Pityriasis rosea",
        "explanation": "A solitary 'herald patch' with a fine collarette of scale followed 1–2 weeks later by a symmetrical 'Christmas tree' eruption along Langer's cleavage lines on the back confirms pityriasis rosea. It is benign and self-limiting, resolving within 6–8 weeks."
    },

    # =========================================================================
    # 3. ENDOCRINOLOGY / METABOLIC (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "Twenty-four hours after a total thyroidectomy, a 42-year-old woman develops perioral tingling and finger cramps. Inflating a blood pressure cuff above systolic pressure for 2 minutes provokes carpopedal spasm (Trousseau's sign). What is the immediate treatment?",
        "options": [
            "Intravenous 10% calcium gluconate",
            "Intravenous magnesium sulfate alone",
            "Oral cholecalciferol",
            "Intravenous hydrocortisone",
            "Intravenous potassium chloride"
        ],
        "correct_answer": "Intravenous 10% calcium gluconate",
        "explanation": "Trousseau's sign (carpopedal spasm induced by cuff inflation) is a highly specific bedside indicator of acute hypocalcaemia—here due to inadvertent parathyroid gland injury or removal during thyroidectomy. Symptomatic hypocalcaemia requires immediate IV 10% calcium gluconate with ECG monitoring."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 36-year-old man experiences episodic pounding headaches, drenching sweats, palpitations, and sudden blood pressure spikes to 210/115 mmHg that resolve within 30 minutes. What is the best first-line screening investigation?",
        "options": [
            "Plasma free metanephrines (or 24-hour urinary metanephrines)",
            "Plasma aldosterone-to-renin ratio",
            "Overnight dexamethasone suppression test",
            "Adrenal CT scan as the initial test",
            "Random serum cortisol"
        ],
        "correct_answer": "Plasma free metanephrines (or 24-hour urinary metanephrines)",
        "explanation": "The classic triad of episodic headache, diaphoresis, and palpitations with paroxysmal hypertension points straight to phaeochromocytoma. Biochemical confirmation with plasma free or 24-hour urinary metanephrines always precedes adrenal imaging, and alpha-blockade (phenoxybenzamine/doxazosin) must precede beta-blockade."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 48-year-old man notices his wedding ring no longer fits, his shoe size has risen by two sizes, and his jaw has become prominent. Examination reveals coarse facial features, spade-like hands, and bitemporal hemianopia. What is the initial screening blood test?",
        "options": [
            "Serum insulin-like growth factor 1 (IGF-1)",
            "Random serum growth hormone level",
            "Serum prolactin",
            "9 am serum cortisol",
            "Thyroid-stimulating hormone (TSH)"
        ],
        "correct_answer": "Serum insulin-like growth factor 1 (IGF-1)",
        "explanation": "Acral enlargement, prognathism, and bitemporal hemianopia (optic chiasm compression by a pituitary macroadenoma) confirm acromegaly. Because growth hormone is secreted in erratic pulses, serum IGF-1 is the best initial screen, followed by an oral glucose tolerance test (failure of GH suppression)."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 39-year-old woman presents with progressive central obesity, round 'moon' facies, proximal muscle weakness, easy bruising, and wide (>1 cm) purple abdominal striae. Which initial test screens for this condition?",
        "options": [
            "Overnight 1 mg dexamethasone suppression test",
            "Short Synacthen (ACTH stimulation) test",
            "Random afternoon serum cortisol",
            "Plasma aldosterone-to-renin ratio",
            "Serum IGF-1"
        ],
        "correct_answer": "Overnight 1 mg dexamethasone suppression test",
        "explanation": "Wide violaceous striae (>1 cm), proximal myopathy, and easy bruising distinguish true Cushing's syndrome from simple obesity. First-line screening uses an overnight 1 mg dexamethasone suppression test (failure to suppress morning cortisol), 24-hour urinary free cortisol, or late-night salivary cortisol."
    },

    # =========================================================================
    # 4. GASTROENTEROLOGY / CLINICAL NUTRITION (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 21-year-old man presents with unexplained cirrhosis, a coarse resting tremor, and mood changes. Slit-lamp examination reveals golden-brown rings around the corneal limbus (Kayser-Fleischer rings). What is the expected serum caeruloplasmin result?",
        "options": [
            "Low serum caeruloplasmin",
            "High serum caeruloplasmin",
            "Normal serum caeruloplasmin with low urinary copper",
            "Absent serum ferritin",
            "Elevated alpha-1 antitrypsin"
        ],
        "correct_answer": "Low serum caeruloplasmin",
        "explanation": "Kayser-Fleischer rings (copper deposition in Descemet's membrane) paired with liver disease and neuropsychiatric signs confirm Wilson's disease (autosomal recessive ATP7B mutation). Impaired biliary copper excretion leads to low serum caeruloplasmin and high 24-hour urinary copper."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 52-year-old man presents with newly diagnosed diabetes mellitus, cirrhosis, pain in his 2nd and 3rd MCP joints, and diffuse slate-grey 'bronze' skin hyperpigmentation. Which blood test pair is the initial screen?",
        "options": [
            "Transferrin saturation and serum ferritin",
            "Serum caeruloplasmin and urinary copper",
            "Anti-mitochondrial antibodies and ALP",
            "Alpha-fetoprotein and liver ultrasound",
            "Serum amylase and lipase"
        ],
        "correct_answer": "Transferrin saturation and serum ferritin",
        "explanation": "The classic 'bronze diabetes' triad of cirrhosis, diabetes, and slate-grey skin pigmentation—often accompanied by 2nd/3rd MCP arthropathy—indicates hereditary haemochromatosis (HFE C282Y mutation). First-line screening looks for raised transferrin saturation (>45%) and elevated serum ferritin."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 34-year-old woman has a 1-year history of progressive dysphagia to both solids and liquids from onset, with regurgitation of undigested food. Barium swallow reveals a dilated oesophagus tapering smoothly to a 'bird's beak' narrowing. What is the diagnosis?",
        "options": [
            "Achalasia",
            "Oesophageal squamous cell carcinoma",
            "Diffuse oesophageal spasm",
            "Peptic oesophageal stricture",
            "Pharyngeal pouch (Zenker's diverticulum)"
        ],
        "correct_answer": "Achalasia",
        "explanation": "Dysphagia to both solids and liquids right from the start plus a classic 'bird's beak' tapering on barium swallow points straight to achalasia—caused by degeneration of inhibitory ganglion cells in Auerbach's myenteric plexus, preventing lower oesophageal sphincter relaxation."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 78-year-old care-home resident presents with absolute constipation and massive tympanic abdominal distension. Plain abdominal X-ray shows a hugely dilated loop of large bowel arising from the pelvis in a 'coffee bean' shape. What is the initial management?",
        "options": [
            "Flexible sigmoidoscopy and decompression",
            "Oral osmotic laxatives and observation",
            "Immediate emergency total colectomy",
            "Nasogastric tube alone without endoscopy",
            "Urgent upper GI endoscopy"
        ],
        "correct_answer": "Flexible sigmoidoscopy and decompression",
        "explanation": "A giant 'coffee bean' loop of dilated colon pointing towards the right upper quadrant on abdominal X-ray confirms sigmoid volvulus. Provided there are no signs of ischaemia or perforation, first-line treatment is urgent decompression via flexible sigmoidoscopy and flatus tube insertion."
    },

    # =========================================================================
    # 5. INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 64-year-old man presents with fatigue, spontaneous bruising, gum hypertrophy, and pancytopenia. His peripheral blood film shows numerous myeloblasts containing needle-like pink cytoplasmic inclusions (Auer rods). What is the diagnosis?",
        "options": [
            "Acute myeloid leukaemia (AML)",
            "Acute lymphoblastic leukaemia (ALL)",
            "Chronic lymphocytic leukaemia (CLL)",
            "Chronic myeloid leukaemia (CML)",
            "Myelodysplastic syndrome"
        ],
        "correct_answer": "Acute myeloid leukaemia (AML)",
        "explanation": "Auer rods—needle-shaped aggregates of myeloperoxidase granules inside myeloblasts—are the unmistakable hallmark of acute myeloid leukaemia (AML), and are especially abundant in acute promyelocytic leukaemia (APML, t(15;17)). Gum infiltration is a classic additional clue in monocytic AML."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 24-year-old man presents with painless, rubbery cervical lymphadenopathy that aches noticeably after drinking alcohol, alongside drenching night sweats. Excision biopsy reveals large binucleated 'owl's eye' Reed-Sternberg cells. What is the diagnosis?",
        "options": [
            "Hodgkin lymphoma",
            "Burkitt lymphoma",
            "Infectious mononucleosis",
            "Diffuse large B-cell lymphoma",
            "Tuberculous lymphadenitis"
        ],
        "correct_answer": "Hodgkin lymphoma",
        "explanation": "Alcohol-induced lymph node pain in a young adult combined with binucleated 'owl's eye' Reed-Sternberg cells (CD15+, CD30+) on lymph node biopsy confirms Hodgkin lymphoma. It typically spreads predictably to contiguous lymph node groups and carries a high cure rate."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "An unvaccinated 5-year-old boy presents with high fever, cough, coryza, and red watery eyes. Examination of his buccal mucosa shows tiny white 'grains of salt' spots on an erythematous base (Koplik spots) just before a rash begins behind his ears. What is the diagnosis?",
        "options": [
            "Measles",
            "Rubella",
            "Scarlet fever",
            "Kawasaki disease",
            "Roseola infantum"
        ],
        "correct_answer": "Measles",
        "explanation": "The prodrome of the '3 Cs' (cough, coryza, conjunctivitis) followed by Koplik spots on the buccal mucosa opposite the molars confirms measles before the maculopapular rash even spreads from behind the ears downwards. Notify public health immediately."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 70-year-old woman presents with worsening back pain, fatigue, hypercalcaemia, renal impairment, and anaemia. Blood film shows stacks of red cells (rouleaux formation), and skull X-ray reveals 'punched-out' lytic lesions. What is the diagnosis?",
        "options": [
            "Multiple myeloma",
            "Primary hyperparathyroidism",
            "Paget's disease of bone",
            "Waldenström macroglobulinaemia",
            "Chronic lymphocytic leukaemia"
        ],
        "correct_answer": "Multiple myeloma",
        "explanation": "The CRAB tetrad (hyperCalcaemia, Renal impairment, Anaemia, Bone pain/lytic lesions) plus rouleaux on blood film and 'punched-out' lytic skull lesions confirms multiple myeloma—a clonal plasma cell malignancy diagnosed via serum protein electrophoresis and bone marrow biopsy."
    },

    # =========================================================================
    # 6. MUSCULOSKELETAL (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 38-year-old man with chronic inflammatory lower back pain has restricted lumbar flexion (positive Schober's test). Lumbar spine X-ray shows bridging syndesmophytes fusing the vertebrae into a 'bamboo spine'. Which HLA allele is strongly associated?",
        "options": [
            "HLA-B27",
            "HLA-DR4",
            "HLA-DQ2",
            "HLA-B51",
            "HLA-DR2"
        ],
        "correct_answer": "HLA-B27",
        "explanation": "A 'bamboo spine' from calcified syndesmophytes and sacroiliac fusion is the classic late radiographic feature of ankylosing spondylitis (axial spondyloarthritis). Over 90% of affected patients carry the HLA-B27 allele."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 74-year-old woman develops an acutely hot, swollen right knee. Knee X-ray shows linear calcification of the articular cartilage (chondrocalcinosis), and joint fluid microscopy reveals weakly positively birefringent rhomboid-shaped crystals. What is the diagnosis?",
        "options": [
            "Pseudogout (calcium pyrophosphate deposition)",
            "Acute gout",
            "Septic arthritis",
            "Reactive arthritis",
            "Rheumatoid arthritis"
        ],
        "correct_answer": "Pseudogout (calcium pyrophosphate deposition)",
        "explanation": "Chondrocalcinosis on X-ray and weakly positively birefringent rhomboid crystals under polarised light confirm pseudogout (CPPD), most commonly affecting the knee or wrist. By contrast, gout displays strongly negatively birefringent needle-shaped monosodium urate crystals."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 67-year-old woman has chronic hand pain worse after gardening, with 10 minutes of morning stiffness. Examination reveals hard bony nodules at the distal interphalangeal joints (Heberden's nodes) and proximal interphalangeal joints (Bouchard's nodes). What is the diagnosis?",
        "options": [
            "Osteoarthritis",
            "Rheumatoid arthritis",
            "Psoriatic arthritis",
            "Tophaceous gout",
            "Systemic sclerosis"
        ],
        "correct_answer": "Osteoarthritis",
        "explanation": "Brief morning stiffness (<30 minutes), pain aggravated by use, and bony osteophytic swellings at the DIP joints (Heberden's nodes) and PIP joints (Bouchard's nodes) point straight to osteoarthritis. Rheumatoid arthritis classically spares the DIP joints."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 15-year-old boy has 6 weeks of worsening night-time pain and swelling just above his right knee. Plain X-ray shows a destructive distal femoral lesion with periosteal elevation forming a 'Codman's triangle' and a 'sunburst' spiculated pattern. What is the diagnosis?",
        "options": [
            "Osteosarcoma",
            "Ewing's sarcoma",
            "Osteoid osteoma",
            "Giant cell tumour of bone",
            "Simple bone cyst"
        ],
        "correct_answer": "Osteosarcoma",
        "explanation": "Night-time metaphyseal bone pain around the knee in an adolescent combined with Codman's triangle and a 'sunburst' periosteal reaction on X-ray is the classic presentation of osteosarcoma (whereas Ewing's sarcoma typically shows diaphyseal 'onion-skinning')."
    },

    # =========================================================================
    # 7. PAEDIATRICS (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "An 8-month-old boy has episodes of inconsolable crying where he draws his knees up to his chest, a sausage-shaped RUQ mass, and passes 'redcurrant jelly' stool. Ultrasound shows a 'target' (doughnut) sign. What is the first-line treatment?",
        "options": [
            "Pneumatic (air) enema reduction",
            "Immediate laparotomy and bowel resection",
            "Oral polyethylene glycol laxatives",
            "Intravenous antibiotics and observation",
            "Rectal suction biopsy"
        ],
        "correct_answer": "Pneumatic (air) enema reduction",
        "explanation": "Paroxysmal colicky pain with drawing up of the legs, 'redcurrant jelly' stool, and a target sign on ultrasound confirm intussusception (telescoping of bowel, usually ileocolic). In a stable child without peritonitis, pneumatic (air) enema reduction is first-line."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 5-week-old boy has forceful, projectile non-bilious vomiting after every feed yet remains ravenously hungry. Examination reveals a palpable 'olive-shaped' mass in the right upper quadrant. What blood gas abnormality is classic?",
        "options": [
            "Hypochloraemic, hypokalaemic metabolic alkalosis",
            "Hyperchloraemic metabolic acidosis",
            "High-anion-gap lactic acidosis",
            "Respiratory alkalosis with hyperkalaemia",
            "Hypernatraemic metabolic acidosis"
        ],
        "correct_answer": "Hypochloraemic, hypokalaemic metabolic alkalosis",
        "explanation": "Projectile non-bilious vomiting in a hungry 2–8-week-old infant with an 'olive' mass confirms hypertrophic pyloric stenosis. Persistent loss of gastric hydrochloric acid (H+ and Cl-) plus renal potassium exchange produces the classic hypochloraemic, hypokalaemic metabolic alkalosis."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "An unvaccinated 3-year-old boy presents with high fever, muffled voice, drooling, inspiratory stridor, and sits leaning forward in the 'tripod position'. What is the single most important immediate action?",
        "options": [
            "Do not examine the throat; call senior anaesthetics and ENT to secure the airway",
            "Inspect the pharynx with a tongue depressor to exclude tonsillitis",
            "Send him immediately to radiology for a lateral neck X-ray",
            "Administer oral amoxicillin and observe in the waiting room",
            "Obtain intravenous access and take blood cultures immediately"
        ],
        "correct_answer": "Do not examine the throat; call senior anaesthetics and ENT to secure the airway",
        "explanation": "High fever, drooling, toxic appearance, muffled voice, and the tripod posture indicate acute epiglottitis (typically Haemophilus influenzae type b; 'thumbprint' sign on X-ray). Agitating the child with throat exams, cannulation, or X-rays can trigger fatal complete airway obstruction—secure the airway first."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old girl develops a bright red 'slapped cheek' rash sparing her mouth and nasal bridge, followed 2 days later by a lacy, reticular rash on her arms and thighs. What is the causative virus?",
        "options": [
            "Parvovirus B19",
            "Human herpesvirus 6 (HHV-6)",
            "Coxsackievirus A16",
            "Measles morbillivirus",
            "Epstein-Barr virus"
        ],
        "correct_answer": "Parvovirus B19",
        "explanation": "A fiery red 'slapped cheek' facial rash followed by a lacy reticular rash on the limbs confirms erythema infectiosum (fifth disease), caused by Parvovirus B19. Once the rash appears, the child is no longer infectious—though pregnant contacts and sickle cell patients require assessment."
    },

    # =========================================================================
    # 8. PHARMACOLOGY (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 22-year-old woman presents 5 hours after ingesting 18 g of paracetamol. Her 4-hour plasma paracetamol level plots above the treatment line, so IV N-acetylcysteine is started. How does N-acetylcysteine protect the liver?",
        "options": [
            "Replenishes hepatic glutathione stores to detoxify NAPQI",
            "Inhibits gastric paracetamol absorption in the duodenum",
            "Induces renal excretion of unchanged paracetamol",
            "Directly chelates paracetamol in the bloodstream",
            "Blocks hepatic glucuronidation enzymes"
        ],
        "correct_answer": "Replenishes hepatic glutathione stores to detoxify NAPQI",
        "explanation": "In paracetamol overdose, normal glucuronidation and sulfation pathways saturate, shunting metabolism via CYP450 to the toxic metabolite NAPQI. N-acetylcysteine provides cysteine to replenish hepatic glutathione stores, which conjugate and neutralise NAPQI before it causes centrilobular necrosis."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 45-year-old man becomes deeply sedated with respiratory depression (RR 6/min) after receiving intravenous midazolam for a colonoscopy. What is the specific pharmacological reversal agent?",
        "options": [
            "Intravenous flumazenil",
            "Intravenous naloxone",
            "Intravenous protamine sulfate",
            "Intravenous atropine",
            "Intravenous glucagon"
        ],
        "correct_answer": "Intravenous flumazenil",
        "explanation": "Flumazenil is a competitive antagonist at the GABAA benzodiazepine binding site and rapidly reverses iatrogenic benzodiazepine sedation. (Note: it is avoided in mixed overdoses or chronic benzodiazepine users because it can precipitate refractory seizures.)"
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 51-year-old farmer exposed to agricultural pesticide arrives with pinpoint pupils, profuse salivation, lacrimation, bronchorrhoea, bradycardia, and muscle fasciculations. What is the immediate first-line antidote?",
        "options": [
            "Intravenous atropine",
            "Intravenous naloxone",
            "Intravenous flumazenil",
            "Intravenous N-acetylcysteine",
            "Intravenous calcium gluconate"
        ],
        "correct_answer": "Intravenous atropine",
        "explanation": "Organophosphate pesticides irreversibly inhibit acetylcholinesterase, flooding muscarinic and nicotinic synapses (SLUDGE: salivation, lacrimation, urination, diarrhoea, GI cramps, emesis + miosis and bronchorrhoea). High-dose IV atropine competitively blocks muscarinic receptors to dry lethal airway secretions (followed by pralidoxime)."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 68-year-old man develops major bleeding shortly after starting an intravenous unfractionated heparin infusion, with an APTT ratio of 4.2. Which specific antidote immediately reverses unfractionated heparin?",
        "options": [
            "Intravenous protamine sulfate",
            "Intravenous phytomenadione (vitamin K1)",
            "Intravenous idarucizumab",
            "Intravenous tranexamic acid alone",
            "Intravenous 4-factor prothrombin complex concentrate"
        ],
        "correct_answer": "Intravenous protamine sulfate",
        "explanation": "Protamine sulfate is a strongly basic (positively charged) protein that binds directly to acidic (negatively charged) unfractionated heparin, forming a stable inactive complex that immediately neutralises its anticoagulant activity."
    },

    # =========================================================================
    # 9. PSYCHIATRY / NEUROLOGY (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 24-year-old cyclist struck on the temple briefly loses consciousness, recovers (lucid interval), then rapidly deteriorates with a fixed dilated ipsilateral pupil. CT head shows a biconvex 'lemon-shaped' hyperdensity that does not cross suture lines. Which vessel is torn?",
        "options": [
            "Middle meningeal artery",
            "Cortical bridging veins",
            "Anterior communicating artery",
            "Middle cerebral artery",
            "Superior sagittal sinus"
        ],
        "correct_answer": "Middle meningeal artery",
        "explanation": "A lucid interval followed by rapid neurological decline and a biconvex ('lemon-shaped') haematoma bounded by suture lines confirms an acute extradural (epidural) haematoma, classically caused by a pterion fracture tearing the middle meningeal artery."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 49-year-old woman develops a sudden 'thunderclap' headache peaking instantly, with neck stiffness. Non-contrast CT head at 14 hours is normal, so a lumbar puncture is performed, revealing yellow CSF supernatant (xanthochromia). What is the diagnosis?",
        "options": [
            "Subarachnoid haemorrhage",
            "Bacterial meningitis",
            "Idiopathic intracranial hypertension",
            "Cerebral venous sinus thrombosis",
            "Traumatic lumbar puncture tap"
        ],
        "correct_answer": "Subarachnoid haemorrhage",
        "explanation": "CT sensitivity for subarachnoid haemorrhage drops after 6–12 hours. Xanthochromia—yellow discoloration of spun CSF from bilirubin breakdown of red cells, tested >12 hours after headache onset—confirms a true subarachnoid haemorrhage rather than a traumatic tap."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 34-year-old woman has drooping eyelids and double vision that worsen by evening and improve with rest. Sustained upward gaze for 60 seconds provokes progressive ptosis. Which autoantibody is positive in ~85% of cases?",
        "options": [
            "Anti-acetylcholine receptor (AChR) antibodies",
            "Anti-voltage-gated calcium channel (VGCC) antibodies",
            "Anti-aquaporin-4 antibodies",
            "Anti-NMDA receptor antibodies",
            "Anti-Jo-1 antibodies"
        ],
        "correct_answer": "Anti-acetylcholine receptor (AChR) antibodies",
        "explanation": "Fatigable ocular and bulbar weakness that worsens with use and improves with rest is the signature of myasthenia gravis, caused in ~85% of cases by IgG autoantibodies blocking postsynaptic nicotinic acetylcholine receptors at the neuromuscular junction (and associated with thymoma)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 31-year-old man develops progressive symmetrical ascending leg weakness and absent ankle and knee reflexes 2 weeks after Campylobacter gastroenteritis. What is the classic lumbar puncture finding?",
        "options": [
            "Elevated CSF protein with a normal white cell count",
            "Markedly raised CSF neutrophils with low glucose",
            "Oligoclonal IgG bands absent from serum",
            "Xanthochromia with elevated red blood cells",
            "Low CSF protein with high lymphocytes"
        ],
        "correct_answer": "Elevated CSF protein with a normal white cell count",
        "explanation": "Ascending symmetrical weakness with areflexia following Campylobacter jejuni infection confirms Guillain-Barré syndrome (acute inflammatory demyelinating polyneuropathy). Lumbar puncture characteristically shows albuminocytologic dissociation: high CSF protein with a normal white cell count."
    },

    # =========================================================================
    # 10. RENAL / UROLOGY (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 5-year-old boy presents with marked periorbital and leg oedema and frothy urine. Investigations show 4+ proteinuria, serum albumin 18 g/L, and hyperlipidaemia, with normal BP and renal function. What is the commonest underlying cause?",
        "options": [
            "Minimal change disease",
            "Membranous nephropathy",
            "Focal segmental glomerulosclerosis",
            "Post-streptococcal glomerulonephritis",
            "Diabetic nephropathy"
        ],
        "correct_answer": "Minimal change disease",
        "explanation": "Heavy proteinuria, hypoalbuminaemia (<25 g/L), oedema, and hyperlipidaemia define nephrotic syndrome. In children, ~90% of cases are caused by minimal change disease (podocyte foot-process effacement on electron microscopy), which responds dramatically to oral prednisolone."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 44-year-old man with hypertension, haematuria, and bilaterally enlarged, ballotable flank masses has multiple bilateral renal cysts on ultrasound. Which life-threatening extrarenal complication is associated with this condition?",
        "options": [
            "Intracranial berry aneurysms (subarachnoid haemorrhage)",
            "Acute aortic dissection",
            "Pulmonary fibrosis",
            "Splenic artery rupture",
            "Primary sclerosing cholangitis"
        ],
        "correct_answer": "Intracranial berry aneurysms (subarachnoid haemorrhage)",
        "explanation": "Hypertension, haematuria, and bilaterally enlarged ballotable kidneys indicate autosomal dominant polycystic kidney disease (ADPKD, PKD1/PKD2 mutations). Important extrarenal associations include intracranial berry aneurysms (risking subarachnoid haemorrhage), hepatic cysts, and mitral valve prolapse."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 28-year-old male smoker presents with haemoptysis and rapidly progressive glomerulonephritis. Renal biopsy shows linear IgG deposits along the glomerular basement membrane. Which autoantibody causes this syndrome?",
        "options": [
            "Anti-glomerular basement membrane (anti-GBM) antibodies",
            "c-ANCA (anti-PR3) antibodies",
            "p-ANCA (anti-MPO) antibodies",
            "Anti-double-stranded DNA antibodies",
            "Anti-phospholipase A2 receptor antibodies"
        ],
        "correct_answer": "Anti-glomerular basement membrane (anti-GBM) antibodies",
        "explanation": "Pulmonary haemorrhage plus rapidly progressive glomerulonephritis with linear IgG immunofluorescence along the glomerular basement membrane confirms Goodpasture's syndrome, caused by anti-GBM antibodies targeting type IV collagen in alveolar and glomerular basement membranes."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 10-year-old boy develops smoky-brown urine, periorbital oedema, and hypertension 2 weeks after impetigo. Urine microscopy shows dysmorphic red blood cells and red blood cell casts. What does the presence of red cell casts confirm?",
        "options": [
            "Glomerular bleeding (glomerulonephritis)",
            "Urothelial bladder carcinoma",
            "Lower urinary tract infection",
            "Ureteric calculus",
            "Acute tubular necrosis"
        ],
        "correct_answer": "Glomerular bleeding (glomerulonephritis)",
        "explanation": "Red blood cell casts form when red cells leak through damaged glomeruli and become moulded inside renal tubules by Tamm-Horsfall protein. Together with dysmorphic RBCs, they confirm glomerular bleeding—here post-streptococcal glomerulonephritis."
    },

    # =========================================================================
    # 11. REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 26-year-old woman at 11 weeks gestation presents with severe hyperemesis, vaginal bleeding, a uterus larger than dates, and a beta-hCG of 180,000 IU/L. Pelvic ultrasound shows a classic 'snowstorm' appearance with no fetus. What is the diagnosis?",
        "options": [
            "Complete hydatidiform mole",
            "Incomplete miscarriage",
            "Tubal ectopic pregnancy",
            "Dichorionic twin pregnancy",
            "Uterine leiomyoma"
        ],
        "correct_answer": "Complete hydatidiform mole",
        "explanation": "A uterus larger than gestational dates, markedly elevated beta-hCG, severe hyperemesis, and a 'snowstorm' (vesicular) ultrasound pattern confirm a complete hydatidiform mole. Management is suction evacuation with mandatory serial hCG follow-up to detect gestational trophoblastic neoplasia."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 24-year-old woman presents with frothy, offensive yellow-green vaginal discharge and vulval irritation. Speculum examination reveals punctate cervical haemorrhages ('strawberry cervix'). What is the first-line treatment?",
        "options": [
            "Oral metronidazole",
            "Oral fluconazole",
            "Oral doxycycline",
            "Intramuscular ceftriaxone",
            "Topical clotrimazole pessary"
        ],
        "correct_answer": "Oral metronidazole",
        "explanation": "Frothy yellow-green discharge and a 'strawberry cervix' (colpitis macularis) point straight to Trichomonas vaginalis infection. First-line treatment is oral metronidazole (400 mg twice daily for 5–7 days or 2 g single dose), alongside partner notification and treatment."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 27-year-old woman reports thin grey-white vaginal discharge with an unpleasant fishy odour worse after intercourse (vaginal pH 5.6). Microscopy shows vaginal epithelial cells heavily coated with bacteria ('clue cells'). What is the diagnosis?",
        "options": [
            "Bacterial vaginosis",
            "Vulvovaginal candidiasis",
            "Chlamydia trachomatis",
            "Neisseria gonorrhoeae",
            "Atrophic vaginitis"
        ],
        "correct_answer": "Bacterial vaginosis",
        "explanation": "Thin grey-white discharge, vaginal pH >4.5, a fishy amine odour, and 'clue cells' on microscopy fulfil Amsel's criteria for bacterial vaginosis—caused by overgrowth of anaerobic bacteria (e.g. Gardnerella vaginalis) replacing normal lactobacilli."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 32-year-old woman at 36 weeks gestation has BP 168/112 mmHg, 3+ proteinuria, severe frontal headache, flashing lights, and brisk reflexes with 3 beats of clonus. Which IV drug is given to prevent eclamptic seizures?",
        "options": [
            "Intravenous magnesium sulfate",
            "Intravenous diazepam",
            "Intravenous phenytoin",
            "Intravenous labetalol alone",
            "Intravenous calcium gluconate"
        ],
        "correct_answer": "Intravenous magnesium sulfate",
        "explanation": "Severe hypertension, proteinuria, visual aura, headache, and clonus indicate severe pre-eclampsia with impending eclampsia. Intravenous magnesium sulfate (4 g loading dose followed by 1 g/hour infusion) is the first-line drug to prevent and treat eclamptic seizures."
    },

    # =========================================================================
    # 12. RESPIRATORY (4 Questions)
    # =========================================================================
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "After blunt chest trauma, a 29-year-old man becomes acutely hypoxic and hypotensive (BP 78/48 mmHg) with absent right breath sounds, right hyper-resonance, raised JVP, and tracheal deviation to the left. What is the immediate action?",
        "options": [
            "Immediate needle decompression before chest X-ray",
            "Urgent portable chest X-ray to confirm the diagnosis",
            "CT thorax with contrast",
            "High-flow oxygen and observe for 30 minutes",
            "Intravenous furosemide"
        ],
        "correct_answer": "Immediate needle decompression before chest X-ray",
        "explanation": "Hypoxia, obstructive shock, unilateral absent breath sounds with hyper-resonance, and contralateral tracheal deviation confirm a tension pneumothorax. This is a clinical diagnosis—never delay life-saving immediate needle decompression (followed by chest drain) for a chest X-ray."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "Ten days after knee replacement, a 56-year-old woman develops sudden pleuritic chest pain, tachycardia, and SpO2 89%. Her ECG shows sinus tachycardia with a deep S wave in lead I, and a Q wave with inverted T wave in lead III (S1Q3T3). What is the definitive diagnostic scan?",
        "options": [
            "CT pulmonary angiogram (CTPA)",
            "Serum D-dimer alone",
            "Transthoracic echocardiogram",
            "High-resolution CT chest",
            "Plain chest X-ray"
        ],
        "correct_answer": "CT pulmonary angiogram (CTPA)",
        "explanation": "Recent orthopaedic surgery, acute pleuritic chest pain, hypoxia, and the classic right-heart-strain S1Q3T3 pattern on ECG point to acute pulmonary embolism. In a high-probability (Wells >4) haemodynamically stable patient, go straight to CTPA rather than D-dimer."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 65-year-old heavy smoker presents with right shoulder and inner-arm pain, small hand muscle wasting, and right-sided ptosis, miosis, and facial anhidrosis (Horner's syndrome). Where is the underlying tumour located?",
        "options": [
            "Apex of the right lung (Pancoast tumour)",
            "Left main bronchus",
            "Posterior mediastinum",
            "Right lower lobe",
            "Anterior diaphragmatic pleura"
        ],
        "correct_answer": "Apex of the right lung (Pancoast tumour)",
        "explanation": "Horner's syndrome (ptosis, miosis, anhidrosis from sympathetic chain invasion) plus C8–T1 brachial plexus hand wasting and shoulder pain in a smoker is the classic presentation of an apical lung cancer—a Pancoast tumour."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 74-year-old man wakes gasping for air with pink frothy sputum and bilateral basal crackles. Chest X-ray shows cardiomegaly, upper lobe venous diversion, Kerley B lines, and bilateral perihilar 'bat's wing' shadowing. What is the diagnosis?",
        "options": [
            "Acute cardiogenic pulmonary oedema",
            "Community-acquired pneumonia",
            "Idiopathic pulmonary fibrosis",
            "Bilateral pulmonary emboli",
            "Mesothelioma"
        ],
        "correct_answer": "Acute cardiogenic pulmonary oedema",
        "explanation": "Pink frothy sputum with the classic ABCDE chest X-ray findings—Alveolar 'bat's wing' oedema, Kerley B lines (interstitial septal lines), Cardiomegaly, upper lobe Diversion, and pleural Effusions—confirms acute cardiogenic pulmonary oedema."
    }
]
