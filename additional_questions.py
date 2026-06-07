# Additional MSRA Questions matching the blueprint
# Contains 26 EMQ themes (130 questions) and 14 PD templates (70 questions)

NEW_EMQ_THEMES = [
    # --- CARDIOVASCULAR (2 themes) ---
    {
        "theme": "Management of Arrhythmias",
        "category": "Cardiovascular",
        "options": [
            "Bisoprolol",
            "Digoxin",
            "Amiodarone",
            "Flecainide",
            "Synchronized DC Cardioversion",
            "Adenosine",
            "Atropine",
            "Verapamil"
        ],
        "scenarios": [
            {
                "scenario": "A 68-year-old male is brought to the ED with severe palpitations and chest discomfort. He is hypotensive (BP 84/50 mmHg) and cold to touch. ECG shows atrial fibrillation with a rapid ventricular rate.",
                "correct": "Synchronized DC Cardioversion",
                "explanation": "In patients with acute, haemodynamically unstable arrhythmias (suggested here by hypotension and chest pain), immediate synchronized DC cardioversion is the treatment of choice to restore sinus rhythm."
            },
            {
                "scenario": "A 32-year-old female presents with a sudden onset of rapid, regular palpitations. Vitals: BP 118/76 mmHg, HR 168 bpm. An ECG confirms supraventricular tachycardia (SVT). Vagal maneuvers have been unsuccessful.",
                "correct": "Adenosine",
                "explanation": "For stable patients with SVT, vagal maneuvers are first-line. If these fail, intravenous adenosine is administered as a rapid bolus to transiently block the AV node and terminate the re-entrant pathway."
            },
            {
                "scenario": "An 84-year-old sedentary male is diagnosed with permanent atrial fibrillation during a routine clinic visit. He has a resting heart rate of 112 bpm but is completely asymptomatic. He has a history of mild asthma.",
                "correct": "Digoxin",
                "explanation": "In sedentary patients with non-paroxysmal atrial fibrillation who require rate control, digoxin is an appropriate first-line choice. Beta-blockers are avoided or used with caution in asthma."
            },
            {
                "scenario": "A 75-year-old female presents with a 2-hour history of severe dizziness. Vitals: BP 85/52 mmHg, HR 32 bpm. The ECG shows a complete (third-degree) heart block with a slow ventricular escape rhythm.",
                "correct": "Atropine",
                "explanation": "For symptomatic bradycardia, intravenous atropine (typically 500 micrograms) is the first-line drug therapy to improve heart rate and perfusion while preparing for potential pacing."
            },
            {
                "scenario": "A 45-year-old male with recurrent paroxysmal atrial fibrillation and no history of structural or ischaemic heart disease presents for a rhythm control management review. You decide to initiate a pill-in-the-pocket strategy.",
                "correct": "Flecainide",
                "explanation": "Flecainide (a Class Ic antiarrhythmic) can be used as a rhythm control agent or 'pill-in-the-pocket' for paroxysmal AF in patients who have NO structural or ischaemic heart disease."
            }
        ]
    },
    {
        "theme": "Investigation of Cardiovascular Symptoms",
        "category": "Cardiovascular",
        "options": [
            "12-lead ECG",
            "24-hour ECG monitor",
            "Echocardiogram",
            "Coronary Angiography",
            "CT Coronary Angiogram",
            "Exercise Tolerance Test",
            "Serum Troponin",
            "Cardiac MRI"
        ],
        "scenarios": [
            {
                "scenario": "A 54-year-old male presents to the ED with a 2-hour history of severe retrosternal chest pain radiating to his left shoulder. He is diaphoretic. What is the immediate first-line investigation?",
                "correct": "12-lead ECG",
                "explanation": "A 12-lead ECG should be performed within 10 minutes of arrival for all patients presenting with chest pain of suspected cardiac origin to screen for STEMI or other acute ischaemic changes."
            },
            {
                "scenario": "A 28-year-old female describes experiencing rapid palpitations daily, lasting for 1 to 2 minutes, which are resolved by rest. Her physical examination, bloods, and baseline ECG are entirely normal.",
                "correct": "24-hour ECG monitor",
                "explanation": "For patients reporting daily symptoms of suspected arrhythmia where the baseline ECG is normal, a 24-hour ambulatory ECG monitor is the preferred investigation to catch the episode."
            },
            {
                "scenario": "A 67-year-old male presents with exertional shortness of breath. On examination, he has a harsh ejection systolic murmur radiating to the carotid arteries. You suspect aortic stenosis.",
                "correct": "Echocardiogram",
                "explanation": "An transthoracic echocardiogram is the diagnostic investigation of choice to visualize valvular structures, measure valve gradients, and confirm suspected aortic stenosis."
            },
            {
                "scenario": "A 58-year-old male with a history of hypertension presents to his GP with a 3-week history of retrosternal chest tightness when walking up steep hills. You want to arrange the first-line diagnostic imaging for stable angina.",
                "correct": "CT Coronary Angiogram",
                "explanation": "According to current NICE guidelines, CT coronary angiography is recommended as the first-line diagnostic investigation for patients with suspected stable angina."
            },
            {
                "scenario": "A 62-year-old female is admitted with chest pain. Her ECG shows non-specific ST-segment flattening. You need to distinguish between unstable angina and a non-ST-elevation myocardial infarction (NSTEMI).",
                "correct": "Serum Troponin",
                "explanation": "Serum cardiac troponin measurements (preferably high-sensitivity assays) are essential to identify myocardial necrosis and differentiate NSTEMI (positive troponin) from unstable angina (negative troponin)."
            }
        ]
    },

    # --- RESPIRATORY (2 themes) ---
    {
        "theme": "Management of Respiratory Conditions",
        "category": "Respiratory",
        "options": [
            "Inhaled Salbutamol",
            "Inhaled Beclometasone",
            "Nebulized Ipratropium",
            "Intravenous Magnesium Sulfate",
            "Oral Prednisolone",
            "Intravenous Hydrocortisone",
            "Long-term Oxygen Therapy",
            "Non-invasive Ventilation"
        ],
        "scenarios": [
            {
                "scenario": "A 24-year-old female with known asthma presents to the GP with worsening nocturnal cough and wheeze. She is currently using a short-acting beta agonist three times a week. You decide to start a preventer inhaler.",
                "correct": "Inhaled Beclometasone",
                "explanation": "For patients with asthma whose symptoms are not controlled by a short-acting beta-2 agonist (SABA) alone, the first step is to add an inhaled corticosteroid (ICS) like beclometasone as maintenance therapy."
            },
            {
                "scenario": "A 68-year-old male with stable COPD has a chronic oxygen saturation of 87% on room air. Arterial blood gas on two separate occasions shows a pO2 of 7.1 kPa. He does not smoke and has no other co-morbidities.",
                "correct": "Long-term Oxygen Therapy",
                "explanation": "Long-term oxygen therapy (LTOT) is indicated in COPD patients with a stable pO2 < 7.3 kPa on room air, or 7.3-8.0 kPa if there is pulmonary hypertension, polycythemia, or peripheral edema."
            },
            {
                "scenario": "A 22-year-old male with a severe asthma exacerbation has received multiple back-to-back salbutamol and ipratropium nebulisers and IV steroids, but remains distressed with a peak flow of 30% predicted.",
                "correct": "Intravenous Magnesium Sulfate",
                "explanation": "In patients with acute severe or life-threatening asthma who show a poor response to initial bronchodilator therapy, a single dose of intravenous magnesium sulfate should be administered to induce bronchodilation."
            },
            {
                "scenario": "A 72-year-old female is admitted to the hospital with an acute exacerbation of COPD. She is dyspnoeic and has an arterial blood gas showing pH 7.28, pCO2 7.8 kPa, and pO2 7.9 kPa on controlled oxygen.",
                "correct": "Non-invasive Ventilation",
                "explanation": "In acute exacerbations of COPD, non-invasive ventilation (NIV), specifically BiPAP, is indicated for respiratory acidosis (pH 7.25-7.35) and hypercapnia that persists despite optimal medical therapy."
            },
            {
                "scenario": "A 19-year-old female presents to the emergency department with a moderate asthma attack. She is speaking in complete sentences and has a peak flow of 65% of her best. What systemic therapy is indicated?",
                "correct": "Oral Prednisolone",
                "explanation": "For all acute asthma exacerbations (moderate, severe, or life-threatening), systemic corticosteroids (typically oral prednisolone for 5 days) are indicated to reduce airway inflammation."
            }
        ]
    },
    {
        "theme": "Pleural Disease and Chest X-Ray Findings",
        "category": "Respiratory",
        "options": [
            "Pleural effusion",
            "Pneumothorax",
            "Tension pneumothorax",
            "Lobar pneumonia",
            "Pulmonary edema",
            "Lung malignancy",
            "Pulmonary fibrosis",
            "Bronchiectasis"
        ],
        "scenarios": [
            {
                "scenario": "A 65-year-old male smoker presents with progressive dyspnoea. Chest X-ray reveals a dense, uniform opacity at the left base with blunting of the costophrenic angle and a curved upper border (meniscus).",
                "correct": "Pleural effusion",
                "explanation": "A pleural effusion characteristically presents on a chest X-ray as a homogenous opacity at the lung base with blunting of the costophrenic angle and a classic meniscus sign."
            },
            {
                "scenario": "A 22-year-old tall, thin male presents with sudden-onset left-sided pleuritic chest pain and breathlessness. Chest X-ray shows a visible thin white pleural line on the left, with an absence of lung markings peripheral to it.",
                "correct": "Pneumothorax",
                "explanation": "A simple pneumothorax is identified on chest X-ray by a thin, sharp pleural line representing the collapsed lung boundary, with a complete absence of bronchovascular markings peripheral to it."
            },
            {
                "scenario": "A 74-year-old female presents with acute severe dyspnoea and orthopnoea. Chest X-ray shows cardiomegaly, bilateral alveolar bats-wing shadowing, upper lobe blood diversion, and Kerley B lines.",
                "correct": "Pulmonary edema",
                "explanation": "Pulmonary edema secondary to congestive heart failure shows characteristic chest X-ray findings: cardiomegaly, bats-wing alveolar infiltrates, Kerley B lines (interstitial edema), and pleural effusions."
            },
            {
                "scenario": "A 34-year-old male presents with a high fever, productive cough with rusty sputum, and pleuritic chest pain. Chest X-ray shows homogeneous consolidation of the right middle lobe with air bronchograms.",
                "correct": "Lobar pneumonia",
                "explanation": "Lobar pneumonia presents radiologically as a well-defined area of homogeneous consolidation matching a lobe, often accompanied by air bronchograms (patent airways surrounded by fluid-filled alveoli)."
            },
            {
                "scenario": "A 45-year-old male is brought to the ED in respiratory distress following a motor vehicle collision. Vitals: BP 80/40 mmHg, HR 135 bpm. Trachea is deviated to the right, and breath sounds are absent on the left.",
                "correct": "Tension pneumothorax",
                "explanation": "A tension pneumothorax is a clinical emergency characterized by respiratory distress, hypotension, tachycardia, tracheal deviation away from the affected side, and absent breath sounds on the affected side."
            }
        ]
    },

    # --- ENDOCRINOLOGY / METABOLIC (2 themes) ---
    {
        "theme": "Management of Diabetes Mellitus",
        "category": "Endocrinology / Metabolic",
        "options": [
            "Metformin",
            "Gliclazide",
            "Pioglitazone",
            "Sitagliptin",
            "Empagliflozin",
            "Subcutaneous basal-bolus insulin",
            "Fixed-rate intravenous insulin infusion",
            "Oral glucose"
        ],
        "scenarios": [
            {
                "scenario": "A 54-year-old male is newly diagnosed with Type 2 Diabetes. His HbA1c is 58 mmol/mol despite 6 months of lifestyle modifications. He has no other medical conditions and normal renal function.",
                "correct": "Metformin",
                "explanation": "Metformin is the first-line pharmacological treatment for Type 2 Diabetes, unless contraindicated (e.g. renal impairment with eGFR < 30 ml/min)."
            },
            {
                "scenario": "A 62-year-old female with Type 2 Diabetes and established ischaemic heart disease has an HbA1c of 64 mmol/mol on Metformin monotherapy. You want to select a second-line agent that offers cardiovascular benefit.",
                "correct": "Empagliflozin",
                "explanation": "For patients with Type 2 Diabetes and established cardiovascular disease, an SGLT2 inhibitor (like empagliflozin or dapagliflozin) should be added to metformin first-line due to proven cardioprotective benefits."
            },
            {
                "scenario": "A 21-year-old female with Type 1 Diabetes is admitted with a 2-day history of vomiting and confusion. Lab findings: glucose 22 mmol/L, blood ketones 4.8 mmol/L, venous pH 7.12. Intravenous saline fluids are running.",
                "correct": "Fixed-rate intravenous insulin infusion",
                "explanation": "In the management of Diabetic Ketoacidosis (DKA), once intravenous fluid resuscitation is initiated, a fixed-rate intravenous soluble insulin infusion (0.1 units/kg/hour) must be commenced immediately."
            },
            {
                "scenario": "A 68-year-old male with Type 2 Diabetes is brought to the clinic feeling sweaty, shaky, and confused. A capillary blood glucose measurement is 2.8 mmol/L. He is conscious and able to swallow safely.",
                "correct": "Oral glucose",
                "explanation": "For conscious patients experiencing a mild-to-moderate hypoglycaemic episode (glucose < 4.0 mmol/L) who are able to swallow, the treatment of choice is 15-20g of fast-acting oral glucose (e.g. fruit juice, jelly babies)."
            },
            {
                "scenario": "A 15-year-old boy is newly diagnosed with Type 1 Diabetes Mellitus after presenting with polyuria, polydipsia, and weight loss. What is the standard long-term maintenance insulin regimen?",
                "correct": "Subcutaneous basal-bolus insulin",
                "explanation": "Type 1 Diabetes Mellitus is caused by autoimmune destruction of beta cells. The standard long-term insulin replacement regimen is a multiple daily injection (basal-bolus) subcutaneous insulin regimen."
            }
        ]
    },
    {
        "theme": "Diagnosis of Endocrine Disorders",
        "category": "Endocrinology / Metabolic",
        "options": [
            "Addison's disease",
            "Cushing's syndrome",
            "Conn's syndrome",
            "Phaeochromocytoma",
            "Acromegaly",
            "Diabetes insipidus",
            "Primary hyperparathyroidism",
            "Prolactinoma"
        ],
        "scenarios": [
            {
                "scenario": "A 34-year-old female presents with hypertension and muscle weakness. Blood tests reveal persistent hypokalaemia and elevated aldosterone levels. Plasma renin activity is suppressed.",
                "correct": "Conn's syndrome",
                "explanation": "Conn's syndrome (primary hyperaldosteronism) is characterized by hypertension, hypokalaemia, muscle weakness, elevated aldosterone, and suppressed renin activity."
            },
            {
                "scenario": "A 42-year-old male presents with weight gain, central obesity, abdominal purple striae, and proximal muscle weakness. A 24-hour urinary free cortisol is elevated, and low-dose dexamethasone fails to suppress cortisol.",
                "correct": "Cushing's syndrome",
                "explanation": "Cushing's syndrome is caused by chronic glucocorticoid excess, presenting with central obesity, purple striae, hypertension, proximal muscle wasting, and failure to suppress cortisol on dexamethasone suppression testing."
            },
            {
                "scenario": "A 28-year-old female presents with amenorrhoea and galactorrhoea. Pregnancy test is negative. Blood tests show significantly elevated prolactin levels, and MRI reveals a 6mm pituitary mass.",
                "correct": "Prolactinoma",
                "explanation": "A prolactinoma is a prolactin-secreting pituitary microadenoma or macroadenoma, presenting in women with amenorrhoea, galactorrhoea, and infertility."
            },
            {
                "scenario": "A 48-year-old male presents with sweating, headaches, and episodes of palpitations and severe anxiety. His blood pressure during these episodes is found to be 210/120 mmHg. 24-hour urinary metanephrines are elevated.",
                "correct": "Phaeochromocytoma",
                "explanation": "A phaeochromocytoma is a catecholamine-producing tumor of the adrenal medulla, presenting with the classic triad of episodic headaches, sweating, and palpitations, alongside severe hypertension."
            },
            {
                "scenario": "A 52-year-old female is investigated for osteoporosis. Routine bloods show: calcium 2.78 mmol/L (elevated), phosphate 0.72 mmol/L (low), and an inappropriately elevated parathyroid hormone (PTH) level.",
                "correct": "Primary hyperparathyroidism",
                "explanation": "Primary hyperparathyroidism presents with hypercalcaemia, hypophosphataemia, and inappropriately elevated PTH levels, often presenting as bone pain, kidney stones, or osteoporosis."
            }
        ]
    },

    # --- GASTROENTEROLOGY / CLINICAL NUTRITION (2 themes) ---
    {
        "theme": "Management of Gastrointestinal Emergencies",
        "category": "Gastroenterology / Clinical Nutrition",
        "options": [
            "Intravenous terlipressin and urgent endoscopy",
            "Urgent surgical laparotomy",
            "Intravenous proton pump inhibitor",
            "Intravenous fluids and bowel rest",
            "Oral mesalazine",
            "Intravenous corticosteroids",
            "ERCP",
            "Gluten-free diet"
        ],
        "scenarios": [
            {
                "scenario": "A 54-year-old male with a history of liver cirrhosis is admitted hematemesis and melaena. Vitals: BP 88/44 mmHg, HR 122 bpm. What is the immediate first-line management alongside fluid resuscitation?",
                "correct": "Intravenous terlipressin and urgent endoscopy",
                "explanation": "For suspected variceal haemorrhage (common in cirrhosis), management includes fluid resuscitation, intravenous terlipressin (vasoconstrictor), prophylactic antibiotics, and urgent therapeutic endoscopy."
            },
            {
                "scenario": "A 32-year-old female with ulcerative colitis is admitted with a severe flare (8 bloody stools/day, fever 38.4°C, HR 105 bpm). Abdominal X-ray shows a colonic diameter of 5.5cm. What is the first-line medical therapy?",
                "correct": "Intravenous corticosteroids",
                "explanation": "Acute severe ulcerative colitis (Truelove and Witts criteria met) requires admission for intravenous corticosteroids (e.g. methylprednisolone or hydrocortisone) and close monitoring for toxic megacolon."
            },
            {
                "scenario": "A 68-year-old female presents with severe right upper quadrant pain, high fever with chills, and jaundice. Ultrasound shows a dilated common bile duct with stones. What is the definitive management?",
                "correct": "ERCP",
                "explanation": "Ascending cholangitis (Charcot's triad: RUQ pain, fever, jaundice) is a medical emergency requiring intravenous antibiotics and urgent biliary decompression, typically via ERCP."
            },
            {
                "scenario": "A 45-year-old male presents with sudden-onset, severe abdominal pain. On exam, he has a rigid abdomen with guarding and rebound tenderness. Erect chest X-ray shows pneumoperitoneum. What is the immediate management?",
                "correct": "Urgent surgical laparotomy",
                "explanation": "Pneumoperitoneum (free air under the diaphragm) indicates a perforated hollow viscus, which is a surgical emergency requiring immediate laparotomy or laparoscopic repair."
            },
            {
                "scenario": "A 58-year-old male is admitted with a 12-hour history of severe epigastric pain radiating to his back, accompanied by persistent vomiting. Amylase is 1200 U/L. What is the cornerstone of initial management?",
                "correct": "Intravenous fluids and bowel rest",
                "explanation": "Acute pancreatitis is diagnosed by clinical features and amylase/lipase > 3x the upper limit of normal. Cornerstones of initial management are aggressive intravenous fluid resuscitation, analgesia, and bowel rest."
            }
        ]
    },
    {
        "theme": "Interpretation of Liver Function Tests",
        "category": "Gastroenterology / Clinical Nutrition",
        "options": [
            "Paracetamol hepatotoxicity",
            "Gilbert's syndrome",
            "Alcoholic hepatitis",
            "Primary biliary cholangitis",
            "Acute cholecystitis",
            "Choledocholithiasis",
            "Non-alcoholic fatty liver disease",
            "Hepatic encephalopathy"
        ],
        "scenarios": [
            {
                "scenario": "A 22-year-old male has routine bloods showing isolated bilirubin elevation of 48 umol/L. ALT, ALP, albumin, and blood film are normal. He noticed mild yellowing of his eyes during a recent flu-like illness.",
                "correct": "Gilbert's syndrome",
                "explanation": "Gilbert's syndrome is a benign autosomal recessive condition characterized by isolated unconjugated hyperbilirubinaemia, typically triggered by stress, fasting, infection, or dehydration."
            },
            {
                "scenario": "A 45-year-old female presents with generalized pruritus and fatigue. LFTs show a cholestatic pattern: ALP 480 U/L (elevated), ALT 45 U/L (normal). Autoantibody screening is positive for anti-mitochondrial antibodies (AMA).",
                "correct": "Primary biliary cholangitis",
                "explanation": "Primary biliary cholangitis (PBC) is an autoimmune destruction of intrahepatic bile ducts, characteristically presenting in middle-aged women with pruritus, fatigue, cholestatic LFTs, and positive AMA."
            },
            {
                "scenario": "A 52-year-old heavy drinker presents with jaundice, fever, and tender hepatomegaly. LFTs show: bilirubin 140 umol/L, AST 240 U/L, ALT 110 U/L (AST to ALT ratio > 2:1).",
                "correct": "Alcoholic hepatitis",
                "explanation": "Alcoholic hepatitis presents with jaundice, hepatomegaly, and a classic AST:ALT ratio of 2:1 or greater in the context of heavy chronic alcohol consumption."
            },
            {
                "scenario": "A 68-year-old female presents with colicky right upper quadrant pain. LFTs reveal elevated ALP and bilirubin. Ultrasound shows gallstones and a dilated common bile duct, but no gallbladder wall thickening.",
                "correct": "Choledocholithiasis",
                "explanation": "Choledocholithiasis (gallstones in the common bile duct) presents with biliary colic and biliary obstruction (elevated bilirubin/ALP, dilated CBD on scan) without inflammatory signs of cholecystitis."
            },
            {
                "scenario": "A 48-year-old obese male with type 2 diabetes has persistently elevated ALT (68 U/L) and AST (52 U/L) on routine bloods. He does not drink alcohol. Ultrasound shows diffuse increased echogenicity of the liver parenchyma.",
                "correct": "Non-alcoholic fatty liver disease",
                "explanation": "Non-alcoholic fatty liver disease (NAFLD) is associated with obesity, diabetes, and metabolic syndrome. LFTs show mild transaminase elevation (ALT > AST), and ultrasound shows a hyperechoic ('bright') liver."
            }
        ]
    },

    # --- INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS (2 themes) ---
    {
        "theme": "Management of Systemic Infections",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "options": [
            "Intramuscular Benzylpenicillin",
            "Intravenous Ceftriaxone",
            "Intravenous Piperacillin-Tazobactam",
            "Oral Amoxicillin",
            "Intravenous Acyclovir",
            "Oral Fluconazole",
            "Oral Clarithromycin",
            "Intravenous Vancomycin"
        ],
        "scenarios": [
            {
                "scenario": "A 4-year-old child is brought to the GP surgery with a high fever, lethargy, photophobia, and a non-blanching petechial rash on their trunk. You suspect meningococcal septicaemia. What is the immediate primary care action?",
                "correct": "Intramuscular Benzylpenicillin",
                "explanation": "In primary care, if meningococcal septicaemia is suspected, the patient should receive a single dose of IM benzylpenicillin immediately and be transferred urgently to the hospital."
            },
            {
                "scenario": "A 72-year-old male undergoing chemotherapy for lymphoma is admitted with a temperature of 38.9°C and chills. Neutrophil count is 0.3 x 10^9/L. Vitals: BP 95/55 mmHg, HR 105 bpm. What is the first-line treatment?",
                "correct": "Intravenous Piperacillin-Tazobactam",
                "explanation": "Neutropenic sepsis is a medical emergency. Broad-spectrum antipseudomonal beta-lactam monotherapy (typically IV piperacillin-tazobactam/Tazocin) must be administered within 1 hour of arrival."
            },
            {
                "scenario": "A 28-year-old female presents with severe headache, fever, confusion, and expressive dysphasia. Lumbar puncture shows CSF lymphocytosis, normal glucose, and slightly elevated protein. PCR for HSV-1 is pending.",
                "correct": "Intravenous Acyclovir",
                "explanation": "For suspected viral encephalitis (suggested by fever, headache, focal neurological deficit, and confusion), empiric intravenous acyclovir must be started immediately to cover HSV."
            },
            {
                "scenario": "A 61-year-old male is admitted with severe community-acquired pneumonia (CURB-65 score of 3). What is the standard empiric intravenous antibiotic regimen according to NICE guidelines?",
                "correct": "Intravenous Ceftriaxone",
                "explanation": "Severe community-acquired pneumonia (CURB-65 score >= 3) is treated first-line with a broad-spectrum cephalosporin (like IV ceftriaxone) co-prescribed with a macrolide (like oral/IV clarithromycin)."
            },
            {
                "scenario": "A 32-year-old male with a history of intravenous drug use is admitted with fever and a new diastolic murmur. Blood cultures are positive for MRSA. Echocardiogram confirms tricuspid valve endocarditis.",
                "correct": "Intravenous Vancomycin",
                "explanation": "MRSA infective endocarditis is treated with glycopeptides like intravenous vancomycin, titrated based on trough levels to ensure therapeutic dosing."
            }
        ]
    },
    {
        "theme": "Diagnosis of Hematological Malignancies",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "options": [
            "Acute Lymphoblastic Leukaemia",
            "Acute Myeloid Leukaemia",
            "Chronic Lymphocytic Leukaemia",
            "Chronic Myeloid Leukaemia",
            "Multiple Myeloma",
            "Hodgkin's Lymphoma",
            "Non-Hodgkin's Lymphoma",
            "Polycythaemia Vera"
        ],
        "scenarios": [
            {
                "scenario": "A 68-year-old male presents with lower back pain and fatigue. Bloods show: Hb 9.2 g/dL, calcium 2.82 mmol/L (elevated), creatinine 168 umol/L. Serum protein electrophoresis reveals an IgG monoclonal band (paraprotein).",
                "correct": "Multiple Myeloma",
                "explanation": "Multiple myeloma presents with CRAB features: Calcium elevation, Renal impairment, Anaemia, and Bone lesions/pain, characterized by a monoclonal protein band on electrophoresis."
            },
            {
                "scenario": "A 4-year-old child presents with bruising, pallor, bone pain, and hepatosplenomegaly. Full blood count shows: Hb 7.8 g/dL, platelets 32 x 10^9/L, white blood cells 48 x 10^9/L with 85% lymphoblasts on blood film.",
                "correct": "Acute Lymphoblastic Leukaemia",
                "explanation": "ALL is the most common childhood cancer, presenting with bone marrow failure (bruising, anemia, infections), bone pain, organomegaly, and lymphoblasts on blood film."
            },
            {
                "scenario": "A 72-year-old asymptomatic male has routine bloods showing isolated white cell count of 35 x 10^9/L, with 88% mature lymphocytes. The blood film shows numerous smudge/smear cells.",
                "correct": "Chronic Lymphocytic Leukaemia",
                "explanation": "CLL is characterized by mature lymphocytosis on FBC in older adults, with smudge cells (fragile neoplastic lymphocytes broken during slide preparation) seen on blood film."
            },
            {
                "scenario": "A 52-year-old male presents with lethargy and left upper quadrant fullness. On examination, he has massive splenomegaly. FBC shows leucocytosis (WBC 110 x 10^9/L) with the presence of the Philadelphia chromosome t(9;22).",
                "correct": "Chronic Myeloid Leukaemia",
                "explanation": "CML is a myeloproliferative disorder presenting with marked leucocytosis, splenomegaly, and the diagnostic t(9;22) translocation creating the BCR-ABL fusion gene (Philadelphia chromosome)."
            },
            {
                "scenario": "A 24-year-old female presents with a painless, rubbery left supraclavicular lymph node. She notes fever, night sweats, and weight loss over the past 3 months. Excision biopsy shows Reed-Sternberg cells.",
                "correct": "Hodgkin's Lymphoma",
                "explanation": "Hodgkin's Lymphoma classically presents in young adults with painless lymphadenopathy, 'B symptoms' (fever, night sweats, weight loss), and diagnostic Reed-Sternberg cells on biopsy."
            }
        ]
    },

    # --- MUSCULOSKELETAL (2 themes) ---
    {
        "theme": "Management of Rheumatological Conditions",
        "category": "Musculoskeletal",
        "options": [
            "Oral Methotrexate",
            "Oral Sulfasalazine",
            "Oral Ibuprofen",
            "Oral Colchicine",
            "Oral Allopurinol",
            "Oral Prednisolone",
            "Infliximab",
            "Intramuscular Methylprednisolone"
        ],
        "scenarios": [
            {
                "scenario": "A 54-year-old male presents with a first attack of acute, red, swollen right first MTP joint. He has a history of asthma. Renal function is normal. What is the most appropriate first-line treatment?",
                "correct": "Oral Colchicine",
                "explanation": "First-line therapies for acute gout are NSAIDs or colchicine. In patients with asthma, NSAIDs (like Ibuprofen) should be avoided or used with caution to prevent bronchospasm, making colchicine the preferred option."
            },
            {
                "scenario": "A 68-year-old female is diagnosed with Polymyalgia Rheumatica (PMR) based on bilateral shoulder and pelvic girdle stiffness and ESR 74 mm/hr. What is the first-line medical treatment?",
                "correct": "Oral Prednisolone",
                "explanation": "Polymyalgia rheumatica (PMR) is treated first-line with low-dose oral corticosteroids (typically prednisolone 15mg daily), which usually results in a rapid and dramatic resolution of symptoms."
            },
            {
                "scenario": "A 38-year-old female with newly diagnosed, active rheumatoid arthritis is started on DMARD therapy. What is the standard first-line disease-modifying drug recommended by NICE?",
                "correct": "Oral Methotrexate",
                "explanation": "For active rheumatoid arthritis, NICE recommends first-line DMARD monotherapy with oral methotrexate (alongside short-term corticosteroid bridging to induce rapid remission)."
            },
            {
                "scenario": "A 45-year-old male with recurrent gouty attacks is ready to start uric acid-lowering therapy. His last acute attack resolved completely 3 weeks ago. What drug should be initiated?",
                "correct": "Oral Allopurinol",
                "explanation": "Allopurinol (a xanthine oxidase inhibitor) is the first-line long-term prophylactic drug used to lower serum uric acid levels and prevent recurrent gouty flares."
            },
            {
                "scenario": "A 28-year-old male with severe ankylosing spondylitis has persistent high disease activity despite max-dose treatment with two different NSAIDs. What is the next step in specialist management?",
                "correct": "Infliximab",
                "explanation": "For patients with severe active ankylosing spondylitis that has not responded to NSAIDs, anti-TNF alpha therapy (such as infliximab, adalimumab, or etanercept) is indicated."
            }
        ]
    },
    {
        "theme": "Investigation of Musculoskeletal Pain",
        "category": "Musculoskeletal",
        "options": [
            "Joint aspiration and fluid analysis",
            "X-ray of the joint",
            "MRI of the spine",
            "DXA scan",
            "Serum uric acid",
            "Anti-CCP antibodies",
            "Serum CK",
            "Autoantibody screen"
        ],
        "scenarios": [
            {
                "scenario": "A 72-year-old female presents with a hot, red, swollen right knee. She is febrile (38.2°C) and unable to bear weight. What is the most urgent diagnostic investigation?",
                "correct": "Joint aspiration and fluid analysis",
                "explanation": "A hot, swollen, painful joint is a suspected septic arthritis until proven otherwise. Immediate joint aspiration for microscopy, Gram stain, and culture is the critical diagnostic test before starting antibiotics."
            },
            {
                "scenario": "A 62-year-old female presents with persistent pain in both hands, particularly the DIP joints and thumb bases. You want to confirm the clinical diagnosis of hand osteoarthritis. What imaging is required?",
                "correct": "X-ray of the joint",
                "explanation": "Plain radiography is the gold standard imaging modality to diagnose and assess osteoarthritis, showing joint space narrowing, osteophytes, subchondral sclerosis, and subchondral cysts."
            },
            {
                "scenario": "A 76-year-old postmenopausal female sustains a low-trauma mechanical fall resulting in a wrist fracture. You want to assess her bone mineral density to evaluate for osteoporosis.",
                "correct": "DXA scan",
                "explanation": "Dual-energy X-ray absorptiometry (DXA) scanning is the gold standard method used to measure bone mineral density (T-score) and diagnose osteoporosis."
            },
            {
                "scenario": "A 32-year-old female presents with symmetrical inflammatory arthritis of the hands. Rheumatoid factor is negative. What serological test has the highest specificity for diagnosing rheumatoid arthritis?",
                "correct": "Anti-CCP antibodies",
                "explanation": "Anti-cyclic citrullinated peptide (anti-CCP) antibodies have a very high specificity (>95%) for rheumatoid arthritis and can predict radiographic joint destruction."
            },
            {
                "scenario": "A 55-year-old male presents with lower back pain radiating down both legs, accompanied by new urinary incontinence, saddle anaesthesia, and reduced anal tone.",
                "correct": "MRI of the spine",
                "explanation": "Cauda equina syndrome (suggested by bilateral sciatica, saddle anaesthesia, and bladder dysfunction) is a neurosurgical emergency requiring an immediate MRI spine to diagnose the site of compression."
            }
        ]
    },

    # --- PAEDIATRICS (2 themes) ---
    {
        "theme": "Management of Paediatric Emergencies",
        "category": "Paediatrics",
        "options": [
            "Inhaled Salbutamol",
            "Oral Dexamethasone",
            "Nebulized Adrenaline",
            "Intravenous Ceftriaxone",
            "Buccal Midazolam",
            "High-flow oxygen",
            "Bolus of 0.9% Normal Saline",
            "Oral Paracetamol"
        ],
        "scenarios": [
            {
                "scenario": "A 2-year-old child presents with a barking cough and hoarseness. On examination, the child is systemically well but has a mild inspiratory stridor when agitated. What is the first-line treatment?",
                "correct": "Oral Dexamethasone",
                "explanation": "For all children with croup (regardless of severity), a single dose of oral dexamethasone (0.15mg/kg) or oral prednisolone is the first-line medical treatment."
            },
            {
                "scenario": "An 18-month-old infant is brought to the ED in the middle of a generalized tonic-clonic convulsion. The seizure has been active for 7 minutes, and intravenous access cannot be established.",
                "correct": "Buccal Midazolam",
                "explanation": "For status epilepticus/prolonged convulsion (>5 minutes) in children without IV access, buccal midazolam (or rectal diazepam) is the first-line emergency rescue medication."
            },
            {
                "scenario": "A 3-year-old child is brought to ED with severe breathlessness and a harsh barking cough. On examination, the child is lethargic, has severe chest recession, and loud inspiratory stridor at rest.",
                "correct": "Nebulized Adrenaline",
                "explanation": "Severe croup with respiratory distress and stridor at rest is managed immediately with nebulized adrenaline to reduce airway edema, alongside systemic corticosteroids."
            },
            {
                "scenario": "A 5-year-old child is brought to ED with high fever, neck stiffness, and irritability. Lumbar puncture confirms suspected bacterial meningitis. What is the immediate hospital treatment?",
                "correct": "Intravenous Ceftriaxone",
                "explanation": "Empiric antibiotic therapy for suspected bacterial meningitis in children aged over 3 months is intravenous ceftriaxone (third-generation cephalosporin)."
            },
            {
                "scenario": "An 8-month-old infant is admitted with dehydration secondary to severe gastroenteritis. The infant is pale, cold, lethargic, and has a capillary refill time of 4 seconds. What is the immediate management?",
                "correct": "Bolus of 0.9% Normal Saline",
                "explanation": "In children showing signs of hypovolaemic shock (lethargy, cold extremities, delayed capillary refill time > 2s), immediate management is a rapid IV bolus of 20 ml/kg of 0.9% sodium chloride."
            }
        ]
    },
    {
        "theme": "Diagnosis of Paediatric Conditions",
        "category": "Paediatrics",
        "options": [
            "Bronchiolitis",
            "Croup",
            "Epiglottitis",
            "Pyloric stenosis",
            "Intussusception",
            "Transient tachypnoea of the newborn",
            "Respiratory Distress Syndrome",
            "Febrile convulsion"
        ],
        "scenarios": [
            {
                "scenario": "An 18-month-old infant is brought with a running nose and wet cough, which has progressed to severe wheezing and tachypnoea. On examination, there are bilateral fine crackles and wheeze. Oxygen sat is 94% on room air.",
                "correct": "Bronchiolitis",
                "explanation": "Bronchiolitis typically affects infants < 2 years, presenting with a coryzal prodrome followed by respiratory distress, bilateral wheeze, and fine chest crackles, most commonly caused by RSV."
            },
            {
                "scenario": "A 4-week-old male infant presents with projectile, non-bilious vomiting after every feed. The infant is hungry and eager to feed again. On examination, a small, firm olive-shaped mass is felt in the upper abdomen.",
                "correct": "Pyloric stenosis",
                "explanation": "Congenital hypertrophic pyloric stenosis classically presents in male infants aged 2-8 weeks with projectile non-bilious vomiting, persistent hunger, and a palpable 'olive-shaped' RUQ mass."
            },
            {
                "scenario": "An 8-month-old infant presents with episodes of severe, colicky abdominal pain during which they draw their knees to their chest and cry inconsolably. Between episodes, the infant is lethargic. A sausage-shaped mass is palpable.",
                "correct": "Intussusception",
                "explanation": "Intussusception is the invagination of bowel segment, classically presenting in infants with episodic colic, knees-to-chest drawing, sausage-shaped abdominal mass, and late-stage 'red-currant jelly' stools."
            },
            {
                "scenario": "A 4-year-old child presents with sudden onset of high fever, sore throat, drooling, and difficulty breathing. The child is sitting upright, leaning forward with their chin jutting out (tripod position), and looks toxic.",
                "correct": "Epiglottitis",
                "explanation": "Acute epiglottitis (rare due to Hib vaccine) is a life-threatening airway emergency presenting with rapid fever, severe sore throat, drooling, dyspnoea, and a classic 'tripod' sitting position."
            },
            {
                "scenario": "A term male infant delivered via elective Caesarean section develops tachypnoea (RR 75/min) and mild grunting within an hour of birth. Chest X-ray shows fluid in the horizontal fissure and mild cardiomegaly. Symptoms resolve in 24 hours.",
                "correct": "Transient tachypnoea of the newborn",
                "explanation": "TTN is caused by delayed clearance of fetal lung fluid, common in Caesarean births. It presents with early tachypnoea that is self-limiting and resolves within 24-48 hours with supportive care."
            }
        ]
    },

    # --- PSYCHIATRY / NEUROLOGY (2 themes) ---
    {
        "theme": "Management of Psychiatric Conditions",
        "category": "Psychiatry / Neurology",
        "options": [
            "Sertraline",
            "Fluoxetine",
            "Haloperidol",
            "Olanzapine",
            "Lithium carbonate",
            "Diazepam",
            "Cognitive Behavioural Therapy",
            "Chlordiazepoxide"
        ],
        "scenarios": [
            {
                "scenario": "A 28-year-old female presents with a 6-month history of severe panic attacks, hypervigilance, and flashbacks following a traumatic physical assault. You want to offer the first-line psychological intervention.",
                "correct": "Cognitive Behavioural Therapy",
                "explanation": "For Post-Traumatic Stress Disorder (PTSD), first-line interventions include trauma-focused Cognitive Behavioural Therapy (CBT) or Eye Movement Desensitisation and Reprocessing (EMDR)."
            },
            {
                "scenario": "A 16-year-old adolescent presents with a 4-week history of low mood, anhedonia, and poor concentration. You diagnose moderate-to-severe depression. What is the first-line medication recommended by NICE for adolescents?",
                "correct": "Fluoxetine",
                "explanation": "For children and young people (aged 12-18) with moderate-to-severe depression, fluoxetine (an SSRI) is the only antidepressant recommended as first-line therapy, combined with psychological therapy."
            },
            {
                "scenario": "A 68-year-old male with a history of ischaemic heart disease presents with moderate depression and anxiety. You decide to prescribe an SSRI. Which agent has the safest cardiovascular profile for cardiac patients?",
                "correct": "Sertraline",
                "explanation": "Sertraline is the SSRI of choice for patients with depression and co-existing unstable angina or recent myocardial infarction, as it has the safest cardiovascular profile."
            },
            {
                "scenario": "A 45-year-old male with bipolar disorder presents for a medication review. He has been taking a mood stabilizer for 5 years. He describes polyuria, polydipsia, and a fine hand tremor. Blood tests show elevated TSH.",
                "correct": "Lithium carbonate",
                "explanation": "Lithium carbonate is a common mood stabilizer for bipolar disorder. Side effects include fine tremor, nephrogenic diabetes insipidus (polyuria/polydipsia), and hypothyroidism (elevated TSH)."
            },
            {
                "scenario": "A 42-year-old male is admitted to the hospital for elective hip surgery. He has a history of heavy daily alcohol consumption and develops tremors, sweating, tachycardia, and visual hallucinations 24 hours after admission.",
                "correct": "Chlordiazepoxide",
                "explanation": "This patient is experiencing alcohol withdrawal syndrome (delirium tremens). The management of choice is a reducing regimen of a long-acting benzodiazepine, typically chlordiazepoxide (or diazepam)."
            }
        ]
    },
    {
        "theme": "Diagnosis of Neurological Conditions",
        "category": "Psychiatry / Neurology",
        "options": [
            "Migraine",
            "Tension-type headache",
            "Cluster headache",
            "Subarachnoid haemorrhage",
            "Multiple sclerosis",
            "Epilepsy",
            "Transient Ischaemic Attack",
            "Epilepsy status epilepticus"
        ],
        "scenarios": [
            {
                "scenario": "A 34-year-old male presents with recurrent episodes of excruciating, sharp, unilateral pain around his right eye, lasting 45 minutes and occurring multiple times a day. The pain is accompanied by right eye watering and nasal congestion.",
                "correct": "Cluster headache",
                "explanation": "Cluster headaches present as unilateral, severe periorbital pain lasting 15-180 minutes, associated with ipsilateral autonomic features (lacrimation, rhinorrhea, miosis, ptosis) and restlessness."
            },
            {
                "scenario": "A 42-year-old female presents with a sudden, extremely severe headache that she describes as feeling like she was 'hit over the back of the head with a shovel'. On exam, she has neck stiffness and photophobia.",
                "correct": "Subarachnoid haemorrhage",
                "explanation": "A subarachnoid haemorrhage classically presents with a hyperacute-onset 'thunderclap' headache reaching maximum intensity within seconds/minutes, often with meningism (neck stiffness, photophobia)."
            },
            {
                "scenario": "A 28-year-old female presents with a 2-week history of numbness in her left arm, followed by blurry vision in her right eye that is worse when taking a hot shower (Uhthoff's phenomenon). She had an episode of double vision last year.",
                "correct": "Multiple sclerosis",
                "explanation": "Multiple sclerosis is characterized by neurological lesions disseminated in time and space, commonly presenting with optic neuritis (painful loss of vision), sensory deficits, and temperature-sensitivity (Uhthoff's phenomenon)."
            },
            {
                "scenario": "A 65-year-old male describes a sudden, painless loss of vision in his left eye ('like a curtain coming down') and weak right hand grip that resolved completely within 30 minutes. He is now asymptomatic and neurologically normal.",
                "correct": "Transient Ischaemic Attack",
                "explanation": "A TIA is characterized by transient neurological dysfunction (like amaurosis fugax or hemiparesis) lasting less than 24 hours (usually < 1 hour) with complete resolution, indicating focal cerebral or retinal ischaemia."
            },
            {
                "scenario": "A 22-year-old female is brought to the ED by ambulance. She has been experiencing continuous generalized tonic-clonic seizures for the past 30 minutes without recovering consciousness between episodes.",
                "correct": "Epilepsy status epilepticus",
                "explanation": "Status epilepticus is defined as a seizure lasting > 5 minutes, or recurrent seizures without recovery of consciousness between episodes, which is a life-threatening medical emergency."
            }
        ]
    },

    # --- RENAL / UROLOGY (2 themes) ---
    {
        "theme": "Management of Renal and Urological Conditions",
        "category": "Renal / Urology",
        "options": [
            "Intravenous Calcium Gluconate",
            "Nitrofurantoin",
            "Tamsulosin",
            "Finasteride",
            "Urgent nephrostomy",
            "Intravenous 0.9% Saline",
            "Emergency hemodialysis",
            "Oral Sodium Bicarbonate"
        ],
        "scenarios": [
            {
                "scenario": "A 68-year-old male is admitted with an AKI stage 3. His serum potassium is 6.9 mmol/L, and ECG shows widened QRS complexes and peaked T waves. What is the immediate pharmacological priority?",
                "correct": "Intravenous Calcium Gluconate",
                "explanation": "In severe hyperkalaemia (K > 6.5 mmol/L or with ECG changes), the primary and immediate action is to stabilize the cardiac membrane with intravenous calcium gluconate to prevent arrhythmias."
            },
            {
                "scenario": "A 72-year-old male presents with a high fever, severe right-sided loin pain, and anuria. Renal ultrasound shows a large calculus obstructing the right pelviureteric junction with hydronephrosis. What is the management?",
                "correct": "Urgent nephrostomy",
                "explanation": "An obstructed, infected kidney (renal colic with fever/hydronephrosis) is a medical emergency requiring urgent decompression, either via retrograde stent insertion or percutaneous nephrostomy."
            },
            {
                "scenario": "A 28-year-old female who is 14 weeks pregnant presents with dysuria and frequency. Urine dipstick is positive for nitrites and leucocytes. What is the first-line empirical antibiotic of choice?",
                "correct": "Nitrofurantoin",
                "explanation": "Nitrofurantoin is the first-line antibiotic for lower UTIs in pregnant women (unless at term, where it risks neonatal haemolysis, where cephalexin or amoxicillin is preferred)."
            },
            {
                "scenario": "A 75-year-old male complains of hesitancy, weak stream, and nocturia. Rectal exam reveals a smooth, symmetrically enlarged prostate. You want to prescribe an alpha-1 blocker to improve his symptoms rapidly.",
                "correct": "Tamsulosin",
                "explanation": "Alpha-1 adrenoreceptor antagonists (like tamsulosin) act on smooth muscle of the bladder neck and prostate to improve urinary flow symptoms rapidly (within days) in BPH."
            },
            {
                "scenario": "A 64-year-old male with anuria is admitted with severe volume overload and pulmonary edema. Lab results: potassium 7.2 mmol/L, pH 7.05, urea 38 mmol/L. He is unresponsive to high-dose IV furosemide.",
                "correct": "Emergency hemodialysis",
                "explanation": "Indications for emergency hemodialysis in AKI include refractory hyperkalaemia, refractory metabolic acidosis (pH < 7.2), fluid overload unresponsive to diuretics, and severe uraemic complications."
            }
        ]
    },
    {
        "theme": "Diagnosis of Renal Impairment",
        "category": "Renal / Urology",
        "options": [
            "Acute Kidney Injury stage 1",
            "Acute Kidney Injury stage 3",
            "Chronic Kidney Disease stage 4",
            "Nephrotic syndrome",
            "Acute tubular necrosis",
            "Pre-renal uraemia",
            "Post-renal obstruction",
            "Glomerulonephritis"
        ],
        "scenarios": [
            {
                "scenario": "A 72-year-old male is admitted with severe gastroenteritis and dehydration. Bloods show: creatinine 240 umol/L (baseline 80 umol/L, 3x baseline), urea 28 mmol/L, potassium 5.2 mmol/L. Urine output has been <0.3 ml/kg/h for 12 hours.",
                "correct": "Acute Kidney Injury stage 3",
                "explanation": "AKI Stage 3 is defined by a rise in creatinine >= 3.0x baseline, or creatinine >= 354 umol/L with an acute rise, or urine output < 0.3 ml/kg/h for >= 24 hours (or anuria for >= 12 hours)."
            },
            {
                "scenario": "A 5-year-old boy presents with progressive swelling around his eyes (periorbital edema) and swollen ankles. Urinalysis shows 4+ protein, and serum albumin is 18 g/L (reference > 35). Total cholesterol is elevated.",
                "correct": "Nephrotic syndrome",
                "explanation": "Nephrotic syndrome is defined by the triad of heavy proteinuria (>3.5g/24h or 4+ on dipstick), hypoalbuminaemia (<30g/L), and generalized edema, often with hyperlipidaemia."
            },
            {
                "scenario": "A 65-year-old male with a history of prostate cancer presents with lower abdominal pain and anuria. Ultrasound reveals bilateral hydronephrosis and a severely distended urinary bladder.",
                "correct": "Post-renal obstruction",
                "explanation": "Post-renal AKI is caused by obstruction of urine outflow (e.g. BPH, prostate cancer, renal stones), characterized by hydronephrosis on ultrasound and urinary retention."
            },
            {
                "scenario": "A 58-year-old diabetic female has routine bloods showing: eGFR 24 ml/min/1.73m2 (baseline 25 ml/min six months ago), creatinine 210 umol/L. She has persistent microalbuminuria.",
                "correct": "Chronic Kidney Disease stage 4",
                "explanation": "CKD Stage 4 is defined by a severely decreased GFR of 15 - 29 ml/min/1.73m2, present for at least 3 months, indicating chronic progressive loss of renal function."
            },
            {
                "scenario": "A 78-year-old male hospitalized for severe sepsis is treated with IV gentamicin. Over the next 4 days, his creatinine rises from 90 to 220 umol/L. Urinalysis shows dark brown ('muddy brown') granular casts.",
                "correct": "Acute tubular necrosis",
                "explanation": "Acute tubular necrosis (ATN) is a common cause of intrinsic AKI in hospitalized patients, triggered by ischaemia or nephrotoxins (like gentamicin), showing classic 'muddy brown' casts on urinalysis."
            }
        ]
    },

    # --- REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY (2 themes) ---
    {
        "theme": "Management of Obstetric Emergencies",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "options": [
            "Intravenous Magnesium Sulfate",
            "Intramuscular Dexamethasone",
            "Emergency lower segment Caesarean section",
            "Intravenous Labetalol",
            "Intramuscular Adrenaline",
            "Ergometrine",
            "Surgical laparoscopy",
            "Syntocinon infusion"
        ],
        "scenarios": [
            {
                "scenario": "A 34-year-old pregnant female at 32 weeks gestation is admitted with severe pre-eclampsia. Suddenly, she develops generalized tonic-clonic convulsions. What is the immediate drug of choice to control the seizures?",
                "correct": "Intravenous Magnesium Sulfate",
                "explanation": "In eclampsia (seizures in pre-eclampsia), the immediate drug of choice to treat and prevent further seizures is intravenous magnesium sulfate (a loading dose followed by maintenance infusion)."
            },
            {
                "scenario": "A 28-year-old pregnant female at 30 weeks gestation is admitted in threatened preterm labour. She is contracting regularly and cervix is dilated. What medication is indicated to promote fetal lung maturity?",
                "correct": "Intramuscular Dexamethasone",
                "explanation": "For women in threatened or established preterm labour between 24 and 34 weeks of gestation, antenatal corticosteroids (typically IM dexamethasone or betamethasone) are indicated to stimulate fetal surfactant production."
            },
            {
                "scenario": "A 32-year-old female at 39 weeks gestation has a prolonged second stage of labour. CTG reveals severe, persistent bradycardia of 80 bpm with loss of variability. She is fully dilated and head is at -3 station.",
                "correct": "Emergency lower segment Caesarean section",
                "explanation": "For acute fetal distress during labour (persistent bradycardia) when instrumental vaginal delivery is not feasible (e.g. high fetal station at -3), an emergency Caesarean section is indicated."
            },
            {
                "scenario": "A 35-year-old female experiences severe postpartum haemorrhage (PPH) of 1200ml following a vaginal delivery. The uterus is soft, boggy, and palpated above the umbilicus. What is the first-line pharmacological treatment?",
                "correct": "Syntocinon infusion",
                "explanation": "Uterine atony is the most common cause of PPH. Initial pharmacological management consists of uterine massage, intravenous syntocinon (oxytocin), or ergometrine to stimulate uterine contraction."
            },
            {
                "scenario": "A 24-year-old female who is 34 weeks pregnant has a blood pressure of 165/110 mmHg on two separate readings. She has headache and visual blurriness. What is the first-line medication to lower her blood pressure?",
                "correct": "Intravenous Labetalol",
                "explanation": "For severe gestational hypertension or pre-eclampsia (BP >= 160/110 mmHg), labetalol (first-line) or nifedipine is used to reduce the risk of maternal stroke."
            }
        ]
    },
    {
        "theme": "Diagnosis of Gynaecological Conditions",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "options": [
            "Ectopic pregnancy",
            "Pelvic Inflammatory Disease",
            "Endometriosis",
            "Polycystic Ovary Syndrome",
            "Ovarian cancer",
            "Cervical cancer",
            "Uterine fibroids",
            "Miscarriage"
        ],
        "scenarios": [
            {
                "scenario": "A 28-year-old female presents with a 3-month history of severe pelvic pain during menstruation (dysmenorrhoea), pain during intercourse (dyspareunia), and chronic pelvic pain throughout her cycle.",
                "correct": "Endometriosis",
                "explanation": "Endometriosis is characterized by the presence of endometrial tissue outside the uterine cavity, presenting with the classic triad of dysmenorrhoea, dyspareunia, and chronic pelvic pain, often with subfertility."
            },
            {
                "scenario": "A 22-year-old female presents with lower abdominal pain, deep dyspareunia, and abnormal purulent vaginal discharge. On speculum examination, she has cervical motion tenderness ('excitation') and adnexal tenderness.",
                "correct": "Pelvic Inflammatory Disease",
                "explanation": "PID is an ascending infection of the female reproductive tract, typically caused by Chlamydia or Gonorrhoea, presenting with pelvic pain, cervical excitation, fever, and purulent discharge."
            },
            {
                "scenario": "A 24-year-old female presents with irregular periods (oligomenorrhoea), hirsutism, and acne. On examination, her BMI is 31. Ultrasound reveals multiple small peripheral ovarian follicles ('string of pearls' appearance).",
                "correct": "Polycystic Ovary Syndrome",
                "explanation": "PCOS is diagnosed using the Rotterdam criteria (any 2 of: oligomenorrhoea/anovulation, clinical/biochemical hyperandrogenism, and polycystic ovaries on ultrasound)."
            },
            {
                "scenario": "A 62-year-old female presents with abdominal bloating, early satiety, and pelvic discomfort. On examination, a firm adnexal mass is felt. Blood tests show an elevated serum CA125 level.",
                "correct": "Ovarian cancer",
                "explanation": "Ovarian cancer typically presents in postmenopausal women with vague abdominal symptoms (bloating, early satiety) and is investigated with serum CA125 and pelvic ultrasound."
            },
            {
                "scenario": "A 32-year-old female who is 8 weeks pregnant presents with crampy lower abdominal pain and moderate vaginal bleeding. Speculum exam reveals an open cervical os with visible products of conception.",
                "correct": "Miscarriage",
                "explanation": "An inevitable or incomplete miscarriage is characterized by lower abdominal cramps, vaginal bleeding in early pregnancy, and a dilated/open cervical os on speculum examination."
            }
        ]
    },

    # --- DERMATOLOGY / OPHTHALMOLOGY / ENT (3 themes) ---
    {
        "theme": "Diagnosis of Skin Lesions",
        "category": "Dermatology / Ophthalmology / ENT",
        "options": [
            "Melanoma",
            "Basal Cell Carcinoma",
            "Squamous Cell Carcinoma",
            "Seborrheic keratosis",
            "Actinic keratosis",
            "Psoriasis",
            "Eczema",
            "Shingles"
        ],
        "scenarios": [
            {
                "scenario": "A 72-year-old male presents with a slow-growing lesion on his nose. On inspection, there is a 6mm pearly nodule with raised, rolled borders and telangiectasia. The center is slightly ulcerated ('rodent ulcer').",
                "correct": "Basal Cell Carcinoma",
                "explanation": "Basal cell carcinoma (BCC) is the most common skin cancer, classically presenting as a pearly nodule with rolled borders, telangiectasia, and central ulceration on sun-exposed areas."
            },
            {
                "scenario": "A 48-year-old female presents with a mole on her left calf that has recently changed shape and color. On examination, there is an asymmetrical, 8mm pigmented macule with irregular borders and multiple shades of brown.",
                "correct": "Melanoma",
                "explanation": "Malignant melanoma is characterized by the ABCDE criteria (Asymmetry, Border irregularity, Color variegation, Diameter > 6mm, Evolving/changing)."
            },
            {
                "scenario": "A 68-year-old farmer presents with multiple rough, scaly, sand-paper-like patches on his bald scalp. They are erythematous and non-tender. There is no induration or ulceration.",
                "correct": "Actinic keratosis",
                "explanation": "Actinic (solar) keratoses are dysplastic precursor lesions caused by UV exposure, presenting as dry, rough, scaly, sandpaper-like papules on sun-damaged skin."
            },
            {
                "scenario": "A 58-year-old female presents with a dark brown, raised, warty-looking lesion on her trunk. It appears to be 'stuck-on' to the skin surface, has a greasy texture, and shows comedo-like openings under dermoscopy.",
                "correct": "Seborrheic keratosis",
                "explanation": "Seborrheic keratoses are benign epidermal proliferations, very common in older adults, characterized by a classic 'stuck-on', warty, or greasy appearance."
            },
            {
                "scenario": "A 76-year-old male presents with a rapidly growing, firm, hyperkeratotic nodule on his lower lip that has started to ulcerate. He is a retired construction worker.",
                "correct": "Squamous Cell Carcinoma",
                "explanation": "Squamous cell carcinoma (SCC) presents as a rapidly growing, scaly, or crusted nodule that may ulcerate, commonly arising on sun-exposed sites (like the lower lip) in patients with high UV exposure."
            }
        ]
    },
    {
        "theme": "Management of Red Eye",
        "category": "Dermatology / Ophthalmology / ENT",
        "options": [
            "Topical Chloramphenicol",
            "Topical Aciclovir",
            "Topical Prednisolone",
            "Intravenous Acetazolamide",
            "Laser iridotomy",
            "Urgent ophthalmology referral",
            "Reassurance and warm compresses",
            "Topical Latanoprost"
        ],
        "scenarios": [
            {
                "scenario": "A 24-year-old male presents with a 24-hour history of a sticky, red right eye with purulent discharge. On examination, the conjunctiva is injected, but vision is normal and the pupil is reactive.",
                "correct": "Topical Chloramphenicol",
                "explanation": "Bacterial conjunctivitis presents with acute red eye and purulent discharge. Broad-spectrum topical antibiotics (like chloramphenicol drops) are used to speed up resolution."
            },
            {
                "scenario": "A 68-year-old female presents to the eye clinic with sudden, severe left eye pain, blurred vision, and vomiting. The left eye is red, cornea is hazy, and the pupil is fixed and mid-dilated. What is the immediate medical management?",
                "correct": "Intravenous Acetazolamide",
                "explanation": "Acute angle closure glaucoma is an ocular emergency. Immediate medical therapy is targeted at lowering intraocular pressure using intravenous acetazolamide."
            },
            {
                "scenario": "A 32-year-old female presents with a red right eye, pain, and photophobia. Slit lamp examination with fluorescein staining reveals a branching, dendritic corneal ulcer.",
                "correct": "Topical Aciclovir",
                "explanation": "Herpes simplex keratitis classically presents as a painful red eye with photophobia and a characteristic dendritic ulcer on fluorescein staining, managed with topical antiviral (ganciclovir or aciclovir) ointment."
            },
            {
                "scenario": "A 28-year-old male with a history of ankylosing spondylitis presents with a painful, photophobic red right eye. Examination reveals a small, irregular pupil and ciliary injection. You suspect acute anterior uveitis.",
                "correct": "Urgent ophthalmology referral",
                "explanation": "Acute anterior uveitis (iritis) is an inflammatory condition requiring urgent ophthalmology assessment to confirm diagnosis and prescribe specialist treatment (topical steroids and cycloplegics)."
            },
            {
                "scenario": "A 45-year-old male presents with a localized, bright red patch in the white of his left eye. He has no pain, discharge, or visual changes. It started after a severe coughing fit. Vitals are normal.",
                "correct": "Reassurance and warm compresses",
                "explanation": "A subconjunctival haemorrhage is a benign, painless extravasation of blood under the conjunctiva, often following coughing/straining, requiring only reassurance as it resolves spontaneously in 10-14 days."
            }
        ]
    },
    {
        "theme": "Diagnosis of ENT Conditions",
        "category": "Dermatology / Ophthalmology / ENT",
        "options": [
            "Otitis media",
            "Otitis externa",
            "Vestibular neuronitis",
            "Benign Paroxysmal Positional Vertigo",
            "Meniere's disease",
            "Tonsillitis",
            "Epistaxis",
            "Acoustic neuroma"
        ],
        "scenarios": [
            {
                "scenario": "A 24-year-old female swimmer presents with a 2-day history of right ear pain, itching, and discharge. On examination, the external ear canal is erythematous and swollen, and tragal pressure causes severe pain.",
                "correct": "Otitis externa",
                "explanation": "Otitis externa (swimmer's ear) is inflammation of the external ear canal, presenting with ear canal swelling, erythema, discharge, and characteristically severe pain on tragal manipulation."
            },
            {
                "scenario": "A 42-year-old male describes brief episodes of severe vertigo lasting 10-20 seconds, triggered by rolling over in bed or looking up. The symptoms are reproduced in clinic by performing the Dix-Hallpike maneuver.",
                "correct": "Benign Paroxysmal Positional Vertigo",
                "explanation": "BPPV is caused by canalolithiasis in the semicircular canals, presenting with brief, positional-induced vertigo episodes, diagnosed by Dix-Hallpike and treated with Epley maneuver."
            },
            {
                "scenario": "A 35-year-old female presents with recurrent episodes of vertigo lasting 2-4 hours, accompanied by fluctuating left-sided hearing loss, tinnitus, and a sensation of fullness in the left ear.",
                "correct": "Meniere's disease",
                "explanation": "Meniere's disease is caused by endolymphatic hydrops, presenting with the triad of episodic vertigo (lasting hours), fluctuating sensorineural hearing loss, tinnitus, and aural fullness."
            },
            {
                "scenario": "A 52-year-old female presents with a 2-day history of constant, severe vertigo, nausea, and vomiting. She is bed-bound. She had a cold last week. Examination shows horizontal nystagmus. Hearing is completely normal.",
                "correct": "Vestibular neuronitis",
                "explanation": "Vestibular neuronitis is acute inflammation of the vestibular nerve, classically presenting with rapid, constant vertigo, nausea, and nystagmus following a viral prodrome, without hearing loss."
            },
            {
                "scenario": "A 58-year-old male presents with slowly progressive, unilateral hearing loss on the right side over the last 18 months, accompanied by mild right-sided tinnitus and unsteadiness. MRI reveals a cerebellopontine angle tumor.",
                "correct": "Acoustic neuroma",
                "explanation": "An acoustic neuroma (vestibular schwannoma) is a benign tumor of the vestibulocochlear nerve (CN VIII), presenting with progressive unilateral sensorineural hearing loss, tinnitus, and balance issues."
            }
        ]
    },

    # --- PHARMACOLOGY (3 themes) ---
    {
        "theme": "Antidotes for Drug Overdoses",
        "category": "Pharmacology",
        "options": [
            "N-acetylcysteine",
            "Naloxone",
            "Flumazenil",
            "Atropine",
            "Digoxin-specific antibody fragments",
            "Calcium gluconate",
            "Phytomenadione (Vitamin K)",
            "Protamine sulfate"
        ],
        "scenarios": [
            {
                "scenario": "A 24-year-old male is brought to the ED unresponsive. Vitals: RR 6 breaths/min, pinpoint pupils. A clinical diagnosis of opioid overdose is made. What is the immediate pharmacological antidote?",
                "correct": "Naloxone",
                "explanation": "Naloxone is a competitive opioid receptor antagonist used as the immediate antidote for opioid overdose to reverse severe respiratory depression."
            },
            {
                "scenario": "A 72-year-old male with atrial fibrillation is admitted with nausea, confusion, and yellow-green visual halos. ECG shows a ventricular tachycardia with a 'reverse tick' appearance. He takes Digoxin.",
                "correct": "Digoxin-specific antibody fragments",
                "explanation": "Severe digoxin toxicity presenting with cardiac arrhythmias, hyperkalaemia, or haemodynamic instability is treated with digoxin-specific antibody fragments (Digibind)."
            },
            {
                "scenario": "A 32-year-old female is admitted after ingesting 24 tablets of paracetamol 6 hours ago. Her blood paracetamol levels are plotted above the treatment line on the nomogram. What therapy must be started?",
                "correct": "N-acetylcysteine",
                "explanation": "Intravenous N-acetylcysteine (NAC) is the antidote for paracetamol overdose, acting as a precursor for glutathione to prevent toxic metabolite-induced hepatotoxicity."
            },
            {
                "scenario": "A 68-year-old female on Warfarin for a prosthetic heart valve is admitted with a massive gastrointestinal bleed. Her INR is 8.4. You need to reverse the anticoagulation urgently.",
                "correct": "Phytomenadione (Vitamin K)",
                "explanation": "For major bleeding with elevated INR in patients on warfarin, the anticoagulation is reversed using intravenous Vitamin K (phytomenadione) alongside prothrombin complex concentrate (PCC)."
            },
            {
                "scenario": "A 54-year-old male is brought to ED after accidentally taking too many sleeping pills (Diazepam). He is drowsy but breathing safely. What is the specific benzodiazepine receptor antagonist available?",
                "correct": "Flumazenil",
                "explanation": "Flumazenil is a benzodiazepine receptor antagonist. It is rarely used in routine overdose due to the risk of precipitating severe, treatment-resistant seizures in chronic users."
            }
        ]
    },
    {
        "theme": "Drug Side Effects and Monitoring",
        "category": "Pharmacology",
        "options": [
            "Lithium toxicity",
            "Amiodarone-induced thyroid dysfunction",
            "Statin-induced myopathy",
            "ACE-inhibitor cough",
            "Gentamicin toxicity",
            "Digoxin toxicity",
            "Haloperidol tardive dyskinesia",
            "Methotrexate pneumonitis"
        ],
        "scenarios": [
            {
                "scenario": "A 68-year-old male recently started on Ramipril for hypertension presents with a persistent, dry, hacking cough that is worse at night. He has no other chest symptoms, and examination is normal.",
                "correct": "ACE-inhibitor cough",
                "explanation": "A dry cough is a common side effect of ACE inhibitors (like ramipril), caused by increased accumulation of bradykinin in the respiratory tract. Swapping to an ARB (like losartan) resolves it."
            },
            {
                "scenario": "A 54-year-old female taking Atorvastatin 40mg nightly complains of severe, bilateral thigh pain and weakness that began 2 weeks ago. Blood tests show a serum Creatine Kinase (CK) level of 1200 U/L.",
                "correct": "Statin-induced myopathy",
                "explanation": "Statins can cause myalgia, myopathy, and rarely rhabdomyolysis, marked by muscle pain/weakness and elevated creatine kinase (CK) levels."
            },
            {
                "scenario": "A 72-year-old male taking Lithium for bipolar disorder presents with ataxia, coarse hand tremor, vomiting, and confusion. He was recently started on a loop diuretic for heart failure.",
                "correct": "Lithium toxicity",
                "explanation": "Lithium has a narrow therapeutic range (0.4-1.0 mmol/L). Toxicity presents with neurological symptoms (ataxia, coarse tremor, confusion) and is often precipitated by drugs affecting renal clearance (diuretics, NSAIDs, ACEIs)."
            },
            {
                "scenario": "A 62-year-old female taking an antiarrhythmic for atrial fibrillation presents with weight loss, heat intolerance, and sweating. Bloods show: TSH <0.01 mU/L, Free T4 28 pmol/L. She also has blue-grey skin discoloration.",
                "correct": "Amiodarone-induced thyroid dysfunction",
                "explanation": "Amiodarone is iodine-rich and can cause both hypothyroidism and hyperthyroidism, as well as blue-grey skin pigmentation, corneal microdeposits, and pulmonary fibrosis."
            },
            {
                "scenario": "A 68-year-old patient on weekly Methotrexate for rheumatoid arthritis presents with a 1-week history of dry cough, progressive breathlessness, and fever. Chest X-ray shows diffuse interstitial infiltrates.",
                "correct": "Methotrexate pneumonitis",
                "explanation": "Methotrexate pneumonitis is a rare but life-threatening hypersensitivity reaction presenting with dry cough, dyspnoea, fever, and interstitial changes, requiring drug suspension and corticosteroids."
            }
        ]
    },
    {
        "theme": "Mechanism of Action of Common Drugs",
        "category": "Pharmacology",
        "options": [
            "Proton pump inhibitor",
            "Beta-blocker",
            "HMG-CoA reductase inhibitor",
            "Loop diuretic",
            "ACE inhibitor",
            "DOAC",
            "Sulfonylurea",
            "SSRI"
        ],
        "scenarios": [
            {
                "scenario": "A 54-year-old male is started on Lansoprazole for severe gastroesophageal reflux disease. What is the mechanism of action of this drug class?",
                "correct": "Proton pump inhibitor",
                "explanation": "Lansoprazole is a proton pump inhibitor (PPI) that works by irreversibly blocking the hydrogen/potassium adenosine triphosphatase enzyme system (the H+/K+ ATPase pump) of gastric parietal cells."
            },
            {
                "scenario": "A 62-year-old male is started on Atorvastatin for primary prevention of cardiovascular disease. What enzyme does this drug class inhibit to reduce cholesterol synthesis?",
                "correct": "HMG-CoA reductase inhibitor",
                "explanation": "Statins work by competitively inhibiting HMG-CoA reductase, the rate-limiting enzyme in hepatic cholesterol synthesis, which upregulates LDL receptors on hepatocytes."
            },
            {
                "scenario": "A 74-year-old female is prescribed Furosemide to treat fluid overload in congestive heart failure. Where and how does this medication act in the nephron?",
                "correct": "Loop diuretic",
                "explanation": "Furosemide is a loop diuretic that acts on the thick ascending limb of the loop of Henle, inhibiting the Na+/K+/2Cl- cotransporter to increase water excretion."
            },
            {
                "scenario": "A 45-year-old female is started on Sertraline for major depressive disorder. What is the primary mechanism of action of this antidepressant?",
                "correct": "SSRI",
                "explanation": "Sertraline is a Selective Serotonin Reuptake Inhibitor (SSRI) that works by inhibiting the presynaptic serotonin transporter, increasing synaptic serotonin concentration."
            },
            {
                "scenario": "A 58-year-old male is started on Ramipril to treat hypertension. What enzyme is inhibited by this class of medication to reduce angiotensin II levels?",
                "correct": "ACE inhibitor",
                "explanation": "Ramipril is an Angiotensin-Converting Enzyme (ACE) inhibitor, which prevents the conversion of angiotensin I to the potent vasoconstrictor angiotensin II."
            }
        ]
    }
]

# --- PROFESSIONAL DILEMMAS: 7 RANKING TEMPLATES ---
NEW_PD_RANKING_TEMPLATES = [
    # 1. Wrong medication administered
    {
        "scenario": "You are a {role_me} on the {dept}. A staff nurse tells you in confidence that they have accidentally administered a double dose of {medication} to a patient. The patient appears well and stable. How should you rank these actions?",
        "options": [
            "Acknowledge the nurse's honesty, immediately assess the patient, check their vitals, and review the drug charts.",
            "Inform your senior registrar or consultant on duty about the medication error.",
            "Document the error and your clinical assessment transparently in the patient's medical notes.",
            "Submit a formal incident report (e.g. Datix) to ensure systematic review.",
            "Tell the nurse to keep quiet about the mistake since the patient is stable and to avoid unnecessary paperwork."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Patient safety is the absolute first priority; immediate clinical assessment is required. The senior team must be informed of errors. Transparent documentation is a legal and professional duty. Systemic reporting via Datix prevents future errors. Hiding the error is unprofessional and dangerous."
    },
    # 2. Underperforming Colleague
    {
        "scenario": "You notice that a fellow junior doctor, {colleague_name}, is struggling to complete routine ward tasks in the {dept}, leading to major discharge delays and clinical tasks being missed. How should you rank these actions?",
        "options": [
            "Speak to {colleague_name} privately, express your concern, and ask if they are okay or if they need help with their workload.",
            "Suggest to {colleague_name} that you both review the remaining tasks together and allocate them based on priority.",
            "Discuss the situation with your registrar to see if ward support or clinical schedules can be adjusted.",
            "Say nothing to {colleague_name} but complain about their speed and incompetence to the ward nursing staff.",
            "Refuse to cover any of their missed tasks, letting patient care suffer to teach them a lesson."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Supportive peer interaction is first-line. Offering joint prioritization helps resolve immediate risk. Involving seniors is appropriate for structural workload issues. Gossiping to nurses is unprofessional. Sabotaging patient care is dangerous and unacceptable."
    },
    # 3. Needlestick Injury from patient with unknown status
    {
        "scenario": "While performing a {procedure} on a patient with unknown blood-borne virus status in the {dept}, you sustain a needlestick injury. How should you rank these actions?",
        "options": [
            "Immediately encourage bleeding from the wound and wash it thoroughly with warm running water and soap.",
            "Report immediately to Occupational Health or the Emergency Department for post-exposure prophylaxis assessment.",
            "Log the needlestick injury in the hospital's incident reporting system (Datix).",
            "Ask a colleague to test the patient's blood sample for viral markers without the patient's knowledge.",
            "Apply a strong chemical disinfectant to the wound and continue your shift without telling anyone."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Immediate first aid (washing) is critical. Occupational Health/ED reporting ensures timely PEP. Logging via Datix is necessary. Testing a patient without consent is a major ethical breach. Squeezing chemicals or hiding the injury compromises health."
    },
    # 4. Patient Refusing Life-Saving Treatment
    {
        "scenario": "A patient on the {dept} who is diagnosed with {condition} refuses to undergo {treatment}, despite being told it is life-saving. The patient is alert, orientated, and appears to understand the risks. How should you rank these actions?",
        "options": [
            "Explore the patient's reasons for refusal, address their concerns, and explain the risks of not having the treatment.",
            "Offer alternative treatment options, suggest speaking with their family (if consented), or getting a second consultant opinion.",
            "Accept the patient's refusal, document the discussion and capacity assessment in the notes, and arrange safety netting.",
            "Administer the {treatment} anyway against their will while they are asleep to save their life.",
            "Tell the patient they are being foolish and refuse to provide any further medical care."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Patient autonomy is paramount. First explore and address concerns. Offering alternatives and second opinions respects autonomy. Documenting capacity and refusal is standard. Forcing treatment on a capacitous patient is assault. Abandoning a patient is a severe professional violation."
    },
    # 5. Research Data Manipulation
    {
        "scenario": "You are working on a research project with a colleague, {colleague_name}, in the {dept}. You notice they are altering statistical data to make the results look significant before submission. How should you rank these actions?",
        "options": [
            "Speak to {colleague_name} privately, point out the discrepancies, and ask them to revert to the original raw data.",
            "Raise your concerns with the principal investigator or research supervisor of the project.",
            "Withdraw your name from the research paper to protect your professional integrity.",
            "Ignore the data manipulation to avoid professional conflict and maintain your friendship.",
            "Help {colleague_name} alter the remaining data to ensure the paper gets published in a prestigious journal."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Integrity in research is a fundamental GMC duty. First address directly to allow correction. Escalating to supervisors is necessary if uncorrected. Withdrawing protects you but doesn't solve the fraud. Ignoring is complicity. Participating in research fraud is a severe professional violation."
    },
    # 6. Inappropriate boundaries (Patient flirting)
    {
        "scenario": "A patient on the {dept} who you recently treated sends you personal, flirtatious messages on social media, requesting a date. How should you rank these actions?",
        "options": [
            "Politely decline the invitation, explaining that professional boundaries prevent you from social relationships with patients.",
            "Document the messages and your response in the patient's medical records or log it in your portfolio.",
            "Discuss the interaction with your clinical supervisor or consultant to seek advice.",
            "Ignore the messages completely, hoping the patient will understand and stop writing.",
            "Accept the invitation, block them on work channels, and meet them in private outside the hospital."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Clear, polite declination maintains professional boundaries (most appropriate). Documenting protects you. Supervisor discussion provides guidance. Ignoring is passive and may escalate boundaries. Engaging in social/romantic relationships with active patients is a major violation of GMC guidance."
    },
    # 7. Conflict between colleagues
    {
        "scenario": "While on duty in the {dept}, you witness two senior nurses, {nurse1} and {nurse2}, arguing loudly and using unprofessional language in the middle of the ward corridor in front of patients. How should you rank these actions?",
        "options": [
            "Approach them calmly and politely suggest that they move their discussion to a private office or break room.",
            "Inform the ward manager or nurse in charge about the active conflict so they can intervene.",
            "Focus on your clinical tasks, making sure patients on the ward are not left unattended during the dispute.",
            "Stand nearby and watch the argument to see who is right and tell other colleagues about it later.",
            "Join in the argument to defend the nurse you believe is in the right."
        ],
        "correct_order": [0, 1, 2, 3, 4],
        "explanation": "Immediate polite intervention protects patient environment (most appropriate). Escalating to managers is appropriate. Focusing on clinical work is neutral. Watching/gossiping is unprofessional. Joining a public argument escalates conflict and damages professional standards."
    }
]

NEW_PD_RANKING_VARS = [
    # 1. Wrong medication administered
    [
        {"role_me": "foundation doctor", "dept": "Geriatric Ward", "medication": "an oral hypoglycaemic"},
        {"role_me": "F2 doctor", "dept": "Emergency Department", "medication": "intravenous paracetamol"},
        {"role_me": "FY1 doctor", "dept": "Acute Medical Unit", "medication": "daily low molecular weight heparin"},
        {"role_me": "SHO", "dept": "Surgical Assessment Unit", "medication": "post-operative antibiotic"},
        {"role_me": "FY1 doctor", "dept": "Paediatric Ward", "medication": "oral liquid ibuprofen"}
    ],
    # 2. Underperforming Colleague
    [
        {"colleague_name": "Dr. Sarah Taylor", "dept": "Medical Admissions Ward"},
        {"colleague_name": "Dr. Alex Mercer", "dept": "Elderly Care Ward"},
        {"colleague_name": "Dr. Lily Evans", "dept": "Emergency Department"},
        {"colleague_name": "Dr. Marcus Vance", "dept": "Surgical Assessment Unit"},
        {"colleague_name": "Dr. Ryan Cooper", "dept": "Busy Paediatric Ward"}
    ],
    # 3. Needlestick Injury
    [
        {"procedure": "venepuncture", "dept": "Acute Medical Unit"},
        {"procedure": "lumbar puncture", "dept": "Medical Admissions Ward"},
        {"procedure": "cannulation", "dept": "Emergency Department"},
        {"procedure": "arterial blood gas", "dept": "Respiratory Ward"},
        {"procedure": "pleural tap", "dept": "Oncology Ward"}
    ],
    # 4. Patient Refusing Life-Saving Treatment
    [
        {"dept": "Cardiology Ward", "condition": "an acute myocardial infarction", "treatment": "urgent coronary angiography"},
        {"dept": "Surgical Ward", "condition": "suspected acute appendicitis", "treatment": "an emergency appendicectomy"},
        {"dept": "Medical Ward", "condition": "severe diabetic ketoacidosis", "treatment": "an intravenous insulin infusion"},
        {"dept": "Respiratory Unit", "condition": "a massive pleural effusion", "treatment": "chest drain insertion"},
        {"dept": "Renal Unit", "condition": "life-threatening hyperkalaemia", "treatment": "intravenous calcium gluconate"}
    ],
    # 5. Research Data Manipulation
    [
        {"colleague_name": "Dr. James Patel", "dept": "Oncology Department"},
        {"colleague_name": "Dr. Chloe Bennett", "dept": "Cardiology Unit"},
        {"colleague_name": "Dr. Ryan Cooper", "dept": "Paediatric Department"},
        {"colleague_name": "Dr. Emma Watson", "dept": "Gastroenterology Unit"},
        {"colleague_name": "Dr. Sam Taylor", "dept": "Neurology Department"}
    ],
    # 6. Inappropriate boundaries
    [
        {"dept": "General Practice Clinic"},
        {"dept": "Emergency Department"},
        {"dept": "Psychiatry Outpatient Clinic"},
        {"dept": "General Surgical Ward"},
        {"dept": "Antenatal Clinic"}
    ],
    # 7. Conflict between colleagues
    [
        {"dept": "General Medical Ward", "nurse1": "Nurse Kelly", "nurse2": "Nurse Jackson"},
        {"dept": "Surgical Ward", "nurse1": "Nurse Higgins", "nurse2": "Nurse Davies"},
        {"dept": "Paediatric Unit", "nurse1": "Nurse Thompson", "nurse2": "Nurse Green"},
        {"dept": "Emergency Department", "nurse1": "Nurse Brown", "nurse2": "Nurse Smith"},
        {"dept": "Maternity Ward", "nurse1": "Nurse Carter", "nurse2": "Nurse Jones"}
    ]
]

# --- PROFESSIONAL DILEMMAS: 7 SELECTION TEMPLATES ---
NEW_PD_SELECTION_TEMPLATES = [
    # 1. Colleague Bullying/Harassment
    {
        "scenario": "You are a {role_me} in the {dept}. You witness a senior registrar, {senior_name}, constantly belittling and shouting at {junior_role} in front of patients and other staff members. Choose the THREE most appropriate actions.",
        "options": [
            "Comfort {junior_role} privately and offer them support and advice on how to handle the situation.",
            "Speak to {senior_role} privately to express your concern about how their behaviour affects team morale and safety.",
            "Report the behaviour to your educational supervisor or the clinical director of the department.",
            "Encourage {junior_role} to document the incidents and contact occupational health or their union.",
            "Comment on the registrar's behavior during a department meeting in front of everyone.",
            "Join in with the registrar's criticisms to avoid becoming a target yourself.",
            "Ignore the situation, assuming it is a standard teaching method and not your business.",
            "Tell {junior_role} that they are too sensitive and should consider a different career."
        ],
        "correct_answers": [0, 2, 3],
        "explanation": "Supporting the victim is a primary duty of care. Escalating bullying to supervisors is necessary to address systemic behavior. Encouraging documentation and union/occupational support empowers the victim. Public confrontation or complicity are unprofessional, and ignoring it neglects professional duties."
    },
    # 2. Suspected Elder Abuse
    {
        "scenario": "An elderly patient, {patient_name}, is admitted to the {dept} from a local nursing home with a {injury_type}. The patient is withdrawn, and the care home staff's explanation of the injury is inconsistent. Choose the THREE most appropriate actions.",
        "options": [
            "Discuss your concerns regarding the injury pattern and history with your supervising consultant.",
            "Contact the hospital's adult safeguarding team to raise a formal safeguarding alert.",
            "Document a detailed, objective account of all physical findings, history given, and discrepancies in the notes.",
            "Confront the care home staff directly and accuse them of abusing the patient.",
            "Accept the care home staff's explanation without question to avoid conflict.",
            "Discharge the patient back to the nursing home immediately after treating the physical injury.",
            "Ask the care home staff to sign a promise that they will monitor the patient more closely.",
            "Call the police immediately to arrest the care home manager without consulting your team."
        ],
        "correct_answers": [0, 1, 2],
        "explanation": "Adult safeguarding is a major professional responsibility. Mismatches in history and injury must be discussed with seniors and escalated to the safeguarding team. Objective documentation of findings is essential. Direct confrontation is unsafe, while ignoring risk or discharging prematurely is negligent."
    },
    # 3. Disclosing Medical Error (No Harm)
    {
        "scenario": "You are a {role_me} on the {dept}. You discover that you have accidentally prescribed a double dose of {medication} to a patient. The patient received the dose but shows no adverse effects. Choose the THREE most appropriate actions.",
        "options": [
            "Apologize to the patient, explain the error clearly, and outline any monitoring required.",
            "Inform your supervising registrar or consultant about the prescribing error.",
            "Log the prescribing error in the hospital's incident reporting system (Datix).",
            "Say nothing to the patient since no harm was caused, to avoid causing them unnecessary anxiety.",
            "Ask the nurse who administered the medication to keep the mistake confidential.",
            "Document the corrected dose in the notes but do not mention that an error occurred.",
            "Blame the pharmacy department for not warning you about the dose limits.",
            "File a formal complaint against the nurse for administering the medication without questioning it."
        ],
        "correct_answers": [0, 1, 2],
        "explanation": "GMC's duty of candour requires open and honest disclosure of errors to patients, even if no harm is caused. Informing seniors is essential for patient monitoring. Logging on Datix ensures systemic analysis. Hiding errors, blaming others, or punishing colleagues is unprofessional and violates duty of candour."
    },
    # 4. Confused Patient Wandering
    {
        "scenario": "You are working on the {dept} and notice a confused patient, {patient_name}, who is dressed in their coat and attempting to leave the ward unsupervised, stating they need to go to {destination}. Choose the THREE most appropriate actions.",
        "options": [
            "Approach the patient calmly, introduce yourself, and gently guide them back to a comfortable seating area on the ward.",
            "Perform a rapid assessment of the patient's mental capacity and review their current medical status for acute delirium.",
            "Inform the nurse in charge of the ward so that a supervising staff member or family contact can be arranged.",
            "Physically restrain the patient to prevent them from walking out of the ward entrance.",
            "Lock the ward doors permanently to prevent any patient from leaving the ward.",
            "Administer a rapid chemical sedative injection without clinical assessment to keep them quiet.",
            "Ignore the patient, assuming they have the right to leave since they are dressed to go.",
            "Call security immediately to have the patient arrested and escorted to a police cell."
        ],
        "correct_answers": [0, 1, 2],
        "explanation": "Gently guiding the patient and de-escalating is the safest immediate action. Assessing capacity and checking for acute delirium (medical causes) is crucial. Coordinating with nursing staff ensures ongoing safety. Unjustified restraint, locking doors, or sedating without assessment are illegal/unsafe. Ignoring the patient violates duty of care."
    },
    # 5. Conflicting Senior Instructions
    {
        "scenario": "You are a {role_me} in the {dept}. The registrar tells you to start a patient on {treatment_regimen_a}, but later, the consultant tells you to start them on {treatment_regimen_b} instead. Choose the THREE most appropriate actions.",
        "options": [
            "Speak to the registrar privately to clarify the treatment plan and mention the consultant's conflicting instruction.",
            "Discuss the discrepancy with the consultant if the registrar is unreachable or insists on their plan.",
            "Document the final agreed treatment plan and the rationale behind it clearly in the medical records.",
            "Implement the registrar's plan because they are your immediate supervisor and you work with them daily.",
            "Implement the consultant's plan without telling the registrar to avoid conflict.",
            "Implement both treatment plans simultaneously to ensure all instructions are followed.",
            "Complain to the patient about the lack of communication within the senior medical team.",
            "Ignore both instructions and wait until the next ward round for clarification."
        ],
        "correct_answers": [0, 1, 2],
        "explanation": "Clear communication within the team is vital. Clarifying with the registrar directly maintains professional relationships. If discrepancies persist, consult the consultant (who has ultimate clinical responsibility). Documenting the final plan is essential. Implementing conflicting plans, complaining to the patient, or taking unilateral action without discussion is unsafe."
    },
    # 6. Colleague Repeated Sickness
    {
        "scenario": "A fellow junior doctor, {colleague_name}, has called in sick at short notice for the {sick_count} time this month, leaving the {dept} severely short-staffed and the remaining team under extreme pressure. Choose the THREE most appropriate actions.",
        "options": [
            "Speak to {colleague_name} privately when they return to check on their welfare and see if they need support.",
            "Inform the clinical lead or rota coordinator about the staffing difficulties and increased workload pressure.",
            "Work with the remaining ward team to prioritize clinical tasks and ensure patient safety is maintained.",
            "Complain about {colleague_name}'s frequent absences to other staff members in the hospital canteen.",
            "Refuse to perform any tasks beyond your normal workload, leaving shifts short-staffed.",
            "Try to complete all routine and non-urgent tasks yourself without escalating the staffing issues.",
            "Send an angry text message to {colleague_name} demanding to know why they are absent.",
            "Leave the ward early as a protest against the poor working conditions."
        ],
        "correct_answers": [0, 1, 2],
        "explanation": "Supporting colleague welfare is a professional duty. Escalating rota gaps is necessary for clinical safety management. Prioritizing clinical tasks with the team ensures immediate patient safety. Gossiping, refusing work, sending hostile messages, or walking away compromise patient care and are unprofessional."
    },
    # 7. Patient Requesting Access to Notes
    {
        "scenario": "A patient, {patient_name}, admitted to the {dept} demands that you immediately print and hand over all of their medical records and clinical notes. Choose the THREE most appropriate actions.",
        "options": [
            "Explain the hospital's formal process for accessing health records (under GDPR/Subject Access Request).",
            "Inform the ward manager or patient experience team of the patient's request to assist with the process.",
            "Document the patient's request and your discussion in their medical records.",
            "Hand over the patient's paper chart directly to them to take home.",
            "Log into the clinical portal, print out all notes, and hand them to the patient immediately.",
            "Refuse the request flatly and tell the patient they have no right to see their notes.",
            "Tell the patient's relatives that the patient is acting suspiciously by demanding their records.",
            "Suggest that the patient hire a lawyer to obtain their records."
        ],
        "correct_answers": [0, 1, 2],
        "explanation": "Patients have a legal right to access records, but it must be done through formal channels (SAR/GDPR) to ensure data verification and protection (e.g. redacting third-party data). Involving ward managers helps coordinate this. Documenting the request is good practice. Uncontrolled printing or flat refusal violate safety and legal guidelines."
    }
]

NEW_PD_SELECTION_VARS = [
    # 1. Colleague Bullying/Harassment
    [
        {"role_me": "foundation doctor", "dept": "Geriatric Ward", "senior_name": "Dr. Sterling (the consultant)", "junior_role": "the nursing student", "senior_role": "Dr. Sterling"},
        {"role_me": "F2 doctor", "dept": "Emergency Department", "senior_name": "Dr. Vance (the senior registrar)", "junior_role": "the medical student", "senior_role": "Dr. Vance"},
        {"role_me": "FY1 doctor", "dept": "Acute Medical Unit", "senior_name": "Dr. Korda (the consultant)", "junior_role": "the junior pharmacist", "senior_role": "Dr. Korda"},
        {"role_me": "SHO", "dept": "Surgical Assessment Unit", "senior_name": "Mr. Black (the consultant surgeon)", "junior_role": "the F1 doctor", "senior_role": "Mr. Black"},
        {"role_me": "FY1 doctor", "dept": "Paediatric Ward", "senior_name": "Dr. Thorne (the clinical lead)", "junior_role": "the ward clerk", "senior_role": "Dr. Thorne"}
    ],
    # 2. Suspected Elder Abuse
    [
        {"patient_name": "Mrs. Ethel G.", "dept": "Geriatric Ward", "injury_type": "deep laceration on her wrist"},
        {"patient_name": "Mr. Arthur P.", "dept": "Emergency Department", "injury_type": "bruise on his upper arm"},
        {"patient_name": "Mrs. Beatrice S.", "dept": "Acute Medical Unit", "injury_type": "skin tear on her shoulder"},
        {"patient_name": "Mr. Harold M.", "dept": "Surgical Assessment Unit", "injury_type": "hematoma on his forehead"},
        {"patient_name": "Mrs. Florence C.", "dept": "Medical Ward", "injury_type": "fractured clavicle"}
    ],
    # 3. Disclosing Medical Error
    [
        {"role_me": "foundation doctor", "dept": "Geriatric Ward", "medication": "anti-hypertensive medication"},
        {"role_me": "F2 doctor", "dept": "Emergency Department", "medication": "intravenous paracetamol"},
        {"role_me": "FY1 doctor", "dept": "Acute Medical Unit", "medication": "daily low molecular weight heparin"},
        {"role_me": "SHO", "dept": "Surgical Assessment Unit", "medication": "post-operative antibiotic"},
        {"role_me": "FY1 doctor", "dept": "Paediatric Ward", "medication": "oral liquid ibuprofen"}
    ],
    # 4. Confused Patient Wandering
    [
        {"patient_name": "Mr. Thomas", "dept": "Elderly Care Ward", "destination": "the local post office"},
        {"patient_name": "Mrs. Davies", "dept": "Acute Medical Unit", "destination": "her childhood home"},
        {"patient_name": "Mr. Jackson", "dept": "Stroke Rehabilitation Ward", "destination": "his former workplace"},
        {"patient_name": "Mrs. Higgins", "dept": "Surgical Ward", "destination": "the supermarket to buy milk"},
        {"patient_name": "Mr. Kelly", "dept": "Cardiology Ward", "destination": "feed his pet dog at home"}
    ],
    # 5. Conflicting Senior Instructions
    [
        {"role_me": "foundation doctor", "dept": "Geriatric Ward", "treatment_regimen_a": "oral anticoagulation", "treatment_regimen_b": "antiplatelet therapy alone"},
        {"role_me": "F2 doctor", "dept": "Emergency Department", "treatment_regimen_a": "intravenous fluid restriction", "treatment_regimen_b": "an active fluid bolus"},
        {"role_me": "FY1 doctor", "dept": "Acute Medical Unit", "treatment_regimen_a": "high-dose oral steroids", "treatment_regimen_b": "intravenous antibiotic coverage"},
        {"role_me": "SHO", "dept": "Surgical Assessment Unit", "treatment_regimen_a": "conservative management", "treatment_regimen_b": "emergency surgical exploration"},
        {"role_me": "FY1 doctor", "dept": "Paediatric Ward", "treatment_regimen_a": "oral rehydration therapy", "treatment_regimen_b": "intravenous saline fluids"}
    ],
    # 6. Colleague Repeated Sickness
    [
        {"colleague_name": "Dr. Sarah", "sick_count": "third", "dept": "General Medical Ward"},
        {"colleague_name": "Dr. Ahmed", "sick_count": "fourth", "dept": "Busy AMU"},
        {"colleague_name": "Dr. Jess", "sick_count": "third", "dept": "Surgical Ward"},
        {"colleague_name": "Dr. Leo", "sick_count": "fifth", "dept": "Emergency Department"},
        {"colleague_name": "Dr. Emma", "sick_count": "fourth", "dept": "Paediatric Ward"}
    ],
    # 7. Patient Requesting Access to Notes
    [
        {"patient_name": "Mr. Watson", "dept": "Respiratory Ward"},
        {"patient_name": "Mrs. Holmes", "dept": "Cardiology Ward"},
        {"patient_name": "Mr. Smith", "dept": "Gastroenterology Ward"},
        {"patient_name": "Mrs. Jones", "dept": "Orthopaedic Ward"},
        {"patient_name": "Mr. Brown", "dept": "Endocrine Unit"}
    ]
]
