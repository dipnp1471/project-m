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
                    "correct": "Reassure and advise simple analgesia for musculoskeletal pain",
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
        },
        {
            "theme": "Investigation of Thyroid Status",
            "category": "Endocrinology / Metabolic",
            "options": [
                "Primary hypothyroidism",
                "Subclinical hypothyroidism",
                "Graves' disease",
                "Toxic multinodular goitre",
                "De Quervain's thyroiditis",
                "Sick euthyroid syndrome",
                "Poor compliance with Levothyroxine",
                "Pituitary adenoma (TSH-secreting)"
            ],
            "scenarios": [
                {
                    "scenario": "A 32-year-old female presents with weight gain, lethargy, cold intolerance, and a husky voice. Bloods show: TSH 14.2 mU/L (0.4-4.5), Free T4 6.1 pmol/L (9.0-21.0).",
                    "correct": "Primary hypothyroidism",
                    "explanation": "Elevated TSH with low Free T4 is diagnostic of primary hypothyroidism."
                },
                {
                    "scenario": "A 45-year-old female is found to have a TSH of 6.8 mU/L (0.4-4.5) on routine screening. She has no symptoms of thyroid disease, and her Free T4 is 14.5 pmol/L (9.0-21.0).",
                    "correct": "Subclinical hypothyroidism",
                    "explanation": "Subclinical hypothyroidism is defined by an elevated TSH in the presence of normal thyroid hormone levels (Free T4) and no/minimal clinical symptoms."
                },
                {
                    "scenario": "A 28-year-old female presents with weight loss, palpitations, and heat intolerance. On exam, she has a smooth, diffuse goitre, bilateral exophthalmos, and pretibial myxoedema. TSH is < 0.01 mU/L, Free T4 is 38 pmol/L.",
                    "correct": "Graves' disease",
                    "explanation": "Graves' disease is the most common cause of hyperthyroidism, characterized by diffuse goitre, exophthalmos (eye signs), and pretibial myxoedema, caused by autoantibodies to the TSH receptor."
                },
                {
                    "scenario": "A 36-year-old female presents with a painful, tender neck swelling, fever, and palpitations following a viral upper respiratory infection. Bloods: TSH 0.05 mU/L, Free T4 26 pmol/L. Radioactive iodine uptake scan shows very low uptake.",
                    "correct": "De Quervain's thyroiditis",
                    "explanation": "De Quervain's (subacute) thyroiditis presents with a tender/painful goitre, fever, and transient hyperthyroidism following a viral infection, characterized by low radioactive iodine uptake."
                },
                {
                    "scenario": "A 75-year-old male is admitted to the ICU with severe sepsis secondary to pneumonia. Routine thyroid tests show: TSH 0.12 mU/L (0.4-4.5), Free T4 7.2 pmol/L (9.0-21.0), and low Free T3. He has no prior history of thyroid disease.",
                    "correct": "Sick euthyroid syndrome",
                    "explanation": "Sick euthyroid syndrome (non-thyroidal illness) occurs in patients with acute severe non-thyroidal illness, presenting with low/normal TSH and low thyroid hormone levels (especially T3) without primary thyroid pathology."
                }
            ]
        },
        {
            "theme": "Differential Diagnosis of Chronic Diarrhoea",
            "category": "Gastroenterology / Clinical Nutrition",
            "options": [
                "Crohn's disease",
                "Ulcerative colitis",
                "Coeliac disease",
                "Irritable bowel syndrome (IBS)",
                "Pancreatic insufficiency",
                "Laxative abuse",
                "Microscopic colitis",
                "Bile acid malabsorption"
            ],
            "scenarios": [
                {
                    "scenario": "A 24-year-old male presents with a 6-month history of intermittent diarrhoea, abdominal pain, weight loss, and recurrent mouth ulcers. Examination shows a painful perianal skin tag and a palpable right lower quadrant mass.",
                    "correct": "Crohn's disease",
                    "explanation": "Crohn's disease is a chronic inflammatory bowel disease that can affect any part of the GI tract (mouth to anus), presenting with mouth ulcers, perianal disease, and patchy trans-mural inflammation."
                },
                {
                    "scenario": "A 29-year-old female presents with bloody diarrhoea, urgency, tenesmus, and crampy left-sided abdominal pain. Colonoscopy shows continuous, superficial mucosal inflammation extending from the rectum up to the descending colon.",
                    "correct": "Ulcerative colitis",
                    "explanation": "Ulcerative colitis is characterized by continuous mucosal inflammation starting in the rectum and extending proximally, typically presenting with bloody diarrhoea, urgency, and tenesmus."
                },
                {
                    "scenario": "A 34-year-old female presents with chronic bloating, flatulence, and pale, foul-smelling, floating stools (steatorrhoea). She has a history of chronic pancreatitis and heavy alcohol use.",
                    "correct": "Pancreatic insufficiency",
                    "explanation": "Exocrine pancreatic insufficiency results in inadequate production of digestive enzymes, leading to fat malabsorption, weight loss, and steatorrhoea (pale, smelly, floating stools), commonly caused by chronic pancreatitis."
                },
                {
                    "scenario": "A 21-year-old female describes bloating, flatulence, and intermittent abdominal cramps relieved by defecation. Her bowel habit alternates between constipation and diarrhoea, and symptoms are worse during periods of stress. Inflammatory markers, celiac serology, and fecal calprotectin are normal.",
                    "correct": "Irritable bowel syndrome (IBS)",
                    "explanation": "IBS is a functional bowel disorder characterized by abdominal pain (often relieved by defecation), bloating, and altered bowel habits, in the absence of organic disease (normal calprotectin/serology)."
                },
                {
                    "scenario": "A 30-year-old male presents with fatigue, abdominal bloating, and intermittent loose stools. Blood tests show a microcytic anaemia. Serology is positive for IgA anti-tissue transglutaminase (anti-tTG) antibodies.",
                    "correct": "Coeliac disease",
                    "explanation": "Coeliac disease is an autoimmune enteropathy triggered by gluten ingestion, presenting with diarrhoea, bloating, malabsorption (e.g., iron deficiency anaemia), and positive anti-tTG antibodies."
                }
            ]
        },
        {
            "theme": "Differential Diagnosis of Anaemia",
            "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
            "options": [
                "Iron deficiency anaemia",
                "Thalassaemia trait",
                "Anaemia of chronic disease",
                "Vitamin B12 deficiency",
                "Folate deficiency",
                "Autoimmune haemolytic anaemia",
                "Aplastic anaemia",
                "Sickle cell anaemia"
            ],
            "scenarios": [
                {
                    "scenario": "A 62-year-old strict vegan presents with progressive fatigue and numbness/pins-and-needles in both feet. Bloods show: Hb 8.4 g/dL, MCV 112 fL, and hypersegmented neutrophils on blood film.",
                    "correct": "Vitamin B12 deficiency",
                    "explanation": "Strict vegans are at risk of Vitamin B12 deficiency. It presents with macrocytic anaemia and neurological symptoms (peripheral neuropathy, subacute combined degeneration of the spinal cord) and hypersegmented neutrophils."
                },
                {
                    "scenario": "A 45-year-old female with long-standing rheumatoid arthritis is found to have: Hb 10.2 g/dL, MCV 82 fL. Iron studies show: low serum iron, high ferritin, and low Total Iron Binding Capacity (TIBC).",
                    "correct": "Anaemia of chronic disease",
                    "explanation": "Anaemia of chronic disease is typically normocytic/mildly microcytic, associated with chronic inflammation (like RA), characterized by low serum iron but high ferritin (reflecting locked-away iron stores) and low TIBC."
                },
                {
                    "scenario": "A 24-year-old pregnant female at 12 weeks gestation presents with tiredness. Bloods show: Hb 9.8 g/dL, MCV 74 fL. Iron studies show: low serum iron, low ferritin, and high TIBC.",
                    "correct": "Iron deficiency anaemia",
                    "explanation": "Iron deficiency anaemia is a microcytic, hypochromic anaemia characterized by depleted iron stores (low ferritin) and compensatory increase in iron-binding capacity (high TIBC)."
                },
                {
                    "scenario": "An asymptomatic 22-year-old male of Greek descent has a routine check-up. Bloods show: Hb 11.5 g/dL, MCV 62 fL (disproportionately low). Ferritin and iron levels are completely normal. Haemoglobin electrophoresis shows elevated HbA2.",
                    "correct": "Thalassaemia trait",
                    "explanation": "Beta-thalassaemia trait is characterized by a mild microcytic anaemia with a disproportionately low MCV and normal iron stores, confirmed by elevated HbA2 on electrophoresis."
                },
                {
                    "scenario": "A 55-year-old male with a history of alcohol dependency presents with fatigue. Bloods: Hb 9.2 g/dL, MCV 108 fL. Vitamin B12 levels are normal, but red cell folate is low. He has no neurological symptoms.",
                    "correct": "Folate deficiency",
                    "explanation": "Folate deficiency causes macrocytic anaemia similar to B12 deficiency but without the associated neurological symptoms (subacute combined degeneration). Alcoholism is a common cause."
                }
            ]
        },
        {
            "theme": "Diagnosis of Joint Pain",
            "category": "Musculoskeletal",
            "options": [
                "Osteoarthritis",
                "Rheumatoid arthritis",
                "Gout",
                "Pseudogout",
                "Septic arthritis",
                "Reactive arthritis",
                "Ankylosing spondylitis",
                "Psoriatic arthritis"
            ],
            "scenarios": [
                {
                    "scenario": "A 68-year-old female complains of mechanical pain in both knees, which is worse with walking and relieved by rest. On examination, there is crepitus, bony enlargement, and restricted range of movement. X-ray shows joint space narrowing, subchondral sclerosis, and osteophytes.",
                    "correct": "Osteoarthritis",
                    "explanation": "Osteoarthritis is characterized by mechanical joint pain (worse with use), bony swelling, and classic X-ray findings: loss of joint space, osteophytes, subchondral sclerosis, and subchondral cysts (LOSS)."
                },
                {
                    "scenario": "A 32-year-old male presents with a 6-month history of lower back pain and morning stiffness that lasts for 2 hours and improves with physical activity. He is found to be HLA-B27 positive, and pelvic X-ray shows bilateral sacroiliitis.",
                    "correct": "Ankylosing spondylitis",
                    "explanation": "Ankylosing spondylitis is an inflammatory arthritis affecting the spine and sacroiliac joints, typical in young males, presenting with morning back stiffness that improves with exercise, strongly associated with HLA-B27."
                },
                {
                    "scenario": "A 26-year-old male presents with acute swelling and pain in his left knee, accompanied by painful red eyes (conjunctivitis) and dysuria, starting 2 weeks after a self-limiting episode of urethritis.",
                    "correct": "Reactive arthritis",
                    "explanation": "Reactive arthritis is a sterile inflammatory arthritis that develops after a gastrointestinal or genitourinary infection (classic triad: conjunctivitis, urethritis, and arthritis)."
                },
                {
                    "scenario": "A 72-year-old female presents with acute pain and swelling in her right knee. Joint aspiration reveals turbid fluid. Polarized light microscopy shows positively birefringent, rhomboid-shaped crystals.",
                    "correct": "Pseudogout",
                    "explanation": "Pseudogout (calcium pyrophosphate deposition) typically affects the knee in elderly patients, showing positively birefringent rhomboid-shaped crystals under polarized light."
                },
                {
                    "scenario": "A 54-year-old male presents with sudden-onset, excruciating pain, redness, and swelling in his left first metatarsophalangeal (MTP) joint, waking him from sleep. Aspiration of the joint shows negatively birefringent needle-shaped crystals.",
                    "correct": "Gout",
                    "explanation": "Gout is an inflammatory arthritis caused by monosodium urate crystal deposition, classically presenting as acute monoarthritis of the first MTP joint (podagra), with negatively birefringent needle-shaped crystals."
                }
            ]
        },
        {
            "theme": "Assessment of Paediatric Rashes",
            "category": "Paediatrics",
            "options": [
                "Measles",
                "Scarlet fever",
                "Chickenpox (Varicella)",
                "Erythema infectiosum (Fifth disease)",
                "Roseola infantum",
                "Hand, foot, and mouth disease",
                "Meningococcal septicaemia",
                "Impetigo"
            ],
            "scenarios": [
                {
                    "scenario": "A 4-year-old child presents with a high fever, cough, runny nose, and conjunctivitis. On examination, there are small, greyish-white spots on the buccal mucosa opposite the lower molars. A maculopapular rash started behind the ears yesterday and is spreading to the face and neck.",
                    "correct": "Measles",
                    "explanation": "Measles presents with the prodrome of cough, coryza, and conjunctivitis (the 3 Cs), Koplik's spots (buccal mucosa spots), followed by a maculopapular rash spreading cranio-caudally."
                },
                {
                    "scenario": "A 6-year-old child has a sore throat, headache, and high fever. On examination, they have tonsillar hypertrophy with exudate, a flushed face with perioral pallor, a 'strawberry tongue', and a widespread fine, erythematous rash that feels like sandpaper.",
                    "correct": "Scarlet fever",
                    "explanation": "Scarlet fever is caused by Group A Streptococcus, presenting with tonsillitis, strawberry tongue, and a characteristic sandpaper-like rash with perioral pallor."
                },
                {
                    "scenario": "An 11-month-old infant is brought with a history of a high fever (39.5°C) lasting 3 days, during which the infant was otherwise relatively well. The fever has suddenly subsided today, and a rosy, non-pruritic maculopapular rash has appeared on the trunk and limbs.",
                    "correct": "Roseola infantum",
                    "explanation": "Roseola infantum (HHV-6) classically presents with a high fever in an infant which falls suddenly, immediately followed by the appearance of a maculopapular rash on the trunk."
                },
                {
                    "scenario": "A 3-year-old child presents with a 24-hour history of mild fever and malaise, followed by the appearance of crops of itchy, red macules that rapidly progress to papules, vesicles, and then crust over. Lesions are seen at various stages of development across the trunk and face.",
                    "correct": "Chickenpox (Varicella)",
                    "explanation": "Chickenpox presents with a classic itchy, vesicular rash appearing in crops, so lesions in all stages (macules, papules, vesicles, crusts) are visible simultaneously."
                },
                {
                    "scenario": "A 5-year-old child is brought to the GP surgery with a low-grade fever and a bright red, confluent rash on both cheeks, giving a 'slapped-cheek' appearance. A lace-like macular rash is also developing on the limbs.",
                    "correct": "Erythema infectiosum (Fifth disease)",
                    "explanation": "Erythema infectiosum (Fifth disease, caused by Parvovirus B19) classically presents with a 'slapped-cheek' rash followed by a reticulate (lace-like) rash on the trunk and limbs."
                }
            ]
        },
        {
            "theme": "Diagnosis of Tremor and Movement Disorders",
            "category": "Psychiatry / Neurology",
            "options": [
                "Parkinson's disease",
                "Essential tremor",
                "Drug-induced parkinsonism",
                "Huntington's disease",
                "Cerebellar syndrome",
                "Wilson's disease",
                "Benign essential blepharospasm",
                "Multiple system atrophy (MSA)"
            ],
            "scenarios": [
                {
                    "scenario": "A 68-year-old male presents with a slow, unilateral tremor in his right hand at rest, which disappears during voluntary movement. On examination, he has cogwheel rigidity, an expressionless face (masked facies), and a slow, shuffling gait.",
                    "correct": "Parkinson's disease",
                    "explanation": "Parkinson's disease is characterized by the triad of resting tremor (often pill-rolling), rigidity (cogwheel), and bradykinesia (slow movements, shuffling gait), usually starting unilaterally."
                },
                {
                    "scenario": "A 42-year-old female presents with a fine, bilateral tremor of the hands that is absent at rest but becomes prominent when she holds her arms outstretched or writes. She notes that the tremor improves significantly after drinking a glass of wine. Her father had a similar tremor.",
                    "correct": "Essential tremor",
                    "explanation": "Essential tremor is a postural and action tremor (absent at rest), often autosomal dominant (family history), and characteristically improves with alcohol."
                },
                {
                    "scenario": "A 35-year-old male is brought to clinic due to involuntary, jerky movements of his limbs (chorea) and progressive personality changes and cognitive decline. His mother died in her 40s with a similar progressive neurological disease.",
                    "correct": "Huntington's disease",
                    "explanation": "Huntington's disease is an autosomal dominant neurodegenerative disorder characterized by chorea, psychiatric symptoms (personality changes), and cognitive decline, typically presenting in mid-life."
                },
                {
                    "scenario": "A 58-year-old female with schizophrenia has been taking Haloperidol for 6 months. She presents with a new bilateral resting tremor, generalized muscle stiffness, and slow movements. She has no family history of neurological disease.",
                    "correct": "Drug-induced parkinsonism",
                    "explanation": "Drug-induced parkinsonism is a common extrapyramidal side effect of dopamine antagonists like typical antipsychotics (e.g. Haloperidol), presenting with bilateral parkinsonian features."
                },
                {
                    "scenario": "A 55-year-old male with a history of chronic alcohol excess presents with unsteady gait. Examination reveals a broad-based gait, intention tremor (worse as hand approaches target), past-pointing, and dysdiadochokinesia.",
                    "correct": "Cerebellar syndrome",
                    "explanation": "Cerebellar dysfunction leads to symptoms summarized by 'DANISH': Dysdiadochokinesia, Ataxia (broad-based gait), Nystagmus, Intention tremor, Slurred speech, Hypotonia."
                }
            ]
        },
        {
            "theme": "Causes of Hematuria",
            "category": "Renal / Urology",
            "options": [
                "Urinary tract infection (UTI)",
                "Bladder transitional cell carcinoma",
                "Renal cell carcinoma",
                "IgA nephropathy",
                "Post-streptococcal glomerulonephritis",
                "Renal calculi",
                "Benign prostatic hyperplasia (BPH)",
                "Polycystic kidney disease"
            ],
            "scenarios": [
                {
                    "scenario": "A 67-year-old male who worked in the industrial rubber industry and is a heavy smoker presents with several episodes of painless macroscopic hematuria over the last month. He has no voiding symptoms.",
                    "correct": "Bladder transitional cell carcinoma",
                    "explanation": "Painless macroscopic hematuria in an older person (especially with risk factors like smoking or industrial dye/rubber exposure) is bladder cancer (TCC) until proven otherwise."
                },
                {
                    "scenario": "A 22-year-old male presents with macroscopic hematuria that began yesterday, in the middle of a sore throat and fever. A urinalysis shows blood 3+ and protein 1+. His blood pressure and renal function are normal.",
                    "correct": "IgA nephropathy",
                    "explanation": "IgA nephropathy (Berger's disease) characteristically presents with synpharyngitic hematuria (macroscopic hematuria occurring concurrent with or 1-2 days after an upper respiratory infection)."
                },
                {
                    "scenario": "A 42-year-old female presents with sudden-onset, severe, right-sided loin pain that radiates down to her groin. She is extremely restless and vomiting. Urinalysis reveals blood 3+ but no nitrites or leucocytes.",
                    "correct": "Renal calculi",
                    "explanation": "Renal calculi (kidney stones) present with acute, severe, colicky loin-to-groin pain (renal colic), restlessness, and microscopic/macroscopic hematuria."
                },
                {
                    "scenario": "A 75-year-old male complains of a weak urinary stream, hesitancy, nocturia, and terminal dribbling. He has noticed occasional blood in his urine. Rectal exam reveals a smooth, enlarged prostate with no nodules.",
                    "correct": "Benign prostatic hyperplasia (BPH)",
                    "explanation": "BPH presents with lower urinary tract symptoms (hesitancy, weak stream, nocturia, dribbling) and can cause hematuria due to rupture of congested prostatic veins."
                },
                {
                    "scenario": "An 8-year-old boy presents with dark, tea-colored urine, puffy eyes (periorbital oedema), and a blood pressure of 135/85 mmHg (hypertensive). He had a severe sore throat 2 weeks ago which resolved.",
                    "correct": "Post-streptococcal glomerulonephritis",
                    "explanation": "Post-streptococcal glomerulonephritis presents 1-3 weeks after a streptococcal throat or skin infection, with nephritic syndrome: hematuria (tea-colored urine), hypertension, and mild oedema."
                }
            ]
        },
        {
            "theme": "Causes of Abnormal Vaginal Bleeding",
            "category": "Reproductive / Obstetrics & Gynaecology",
            "options": [
                "Cervical ectropion",
                "Cervical cancer",
                "Endometrial cancer",
                "Endometrial polyp",
                "Chlamydia trachomatis infection",
                "Uterine fibroids",
                "Atrophic vaginitis",
                "Breakthrough bleeding due to COCP"
            ],
            "scenarios": [
                {
                    "scenario": "A 24-year-old female on the combined oral contraceptive pill presents with postcoital bleeding. Speculum examination reveals a red, velvety, circular area around the external cervical os that bleeds easily on contact. Cervical swab is negative.",
                    "correct": "Cervical ectropion",
                    "explanation": "Cervical ectropion (eversion of columnar epithelium) is common in women on estrogen-containing contraceptives or during pregnancy, presenting with postcoital bleeding and a red, velvety cervical os."
                },
                {
                    "scenario": "A 61-year-old postmenopausal female presents with a 2-week history of light vaginal bleeding. She has never used HRT and went through menopause at age 52. She is obese and has Type 2 Diabetes.",
                    "correct": "Endometrial cancer",
                    "explanation": "Any postmenopausal bleeding (PMB) must be investigated for endometrial cancer. Risk factors include obesity, diabetes, early menarche/late menopause (increased estrogen exposure)."
                },
                {
                    "scenario": "A 22-year-old female presents with intermenstrual bleeding, postcoital bleeding, and a yellow vaginal discharge. On examination, the cervix is friable and inflamed. She recently started a new relationship.",
                    "correct": "Chlamydia trachomatis infection",
                    "explanation": "Chlamydia is a common STI presenting with abnormal vaginal bleeding (postcoital, intermenstrual), purulent discharge, and a friable cervix."
                },
                {
                    "scenario": "A 42-year-old female presents with increasingly heavy and painful periods. On abdominal examination, a firm, non-tender pelvic mass is felt rising from the pelvis, equivalent to a 14-week gravid uterus. Ultrasound confirms multiple benign uterine smooth muscle tumors.",
                    "correct": "Uterine fibroids",
                    "explanation": "Uterine fibroids (leiomyomas) are benign smooth muscle tumors presenting with menorrhagia (heavy menstrual bleeding) and pelvic pressure/enlarged uterus."
                },
                {
                    "scenario": "A 65-year-old postmenopausal female complains of vaginal dryness, burning, and itching. She notes slight blood spotting after intercourse. On speculum exam, the vaginal mucosa appears thin, pale, and dry with petechiae.",
                    "correct": "Atrophic vaginitis",
                    "explanation": "Atrophic vaginitis is caused by estrogen deficiency in postmenopausal women, leading to thin, dry, inflamed vaginal mucosa that is prone to bleeding/spotting (especially postcoital)."
                }
            ]
        }
    ]

    # Unpack EMQs
    for t in emq_themes:
        for s in t["scenarios"]:
            # Shuffling the options lists for database representation (so it looks clean and randomized)
            opts = list(t["options"])
            random.shuffle(opts)
            questions.append({
                "id": f"q_{q_id}",
                "exam": "MSRA",
                "type": "emq",
                "category": t["category"],
                "emq_theme": t["theme"],
                "options": opts,
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
            "scenario": "You are a {role_me} in the {dept}. You notice your colleague, {colleague_name} (another {role_colleague}), smells strongly of alcohol and is slurring their words slightly while preparing to perform a {procedure} on a patient. How should you rank these actions?",
            "options": [
                "Ask {colleague_name} to step away from the patient, and suggest they speak with you in private.",
                "Report the issue immediately to the {senior_role} on duty.",
                "Take over the {procedure} quietly and say nothing to keep the peace.",
                "Confront {colleague_name} loudly in front of the patient and staff to protect patient safety.",
                "Ignore it as they are a competent doctor and you do not want to get them in trouble."
            ],
            "correct_order": [0, 1, 2, 3, 4],
            "explanation": "Patient safety is paramount. The immediate action is to stop the colleague from performing clinical procedures (most appropriate). Escalating to the supervisor/consultant is critical to ensure patient safety and colleague welfare. Quietly taking over without addressing the issue leaves patients at risk from other actions. Confronting them publicly is unprofessional and undermines patient trust. Ignoring it is the least appropriate action and violates professional duties."
        },
        {
            "scenario": "A {person_type} is angry about waiting {wait_time} hours in the {dept} and starts shouting at {staff_member}, demanding immediate attention. You are passing by and witness this. How should you rank these actions?",
            "options": [
                "Approach the {person_type} calmly, introduce yourself, and ask if you can discuss their concerns in a quiet room.",
                "Support {staff_member} by telling the {person_type} that shouting is unacceptable and they must wait their turn.",
                "Call security immediately to have the {person_type} removed from the building.",
                "Ignore the situation and walk away to avoid getting involved in a non-clinical dispute."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "De-escalating the situation by speaking calmly in a private space is the most professional and effective response. Supporting the staff member while maintaining boundaries is appropriate but less active. Calling security immediately is excessive unless there is an active threat of violence. Ignoring the distress and walking away is unprofessional as it neglects staff safety and patient distress."
        },
        {
            "scenario": "While in the hospital {public_place}, you overhear two doctors, {doc1} and {doc2}, discussing a patient's sensitive diagnosis of {condition} in detail. Other members of the public are present and listening. How should you rank these actions?",
            "options": [
                "Intervene gently in the moment, reminding them that they are in a public space.",
                "Wait until you exit the {public_place} and speak to them privately about patient confidentiality.",
                "Say nothing to them but file a formal incident report (Datix) about the confidentiality breach.",
                "Join in the conversation or ask details about {condition} to learn more about the case."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "Patient confidentiality is a core professional duty. Intervening immediately and gently is the most appropriate action as it stops the breach in progress. Speaking to them privately afterward is also appropriate as it addresses the behaviour directly without public embarrassment. Reporting the incident without speaking to them is helpful for clinical governance but does not stop the active breach. Joining the conversation is a further breach of confidentiality and is the least appropriate action."
        },
        {
            "scenario": "Your colleague, {colleague_name}, is consistently {late_time} minutes late for handovers in the {dept}, leaving you to manage the ward alone and feeling increasingly stressed. How should you rank these actions?",
            "options": [
                "Speak to {colleague_name} privately to express your concerns and ask if they are okay or need support.",
                "Discuss the workload with your {senior_role} to see if ward staffing or handovers can be adjusted.",
                "Say nothing to {colleague_name} but complain about their lateness to other team members on the ward.",
                "Stop doing any handover work for them and leave the ward exactly on time, leaving patients unattended."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "Open communication and professional teamwork are key. Speaking to the colleague privately addresses the issue constructively and checks on their welfare (most appropriate). Escalating to a senior is a reasonable next step if the workload is unsafe. Complaining to others is unprofessional and breeds resentment. Abandoning the ward and leaving patients unattended is extremely unsafe and the least appropriate action."
        },
        {
            "scenario": "You are a junior doctor on the {dept}. You prescribe {medication} for a patient, but {nurse_name}, an experienced ward nurse, disagrees with your decision and refuses to administer it. How should you rank these actions?",
            "options": [
                "Discuss {nurse_name}'s concerns with them to understand their reasoning, and review the guidelines together.",
                "Ask your {senior_role} to review the patient and resolve the disagreement.",
                "Administer {medication} yourself without addressing {nurse_name}'s concerns.",
                "Document in the medical notes that the nurse refused to administer the medication and report them to the head nurse."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "Respecting the expertise of nursing colleagues and working collaboratively is essential. Discussing their concerns directly allows you to check for errors and review guidelines together (most appropriate). Involving a senior doctor is a safe way to resolve a persistent impasse. Administering it yourself bypasses team safety checks and increases risk. Reporting the nurse without discussion is hostile, unprofessional, and does not resolve the clinical issue."
        },
        {
            "scenario": "You receive a phone call from {relative_relation} of a patient admitted with {condition} to the {dept}. They demand a detailed update on the patient's prognosis, but you notice the patient has not documented any consent to share information. How should you rank these actions?",
            "options": [
                "Explain politely that you cannot disclose patient information without the patient's consent, and offer to ask the patient for permission.",
                "Check the medical records to see if there is documented consent, and if not, call the patient's next of kin to update them anyway.",
                "Give the {relative_relation} a vague update about the patient being 'stable' to keep them happy without giving specific details.",
                "Give the {relative_relation} full details of the patient's condition to avoid causing them distress."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "You have a strict legal and ethical duty to maintain patient confidentiality. Explaining this politely and offering to seek consent is the correct and professional response. Checking records is good practice, but updating the relative without consent is a breach. Giving vague updates is misleading and still breaches confidentiality principles. Disclosing full details without consent is a direct breach of confidentiality and is the least appropriate action."
        },
        {
            "scenario": "A patient admitted to the {dept} with {symptom} insists on leaving the hospital against medical advice (AMA) because they have a {excuse}. How should you rank these actions?",
            "options": [
                "Explore the patient's reasons for wanting to leave, explain the risks of leaving, and assess their mental capacity.",
                "Offer alternative outpatient follow-ups, safety-net advice, and ask if they will stay for key tests.",
                "Tell them they are not allowed to leave and threaten to call security to restrain them.",
                "Let them leave immediately without explanation, and delete their admission file to save paperwork."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "Patient autonomy must be respected, but you must ensure they make an informed decision and have mental capacity. Exploring their reasons and explaining risks is the first-line response (most appropriate). Offering harm-reduction and safety-netting is crucial for patients who still choose to leave. Coercing or restraining a capacitous patient is illegal and unprofessional. Letting them leave without any safety-netting or destroying records is negligent and the least appropriate action."
        },
        {
            "scenario": "During a ward round on the {dept}, your supervisor, {senior_name}, belittles your knowledge and speaks rudely to you in front of the patient and staff. How should you rank these actions?",
            "options": [
                "Wait until the ward round is finished, and speak to {senior_name} privately to explain how their comments made you feel.",
                "Discuss the incident with your educational supervisor or clinical tutor to seek guidance on how to handle it.",
                "Confront {senior_name} angrily in front of the patient to defend your dignity.",
                "Say nothing, but refuse to work with {senior_name} on future shifts, leaving shifts short-staffed."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "Professionalism must be maintained at all times, even in the face of poor behaviour from seniors. Speaking privately and calmly is the most mature and constructive action. Seeking advice from an educational supervisor is a supportive and appropriate step. Confronting them publicly in front of patients undermines professional standards and patient trust. Unilaterally refusing to work shifts compromises patient care and is the least appropriate action."
        },
        {
            "scenario": "Your registrar, {senior_name}, asks you to perform a {procedure} on a patient in the {dept}. You have only observed this procedure once and do not feel competent to perform it unsupervised. How should you rank these actions?",
            "options": [
                "Explain to {senior_name} that you do not feel competent to do it alone, and ask if they can supervise you while you perform it.",
                "Decline to do the procedure and suggest {senior_name} performs it, offering to assist.",
                "Attempt the procedure anyway to avoid appearing incompetent or lazy to your senior.",
                "Ignore the request, walk away, and leave the patient without the procedure."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "You must always work within your limits of competence to ensure patient safety. Asking for supervision allows you to learn safely while protecting the patient (most appropriate). Declining but offering to assist is a safe alternative. Performing an unsupervised procedure you are not competent in puts the patient at risk of harm. Ignoring the request and leaving the patient unattended is irresponsible and the least appropriate action."
        },
        {
            "scenario": "A grateful patient on the {dept} offers you a {gift_item} as a personal thank you for your care during their admission. How should you rank these actions?",
            "options": [
                "Thank the patient warmly but politely decline the gift, explaining that hospital policy prevents you from accepting personal gifts.",
                "Suggest that if they wish to express gratitude, they could write a thank-you letter or donate to the hospital charity.",
                "Accept the gift but report it to your clinical lead and document it in your portfolio.",
                "Accept the gift and keep it for yourself, saying nothing to anyone."
            ],
            "correct_order": [0, 1, 2, 3],
            "explanation": "GMC guidelines state that doctors must not accept gifts that could be seen as an inducement or affect the doctor-patient relationship. Declining politely is the most appropriate action. Redirecting their gratitude to a charity or letter is highly constructive. Accepting and reporting is less appropriate but transparent. Keeping the gift silently violates professional standards and is the least appropriate."
        }
    ]

    pd_ranking_vars = [
        # Template 0 (Impaired colleague)
        [
            {"role_me": "F2 doctor", "dept": "Emergency Department", "colleague_name": "Dr. James Patel", "role_colleague": "F2 doctor", "procedure": "intravenous cannula", "senior_role": "consultant"},
            {"role_me": "FY1 doctor", "dept": "Acute Medical Unit", "colleague_name": "Dr. Chloe Bennett", "role_colleague": "FY1 doctor", "procedure": "lumbar puncture", "senior_role": "medical registrar"},
            {"role_me": "SHO", "dept": "Paediatric Assessment Unit", "colleague_name": "Dr. Ryan Cooper", "role_colleague": "locum SHO", "procedure": "arterial blood gas", "senior_role": "paediatric consultant"},
            {"role_me": "F2 doctor", "dept": "Surgical Assessment Unit", "colleague_name": "Dr. Hannah Ward", "role_colleague": "F2 colleague", "procedure": "urinary catheterization", "senior_role": "surgical registrar"},
            {"role_me": "FY1 doctor", "dept": "Geriatric Ward", "colleague_name": "Dr. Sam Taylor", "role_colleague": "FY1 doctor", "procedure": "nasogastric tube insertion", "senior_role": "consultant geriatrician"}
        ],
        # Template 1 (Angry patient/relative)
        [
            {"person_type": "patient", "wait_time": "2", "dept": "Outpatient Clinic", "staff_member": "the receptionist"},
            {"person_type": "relative", "wait_time": "3", "dept": "Emergency Waiting Room", "staff_member": "the triage nurse"},
            {"person_type": "patient", "wait_time": "1.5", "dept": "Antenatal Clinic", "staff_member": "the clinic clerk"},
            {"person_type": "relative", "wait_time": "4", "dept": "Paediatric ED", "staff_member": "the ward clerk"},
            {"person_type": "patient", "wait_time": "2.5", "dept": "Surgical Admissions Unit", "staff_member": "the receptionist"}
        ],
        # Template 2 (Confidentiality breach)
        [
            {"public_place": "passenger lift", "doc1": "Dr. Miller", "doc2": "Dr. Jones", "condition": "metastatic lung cancer"},
            {"public_place": "main cafeteria", "doc1": "Dr. Watson", "doc2": "Dr. Holmes", "condition": "severe schizophrenia"},
            {"public_place": "main reception area", "doc1": "Dr. Evans", "doc2": "Dr. Green", "condition": "HIV infection"},
            {"public_place": "public corridor", "doc1": "Dr. Davis", "doc2": "Dr. Knight", "condition": "suspected tuberculosis"},
            {"public_place": "hospital coffee shop", "doc1": "Dr. Smith", "doc2": "Dr. Brown", "condition": "acute liver failure"}
        ],
        # Template 3 (Colleague late / Overworked)
        [
            {"colleague_name": "Dr. Alex Mercer", "late_time": "30", "dept": "Medical Ward", "senior_role": "ward registrar"},
            {"colleague_name": "Dr. Lily Evans", "late_time": "45", "dept": "Emergency Department", "senior_role": "consultant on-call"},
            {"colleague_name": "Dr. Marcus Vance", "late_time": "20", "dept": "Paediatric Ward", "senior_role": "senior registrar"},
            {"colleague_name": "Dr. Sarah Connor", "late_time": "35", "dept": "Surgical Ward", "senior_role": "surgical registrar"},
            {"colleague_name": "Dr. David Tennant", "late_time": "40", "dept": "Obstetrics Assessment Unit", "senior_role": "obstetric registrar"}
        ],
        # Template 4 (Disagreement with nurse)
        [
            {"dept": "Respiratory Ward", "medication": "low molecular weight heparin", "nurse_name": "Nurse Higgins", "senior_role": "medical registrar"},
            {"dept": "Cardiology Ward", "medication": "intravenous furosemide", "nurse_name": "Nurse Kelly", "senior_role": "cardiology registrar"},
            {"dept": "Paediatric Ward", "medication": "oral amoxicillin", "nurse_name": "Nurse Jackson", "senior_role": "paediatric registrar"},
            {"dept": "Surgical Ward", "medication": "intravenous morphine", "nurse_name": "Nurse Davies", "senior_role": "surgical registrar"},
            {"dept": "AMU", "medication": "intravenous gentamicin", "nurse_name": "Nurse Thompson", "senior_role": "medical registrar"}
        ],
        # Template 5 (Relative asking for info)
        [
            {"relative_relation": "the spouse", "condition": "alcoholic hepatitis", "dept": "Gastroenterology Ward"},
            {"relative_relation": "the sibling", "condition": "an acute psychotic episode", "dept": "Psychiatric Unit"},
            {"relative_relation": "the adult child", "condition": "advanced dementia", "dept": "Geriatric Assessment Ward"},
            {"relative_relation": "the cousin", "condition": "a sexually transmitted infection", "dept": "Outpatient Clinic"},
            {"relative_relation": "the parent", "condition": "an accidental drug overdose", "dept": "Intensive Care Unit"}
        ],
        # Template 6 (Patient leaving AMA)
        [
            {"dept": "Cardiology Ward", "symptom": "intermittent chest pain", "excuse": "important business meeting"},
            {"dept": "Surgical Assessment Unit", "symptom": "suspected acute appendicitis", "excuse": "pet dog at home that needs feeding"},
            {"dept": "Emergency Department", "symptom": "a severe head injury", "excuse": "family dinner party"},
            {"dept": "Medical Ward", "symptom": "uncontrolled diabetes and ketones", "excuse": "phobia of hospitals"},
            {"dept": "Clinical Decision Unit", "symptom": "a suspected deep vein thrombosis", "excuse": "pre-booked flight tomorrow"}
        ],
        # Template 7 (Senior colleague rude)
        [
            {"dept": "Endocrine Ward", "senior_name": "Dr. Sterling (the consultant)"},
            {"dept": "Acute Stroke Unit", "senior_name": "Dr. Vance (the senior registrar)"},
            {"dept": "Paediatric Ward", "senior_name": "Dr. Korda (the consultant)"},
            {"dept": "General Surgery Ward", "senior_name": "Mr. Black (the consultant surgeon)"},
            {"dept": "Neonatal Unit", "senior_name": "Dr. Thorne (the clinical lead)"}
        ],
        # Template 8 (Competency limits)
        [
            {"senior_name": "Dr. Gregory (the registrar)", "procedure": "chest drain insertion", "dept": "Respiratory Ward"},
            {"senior_name": "Dr. House (the senior registrar)", "procedure": "lumbar puncture", "dept": "Medical Admissions Unit"},
            {"senior_name": "Mr. Thomas (the consultant)", "procedure": "central line insertion", "dept": "Surgical ICU"},
            {"senior_name": "Dr. Allison (the registrar)", "procedure": "ascitic drain insertion", "dept": "Gastroenterology Ward"},
            {"senior_name": "Dr. Chase (the registrar)", "procedure": "joint aspiration", "dept": "Rheumatology Clinic"}
        ],
        # Template 9 (Gifts from patients)
        [
            {"dept": "Geriatric Ward", "gift_item": "valuable gold watch"},
            {"dept": "Maternity Ward", "gift_item": "box of luxury chocolates containing an envelope with £100 cash"},
            {"dept": "Oncology Day Unit", "gift_item": "case of expensive vintage wine"},
            {"dept": "Orthopaedic Ward", "gift_item": "cheque for £500 made out to you personally"},
            {"dept": "General Practice Clinic", "gift_item": "pair of expensive designer sunglasses"}
        ]
    ]

    for i in range(50):
        tmpl_idx = i % len(pd_ranking_templates)
        tmpl = pd_ranking_templates[tmpl_idx]
        var_idx = i // len(pd_ranking_templates)
        var_params = pd_ranking_vars[tmpl_idx][var_idx]
        
        scenario_text = tmpl["scenario"].format(**var_params)
        formatted_options = [opt.format(**var_params) for opt in tmpl["options"]]
        
        # correct_answer must contain the formatted options in correct order
        correct_answer = [formatted_options[idx] for idx in tmpl["correct_order"]]
        
        shuffled_options = list(formatted_options)
        random.shuffle(shuffled_options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "ranking",
            "category": "Professional Dilemmas",
            "scenario": scenario_text,
            "options": shuffled_options,
            "correct_answer": correct_answer,
            "explanation": tmpl["explanation"]
        })
        q_id += 1

    # ----------------------------------------------------
    # PROFESSIONAL DILEMMAS: SELECTION QUESTIONS (50 questions)
    # ----------------------------------------------------
    
    pd_selection_templates = [
        # 1. Accidental Prescribing Error
        {
            "scenario": "You are a {role_me} in the {dept}. You realize you have accidentally prescribed a double dose of {medication} for a patient. The patient has not yet received the medication. Choose the THREE most appropriate actions.",
            "options": [
                "Immediately correct the prescription chart to the correct dose.",
                "Document the incident and dose correction in the patient's medical records.",
                "Fill out an incident report (e.g. Datix) to ensure systematic review.",
                "Inform the ward sister/nurse about the error so they are aware.",
                "Discuss the mistake with your senior registrar or consultant.",
                "Say nothing since the patient didn't receive it, to avoid unnecessary paperwork.",
                "Blame the pharmacist for not catching the error earlier.",
                "Advise the patient that they should change doctors due to poor ward safety."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "The priority is correcting the chart immediately. Once corrected, it must be documented transparently in the patient's medical notes. Filing a systematic incident report (Datix) is crucial for clinical governance and patient safety improvement. Blaming others, saying nothing, or alarming the patient are unprofessional."
        },
        # 2. Colleague mental health / Overwhelmed
        {
            "scenario": "A fellow junior doctor, {colleague_name}, tells you in confidence that they are feeling completely overwhelmed by the workload in the {dept} and have started self-medicating with {medication} from {source}. Choose the THREE most appropriate actions.",
            "options": [
                "Encourage {colleague_name} to speak to Occupational Health or their GP.",
                "Inform their educational supervisor about your concerns for their safety and patient safety.",
                "Advise them to stop using {source} immediately.",
                "Offer to help them with some of their clinical tasks to ease their immediate workload.",
                "Report the theft of ward medicines to the clinical lead immediately.",
                "Promise to keep the secret and say nothing to anyone.",
                "Confront them and threaten to call the police if they don't confess.",
                "Recommend a different sleep aid that they can buy over the counter."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "You have a duty of care to both your colleague and patients. Encouraging them to seek professional support (Occupational Health/GP) is critical. Advising them to stop taking ward supplies addresses the immediate risk and illegality. Informing their supervisor is necessary because their impairment and unauthorized access to medications create significant safety concerns."
        },
        # 3. Relative Demanding Futile Treatment
        {
            "scenario": "A patient with advanced {condition} in the {dept} is nearing the end of life. Their {relative_relation} is extremely distressed and demanding that the clinical team continue aggressive {treatment} which the consultant has determined is futile. Choose the THREE most appropriate actions.",
            "options": [
                "Arrange a formal meeting with the family, senior nurse, and consultant to discuss the clinical reasoning and care goals.",
                "Involve a palliative care specialist or chaplain to support the family through their distress.",
                "Offer to seek a second clinical opinion from another independent consultant to reassure the family.",
                "Accede to the family's demands and initiate {treatment} to avoid conflict.",
                "Tell the {relative_relation} that their demands are ridiculous and refuse to speak to them further.",
                "Instruct the nursing staff to ban the {relative_relation} from visiting the ward.",
                "Tell the patient directly that their family is causing trouble for the staff.",
                "Call security to have the family escorted off the premises immediately."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Open communication and empathy are key. Arranging a formal meeting to discuss goals of care and involving support (palliative care/chaplains) addresses the emotional distress of the family while maintaining clinical standards. Offering a second opinion is a supportive way to resolve conflict. Initiating futile treatments is clinically inappropriate, while hostility or security calls are unprofessional and escalate the issue."
        },
        # 4. Needlestick Injury
        {
            "scenario": "While performing a {procedure} on a patient in the {dept} who is known to be positive for {virus}, you accidentally sustain a needlestick injury. Choose the THREE most appropriate actions.",
            "options": [
                "Immediately encourage bleeding and wash the wound thoroughly with warm running water and soap.",
                "Report the injury immediately to Occupational Health or the Emergency Department for post-exposure management.",
                "Ensure the incident is formally logged in the hospital's accident reporting system (Datix).",
                "Squeeze the wound tightly and apply a strong disinfectant like bleach to sterilize it.",
                "Continue with your shift and wait to see if any symptoms develop before reporting it.",
                "Ask a colleague to test the patient's blood sample without the patient's knowledge or consent.",
                "Confront the patient and blame them for not warning you more clearly about their status.",
                "Keep the incident confidential to avoid any professional stigma."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Immediate first aid (washing the wound) is the first priority. Reporting to Occupational Health or ED immediately ensures you receive timely post-exposure prophylaxis (PEP) if indicated. Logging it on Datix ensures proper reporting and governance. Harsh chemicals can damage tissue further, testing without consent is unethical, and delaying reporting compromises your health."
        },
        # 5. Colleague Social Media Post
        {
            "scenario": "You notice that your colleague, {colleague_name}, has posted a photo of a patient's {photo_detail} on their public social media account, with a joking caption. Although the patient's face is not visible, the {identifying_detail} is recognizable. Choose the THREE most appropriate actions.",
            "options": [
                "Speak to {colleague_name} privately and advise them to remove the post immediately.",
                "Report the post to the ward manager or clinical director due to the patient confidentiality breach.",
                "Document the details of the post (e.g. date, content) to support any subsequent investigation.",
                "Comment on the post with a joke to show solidarity with your colleague.",
                "Report the post to the social media platform's support line but say nothing to the hospital.",
                "Ignore the post since the patient's name and face were not directly shown.",
                "Confront {colleague_name} publicly in the comments section of the post.",
                "Advise the patient's relatives to check the colleague's social media page."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Protecting patient privacy is paramount. Speaking to the colleague privately is the fastest way to get the post removed. Reporting it to the ward manager ensures the organization is aware of the breach, and documenting the details is necessary for evidence. Ignoring it is a breach of your professional duties, and public comments or informing the family inappropriately escalates the issue."
        },
        # 6. Informed Consent / Language Barrier
        {
            "scenario": "You are preparing to obtain consent for a {procedure} from a patient in the {dept} who speaks very little English. Their {relative_relation} offers to translate for them. Choose the THREE most appropriate actions.",
            "options": [
                "Arrange for a professional hospital interpreter (telephone or face-to-face) to translate the consent process.",
                "Check the patient's understanding of key risks and benefits of the {procedure} via the professional interpreter.",
                "Document the use of the professional interpreter and the translator's ID number in the patient's medical records.",
                "Accept the {relative_relation}'s offer to translate to save time and resources.",
                "Proceed with obtaining consent using sign language and gestures.",
                "Ask a colleague who speaks a little of the patient's language to translate the complex risks.",
                "Postpone the {procedure} indefinitely without trying to find an interpreter.",
                "Have the patient sign the English consent form and assume they understand."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Valid consent requires clear understanding. Using professional interpreters is mandatory to avoid misunderstandings or conflicts of interest that occur with relatives. Verifying understanding and documenting the interpreter's details are standard requirements. Relative translation is unsafe for complex medical risks, and signing without understanding is invalid consent."
        },
        # 7. Patient Disclosing Self-Harm / Confidentiality
        {
            "scenario": "A {age}-year-old patient admitted to the {dept} discloses to you that they are regularly self-harming, but begs you not to tell their parents or guardians. Choose the THREE most appropriate actions.",
            "options": [
                "Assess the patient's immediate safety and risk of severe self-harm or suicide.",
                "Explain to the patient that you cannot keep this information secret due to safeguarding duties, but will support them in informing their family.",
                "Inform the ward safeguarding lead or your supervising consultant about the disclosure.",
                "Promise the patient that you will keep the secret to maintain their trust.",
                "Immediately phone the patient's parents behind their back without telling the patient.",
                "Discharge the patient immediately to avoid safeguarding paperwork.",
                "Suggest that they try to distract themselves with hobbies instead of self-harming.",
                "Confront the patient about their behaviour and tell them they are wasting ward beds."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Safeguarding and patient safety override confidentiality when there is risk of harm. Assessing immediate risk is the first step. You must be honest with the patient about your limits of confidentiality while offering support. Escalating to the safeguarding lead/supervisor is a legal and professional requirement. Promising secrecy is unsafe, and acting behind their back without discussion breaks trust."
        },
        # 8. Colleague Plagiarism / Fraud
        {
            "scenario": "Your colleague, {colleague_name}, asks you to review a draft of their {project_type} for an upcoming national audit. You realize they have copied your data and slides from your project last year, presenting them as their own work. Choose the THREE most appropriate actions.",
            "options": [
                "Speak to {colleague_name} privately, point out the plagiarism, and ask them to remove or properly credit your work.",
                "Raise the issue with the director of medical education or the audit lead if the colleague refuses to correct it.",
                "Keep records of your original project files and data as evidence of your authorship.",
                "Confront the colleague publicly during the department's presentation meeting.",
                "Agree to let them use it if they promise to include your name as a co-author on the new draft.",
                "Say nothing to avoid professional conflict and damaging your relationship with them.",
                "Delete the colleague's presentation files from the shared drive when they are not looking.",
                "Report the colleague immediately to the General Medical Council (GMC) as a first step."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Doctors must be honest and trustworthy. Addressing the issue privately first allows the colleague to correct their behavior. Escalating to the audit lead or director of medical education is necessary if they refuse to act. Keeping evidence is key. Public confrontation, collusion, or sabotage are unprofessional and GMC referral is a disproportionate first step."
        },
        # 9. Suspected Child Safeguarding
        {
            "scenario": "A parent brings their {age}-month-old infant to the {dept} with a {injury_type}. The parent's explanation of how it happened (falling from a {fall_source}) does not align with the typical injury pattern. Choose the THREE most appropriate actions.",
            "options": [
                "Discuss the case and the mismatch between history and injury mechanism with a senior paediatrician or consultant.",
                "Contact the hospital's safeguarding children team or local social services to raise a child protection concern.",
                "Document a detailed and objective account of the physical findings, history given, and any discrepancies in the notes.",
                "Confront the parent and accuse them of abusing the child in front of others.",
                "Accept the parent's explanation to avoid causing offence or distress.",
                "Discharge the infant home immediately once the {injury_type} is treated.",
                "Ask the parent to sign a document promising they will be more careful in the future.",
                "Call the police immediately to arrest the parent without consulting any clinical seniors."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Child safety is a major safeguarding responsibility. Mismatches between history and physical signs must be escalated to a senior paediatrician and the safeguarding team. Precise, objective documentation of the findings and discrepancies is vital. Public confrontation is unsafe and unprofessional, while ignoring the risk or premature discharge is negligent."
        },
        # 10. Equipment Malfunction / Near Miss
        {
            "scenario": "During a routine check of the {equipment_name} in the {dept}, you discover that {defect_detail}. Choose the THREE most appropriate actions.",
            "options": [
                "Immediately source a replacement or restock the missing items to ensure clinical readiness.",
                "Log the equipment deficiency on the hospital's incident reporting system (Datix) as a near-miss.",
                "Inform the ward manager or nurse in charge so that they can address any systemic checking failures.",
                "Leave the {equipment_name} as it is, assuming the next shift will check and fix it.",
                "File a complaint against the nurse who was signed off as checking it yesterday.",
                "Write an angry note on the whiteboard criticizing ward organization.",
                "Hide the {equipment_name} so that staff are forced to find a new one.",
                "Wait until an emergency occurs to see if the missing items are actually needed."
            ],
            "correct_answers": [0, 1, 2],
            "explanation": "Maintaining clinical equipment is essential for safety. Restocking or replacing ensures the ward is prepared. Logging the near-miss and informing the manager allows for root-cause analysis and systemic improvement. Inaction, blame culture, or passive-aggressive behavior do not solve the safety issue."
        }
    ]

    pd_selection_vars = [
        # Template 0 (Accidental Prescribing Error)
        [
            {"role_me": "foundation doctor", "dept": "Geriatric Ward", "medication": "anti-hypertensive medication"},
            {"role_me": "F2 doctor", "dept": "Emergency Department", "medication": "intravenous paracetamol"},
            {"role_me": "FY1 doctor", "dept": "Acute Medical Unit", "medication": "daily low molecular weight heparin"},
            {"role_me": "SHO", "dept": "Surgical Assessment Unit", "medication": "post-operative antibiotic"},
            {"role_me": "FY1 doctor", "dept": "Paediatric Ward", "medication": "oral liquid ibuprofen"}
        ],
        # Template 1 (Colleague mental health / Overwhelmed)
        [
            {"colleague_name": "Dr. Sarah", "dept": "Respiratory Ward", "medication": "sleeping pills", "source": "the ward drug cupboard"},
            {"colleague_name": "Dr. Ahmed", "dept": "Busy AMU", "medication": "anxiolytics", "source": "the emergency drug trolley"},
            {"colleague_name": "Dr. Jess", "dept": "Surgical Ward", "medication": "opioid painkillers", "source": "the theatre stockroom"},
            {"colleague_name": "Dr. Leo", "dept": "Emergency Department", "medication": "sedatives", "source": "the ward stock cupboard"},
            {"colleague_name": "Dr. Emma", "dept": "Paediatric Ward", "medication": "strong sleeping aids", "source": "the ward treatment room"}
        ],
        # Template 2 (Relative Demanding Futile Treatment)
        [
            {"condition": "metastatic lung cancer", "dept": "Oncology Ward", "relative_relation": "son", "treatment": "cardiopulmonary resuscitation (CPR)"},
            {"condition": "end-stage kidney disease", "dept": "Renal Unit", "relative_relation": "daughter", "treatment": "intravenous hemodialysis"},
            {"condition": "severe congestive heart failure", "dept": "Cardiology Ward", "relative_relation": "spouse", "treatment": "invasive mechanical ventilation"},
            {"condition": "advanced multi-infarct dementia", "dept": "Geriatric Ward", "relative_relation": "husband", "treatment": "intravenous antibiotics"},
            {"condition": "decompensated liver cirrhosis", "dept": "Gastroenterology Ward", "relative_relation": "sister", "treatment": "cardiopulmonary resuscitation (CPR)"}
        ],
        # Template 3 (Needlestick Injury)
        [
            {"procedure": "venepuncture", "dept": "Acute Medical Unit", "virus": "Hepatitis C"},
            {"procedure": "lumbar puncture", "dept": "Medical Admissions Ward", "virus": "HIV"},
            {"procedure": "cannulation", "dept": "Emergency Department", "virus": "Hepatitis B"},
            {"procedure": "arterial blood gas", "dept": "Respiratory Ward", "virus": "Hepatitis C"},
            {"procedure": "pleural tap", "dept": "Oncology Ward", "virus": "HIV"}
        ],
        # Template 4 (Colleague Social Media Post)
        [
            {"colleague_name": "Dr. Green", "photo_detail": "unusual skin lesion", "identifying_detail": "distinctive tattoo nearby"},
            {"colleague_name": "Dr. Carter", "photo_detail": "complex hand fracture", "identifying_detail": "unique wedding ring"},
            {"colleague_name": "Dr. Miller", "photo_detail": "severe abdominal swelling", "identifying_detail": "hospital wristband and name"},
            {"colleague_name": "Dr. Bell", "photo_detail": "unusual skull X-ray", "identifying_detail": "patient's unique birthmark"},
            {"colleague_name": "Dr. Vance", "photo_detail": "rare eye pathology", "identifying_detail": "distinctive facial scarring"}
        ],
        # Template 5 (Informed Consent / Language Barrier)
        [
            {"procedure": "lumbar puncture", "dept": "Neurology Ward", "relative_relation": "teenage daughter"},
            {"procedure": "inguinal hernia repair", "dept": "Surgical Day Unit", "relative_relation": "adult son"},
            {"procedure": "diagnostic endoscopy", "dept": "Gastroenterology Unit", "relative_relation": "niece"},
            {"procedure": "pleural aspiration", "dept": "Respiratory Clinic", "relative_relation": "brother"},
            {"procedure": "cataract surgery", "dept": "Ophthalmology Day Ward", "relative_relation": "grandson"}
        ],
        # Template 6 (Patient Disclosing Self-Harm / Confidentiality)
        [
            {"age": "16", "dept": "Paediatric Ward"},
            {"age": "17", "dept": "Adolescent Mental Health Clinic"},
            {"age": "15", "dept": "Emergency Department"},
            {"age": "16", "dept": "General Practice Clinic"},
            {"age": "17", "dept": "Surgical Assessment Unit"}
        ],
        # Template 7 (Colleague Plagiarism / Fraud)
        [
            {"colleague_name": "Dr. Taylor", "project_type": "quality improvement (QI) project"},
            {"colleague_name": "Dr. Morgan", "project_type": "clinical audit presentation"},
            {"colleague_name": "Dr. Brooks", "project_type": "case report submission"},
            {"colleague_name": "Dr. Scott", "project_type": "research abstract draft"},
            {"colleague_name": "Dr. Hughes", "project_type": "teaching module project"}
        ],
        # Template 8 (Suspected Child Safeguarding)
        [
            {"age": "14", "dept": "Paediatric ED", "injury_type": "spiral humeral fracture", "fall_source": "low sofa"},
            {"age": "9", "dept": "Paediatric Clinic", "injury_type": "multiple cigarette burns", "fall_source": "hot radiator"},
            {"age": "18", "dept": "Emergency Department", "injury_type": "severe subdural haematoma", "fall_source": "changing mat"},
            {"age": "24", "dept": "Surgical Assessment Unit", "injury_type": "bruising in a shape of a hand on the thigh", "fall_source": "coffee table edge"},
            {"age": "6", "dept": "Urgent Care Centre", "injury_type": "scald on both feet", "fall_source": "bath spill"}
        ],
        # Template 9 (Equipment Malfunction / Near Miss)
        [
            {"equipment_name": "resuscitation trolley", "dept": "Cardiology Ward", "defect_detail": "the emergency oxygen cylinders are completely empty"},
            {"equipment_name": "intubation equipment bag", "dept": "Maternity Theatre", "defect_detail": "several key laryngoscope blades are missing"},
            {"equipment_name": "anaphylaxis rescue kit", "dept": "Outpatient Clinic", "defect_detail": "the adrenaline pre-filled syringes have expired"},
            {"equipment_name": "defibrillator machine", "dept": "AMU", "defect_detail": "the battery is dead and it is not plugged in"},
            {"equipment_name": "emergency drug cupboard", "dept": "Paediatric Ward", "defect_detail": "the keys have been left in the lock unsupervised"}
        ]
    ]

    for i in range(50):
        tmpl_idx = i % len(pd_selection_templates)
        tmpl = pd_selection_templates[tmpl_idx]
        var_idx = i // len(pd_selection_templates)
        var_params = pd_selection_vars[tmpl_idx][var_idx]
        
        scenario_text = tmpl["scenario"].format(**var_params)
        formatted_options = [opt.format(**var_params) for opt in tmpl["options"]]
        
        # correct_answer must contain the formatted options at correct indices
        correct_answer = [formatted_options[idx] for idx in tmpl["correct_answers"]]
        
        shuffled_options = list(formatted_options)
        random.shuffle(shuffled_options)
        
        questions.append({
            "id": f"q_{q_id}",
            "exam": "MSRA",
            "type": "selection",
            "category": "Professional Dilemmas",
            "scenario": scenario_text,
            "options": shuffled_options,
            "correct_answer": correct_answer,
            "explanation": tmpl["explanation"]
        })
        q_id += 1

    # Save to file
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions.")

if __name__ == "__main__":
    generate_questions()
