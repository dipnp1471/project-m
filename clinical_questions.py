# -*- coding: utf-8 -*-
"""
High-Yield Clinical Problem Solving Questions (MSRA / UKMLA / AKT Format)
60 concise, high-impact clinical reasoning vignettes designed around NICE CKS, BNF, and UK guidelines.
5 questions for each of the 12 clinical domains.
"""

CLINICAL_QUESTIONS = [
    # =========================================================================
    # 1. CARDIOVASCULAR
    # =========================================================================
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 58-year-old man with diet-controlled type 2 diabetes has stage 1 hypertension (ABPM daytime average 146/92 mmHg) and a QRISK3 score of 14%. Renal function and electrolytes are normal. What is the first-line antihypertensive?",
        "options": [
            "Ramipril",
            "Amlodipine",
            "Indapamide",
            "Bisoprolol",
            "Doxazosin"
        ],
        "correct_answer": "Ramipril",
        "explanation": "Although adults aged >=55 without diabetes start on a calcium channel blocker (amlodipine), NICE NG136 specifies that adults of any age with type 2 diabetes should be offered an ACE inhibitor (ramipril) or ARB first-line for its renoprotective effect on glomerular efferent arteriolar pressure."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 64-year-old man with central crushing chest pain has 3 mm ST-segment elevation in leads II, III, and aVF. His BP is 84/52 mmHg, HR is 56 bpm, JVP is raised at 6 cm, and both lung fields are clear. While awaiting primary PCI, what is the immediate management for his hypotension?",
        "options": [
            "Intravenous 0.9% sodium chloride bolus",
            "Sublingual glyceryl trinitrate (GTN)",
            "Intravenous furosemide 40 mg",
            "Oral bisoprolol 2.5 mg",
            "Intravenous dobutamine infusion"
        ],
        "correct_answer": "Intravenous 0.9% sodium chloride bolus",
        "explanation": "Inferior STEMI (leads II, III, aVF) with the triad of hypotension, raised JVP, and clear lungs indicates acute right ventricular infarction. The ischaemic right ventricle is preload-dependent: nitrates or diuretics cause catastrophic cardiovascular collapse, whereas cautious IV 0.9% sodium chloride boluses maintain right ventricular filling."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 54-year-old car driver (Group 1 licence) is ready for discharge after an NSTEMI treated with successful PCI and stenting to the LAD. Echocardiography shows an LVEF of 52%, and no further revascularisation is planned. What driving advice applies?",
        "options": [
            "Stop driving for 1 week; no need to notify the DVLA",
            "Stop driving for 4 weeks; no need to notify the DVLA",
            "Stop driving for 4 weeks and notify the DVLA immediately",
            "Stop driving for 6 weeks until cardiology clinic review",
            "Resume driving immediately upon hospital discharge"
        ],
        "correct_answer": "Stop driving for 1 week; no need to notify the DVLA",
        "explanation": "Under DVLA rules for Group 1 drivers after ACS, if PCI is successful, no further urgent revascularisation is planned, and LVEF is at least 40%, driving may resume after 1 week without notifying the DVLA. Medically managed ACS without successful PCI requires 4 weeks off driving."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 38-year-old woman has persistent hypertension (168/104 mmHg) despite adherence to amlodipine, indapamide, and doxazosin. She does not eat liquorice. Bloods show: Na+ 145 mmol/L, K+ 2.9 mmol/L, bicarbonate 31 mmol/L, and creatinine 68 umol/L. What is the initial diagnostic test?",
        "options": [
            "Plasma aldosterone-to-renin ratio",
            "24-hour urinary free cortisol",
            "CT scan of the adrenal glands",
            "Renal artery Doppler ultrasound",
            "24-hour urinary metanephrines"
        ],
        "correct_answer": "Plasma aldosterone-to-renin ratio",
        "explanation": "Resistant hypertension in a young patient with hypokalaemia and metabolic alkalosis points to primary hyperaldosteronism (Conn's syndrome). Autonomous aldosterone secretion retains sodium and excretes potassium/H+ while suppressing renin. A plasma aldosterone-to-renin ratio (high aldosterone, suppressed renin) is the first-line screening test before adrenal imaging."
    },
    {
        "type": "sba",
        "category": "Cardiovascular",
        "scenario": "A 71-year-old man with a bioprosthetic aortic valve presents with 3 weeks of fevers, night sweats, splinter haemorrhages, and a new regurgitant murmur. Three blood culture sets grow Streptococcus gallolyticus (S. bovis). Alongside IV antibiotics and echocardiography, which investigation is mandatory?",
        "options": [
            "Colonoscopy",
            "High-resolution CT chest",
            "Dental orthopantomogram",
            "Flexible cystoscopy",
            "MR cholangiopancreatography (MRCP)"
        ],
        "correct_answer": "Colonoscopy",
        "explanation": "Streptococcus gallolyticus (formerly S. bovis biotype I) endocarditis or bacteraemia is strongly associated with occult colonic neoplasia (adenomatous polyps or colorectal carcinoma in >50% of cases), as the organism translocates across disrupted bowel mucosa. Full colonoscopy is mandatory even without gastrointestinal symptoms."
    },

    # =========================================================================
    # 2. DERMATOLOGY / OPHTHALMOLOGY / ENT
    # =========================================================================
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 46-year-old woman wakes with sudden hearing loss and tinnitus in her left ear, without pain or discharge. Otoscopy is normal bilaterally. Rinne's test is positive (AC > BC) bilaterally, and Weber's test lateralises to the right ear. What is the most appropriate management?",
        "options": [
            "Same-day ENT referral and high-dose oral prednisolone",
            "Reassurance and olive oil ear drops for 2 weeks",
            "Fluticasone nasal spray and Valsalva manoeuvres for 6 weeks",
            "Oral amoxicillin for 5 days for acute otitis media",
            "Routine outpatient audiology referral within 6 weeks"
        ],
        "correct_answer": "Same-day ENT referral and high-dose oral prednisolone",
        "explanation": "Weber's test lateralising to the unaffected (right) ear with bilateral positive Rinne's tests confirms acute left sensorineural hearing loss. Idiopathic sudden sensorineural hearing loss (<72 hours) is an otological emergency requiring same-day ENT assessment, pure-tone audiometry, and urgent oral or intratympanic corticosteroids."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 22-year-old soft contact lens wearer presents with 24 hours of severe right eye pain, photophobia, and blurred vision (acuity 6/18). Examination shows circumcorneal redness and a 2 mm white corneal opacity that stains with fluorescein. What is the immediate action?",
        "options": [
            "Same-day emergency ophthalmology referral",
            "Topical chloramphenicol drops and review in 48 hours",
            "Topical fusidic acid gel and discard contact lenses",
            "Eye pad with topical cyclopentolate and review tomorrow",
            "Oral aciclovir 800 mg five times daily"
        ],
        "correct_answer": "Same-day emergency ophthalmology referral",
        "explanation": "A painful red eye, reduced visual acuity, photophobia, and a fluorescein-staining corneal opacity in a contact lens wearer indicates bacterial keratitis (typically Pseudomonas aeruginosa) until proven otherwise. Pseudomonas can cause corneal perforation within 24–48 hours; same-day slit-lamp scraping and intensive topical fluoroquinolones are mandatory (chloramphenicol does not cover Pseudomonas)."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 26-year-old man develops a symmetrical rash over his hands, palms, and forearms over 48 hours. Each 1 cm lesion has a dusky blistered centre, a pale oedematous middle ring, and an outer erythematous halo. Mucosae are spared. He had a cold sore 10 days ago. What is the commonest trigger?",
        "options": [
            "Herpes simplex virus (HSV)",
            "Epstein-Barr virus (EBV)",
            "Streptococcus pyogenes",
            "Varicella-zoster virus (VZV)",
            "Staphylococcus aureus"
        ],
        "correct_answer": "Herpes simplex virus (HSV)",
        "explanation": "Acral lesions with three concentric zones (central dusky/blistered zone, pale oedematous ring, and outer erythematous halo) are classic target lesions of erythema multiforme. When mucosae are spared (erythema multiforme minor), it is triggered in 70–80% of cases by preceding Herpes simplex virus infection (with Mycoplasma pneumoniae second)."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 74-year-old woman has an asymptomatic, slowly enlarging red patch on her right shin for 9 months that failed to clear with hydrocortisone cream. Examination shows a solitary, sharply demarcated 1.8 cm erythematous scaly plaque without ulceration. Dermoscopy shows clustered glomerular vessels. What is the likely diagnosis?",
        "options": [
            "Bowen's disease (squamous cell carcinoma in situ)",
            "Nodular basal cell carcinoma",
            "Discoid eczema",
            "Amelanotic malignant melanoma",
            "Pyoderma gangrenosum"
        ],
        "correct_answer": "Bowen's disease (squamous cell carcinoma in situ)",
        "explanation": "A solitary, well-demarcated erythematous scaly plaque on the sun-exposed lower leg of an older woman that fails to respond to topical steroids is typical of Bowen's disease (SCC in situ). Untreated, 3–5% progress to invasive SCC; treatments include topical 5-fluorouracil, cryotherapy, curettage, or excision."
    },
    {
        "type": "sba",
        "category": "Dermatology / Ophthalmology / ENT",
        "scenario": "A 68-year-old long-sighted woman presents at 10 pm with severe right frontal headache, vomiting, and halos around lights, 10 days after starting amitriptyline for sciatica. The right eye is red with a hazy cornea, a fixed mid-dilated pupil, and a hard globe. How did amitriptyline trigger this?",
        "options": [
            "Antimuscarinic mydriasis crowding the iridocorneal angle",
            "Alpha-1 stimulation increasing ciliary aqueous secretion",
            "Serotonergic vasoconstriction of the central retinal artery",
            "Direct thrombosis of the central retinal vein",
            "Histamine H1 blockade causing corneal endothelial oedema"
        ],
        "correct_answer": "Antimuscarinic mydriasis crowding the iridocorneal angle",
        "explanation": "Tricyclic antidepressants like amitriptyline have potent antimuscarinic properties that dilate the pupil (mydriasis). In a hypermetropic (long-sighted) eye with a shallow anterior chamber, the dilated iris bunches up peripherally and obstructs trabecular meshwork outflow at the iridocorneal angle, precipitating acute angle-closure glaucoma."
    },

    # =========================================================================
    # 3. ENDOCRINOLOGY / METABOLIC
    # =========================================================================
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 42-year-old woman has 5 months of fatigue, cold intolerance, constipation, and weight gain. Initial bloods show TSH 7.8 mU/L (0.4–4.5) and normal free T4 (13.2 pmol/L). Repeat tests 3 months later show TSH 8.4 mU/L, free T4 12.8 pmol/L, and positive anti-TPO antibodies. What does NICE recommend?",
        "options": [
            "Offer a 6-month trial of oral levothyroxine",
            "Reassure and repeat TFTs in 12 months without treatment",
            "Refer to endocrinology for radioactive iodine therapy",
            "Start oral liothyronine (T3) monotherapy",
            "Arrange thyroid ultrasound and fine-needle aspiration"
        ],
        "correct_answer": "Offer a 6-month trial of oral levothyroxine",
        "explanation": "This is persistent subclinical hypothyroidism (TSH 4.5–10 mU/L with normal free T4 on two occasions 3 months apart). Under NICE NG145, while levothyroxine is routine for TSH >=10 mU/L, adults aged <65 with TSH <10 mU/L and hypothyroid symptoms should be offered a 6-month trial of levothyroxine."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 34-year-old woman with vitiligo presents with fatigue, postural dizziness, weight loss, and pigmented palmar creases. Bloods show: Na+ 127 mmol/L, K+ 5.8 mmol/L, glucose 3.2 mmol/L, TSH 14.5 mU/L, free T4 7.8 pmol/L, and 9 am cortisol 62 nmol/L. Why must hydrocortisone be started before levothyroxine?",
        "options": [
            "Levothyroxine accelerates hepatic cortisol clearance, precipitating adrenal crisis",
            "Hydrocortisone inhibits peripheral T4-to-rT3 conversion, preventing thyroid storm",
            "Levothyroxine blocks distal renal mineralocorticoid receptors, worsening hyperkalaemia",
            "Starting levothyroxine first causes pituitary apoplexy via TSH suppression",
            "Levothyroxine chelates oral hydrocortisone in the gut lumen"
        ],
        "correct_answer": "Levothyroxine accelerates hepatic cortisol clearance, precipitating adrenal crisis",
        "explanation": "This patient has autoimmune polyendocrine syndrome type 2 (Addison's disease plus autoimmune hypothyroidism). When adrenal insufficiency and hypothyroidism coexist, glucocorticoid replacement (hydrocortisone) must always precede levothyroxine, because thyroid hormone increases basal metabolic rate and hepatic cortisol clearance, exhausting residual cortisol and triggering an Addisonian crisis."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 76-year-old woman develops mild confusion 2 weeks after starting citalopram. She is clinically euvolaemic (BP 128/76 mmHg, moist mucosae, no oedema). Bloods and urine show: serum Na+ 122 mmol/L, serum osmolality 252 mOsm/kg, urine osmolality 490 mOsm/kg, and urine Na+ 48 mmol/L. TFTs and cortisol are normal. What is the diagnosis?",
        "options": [
            "Syndrome of inappropriate ADH secretion (SIADH)",
            "Cranial diabetes insipidus",
            "Primary polydipsia",
            "Cerebral salt wasting syndrome",
            "Addison's disease"
        ],
        "correct_answer": "Syndrome of inappropriate ADH secretion (SIADH)",
        "explanation": "SSRIs like citalopram commonly trigger SIADH in older adults. All diagnostic criteria are met: clinical euvolaemia, hypotonic hyponatraemia (Na+ <135 mmol/L, osmolality <275 mOsm/kg), inappropriately concentrated urine (>100 mOsm/kg), raised urinary sodium (>20–30 mmol/L), and normal renal, adrenal, and thyroid function."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 29-year-old woman started on carbimazole 40 mg daily 4 weeks ago for Graves' disease phones the GP surgery with a severe sore throat, painful mouth ulcers, and a fever of 38.7°C. What is the single most important immediate instruction?",
        "options": [
            "Stop carbimazole immediately and attend today for an urgent full blood count",
            "Continue carbimazole, take paracetamol, and book a throat swab in 48 hours",
            "Halve carbimazole to 20 mg daily and start phenoxymethylpenicillin",
            "Switch carbimazole to propylthiouracil immediately without blood tests",
            "Continue carbimazole and attend for urgent thyroid function tests"
        ],
        "correct_answer": "Stop carbimazole immediately and attend today for an urgent full blood count",
        "explanation": "Carbimazole and propylthiouracil carry a ~0.1–0.5% risk of idiosyncratic agranulocytosis, especially in the first 3 months. Any patient developing a sore throat, mouth ulcers, bruising, or fever must withhold the drug immediately and have a same-day full blood count to check the neutrophil count."
    },
    {
        "type": "sba",
        "category": "Endocrinology / Metabolic",
        "scenario": "A 19-year-old man with type 1 diabetes is admitted in DKA (pH 7.14, ketones 5.6 mmol/L, glucose 26.4 mmol/L). He starts a fixed-rate IV insulin infusion alongside his first litre of 0.9% sodium chloride. His initial serum potassium is 5.8 mmol/L. How should IV potassium be managed right now?",
        "options": [
            "Give 0.9% sodium chloride with no added potassium until K+ falls below 5.5 mmol/L",
            "Add 40 mmol/L potassium chloride immediately as insulin shifts K+ into cells",
            "Add 20 mmol/L potassium chloride and give IV calcium gluconate",
            "Pause the insulin infusion until serum K+ falls below 5.0 mmol/L",
            "Give nebulised salbutamol before continuing fluid resuscitation"
        ],
        "correct_answer": "Give 0.9% sodium chloride with no added potassium until K+ falls below 5.5 mmol/L",
        "explanation": "Despite total-body potassium depletion in DKA, adding potassium when serum K+ is >5.5 mmol/L risks fatal hyperkalaemic arrhythmias. JBDS guidelines specify: no potassium in the first bag or while K+ >5.5 mmol/L; add 40 mmol/L KCl once K+ is 3.5–5.5 mmol/L and passing urine; pause insulin if K+ <3.5 mmol/L."
    },

    # =========================================================================
    # 4. GASTROENTEROLOGY / CLINICAL NUTRITION
    # =========================================================================
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 27-year-old woman presents with 6 months of bloating, loose stools, and iron-deficiency anaemia (Hb 103 g/L, MCV 72 fL). You suspect coeliac disease. According to NICE, which first-line serology and dietary advice should you give?",
        "options": [
            "Total IgA and IgA-tTG, while eating gluten in >1 meal daily for >=6 weeks",
            "IgG deamidated gliadin peptide (DGP) after excluding gluten for 2 weeks",
            "HLA-DQ2 and HLA-DQ8 genetic typing as the initial screen",
            "IgA endomysial antibodies (EMA) alone on a gluten-free diet",
            "Faecal calprotectin and anti-Saccharomyces cerevisiae antibodies"
        ],
        "correct_answer": "Total IgA and IgA-tTG, while eating gluten in >1 meal daily for >=6 weeks",
        "explanation": "NICE NG20 recommends checking total serum IgA alongside IgA tissue transglutaminase (tTG) first-line, because 2–3% of coeliac patients have selective IgA deficiency (causing a false-negative IgA-tTG). Patients must eat gluten in more than one meal daily for at least 6 weeks before testing."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 31-year-old man with ulcerative colitis passes 8 bloody stools/day for 4 days. He has T 38.2°C, HR 98 bpm, Hb 96 g/L, and ESR 44 mm/hr. His abdomen is soft with a transverse colon diameter of 4.2 cm on X-ray. How is this classified and treated?",
        "options": [
            "Acute severe ulcerative colitis; admit for IV hydrocortisone",
            "Moderately active flare; discharge on oral and rectal mesalazine",
            "Toxic megacolon; proceed to emergency subtotal colectomy",
            "Acute severe ulcerative colitis; start IV infliximab first-line",
            "Mild flare; start a tapering course of oral budesonide"
        ],
        "correct_answer": "Acute severe ulcerative colitis; admit for IV hydrocortisone",
        "explanation": "By Truelove and Witts' criteria, >=6 bloody stools/day plus any systemic toxicity feature (T >37.8°C, HR >90 bpm, Hb <105 g/L, or ESR >30 mm/hr) defines acute severe ulcerative colitis (toxic megacolon requires colonic dilatation >6 cm). First-line treatment is inpatient IV hydrocortisone and VTE prophylaxis."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 44-year-old man with alcohol dependence (BMI 15.6 kg/m²) who has not eaten for 8 days is given IV Pabrinex and started on nasogastric feeding. Forty-eight hours later, he develops muscle weakness, paraesthesia, diplopia, and ventricular ectopics. Which electrolyte abnormality is the hallmark of this complication?",
        "options": [
            "Severe hypophosphataemia",
            "Hypercalcaemia",
            "Hyperkalaemia",
            "Hypermagnesaemia",
            "High-anion-gap metabolic acidosis"
        ],
        "correct_answer": "Severe hypophosphataemia",
        "explanation": "Reintroducing carbohydrates after prolonged starvation (>5 days) triggers an insulin surge that drives phosphate, potassium, and magnesium into cells while consuming phosphate for ATP synthesis (refeeding syndrome). Severe hypophosphataemia is the hallmark feature, causing weakness, rhabdomyolysis, seizures, and arrhythmias."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 58-year-old man with alcohol-related cirrhosis and tense ascites is admitted with mild abdominal discomfort and grade 2 hepatic encephalopathy. He is afebrile. A diagnostic ascitic tap is performed. Which fluid threshold mandates empirical IV antibiotics for spontaneous bacterial peritonitis (SBP)?",
        "options": [
            "Ascitic fluid neutrophil count >=250 cells/mm³",
            "Ascitic fluid total white cell count >=1,000 cells/mm³",
            "Serum-ascites albumin gradient (SAAG) <11 g/L",
            "Positive Gram stain on microscopy only",
            "Ascitic fluid pH <7.30 with raised amylase"
        ],
        "correct_answer": "Ascitic fluid neutrophil count >=250 cells/mm³",
        "explanation": "SBP often presents subtly with encephalopathy or renal deterioration without fever. Because ascitic cultures take 48 hours and can be negative, an ascitic fluid polymorphonuclear (neutrophil) count >=250 cells/mm³ (0.25 x 10⁹/L) is the diagnostic threshold to start immediate empirical IV antibiotics (e.g. cefotaxime) and IV albumin."
    },
    {
        "type": "sba",
        "category": "Gastroenterology / Clinical Nutrition",
        "scenario": "A 41-year-old smoker presents with a 3-week history of solid food sticking briefly behind his sternum after swallowing. His weight is stable, he has no odynophagia, and his Hb is 148 g/L. Under NICE NG12 guidelines, what is the next step?",
        "options": [
            "Urgent 2-week wait referral for upper GI endoscopy",
            "4-week trial of oral omeprazole 20 mg daily",
            "Carbon-13 urea breath test for H. pylori",
            "Routine outpatient barium swallow",
            "Reassurance and advice on chewing thoroughly"
        ],
        "correct_answer": "Urgent 2-week wait referral for upper GI endoscopy",
        "explanation": "Under NICE NG12, dysphagia at ANY age (or age >=55 with weight loss and upper abdominal pain, reflux, or dyspepsia) requires an urgent 2-week wait upper GI endoscopy (OGD). True dysphagia must never be masked with an empirical PPI trial before excluding oesophageal malignancy."
    },

    # =========================================================================
    # 5. INFECTIOUS DISEASES / HAEMATOLOGY / IMMUNOLOGY / ALLERGIES / GENETICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "An 18-year-old student with fever, exudative tonsillitis, and posterior cervical lymphadenopathy was prescribed amoxicillin 4 days ago. She now has a widespread symmetrical maculopapular rash and mild splenomegaly, with no airway swelling or wheeze. What explains this rash?",
        "options": [
            "Amoxicillin-EBV interaction; not a true penicillin allergy",
            "IgE-mediated type I allergy requiring lifelong penicillin avoidance",
            "Scarlet fever caused by group A Streptococcus",
            "Stevens-Johnson syndrome from beta-lactam exposure",
            "Secondary syphilis rash"
        ],
        "correct_answer": "Amoxicillin-EBV interaction; not a true penicillin allergy",
        "explanation": "Pharyngitis, posterior cervical lymphadenopathy, and splenomegaly in a young adult indicate infectious mononucleosis (EBV). Giving amoxicillin or ampicillin during acute EBV triggers a florid maculopapular rash in 80–90% of patients via transient immune complexes—it is not a true IgE penicillin allergy."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 79-year-old man on warfarin for a mechanical mitral valve presents with major haematemesis and melaena. His BP is 86/52 mmHg, HR is 118 bpm, Hb is 74 g/L, and INR is 6.8. Alongside resuscitation, what is the immediate reversal regimen?",
        "options": [
            "IV 4-factor prothrombin complex concentrate (PCC) plus IV phytomenadione (vitamin K1) 5 mg",
            "IV phytomenadione (vitamin K1) 10 mg alone and recheck INR in 6 hours",
            "Four units of ABO-matched fresh frozen plasma (FFP) first-line",
            "Oral phytomenadione 5 mg plus IV tranexamic acid only",
            "IV idarucizumab plus platelet transfusion"
        ],
        "correct_answer": "IV 4-factor prothrombin complex concentrate (PCC) plus IV phytomenadione (vitamin K1) 5 mg",
        "explanation": "Life-threatening warfarin bleeding requires immediate reversal with BOTH IV 4-factor PCC (normalises INR within 10–15 minutes by replacing factors II, VII, IX, and X) and IV vitamin K1 5 mg (sustains endogenous clotting factor synthesis once short-acting factor VII in PCC wears off)."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 56-year-old woman 10 days post-FEC-T chemotherapy for breast cancer presents feeling shivery with a temperature of 38.4°C, HR 98 bpm, and BP 116/72 mmHg. She has no localising signs. Blood cultures and FBC are sent. What is the immediate next step?",
        "options": [
            "Give empirical IV piperacillin-tazobactam immediately without waiting for the FBC",
            "Wait 45 minutes for the neutrophil count (<0.5 x 10⁹/L) before giving antibiotics",
            "Give subcutaneous G-CSF and observe for 4 hours",
            "Perform a chest X-ray and lumbar puncture before giving antibiotics",
            "Discharge on oral co-amoxiclav and ciprofloxacin with clinic review tomorrow"
        ],
        "correct_answer": "Give empirical IV piperacillin-tazobactam immediately without waiting for the FBC",
        "explanation": "Fever (>38.0°C) or sepsis signs within 6 weeks of systemic chemotherapy is neutropenic sepsis until proven otherwise. NICE CG151 mandates empirical IV piperacillin-tazobactam (Tazocin) within 1 hour of arrival—never delay antibiotics while awaiting laboratory confirmation of neutropenia."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 62-year-old man with bulky Burkitt lymphoma starts R-CHOP chemotherapy. Thirty-six hours later, he develops nausea, muscle spasms, oliguria, and tall tented T waves on ECG. Which electrolyte tetrad defines this emergency?",
        "options": [
            "Hyperkalaemia, hyperphosphataemia, hyperuricaemia, and hypocalcaemia",
            "Hyperkalaemia, hyperphosphataemia, hyperuricaemia, and hypercalcaemia",
            "Hypokalaemia, hypophosphataemia, hyperuricaemia, and hypercalcaemia",
            "Hyponatraemia, hypokalaemia, hypocalcaemia, and metabolic alkalosis",
            "Hypernatraemia, hypercalcaemia, hypophosphataemia, and hypoglycaemia"
        ],
        "correct_answer": "Hyperkalaemia, hyperphosphataemia, hyperuricaemia, and hypocalcaemia",
        "explanation": "Tumour lysis syndrome (TLS) follows rapid breakdown of malignant cells, releasing intracellular potassium, phosphate, and nucleic acids (metabolised to uric acid). This produces 'three ups and one down': hyperkalaemia, hyperphosphataemia, and hyperuricaemia, with secondary hypocalcaemia as calcium precipitates with excess phosphate."
    },
    {
        "type": "sba",
        "category": "Infectious Diseases / Haematology / Immunology / Allergies / Genetics",
        "scenario": "A 29-year-old woman at 16 weeks gestation spent 3 hours indoors yesterday with her nephew, who developed a chickenpox rash this morning. She is asymptomatic, recalls no past history of chickenpox, and is unvaccinated. What is the first step?",
        "options": [
            "Check maternal serum for VZV IgG antibodies urgently",
            "Start oral aciclovir 800 mg five times daily immediately",
            "Give intramuscular VZIG today without blood testing",
            "Reassure her that chickenpox poses no risk at 16 weeks",
            "Admit immediately for intravenous aciclovir"
        ],
        "correct_answer": "Check maternal serum for VZV IgG antibodies urgently",
        "explanation": "Over 80% of UK adults with no recalled history of chickenpox are actually immune on serology. After significant exposure (>15 minutes in the same room or face-to-face contact), RCOG guidelines state the first step is urgent maternal VZV IgG testing; if seronegative, oral aciclovir (days 7–14 post-exposure) or VZIG is given."
    },

    # =========================================================================
    # 6. MUSCULOSKELETAL
    # =========================================================================
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 43-year-old man with lower back pain develops 24 hours of severe pain radiating down both legs, numbness when wiping his perineum, and difficulty initiating micturition. What is the immediate action?",
        "options": [
            "Same-day emergency hospital transfer for urgent lumbosacral MRI",
            "Urgent 2-week wait outpatient lumbar spine MRI",
            "Oral naproxen and amitriptyline with review in 48 hours",
            "Urgent plain radiographs of the lumbar spine today",
            "Community musculoskeletal physiotherapy triage referral"
        ],
        "correct_answer": "Same-day emergency hospital transfer for urgent lumbosacral MRI",
        "explanation": "Bilateral sciatica with saddle/perineal sensory loss or bladder/bowel dysfunction indicates suspected cauda equina syndrome. This neurosurgical emergency requires immediate same-day hospital transfer for emergency MRI and surgical decompression to prevent permanent paraplegia and incontinence."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 72-year-old woman has 6 weeks of bilateral shoulder and hip aching with 2 hours of morning stiffness. She has no headache, visual symptoms, or jaw claudication. Supported muscle power is 5/5. Bloods show ESR 68 mm/hr, CRP 52 mg/L, and normal CK (78 U/L). What is the initial treatment?",
        "options": [
            "Oral prednisolone 15 mg once daily",
            "Oral prednisolone 60 mg once daily",
            "Oral methotrexate 15 mg once weekly",
            "Oral ibuprofen 400 mg three times daily",
            "Single intramuscular methylprednisolone 120 mg injection"
        ],
        "correct_answer": "Oral prednisolone 15 mg once daily",
        "explanation": "Bilateral shoulder and pelvic girdle pain with morning stiffness >45 minutes in a patient >50 years, raised ESR/CRP, and normal CK (excluding polymyositis) is classic for polymyalgia rheumatica (PMR). Without giant cell arteritis symptoms (which need 40–60 mg), NICE recommends prednisolone 15 mg daily."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 69-year-old man wakes with an acutely painful, red, swollen right first MTP joint. He is afebrile. He has stage 4 CKD (eGFR 21 mL/min/1.73m²), hypertension, and a past peptic ulcer, and takes no urate-lowering therapy. What is the safest treatment for this acute flare?",
        "options": [
            "Oral prednisolone 30–35 mg once daily for 5 days",
            "Oral naproxen 500 mg twice daily with omeprazole",
            "Oral allopurinol 100 mg once daily started today",
            "High-dose oral colchicine 500 mcg every 2 hours",
            "Oral febuxostat 80 mg once daily"
        ],
        "correct_answer": "Oral prednisolone 30–35 mg once daily for 5 days",
        "explanation": "In acute gout (podagra), NSAIDs are contraindicated by stage 4 CKD and peptic ulcer history, while colchicine carries severe toxicity risks in advanced renal impairment. A short course of oral prednisolone (30–35 mg daily for 5 days) is safest; allopurinol must never be started during an acute flare."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 76-year-old woman has a femoral neck T-score of -2.9 on DEXA after a wrist fracture. She has achalasia with delayed oesophageal emptying, normal calcium/vitamin D, and eGFR 66 mL/min/1.73m². Why is oral alendronic acid contraindicated?",
        "options": [
            "Delayed oesophageal emptying predisposes to severe chemical oesophagitis and ulceration",
            "Bisphosphonates relax the lower oesophageal sphincter via calcium blockade",
            "Achalasia prevents gastric acid conversion of alendronate to its active form",
            "Alendronate causes cervical vertebral osteonecrosis in patients with dysphagia",
            "Bisphosphonates destroy myenteric plexus ganglion cells"
        ],
        "correct_answer": "Delayed oesophageal emptying predisposes to severe chemical oesophagitis and ulceration",
        "explanation": "Oral bisphosphonates are direct mucosal irritants. They are strictly contraindicated in oesophageal abnormalities that delay emptying (achalasia, stricture) or when a patient cannot sit upright for 30 minutes; parenteral zoledronic acid or denosumab should be used instead."
    },
    {
        "type": "sba",
        "category": "Musculoskeletal",
        "scenario": "A 32-year-old mother 3 months postpartum has 4 weeks of radial right wrist pain when lifting her baby. She has tenderness over the radial styloid, and ulnar deviation of the wrist with the thumb tucked in the fist (Finkelstein's test) reproduces sharp pain. Which tendons are affected?",
        "options": [
            "Abductor pollicis longus and extensor pollicis brevis",
            "Flexor pollicis longus and flexor carpi radialis",
            "Extensor pollicis longus and extensor carpi radialis brevis",
            "Abductor pollicis brevis and opponens pollicis",
            "Extensor digitorum and extensor indicis"
        ],
        "correct_answer": "Abductor pollicis longus and extensor pollicis brevis",
        "explanation": "Radial wrist pain in a new mother with radial styloid tenderness and a positive Finkelstein's test indicates De Quervain's tenosynovitis, caused by stenosing tenosynovitis of the first dorsal extensor compartment tendons: abductor pollicis longus (APL) and extensor pollicis brevis (EPB)."
    },

    # =========================================================================
    # 7. PAEDIATRICS
    # =========================================================================
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 6-year-old boy has 2 days of fever (38.9°C), exudative tonsillitis, a 'strawberry tongue', and a diffuse blanching 'sandpaper' rash over his trunk and axillae. He has no drug allergies. What is the correct antibiotic regimen and school exclusion advice?",
        "options": [
            "Oral phenoxymethylpenicillin for 10 days; return to school 24 hours after starting antibiotics",
            "Oral amoxicillin for 5 days; stay off school until the rash desquamates",
            "Supportive care only; no school exclusion required",
            "Oral clarithromycin for 7 days; stay off school for 5 days",
            "Hospital admission for IV immunoglobulin and high-dose aspirin"
        ],
        "correct_answer": "Oral phenoxymethylpenicillin for 10 days; return to school 24 hours after starting antibiotics",
        "explanation": "Exudative tonsillitis, 'strawberry tongue', and a coarse 'sandpaper' rash indicate scarlet fever (Group A Streptococcus). NICE and UKHSA recommend 10 days of oral phenoxymethylpenicillin (Penicillin V), notification to public health, and school exclusion until 24 hours after starting antibiotics."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 10-week-old formula-fed infant presents with frequent posseting, loose mucous stools, and facial/trunk eczema. He is thriving along the 50th centile. You suspect mild-to-moderate non-IgE cow's milk protein allergy (CMPA). What is the first-line formula in primary care?",
        "options": [
            "Extensively hydrolysed formula (eHF)",
            "Amino acid-based formula (AAF)",
            "Soya-based infant formula",
            "Lactose-free cow's milk formula",
            "Goat's milk infant formula"
        ],
        "correct_answer": "Extensively hydrolysed formula (eHF)",
        "explanation": "In formula-fed infants with mild-to-moderate CMPA, an extensively hydrolysed formula (eHF) is first-line in primary care. Amino acid formulas (AAF) are reserved for severe CMPA (anaphylaxis, faltering growth, or eHF failure). Soya is avoided under 6 months, and goat/lactose-free formulas still trigger CMPA."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 4-year-old boy wakes with a right-sided limp 1 week after a viral cold. He is afebrile (36.6°C), looks well, and weight-bears with a mild limp and slight discomfort at extreme hip internal rotation. WCC is 7.6 x 10⁹/L, CRP 3 mg/L, and ESR 10 mm/hr. What is the diagnosis and management?",
        "options": [
            "Transient synovitis; rest, ibuprofen, and safety-netting for fever or inability to weight-bear",
            "Septic arthritis; immediate hip arthrotomy and IV ceftriaxone",
            "Slipped capital femoral epiphysis; nil by mouth for urgent pinning",
            "Developmental dysplasia of the hip; apply a Pavlik harness",
            "Juvenile idiopathic arthritis; start oral methotrexate"
        ],
        "correct_answer": "Transient synovitis; rest, ibuprofen, and safety-netting for fever or inability to weight-bear",
        "explanation": "Transient synovitis (irritable hip) is the commonest cause of hip pain in children aged 3–8 years after a viral URTI. With 0/4 Kocher criteria (weight-bearing, afebrile, normal WCC and ESR/CRP), septic arthritis is <0.2% likely; management is rest, ibuprofen, and red-flag safety-netting."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 20-month-old girl presents with coryza, a hoarse voice, and a 'seal-like' barking cough. Sitting calmly, she has no stridor at rest, no chest wall recession, and SpO2 99% in air; faint stridor appears only when she cries. What is the appropriate treatment?",
        "options": [
            "Single dose of oral dexamethasone (0.15 mg/kg)",
            "Steam inhalation only, as steroids are reserved for stridor at rest",
            "Nebulised adrenaline 1:1000 and emergency ambulance transfer",
            "Oral amoxicillin for 5 days",
            "Inhaled salbutamol via spacer"
        ],
        "correct_answer": "Single dose of oral dexamethasone (0.15 mg/kg)",
        "explanation": "Barking cough with stridor only on agitation and no recession indicates mild croup. Crucially, NICE recommends that ALL children with croup—including mild cases managed at home—receive a single dose of oral dexamethasone (0.15 mg/kg) to reduce symptom duration and progression."
    },
    {
        "type": "sba",
        "category": "Paediatrics",
        "scenario": "A 5-day-old term neonate presents with two episodes of dark green (bilious) vomiting over 3 hours. The abdomen is currently soft and non-distended, and observations are stable. Which urgent investigation is required to exclude the most time-critical surgical emergency?",
        "options": [
            "Urgent upper gastrointestinal contrast study",
            "Abdominal ultrasound for a pyloric 'olive' mass",
            "Rectal suction biopsy for ganglion cells",
            "Diagnostic pneumatic air enema",
            "24-hour oesophageal pH monitoring"
        ],
        "correct_answer": "Urgent upper gastrointestinal contrast study",
        "explanation": "Bilious vomiting in a neonate is intestinal malrotation with midgut volvulus until proven otherwise, which can cause total small-bowel necrosis within hours even before abdominal distension develops. An urgent upper GI contrast study is the gold standard to check the duodenojejunal flexure position."
    },

    # =========================================================================
    # 8. PHARMACOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 68-year-old woman taking weekly methotrexate for rheumatoid arthritis presents with an uncomplicated lower UTI (eGFR 68 mL/min/1.73m²). Why is trimethoprim strictly contraindicated?",
        "options": [
            "Additive dihydrofolate reductase inhibition causes life-threatening pancytopenia",
            "Trimethoprim induces CYP3A4, triggering an acute rheumatoid flare",
            "Co-administration causes acute uric acid renal cortical necrosis",
            "Trimethoprim displaces methotrexate from haemoglobin, causing methaemoglobinaemia",
            "Combined therapy causes acute cholestatic liver failure"
        ],
        "correct_answer": "Additive dihydrofolate reductase inhibition causes life-threatening pancytopenia",
        "explanation": "Both methotrexate and trimethoprim (and co-trimoxazole) inhibit dihydrofolate reductase, and trimethoprim also reduces renal tubular methotrexate excretion. Co-prescribing them causes potentially fatal bone marrow suppression (pancytopenia) and severe mucositis; nitrofurantoin is safe here."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 71-year-old man with penicillin anaphylaxis is prescribed clarithromycin for pneumonia. His regular medications are ramipril, amlodipine, and atorvastatin 40 mg nightly. What medication adjustment is required?",
        "options": [
            "Temporarily withhold atorvastatin during the clarithromycin course",
            "Temporarily withhold ramipril to prevent hyperkalaemia",
            "Double atorvastatin to 80 mg nightly due to enzyme induction",
            "Switch amlodipine to verapamil during antibiotic therapy",
            "No adjustment is needed as atorvastatin is renally excreted"
        ],
        "correct_answer": "Temporarily withhold atorvastatin during the clarithromycin course",
        "explanation": "Clarithromycin and erythromycin potently inhibit hepatic CYP3A4, which metabolises atorvastatin and simvastatin. Co-administration markedly raises statin levels, risking severe myopathy and rhabdomyolysis; BNF advises pausing atorvastatin or simvastatin until the macrolide course finishes."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 59-year-old man taking sertraline 100 mg daily is prescribed oral naproxen (with lansoprazole) for an osteoarthritis flare. By what mechanism do SSRIs markedly increase upper GI bleeding risk when combined with NSAIDs?",
        "options": [
            "SSRIs block platelet serotonin uptake, depleting serotonin needed for platelet aggregation",
            "SSRIs directly stimulate parietal cell H+/K+-ATPase acid secretion",
            "SSRIs inhibit gastric cyclooxygenase-1 (COX-1) prostaglandin synthesis",
            "SSRIs displace naproxen from albumin, causing mucosal burns",
            "SSRIs impair hepatic synthesis of vitamin K clotting factors"
        ],
        "correct_answer": "SSRIs block platelet serotonin uptake, depleting serotonin needed for platelet aggregation",
        "explanation": "Platelets cannot synthesise serotonin and rely on the serotonin transporter (SERT) to take it up from plasma to amplify ADP-mediated platelet aggregation during vascular injury. SSRIs block platelet SERT, impairing primary haemostasis and synergistically increasing NSAID GI bleeding risk."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 52-year-old woman stable on lithium carbonate (trough 0.7 mmol/L) starts bendroflumethiazide 2.5 mg daily for hypertension. Two weeks later, she presents with coarse tremor, dysarthria, and ataxia, with a lithium level of 2.1 mmol/L. How did the thiazide cause lithium toxicity?",
        "options": [
            "Distal sodium depletion triggers compensatory proximal tubular reabsorption of sodium and lithium",
            "Thiazides inhibit hepatic glucuronidation of lithium",
            "Hypokalaemia increases blood-brain barrier permeability to lithium",
            "Thiazides compete with lithium for active secretion in the collecting duct",
            "Metabolic alkalosis converts lithium into a lipid-soluble form"
        ],
        "correct_answer": "Distal sodium depletion triggers compensatory proximal tubular reabsorption of sodium and lithium",
        "explanation": "The kidneys handle lithium like sodium, reabsorbing 70–80% in the proximal convoluted tubule. Thiazide-induced sodium depletion in the distal convoluted tubule triggers a compensatory surge in proximal tubular sodium—and lithium—reabsorption, cutting lithium clearance by up to 40%."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 67-year-old man with type 2 diabetes and hypertension develops profuse vomiting and diarrhoea and cannot keep fluids down. He takes metformin, ramipril, and atorvastatin. Pausing metformin ('sick day rules') prevents which life-threatening metabolic complication?",
        "options": [
            "Lactic acidosis",
            "Hyperosmolar hyperglycaemic state (HHS)",
            "Severe hypoglycaemic coma",
            "Syndrome of inappropriate ADH secretion (SIADH)",
            "Acute hepatic necrosis"
        ],
        "correct_answer": "Lactic acidosis",
        "explanation": "Metformin inhibits hepatic gluconeogenesis from lactate and is excreted unchanged by the kidneys. Acute dehydration or AKI causes plasma metformin accumulation alongside tissue hypoperfusion, precipitating fatal metformin-associated lactic acidosis (MALA)."
    },

    # =========================================================================
    # 9. PSYCHIATRY / NEUROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 74-year-old man presents with a 9-month history of a broad-based 'magnetic' shuffling gait, urinary incontinence, and cognitive slowing, without tremor or rigidity. CT head shows ventriculomegaly out of proportion to sulcal atrophy. What is the definitive treatment?",
        "options": [
            "Ventriculoperitoneal (VP) shunt insertion",
            "Subthalamic nucleus deep brain stimulation",
            "Bilateral decompressive craniectomy",
            "Carotid endarterectomy",
            "Oral levodopa-carbidopa therapy"
        ],
        "correct_answer": "Ventriculoperitoneal (VP) shunt insertion",
        "explanation": "The triad of gait apraxia ('magnetic' gait), urinary incontinence, and cognitive decline ('wet, wobbly, and wacky') with disproportionate ventriculomegaly on CT indicates Normal Pressure Hydrocephalus (NPH). It is a reversible dementia treated with ventriculoperitoneal (VP) shunting."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 28-year-old man on fluoxetine takes tramadol and dextromethorphan cough syrup. Six hours later he is agitated, sweaty, and febrile (38.9°C), with HR 132 bpm, BP 164/98 mmHg, dilated pupils, marked lower-limb hyperreflexia, and bilateral ankle clonus. What is the diagnosis?",
        "options": [
            "Serotonin syndrome",
            "Neuroleptic malignant syndrome",
            "Anticholinergic toxidrome",
            "Malignant hyperthermia",
            "Opioid toxicity"
        ],
        "correct_answer": "Serotonin syndrome",
        "explanation": "Combining an SSRI (fluoxetine) with serotonergic agents like tramadol and dextromethorphan precipitates serotonin syndrome. Rapid onset (within hours), hyperreflexia, and inducible ankle clonus distinguish it from neuroleptic malignant syndrome (which causes slow-onset 'lead-pipe' rigidity and hyporeflexia)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 73-year-old woman has 10 days of right temporal headache, scalp tenderness, and jaw claudication, plus two episodes of transient right-eye visual loss today. The right temporal artery is tender and non-pulsatile. What is the immediate management?",
        "options": [
            "Same-day ophthalmology referral for IV methylprednisolone (and 60 mg oral prednisolone immediately)",
            "Oral prednisolone 15 mg daily and routine temporal artery ultrasound",
            "Oral aspirin 300 mg only and TIA clinic referral within 7 days",
            "Withhold steroids until temporal artery biopsy is completed",
            "Oral sumatriptan 50 mg and review in 48 hours"
        ],
        "correct_answer": "Same-day ophthalmology referral for IV methylprednisolone (and 60 mg oral prednisolone immediately)",
        "explanation": "Jaw claudication and scalp tenderness indicate giant cell arteritis (GCA), and transient visual loss (amaurosis fugax) heralds imminent permanent blindness from anterior ischaemic optic neuropathy. GCA with visual symptoms requires immediate IV methylprednisolone (giving 60 mg oral prednisolone immediately if delayed)."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 68-year-old man in sinus rhythm presents 10 hours after onset of an acute right MCA ischaemic stroke (haemorrhage excluded on CT; outside the thrombolysis window). Under NICE guidelines, what is the standard acute and long-term antiplatelet regimen?",
        "options": [
            "Aspirin 300 mg daily for 14 days, then clopidogrel 75 mg daily long-term",
            "Clopidogrel 75 mg daily immediately without initial aspirin",
            "Aspirin 75 mg plus dipyridamole 200 mg twice daily indefinitely",
            "Apixaban 5 mg twice daily started immediately",
            "Aspirin 75 mg plus ticagrelor 90 mg twice daily for 12 months"
        ],
        "correct_answer": "Aspirin 300 mg daily for 14 days, then clopidogrel 75 mg daily long-term",
        "explanation": "Once haemorrhage is excluded on CT, NICE NG128 recommends aspirin 300 mg daily (with gastroprotection) for 14 days in non-cardioembolic acute ischaemic stroke, switching after 14 days (or at discharge) to clopidogrel 75 mg once daily monotherapy for long-term secondary prevention."
    },
    {
        "type": "sba",
        "category": "Psychiatry / Neurology",
        "scenario": "A 61-year-old man who had an anterior STEMI 6 weeks ago presents with a 1-month history of moderate-to-severe depression and wishes to start an antidepressant alongside CBT. Which antidepressant is the safest first-line choice post-MI?",
        "options": [
            "Sertraline",
            "Citalopram",
            "Amitriptyline",
            "Venlafaxine",
            "Phenelzine"
        ],
        "correct_answer": "Sertraline",
        "explanation": "Sertraline is the first-line SSRI after myocardial infarction or in unstable coronary disease (proven safe in the SADHART trial). Citalopram/escitalopram prolong the QT interval, tricyclics (amitriptyline) are cardiotoxic and pro-arrhythmic, and venlafaxine can worsen hypertension."
    },

    # =========================================================================
    # 10. RENAL / UROLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 66-year-old man with hypertension and type 2 diabetes starts ramipril 2.5 mg daily. Baseline bloods were K+ 4.4 mmol/L, creatinine 100 umol/L, and eGFR 68. Two weeks later, bloods show K+ 4.8 mmol/L, creatinine 118 umol/L, and eGFR 56. What is the appropriate action?",
        "options": [
            "Continue ramipril at the same dose and recheck U&Es in 1–2 weeks",
            "Stop ramipril immediately and request urgent CT renal angiography",
            "Switch ramipril to losartan as ARBs do not affect eGFR",
            "Add oral sodium zirconium cyclosilicate",
            "Halve ramipril and start furosemide 40 mg daily"
        ],
        "correct_answer": "Continue ramipril at the same dose and recheck U&Es in 1–2 weeks",
        "explanation": "ACE inhibitors dilate the glomerular efferent arteriole, reducing intraglomerular pressure. A creatinine rise of up to 30% (here 18%) or an eGFR drop of up to 25% (here 18%) with K+ <5.5 mmol/L is an expected renoprotective effect; NICE advises continuing the drug and rechecking U&Es."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 15-year-old boy presents with 2 hours of sudden severe right scrotal and lower abdominal pain with vomiting. He is afebrile, the right testis lies high and transversely, and the right cremasteric reflex is absent. Urine dipstick is negative. What is the immediate action?",
        "options": [
            "Immediate surgical exploration and bilateral orchidopexy",
            "Urgent Doppler ultrasound of the testes to check blood flow",
            "IM ceftriaxone and oral doxycycline for epididymo-orchitis",
            "Manual detorsion and discharge if pain improves",
            "Urgent non-contrast CT abdomen and pelvis"
        ],
        "correct_answer": "Immediate surgical exploration and bilateral orchidopexy",
        "explanation": "Sudden severe scrotal pain, a high-riding transverse testis, and an absent cremasteric reflex indicate acute testicular torsion. Testicular salvage drops sharply after 6 hours: immediate surgical exploration and bilateral orchidopexy are mandatory, without delaying for Doppler ultrasound."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 69-year-old man taking finasteride 5 mg daily for BPH for 9 months requests a PSA test. His PSA returns at 2.8 ng/mL (age-specific upper limit of normal is 4.0 ng/mL). How should this result be interpreted and managed?",
        "options": [
            "Finasteride halves PSA; his corrected PSA is ~5.6 ng/mL, requiring a 2-week wait urology referral",
            "Reassure him that 2.8 ng/mL is below the 4.0 ng/mL cut-off",
            "Stop tamsulosin for 2 weeks and repeat PSA",
            "Prescribe 4 weeks of ciprofloxacin and repeat PSA",
            "Reassure him that finasteride prevents prostate cancer"
        ],
        "correct_answer": "Finasteride halves PSA; his corrected PSA is ~5.6 ng/mL, requiring a 2-week wait urology referral",
        "explanation": "5-alpha-reductase inhibitors (finasteride, dutasteride) shrink prostatic epithelium and halve serum PSA after 6 months. The measured PSA must therefore be doubled (2.8 x 2 = 5.6 ng/mL); since 5.6 ng/mL exceeds the 4.0 ng/mL threshold, an urgent 2-week wait referral is required."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 39-year-old man presents with 3 hours of excruciating waves of left loin-to-groin pain. He is afebrile, eGFR is >90 mL/min/1.73m², and urine dipstick shows 3+ blood with negative nitrites. According to NICE, what is the first-line analgesia and gold-standard imaging?",
        "options": [
            "An NSAID (any route) and low-dose non-contrast CT KUB within 24 hours",
            "IV morphine first-line and an intravenous urogram (IVU)",
            "Oral tamsulosin for analgesia and a plain KUB X-ray",
            "Oral codeine and renal tract ultrasound within 72 hours",
            "IV paracetamol only and contrast-enhanced CT abdomen"
        ],
        "correct_answer": "An NSAID (any route) and low-dose non-contrast CT KUB within 24 hours",
        "explanation": "NICE NG118 recommends an NSAID (e.g. diclofenac or ibuprofen by any route) as first-line analgesia for renal colic, as it reduces prostaglandin-mediated ureteric spasm and glomerular pressure better than opioids. Urgent low-dose non-contrast CT KUB within 24 hours is the diagnostic gold standard."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 22-year-old man passes painless frank red urine 36 hours after developing a viral sore throat. He had a similar self-limiting episode during a cold 18 months ago. BP is 124/76 mmHg, creatinine is 82 umol/L, and C3/C4 complement levels are normal. What is the diagnosis?",
        "options": [
            "IgA nephropathy (Berger's disease)",
            "Post-streptococcal glomerulonephritis",
            "Minimal change disease",
            "Goodpasture's syndrome (anti-GBM disease)",
            "Alport syndrome"
        ],
        "correct_answer": "IgA nephropathy (Berger's disease)",
        "explanation": "Recurrent painless macroscopic haematuria within 24–72 hours of a viral URTI ('synpharyngitic haematuria') with normal complement levels is classic for IgA nephropathy (Berger's disease). In contrast, post-streptococcal glomerulonephritis occurs 1–3 weeks post-infection with low C3."
    },

    # =========================================================================
    # 11. REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY
    # =========================================================================
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 26-year-old woman requests emergency contraception 84 hours (3.5 days) after unprotected intercourse on day 11 of a regular 28-day cycle. She declines a copper IUD and has no medical conditions. Which oral emergency contraceptive is indicated?",
        "options": [
            "Ulipristal acetate 30 mg single oral dose",
            "Levonorgestrel 1.5 mg single oral dose",
            "Levonorgestrel 3 mg double oral dose",
            "Oral mifepristone 200 mg",
            "Desogestrel 75 mcg daily started today"
        ],
        "correct_answer": "Ulipristal acetate 30 mg single oral dose",
        "explanation": "When a copper IUD is declined at 84 hours (3.5 days) post-UPSI, ulipristal acetate (ellaOne 30 mg) is the only effective oral option. Levonorgestrel is licensed only up to 72 hours and fails once the LH surge starts, whereas ulipristal works up to 120 hours (5 days) and up to the LH peak."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 41-year-old woman in her first pregnancy attends her 10-week booking visit. Her BP is 120/74 mmHg, BMI is 36 kg/m², urine dipstick is negative, and she has no medical history. Under NICE guidelines, what pre-eclampsia prophylaxis is indicated?",
        "options": [
            "Oral aspirin 75–150 mg daily from 12 weeks until birth",
            "Oral labetalol 100 mg twice daily starting immediately",
            "High-dose folic acid 5 mg daily as sole prophylaxis",
            "Subcutaneous enoxaparin 40 mg daily from 28 weeks only",
            "No prophylaxis needed as booking BP is normal"
        ],
        "correct_answer": "Oral aspirin 75–150 mg daily from 12 weeks until birth",
        "explanation": "NICE NG133 advises low-dose aspirin (75–150 mg daily from 12 weeks until birth) for women with 1 high-risk factor OR >=2 moderate-risk factors (primigravida, age >=40, pregnancy interval >10 years, BMI >=35, family history of pre-eclampsia, multiple pregnancy). She has three: first pregnancy, age 41, and BMI 36."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A stable 29-year-old woman at 6 weeks gestation has mild left iliac fossa discomfort and spotting. TVUS shows an unruptured 22 mm left tubal ectopic pregnancy with no fetal heartbeat and no free fluid; serum beta-hCG is 1,150 IU/L. Why is she eligible for systemic methotrexate?",
        "options": [
            "Unruptured mass <35 mm, no fetal heartbeat, beta-hCG <1,500 IU/L, and no significant pain",
            "Any ectopic pregnancy qualifies provided there is no vaginal bleeding",
            "A visible fetal heartbeat is required for methotrexate to target trophoblasts",
            "Methotrexate is only used when beta-hCG exceeds 5,000 IU/L",
            "Only left-sided tubal ectopic pregnancies qualify for medical management"
        ],
        "correct_answer": "Unruptured mass <35 mm, no fetal heartbeat, beta-hCG <1,500 IU/L, and no significant pain",
        "explanation": "Under NICE NG126, single-dose IM methotrexate is first-line medical therapy for ectopic pregnancy when all criteria are met: haemodynamically stable without significant pain, unruptured adnexal mass <35 mm, no visible fetal heartbeat, beta-hCG <1,500 IU/L, no intrauterine pregnancy, and reliable follow-up."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 49-year-old woman with an intact uterus has severe hot flushes and night sweats. Her periods have become irregular and her last period was 4 months ago. She has no contraindications to hormone replacement therapy (HRT). Which HRT regimen is appropriate?",
        "options": [
            "Sequential (cyclical) combined HRT",
            "Continuous combined HRT",
            "Unopposed transdermal oestradiol monotherapy",
            "Topical vaginal oestriol cream alone",
            "Oral tibolone started immediately"
        ],
        "correct_answer": "Sequential (cyclical) combined HRT",
        "explanation": "With an intact uterus, progestogen must be given alongside oestrogen to prevent endometrial hyperplasia/cancer. Because her last period was <12 months ago (perimenopausal), sequential (cyclical) combined HRT is required; starting continuous combined HRT or tibolone within 12 months causes erratic breakthrough bleeding."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 31-year-old woman at 9 weeks gestation presents with an uncomplicated lower UTI and is prescribed 7 days of nitrofurantoin. Why was trimethoprim avoided now, and when in pregnancy must nitrofurantoin be avoided?",
        "options": [
            "Trimethoprim is a folate antagonist (1st trimester teratogen); nitrofurantoin risks neonatal haemolysis at term",
            "Trimethoprim causes neonatal haemolysis in the 1st trimester; nitrofurantoin causes neural tube defects at term",
            "Trimethoprim closes the ductus arteriosus; nitrofurantoin causes congenital deafness",
            "Trimethoprim stains fetal teeth; nitrofurantoin causes maternal agranulocytosis at term",
            "Both antibiotics are contraindicated throughout all three trimesters"
        ],
        "correct_answer": "Trimethoprim is a folate antagonist (1st trimester teratogen); nitrofurantoin risks neonatal haemolysis at term",
        "explanation": "Trimethoprim inhibits dihydrofolate reductase and is avoided in the 1st trimester due to neural tube defect risk. Nitrofurantoin is safe in the 1st and 2nd trimesters but avoided at term/late 3rd trimester because immature neonatal erythrocyte glutathione enzymes predispose to neonatal haemolysis."
    },

    # =========================================================================
    # 12. RESPIRATORY
    # =========================================================================
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 24-year-old woman with acute asthma cannot complete sentences. She has RR 28/min, HR 118 bpm, PEF 38% predicted, and SpO2 93% on oxygen. ABG shows: pH 7.36, PaO2 9.6 kPa, and PaCO2 5.3 kPa (4.7–6.0). How is this exacerbation classified?",
        "options": [
            "Life-threatening asthma",
            "Moderate asthma exacerbation",
            "Acute severe asthma",
            "Brittle asthma",
            "Near-fatal asthma"
        ],
        "correct_answer": "Life-threatening asthma",
        "explanation": "While PEF 33–50%, RR >=25/min, and HR >=110 bpm fit acute severe asthma, the critical clue is the 'normal' PaCO2 (5.3 kPa). Hyperventilation during an asthma attack should lower PaCO2 (<4.6 kPa); a normal PaCO2 (4.6–6.0 kPa) signals respiratory muscle exhaustion and defines life-threatening asthma."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 68-year-old smoker with mild heart failure has a right pleural effusion. Results show: serum protein 66 g/L, serum LDH 200 U/L (ULN 210 U/L); pleural protein 28 g/L, pleural LDH 150 U/L. Using Light's criteria, how is this effusion classified?",
        "options": [
            "Exudate, as pleural-to-serum LDH ratio is >0.6 (and pleural LDH >2/3 serum ULN)",
            "Transudate, as pleural-to-serum protein ratio is <0.5",
            "Transudate, as pleural fluid protein is <30 g/L",
            "Exudate, only if all three of Light's criteria are met",
            "Chylothorax, due to discordant protein and LDH"
        ],
        "correct_answer": "Exudate, as pleural-to-serum LDH ratio is >0.6 (and pleural LDH >2/3 serum ULN)",
        "explanation": "When pleural protein is borderline (25–35 g/L), Light's criteria classify an effusion as an EXUDATE if ANY ONE criterion is met: (1) pleural/serum protein >0.5 (28/66 = 0.42), (2) pleural/serum LDH >0.6 (150/200 = 0.75—positive), or (3) pleural LDH >2/3 serum ULN (150 > 140—positive)."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 67-year-old non-smoking ex-smoker with stable COPD has two room-air ABGs taken 3 weeks apart showing PaO2 7.6 kPa and 7.5 kPa. Under NICE guidelines, which additional feature qualifies him for Long-Term Oxygen Therapy (LTOT)?",
        "options": [
            "Peripheral oedema, pulmonary hypertension, or polycythaemia (haematocrit >55%)",
            "FEV1 <50% of predicted",
            "More than two COPD exacerbations in the past year",
            "Smoking <5 cigarettes per day",
            "MRC dyspnoea scale score of 3"
        ],
        "correct_answer": "Peripheral oedema, pulmonary hypertension, or polycythaemia (haematocrit >55%)",
        "explanation": "Under NICE NG115, stable non-smokers qualify for LTOT if PaO2 is <7.3 kPa on two readings >=3 weeks apart, OR if PaO2 is 7.3–8.0 kPa accompanied by secondary polycythaemia (haematocrit >55%), peripheral oedema, pulmonary hypertension (cor pulmonale), or nocturnal hypoxaemia."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 66-year-old man presents with right lower lobe pneumonia. He is alert (AMTS 10/10) with RR 24/min, BP 126/78 mmHg, HR 92 bpm, and venous urea 8.4 mmol/L. What is his CURB-65 score and recommended management?",
        "options": [
            "CURB-65 score 2; consider hospital-supervised treatment",
            "CURB-65 score 1; discharge home on oral amoxicillin",
            "CURB-65 score 3; admit to HDU for IV co-amoxiclav and clarithromycin",
            "CURB-65 score 0; manage conservatively without antibiotics",
            "CURB-65 score 4; intubate and transfer to ICU"
        ],
        "correct_answer": "CURB-65 score 2; consider hospital-supervised treatment",
        "explanation": "CURB-65 awards 1 point each for: Confusion (AMTS <=8) [0], Urea >7 mmol/L [1: 8.4], RR >=30/min [0], BP <90 systolic or <=60 diastolic [0], and Age >=65 [1: 66]. A score of 2 indicates moderate-severity CAP (~9% mortality), warranting hospital-supervised treatment."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 22-year-old man with no lung disease presents with mild right pleuritic chest pain. He is not breathless on walking, observations are normal (SpO2 99% in air), and CXR shows a 2.4 cm primary spontaneous pneumothorax. Under BTS guidelines, what is the appropriate management?",
        "options": [
            "Conservative outpatient management with safety-netting and review",
            "Immediate 28 Fr intercostal chest drain insertion",
            "Emergency needle decompression in the 2nd intercostal space",
            "Urgent VATS pleurodesis today",
            "Inpatient admission for 100% oxygen for 5 days"
        ],
        "correct_answer": "Conservative outpatient management with safety-netting and review",
        "explanation": "Under 2023 BTS pleural guidelines, management of primary spontaneous pneumothorax is guided by breathlessness and physiological stability rather than a rigid 2 cm size cut-off. Stable patients without breathlessness can be safely managed conservatively as outpatients with close follow-up."
    }
]
