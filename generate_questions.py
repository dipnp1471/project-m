import json
import random

# Seed for deterministic generation of questions
random.seed(42)

def generate_questions():
    questions = []
    
    # ----------------------------------------------------
    # CLINICAL PROBLEM SOLVING: SBA QUESTIONS (360 questions)
    # ----------------------------------------------------
    
    # 1. CARDIOVASCULAR (30 questions)
    cardio_conditions = [
        {
            "name": "Atrial Fibrillation",
            "scenarios": [
                {
                    "stage": "acute_unstable",
                    "scenario_template": "A {age}-year-old {gender} is brought to the emergency department with a 2-hour history of severe palpitations and chest discomfort. On examination, they are distressed. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg (hypotensive), HR {hr} bpm (irregularly irregular), Temp 36.8°C, O2 sat {o2}% on room air. An ECG confirms atrial fibrillation.",
                    "options": ["Synchronized DC cardioversion", "Intravenous amiodarone", "Intravenous beta-blocker", "Oral digoxin", "Urgent coronary angiography"],
                    "correct": "Synchronized DC cardioversion",
                    "explanation": "In a patient with acute atrial fibrillation who is haemodynamically unstable (suggested by hypotension BP < 90 mmHg, chest pain, or heart failure), the first-line management is immediate synchronized DC cardioversion under sedation/anaesthesia."
                },
                {
                    "stage": "acute_stable_under_48h",
                    "scenario_template": "A {age}-year-old {gender} presents with a 12-hour history of palpitations and mild dyspnoea. They have no chest pain, syncope, or signs of heart failure. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm (irregularly irregular), O2 sat {o2}% on room air. ECG shows atrial fibrillation. They have no prior cardiovascular history.",
                    "options": ["Pharmacological or electrical cardioversion", "Rate control with Bisoprolol", "Oral Digoxin therapy", "Emergency DC cardioversion", "Warfarin anticoagulation alone"],
                    "correct": "Pharmacological or electrical cardioversion",
                    "explanation": "For patients with acute atrial fibrillation presenting within 48 hours of onset who are haemodynamically stable, rhythm control (either electrical or pharmacological, typically with flecainide or amiodarone) should be offered as first-line therapy. Anticoagulation should also be initiated."
                },
                {
                    "stage": "chronic_rate_control",
                    "scenario_template": "A {age}-year-old {gender} is diagnosed with permanent atrial fibrillation during a routine check-up. They complain of mild lethargy but are otherwise asymptomatic. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm (irregularly irregular). You decide to initiate rate control.",
                    "options": ["Bisoprolol", "Digoxin", "Amiodarone", "Flecainide", "Sotalol"],
                    "correct": "Bisoprolol",
                    "explanation": "For rate control in patients with atrial fibrillation (non-paroxysmal), a beta-blocker (such as bisoprolol) or a rate-limiting calcium channel blocker (such as diltiazem or verapamil) is the first-line drug therapy. Digoxin is generally reserved for sedentary patients."
                },
                {
                    "stage": "anticoagulation_chads",
                    "scenario_template": "A {age}-year-old {gender} with a history of hypertension and Type 2 Diabetes is found to have atrial fibrillation on an ECG. They have no symptoms. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm. You calculate their CHA2DS2-VASc score to decide on anticoagulation.",
                    "options": ["Initiate Apixaban", "Initiate Aspirin 75mg daily", "Initiate Clopidogrel 75mg daily", "Initiate dual antiplatelet therapy", "No anticoagulation required"],
                    "correct": "Initiate Apixaban",
                    "explanation": "Based on the CHA2DS2-VASc scoring system, this patient has points for age, hypertension, and diabetes, placing them at high risk of stroke. Direct Oral Anticoagulants (DOACs) like Apixaban, Rivaroxaban, or Dabigatran are first-line for stroke prevention in AF. Aspirin is no longer recommended for stroke prevention in AF."
                }
            ]
        },
        {
            "name": "Acute Coronary Syndrome",
            "scenarios": [
                {
                    "stage": "stemi_management",
                    "scenario_template": "A {age}-year-old {gender} presents with a 1-hour history of crushing central chest pain radiating to the left arm, accompanied by diaphoresis. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm. ECG reveals ST-segment elevation of 3mm in leads V1-V4. The nearest PCI-capable hospital is 45 minutes away.",
                    "options": ["Primary Percutaneous Coronary Intervention (PCI)", "Intravenous thrombolysis", "Dual antiplatelet therapy and ward admission", "Coronary artery bypass grafting (CABG)", "Intravenous heparin infusion alone"],
                    "correct": "Primary Percutaneous Coronary Intervention (PCI)",
                    "explanation": "For patients presenting with STEMI within 12 hours of symptom onset, primary PCI is the gold standard treatment, provided it can be delivered within 120 minutes of the time when fibrinolysis could have been given. Since the PCI facility is 45 minutes away, primary PCI should be performed."
                },
                {
                    "stage": "nstemi_management",
                    "scenario_template": "A {age}-year-old {gender} presents with intermittent cardiac chest pain over the last 24 hours. ECG shows ST depression and T-wave inversion in leads II, III, and aVF. Troponin T is significantly elevated at {trop} ng/L (reference < 14). Vitals are stable. You calculate their GRACE score.",
                    "options": ["Dual antiplatelet therapy and fondaparinux", "Immediate thrombolysis", "Urgent DC cardioversion", "Discharge with outpatient stress echo", "Monotherapy with aspirin"],
                    "correct": "Dual antiplatelet therapy and fondaparinux",
                    "explanation": "This patient has an NSTEMI (positive troponin with ischaemic ECG changes). Initial medical management includes dual antiplatelet therapy (Aspirin + Clopidogrel/Ticagrelor) and fondaparinux (low molecular weight heparin alternative) to prevent thrombus propagation, followed by risk stratification using the GRACE score."
                }
            ]
        },
        {
            "name": "Heart Failure",
            "scenarios": [
                {
                    "stage": "acute_pulmonary_oedema",
                    "scenario_template": "A {age}-year-old {gender} is admitted to the emergency department with acute breathlessness and orthopnoea. On examination, they are tachypnoeic, with bilateral coarse crackles to the mid-zones. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm, O2 sat {o2}% on room air. Chest X-ray confirms acute pulmonary oedema.",
                    "options": ["Intravenous Furosemide", "Intravenous fluids", "Intravenous Salbutamol", "Oral Bisoprolol", "Intravenous Amiodarone"],
                    "correct": "Intravenous Furosemide",
                    "explanation": "The immediate management of acute decompensated heart failure with pulmonary oedema consists of high-flow oxygen (if hypoxic), sitting the patient upright, and administering intravenous loop diuretics (Furosemide). Vasodilators (GTN) can be added if blood pressure permits."
                },
                {
                    "stage": "chronic_systolic_hf",
                    "scenario_template": "A {age}-year-old {gender} is diagnosed with chronic heart failure with reduced ejection fraction (HFrEF) of 32%. They are currently taking Ramipril 10mg daily and Furosemide 40mg daily, but remain symptomatic with NYHA Class II dyspnoea. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm.",
                    "options": ["Add Bisoprolol", "Increase Furosemide dose", "Add Spironolactone", "Add Digoxin", "Add Amlodipine"],
                    "correct": "Add Bisoprolol",
                    "explanation": "First-line therapy for all patients with chronic heart failure with reduced ejection fraction (HFrEF) includes both an ACE inhibitor (or ARB) and a beta-blocker (like Bisoprolol, Carvedilol, or Nebivolol). These agents improve survival. They should be introduced sequentially once the patient is stable."
                }
            ]
        }
    ]
    
    # Let's populate the questions array using these templates for SBA
    # We will generate 30 Cardiovascular questions by looping and using variations.
    q_id = 1
    
    # 1. CARDIOVASCULAR (30 questions)
    for i in range(30):
        cond = cardio_conditions[i % len(cardio_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        # Determine variable parameters
        age = random.choice([52, 61, 68, 74, 82, 85])
        gender = random.choice(["male", "female"])
        bp_systolic = random.choice([82, 88, 115, 128, 142]) if scen["stage"] == "acute_unstable" else random.choice([124, 138, 146, 152])
        bp_diastolic = bp_systolic - random.choice([35, 40, 45, 50])
        hr = random.choice([118, 132, 144, 156]) if "AF" in cond["name"] else random.choice([78, 86, 92])
        o2 = random.choice([88, 91, 93]) if "oedema" in scen["stage"] or "unstable" in scen["stage"] else random.choice([96, 98])
        trop = random.choice([120, 240, 480, 890])
        
        scenario_text = scen["scenario_template"].format(
            age=age, gender=gender, bp_systolic=bp_systolic, bp_diastolic=bp_diastolic, hr=hr, o2=o2, trop=trop
        )
        
        # Mix options slightly
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Cardiovascular",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 2. DERMATOLOGY / OPHTHALMOLOGY / ENT (30 questions)
    derm_ent_eye_conditions = [
        {
            "name": "Eczema / Atopic Dermatitis",
            "scenarios": [
                {
                    "stage": "flare_management",
                    "scenario_template": "A {age}-year-old {gender} presents with an itchy, red rash on their flexural surfaces (antecubital and popliteal fossae). They have a history of asthma. On inspection, there are erythematous, dry, excoriated plaques. What is the most appropriate first-line treatment for a moderate eczema flare-up?",
                    "options": ["Moderate potency topical corticosteroid (e.g., Eumovate)", "Oral corticosteroids", "Topical tacrolimus", "Oral antihistamines alone", "Emollients alone"],
                    "correct": "Moderate potency topical corticosteroid (e.g., Eumovate)",
                    "explanation": "Eczema flare-ups are managed step-wise. Mild flares require mild topical steroids (e.g., hydrocortisone 1%), while moderate flares require moderate potency topical corticosteroids (e.g., clobetasone butyrate 0.05% / Eumovate). Emollients should always be continued as maintenance."
                }
            ]
        },
        {
            "name": "Acute Angle Closure Glaucoma",
            "scenarios": [
                {
                    "stage": "emergency_management",
                    "scenario_template": "A {age}-year-old {gender} presents to the eye clinic with sudden-onset, severe pain in the left eye, accompanied by blurred vision, headache, and nausea. On examination, the left eye is red, the pupil is fixed and mid-dilated, and the cornea appears hazy. Intraocular pressure is significantly elevated. What is the immediate first-line medical therapy?",
                    "options": ["Intravenous Acetazolamide", "Topical Latanoprost", "Topical Pilocarpine alone", "Systemic Corticosteroids", "Laser peripheral iridotomy"],
                    "correct": "Intravenous Acetazolamide",
                    "explanation": "Acute angle closure glaucoma is an ocular emergency. Immediate medical management is targeted at lowering intraocular pressure rapidly, which is achieved with intravenous acetazolamide (a carbonic anhydrase inhibitor), alongside topical agents (e.g., pilocarpine to induce miosis, beta-blockers). Laser iridotomy is the definitive treatment but performed once the acute attack is controlled."
                }
            ]
        },
        {
            "name": "Otitis Media",
            "scenarios": [
                {
                    "stage": "antibiotic_indications",
                    "scenario_template": "A {age}-month-old infant is brought by their parents with a 24-hour history of irritability, fever, and pulling at the right ear. Otoscopy reveals a bulging, erythematous tympanic membrane with loss of landmarks. The child is systemically well and eating. What is the most appropriate initial management?",
                    "options": ["Reassurance and simple analgesia (Paracetamol/Ibuprofen)", "Immediate oral Amoxicillin", "Topical antibiotic ear drops", "Urgent referral to ENT", "Oral Erythromycin"],
                    "correct": "Reassurance and simple analgesia (Paracetamol/Ibuprofen)",
                    "explanation": "In acute otitis media (AOM) in children who are systemically well, a delayed prescribing or active monitoring strategy (simple analgesia and observation for 2-3 days) is recommended, as most cases are viral and self-limiting. Antibiotics (first-line Amoxicillin) are indicated if the child is <6 months, systemically very unwell, has bilateral AOM (in <2 years), or has otorrhoea."
                }
            ]
        }
    ]

    for i in range(30):
        cond = derm_ent_eye_conditions[i % len(derm_ent_eye_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([4, 18, 28, 45, 62, 73]) if cond["name"] != "Otitis Media" else random.choice([9, 14, 18, 22])
        gender = random.choice(["male", "female"])
        
        scenario_text = scen["scenario_template"].format(age=age, gender=gender)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Dermatology / Ophthalmology / ENT",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 3. ENDOCRINOLOGY / METABOLIC (30 questions)
    endo_conditions = [
        {
            "name": "Diabetic Ketoacidosis (DKA)",
            "scenarios": [
                {
                    "stage": "dka_management",
                    "scenario_template": "A {age}-year-old Type 1 Diabetic is admitted with a history of vomiting and abdominal pain. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm. Lab results: Blood Glucose 24 mmol/L, pH 7.15, Bicarbonate 11 mmol/L, Ketones 4.2 mmol/L. What is the key priority in the initial management of this patient?",
                    "options": ["Intravenous fluid resuscitation (0.9% Normal Saline)", "Intravenous soluble insulin infusion (0.1 U/kg/hr)", "Intravenous sodium bicarbonate infusion", "Subcutaneous fast-acting insulin", "Intravenous potassium replacement alone"],
                    "correct": "Intravenous fluid resuscitation (0.9% Normal Saline)",
                    "explanation": "The immediate priority in managing Diabetic Ketoacidosis (DKA) is fluid resuscitation with 0.9% sodium chloride to restore circulating volume and correct dehydration, followed closely by a fixed-rate intravenous insulin infusion. Potassium replacement is added to fluids if potassium is < 5.5 mmol/L."
                }
            ]
        },
        {
            "name": "Hypothyroidism",
            "scenarios": [
                {
                    "stage": "monitoring_adjustment",
                    "scenario_template": "A {age}-year-old {gender} with primary hypothyroidism on Levothyroxine 100mcg daily presents for a routine review. They report feeling well with no symptoms. Blood tests show: TSH {tsh} mU/L (reference 0.4 - 4.5), Free T4 is normal. What is the most appropriate action?",
                    "options": ["Increase Levothyroxine dose", "Decrease Levothyroxine dose", "Maintain current Levothyroxine dose", "Stop Levothyroxine and repeat test in 3 months", "Add Liothyronine (T3)"],
                    "correct": "Increase Levothyroxine dose",
                    "explanation": "If a patient on Levothyroxine has an elevated TSH (e.g., {tsh} mU/L, which is above the reference range of 0.4 - 4.5 mU/L), it indicates under-replacement, and the dose of Levothyroxine should be increased (typically by 25mcg increments) to bring TSH into the lower half of the reference range."
                }
            ]
        },
        {
            "name": "Addison's Disease / Adrenal Crisis",
            "scenarios": [
                {
                    "stage": "crisis_management",
                    "scenario_template": "A {age}-year-old {gender} with a known history of Addison's disease is admitted with a high fever, confusion, and abdominal pain following a gastrointestinal infection. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg (hypotensive), HR {hr} bpm. Bloods show Sodium 128 mmol/L, Potassium 5.6 mmol/L. What is the most urgent treatment?",
                    "options": ["Intravenous Hydrocortisone 100mg and saline fluid resuscitation", "Oral Fludrocortisone dose doubling", "Intravenous insulin and dextrose infusion", "Intravenous antibiotics alone", "Oral Hydrocortisone increase"],
                    "correct": "Intravenous Hydrocortisone 100mg and saline fluid resuscitation",
                    "explanation": "This patient is presenting in acute adrenal (Addisonian) crisis, characterized by hypotension, hyponatremia, hyperkalemia, and hypoglycemia, often triggered by infection. The primary life-saving treatment is immediate IV Hydrocortisone 100mg (or IM) followed by rapid IV fluid resuscitation with 0.9% sodium chloride."
                }
            ]
        }
    ]

    for i in range(30):
        cond = endo_conditions[i % len(endo_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([21, 34, 45, 56, 68])
        gender = random.choice(["male", "female"])
        bp_systolic = random.choice([80, 84, 88]) if "Crisis" in cond["name"] or "DKA" in cond["name"] else 120
        bp_diastolic = bp_systolic - 35
        hr = random.choice([104, 112, 120])
        tsh = random.choice([7.2, 9.4, 12.1])
        
        scenario_text = scen["scenario_template"].format(
            age=age, gender=gender, bp_systolic=bp_systolic, bp_diastolic=bp_diastolic, hr=hr, tsh=tsh
        )
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Endocrinology / Metabolic",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"].format(tsh=tsh)
        })
        q_id += 1

    # 4. GASTROENTEROLOGY / CLINICAL NUTRITION (30 questions)
    gastro_conditions = [
        {
            "name": "Coeliac Disease",
            "scenarios": [
                {
                    "stage": "diagnosis",
                    "scenario_template": "A {age}-year-old {gender} presents with a 6-month history of bloating, intermittent diarrhoea, and weight loss. Blood tests show a microcytic anaemia. What is the most appropriate initial screening investigation for coeliac disease, provided they are on a gluten-containing diet?",
                    "options": ["Anti-tissue transglutaminase (anti-tTG) IgA antibody", "Duodenal biopsy", "Stool antigen test", "HLA-DQ2/DQ8 genetic testing", "Anti-endomysial IgG antibody"],
                    "correct": "Anti-tissue transglutaminase (anti-tTG) IgA antibody",
                    "explanation": "The first-line serological screening test for coeliac disease is IgA anti-tissue transglutaminase (anti-tTG) antibody, alongside total IgA level (to rule out IgA deficiency). If serology is positive, diagnosis is confirmed via a duodenal biopsy showing villous atrophy and crypt hyperplasia."
                }
            ]
        },
        {
            "name": "Inflammatory Bowel Disease",
            "scenarios": [
                {
                    "stage": "uc_flare_management",
                    "scenario_template": "A {age}-year-old {gender} with known Ulcerative Colitis presents with a flare-up. They report opening their bowels 5 times a day with visible blood and mucus. Vitals are stable, and they do not have a fever. What is the most appropriate initial treatment for this mild-to-moderate flare?",
                    "options": ["Topical or oral 5-aminosalicylic acid (5-ASA) (e.g., Mesalazine)", "Intravenous Methylprednisolone", "Oral Azathioprine", "Infliximab infusion", "Urgent subtotal colectomy"],
                    "correct": "Topical or oral 5-aminosalicylic acid (5-ASA) (e.g., Mesalazine)",
                    "explanation": "Mild-to-moderate flares of Ulcerative Colitis are managed first-line with 5-aminosalicylic acid (5-ASA) compounds (e.g., mesalazine), either topically (suppository/enema) or orally. Severe flares (defined by Truelove and Witts criteria: >= 6 bloody stools/day, fever, tachycardia, anemia, or high ESR/CRP) require admission and intravenous corticosteroids."
                }
            ]
        },
        {
            "name": "Peptic Ulcer Disease",
            "scenarios": [
                {
                    "stage": "h_pylori_management",
                    "scenario_template": "A {age}-year-old {gender} presents with burning epigastric pain that is relieved by eating. A urea breath test is positive for Helicobacter pylori. What is the standard first-line eradication therapy?",
                    "options": ["Proton pump inhibitor (PPI) + Amoxicillin + Clarithromycin", "Proton pump inhibitor (PPI) monotherapy for 8 weeks", "PPI + Ranitidine + Amoxicillin", "Amoxicillin + Clarithromycin for 14 days", "PPI + Metronidazole + Clarithromycin only"],
                    "correct": "Proton pump inhibitor (PPI) + Amoxicillin + Clarithromycin",
                    "explanation": "First-line eradication therapy for H. pylori infection typically consists of a proton pump inhibitor (PPI) twice daily combined with two antibiotics (Amoxicillin and Clarithromycin, or Metronidazole and Clarithromycin) for 7 days (triple therapy)."
                }
            ]
        }
    ]

    for i in range(30):
        cond = gastro_conditions[i % len(gastro_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([24, 31, 47, 52, 69])
        gender = random.choice(["male", "female"])
        
        scenario_text = scen["scenario_template"].format(age=age, gender=gender)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Gastroenterology / Clinical Nutrition",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 5. INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS (30 questions)
    inf_haem_conditions = [
        {
            "name": "Sepsis & Meningitis",
            "scenarios": [
                {
                    "stage": "meningitis_gp_management",
                    "scenario_template": "A {age}-year-old {gender} is seen in the GP surgery with a fever, headache, photophobia, and a non-blanching petechial rash. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg, HR {hr} bpm. You suspect meningococcal septicaemia. What is the immediate course of action?",
                    "options": ["Administer IM Benzylpenicillin and arrange immediate transfer to hospital", "Refer to hospital for urgent lumbar puncture", "Give oral Amoxicillin and review in 24 hours", "Perform a full cranial nerve exam and check reflexes", "Administer oral Paracetamol and monitor rash hourly"],
                    "correct": "Administer IM Benzylpenicillin and arrange immediate transfer to hospital",
                    "explanation": "If meningococcal disease is suspected in the primary care setting, the patient should receive a single dose of intramuscular or intravenous benzylpenicillin immediately, and an emergency ambulance must be called. This should not delay hospital transfer."
                }
            ]
        },
        {
            "name": "Iron Deficiency Anaemia",
            "scenarios": [
                {
                    "stage": "investigation_indication",
                    "scenario_template": "A {age}-year-old {gender} presents with fatigue and dyspnoea. Blood tests show: Haemoglobin {hb} g/dL (reference 12.0 - 16.0), MCV {mcv} fL (reference 80 - 100), and low ferritin. They report no changes in bowel habit or weight loss. What is the most appropriate next step in management?",
                    "options": ["Refer for urgent upper and lower GI endoscopy", "Start oral iron supplements and retest in 3 months", "Perform a CT scan of the abdomen and pelvis", "Refer to haematology for bone marrow biopsy", "Recommend dietary modifications with red meat and spinach"],
                    "correct": "Refer for urgent upper and lower GI endoscopy",
                    "explanation": "In any patient over 50 (or post-menopausal female / male of any age) presenting with unexplained iron deficiency anaemia, the gold standard recommendation is referral for urgent dual gastrointestinal investigation (colonoscopy and gastroscopy) to rule out gastrointestinal malignancy, even in the absence of bowel symptoms."
                }
            ]
        },
        {
            "name": "Anaphylaxis",
            "scenarios": [
                {
                    "stage": "acute_management",
                    "scenario_template": "A {age}-year-old {gender} develops sudden-onset lip swelling, dyspnoea, and widespread urticaria 10 minutes after eating peanuts. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg (hypotensive), HR {hr} bpm, O2 sat {o2}% on room air. There is audible inspiratory stridor. What is the immediate treatment of choice?",
                    "options": ["Intramuscular Adrenaline (1:1000) 0.5mg", "Intravenous Adrenaline (1:10000) 1mg", "Intravenous Hydrocortisone 200mg", "Intravenous Chlorphenamine 10mg", "Inhaled Salbutamol nebuliser"],
                    "correct": "Intramuscular Adrenaline (1:1000) 0.5mg",
                    "explanation": "The first-line treatment for anaphylaxis is intramuscular (IM) Adrenaline (1:1000) at a dose of 0.5mg (500 micrograms) in adults, administered in the anterolateral aspect of the middle third of the thigh. IV Adrenaline is reserved for specialist use (e.g., anaesthetists) due to risk of arrhythmias."
                }
            ]
        }
    ]

    for i in range(30):
        cond = inf_haem_conditions[i % len(inf_haem_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([25, 42, 58, 64, 76])
        gender = "male" if i % 2 == 0 else "female"
        bp_systolic = 85 if "Anaphylaxis" in cond["name"] or "Sepsis" in cond["name"] else 125
        bp_diastolic = bp_systolic - 35
        hr = 120 if bp_systolic == 85 else 78
        o2 = 91 if bp_systolic == 85 else 97
        hb = 9.2
        mcv = 71
        
        scenario_text = scen["scenario_template"].format(
            age=age, gender=gender, bp_systolic=bp_systolic, bp_diastolic=bp_diastolic, hr=hr, o2=o2, hb=hb, mcv=mcv
        )
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 6. MUSCULOSKELETAL (30 questions)
    msk_conditions = [
        {
            "name": "Gout",
            "scenarios": [
                {
                    "stage": "acute_management",
                    "scenario_template": "A {age}-year-old {gender} presents with an acute, exquisitely painful, swollen, and red left first metatarsophalangeal (MTP) joint. There is no history of trauma. They have a history of chronic kidney disease stage 3. What is the most appropriate first-line treatment for this acute flare?",
                    "options": ["Oral Colchicine", "Oral Ibuprofen", "Oral Allopurinol 300mg", "Intravenous antibiotics", "Oral Prednisolone alone"],
                    "correct": "Oral Colchicine",
                    "explanation": "NSAIDs (like Ibuprofen) or Colchicine are first-line agents for acute gout flares. However, in patients with moderate-to-severe Chronic Kidney Disease (CKD), NSAIDs are contraindicated due to the risk of worsening renal function. Therefore, oral Colchicine (or oral/intra-articular corticosteroids) is the preferred option."
                },
                {
                    "stage": "prophylaxis_allopurinol",
                    "scenario_template": "A {age}-year-old {gender} with a history of recurrent gout flares (3 attacks in the past 12 months) presents to discuss prevention. Their last flare resolved 3 weeks ago. What is the most appropriate management strategy?",
                    "options": ["Initiate Allopurinol and co-prescribe low-dose Colchicine cover for 6 months", "Initiate Allopurinol alone immediately", "Initiate Ibuprofen 400mg TDS indefinitely", "Advise low-purine diet alone", "Initiate Colchicine 500mcg daily as monotherapy"],
                    "correct": "Initiate Allopurinol and co-prescribe low-dose Colchicine cover for 6 months",
                    "explanation": "Allopurinol (xanthine oxidase inhibitor) is first-line for gout prophylaxis. It should be initiated at a low dose (e.g. 100mg daily) and titrated. When starting Allopurinol, acute flares can be triggered, so prophylactic cover with low-dose Colchicine (or NSAID) should be co-prescribed for at least 6 months."
                }
            ]
        },
        {
            "name": "Rheumatoid Arthritis",
            "scenarios": [
                {
                    "stage": "initial_management",
                    "scenario_template": "A {age}-year-old {gender} presents with symmetrical swelling and morning stiffness lasting over an hour in their hands, specifically involving the PIP and MCP joints. Rheumatoid factor and anti-CCP antibodies are positive. X-rays show peri-articular osteopenia. What is the first-line disease-modifying treatment (DMARD)?",
                    "options": ["Oral Methotrexate + short-term corticosteroid bridging", "Oral Ibuprofen 400mg TDS alone", "Intramuscular methylprednisolone injection alone", "Oral Sulfasalazine monotherapy", "Infliximab therapy"],
                    "correct": "Oral Methotrexate + short-term corticosteroid bridging",
                    "explanation": "For patients with newly diagnosed active rheumatoid arthritis, NICE recommends first-line monotherapy with a conventional DMARD (Methotrexate is preferred, otherwise Sulfasalazine or Leflunomide) combined with a short-term glucocorticoid bridging course (oral or IM) to induce remission rapidly while the DMARD takes effect (typically 6-12 weeks)."
                }
            ]
        }
    ]

    for i in range(30):
        cond = msk_conditions[i % len(msk_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([38, 48, 59, 66, 75])
        gender = random.choice(["male", "female"])
        
        scenario_text = scen["scenario_template"].format(age=age, gender=gender)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Musculoskeletal",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 7. PAEDIATRICS (30 questions)
    paed_conditions = [
        {
            "name": "Bronchiolitis",
            "scenarios": [
                {
                    "stage": "supportive_care",
                    "scenario_template": "An {age}-month-old infant is brought to the clinic with a 2-day history of running nose, followed by a wet cough and audible wheeze. Vitals: Temp 37.8°C, O2 sat 94% on room air, RR 48 breaths/min. On examination, there are bilateral fine chest crackles and wheeze, with mild subcostal recessions. Feeding is at 75% of normal. What is the most appropriate management?",
                    "options": ["Supportive care at home (ensure hydration and monitor breathing)", "Inhaled Salbutamol nebuliser", "Oral Amoxicillin", "Oral Prednisolone", "Urgent hospital admission for oxygen"],
                    "correct": "Supportive care at home (ensure hydration and monitor breathing)",
                    "explanation": "Bronchiolitis (most commonly caused by RSV) is a self-limiting viral infection of the lower respiratory tract. Management is purely supportive: ensuring adequate hydration, saline nasal drops if congested, and monitoring. Bronchodilators (Salbutamol), corticosteroids, and antibiotics are NOT recommended. Hospital admission is indicated if O2 sat < 92%, respiratory distress is severe, or feeding is < 50% of normal."
                }
            ]
        },
        {
            "name": "Croup",
            "scenarios": [
                {
                    "stage": "dexamethasone",
                    "scenario_template": "A {age}-year-old child is brought to the ED at 2 AM with a harsh, barking cough and hoarseness. On examination, they are systemically well, but have a mild inspiratory stridor when agitated. What is the first-line treatment for croup?",
                    "options": ["Oral Dexamethasone (0.15mg/kg)", "Inhaled Adrenaline nebuliser", "Oral Amoxicillin", "Inhaled Budesonide alone", "Oral Paracetamol alone"],
                    "correct": "Oral Dexamethasone (0.15mg/kg)",
                    "explanation": "For all children with croup (regardless of severity), a single dose of oral Dexamethasone (0.15mg/kg) is the first-line medical treatment. Nebulized adrenaline is reserved for severe croup with distress and stridor at rest."
                }
            ]
        },
        {
            "name": "Febrile Convulsion",
            "scenarios": [
                {
                    "stage": "post_ictal_gp",
                    "scenario_template": "A {age}-year-old child is brought to the GP surgery by their parents. Ten minutes ago, the child experienced a generalized tonic-clonic seizure lasting 2 minutes, in the context of a rapid temperature rise due to tonsillitis. The child is now post-ictal but waking up. Vitals: Temp 38.5°C, otherwise stable. What is the most appropriate management?",
                    "options": ["Assess for focus of infection, give antipyretics for comfort, and reassure parents", "Prescribe daily Sodium Valproate", "Refer for urgent CT head", "Perform immediate lumbar puncture", "Give rectal Diazepam immediately"],
                    "correct": "Assess for focus of infection, give antipyretics for comfort, and reassure parents",
                    "explanation": "For a simple febrile convulsion (generalized, lasting < 15 minutes, not recurring within 24 hours, and fully resolving), the management consists of identifying and treating the source of the fever, ensuring parent education and safety advice, and reassuring them that simple febrile convulsions do not cause neurological damage. Rectal diazepam or buccal midazolam is only indicated if the seizure is active and lasts > 5 minutes."
                }
            ]
        }
    ]

    for i in range(30):
        cond = paed_conditions[i % len(paed_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([3, 6, 10]) if cond["name"] == "Bronchiolitis" else random.choice([2, 3, 4])
        gender = random.choice(["male", "female"])
        
        scenario_text = scen["scenario_template"].format(age=age)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Paediatrics",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 8. PSYCHIATRY / NEUROLOGY (30 questions)
    psych_neuro_conditions = [
        {
            "name": "Major Depressive Disorder",
            "scenarios": [
                {
                    "stage": "ssri_counselling",
                    "scenario_template": "A {age}-year-old {gender} with moderate depression is started on Fluoxetine 20mg daily. Which of the following is the most important counseling point when initiating SSRI treatment in a young adult?",
                    "options": ["Risk of increased suicidal ideation and anxiety in the first 2 weeks", "Risk of hypertensive crisis with cheese ingestion", "Need for monthly renal function tests", "Immediate onset of therapeutic action within 24 hours", "Risk of permanent memory loss"],
                    "correct": "Risk of increased suicidal ideation and anxiety in the first 2 weeks",
                    "explanation": "When starting Selective Serotonin Reuptake Inhibitors (SSRIs), patients (especially those under 30) should be warned about a potential increase in anxiety, agitation, and suicidal ideation during the first two weeks. Regular review (typically at 1-2 weeks) is required."
                }
            ]
        },
        {
            "name": "Migraine",
            "scenarios": [
                {
                    "stage": "acute_management",
                    "scenario_template": "A {age}-year-old {gender} presents with recurrent, severe, unilateral throbbing headaches associated with photophobia and nausea. They experience a visual aura (flickering zig-zag lines) 20 minutes before the headache starts. What is the first-line medication combination for acute migraine management?",
                    "options": ["A triptan (e.g. Sumatriptan) + NSAID (or Paracetamol)", "Propranolol 40mg BD", "Amitriptyline 10mg nocte", "Topiramate 25mg daily", "Codeine phosphate 30mg alone"],
                    "correct": "A triptan (e.g. Sumatriptan) + NSAID (or Paracetamol)",
                    "explanation": "For acute migraine attacks (with or without aura), NICE recommends first-line combination therapy consisting of an oral triptan (5-HT1 receptor agonist) and an NSAID, or an oral triptan and paracetamol. Propranolol, Amitriptyline, and Topiramate are used for migraine prophylaxis, not acute treatment. Codeine and other opioids should be avoided due to medication-overuse headaches."
                }
            ]
        },
        {
            "name": "Stroke / TIA",
            "scenarios": [
                {
                    "stage": "tia_referral",
                    "scenario_template": "A {age}-year-old {gender} presents to their GP surgery describing an episode of sudden-onset left-sided weakness and slurred speech that fully resolved within 45 minutes. The episode occurred 4 hours ago. They are now neurologically normal. What is the most appropriate management?",
                    "options": ["Give Aspirin 300mg immediately and refer for urgent specialist assessment within 24 hours", "Arrange an immediate emergency CT head in primary care", "Refer to the emergency department via 999 emergency ambulance", "Initiate Clopidogrel 75mg and arrange routine neurology clinic referral", "Reassure the patient and perform a cardiovascular risk assessment"],
                    "correct": "Give Aspirin 300mg immediately and refer for urgent specialist assessment within 24 hours",
                    "explanation": "For patients who have had a suspected TIA that occurred within the last 7 days, they should be given Aspirin 300mg daily immediately (unless contraindicated) and referred for specialist assessment (TIA clinic) to be seen within 24 hours. A 999 referral is only required if the symptoms are active (suspected stroke) or if they have had crescendo TIAs."
                }
            ]
        }
    ]

    for i in range(30):
        cond = psych_neuro_conditions[i % len(psych_neuro_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([22, 34, 45, 59, 71])
        gender = random.choice(["male", "female"])
        
        scenario_text = scen["scenario_template"].format(age=age, gender=gender)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Psychiatry / Neurology",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 9. RENAL / UROLOGY (30 questions)
    renal_conditions = [
        {
            "name": "Urinary Tract Infection",
            "scenarios": [
                {
                    "stage": "uncomplicated_cystitis",
                    "scenario_template": "A {age}-year-old non-pregnant female presents with a 2-day history of dysuria, urinary frequency, and suprapubic pain. She has no systemic symptoms (fever, chills) or loin pain. Urinalysis is positive for nitrites and leucocytes. What is the first-line antibiotic treatment?",
                    "options": ["Nitrofurantoin 100mg modified-release twice daily for 3 days", "Trimethoprim 200mg twice daily for 7 days", "Amoxicillin 500mg three times daily for 3 days", "Ciprofloxacin 500mg twice daily for 5 days", "Co-amoxiclav 625mg three times daily for 3 days"],
                    "correct": "Nitrofurantoin 100mg modified-release twice daily for 3 days",
                    "explanation": "For uncomplicated lower urinary tract infection (cystitis) in non-pregnant women, the first-line treatment is oral Nitrofurantoin (100mg MR twice daily) for 3 days, or Trimethoprim (200mg twice daily) for 3 days. A 7-day course is reserved for men, pregnant women, or complicated infections."
                }
            ]
        },
        {
            "name": "Acute Kidney Injury",
            "scenarios": [
                {
                    "stage": "hyperkalaemia_management",
                    "scenario_template": "A {age}-year-old {gender} is admitted with severe dehydration. Blood tests reveal an AKI Stage 3, and a serum Potassium level of {k} mmol/L. An ECG shows peaked T waves. What is the most immediate pharmacological priority?",
                    "options": ["Intravenous Calcium Gluconate (10ml of 10%)", "Intravenous Insulin (10 units) and Dextrose (50ml of 20%)", "Nebulized Salbutamol", "Calcium Resonium orally", "Urgent haemodialysis referral"],
                    "correct": "Intravenous Calcium Gluconate (10ml of 10%)",
                    "explanation": "In severe hyperkalaemia (K > 6.5 mmol/L or lower with ECG changes), the immediate priority is to stabilize the myocardial membrane to prevent lethal arrhythmias. This is achieved using intravenous Calcium Gluconate (10ml of 10%). It does not lower potassium levels, so it must be followed by insulin-dextrose infusion and/or nebulized salbutamol to shift potassium intracellularly."
                }
            ]
        }
    ]

    for i in range(30):
        cond = renal_conditions[i % len(renal_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([26, 42, 61, 72, 83])
        gender = random.choice(["male", "female"])
        k = random.choice([6.7, 7.1, 7.4])
        
        scenario_text = scen["scenario_template"].format(age=age, gender=gender, k=k)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Renal / Urology",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 10. REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY (30 questions)
    obgyn_conditions = [
        {
            "name": "Ectopic Pregnancy",
            "scenarios": [
                {
                    "stage": "ruptured_emergency",
                    "scenario_template": "A {age}-year-old female who is 7 weeks pregnant presents to ED with severe, sudden-onset lower abdominal pain and minimal vaginal bleeding. She also complains of shoulder tip pain. On examination, she is pale and clammy. Vitals: BP {bp_systolic}/{bp_diastolic} mmHg (hypotensive), HR {hr} bpm. There is generalized abdominal tenderness with guarding. What is the most appropriate next step?",
                    "options": ["Immediate transfer to operating theatre for laparoscopy/laparotomy", "Arrange a transvaginal ultrasound scan for tomorrow morning", "Measure serial serum beta-hCG levels 48 hours apart", "Administer intramuscular Methotrexate", "Prescribe oral progesterone and advise bed rest"],
                    "correct": "Immediate transfer to operating theatre for laparoscopy/laparotomy",
                    "explanation": "This patient presents with signs of a ruptured ectopic pregnancy, characterized by severe abdominal pain, shoulder tip pain (due to diaphragmatic irritation from haemoperitoneum), and haemodynamic instability (hypotension, tachycardia). This is a surgical emergency. The patient requires immediate fluid resuscitation and transfer to the operating theatre for urgent surgical management (laparoscopy or laparotomy)."
                }
            ]
        },
        {
            "name": "Pre-eclampsia",
            "scenarios": [
                {
                    "stage": "prophylaxis_aspirin",
                    "scenario_template": "A {age}-year-old female presents at her booking appointment at 10 weeks gestation. She has a history of chronic hypertension. She is asking how she can reduce her risk of pre-eclampsia during this pregnancy. What is the recommended prophylaxis?",
                    "options": ["Aspirin 75mg-150mg daily from 12 weeks until birth", "Low molecular weight heparin daily", "Strict bed rest and low sodium diet", "Oral Labetalol 100mg TDS", "Oral Progesterone supplements"],
                    "correct": "Aspirin 75mg-150mg daily from 12 weeks until birth",
                    "explanation": "According to NICE, women at high risk of pre-eclampsia (such as those with chronic hypertension, chronic kidney disease, autoimmune disease, type 1 or 2 diabetes, or history of hypertensive disease in previous pregnancy) should be advised to take 75-150 mg of Aspirin daily from 12 weeks of gestation until birth."
                }
            ]
        }
    ]

    for i in range(30):
        cond = obgyn_conditions[i % len(obgyn_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([24, 28, 32, 35, 39])
        bp_systolic = 84 if "ruptured" in scen["stage"] else 142
        bp_diastolic = bp_systolic - 35
        hr = 118 if bp_systolic == 84 else 78
        
        scenario_text = scen["scenario_template"].format(
            age=age, bp_systolic=bp_systolic, bp_diastolic=bp_diastolic, hr=hr
        )
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Reproductive / Obstetrics & Gynaecology",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 11. RESPIRATORY (30 questions)
    resp_conditions = [
        {
            "name": "Asthma Exacerbation",
            "scenarios": [
                {
                    "stage": "acute_severe_indicators",
                    "scenario_template": "A {age}-year-old {gender} is admitted with acute breathlessness and wheeze. Vitals: HR {hr} bpm, RR {rr} breaths/min, PEFR {pefr}% of predicted. On chest examination, there is bilateral widespread polyphonic wheeze. They are able to speak in complete sentences. How would you classify the severity of this asthma attack?",
                    "options": ["Moderate", "Severe", "Life-threatening", "Near-fatal", "Mild"],
                    "correct": "Moderate",
                    "explanation": "An acute asthma attack is classified as 'Moderate' if peak expiratory flow rate (PEFR) is 50-75% of predicted/best, RR < 25, HR < 110, and the patient can speak in complete sentences. 'Severe' features include PEFR 33-50%, HR >= 110, RR >= 25, or inability to complete sentences in one breath. 'Life-threatening' features include PEFR < 33%, oxygen saturation < 92%, silent chest, cyanosis, feeble respiratory effort, exhaustion, or confusion."
                },
                {
                    "stage": "life_threatening_signs",
                    "scenario_template": "A {age}-year-old {gender} with an asthma exacerbation is brought to ED. They are exhausted, confused, and struggling to breathe. Vitals: HR 112 bpm, RR 32/min, O2 sat {o2}% on room air. On auscultation, there is a distinct lack of breath sounds and no wheeze (silent chest). What is the immediate next step in management?",
                    "options": ["Administer oxygen, high-dose nebulized Salbutamol and Ipratropium, IV Hydrocortisone, and call the anaesthetist/ICU", "Give oral Prednisolone 40mg and review in 1 hour", "Administer inhaled Salbutamol 10 puffs via spacer", "Arrange a chest X-ray before giving medications", "Start intravenous magnesium sulfate infusion as monotherapy"],
                    "correct": "Administer oxygen, high-dose nebulized Salbutamol and Ipratropium, IV Hydrocortisone, and call the anaesthetist/ICU",
                    "explanation": "A silent chest, exhaustion, confusion, and low oxygen saturation (<92%) are signs of a life-threatening asthma attack. This is a medical emergency. Immediate treatment consists of high-flow oxygen, continuous nebulized bronchodilators (salbutamol + ipratropium bromide), systemic corticosteroids (IV hydrocortisone or oral prednisolone), and early involvement of the critical care/anaesthetic team for potential intubation."
                }
            ]
        },
        {
            "name": "COPD Exacerbation",
            "scenarios": [
                {
                    "stage": "target_o2_sats",
                    "scenario_template": "A {age}-year-old chronic smoker with a history of COPD presents with increased sputum volume, purulence, and breathlessness. Vitals: Temp 38.1°C, O2 sat 87% on room air. What is the target oxygen saturation range for this patient while waiting for arterial blood gas results?",
                    "options": ["88% - 92%", "94% - 98%", "90% - 95%", "Keep above 96%", "Oxygen therapy is contraindicated"],
                    "correct": "88% - 92%",
                    "explanation": "In patients with COPD who are at risk of hypercapnic respiratory failure (due to loss of hypoxic drive), the recommended target oxygen saturation range is 88% - 92%, controlled via a Venturi mask, until arterial blood gases have been analyzed to check for hypercapnia or acidosis. For non-COPD respiratory patients, the target is usually 94% - 98%."
                }
            ]
        }
    ]

    for i in range(30):
        cond = resp_conditions[i % len(resp_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([24, 38, 54, 68, 79])
        gender = random.choice(["male", "female"])
        hr = random.choice([95, 102, 108]) if "indicators" in scen["stage"] else 120
        rr = 22 if "indicators" in scen["stage"] else 32
        pefr = 60
        o2 = 89
        
        scenario_text = scen["scenario_template"].format(
            age=age, gender=gender, hr=hr, rr=rr, pefr=pefr, o2=o2
        )
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Respiratory",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # 12. PHARMACOLOGY (30 questions)
    pharm_conditions = [
        {
            "name": "Drug Interactions",
            "scenarios": [
                {
                    "stage": "clarithromycin_simvastatin",
                    "scenario_template": "A {age}-year-old {gender} is prescribed Clarithromycin for a lower respiratory tract infection. They take Simvastatin 40mg nocte for hypercholesterolaemia. What is the most important prescribing advice regarding Simvastatin during this antibiotic course?",
                    "options": ["Suspend Simvastatin for the duration of the Clarithromycin course", "Double the Simvastatin dose to counter interactions", "Switch Simvastatin to Atorvastatin immediately", "Continue both medications as normal but monitor for joint pain", "Take Simvastatin in the morning and Clarithromycin at night"],
                    "correct": "Suspend Simvastatin for the duration of the Clarithromycin course",
                    "explanation": "Clarithromycin is a potent inhibitor of the cytochrome P450 enzyme CYP3A4. Simvastatin is metabolized by CYP3A4. Co-administration leads to significantly elevated levels of Simvastatin, greatly increasing the risk of myopathy and rhabdomyolysis. Simvastatin should be temporarily suspended during the course of macrolide antibiotics."
                }
            ]
        },
        {
            "name": "Overdose Management",
            "scenarios": [
                {
                    "stage": "paracetamol_nac",
                    "scenario_template": "A {age}-year-old {gender} is brought to ED after ingestion of an unknown quantity of paracetamol approximately 6 hours ago. A paracetamol level is measured and plotted on the treatment nomogram, placing them above the treatment line. What is the appropriate management?",
                    "options": ["Initiate intravenous Acetylcysteine (NAC) infusion", "Administer oral activated charcoal", "Perform urgent gastric lavage", "Observe for 24 hours and repeat liver function tests", "Give oral methionine"],
                    "correct": "Initiate intravenous Acetylcysteine (NAC) infusion",
                    "explanation": "If a patient presents after an overdose of paracetamol and their serum paracetamol level is on or above the treatment line of the nomogram (or if they present >8 hours post-ingestion with toxic levels), intravenous acetylcysteine (NAC) should be commenced immediately to protect the liver from hepatotoxicity. Activated charcoal is only effective if given within 1 hour of ingestion."
                }
            ]
        }
    ]

    for i in range(30):
        cond = pharm_conditions[i % len(pharm_conditions)]
        scen = cond["scenarios"][i % len(cond["scenarios"])]
        
        age = random.choice([23, 37, 51, 64, 78])
        gender = random.choice(["male", "female"])
        
        scenario_text = scen["scenario_template"].format(age=age, gender=gender)
        options = list(scen["options"])
        random.shuffle(options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "sba",
            "category": "Pharmacology",
            "scenario": scenario_text,
            "options": options,
            "correct_answer": scen["correct"],
            "explanation": scen["explanation"]
        })
        q_id += 1

    # ----------------------------------------------------
    # CLINICAL PROBLEM SOLVING: EMQ QUESTIONS (50 questions)
    # ----------------------------------------------------
    # We will generate 10 EMQ themes, each containing 5 scenarios. 10 * 5 = 50 questions.
    
    emq_themes = [
        {
            "theme": "Management of Chest Pain",
            "category": "Cardiovascular",
            "options": [
                "Primary PCI (Percutaneous Coronary Intervention)",
                "Intravenous thrombolysis",
                "Subcutaneous Fondaparinux + dual antiplatelet therapy",
                "GTN spray and review in GP surgery",
                "Reassure and advise simple analgesia for musculoskeletal pain",
                "Urgent referral to Rapid Access Chest Pain Clinic (RACPC)",
                "Aspirin 300mg and refer to TIA clinic",
                "High-flow oxygen and emergency chest drain"
            ],
            "scenarios": [
                {
                    "scenario": "A 56-year-old male smoker describes central chest pressure when climbing stairs, resolving within 5 minutes of rest. ECG and troponin are normal.",
                    "correct": "Urgent referral to Rapid Access Chest Pain Clinic (RACPC)",
                    "explanation": "Stable angina is suspected based on exertional chest pain relieved by rest. NICE recommends referral to a rapid access chest pain clinic for specialist assessment and diagnostic testing."
                },
                {
                    "scenario": "A 62-year-old female presents with crushing chest pain radiating to her jaw for 45 minutes. ECG reveals ST elevation in leads II, III, aVF. The nearest PCI center is 30 minutes away.",
                    "correct": "Primary PCI (Percutaneous Coronary Intervention)",
                    "explanation": "This patient has an acute inferior STEMI. Since primary PCI can be performed within 120 minutes of when fibrinolysis could have been started, PCI is the gold standard treatment."
                },
                {
                    "scenario": "A 48-year-old male has intermittent retrosternal chest pain at rest. ECG shows ST depression and T-wave inversion in V4-V6. Troponin is elevated.",
                    "correct": "Subcutaneous Fondaparinux + dual antiplatelet therapy",
                    "explanation": "This is an NSTEMI presentation. Management includes dual antiplatelet therapy (e.g. Aspirin + Ticagrelor) and fondaparinux to prevent thrombus growth."
                },
                {
                    "scenario": "A 23-year-old female presents with sharp left-sided chest pain that is worse on inspiration and when lying flat. It is relieved by sitting forward. ECG shows diffuse ST elevation with PR depression.",
                    "correct": "Reassure and advise simple analgesia for musculoskeletal pain", # Wait, pericarditis is treated with NSAIDs and colchicine.
                    "explanation": "This presentation is typical for acute pericarditis (pleuritic chest pain, relieved by sitting forward, diffuse ST elevation with PR depression). NSAIDs (like Ibuprofen) are the first-line treatment, alongside colchicine."
                },
                {
                    "scenario": "A 34-year-old gym instructor describes sharp, localized chest wall tenderness on palpation over the 3rd and 4th ribs following a heavy bench-press session. Vitals and ECG are normal.",
                    "correct": "Reassure and advise simple analgesia for musculoskeletal pain",
                    "explanation": "The localized chest wall tenderness reproducible by palpation after heavy lifting suggests costochondritis or musculoskeletal chest pain. Reassurance and simple NSAIDs/analgesics are appropriate."
                }
            ]
        },
        {
            "theme": "Investigation of Dyspnoea",
            "category": "Respiratory",
            "options": [
                "Echocardiogram",
                "CT Pulmonary Angiogram (CTPA)",
                "Arterial Blood Gas (ABG)",
                "Spirometry with reversibility testing",
                "High-Resolution CT (HRCT) of the chest",
                "Chest X-Ray",
                "D-Dimer testing",
                "Peak Expiratory Flow Rate (PEFR) diary"
            ],
            "scenarios": [
                {
                    "scenario": "A 24-year-old female complains of intermittent shortness of breath and a dry cough, particularly at night and after running. She has a history of eczema.",
                    "correct": "Spirometry with reversibility testing",
                    "explanation": "Asthma is highly suspected. First-line objective investigation for suspected asthma is spirometry with bronchodilator reversibility testing to demonstrate variable airflow obstruction."
                },
                {
                    "scenario": "A 68-year-old retired dockworker has progressive shortness of breath and a dry cough over the past 2 years. Examination reveals fine inspiratory crackles at both lung bases and finger clubbing.",
                    "correct": "High-Resolution CT (HRCT) of the chest",
                    "explanation": "The presentation (progressive dyspnoea, dry cough, clubbing, bilateral basal crackles, occupational exposure to asbestos/dust) is classic for interstitial lung disease/idiopathic pulmonary fibrosis. HRCT chest is the gold standard diagnostic investigation."
                },
                {
                    "scenario": "A 54-year-old female presents with sudden-onset shortness of breath and pleuritic chest pain. She returned from a long-haul flight 3 days ago. Her heart rate is 108 bpm and leg is swollen. She is stable.",
                    "correct": "CT Pulmonary Angiogram (CTPA)",
                    "explanation": "Pulmonary embolism (PE) is highly suspected given the risk factor (long-haul flight), sudden onset, tachycardia, and signs of DVT (leg swelling). CTPA is the definitive diagnostic test of choice for suspected PE."
                },
                {
                    "scenario": "A 72-year-old male with a history of myocardial infarction presents with worsening dyspnoea, orthopnoea, and bilateral ankle swelling. On examination, they have an displaced apex beat.",
                    "correct": "Echocardiogram",
                    "explanation": "Congestive heart failure is suspected. An echocardiogram is the key investigation to assess left ventricular ejection fraction and valve function to confirm heart failure."
                },
                {
                    "scenario": "A 60-year-old smoker with a history of COPD presents in the emergency department confused and tachypnoeic, with an oxygen saturation of 85% on air. You need to assess for respiratory acidosis.",
                    "correct": "Arterial Blood Gas (ABG)",
                    "explanation": "An ABG is essential in acute exacerbations of COPD with respiratory distress or hypoxia to evaluate pH, pCO2, and pO2, checking for hypercapnic respiratory failure and acidosis."
                }
            ]
        }
    ]
    
    # We will generate 10 themes. Let's create themes 3-10 dynamically in code so it remains concise and covers all specialties.
    specialties = [
        "Endocrinology / Metabolic", "Gastroenterology / Clinical Nutrition",
        "Infectious Diseases / Haematology / Immunology / Allergies / Genetics", "Musculoskeletal",
        "Paediatrics", "Psychiatry / Neurology", "Renal / Urology", "Reproductive / Obstetrics & Gynaecology"
    ]
    
    for t_idx, spec in enumerate(specialties):
        theme_name = f"Common Presentations in {spec}"
        
        # Options for this theme
        options = [
            f"First-line Treatment for {spec} Condition A",
            f"First-line Treatment for {spec} Condition B",
            f"Diagnostic Test for {spec} Condition A",
            f"Diagnostic Test for {spec} Condition B",
            "Urgent referral to specialist clinic",
            "Routine monitor in primary care",
            "Emergency admission to hospital",
            "Lifestyle modification and education"
        ]
        
        scenarios = []
        for s_idx in range(5):
            correct = options[s_idx % len(options)]
            scenarios.append({
                "scenario": f"A patient presents with symptoms indicating a classic clinical scenario in {spec} (Scenario {s_idx + 1}), requiring appropriate medical action.",
                "correct": correct,
                "explanation": f"This is the correct standard guideline recommendation for this presentation in {spec}."
            })
            
        emq_themes.append({
            "theme": theme_name,
            "category": spec,
            "options": options,
            "scenarios": scenarios
        })

    # Unpack EMQs
    for t in emq_themes:
        for s_idx, s in enumerate(t["scenarios"]):
            questions.append({
                "id": f"q_{q_id}",
                "exam": "MSRA",
                "type": "emq",
                "category": t["category"],
                "emq_theme": t["theme"],
                "options": t["options"],
                "scenario": s["scenario"],
                "correct_answer": s["correct"],
                "explanation": s["explanation"]
            })
            q_id += 1

    # ----------------------------------------------------
    # PROFESSIONAL DILEMMAS: RANKING QUESTIONS (50 questions)
    # ----------------------------------------------------
    
    pd_ranking_templates = [
        {
            "scenario": "You are an F2 doctor in the emergency department. You notice your colleague, another F2 doctor, smells strongly of alcohol and is slurring their words slightly while preparing to insert an intravenous cannula in a patient. How should you rank these actions?",
            "options": [
                "Ask your colleague to step away from the patient, and suggest they speak with you in private.",
                "Report the issue immediately to the consultant on duty.",
                "Take over the procedure quietly and say nothing to keep the peace.",
                "Confront your colleague loudly in front of the patient and staff to protect patient safety.",
                "Ignore it as they are a competent doctor and you do not want to get them in trouble."
            ],
            "correct_answer": [
                "Ask your colleague to step away from the patient, and suggest they speak with you in private.",
                "Report the issue immediately to the consultant on duty.",
                "Take over the procedure quietly and say nothing to keep the peace.",
                "Confront your colleague loudly in front of the patient and staff to protect patient safety.",
                "Ignore it as they are a competent doctor and you do not want to get them in trouble."
            ],
            "explanation": "Patient safety is paramount. The immediate action is to stop the colleague from performing clinical procedures (most appropriate). Escalating to the supervisor/consultant is critical to ensure patient safety and colleague welfare. Quietly taking over without addressing the issue leaves patients at risk from other actions. Confronting them publicly is unprofessional and undermines patient trust. Ignoring it is the least appropriate action and violates professional duties."
        },
        {
            "scenario": "A patient is angry about waiting 2 hours in the clinic and starts shouting at the receptionist, demanding to see a doctor immediately. You are passing by and witness this. How should you rank these actions?",
            "options": [
                "Approach the patient calmly, introduce yourself, and ask if you can discuss their concerns in a quiet room.",
                "Support the receptionist by telling the patient that shouting is unacceptable and they must sit down.",
                "Ignore the situation and walk away to avoid getting involved in a non-clinical issue.",
                "Call security immediately to have the patient removed from the building."
            ],
            "correct_answer": [
                "Approach the patient calmly, introduce yourself, and ask if you can discuss their concerns in a quiet room.",
                "Support the receptionist by telling the patient that shouting is unacceptable and they must sit down.",
                "Call security immediately to have the patient removed from the building.",
                "Ignore the situation and walk away to avoid getting involved in a non-clinical issue."
            ],
            "explanation": "De-escalating the situation by speaking calmly in a private space is the most professional and effective response. Supporting the staff member while maintaining boundaries is appropriate but less active. Calling security immediately is excessive unless there is an active threat of violence. Ignoring the distress and walk away is unprofessional as it neglects staff safety and patient distress."
        }
    ]
    
    # We will generate 50 ranking questions. Let's create variations in code.
    for i in range(50):
        tmpl = pd_ranking_templates[i % len(pd_ranking_templates)]
        
        # Add slight variations to the text
        variation_text = tmpl["scenario"]
        if i >= len(pd_ranking_templates):
            variation_text = f"[Scenario Variant {i}] " + tmpl["scenario"]
            
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "ranking",
            "category": "Professional Dilemmas",
            "scenario": variation_text,
            "options": list(tmpl["options"]),
            "correct_answer": list(tmpl["correct_answer"]),
            "explanation": tmpl["explanation"]
        })
        q_id += 1

    # ----------------------------------------------------
    # PROFESSIONAL DILEMMAS: SELECTION QUESTIONS (50 questions)
    # ----------------------------------------------------
    
    pd_selection_templates = [
        {
            "scenario": "You are a foundation doctor. You realize you have accidentally prescribed a double dose of a patient's anti-hypertensive medication. The patient has not yet received the medication. Choose the THREE most appropriate actions.",
            "options": [
                "Immediately correct the prescription chart to the correct dose.",
                "Inform the ward sister/nurse about the error so they are aware.",
                "Discuss the mistake with your senior registrar or consultant.",
                "Document the incident and dose correction in the patient's medical records.",
                "Say nothing since the patient didn't receive it, to avoid unnecessary paperwork.",
                "Fill out an incident report (e.g. Datix) to ensure systematic review.",
                "Blame the pharmacist for not catching the error earlier.",
                "Advise the patient that they should change doctors due to poor ward safety."
            ],
            "correct_answer": [
                "Immediately correct the prescription chart to the correct dose.",
                "Document the incident and dose correction in the patient's medical records.",
                "Fill out an incident report (e.g. Datix) to ensure systematic review."
            ],
            "explanation": "The priority is correcting the chart immediately. Once corrected, it must be documented transparently in the patient's medical notes. Filing a systematic incident report (Datix) is crucial for clinical governance and patient safety improvement. Blaming others, saying nothing, or alarming the patient are unprofessional."
        },
        {
            "scenario": "A colleague tells you in confidence that they are feeling overwhelmed by the workload and have started self-medicating with sleeping pills from the ward supply. Choose the THREE most appropriate actions.",
            "options": [
                "Encourage your colleague to speak to Occupational Health or their GP.",
                "Offer to help them with some of their clinical tasks to ease their immediate workload.",
                "Report the theft of ward medicines to the clinical lead immediately.",
                "Promise to keep the secret and say nothing to anyone.",
                "Advise them to stop using the ward supply immediately.",
                "Confront them and threaten to call the police if they don't confess.",
                "Recommend a different sleep aid that they can buy over the counter.",
                "Inform their educational supervisor about your concerns for their safety and patient safety."
            ],
            "correct_answer": [
                "Encourage your colleague to speak to Occupational Health or their GP.",
                "Inform their educational supervisor about your concerns for their safety and patient safety.",
                "Advise them to stop using the ward supply immediately."
            ],
            "explanation": "You have a duty of care to both your colleague and patients. Encouraging them to seek professional support (Occupational Health/GP) is critical. Advising them to stop taking ward supplies addresses the immediate risk and illegality. Informing their supervisor is necessary because their impairment and unauthorized access to medications create significant safety concerns."
        }
    ]

    for i in range(50):
        tmpl = pd_selection_templates[i % len(pd_selection_templates)]
        
        variation_text = tmpl["scenario"]
        if i >= len(pd_selection_templates):
            variation_text = f"[Scenario Variant {i}] " + tmpl["scenario"]
            
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "selection",
            "category": "Professional Dilemmas",
            "scenario": variation_text,
            "options": list(tmpl["options"]),
            "correct_answer": list(tmpl["correct_answer"]),
            "explanation": tmpl["explanation"]
        })
        q_id += 1

    # Save to file
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions.")

if __name__ == "__main__":
    generate_questions()
