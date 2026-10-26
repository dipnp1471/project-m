# -*- coding: utf-8 -*-
"""
High-Yield Clinical Problem Solving Questions (MSRA / UKMLA / AKT Format)
60 clinical reasoning vignettes designed around NICE CKS, BNF, and UK guidelines.
5 questions for each of the 12 clinical domains.
"""

CLINICAL_QUESTIONS = [
    # =========================================================================
    # 1. CARDIOVASCULAR
    # =========================================================================
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 58-year-old Caucasian man attends his GP surgery after ambulatory blood pressure monitoring (ABPM) confirms a daytime average blood pressure of 146/92 mmHg. His QRISK3 score is 14%. His past medical history includes diet-controlled type 2 diabetes mellitus and mild knee osteoarthritis. Renal function and electrolytes are normal (eGFR >90 mL/min/1.73m², K+ 4.2 mmol/L). According to NICE guidelines, what is the most appropriate first-line antihypertensive medication?",
        "options": [
            "Ramipril",
            "Amlodipine",
            "Indapamide",
            "Bisoprolol",
            "Doxazosin"
        ],
        "correct_answer": "Ramipril",
        "explanation": "While patients aged 55 years or over (without diabetes) are normally started on a calcium channel blocker (such as amlodipine) as Step 1 therapy, NICE NG136 specifies that adults of any age with type 2 diabetes mellitus should be offered an ACE inhibitor (such as ramipril) or an ARB as first-line antihypertensive treatment due to their renoprotective effect on glomerular efferent arteriolar pressure."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 64-year-old man presents to the Emergency Department with a 2-hour history of severe central crushing chest pain radiating to his jaw. His 12-lead ECG shows 3 mm ST-segment elevation in leads II, III, and aVF. On examination, his blood pressure is 84/52 mmHg, heart rate is 56 bpm, jugular venous pressure (JVP) is elevated at 6 cm above the sternal angle, and auscultation of both lung fields is completely clear. While preparing for immediate primary percutaneous coronary intervention (PCI), what is the most appropriate initial management of his hypotension?",
        "options": [
            "Intravenous 0.9% sodium chloride fluid bolus",
            "Sublingual glyceryl trinitrate (GTN) spray",
            "Intravenous furosemide 40 mg",
            "Oral bisoprolol 2.5 mg",
            "Intra-aortic balloon pump insertion before angiography"
        ],
        "correct_answer": "Intravenous 0.9% sodium chloride fluid bolus",
        "explanation": "Inferior STEMI (leads II, III, aVF, typically due to right coronary artery occlusion) accompanied by the triad of hypotension, raised JVP, and clear lung fields indicates acute right ventricular infarction. The ischaemic right ventricle depends heavily on preload to maintain left ventricular filling. Nitrates (GTN) and diuretics reduce preload and precipitate profound cardiovascular collapse; cautious intravenous 0.9% sodium chloride boluses are given to optimise right ventricular preload."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 54-year-old man who drives a standard car (Group 1 licence) is about to be discharged after an NSTEMI that was successfully treated with percutaneous coronary intervention (PCI) and drug-eluting stent insertion to the left anterior descending artery. Pre-discharge echocardiography shows a left ventricular ejection fraction of 52%, and no further revascularisation is planned. What advice should you give him regarding driving?",
        "options": [
            "He must stop driving for 1 week and does not need to notify the DVLA",
            "He must stop driving for 4 weeks and does not need to notify the DVLA",
            "He must stop driving for 4 weeks and must notify the DVLA immediately",
            "He must stop driving for 6 weeks until his cardiology outpatient review",
            "He can resume driving immediately upon hospital discharge"
        ],
        "correct_answer": "He must stop driving for 1 week and does not need to notify the DVLA",
        "explanation": "Under DVLA regulations for Group 1 (car and motorcycle) drivers following acute coronary syndrome (ACS), if the patient is successfully treated by coronary angioplasty (PCI), has no other urgent revascularisation planned, and has a left ventricular ejection fraction of at least 40%, they may resume driving after 1 week and do not need to notify the DVLA. If ACS is managed medically without successful angioplasty, the restriction is 4 weeks."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 38-year-old woman is referred to the hypertension clinic with persistent blood pressure readings around 168/104 mmHg despite adherence to amlodipine, indapamide, and doxazosin. She has no significant past medical history and does not eat liquorice. Blood tests reveal: Na+ 145 mmol/L, K+ 2.9 mmol/L, urea 4.4 mmol/L, creatinine 68 umol/L, and bicarbonate 31 mmol/L. What is the most appropriate initial diagnostic investigation?",
        "options": [
            "Plasma aldosterone-to-renin ratio",
            "24-hour urinary free cortisol",
            "CT scan of the adrenal glands",
            "Renal artery Doppler ultrasound",
            "24-hour urinary metanephrines"
        ],
        "correct_answer": "Plasma aldosterone-to-renin ratio",
        "explanation": "Resistant hypertension in a young patient accompanied by hypokalaemia and metabolic alkalosis strongly points to primary hyperaldosteronism (Conn's syndrome, caused by a unilateral adrenal adenoma or bilateral adrenal hyperplasia). Autonomous aldosterone secretion promotes distal renal sodium retention and potassium/hydrogen ion excretion while suppressing renin. The first-line screening investigation is a plasma aldosterone-to-renin ratio (showing high aldosterone and suppressed renin), performed before adrenal CT imaging."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 71-year-old man with a bioprosthetic aortic valve presents with a 3-week history of fevers, drenching night sweats, and lethargy. Examination reveals splinter haemorrhages and a new aortic regurgitant murmur. Three sets of peripheral blood cultures grow Streptococcus gallolyticus (formerly Streptococcus bovis). Alongside targeted intravenous antibiotic therapy and transoesophageal echocardiography, which additional investigation is mandatory?",
        "options": [
            "Colonoscopy",
            "High-resolution CT of the chest",
            "Orthopantomogram (dental X-ray)",
            "Cystoscopy",
            "MR cholangiopancreatography (MRCP)"
        ],
        "correct_answer": "Colonoscopy",
        "explanation": "Bacteraemia or infective endocarditis caused by Streptococcus gallolyticus (Streptococcus bovis biotype I) has a strong association with underlying colonic neoplasia (adenomatous polyps or colorectal adenocarcinoma, present in over 50% of cases), as the organism translocates across disrupted colonic mucosa. A full colonoscopy is therefore mandatory during or shortly after treatment even in the absence of bowel symptoms."
    },

    # =========================================================================
    # 2. DERMATOLOGY / OPHTHALMOLOGY / ENT
    # =========================================================================
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 46-year-old woman attends an urgent GP appointment after waking up with a marked reduction in hearing in her left ear accompanied by high-pitched tinnitus. She has no ear pain, discharge, or recent upper respiratory tract infection. Otoscopy shows normal, intact tympanic membranes and clear external auditory canals bilaterally. Using a 512 Hz tuning fork, Rinne's test is positive (air conduction > bone conduction) on both sides, and Weber's test lateralises to the right ear. What is the most appropriate management?",
        "options": [
            "Urgent same-day ENT referral and initiation of high-dose oral prednisolone",
            "Reassurance and a 2-week course of olive oil ear drops",
            "A 6-week trial of fluticasone nasal spray and Valsalva manoeuvres",
            "Oral amoxicillin for 5 days for acute otitis media",
            "Routine outpatient audiology referral within 6 weeks"
        ],
        "correct_answer": "Urgent same-day ENT referral and initiation of high-dose oral prednisolone",
        "explanation": "Weber's test lateralising to the unaffected (right) ear combined with a bilateral positive Rinne's test confirms left-sided sensorineural hearing loss. Idiopathic sudden sensorineural hearing loss (SSNHL) developing over <72 hours is an otological emergency. NICE guidelines mandate an urgent same-day referral to ENT (within 24 hours) for pure-tone audiometry, consideration of high-dose oral or intratympanic corticosteroids, and MRI of the internal acoustic meatus."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 22-year-old university student who wears soft contact lenses presents to her GP with a 24-hour history of severe right eye pain, photophobia, watering, and blurred vision. On examination, visual acuity is 6/18 in the right eye and 6/6 in the left. There is circumcorneal redness and a 2 mm circular white opacity on the right cornea that stains brightly with fluorescein drops. What is the most appropriate immediate action?",
        "options": [
            "Same-day emergency referral to ophthalmology",
            "Prescribe topical chloramphenicol 0.5% eye drops and review in 48 hours",
            "Prescribe topical fusidic acid gel and advise discarding the contact lenses",
            "Apply an eye pad with topical cyclopentolate and review tomorrow",
            "Prescribe oral aciclovir 800 mg five times daily"
        ],
        "correct_answer": "Same-day emergency referral to ophthalmology",
        "explanation": "A painful red eye with reduced visual acuity, photophobia, and a fluorescein-staining corneal opacity in a contact lens wearer indicates microbial (bacterial) keratitis—most frequently caused by Pseudomonas aeruginosa—until proven otherwise. Pseudomonas keratitis can cause rapid corneal stromal melting and perforation within 24–48 hours. Same-day emergency ophthalmology assessment for slit-lamp corneal scrapes and intensive topical fluoroquinolone therapy (e.g. ofloxacin/levofloxacin) is mandatory; topical chloramphenicol is ineffective against Pseudomonas."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 26-year-old man presents with an acute symmetrical rash over the backs of his hands, palms, and forearms that appeared 48 hours ago. Examination reveals multiple 1 cm round lesions, each displaying a dusky, blistered centre surrounded by a pale oedematous ring and an outer erythematous halo. His oral, ocular, and genital mucosae are completely normal, and he is afebrile. He recalls having a 'cold sore' on his lower lip 10 days ago. What is the most common infectious trigger for this presentation?",
        "options": [
            "Herpes simplex virus (HSV)",
            "Epstein-Barr virus (EBV)",
            "Streptococcus pyogenes",
            "Varicella-zoster virus (VZV)",
            "Staphylococcus aureus"
        ],
        "correct_answer": "Herpes simplex virus (HSV)",
        "explanation": "Symmetrical acral lesions with three distinct concentric zones (a central dusky/vesicular zone, an intermediate pale oedematous zone, and a peripheral erythematous ring) are the classic target lesions of erythema multiforme. In the absence of mucosal involvement (erythema multiforme minor), the condition is a cell-mediated hypersensitivity reaction triggered in over 70–80% of cases by preceding Herpes simplex virus (HSV-1 or HSV-2) infection (with Mycoplasma pneumoniae being the second most common infectious cause)."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 74-year-old woman presents with a slowly enlarging, asymptomatic red patch on her anterior right lower leg that has been present for 9 months. She previously applied a 2-week course of 1% hydrocortisone cream with no change. Examination shows a solitary, sharply demarcated, erythematous plaque measuring 1.8 cm in diameter with fine surface scale, but no central ulceration, pearly rolled border, or dermal induration. Dermoscopy reveals clustered glomerular vessels. What is the most likely diagnosis?",
        "options": [
            "Bowen's disease (squamous cell carcinoma in situ)",
            "Nodular basal cell carcinoma",
            "Discoid eczema",
            "Amelanotic malignant melanoma",
            "Pyoderma gangrenosum"
        ],
        "correct_answer": "Bowen's disease (squamous cell carcinoma in situ)",
        "explanation": "A solitary, well-demarcated, erythematous scaly plaque on the sun-exposed lower leg of an older woman that fails to respond to topical steroids is characteristic of Bowen's disease (intraepidermal squamous cell carcinoma in situ). Dermoscopy characteristically shows glomerular (coiled) vessels and surface scale. Untreated, Bowen's disease carries a 3–5% risk of progressing to invasive squamous cell carcinoma; management options include topical 5-fluorouracil, cryotherapy, curettage, or surgical excision."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 68-year-old hypermetropic (long-sighted) woman attends the Emergency Department at 10 pm with a severe right frontal headache, nausea, vomiting, and blurred vision with coloured halos around streetlights. Ten days ago, her GP started her on amitriptyline 25 mg at night for sciatica. On examination, the right eye is diffusely injected with a hazy cornea and a fixed, mid-dilated oval pupil, and the globe feels hard on gentle palpation. By what mechanism did amitriptyline precipitate this emergency?",
        "options": [
            "Antimuscarinic pupillary dilatation crowding the iridocorneal drainage angle",
            "Alpha-1 adrenergic stimulation increasing aqueous humour secretion by the ciliary body",
            "Serotonergic vasoconstriction of the central retinal artery",
            "Direct microvascular thrombosis of the central retinal vein",
            "Histamine H1 receptor blockade causing corneal endothelial oedema"
        ],
        "correct_answer": "Antimuscarinic pupillary dilatation crowding the iridocorneal drainage angle",
        "explanation": "This patient has acute angle-closure glaucoma, which classically affects older, hypermetropic individuals (who have a shallow anterior chamber). Tricyclic antidepressants like amitriptyline possess potent antimuscarinic (anticholinergic) properties that induce mydriasis (pupillary dilatation), especially in dim evening light. In a shallow anterior chamber, the dilated iris bunches up peripherally and obstructs the trabecular meshwork at the iridocorneal angle, preventing aqueous humour outflow and causing a rapid spike in intraocular pressure."
    },

    # =========================================================================
    # 3. ENDOCRINOLOGY / METABOLIC
    # =========================================================================
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 42-year-old woman presents with a 5-month history of lethargy, cold intolerance, constipation, and a 4 kg weight gain. Initial thyroid function tests show TSH 7.8 mU/L (normal range 0.4–4.5 mU/L) and free T4 13.2 pmol/L (normal range 10.0–22.0 pmol/L). Repeat testing 3 months later shows TSH 8.4 mU/L, free T4 12.8 pmol/L, and strongly positive anti-thyroid peroxidase (anti-TPO) antibodies. According to NICE guidelines, what is the most appropriate management?",
        "options": [
            "Offer a 6-month trial of oral levothyroxine",
            "Reassure and repeat thyroid function tests in 12 months without treatment",
            "Refer urgently to endocrinology for radioactive iodine therapy",
            "Start oral liothyronine (T3) monotherapy",
            "Arrange a thyroid ultrasound and fine-needle aspiration"
        ],
        "correct_answer": "Offer a 6-month trial of oral levothyroxine",
        "explanation": "This patient has persistent subclinical hypothyroidism (TSH between 4.5 and 10 mU/L with a normal free T4 on two occasions 3 months apart). Under NICE NG145 guidelines, while levothyroxine is routinely started for anyone with a TSH >=10 mU/L, for adults aged under 65 with a TSH <10 mU/L who have symptoms suggestive of hypothyroidism, clinicians should consider offering a 6-month trial of levothyroxine (and discontinuing it if symptoms do not improve despite TSH normalisation)."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 34-year-old woman with vitiligo presents with a 3-month history of progressive fatigue, postural dizziness, anorexia, weight loss, and darkening of her palmar skin creases and buccal mucosa. Blood tests show: Na+ 127 mmol/L, K+ 5.8 mmol/L, urea 9.4 mmol/L, random glucose 3.2 mmol/L, TSH 14.5 mU/L, and free T4 7.8 pmol/L. A 9 am serum cortisol is 62 nmol/L. Why is it critical to initiate hydrocortisone replacement before starting levothyroxine in this patient?",
        "options": [
            "Levothyroxine increases basal metabolic rate and hepatic cortisol clearance, precipitating an acute adrenal crisis",
            "Hydrocortisone inhibits peripheral conversion of T4 to reverse T3, preventing thyroid storm",
            "Levothyroxine blocks mineralocorticoid receptors in the distal renal tubule, worsening hyperkalaemia",
            "Starting levothyroxine first causes acute pituitary apoplexy due to sudden TSH suppression",
            "Levothyroxine chelates oral hydrocortisone in the gastrointestinal tract, preventing steroid absorption"
        ],
        "correct_answer": "Levothyroxine increases basal metabolic rate and hepatic cortisol clearance, precipitating an acute adrenal crisis",
        "explanation": "This patient has autoimmune polyendocrine syndrome type 2 (Schmidt's syndrome), presenting with both primary adrenal insufficiency (Addison's disease: hyponatraemia, hyperkalaemia, hypoglycaemia, hyperpigmentation) and autoimmune hypothyroidism. In any patient with concurrent adrenal insufficiency and hypothyroidism (or panhypopituitarism), glucocorticoid replacement (hydrocortisone) must always be started before levothyroxine. Thyroid hormone accelerates basal metabolic rate and hepatic cytochrome P450 clearance of cortisol, which rapidly exhausts residual cortisol stores and triggers a potentially fatal Addisonian crisis."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 76-year-old woman is brought to her GP surgery with mild confusion and unsteadiness 2 weeks after starting citalopram for depression. On examination, her pulse is 74 bpm, blood pressure is 128/76 mmHg with no postural drop, mucous membranes are moist, JVP is normal, and there is no peripheral oedema. Investigations show: Serum Na+ 122 mmol/L, serum osmolality 252 mOsm/kg, urine osmolality 490 mOsm/kg, and urinary sodium 48 mmol/L. Thyroid function and 9 am cortisol are normal. What is the diagnosis?",
        "options": [
            "Syndrome of inappropriate ADH secretion (SIADH)",
            "Cranial diabetes insipidus",
            "Primary polydipsia",
            "Cerebral salt wasting syndrome",
            "Addison's disease"
        ],
        "correct_answer": "Syndrome of inappropriate ADH secretion (SIADH)",
        "explanation": "SSRIs (such as citalopram) are a well-recognised cause of SIADH, particularly in older adults during the first few weeks of therapy. The diagnostic criteria for SIADH are all met here: clinical euvolaemia, hypotonic hyponatraemia (serum Na+ <135 mmol/L and serum osmolality <275 mOsm/kg), inappropriately concentrated urine (urine osmolality >100 mOsm/kg), elevated urinary sodium (>20–30 mmol/L), and normal renal, adrenal, and thyroid function. First-line management involves stopping the offending drug and fluid restriction."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 29-year-old woman was diagnosed with Graves' thyrotoxicosis 4 weeks ago and started on carbimazole 40 mg daily. She telephones the GP surgery today reporting a severe sore throat, painful mouth ulcers, and a temperature of 38.7°C since yesterday. What is the single most important instruction to give her immediately?",
        "options": [
            "Stop taking carbimazole immediately and attend today for an urgent full blood count",
            "Continue carbimazole, take paracetamol, and book a routine throat swab in 48 hours",
            "Halve the dose of carbimazole to 20 mg daily and start oral phenoxymethylpenicillin",
            "Switch carbimazole to propylthiouracil immediately without blood tests",
            "Continue carbimazole and attend for urgent thyroid function tests to exclude thyroid storm"
        ],
        "correct_answer": "Stop taking carbimazole immediately and attend today for an urgent full blood count",
        "explanation": "Carbimazole and propylthiouracil carry a ~0.1–0.5% risk of idiosyncratic agranulocytosis (severe neutropenia, typically occurring within the first 3 months of treatment). Any patient on antithyroid drug therapy who develops a sore throat, mouth ulcers, bruising, or unexplained fever must stop the drug immediately and have an urgent same-day full blood count (FBC). Carbimazole may only be restarted if the FBC confirms a normal neutrophil count."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 19-year-old man with type 1 diabetes is admitted to the Emergency Department with diabetic ketoacidosis (capillary ketones 5.6 mmol/L, blood glucose 26.4 mmol/L, venous pH 7.14, bicarbonate 9 mmol/L). He is commenced on a fixed-rate intravenous insulin infusion at 0.1 units/kg/hour alongside his first 1-litre bag of 0.9% sodium chloride. His initial laboratory venous potassium returns at 5.8 mmol/L. According to Joint British Diabetes Societies (JBDS) guidelines, how should potassium be managed in his intravenous fluids at this stage?",
        "options": [
            "Give 0.9% sodium chloride with no added potassium until serum potassium falls below 5.5 mmol/L",
            "Add 40 mmol/L potassium chloride immediately because insulin drives potassium into cells",
            "Add 20 mmol/L potassium chloride and administer intravenous calcium gluconate",
            "Pause the fixed-rate insulin infusion until serum potassium falls below 5.0 mmol/L",
            "Administer nebulised salbutamol to lower the potassium before continuing fluids"
        ],
        "correct_answer": "Give 0.9% sodium chloride with no added potassium until serum potassium falls below 5.5 mmol/L",
        "explanation": "Although patients in DKA have a total-body potassium deficit and insulin rapidly drives potassium into cells, potassium replacement must be guided strictly by the serum potassium level to avoid fatal hyperkalaemic arrhythmias: if K+ is >5.5 mmol/L, no potassium is added to the fluid bag; once K+ falls to 3.5–5.5 mmol/L (and the patient is passing urine), 40 mmol/L of potassium chloride is added to the 0.9% sodium chloride; if K+ is <3.5 mmol/L, the insulin infusion must be temporarily paused and senior review sought for higher-rate potassium replacement."
    },

    # =========================================================================
    # 4. GASTROENTEROLOGY / CLINICAL NUTRITION
    # =========================================================================
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 27-year-old woman presents with a 6-month history of abdominal bloating, loose stools, and fatigue. Full blood count reveals a microcytic anaemia (Hb 103 g/L, MCV 72 fL) and low serum ferritin. You suspect coeliac disease and plan to request serological testing. According to NICE guidelines, which first-line blood tests should be requested and what dietary advice must be given?",
        "options": [
            "Total serum IgA and IgA tissue transglutaminase (tTG), while eating gluten in more than one meal daily for at least 6 weeks",
            "IgG deamidated gliadin peptide (DGP) only, after excluding gluten from her diet for 2 weeks",
            "HLA-DQ2 and HLA-DQ8 genetic typing as the initial screening test",
            "IgA endomysial antibodies (EMA) alone, with no specific dietary requirements",
            "Faecal calprotectin and anti-Saccharomyces cerevisiae antibodies (ASCA)"
        ],
        "correct_answer": "Total serum IgA and IgA tissue transglutaminase (tTG), while eating gluten in more than one meal daily for at least 6 weeks",
        "explanation": "NICE NG20 recommends testing for both total serum IgA and IgA tissue transglutaminase (tTG) as the first-line serological choice for suspected coeliac disease. Measuring total IgA simultaneously is essential because selective IgA deficiency occurs in ~2–3% of patients with coeliac disease and would otherwise produce a false-negative IgA-tTG result (requiring IgG-based testing instead). Patients must consume gluten in more than one meal every day for at least 6 weeks prior to both serology and endoscopic duodenal biopsy to avoid false-negative results."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 31-year-old man with known ulcerative colitis presents to the Emergency Department with a 4-day history of passing 8 bloody stools per 24 hours. His temperature is 38.2°C, heart rate is 98 bpm, blood pressure is 118/74 mmHg, haemoglobin is 96 g/L, and ESR is 44 mm/hr. Abdominal examination reveals mild left iliac fossa tenderness with no peritonism, and plain abdominal X-ray shows a transverse colon diameter of 4.2 cm. According to Truelove and Witts' criteria and NICE guidelines, how is this flare classified and what is the first-line inpatient treatment?",
        "options": [
            "Acute severe ulcerative colitis; treat with intravenous hydrocortisone",
            "Moderately active ulcerative colitis; discharge on high-dose oral mesalazine and rectal prednisolone",
            "Toxic megacolon; proceed directly to emergency subtotal colectomy",
            "Acute severe ulcerative colitis; start intravenous infliximab as first-line monotherapy",
            "Mild ulcerative colitis flare; start a tapering course of oral budesonide"
        ],
        "correct_answer": "Acute severe ulcerative colitis; treat with intravenous hydrocortisone",
        "explanation": "Under the Truelove and Witts criteria, an ulcerative colitis flare is classified as 'acute severe' if the patient passes >=6 bloody stools per day PLUS has at least one feature of systemic toxicity: temperature >37.8°C, heart rate >90 bpm, haemoglobin <105 g/L, or ESR >30 mm/hr (all four are present here). Toxic megacolon requires colonic dilatation >6 cm. First-line management of acute severe ulcerative colitis is hospital admission for intravenous corticosteroids (IV hydrocortisone 100 mg four times daily or IV methylprednisolone) alongside prophylactic low-molecular-weight heparin."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 44-year-old man with chronic alcohol dependence and a BMI of 15.6 kg/m² is admitted to the medical ward after eating virtually nothing for 8 days. He is given intravenous thiamine (Pabrinex) and started on nasogastric enteral feeding. Forty-eight hours later, he develops generalised muscle weakness, paraesthesia, diplopia, and ventricular ectopics. Which biochemical abnormality is the primary hallmark of this complication?",
        "options": [
            "Severe hypophosphataemia",
            "Hypercalcaemia",
            "Hyperkalaemia",
            "Hypermagnesaemia",
            "Metabolic acidosis with raised anion gap"
        ],
        "correct_answer": "Severe hypophosphataemia",
        "explanation": "This patient has developed refeeding syndrome, which occurs when carbohydrate nutrition is reintroduced too rapidly after prolonged starvation (>5–10 days) or severe malnutrition. The sudden switch from fat/protein catabolism back to carbohydrate metabolism triggers an insulin surge that drives phosphate, potassium, and magnesium into cells alongside intracellular consumption of phosphate for ATP synthesis. Severe hypophosphataemia (accompanied by hypokalaemia, hypomagnesaemia, and thiamine depletion) is the hallmark biochemical feature, leading to respiratory muscle weakness, rhabdomyolysis, seizures, and cardiac arrhythmias."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 58-year-old man with decompensated alcohol-related liver cirrhosis and tense ascites is admitted with mild diffuse abdominal discomfort and new-onset grade 2 hepatic encephalopathy. He is afebrile (36.8°C). A diagnostic ascitic tap (paracentesis) is performed in the Emergency Department. Which ascitic fluid result is the diagnostic threshold for initiating empirical intravenous antibiotics for spontaneous bacterial peritonitis (SBP)?",
        "options": [
            "Ascitic fluid neutrophil count >=250 cells/mm³ (0.25 x 10⁹/L)",
            "Ascitic fluid total white cell count >=1,000 cells/mm³ (1.0 x 10⁹/L)",
            "Serum-ascites albumin gradient (SAAG) <11 g/L",
            "Positive Gram stain on ascitic fluid microscopy only",
            "Ascitic fluid pH <7.30 with elevated amylase"
        ],
        "correct_answer": "Ascitic fluid neutrophil count >=250 cells/mm³ (0.25 x 10⁹/L)",
        "explanation": "Spontaneous bacterial peritonitis (SBP) frequently presents subtly in cirrhotic patients—often with encephalopathy, worsening renal function, or mild abdominal pain without fever. Because ascitic fluid bacterial cultures take 48 hours and can be negative in up to 40% of cases, the diagnostic threshold to start immediate empirical intravenous antibiotics (e.g. cefotaxime or piperacillin-tazobactam) and intravenous human albumin solution is an ascitic fluid polymorphonuclear (neutrophil) count >=250 cells/mm³."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 41-year-old man attends his GP surgery with a 3-week history of solid food feeling as though it sticks transiently behind his sternum a few seconds after swallowing. His weight is stable, he has no odynophagia or vomiting, and his full blood count is normal (Hb 148 g/L). He smokes 10 cigarettes a day. According to NICE NG12 guidelines on suspected cancer, what is the most appropriate next step?",
        "options": [
            "Urgent 2-week wait referral for upper gastrointestinal endoscopy",
            "A 4-week trial of full-dose oral omeprazole 20 mg daily and review",
            "Carbon-13 urea breath test for Helicobacter pylori",
            "Routine barium swallow examination",
            "Reassurance and lifestyle advice on chewing food thoroughly"
        ],
        "correct_answer": "Urgent 2-week wait referral for upper gastrointestinal endoscopy",
        "explanation": "Under NICE NG12 guidelines for suspected upper gastrointestinal (oesophageal or gastric) cancer, dysphagia (at ANY age) or aged >=55 years with weight loss and upper abdominal pain, reflux, or dyspepsia requires an urgent 2-week wait referral for upper GI endoscopy (OGD). Unlike uncomplicated dyspepsia, true dysphagia is a red-flag symptom that must never be empirically treated with a trial of a proton pump inhibitor before endoscopic exclusion of malignancy."
    },

    # =========================================================================
    # 5. INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "An 18-year-old university student presented to an urgent care centre 4 days ago with fever, severe tonsillar exudates, and bilateral posterior cervical lymphadenopathy. She was prescribed oral amoxicillin for presumed bacterial tonsillitis. Today she attends her GP with a widespread, symmetrical, non-blanching-to-blanching maculopapular rash over her trunk and limbs, without facial oedema, wheeze, or hypotension. Abdominal palpation reveals mild splenomegaly. What is the most accurate explanation for her rash?",
        "options": [
            "A transient reaction to amoxicillin in the context of acute Epstein-Barr virus infection, not a true penicillin allergy",
            "An IgE-mediated type I hypersensitivity reaction requiring lifelong penicillin avoidance",
            "Scarlet fever caused by group A beta-haemolytic Streptococcus",
            "Stevens-Johnson syndrome triggered by beta-lactam antibiotics",
            "Secondary syphilis presenting during young adulthood"
        ],
        "correct_answer": "A transient reaction to amoxicillin in the context of acute Epstein-Barr virus infection, not a true penicillin allergy",
        "explanation": "The triad of pharyngitis, posterior cervical lymphadenopathy, and splenomegaly in a young adult is classic for infectious mononucleosis caused by Epstein-Barr virus (EBV). Administering aminopenicillins (amoxicillin or ampicillin) during acute EBV infection triggers a florid, generalised maculopapular exanthem in 80–90% of patients due to transient immune complex formation and altered drug metabolism. Crucially, this does not represent a true IgE-mediated penicillin allergy, and the patient should not be labelled penicillin-allergic for life."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 79-year-old man taking warfarin for a mechanical mitral valve presents to the Emergency Department with large-volume haematemesis and melaena. His blood pressure is 86/52 mmHg, heart rate is 118 bpm, haemoglobin is 74 g/L, and his INR returns at 6.8. Alongside haemodynamic resuscitation and withholding warfarin, what is the definitive immediate reversal regimen recommended by NICE and British Society for Haematology guidelines?",
        "options": [
            "Intravenous 4-factor prothrombin complex concentrate (PCC) plus intravenous phytomenadione (vitamin K1) 5 mg",
            "Intravenous phytomenadione (vitamin K1) 10 mg alone and recheck INR in 6 hours",
            "Four units of ABO-matched fresh frozen plasma (FFP) as first-line reversal",
            "Oral phytomenadione 5 mg plus intravenous tranexamic acid only",
            "Intravenous idarucizumab plus platelet transfusion"
        ],
        "correct_answer": "Intravenous 4-factor prothrombin complex concentrate (PCC) plus intravenous phytomenadione (vitamin K1) 5 mg",
        "explanation": "In life-threatening or major bleeding on warfarin (irrespective of the INR value), immediate reversal requires BOTH intravenous 4-factor prothrombin complex concentrate (PCC, e.g. Beriplex/Octaplex, containing factors II, VII, IX, and X) AND intravenous phytomenadione (vitamin K1) 5 mg. PCC normalises the INR within 10–15 minutes (unlike FFP, which requires ABO matching, thawing, and large fluid volumes), while IV vitamin K1 sustains endogenous clotting factor synthesis once the short half-life of factor VII in PCC wears off."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 56-year-old woman undergoing adjuvant FEC-T chemotherapy for breast cancer (last cycle administered 10 days ago) attends the Emergency Department feeling shivery and exhausted. Her temperature is 38.4°C, heart rate is 98 bpm, blood pressure is 116/72 mmHg, and respiratory rate is 18/min. She has no localising symptoms on initial history. Blood cultures and a full blood count are taken from her peripheral vein and PICC line. What is the most appropriate immediate next step?",
        "options": [
            "Administer empirical intravenous piperacillin with tazobactam immediately without waiting for the full blood count result",
            "Wait 45 minutes for the laboratory neutrophil count to confirm neutropenia (<0.5 x 10⁹/L) before prescribing antibiotics",
            "Administer subcutaneous granulocyte colony-stimulating factor (G-CSF) and observe for 4 hours",
            "Perform a chest X-ray and lumbar puncture prior to giving intravenous antibiotics",
            "Prescribe oral co-amoxiclav and ciprofloxacin and discharge with oncology follow-up tomorrow"
        ],
        "correct_answer": "Administer empirical intravenous piperacillin with tazobactam immediately without waiting for the full blood count result",
        "explanation": "Any patient who has received systemic anti-cancer therapy within the last 6 weeks (especially at the neutrophil nadir 7–14 days post-chemotherapy) presenting with a temperature >38.0°C or clinical signs of sepsis must be treated as having neutropenic sepsis until proven otherwise. NICE CG151 mandates immediate empirical intravenous piperacillin with tazobactam (Tazocin) within 1 hour of arrival—clinicians must never delay antibiotic administration while waiting for the laboratory full blood count to confirm a neutrophil count <=0.5 x 10⁹/L."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 62-year-old man with bulky, high-grade Burkitt lymphoma commences systemic R-CHOP chemotherapy. Thirty-six hours later, he develops nausea, lethargy, painful muscle spasms, and oliguria, with tall tented T waves on his ECG. Which combination of serum electrolyte and metabolic abnormalities defines this oncological emergency?",
        "options": [
            "Hyperkalaemia, hyperphosphataemia, hyperuricaemia, and hypocalcaemia",
            "Hyperkalaemia, hyperphosphataemia, hyperuricaemia, and hypercalcaemia",
            "Hypokalaemia, hypophosphataemia, hyperuricaemia, and hypercalcaemia",
            "Hyponatraemia, hypokalaemia, hypocalcaemia, and metabolic alkalosis",
            "Hypernatraemia, hypercalcaemia, hypophosphataemia, and hypoglycaemia"
        ],
        "correct_answer": "Hyperkalaemia, hyperphosphataemia, hyperuricaemia, and hypocalcaemia",
        "explanation": "Tumour lysis syndrome (TLS) occurs when rapid destruction of highly proliferative malignant cells (such as Burkitt lymphoma or acute leukaemia) releases vast quantities of intracellular ions and nucleic acids into the circulation. This produces the classic metabolic tetrad of 'three ups and one down': hyperkalaemia, hyperphosphataemia, and hyperuricaemia (from purine catabolism), accompanied by secondary hypocalcaemia because free serum calcium precipitates with the excess phosphate as calcium phosphate in tissues and renal tubules."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 29-year-old woman at 16 weeks gestation contacts her GP surgery after spending 3 hours indoors yesterday with her 4-year-old nephew, who developed a classic vesicular chickenpox rash this morning. She is currently asymptomatic but says she cannot remember ever having chickenpox as a child and has not been vaccinated against varicella. What is the most appropriate initial step in management?",
        "options": [
            "Check maternal serum for varicella-zoster virus (VZV) IgG antibodies urgently",
            "Prescribe oral aciclovir 800 mg five times daily immediately for 7 days",
            "Administer intramuscular varicella-zoster immunoglobulin (VZIG) today without blood testing",
            "Reassure her that chickenpox poses no risk to the fetus between 12 and 24 weeks gestation",
            "Admit immediately to the obstetric unit for intravenous aciclovir"
        ],
        "correct_answer": "Check maternal serum for varicella-zoster virus (VZV) IgG antibodies urgently",
        "explanation": "Significant contact is defined as face-to-face contact or >15 minutes in the same room with an infectious individual (who is contagious from 48 hours before rash onset until all vesicles crust over). Over 80% of UK-born adults who recall no history of chickenpox are actually immune on testing. Therefore, RCOG and UKHSA guidelines state that the first step in a pregnant woman with no definite history of varicella is to urgently test maternal serum (or stored antenatal booking blood) for VZV IgG antibodies. If she is seronegative (non-immune), post-exposure prophylaxis with oral aciclovir (from day 7 to 14 post-exposure) or VZIG is given."
    },

    # =========================================================================
    # 6. MUSCULOSKELETAL
    # =========================================================================
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 43-year-old man with a history of lower back pain presents to his GP with a 24-hour history of severe pain radiating down the back of both legs into his calves. On direct questioning, he mentions that his perineum felt numb when wiping himself after opening his bowels this morning, and he has had to strain to pass urine today. What is the single most appropriate immediate action?",
        "options": [
            "Emergency same-day hospital referral for an urgent MRI of the lumbosacral spine",
            "Request an urgent outpatient lumbar spine MRI under the 2-week wait pathway",
            "Prescribe oral naproxen and amitriptyline and review in 48 hours",
            "Arrange urgent plain radiographs of the lumbar spine and pelvis today",
            "Refer to the community musculoskeletal physiotherapy triage service"
        ],
        "correct_answer": "Emergency same-day hospital referral for an urgent MRI of the lumbosacral spine",
        "explanation": "Bilateral sciatica accompanied by 'red flag' sphincteric or perineal symptoms—specifically saddle/perineal anaesthesia, urinary hesitancy/retention, overflow incontinence, or reduced anal tone—indicates suspected cauda equina syndrome (most commonly caused by a large central L4/L5 or L5/S1 intervertebral disc prolapse). This is a neurosurgical emergency requiring immediate same-day hospital transfer for an emergency MRI of the lumbosacral spine and urgent surgical decompression to prevent permanent paraplegia and incontinence."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 72-year-old woman presents with a 6-week history of severe bilateral aching pain and morning stiffness across her shoulders, neck, and hips. The stiffness lasts for 2 hours each morning, making it difficult for her to get out of bed or raise her arms to brush her hair. She has no headache, visual disturbance, or jaw pain when chewing. On examination, active shoulder abduction is restricted by pain, but distal and proximal muscle power is normal (5/5) once supported. Blood tests show: Hb 114 g/L, ESR 68 mm/hr, CRP 52 mg/L, and creatine kinase (CK) 78 U/L (normal). What is the most appropriate initial treatment?",
        "options": [
            "Oral prednisolone 15 mg once daily",
            "Oral prednisolone 60 mg once daily",
            "Oral methotrexate 15 mg once weekly",
            "Oral ibuprofen 400 mg three times daily",
            "Intramuscular methylprednisolone 120 mg single dose only"
        ],
        "correct_answer": "Oral prednisolone 15 mg once daily",
        "explanation": "Subacute bilateral shoulder and pelvic girdle pain with prolonged morning stiffness (>45 minutes) in a patient aged >50 years with markedly elevated ESR/CRP and a normal serum creatine kinase (which excludes polymyositis) is the classic presentation of polymyalgia rheumatica (PMR). In the absence of cranial symptoms of giant cell arteritis (which would require 40–60 mg prednisolone), NICE guidelines recommend starting oral prednisolone 15 mg once daily, which characteristically produces a dramatic clinical improvement within 1 week."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 69-year-old man presents with a 12-hour history of an exquisitely painful, red, swollen right first metatarsophalangeal (MTP) joint that woke him at 3 am. He is afebrile and systemically well. His past medical history includes hypertension, chronic kidney disease stage 4 (eGFR 21 mL/min/1.73m²), and a peptic ulcer 3 years ago. He does not currently take urate-lowering therapy. What is the safest and most appropriate pharmacological treatment for this acute flare?",
        "options": [
            "Oral prednisolone 30–35 mg once daily for 5 days",
            "Oral naproxen 500 mg twice daily with omeprazole",
            "Oral allopurinol 100 mg once daily started immediately",
            "High-dose oral colchicine 1 mg followed by 500 mcg every 2 hours",
            "Oral febuxostat 80 mg once daily"
        ],
        "correct_answer": "Oral prednisolone 30–35 mg once daily for 5 days",
        "explanation": "This patient has acute gout (podagra). Normally, an NSAID (plus PPI) or low-dose colchicine is first-line for an acute flare. However, NSAIDs are contraindicated in stage 4 CKD (eGFR 21) and peptic ulcer disease, and colchicine carries a high risk of severe toxicity (myopathy,bone marrow suppression, and diarrhoea) in severe renal impairment. Therefore, a short course of an oral corticosteroid (prednisolone 30–35 mg daily for 5 days) or intra-articular steroid injection is the safest effective option. Urate-lowering therapy (allopurinol/febuxostat) must never be initiated during an acute flare as it prolongs and worsens the attack."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 76-year-old woman is reviewed in GP clinic after a DEXA scan performed following a Colles' wrist fracture shows a femoral neck T-score of -2.9. Her past medical history includes achalasia with delayed oesophageal emptying. Her eGFR is 66 mL/min/1.73m², and her serum calcium and vitamin D levels are normal. Why is oral alendronic acid contraindicated in this patient?",
        "options": [
            "Abnormalities of the oesophagus that delay oesophageal emptying predispose to severe chemical oesophagitis and ulceration",
            "Oral bisphosphonates relax the lower oesophageal sphincter via smooth muscle calcium channel blockade",
            "Achalasia prevents gastric acid secretion required to convert alendronate into its active metabolite",
            "Alendronic acid causes selective osteonecrosis of the cervical vertebrae in patients with dysphagia",
            "Oral bisphosphonates trigger autoimmune destruction of myenteric plexus ganglion cells"
        ],
        "correct_answer": "Abnormalities of the oesophagus that delay oesophageal emptying predispose to severe chemical oesophagitis and ulceration",
        "explanation": "Oral bisphosphonates (such as alendronic acid and risedronate) are direct mucosal irritants. That is why patients must take them on an empty stomach with a full glass of plain water and remain upright (sitting or standing) for at least 30 minutes before eating. They are strictly contraindicated in patients with oesophageal abnormalities that delay emptying—such as achalasia or oesophageal stricture—or those unable to sit upright for 30 minutes; parenteral alternatives (intravenous zoledronic acid or subcutaneous denosumab) should be used instead."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 32-year-old woman who gave birth 3 months ago presents with a 4-week history of worsening pain and swelling over the radial aspect of her right wrist, particularly when lifting her baby under the arms. Examination reveals localised tenderness over the tip of the radial styloid process. Asking her to tuck her thumb inside her closed fist and ulnar-deviating the wrist (Finkelstein's test) reproduces sharp pain along the radial wrist. Which tendons are affected in this condition?",
        "options": [
            "Abductor pollicis longus and extensor pollicis brevis",
            "Flexor pollicis longus and flexor carpi radialis",
            "Extensor pollicis longus and extensor carpi radialis brevis",
            "Abductor pollicis brevis and opponens pollicis",
            "Extensor digitorum and extensor indicis"
        ],
        "correct_answer": "Abductor pollicis longus and extensor pollicis brevis",
        "explanation": "Radial wrist pain exacerbated by repetitive thumb abduction/pinching (classically seen in new mothers lifting infants, sometimes called 'baby wrist') with radial styloid tenderness and a positive Finkelstein's test is diagnostic of De Quervain's stenosing tenosynovitis. It is caused by non-inflammatory thickening and entrapment of the tendons of the first dorsal extensor compartment of the wrist—specifically abductor pollicis longus (APL) and extensor pollicis brevis (EPB)—which form the anterior border of the anatomical snuffbox."
    },

    # =========================================================================
    # 7. PAEDIATRICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old boy is brought to his GP with a 2-day history of fever (38.9°C), sore throat, and headache. Today he developed a diffuse, blanching erythematous rash across his neck, chest, and axillae that feels like coarse sandpaper to touch. Examination of the oral cavity shows tonsillar exudates, palatal petechiae, and prominent red papillae protruding through a white coating on his tongue. He has no penicillin allergy. What is the correct antibiotic regimen and school exclusion advice?",
        "options": [
            "Oral phenoxymethylpenicillin (Penicillin V) for 10 days; he can return to school 24 hours after starting antibiotics",
            "Oral amoxicillin for 5 days; he must stay off school until the rash has completely desquamated",
            "Supportive care with paracetamol only as it is viral; no school exclusion is required",
            "Oral clarithromycin for 7 days; he must stay off school for 5 days from rash onset",
            "Urgent hospital admission for intravenous immunoglobulin (IVIG) and high-dose aspirin"
        ],
        "correct_answer": "Oral phenoxymethylpenicillin (Penicillin V) for 10 days; he can return to school 24 hours after starting antibiotics",
        "explanation": "Exudative tonsillitis accompanied by a coarse 'sandpaper' rash, Pastia's lines in skin creases, circumoral pallor, and a 'strawberry tongue' is classic for scarlet fever, caused by an erythrogenic exotoxin-producing strain of Streptococcus pyogenes (Group A Streptococcus). NICE and UKHSA guidelines recommend a 10-day course of oral phenoxymethylpenicillin (Penicillin V) to prevent rheumatic fever and peritonsillar abscess. Scarlet fever is a notifiable disease, and the child may return to school or nursery 24 hours after commencing antibiotic treatment (provided they feel well enough)."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 10-week-old exclusively formula-fed infant is brought to the GP with frequent posseting after feeds, loose stools containing occasional streaks of mucus, and an erythematous eczematous rash on his cheeks and trunk. He is alert, well hydrated, and tracking steadily along the 50th centile for weight and length. You suspect mild-to-moderate non-IgE-mediated cow's milk protein allergy (CMPA). According to NICE guidelines, what is the first-line formula replacement in primary care?",
        "options": [
            "An extensively hydrolysed formula (eHF)",
            "An amino acid-based formula (AAF)",
            "A soya-based infant formula",
            "A lactose-free cow's milk formula",
            "Goat's milk infant formula"
        ],
        "correct_answer": "An extensively hydrolysed formula (eHF)",
        "explanation": "In formula-fed infants with suspected mild-to-moderate IgE- or non-IgE-mediated cow's milk protein allergy (CMPA), the first-line diagnostic and therapeutic replacement in primary care is an extensively hydrolysed formula (eHF) for a 2–4 week elimination trial. Amino acid-based formulas (AAF) are reserved for severe CMPA (e.g. anaphylaxis, faltering growth, or symptoms failing to resolve on an eHF). Soya formula is not recommended under 6 months of age due to phytoestrogens and cross-reactivity, goat's milk shares high protein homology with cow's milk, and lactose-free formula still contains intact cow's milk proteins."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 4-year-old boy is brought to the Paediatric Assessment Unit after waking up with a right-sided limp. He had a mild viral upper respiratory tract infection 1 week ago. On examination, he is afebrile (36.6°C), looks well, and walks across the room with a mild antalgic gait. There is slight discomfort only at the extreme of internal rotation of the right hip, with no overlying erythema or knee swelling. Blood tests show: WCC 7.6 x 10⁹/L, CRP 3 mg/L, and ESR 10 mm/hr. What is the most likely diagnosis and appropriate management?",
        "options": [
            "Transient synovitis (irritable hip); manage with rest, oral ibuprofen, and safety-netting to return urgently if fever develops or he stops weight-bearing",
            "Septic arthritis; arrange immediate theatre hip arthrotomy and intravenous ceftriaxone",
            "Slipped capital femoral epiphysis (SCFE); keep nil by mouth for urgent percutaneous pinning",
            "Developmental dysplasia of the hip (DDH); apply a Pavlik harness for 6 weeks",
            "Juvenile idiopathic arthritis; initiate oral methotrexate and refer to paediatric rheumatology"
        ],
        "correct_answer": "Transient synovitis (irritable hip); manage with rest, oral ibuprofen, and safety-netting to return urgently if fever develops or he stops weight-bearing",
        "explanation": "Transient synovitis (irritable hip) is the commonest cause of acute hip pain in children aged 3–8 years, classically following a recent viral upper respiratory infection. The Kocher criteria help distinguish septic arthritis from transient synovitis using four predictors: (1) non-weight-bearing, (2) fever >38.5°C, (3) WCC >12 x 10⁹/L, and (4) ESR >40 mm/hr (or CRP >20 mg/L). With a Kocher score of 0 (afebrile, weight-bearing, normal inflammatory markers), septic arthritis is <0.2% likely; management is conservative with oral NSAIDs, rest, and clear safety-netting."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 20-month-old girl is brought to an out-of-hours GP clinic with a 24-hour history of coryza, a hoarse voice, and a harsh 'seal-like' barking cough. While sitting calmly on her father's lap, she has no audible stridor at rest, no intercostal or subcostal recession, normal colour, and oxygen saturations of 99% in air. A faint inspiratory stridor is heard only when she cries during examination. What is the most appropriate pharmacological treatment?",
        "options": [
            "A single dose of oral dexamethasone (0.15 mg/kg)",
            "Reassurance and steam inhalation only, as steroids are reserved for stridor at rest",
            "Nebulised adrenaline (epinephrine) 1:1000 and immediate ambulance transfer",
            "Oral amoxicillin 125 mg three times daily for 5 days",
            "Inhaled salbutamol 100 mcg via spacer four times daily"
        ],
        "correct_answer": "A single dose of oral dexamethasone (0.15 mg/kg)",
        "explanation": "A barking cough and hoarse voice with stridor audible only on agitation/crying (and absent at rest, with no chest wall recession) classifies this as mild viral laryngotracheobronchitis (croup). Crucially, NICE guidelines state that ALL children with croup—whether mild, moderate, or severe—should receive a single dose of oral dexamethasone (0.15 mg/kg), as it reduces symptom duration, return visits, and progression to airway obstruction. Children with mild croup can be safely managed at home after receiving oral dexamethasone, whereas stridor at rest or recession (moderate/severe croup) requires hospital admission."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 5-day-old term neonate, born at 39 weeks following an uncomplicated pregnancy and normal vaginal delivery, is brought to the Emergency Department with two episodes of dark green (bilious) vomiting over the past 3 hours. The baby passed meconium within 12 hours of birth. On examination, the abdomen is currently soft and non-distended, capillary refill is 2 seconds, and heart rate is 150 bpm. What is the most important urgent diagnostic investigation to exclude the most time-critical surgical emergency?",
        "options": [
            "Urgent upper gastrointestinal contrast study",
            "Abdominal ultrasound looking for a pyloric 'olive' mass",
            "Rectal suction biopsy for submucosal ganglion cells",
            "Diagnostic pneumatic air enema",
            "24-hour oesophageal pH and impedance monitoring"
        ],
        "correct_answer": "Urgent upper gastrointestinal contrast study",
        "explanation": "Dark green (bilious) vomiting in a neonate is intestinal malrotation with midgut volvulus until proven otherwise. Even if the abdomen initially feels soft and non-distended, twisting of the midgut around the superior mesenteric artery axis can rapidly cause catastrophic total small bowel necrosis within hours. While a plain abdominal X-ray is often performed quickly, the gold-standard investigation to diagnose malrotation/volvulus is an urgent upper gastrointestinal water-soluble contrast study, which demonstrates an abnormally positioned duodenojejunal flexure (ligament of Treitz) to the right of the midline or a 'corkscrew' duodenum."
    },

    # =========================================================================
    # 8. PHARMACOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 68-year-old woman taking once-weekly oral methotrexate and folic acid for rheumatoid arthritis attends her GP surgery with a 2-day history of dysuria and urinary frequency. Urine dipstick is positive for nitrites and leucocytes. Her eGFR is 68 mL/min/1.73m². Why is prescribing trimethoprim strictly contraindicated in this patient?",
        "options": [
            "Both drugs inhibit dihydrofolate reductase, causing additive folate antagonism and life-threatening pancytopenia",
            "Trimethoprim induces hepatic CYP3A4, causing acute rheumatoid arthritis flare",
            "Co-administration precipitates acute uric acid nephropathy and renal cortical necrosis",
            "Trimethoprim displaces methotrexate from red blood cell haemoglobin, causing methemoglobinaemia",
            "Combined therapy causes irreversible cholestatic hepatitis within 24 hours"
        ],
        "correct_answer": "Both drugs inhibit dihydrofolate reductase, causing additive folate antagonism and life-threatening pancytopenia",
        "explanation": "Methotrexate and trimethoprim (as well as co-trimoxazole) both act as folate antagonists by inhibiting dihydrofolate reductase, blocking the conversion of dihydrofolic acid to tetrahydrofolic acid required for DNA synthesis. Furthermore, trimethoprim reduces renal tubular secretion of methotrexate. Co-prescribing them causes severe, potentially fatal bone marrow suppression (myelosuppression/pancytopenia) and mucositis. Nitrofurantoin (provided eGFR >=45 mL/min/1.73m²) is a safe first-line alternative for her uncomplicated lower UTI."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 71-year-old man with a documented history of penicillin anaphylaxis is diagnosed with moderate community-acquired pneumonia and prescribed oral clarithromycin 500 mg twice daily for 5 days. His regular repeat medications are ramipril 10 mg daily, amlodipine 5 mg daily, and atorvastatin 40 mg nightly. What medication adjustment must be made when issuing this prescription?",
        "options": [
            "Temporarily withhold atorvastatin while he is taking clarithromycin to prevent myopathy and rhabdomyolysis",
            "Temporarily withhold ramipril to prevent acute hyperkalaemia",
            "Double the dose of atorvastatin to 80 mg nightly due to enzyme induction",
            "Switch amlodipine to verapamil for the duration of antibiotic therapy",
            "No adjustment is needed as atorvastatin is excreted unchanged by the kidneys"
        ],
        "correct_answer": "Temporarily withhold atorvastatin while he is taking clarithromycin to prevent myopathy and rhabdomyolysis",
        "explanation": "Macrolide antibiotics—specifically clarithromycin and erythromycin—are potent inhibitors of the hepatic cytochrome P450 3A4 (CYP3A4) isoenzyme and organic anion-transporting polypeptide (OATP1B1). Because simvastatin and atorvastatin are extensively metabolised by CYP3A4, co-administration with clarithromycin markedly elevates plasma statin concentrations and can precipitate severe myopathy and acute rhabdomyolysis. BNF guidance states that simvastatin or atorvastatin should be temporarily paused during a short course of clarithromycin."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 59-year-old man who takes sertraline 100 mg daily for generalised anxiety disorder attends his GP with an acute flare of knee osteoarthritis. Topical NSAIDs have been ineffective, and you decide to prescribe a short course of oral naproxen alongside gastroprotection with lansoprazole. By what pharmacological mechanism do SSRIs like sertraline substantially increase the risk of upper gastrointestinal bleeding when combined with NSAIDs?",
        "options": [
            "SSRIs inhibit serotonin reuptake into platelets, depleting platelet serotonin stores required for aggregation",
            "SSRIs directly stimulate parietal cell H+/K+-ATPase pumps to double gastric acid output",
            "SSRIs inhibit hepatic cyclooxygenase-1 (COX-1), blocking prostaglandin E2 synthesis",
            "SSRIs displace naproxen from plasma albumin, causing direct mucosal chemical burns",
            "SSRIs impair hepatic synthesis of vitamin K-dependent clotting factors II, VII, IX, and X"
        ],
        "correct_answer": "SSRIs inhibit serotonin reuptake into platelets, depleting platelet serotonin stores required for aggregation",
        "explanation": "Platelets cannot synthesise serotonin (5-HT) endogenously and rely entirely on the serotonin transporter (SERT) to take up serotonin from the bloodstream. When vascular injury occurs, platelets release stored serotonin to promote vasoconstriction and amplify ADP-induced platelet aggregation. SSRIs block platelet SERT, depleting intraplatelet serotonin and impairing primary haemostasis. When combined with NSAID-induced gastric mucosal injury, the relative risk of upper GI bleeding increases synergistically (up to 6- to 10-fold), mandating co-prescription of a proton pump inhibitor."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 52-year-old woman with bipolar I disorder has been stable on lithium carbonate for 6 years, with consistent 12-hour trough serum lithium levels around 0.7 mmol/L. Two weeks ago, she was started on bendroflumethiazide 2.5 mg daily for hypertension. She now presents to the Emergency Department with nausea, a coarse hand tremor, dysarthria, and ataxia, and her serum lithium level is 2.1 mmol/L. How did bendroflumethiazide precipitate lithium toxicity?",
        "options": [
            "Distal convoluted tubule sodium depletion triggers a compensatory increase in proximal tubular reabsorption of both sodium and lithium",
            "Thiazide diuretics inhibit hepatic glucuronidation of lithium carbonate",
            "Hypokalaemia increases the blood-brain barrier permeability to lithium ions",
            "Thiazides directly compete with lithium for active secretion in the collecting duct",
            "Metabolic alkalosis converts ionised lithium into lipid-soluble non-ionised lithium"
        ],
        "correct_answer": "Distal convoluted tubule sodium depletion triggers a compensatory increase in proximal tubular reabsorption of both sodium and lithium",
        "explanation": "Lithium is a monovalent cation handled by the kidneys in the same way as sodium: approximately 70–80% of filtered lithium is reabsorbed in the proximal convoluted tubule alongside sodium. When a thiazide diuretic inhibits the Na+/Cl- cotransporter in the distal convoluted tubule, the resulting mild extracellular volume and sodium depletion stimulates a compensatory increase in proximal tubular sodium (and therefore lithium) reabsorption, reducing renal lithium clearance by 25–40% and rapidly precipitating toxicity."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 67-year-old man with type 2 diabetes and hypertension telephones the GP surgery with a 36-hour history of profuse watery diarrhoea and vomiting. He is unable to keep fluids down. His regular medications are metformin, ramipril, and atorvastatin. You advise him to temporarily withhold ramipril and metformin ('sick day rules'). What specific life-threatening metabolic complication is prevented by suspending metformin during acute dehydration?",
        "options": [
            "Lactic acidosis",
            "Hyperosmolar hyperglycaemic state (HHS)",
            "Severe hypoglycaemic coma",
            "Syndrome of inappropriate ADH secretion (SIADH)",
            "Acute hepatic necrosis"
        ],
        "correct_answer": "Lactic acidosis",
        "explanation": "Metformin reduces hepatic gluconeogenesis (including conversion of lactate to glucose) and is excreted unchanged by the kidneys. During acute dehydrating illnesses (gastroenteritis, sepsis, or acute kidney injury), reduced renal perfusion causes metformin to accumulate in plasma, while tissue hypoperfusion increases anaerobic lactate production—precipitating life-threatening metformin-associated lactic acidosis (MALA). Under 'sick day rules', patients must temporarily pause metformin (and ACE inhibitors/ARBs, diuretics, and SGLT2 inhibitors) until they are eating and drinking normally for 24–48 hours."
    },

    # =========================================================================
    # 9. PSYCHIATRY / NEUROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 74-year-old man is brought to the neurology clinic by his daughter with a 9-month history of progressive difficulty walking, urinary urgency with episodes of incontinence, and slowed thinking and forgetfulness. On examination, he has a broad-based, shuffling 'magnetic' gait where his feet appear stuck to the floor on initiating movement, but there is no resting tremor and upper limb tone is normal. CT head demonstrates marked enlargement of the lateral and third ventricles out of proportion to cortical sulcal atrophy. What is the definitive surgical treatment?",
        "options": [
            "Ventriculoperitoneal (VP) shunt insertion",
            "Deep brain stimulation of the subthalamic nucleus",
            "Bilateral decompressive craniectomy",
            "Endoscopic third ventriculostomy for aqueductal stenosis",
            "Carotid endarterectomy"
        ],
        "correct_answer": "Ventriculoperitoneal (VP) shunt insertion",
        "explanation": "The clinical triad of gait apraxia ('magnetic' shuffling gait—typically the earliest feature), urinary urgency/incontinence, and subcortical cognitive decline ('wet, wobbly, and wacky'), combined with ventriculomegaly disproportionate to cerebral sulcal atrophy on neuroimaging, is characteristic of Normal Pressure Hydrocephalus (NPH). Unlike Alzheimer's or Parkinson's dementia, NPH is a potentially reversible cause of cognitive and motor decline; following a positive high-volume CSF tap test (lumbar puncture drainage trial), definitive treatment is ventriculoperitoneal (VP) shunting."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 28-year-old man taking fluoxetine 40 mg daily for depression attends the Emergency Department 6 hours after taking several doses of tramadol for acute back pain alongside an over-the-counter dextromethorphan cough suppressant. He is agitated, restless, and profusely sweaty. His temperature is 38.9°C, heart rate is 132 bpm, and blood pressure is 164/98 mmHg. Neurological examination reveals dilated pupils, marked lower-limb hyperreflexia, and inducible bilateral ankle clonus. What is the diagnosis?",
        "options": [
            "Serotonin syndrome",
            "Neuroleptic malignant syndrome",
            "Anticholinergic toxidrome",
            "Malignant hyperthermia",
            "Opioid overdose"
        ],
        "correct_answer": "Serotonin syndrome",
        "explanation": "Both tramadol and dextromethorphan inhibit serotonin reuptake; combining them with an SSRI (fluoxetine) precipitates acute serotonin toxicity (serotonin syndrome). It is distinguished from neuroleptic malignant syndrome (NMS) by its rapid onset (within hours rather than days) and its classic neuromuscular signs: hyperreflexia, myoclonus, and inducible/spontaneous clonus (typically more pronounced in the lower limbs), alongside autonomic instability and agitation. In contrast, NMS (triggered by dopamine antagonists) features 'lead-pipe' muscular rigidity and hyporeflexia."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 73-year-old woman presents to her GP with a 10-day history of a throbbing right temporal headache, scalp tenderness when brushing her hair, and aching in her jaw muscles when chewing meat. This morning she experienced two 15-minute episodes of painless complete loss of vision in her right eye (amaurosis fugax). On examination, the right superficial temporal artery is thickened, tender, and non-pulsatile. What is the most appropriate immediate management?",
        "options": [
            "Same-day emergency ophthalmology referral for intravenous methylprednisolone (giving 60 mg oral prednisolone immediately if there is any delay)",
            "Start oral prednisolone 15 mg daily and arrange a routine temporal artery ultrasound within 2 weeks",
            "Start oral aspirin 300 mg only and refer to the TIA clinic within 7 days",
            "Withhold corticosteroids until a temporal artery biopsy has been performed to avoid false-negative histology",
            "Prescribe oral sumatriptan 50 mg and review in 48 hours"
        ],
        "correct_answer": "Same-day emergency ophthalmology referral for intravenous methylprednisolone (giving 60 mg oral prednisolone immediately if there is any delay)",
        "explanation": "Jaw claudication, scalp tenderness, and a tender non-pulsatile temporal artery in a patient aged >50 years indicate giant cell (temporal) arteritis (GCA). Transient monocular visual loss (amaurosis fugax) or diplopia is a critical warning sign of impending irreversible anterior ischaemic optic neuropathy (permanent blindness). While uncomplicated GCA is treated with oral prednisolone 40–60 mg daily, GCA WITH visual symptoms requires immediate same-day ophthalmology assessment for pulsed intravenous methylprednisolone (500 mg–1 g daily for 3 days), giving 60 mg oral prednisolone immediately before transfer if there is any delay."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 68-year-old man presents to the Emergency Department with left-sided arm and leg weakness that began 10 hours ago. Non-contrast CT head excludes intracerebral haemorrhage and confirms an acute right middle cerebral artery ischaemic stroke. He is outside the window for intravenous thrombolysis and mechanical thrombectomy. His 12-lead ECG and 24-hour telemetry show normal sinus rhythm. According to NICE guidelines, what is the standard antiplatelet regimen for acute management followed by long-term secondary prevention?",
        "options": [
            "Aspirin 300 mg daily for 14 days, followed by clopidogrel 75 mg daily long-term",
            "Clopidogrel 75 mg daily immediately without initial aspirin",
            "Aspirin 75 mg daily plus dipyridamole 200 mg twice daily indefinitely",
            "Apixaban 5 mg twice daily started immediately",
            "Dual antiplatelet therapy with aspirin 75 mg and ticagrelor 90 mg twice daily for 12 months"
        ],
        "correct_answer": "Aspirin 300 mg daily for 14 days, followed by clopidogrel 75 mg daily long-term",
        "explanation": "Under NICE NG128 guidelines for acute ischaemic stroke (once intracerebral haemorrhage has been excluded by neuroimaging), patients who do not have atrial fibrillation are given aspirin 300 mg daily (orally or rectally/via NG tube if dysphagic, alongside a PPI) as soon as possible and continued for 14 days. After 14 days (or on hospital discharge if earlier), they are switched to long-term clopidogrel 75 mg once daily monotherapy as first-line secondary prevention."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 61-year-old man who suffered an acute anterior ST-elevation myocardial infarction 6 weeks ago attends his GP with a 1-month history of persistent low mood, anhedonia, feelings of worthlessness, and early morning wakening. Following discussion, he wishes to start an antidepressant alongside cognitive behavioural therapy. Which antidepressant is the safest first-line pharmacological choice in a patient with a recent myocardial infarction?",
        "options": [
            "Sertraline",
            "Citalopram",
            "Amitriptyline",
            "Venlafaxine",
            "Phenelzine"
        ],
        "correct_answer": "Sertraline",
        "explanation": "Sertraline is the first-line SSRI of choice in patients with recent myocardial infarction or unstable angina, supported by randomised trial evidence (SADHART) demonstrating cardiac safety without pro-arrhythmic effects. In contrast, citalopram and escitalopram cause dose-dependent QT-interval prolongation (predisposing to torsades de pointes), tricyclic antidepressants (amitriptyline, dosulepin) are cardiotoxic and pro-arrhythmic via sodium channel blockade, and venlafaxine can exacerbate hypertension and tachycardia."
    },

    # =========================================================================
    # 10. RENAL / UROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 66-year-old man with hypertension and type 2 diabetes is started on ramipril 2.5 mg once daily. Baseline blood tests prior to starting treatment showed: Na+ 139 mmol/L, K+ 4.4 mmol/L, creatinine 100 umol/L, and eGFR 68 mL/min/1.73m². Repeat renal profile 2 weeks after starting ramipril shows: Na+ 138 mmol/L, K+ 4.8 mmol/L, creatinine 118 umol/L, and eGFR 56 mL/min/1.73m². His blood pressure has improved to 134/80 mmHg. According to NICE guidelines, what is the most appropriate action?",
        "options": [
            "Continue ramipril at the current dose and recheck renal function and potassium in 1–2 weeks",
            "Stop ramipril immediately and refer urgently for CT renal angiography to exclude renal artery stenosis",
            "Switch ramipril to losartan 50 mg daily as ARBs do not affect glomerular filtration rate",
            "Add oral sodium zirconium cyclosilicate to lower his potassium below 4.5 mmol/L",
            "Halve the ramipril dose and start furosemide 40 mg daily"
        ],
        "correct_answer": "Continue ramipril at the current dose and recheck renal function and potassium in 1–2 weeks",
        "explanation": "ACE inhibitors and ARBs dilate the glomerular efferent arteriole, reducing intraglomerular filtration pressure. Consequently, a modest rise in serum creatinine of up to 30% from baseline (here it rose from 100 to 118 umol/L, an 18% increase) or a fall in eGFR of up to 25% (here an 18% decrease), along with a modest rise in potassium (provided K+ remains <5.5 mmol/L), is an expected physiological effect and actually predicts long-term renoprotection. NICE guidelines advise continuing the ACE inhibitor unless serum creatinine rises by >30%, eGFR falls by >25%, or K+ reaches >=5.5–6.0 mmol/L."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 15-year-old boy is brought to the Emergency Department with a 2-hour history of sudden-onset, severe right-sided scrotal and lower abdominal pain accompanied by two episodes of vomiting. On examination, he is afebrile, the right hemiscrotum is erythematous and swollen, the right testis lies high and transversely ('bell-clapper' position), and the right cremasteric reflex is absent. Urine dipstick is completely negative. What is the single most appropriate immediate action?",
        "options": [
            "Immediate surgical referral for emergency scrotal exploration and bilateral orchidopexy",
            "Request an urgent departmental Doppler ultrasound of the testes to confirm reduced blood flow",
            "Administer intramuscular ceftriaxone and oral doxycycline for acute epididymo-orchitis",
            "Attempt manual detorsion in the Emergency Department and discharge if pain improves",
            "Arrange an urgent CT scan of the abdomen and pelvis to exclude a ureteric calculus"
        ],
        "correct_answer": "Immediate surgical referral for emergency scrotal exploration and bilateral orchidopexy",
        "explanation": "Sudden-onset severe scrotal/lower abdominal pain with nausea/vomiting, a high-riding transversely orientated testis, and an absent cremasteric reflex in an adolescent is acute testicular torsion until proven otherwise. Testicular viability drops precipitously after 6 hours of ischaemia. Clinical suspicion mandates immediate surgical scrotal exploration (with detorsion and bilateral orchidopexy, as the bell-clapper deformity is usually bilateral)—clinicians must NEVER delay theatre for a scrotal Doppler ultrasound."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 69-year-old man has been taking finasteride 5 mg daily and tamsulosin 400 mcg daily for the past 9 months for lower urinary tract symptoms secondary to benign prostatic hyperplasia. He attends his GP requesting a prostate-specific antigen (PSA) blood test after his older brother was diagnosed with prostate cancer. His serum PSA result returns at 2.8 ng/mL (laboratory age-specific upper limit of normal for a 60–69-year-old is 4.0 ng/mL). How should this result be interpreted and managed?",
        "options": [
            "Finasteride halves serum PSA levels; his corrected PSA is approximately 5.6 ng/mL, warranting an urgent 2-week wait urology referral",
            "Reassure him that his PSA of 2.8 ng/mL is well below the 4.0 ng/mL threshold and no further action is needed",
            "Stop tamsulosin for 2 weeks and repeat the PSA test, as alpha-blockers falsely lower PSA",
            "Treat empirically with a 4-week course of ciprofloxacin for subclinical prostatitis and repeat PSA",
            "Reassure him that benign prostatic hyperplasia treatment completely prevents prostate adenocarcinoma"
        ],
        "correct_answer": "Finasteride halves serum PSA levels; his corrected PSA is approximately 5.6 ng/mL, warranting an urgent 2-week wait urology referral",
        "explanation": "5-alpha-reductase inhibitors (finasteride and dutasteride) block the conversion of testosterone to dihydrotestosterone (DHT), shrinking prostatic glandular tissue and reducing serum PSA concentrations by approximately 50% after 6 months of treatment. Therefore, when interpreting a PSA level in a patient taking finasteride or dutasteride for >=6 months, the measured PSA value must be DOUBLED (2.8 x 2 = 5.6 ng/mL). Because his corrected PSA of 5.6 ng/mL exceeds the age-specific threshold of 4.0 ng/mL, an urgent 2-week wait referral for suspected prostate cancer is required."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 39-year-old man presents to the Emergency Department with a 3-hour history of sudden-onset, excruciating left loin-to-groin pain that comes in waves. He is restless and pacing the cubicle. His temperature is 36.7°C, heart rate is 92 bpm, blood pressure is 138/84 mmHg, and eGFR is >90 mL/min/1.73m². Urine dipstick shows +++ blood and is negative for nitrites and leucocytes. According to NICE guidelines, what is the first-line analgesia and gold-standard diagnostic imaging?",
        "options": [
            "An NSAID (by any route) for analgesia, and a low-dose non-contrast CT KUB within 24 hours",
            "Intravenous morphine as first-line analgesia, and an intravenous urogram (IVU)",
            "Oral tamsulosin for immediate pain relief, and a plain abdominal radiograph (KUB X-ray)",
            "Oral codeine phosphate, and a renal tract ultrasound within 72 hours",
            "Intravenous paracetamol only, and a contrast-enhanced CT abdomen and pelvis"
        ],
        "correct_answer": "An NSAID (by any route) for analgesia, and a low-dose non-contrast CT KUB within 24 hours",
        "explanation": "NICE NG118 guidelines on renal and ureteric stones recommend offering an NSAID (such as intramuscular/rectal diclofenac, IV ketorolac, or oral ibuprofen) by any route as first-line analgesia for suspected renal colic, as NSAIDs directly inhibit prostaglandin-mediated afferent arteriolar vasodilatation and ureteric smooth muscle spasm, providing superior pain relief to opioids. The gold-standard diagnostic imaging for non-pregnant adults is an urgent low-dose non-contrast CT of the kidneys, ureters, and bladder (CT KUB) performed within 24 hours (sensitivity and specificity >95%)."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 22-year-old man presents to his GP after noticing painless, frank red/cola-coloured urine this morning. He developed a viral sore throat and coryza 36 hours ago. He reports having had a similar 2-day episode of dark urine during a cold 18 months ago that resolved spontaneously. On examination, his blood pressure is 124/76 mmHg and there is no peripheral oedema. Serum creatinine is 82 umol/L and complement C3 and C4 levels are normal. What is the most likely diagnosis?",
        "options": [
            "IgA nephropathy (Berger's disease)",
            "Post-streptococcal glomerulonephritis",
            "Minimal change disease",
            "Goodpasture's syndrome (anti-GBM disease)",
            "Alport syndrome"
        ],
        "correct_answer": "IgA nephropathy (Berger's disease)",
        "explanation": "Recurrent painless macroscopic haematuria occurring within 24–72 hours of a mucosal viral upper respiratory or gastrointestinal infection ('synpharyngitic haematuria') in a young adult with normal serum complement levels is the classic presentation of IgA nephropathy (Berger's disease), the commonest primary glomerulonephritis worldwide. This timing distinguishes it from post-streptococcal glomerulonephritis, which presents after a latent period of 1 to 3 weeks following a streptococcal throat or skin infection and features low serum C3 levels."
    },

    # =========================================================================
    # 11. REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 26-year-old woman attends a sexual health clinic requesting emergency contraception 84 hours (3.5 days) after an episode of unprotected sexual intercourse on day 11 of her regular 28-day menstrual cycle. She is counselled that the copper intrauterine device (Cu-IUD) is the most effective method overall, but she declines an intrauterine procedure and requests an oral tablet. She has no medical conditions and takes no regular medications. Which oral emergency contraceptive is indicated?",
        "options": [
            "Ulipristal acetate 30 mg single oral dose",
            "Levonorgestrel 1.5 mg single oral dose",
            "Levonorgestrel 3 mg double oral dose",
            "Oral mifepristone 200 mg followed by misoprostol",
            "Desogestrel 75 mcg daily started immediately"
        ],
        "correct_answer": "Ulipristal acetate 30 mg single oral dose",
        "explanation": "While the copper IUD is the most effective emergency contraceptive (effective up to 5 days after UPSI or up to 5 days after the earliest estimated date of ovulation), if a woman declines a Cu-IUD at 84 hours (3.5 days) post-UPSI, ulipristal acetate (ellaOne 30 mg) is the only licensed and effective oral option. Levonorgestrel (Levonelle) is licensed only up to 72 hours (3 days) post-UPSI and cannot inhibit ovulation once the luteinising hormone (LH) surge has begun, whereas ulipristal acetate (a selective progesterone receptor modulator) remains effective up to 120 hours (5 days) and works even up to the peak of the LH surge."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 41-year-old woman in her first pregnancy attends her booking midwife appointment at 10 weeks gestation. Her booking blood pressure is 120/74 mmHg, her BMI is 36 kg/m², and urine dipstick is negative for protein. She has no past medical history of chronic hypertension, diabetes, or renal disease. According to NICE guidelines on hypertension in pregnancy, what prophylactic medication should be advised?",
        "options": [
            "Oral aspirin 75–150 mg once daily from 12 weeks gestation until birth",
            "Oral labetalol 100 mg twice daily starting immediately",
            "High-dose folic acid 5 mg daily until 36 weeks gestation only",
            "Subcutaneous enoxaparin 40 mg daily from 28 weeks gestation only",
            "No pharmacological prophylaxis is required as her booking blood pressure is normal"
        ],
        "correct_answer": "Oral aspirin 75–150 mg once daily from 12 weeks gestation until birth",
        "explanation": "NICE NG133 guidelines recommend low-dose aspirin (75–150 mg once daily at night from 12 weeks gestation until birth) to reduce the risk of pre-eclampsia in women with EITHER 1 high risk factor (hypertensive disease in a previous pregnancy, CKD, autoimmune disease such as SLE/APS, type 1 or 2 diabetes, or chronic hypertension) OR >=2 moderate risk factors: (1) first pregnancy (nulliparity), (2) age >=40 years, (3) pregnancy interval >10 years, (4) BMI >=35 kg/m² at booking, (5) family history of pre-eclampsia, or (6) multiple pregnancy. This patient has three moderate risk factors (primigravida, age 41, BMI 36)."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 29-year-old woman at 6 weeks gestation attends the Early Pregnancy Assessment Unit with mild left iliac fossa discomfort and light brownish vaginal spotting. She is haemodynamically stable (BP 118/72 mmHg, HR 70 bpm) and her abdomen is soft with no guarding or rebound tenderness. Transvaginal ultrasound shows an empty uterine cavity and an unruptured 22 mm left tubal ectopic pregnancy with no visible fetal heartbeat and no free pelvic fluid. Her serum beta-hCG is 1,150 IU/L. She wishes to avoid surgery if safe. Why is she eligible for systemic methotrexate therapy?",
        "options": [
            "She is haemodynamically stable without significant pain, the unruptured adnexal mass is <35 mm with no fetal heartbeat, and serum beta-hCG is <1,500 IU/L",
            "Methotrexate can be used in any ectopic pregnancy regardless of beta-hCG level provided there is no vaginal bleeding",
            "Presence of a visible fetal heartbeat on ultrasound is required before methotrexate can target trophoblastic tissue",
            "Systemic methotrexate is only offered when serum beta-hCG is above 5,000 IU/L and the mass is >40 mm",
            "She is eligible only because the ectopic pregnancy is located in the left fallopian tube rather than the right"
        ],
        "correct_answer": "She is haemodynamically stable without significant pain, the unruptured adnexal mass is <35 mm with no fetal heartbeat, and serum beta-hCG is <1,500 IU/L",
        "explanation": "Under NICE NG126 guidelines, systemic single-dose intramuscular methotrexate is a safe first-line medical option for tubal ectopic pregnancy when all of the following criteria are met: no significant pain, unruptured tubal ectopic pregnancy with an adnexal mass smaller than 35 mm, no visible fetal heartbeat, serum beta-hCG <1,500 IU/L (or between 1,500 and 5,000 IU/L alongside surgical options), no intrauterine pregnancy, and the patient is able to attend for repeat beta-hCG monitoring on days 4 and 7."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 49-year-old woman attends her GP with troublesome vasomotor symptoms (frequent hot flushes and drenching night sweats) that are severely affecting her sleep and work. Her menstrual periods have become irregular over the past year, and her last menstrual period was 4 months ago. She has an intact uterus and no history of breast cancer, venous thromboembolism, or cardiovascular disease. Which hormone replacement therapy (HRT) regimen is appropriate?",
        "options": [
            "Sequential (cyclical) combined HRT (oestrogen daily plus progestogen for 12–14 days per cycle)",
            "Continuous combined HRT (oestrogen and progestogen taken every day without a break)",
            "Unopposed transdermal oestradiol monotherapy",
            "Topical vaginal oestriol cream alone",
            "Oral tibolone started immediately"
        ],
        "correct_answer": "Sequential (cyclical) combined HRT (oestrogen daily plus progestogen for 12–14 days per cycle)",
        "explanation": "Choosing the right systemic HRT regimen depends on two key questions: (1) Does the patient have a uterus? Yes—so progestogen must be co-prescribed alongside oestrogen to prevent unopposed oestrogen-induced endometrial hyperplasia and adenocarcinoma. (2) Has it been >=12 months since her last menstrual period? No—her last period was 4 months ago (perimenopausal), so she must be prescribed sequential (cyclical) combined HRT, which produces a regular monthly withdrawal bleed. Starting continuous combined HRT (or tibolone) within 12 months of the last period causes erratic, unscheduled breakthrough bleeding."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 31-year-old woman at 9 weeks gestation presents to her GP with a 2-day history of dysuria and urinary frequency. She has no fever or loin pain. Urine dipstick is positive for nitrites and leucocytes. A midstream urine specimen is sent for culture and sensitivity, and a 7-day course of oral nitrofurantoin is prescribed. Why was trimethoprim avoided in this patient, and at what stage of pregnancy must nitrofurantoin itself be avoided?",
        "options": [
            "Trimethoprim is a folate antagonist (teratogenic in the 1st trimester); nitrofurantoin is avoided at term/3rd trimester due to the risk of neonatal haemolysis",
            "Trimethoprim causes neonatal haemolysis in the 1st trimester; nitrofurantoin causes fetal neural tube defects in the 3rd trimester",
            "Trimethoprim causes premature closure of the ductus arteriosus; nitrofurantoin causes congenital deafness",
            "Trimethoprim stains fetal teeth yellow; nitrofurantoin causes maternal agranulocytosis at term",
            "Both antibiotics are contraindicated throughout all three trimesters of pregnancy"
        ],
        "correct_answer": "Trimethoprim is a folate antagonist (teratogenic in the 1st trimester); nitrofurantoin is avoided at term/3rd trimester due to the risk of neonatal haemolysis",
        "explanation": "All symptomatic UTIs and asymptomatic bacteriuria in pregnancy require a 7-day antibiotic course with urine culture. Trimethoprim inhibits dihydrofolate reductase (a folate antagonist) and is avoided in the first trimester due to the risk of neural tube defects and congenital malformations during organogenesis. Conversely, nitrofurantoin is safe in the first and second trimesters, but must be avoided at term (and in the late third trimester) because immature neonatal erythrocyte enzyme systems (glutathione instability) predispose the newborn to haemolytic anaemia and neonatal jaundice."
    },

    # =========================================================================
    # 12. RESPIRATORY
    # =========================================================================
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 24-year-old woman with asthma is brought to the Emergency Department with acute shortness of breath. She is unable to complete sentences in one breath. Her respiratory rate is 28 breaths/min, heart rate is 118 bpm, peak expiratory flow (PEF) is 38% of predicted, and SpO2 is 93% on supplemental oxygen. An arterial blood gas shows: pH 7.36, PaO2 9.6 kPa, PaCO2 5.3 kPa (normal range 4.7–6.0 kPa), and bicarbonate 23 mmol/L. According to BTS/SIGN and NICE guidelines, how is the severity of this asthma exacerbation classified?",
        "options": [
            "Life-threatening asthma",
            "Moderate asthma exacerbation",
            "Acute severe asthma",
            "Brittle asthma",
            "Near-fatal asthma requiring immediate intubation"
        ],
        "correct_answer": "Life-threatening asthma",
        "explanation": "At first glance, her PEF (33–50%), RR (>=25/min), and HR (>=110 bpm) fit 'acute severe asthma'. However, look closely at the arterial blood gas: her PaCO2 is 5.3 kPa (within the normal range of 4.7–6.0 kPa). During an acute asthma attack, tachypnoea should blow off carbon dioxide, producing a respiratory alkalosis with a LOW PaCO2 (<4.6 kPa). A 'normal' PaCO2 (4.6–6.0 kPa) in a breathless asthmatic indicates respiratory muscle fatigue and failing ventilation—making it a defining feature of life-threatening asthma (whereas raised PaCO2 >6.0 kPa defines near-fatal asthma)."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 68-year-old man with a history of both mild heart failure and a 45-pack-year smoking history presents with a moderate right-sided pleural effusion. Diagnostic pleural aspiration yields straw-coloured fluid. Laboratory results show: Serum total protein 66 g/L, Serum LDH 200 U/L (laboratory upper limit of normal for serum LDH is 210 U/L); Pleural fluid protein 28 g/L, Pleural fluid LDH 150 U/L. Applying Light's criteria, how is this pleural effusion classified?",
        "options": [
            "Exudate, because the pleural fluid-to-serum LDH ratio is >0.6 (and pleural LDH is >2/3 of the upper limit of normal serum LDH)",
            "Transudate, because the pleural fluid-to-serum protein ratio is <0.5",
            "Transudate, because pleural fluid protein is <30 g/L",
            "Exudate, only if all three of Light's criteria are simultaneously positive",
            "Chylothorax, because the LDH is elevated relative to protein"
        ],
        "correct_answer": "Exudate, because the pleural fluid-to-serum LDH ratio is >0.6 (and pleural LDH is >2/3 of the upper limit of normal serum LDH)",
        "explanation": "When total serum protein is normal, pleural fluid protein <30 g/L usually suggests a transudate, and >30 g/L an exudate. However, when protein is borderline (25–35 g/L)—as here (28 g/L)—Light's criteria must be applied. Under Light's criteria, an effusion is an EXUDATE if it meets AT LEAST ONE of: (1) pleural-to-serum protein ratio >0.5 (here 28/66 = 0.42), (2) pleural-to-serum LDH ratio >0.6 (here 150/200 = 0.75—POSITIVE!), or (3) pleural LDH >2/3 the upper limit of normal serum LDH (here 150 > 140 U/L—POSITIVE!). Because criteria 2 and 3 are met, this is an exudative effusion requiring investigation for malignancy or infection."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 67-year-old ex-smoker with severe COPD attends the respiratory outpatient clinic when clinically stable on optimal inhaled triple therapy. Two arterial blood gases taken 3 weeks apart while breathing room air show: Sample 1: PaO2 7.6 kPa, PaCO2 5.6 kPa; Sample 2: PaO2 7.5 kPa, PaCO2 5.5 kPa. According to NICE guidelines, which additional clinical or laboratory finding would qualify this patient for Long-Term Oxygen Therapy (LTOT)?",
        "options": [
            "Peripheral oedema, pulmonary hypertension, or secondary polycythaemia (haematocrit >55%)",
            "A forced expiratory volume in 1 second (FEV1) <50% of predicted",
            "More than two infective COPD exacerbations requiring oral steroids in the past year",
            "Continued smoking of <5 cigarettes per day with morning headaches",
            "AnMRC dyspnoea scale score of 3"
        ],
        "correct_answer": "Peripheral oedema, pulmonary hypertension, or secondary polycythaemia (haematocrit >55%)",
        "explanation": "Long-Term Oxygen Therapy (LTOT, worn for >=15 hours/day) improves survival in chronic hypoxaemic COPD. NICE NG115 specifies two PaO2 thresholds measured on two occasions at least 3 weeks apart in a stable, non-smoking patient: (1) PaO2 <7.3 kPa is an absolute indication for LTOT regardless of other features; (2) PaO2 between 7.3 and 8.0 kPa is an indication for LTOT IF accompanied by secondary polycythaemia (haematocrit >55%), peripheral oedema, pulmonary hypertension (cor pulmonale), or nocturnal hypoxaemia."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 66-year-old man is assessed in the Emergency Department with a 3-day history of fever, productive cough with rusty sputum, and right-sided pleuritic chest pain. Chest X-ray confirms right lower lobe consolidation. On examination, he is fully alert and orientated (AMTS 10/10), his respiratory rate is 24 breaths/min, blood pressure is 126/78 mmHg, and heart rate is 92 bpm. Venous blood tests show urea 8.4 mmol/L, creatinine 92 umol/L, and CRP 145 mg/L. What is his CURB-65 score and recommended management setting?",
        "options": [
            "CURB-65 score of 2; consider hospital-supervised inpatient treatment for moderate-severity community-acquired pneumonia",
            "CURB-65 score of 1; discharge home with a 5-day course of oral amoxicillin monotherapy",
            "CURB-65 score of 3; admit to the high-dependency unit for intravenous co-amoxiclav and clarithromycin",
            "CURB-65 score of 0; reassure and manage conservatively without antibiotics",
            "CURB-65 score of 4; intubate and transfer to the intensive care unit"
        ],
        "correct_answer": "CURB-65 score of 2; consider hospital-supervised inpatient treatment for moderate-severity community-acquired pneumonia",
        "explanation": "The CURB-65 score assigns 1 point for each of: Confusion (new onset or AMTS <=8) [0], Urea >7 mmol/L [1 point: his is 8.4 mmol/L], Respiratory rate >=30/min [0: his is 24], Blood pressure <90 mmHg systolic or <=60 mmHg diastolic [0: his is 126/78], and Age >=65 years [1 point: he is 66]. This gives a CURB-65 score of 2 (moderate severity, ~9% 30-day mortality), which is the threshold for hospital-supervised treatment (short-stay inpatient admission or hospital-at-home) with dual antibiotic therapy (e.g. amoxicillin plus clarithromycin or doxycycline)."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 22-year-old tall, thin man with no history of lung disease presents to the Emergency Department with mild right-sided pleuritic chest pain that started 3 hours ago while sitting at his desk. On examination, he is comfortable at rest and not breathless when walking across the cubicle. His heart rate is 74 bpm, blood pressure is 122/76 mmHg, respiratory rate is 15/min, and SpO2 is 99% on room air. Chest X-ray reveals a right-sided primary spontaneous pneumothorax measuring 2.4 cm at the level of the hilum. According to current BTS/NICE guidelines, what is the most appropriate management?",
        "options": [
            "Conservative outpatient management with safety-netting advice and clinical review in 2–4 weeks",
            "Immediate insertion of a large-bore (28 Fr) intercostal chest drain in the 5th intercostal space",
            "Emergency needle decompression in the 2nd intercostal space mid-clavicular line",
            "Urgent video-assisted thoracoscopic surgery (VATS) pleurodesis today",
            "Inpatient admission for 100% high-flow reservoir mask oxygen therapy for 5 days"
        ],
        "correct_answer": "Conservative outpatient management with safety-netting advice and clinical review in 2–4 weeks",
        "explanation": "Under the updated 2023 British Thoracic Society (BTS) pleural disease guidelines, management of a primary spontaneous pneumothorax (PSP) is now driven primarily by symptoms (breathlessness) and physiological stability rather than a rigid 2 cm radiographic size cut-off alone. In a physiologically stable patient with a PSP who has minimal or no breathlessness and no high-risk features, conservative management (safe discharge with written safety-netting advice and outpatient review every 2–4 days/weeks until resolution) is recommended as a safe first-line option regardless of pneumothorax size on CXR."
    }
]
