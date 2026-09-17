# -*- coding: utf-8 -*-
"""
Part 3: Renal / Urology, Reproductive / Obstetrics & Gynaecology, Respiratory, Pharmacology
4 clinical domains x 13 questions (8 SBA + 5 EMQ) = 52 questions.
"""

PART3_QUESTIONS = [
    # =========================================================================
    # 9. RENAL / UROLOGY (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 72-year-old woman is admitted with urosepsis and severe dehydration. Despite 3 litres of 0.9% sodium chloride, she remains oliguric. Over 48 hours, her serum creatinine rises from 76 to 380 micromol/L. Urinalysis shows no protein or blood on dipstick, but urine microscopy reveals numerous 'muddy brown' granular epithelial casts. What is the underlying renal pathology?",
        "options": [
            "Acute Tubular Necrosis (ATN)",
            "Pre-renal uraemia",
            "Acute Interstitial Nephritis (AIN)",
            "Post-renal obstructive uropathy",
            "Rapidly Progressive Glomerulonephritis"
        ],
        "correct_answer": "Acute Tubular Necrosis (ATN)",
        "explanation": "Prolonged renal hypoperfusion and sepsis lead to ischaemic and toxic injury of tubular epithelial cells, culminating in Acute Tubular Necrosis (ATN). The presence of coarse 'muddy brown' granular casts composed of sloughed necrotic tubular epithelial cells is pathognomonic of ATN."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 64-year-old man with end-stage renal disease on haemodialysis misses two consecutive dialysis sessions. He presents with profound muscular weakness. A 12-lead ECG demonstrates tall, peaked ('tented') T waves across the precordium, PR interval prolongation, and widening of the QRS complex. His serum potassium is 7.4 mmol/L. What is the single most urgent therapeutic intervention to prevent fatal cardiac arrest?",
        "options": [
            "Intravenous Calcium Gluconate 10% (10-20 mL) over 5-10 minutes",
            "Intravenous soluble insulin (10 units) in 50 mL of 50% Dextrose",
            "Nebulised Salbutamol 10-20 mg",
            "Oral Calcium Resonium (calcium polystyrene sulfonate) 15 g",
            "Intravenous Sodium Bicarbonate 8.4% infusion"
        ],
        "correct_answer": "Intravenous Calcium Gluconate 10% (10-20 mL) over 5-10 minutes",
        "explanation": "In severe hyperkalaemia (K+ >6.5 mmol/L or with ECG changes), the first and most urgent priority is cardioprotection to stabilize the resting myocardial membrane potential and prevent fatal ventricular arrhythmias. Intravenous calcium gluconate (or calcium chloride) provides rapid membrane stabilization within 1-3 minutes. Once the myocardium is protected, intracellular shift agents (insulin/dextrose, salbutamol) are administered."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 36-year-old man presents with sudden-onset, excruciating right flank pain that radiates down into his right groin and scrotum, accompanied by nausea and macroscopic haematuria. He is restless and unable to find a comfortable position. Examination shows normal vitals and no peritonism. What is the initial imaging modality of choice according to NICE guidelines?",
        "options": [
            "Non-contrast CT of the Kidneys, Ureters, and Bladder (CT KUB) within 14 hours",
            "Renal and bladder ultrasound scan",
            "Plain radiograph of the KUB",
            "Intravenous Urogram (IVU)",
            "Contrast-enhanced CT abdomen and pelvis"
        ],
        "correct_answer": "Non-contrast CT of the Kidneys, Ureters, and Bladder (CT KUB) within 14 hours",
        "explanation": "NICE guideline NG118 recommends a non-contrast CT KUB as the first-line imaging modality for adults with suspected renal colic, ideally performed within 14 hours of presentation. It has superior sensitivity (>98%) and specificity for identifying stone size, location, and presence of secondary hydronephrosis."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 16-year-old boy is brought to the ED with a 2-hour history of acute, excruciating left testicular pain and nausea. Examination reveals an exquisitely tender, swollen left hemiscrotum with the testis positioned high and lying horizontally. The cremasteric reflex is completely absent on the left side. What is the immediate mandatory management?",
        "options": [
            "Immediate emergency surgical scrotal exploration and bilateral orchidopexy",
            "Urgent Doppler ultrasound of the scrotum to confirm absent arterial flow",
            "Prescribe oral Ciprofloxacin for epididymo-orchitis",
            "Attempt manual detorsion and discharge if pain resolves",
            "Perform urine microscopy and culture"
        ],
        "correct_answer": "Immediate emergency surgical scrotal exploration and bilateral orchidopexy",
        "explanation": "Testicular torsion is a surgical emergency with a 6-hour golden window to salvage testicular viability. Clinical signs of acute onset pain, high-riding horizontal testis, and absent cremasteric reflex warrant immediate emergency surgical scrotal exploration and bilateral orchidopexy. Doppler ultrasound must NEVER delay transfer to theatre when clinical suspicion is high."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 4-year-old boy presents with progressive generalized periorbital and ankle oedema, abdominal distension from ascites, and frothy urine. Blood tests show: serum albumin 18 g/L (reference 35-50), total cholesterol 8.4 mmol/L. Urinalysis reveals 4+ protein with no blood. What is the most likely diagnosis and recommended initial management?",
        "options": [
            "Minimal Change Disease; commence empirical high-dose oral Prednisolone without renal biopsy",
            "Post-streptococcal glomerulonephritis; oral Penicillin V",
            "Focal Segmental Glomerulosclerosis; urgent renal biopsy",
            "Congenital nephrotic syndrome; immediate bilateral nephrectomy",
            "IgA nephropathy; dietary salt restriction alone"
        ],
        "correct_answer": "Minimal Change Disease; commence empirical high-dose oral Prednisolone without renal biopsy",
        "explanation": "Nephrotic syndrome (triad of massive proteinuria >3+ / >3.5 g/day, hypoalbuminaemia <30 g/L, and oedema) in a child under 8 is due to Minimal Change Disease in >85% of cases. In children with typical presentations, renal biopsy is not indicated initially; high-dose oral corticosteroids (prednisolone 60 mg/m2/day) induce complete remission in over 90%."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 74-year-old man with known benign prostatic hyperplasia (BPH) is unable to pass urine for 14 hours. He is in severe distress with a painful, dull, palpable suprapubic mass extending to the umbilicus. A urethral catheter is successfully placed, draining 1,100 mL of clear urine immediately with total relief of pain. Which medication should be initiated to reduce smooth muscle tone in the prostate and bladder neck?",
        "options": [
            "Tamsulosin",
            "Finasteride",
            "Oxybutynin",
            "Tolterodine",
            "Mirabegron"
        ],
        "correct_answer": "Tamsulosin",
        "explanation": "Alpha-1-adrenoceptor antagonists (such as Tamsulosin or Alfuzosin) rapidly relax prostatic and bladder-neck smooth muscle (within 48 hours), significantly increasing the chance of a successful trial without catheter (TWOC). 5-alpha reductase inhibitors (e.g. Finasteride) take up to 6 months to reduce prostate volume and are used for long-term progression prevention."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "A 42-year-old man presents with persistent hypertension (164/98 mmHg) and microscopic haematuria on routine health check. Abdominal examination reveals bilateral, firm, palpable, ballotable flank masses. His father died of a ruptured intracranial berry aneurysm at age 48. What is the underlying genetic condition and its mode of inheritance?",
        "options": [
            "Autosomal Dominant Polycystic Kidney Disease (ADPKD); autosomal dominant inheritance (PKD1 or PKD2 mutations)",
            "Autosomal Recessive Polycystic Kidney Disease (ARPKD); autosomal recessive inheritance (PKHD1)",
            "Von Hippel-Lindau disease; autosomal dominant inheritance (VHL gene)",
            "Alport syndrome; X-linked dominant inheritance (COL4A5)",
            "Medullary cystic kidney disease; autosomal dominant inheritance"
        ],
        "correct_answer": "Autosomal Dominant Polycystic Kidney Disease (ADPKD); autosomal dominant inheritance (PKD1 or PKD2 mutations)",
        "explanation": "Bilateral ballotable flank masses, hypertension, and a family history of subarachnoid haemorrhage from intracranial berry aneurysm are classic for Autosomal Dominant Polycystic Kidney Disease (ADPKD), most commonly caused by mutations in PKD1 (chromosome 16, 85%) or PKD2 (chromosome 4, 15%). Renal ultrasound is the first-line screening modality."
    },
    {
        "type": "sba",
        "category": "Renal / Urology",
        "scenario": "An 82-year-old woman is found on her living room floor 24 hours after an unwitnessed fall. She is dehydrated with dark red-brown ('tea-coloured') urine. Urine dipstick is strongly positive for blood (3+), but microscopic examination shows only 1-2 red blood cells per high-power field. Serum Creatine Kinase (CK) is 38,000 U/L. What is the cornerstone of emergency management to protect against acute tubular necrosis?",
        "options": [
            "Aggressive intravenous volume resuscitation with 0.9% Sodium Chloride aiming for urine output >=200-300 mL/hr",
            "Urgent intravenous Loop Diuretic boluses with Furosemide",
            "Immediate haemodialysis within 2 hours",
            "Intramuscular Vitamin K administration",
            "Fluid restriction to 500 mL per day"
        ],
        "correct_answer": "Aggressive intravenous volume resuscitation with 0.9% Sodium Chloride aiming for urine output >=200-300 mL/hr",
        "explanation": "The patient has rhabdomyolysis following a prolonged lie. Myoglobinuria causes urine dipstick to test falsely positive for blood (as dipstick orthotolidine reagent reacts with myoglobin heme). Massive myoglobin precipitation in renal tubules induces acute tubular necrosis. The primary preventive and therapeutic intervention is aggressive intravenous crystalloid hydration (0.9% saline) aiming for a brisk urine output of 200-300 mL/hr."
    },
    # Renal / Urology EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Renal / Urology",
        "scenario": "Theme: Glomerular Diseases and Proteinuria. Match each clinical vignette with the most likely diagnosis.\n\nVignette 1: An 8-year-old boy presents with smoky brown ('tea-coloured') urine, facial puffiness, and hypertension 2 weeks after recovering from a streptococcal pharyngitis. Serum C3 complement is low and Anti-Streptolysin O Titre (ASOT) is markedly elevated.",
        "options": [
            "Post-Streptococcal Glomerulonephritis (PSGN)",
            "IgA Nephropathy (Berger's Disease)",
            "Anti-GBM Disease (Goodpasture's Syndrome)",
            "Granulomatosis with Polyangiitis (GPA)",
            "Membranous Nephropathy",
            "Minimal Change Disease",
            "Diabetic Nephropathy",
            "Lupus Nephritis"
        ],
        "correct_answer": "Post-Streptococcal Glomerulonephritis (PSGN)",
        "explanation": "Nephritic syndrome presenting 1-3 weeks following streptococcal pharyngitis with transiently depressed serum C3 and elevated ASOT confirms post-streptococcal glomerulonephritis (PSGN)."
    },
    {
        "type": "emq",
        "category": "Renal / Urology",
        "scenario": "Theme: Glomerular Diseases and Proteinuria. Match each clinical vignette with the most likely diagnosis.\n\nVignette 2: A 24-year-old man presents with macroscopic frank haematuria that started concurrently (within 24-48 hours) with the onset of a sore throat and fever. Blood pressure is 134/86 mmHg. Serum complement levels (C3/C4) are completely normal.",
        "options": [
            "Post-Streptococcal Glomerulonephritis (PSGN)",
            "IgA Nephropathy (Berger's Disease)",
            "Anti-GBM Disease (Goodpasture's Syndrome)",
            "Granulomatosis with Polyangiitis (GPA)",
            "Membranous Nephropathy",
            "Minimal Change Disease",
            "Diabetic Nephropathy",
            "Lupus Nephritis"
        ],
        "correct_answer": "IgA Nephropathy (Berger's Disease)",
        "explanation": "Synpharyngitic macroscopic haematuria occurring within 1-2 days of an upper respiratory tract infection with normal serum complement levels is pathognomonic for IgA Nephropathy (Berger's disease)."
    },
    {
        "type": "emq",
        "category": "Renal / Urology",
        "scenario": "Theme: Glomerular Diseases and Proteinuria. Match each clinical vignette with the most likely diagnosis.\n\nVignette 3: A 32-year-old male smoker presents with hemoptysis, shortness of breath, and acute oliguric renal failure with active red cell casts on urinalysis. Renal biopsy demonstrates linear IgG deposition along the glomerular basement membrane.",
        "options": [
            "Post-Streptococcal Glomerulonephritis (PSGN)",
            "IgA Nephropathy (Berger's Disease)",
            "Anti-GBM Disease (Goodpasture's Syndrome)",
            "Granulomatosis with Polyangiitis (GPA)",
            "Membranous Nephropathy",
            "Minimal Change Disease",
            "Diabetic Nephropathy",
            "Lupus Nephritis"
        ],
        "correct_answer": "Anti-GBM Disease (Goodpasture's Syndrome)",
        "explanation": "Pulmonary-renal syndrome with pulmonary haemorrhage and rapidly progressive glomerulonephritis exhibiting characteristic linear IgG basement membrane deposition confirms Anti-GBM disease (Goodpasture's)."
    },
    {
        "type": "emq",
        "category": "Renal / Urology",
        "scenario": "Theme: Glomerular Diseases and Proteinuria. Match each clinical vignette with the most likely diagnosis.\n\nVignette 4: A 54-year-old man presents with chronic crusting sinusitis, epistaxis, saddle-nose deformity, cough with bilateral cavitating pulmonary nodules, and rapidly deteriorating renal function. Serology demonstrates high c-ANCA (anti-PR3) antibodies.",
        "options": [
            "Post-Streptococcal Glomerulonephritis (PSGN)",
            "IgA Nephropathy (Berger's Disease)",
            "Anti-GBM Disease (Goodpasture's Syndrome)",
            "Granulomatosis with Polyangiitis (GPA)",
            "Membranous Nephropathy",
            "Minimal Change Disease",
            "Diabetic Nephropathy",
            "Lupus Nephritis"
        ],
        "correct_answer": "Granulomatosis with Polyangiitis (GPA)",
        "explanation": "The triad of upper airway necrotising granulomas (sinusitis, nasal crusting), lower respiratory tract lesions (cavitating nodules), and pauci-immune crescentic glomerulonephritis with positive c-ANCA/PR3 confirms GPA."
    },
    {
        "type": "emq",
        "category": "Renal / Urology",
        "scenario": "Theme: Glomerular Diseases and Proteinuria. Match each clinical vignette with the most likely diagnosis.\n\nVignette 5: A 59-year-old man presents with progressive peripheral edema, heavy proteinuria of 6.2 g/24h, and hypoalbuminemia. Autoantibody testing reveals positive circulating Anti-Phospholipase A2 Receptor (anti-PLA2R) antibodies.",
        "options": [
            "Post-Streptococcal Glomerulonephritis (PSGN)",
            "IgA Nephropathy (Berger's Disease)",
            "Anti-GBM Disease (Goodpasture's Syndrome)",
            "Granulomatosis with Polyangiitis (GPA)",
            "Membranous Nephropathy",
            "Minimal Change Disease",
            "Diabetic Nephropathy",
            "Lupus Nephritis"
        ],
        "correct_answer": "Membranous Nephropathy",
        "explanation": "Membranous nephropathy is the most common cause of primary nephrotic syndrome in older adults; the presence of circulating anti-PLA2R autoantibodies (present in 70-80% of primary cases) confirms the diagnosis."
    },

    # =========================================================================
    # 10. REPRODUCTIVE / OBSTETRICS & GYNAECOLOGY (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 27-year-old woman presents with 6 weeks of amenorrhoea and light dark vaginal bleeding. She is hemodynamically stable with mild lower pelvic ache. Transvaginal ultrasound demonstrates an empty uterine cavity with an endometrial thickness of 12 mm, and an unruptured left adnexal mass measuring 2.4 cm with no visible embryonic heartbeat. There is no fluid in the pouch of Douglas. Her serum beta-hCG is 1,250 IU/L. According to NICE guideline NG126, what is the most appropriate management?",
        "options": [
            "Systemic medical management with intramuscular Methotrexate",
            "Immediate emergency laparoscopic salpingectomy",
            "Expectant management with repeat scan in 4 weeks",
            "Dilatation and curettage of the uterus",
            "Oral Mifepristone and Misoprostol"
        ],
        "correct_answer": "Systemic medical management with intramuscular Methotrexate",
        "explanation": "NICE guideline NG126 recommends medical management with intramuscular methotrexate as first-line for women with ectopic pregnancy who are hemodynamically stable, have no significant pain, have an unruptured adnexal mass <35 mm, no visible fetal cardiac activity, serum beta-hCG <1,500 IU/L (or <5,000 IU/L), and are able to attend follow-up."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 32-year-old primigravida at 35 weeks gestation presents with severe frontal headache, visual blurring, and epigastric pain. Blood pressure is 174/112 mmHg and urine protein dipstick is 3+. While lying in the assessment room, she suddenly suffers a generalized tonic-clonic convulsion. What is the immediate first-line pharmacological treatment of choice to terminate the seizure and prevent recurrences?",
        "options": [
            "Intravenous Magnesium Sulphate (4 g loading dose over 5-15 min, followed by 1 g/hr infusion)",
            "Intravenous Diazepam 10 mg bolus",
            "Intravenous Phenytoin 18 mg/kg infusion",
            "Intravenous Labetalol 50 mg bolus alone",
            "Emergency delivery via caesarean section while convulsing"
        ],
        "correct_answer": "Intravenous Magnesium Sulphate (4 g loading dose over 5-15 min, followed by 1 g/hr infusion)",
        "explanation": "This patient has eclampsia (generalized tonic-clonic seizures in a woman with pre-eclampsia). The definitive first-line medication for terminating and preventing further eclamptic seizures is intravenous Magnesium Sulphate (Collaborative Eclampsia Trial protocol: 4 g IV over 5-15 mins, followed by 1 g/hr for 24 hours post-delivery or post-last seizure). Antihypertensives (IV labetalol) and prompt delivery are arranged once the mother is stabilized."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 26-year-old woman has just delivered a 4.1 kg infant via normal vaginal delivery. Ten minutes after delivery of the placenta, there is brisk continuous vaginal haemorrhage totalling 1,200 mL. On abdominal palpation, the uterine fundus is soft, boggy, and located above the umbilicus. What is the most common underlying cause of primary postpartum haemorrhage (PPH) and the immediate initial step?",
        "options": [
            "Uterine atony; perform bimanual uterine compression and administer intravenous Oxytocin",
            "Retained placental fragments; immediate manual removal of placenta under general anaesthesia",
            "Cervical laceration; transfer to theatre for speculum examination",
            "Disseminated intravascular coagulation; transfuse fresh frozen plasma",
            "Uterine inversion; perform Johnson's manoeuvre"
        ],
        "correct_answer": "Uterine atony; perform bimanual uterine compression and administer intravenous Oxytocin",
        "explanation": "Uterine atony is the cause of >70-80% of primary postpartum haemorrhages (PPH, defined as >=500 mL blood loss within 24 hours). The soft, 'boggy' uncontracted fundus confirms uterine atony. Immediate management involves bimanual uterine compression (rubbing up the fundus), catheterisation, intravenous oxytocin bolus and infusion, tranexamic acid, and second-line uterotonics (ergometrine, carboprost, misoprostol)."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 34-year-old woman at 33 weeks gestation presents with sudden-onset severe, constant, 'tearing' abdominal pain and dark vaginal bleeding. On abdominal examination, the uterus is hypertonic, tender, and described as 'woody' hard to touch. The fetal heart rate tracing demonstrates prolonged decelerations. What is the most likely diagnosis?",
        "options": [
            "Placental abruption (abruptio placentae)",
            "Placenta praevia",
            "Vasa praevia",
            "Uterine rupture",
            "Preterm labour"
        ],
        "correct_answer": "Placental abruption (abruptio placentae)",
        "explanation": "Severe constant abdominal pain, dark vaginal bleeding (which may be concealed), a hypertonic, woody, exquisitely tender uterus, and fetal distress are diagnostic of placental abruption. In contrast, placenta praevia typically presents with painless, bright red bleeding and a soft, non-tender uterus."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 23-year-old woman with a known 5 cm benign dermoid cyst in her right ovary presents with sudden-onset, severe, sharp right iliac fossa pain radiating to the groin, accompanied by repeated vomiting. On examination, there is marked localized guarding in the right iliac fossa. Bedside urinary beta-hCG is negative. What is the definitive management of choice?",
        "options": [
            "Urgent diagnostic laparoscopy with detorsion and ovarian cystectomy",
            "Intravenous broad-spectrum antibiotics and observation for 24 hours",
            "Transvaginal ultrasound-guided cyst aspiration",
            "Oral analgesia and outpatient gynaecology review",
            "High-dose oral Progestogen therapy"
        ],
        "correct_answer": "Urgent diagnostic laparoscopy with detorsion and ovarian cystectomy",
        "explanation": "Ovarian torsion is a gynaecological emergency where the ovary twists around its infundibulopelvic ligament, causing venous and arterial compromise. Immediate diagnostic laparoscopy is required to untwist the ischaemic ovary (which often recovers viable function even if dark/cyanotic) and preserve ovarian reserve, followed by cystectomy."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 21-year-old sexually active woman presents with lower bilateral abdominal pain, deep dyspareunia, and abnormal purulent vaginal discharge. On bimanual examination, there is marked cervical motion tenderness ('cervical excitation') and bilateral adnexal tenderness. What is the recommended empirical outpatient antibiotic regimen for pelvic inflammatory disease (PID) according to UK BASHH guidelines?",
        "options": [
            "Intramuscular Ceftriaxone 1 g stat plus oral Doxycycline 100 mg BD and oral Metronidazole 400 mg BD for 14 days",
            "Oral Amoxicillin 500 mg TDS for 7 days",
            "Single dose of oral Azithromycin 1 g",
            "Oral Ciprofloxacin 500 mg BD for 5 days",
            "Intramuscular Gentamicin plus oral Erythromycin"
        ],
        "correct_answer": "Intramuscular Ceftriaxone 1 g stat plus oral Doxycycline 100 mg BD and oral Metronidazole 400 mg BD for 14 days",
        "explanation": "BASHH guidelines for outpatient management of acute PID recommend intramuscular Ceftriaxone 1 g stat (to cover Neisseria gonorrhoeae) combined with oral Doxycycline 100 mg twice daily (to cover Chlamydia trachomatis and Mycoplasma genitalium) and oral Metronidazole 400 mg twice daily (to cover anaerobes) for 14 days."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 28-year-old woman presents with oligomenorrhoea, hirsutism, cystic acne, and difficulty conceiving for 18 months. Her BMI is 32 kg/m2. Pelvic ultrasound reveals enlarged ovaries with >20 peripherally arranged follicles in each ovary ('string of pearls' appearance). She wishes to conceive. What is the first-line pharmacological treatment for ovulation induction in Polycystic Ovary Syndrome (PCOS)?",
        "options": [
            "Letrozole",
            "Clomifene citrate plus Metformin",
            "Combined Oral Contraceptive Pill",
            "Exogenous Gonadotrophin injections",
            "Cyproterone acetate"
        ],
        "correct_answer": "Letrozole",
        "explanation": "According to international evidence-based guidelines and current UK practice, Letrozole (an aromatase inhibitor) is now recommended as the first-line pharmacological treatment for ovulation induction in anovulatory PCOS, demonstrating significantly higher live birth and ovulation rates compared with clomifene citrate, with a lower risk of multiple pregnancy."
    },
    {
        "type": "sba",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "A 58-year-old postmenopausal woman (amenorrhoeic for 6 years) presents to her GP reporting a single episode of painless, fresh vaginal spotting 3 days ago. She is not taking hormone replacement therapy. Abdominal and speculum examinations are normal. What is the mandatory next step according to NICE suspected cancer guidelines (NG12)?",
        "options": [
            "Urgent direct access 2-week-wait (2WW) referral for transvaginal ultrasound scan and gynaecology assessment",
            "Prescribe oral Tranexamic acid and review if bleeding recurs",
            "Perform a cervical smear test in the practice and reassure",
            "Prescribe topical vaginal oestrogen cream for presumed atrophic vaginitis",
            "Reassure that a single episode of spotting is common in menopause"
        ],
        "correct_answer": "Urgent direct access 2-week-wait (2WW) referral for transvaginal ultrasound scan and gynaecology assessment",
        "explanation": "Any postmenopausal bleeding (defined as vaginal bleeding occurring >=12 months after the cessation of menstruation) must be treated as endometrial cancer until proven otherwise. NICE guideline NG12 mandates an urgent 2-week wait referral for transvaginal ultrasound (to assess endometrial thickness; cutoff usually >4 mm warrants endometrial biopsy/pipelle)."
    },
    # Reproductive / O&G EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "Theme: Contraception and Emergency Contraception. Match each clinical scenario with the most appropriate contraceptive method.\n\nVignette 1: A 23-year-old woman requests emergency contraception 96 hours (4 days) after unprotected sexual intercourse. She has a BMI of 24 kg/m2 and wishes to have the most effective available emergency method that also provides ongoing long-term contraception.",
        "options": [
            "Copper Intrauterine Device (Cu-IUD)",
            "Ulipristal Acetate (ellaOne)",
            "Levonorgestrel (Levonelle)",
            "Desogestrel (Progestogen-Only Pill)",
            "Combined Hormonal Contraceptive Pill",
            "Intramuscular Depot Medroxyprogesterone Acetate",
            "Etonogestrel Subdermal Implant",
            "Levonorgestrel Intrauterine System (Mirena)"
        ],
        "correct_answer": "Copper Intrauterine Device (Cu-IUD)",
        "explanation": "The Copper IUD is the most effective method of emergency contraception (>99% effective) and can be inserted up to 5 days (120 hours) after unprotected intercourse or up to 5 days after the earliest calculated day of ovulation, providing immediate long-term contraception."
    },
    {
        "type": "emq",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "Theme: Contraception and Emergency Contraception. Match each clinical scenario with the most appropriate contraceptive method.\n\nVignette 2: A 28-year-old woman presents 80 hours after unprotected sex. She declines an intrauterine device. She takes no regular medications. What is the recommended oral emergency contraceptive pill?",
        "options": [
            "Copper Intrauterine Device (Cu-IUD)",
            "Ulipristal Acetate (ellaOne)",
            "Levonorgestrel (Levonelle)",
            "Desogestrel (Progestogen-Only Pill)",
            "Combined Hormonal Contraceptive Pill",
            "Intramuscular Depot Medroxyprogesterone Acetate",
            "Etonogestrel Subdermal Implant",
            "Levonorgestrel Intrauterine System (Mirena)"
        ],
        "correct_answer": "Ulipristal Acetate (ellaOne)",
        "explanation": "Ulipristal acetate (ellaOne) is licensed for emergency oral contraception up to 120 hours (5 days) after unprotected intercourse and is more effective than Levonorgestrel between 72 and 120 hours."
    },
    {
        "type": "emq",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "Theme: Contraception and Emergency Contraception. Match each clinical scenario with the most appropriate contraceptive method.\n\nVignette 3: A 32-year-old woman presents 24 hours after UPSI requesting oral emergency contraception. She has a BMI of 34 kg/m2 and prefers Levonorgestrel. What modification is required for levonorgestrel in patients with a BMI >30 kg/m2 (or weight >70 kg)?",
        "options": [
            "Copper Intrauterine Device (Cu-IUD)",
            "Ulipristal Acetate (ellaOne)",
            "Levonorgestrel (Levonelle)",
            "Desogestrel (Progestogen-Only Pill)",
            "Combined Hormonal Contraceptive Pill",
            "Intramuscular Depot Medroxyprogesterone Acetate",
            "Etonogestrel Subdermal Implant",
            "Levonorgestrel Intrauterine System (Mirena)"
        ],
        "correct_answer": "Levonorgestrel (Levonelle)",
        "explanation": "Levonorgestrel (Levonelle) is licensed up to 72 hours post-UPSI; FSRH guidelines recommend doubling the dose (to 3 mg) in women weighing >70 kg or with a BMI >30 kg/m2, as efficacy is significantly reduced at standard dosing."
    },
    {
        "type": "emq",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "Theme: Contraception and Emergency Contraception. Match each clinical scenario with the most appropriate contraceptive method.\n\nVignette 4: A 29-year-old woman who has severe migraine with visual aura seeks contraception. She has no other medical conditions. Which oral contraceptive option is completely safe and UKMEC 1 (no restriction)?",
        "options": [
            "Copper Intrauterine Device (Cu-IUD)",
            "Ulipristal Acetate (ellaOne)",
            "Levonorgestrel (Levonelle)",
            "Desogestrel (Progestogen-Only Pill)",
            "Combined Hormonal Contraceptive Pill",
            "Intramuscular Depot Medroxyprogesterone Acetate",
            "Etonogestrel Subdermal Implant",
            "Levonorgestrel Intrauterine System (Mirena)"
        ],
        "correct_answer": "Desogestrel (Progestogen-Only Pill)",
        "explanation": "Migraine with aura is an absolute contraindication (UKMEC 4) to oestrogen-containing combined hormonal contraceptives due to heightened ischaemic stroke risk. Progestogen-only methods (e.g. Desogestrel POP) carry no stroke risk and are UKMEC 1."
    },
    {
        "type": "emq",
        "category": "Reproductive / Obstetrics & Gynaecology",
        "scenario": "Theme: Contraception and Emergency Contraception. Match each clinical scenario with the most appropriate contraceptive method.\n\nVignette 5: A 38-year-old mother who smokes 20 cigarettes a day presents requesting the combined oral contraceptive pill. According to UK Medical Eligibility Criteria for Contraceptive Use (UKMEC), why is this pill classified as UKMEC 4 (unacceptable health risk)?",
        "options": [
            "Copper Intrauterine Device (Cu-IUD)",
            "Ulipristal Acetate (ellaOne)",
            "Levonorgestrel (Levonelle)",
            "Desogestrel (Progestogen-Only Pill)",
            "Combined Hormonal Contraceptive Pill",
            "Intramuscular Depot Medroxyprogesterone Acetate",
            "Etonogestrel Subdermal Implant",
            "Levonorgestrel Intrauterine System (Mirena)"
        ],
        "correct_answer": "Combined Hormonal Contraceptive Pill",
        "explanation": "Women aged >=35 who smoke >=15 cigarettes per day have a substantially increased risk of myocardial infarction and venous thromboembolism, making combined hormonal contraceptives an absolute contraindication (UKMEC 4)."
    },

    # =========================================================================
    # 11. RESPIRATORY (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 52-year-old woman presents with acute pleuritic right-sided chest pain and sudden-onset shortness of breath 5 days following a total hip replacement. Vitals: HR 116 bpm, RR 26 breaths/min, BP 128/78 mmHg, SpO2 93% on room air. Her two-level Wells PE score is calculated as 6 points ('PE likely'). What is the most appropriate next management step according to NICE guidelines?",
        "options": [
            "Commence therapeutic anticoagulation (e.g., Apixaban) immediately and arrange an urgent CT Pulmonary Angiogram (CTPA)",
            "Measure serum D-Dimer before considering anticoagulation or imaging",
            "Perform a diagnostic ventilation-perfusion (V/Q) SPECT scan as first-line",
            "Order an immediate portable chest radiograph and discharge if normal",
            "Administer intravenous Alteplase thrombolysis"
        ],
        "correct_answer": "Commence therapeutic anticoagulation (e.g., Apixaban) immediately and arrange an urgent CT Pulmonary Angiogram (CTPA)",
        "explanation": "When PE is 'likely' (Wells score >4 points), NICE guideline NG158 recommends offering immediate therapeutic anticoagulation (DOAC such as Apixaban or Rivaroxaban, or LMWH) without waiting for imaging, followed by an urgent CTPA. D-dimer testing should NOT be used when PE is likely."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 24-year-old man with brittle asthma presents to the ED severe breathlessness. On arrival, he is unable to complete a sentence in one breath. Vitals: RR 32 breaths/min, HR 122 bpm, SpO2 93% on air. His Peak Expiratory Flow Rate (PEFR) is 220 L/min (42% of his predicted best). Auscultation reveals widespread expiratory polyphonic wheezing throughout both lungs. How is this asthma attack classified according to BTS/SIGN guidelines?",
        "options": [
            "Acute severe asthma",
            "Moderate asthma exacerbation",
            "Life-threatening asthma",
            "Near-fatal asthma",
            "Mild chronic asthma"
        ],
        "correct_answer": "Acute severe asthma",
        "explanation": "BTS/SIGN guidelines define acute severe asthma by the presence of any one of: PEFR 33-50% predicted/best, RR >=25 breaths/min, HR >=110 bpm, or inability to complete sentences in one breath. Life-threatening features would include PEFR <33%, SpO2 <92%, silent chest, cyanosis, exhaustion, hypotension, arrhythmia, or normal/elevated PaCO2."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 21-year-old tall, thin male presents to the ED with sudden-onset right pleuritic chest pain and breathlessness. Over 15 minutes, his condition deteriorates rapidly: he is diaphoretic, cyanosed, RR is 38 breaths/min, BP is 78/48 mmHg, and HR is 138 bpm. Examination reveals hyperresonance and absent breath sounds over the right hemithorax, with the trachea deviated markedly to the left. What is the immediate mandatory intervention?",
        "options": [
            "Immediate needle decompression with a large-bore cannula in the 2nd intercostal space mid-clavicular line (or 4th/5th ICS anterior axillary line)",
            "Emergency portable chest X-ray to confirm pneumothorax",
            "High-flow oxygen and wait for cardiothoracic surgical review",
            "Immediate endotracheal intubation and positive pressure ventilation",
            "Perform an emergency bedside echocardiogram"
        ],
        "correct_answer": "Immediate needle decompression with a large-bore cannula in the 2nd intercostal space mid-clavicular line (or 4th/5th ICS anterior axillary line)",
        "explanation": "This patient has a life-threatening tension pneumothorax with obstructive shock. It is a strictly clinical diagnosis. An urgent chest radiograph must NEVER be performed, as delay is fatal. Immediate needle decompression relieves intrathoracic pressure, followed by definitive intercostal chest drain insertion."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 67-year-old man with severe COPD (FEV1 34% predicted) has been clinically stable on maximal inhaler therapy for 2 months. He is a non-smoker for 5 years. Resting arterial blood gas on room air measured on two separate occasions 4 weeks apart shows: PaO2 7.1 kPa (53 mmHg), PaCO2 5.8 kPa. He has no peripheral oedema, polycythaemia, or signs of pulmonary hypertension. Does he meet the criteria for Long-Term Oxygen Therapy (LTOT)?",
        "options": [
            "Yes, because his stable resting PaO2 is consistently below 7.3 kPa",
            "No, resting PaO2 must be <6.0 kPa to qualify for LTOT",
            "No, LTOT is only indicated if cor pulmonale is also present",
            "Yes, but only if used solely during exercise and sleep",
            "No, LTOT causes life-threatening CO2 retention and is contraindicated"
        ],
        "correct_answer": "Yes, because his stable resting PaO2 is consistently below 7.3 kPa",
        "explanation": "NICE and BTS guidelines recommend LTOT for stable COPD patients who have a resting PaO2 <7.3 kPa on air, or PaO2 between 7.3 and 8.0 kPa if there is secondary polycythaemia, peripheral oedema, nocturnal hypoxaemia, or pulmonary hypertension. LTOT must be used for at least 15 hours per day to improve survival."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 76-year-old man presents with fever, cough productive of purulent green sputum, and right-sided pleuritic chest pain. On examination, he is confused with an Abbreviated Mental Test score of 6/10. Vitals: RR 32 breaths/min, BP 106/64 mmHg. Investigations: blood urea 9.2 mmol/L (reference <7.0). Chest X-ray demonstrates right lower lobe consolidation. What is his CURB-65 score and recommended place of care?",
        "options": [
            "CURB-65 score 3; urgent hospital admission and consideration of intensive/high dependency care",
            "CURB-65 score 1; safe for outpatient home management with oral Amoxicillin",
            "CURB-65 score 2; short-stay hospital observation only",
            "CURB-65 score 4; requires immediate mechanical ventilation",
            "CURB-65 score 0; discharge with safety netting"
        ],
        "correct_answer": "CURB-65 score 3; urgent hospital admission and consideration of intensive/high dependency care",
        "explanation": "CURB-65 criteria (1 point each): Confusion (AMTS <=8) = 1, Urea >7 mmol/L = 1, Respiratory rate >=30 = 1, Blood pressure (<90 systolic or <=60 diastolic) = 0, Age >=65 = 1. Total score = 1 + 1 + 1 + 0 + 1 = 4? Wait: C=1 (AMTS 6), U=1 (9.2), R=1 (32), B=0 (106/64), Age=1 (76). Total CURB-65 score is 4, indicating severe pneumonia with high mortality requiring hospital admission and consideration of critical care."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 68-year-old man presents with a 9-month history of insidious, progressive exertional breathlessness and a dry, hacking cough. On examination, there is prominent finger clubbing and bilateral, fine, end-inspiratory 'velcro-like' crackles at both lung bases. High-resolution CT (HRCT) of the chest demonstrates bilateral subpleural, basal-predominant reticular opacities with architectural distortion and honeycombing with traction bronchiectasis. What is the diagnosis?",
        "options": [
            "Idiopathic Pulmonary Fibrosis (IPF) with usual interstitial pneumonia (UIP) pattern",
            "Hypersensitivity pneumonitis",
            "Sarcoidosis",
            "Chronic obstructive pulmonary disease (COPD)",
            "Congestive heart failure"
        ],
        "correct_answer": "Idiopathic Pulmonary Fibrosis (IPF) with usual interstitial pneumonia (UIP) pattern",
        "explanation": "Clubbing, fine 'velcro' bibasilar end-inspiratory crackles, and classic HRCT features of honeycombing and subpleural reticulation without alternative etiology confirm Idiopathic Pulmonary Fibrosis (IPF). Antifibrotic agents (Pirfenidone or Nintedanib) are recommended by NICE if FVC is between 50% and 80%."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 28-year-old Afro-Caribbean woman presents with tender red pretibial skin nodules (erythema nodosum), bilateral ankle arthralgia, and mild dry cough. She is otherwise systemically well. A routine chest radiograph reveals prominent, symmetrical bilateral hilar lymphadenopathy without parenchymal lung infiltrates. What is the diagnosis and typical prognosis?",
        "options": [
            "Löfgren's syndrome (acute sarcoidosis); has an excellent prognosis with spontaneous resolution in >80%",
            "Tuberculosis; requires immediate quadruple antituberculous therapy",
            "Stage IV Sarcoidosis; requires lifelong oral corticosteroids",
            "Hodgkin lymphoma; requires immediate systemic chemotherapy",
            "Bronchogenic small-cell carcinoma; poor prognosis"
        ],
        "correct_answer": "Löfgren's syndrome (acute sarcoidosis); has an excellent prognosis with spontaneous resolution in >80%",
        "explanation": "Löfgren's syndrome is a well-recognized acute benign subtype of sarcoidosis characterized by the triad of erythema nodosum, bilateral hilar lymphadenopathy (BHL), and polyarthralgia/arthritis (especially ankles). It carries a remarkably favorable prognosis, with spontaneous remission occurring in >80-90% of cases, managed symptomatically with NSAIDs."
    },
    {
        "type": "sba",
        "category": "Respiratory",
        "scenario": "A 46-year-old woman with a history of recurrent severe childhood pneumonia presents with chronic daily cough productive of copious, thick, purulent sputum and intermittent haemoptysis for 5 years. Auscultation reveals coarse pan-inspiratory crackles and scattered expiratory wheeze. A high-resolution CT (HRCT) scan demonstrates internal bronchial lumen diameter greater than the adjacent pulmonary artery ('signet ring sign') and bronchial wall thickening. What is the primary cornerstone of long-term management?",
        "options": [
            "Airway clearance techniques (chest physiotherapy) and prompt antibiotic treatment of infective exacerbations",
            "Lifelong daily oral Prednisolone",
            "Prophylactic surgical lobectomy",
            "Continuous long-term inhaled corticosteroid monotherapy",
            "Therapeutic bronchoscopy every 3 months"
        ],
        "correct_answer": "Airway clearance techniques (chest physiotherapy) and prompt antibiotic treatment of infective exacerbations",
        "explanation": "The clinical picture and characteristic HRCT 'signet-ring' sign (bronchodilatation with broncho-arterial ratio >1) confirm bronchiectasis. BTS guidelines identify chest physiotherapy (airway clearance techniques, e.g. active cycle of breathing techniques, flutter devices) as the foundation of maintenance management to prevent mucus plugging, paired with targeted antibiotics for acute exacerbations."
    },
    # Respiratory EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Respiratory",
        "scenario": "Theme: Pleural Disease and Thoracic Pathology. Match each scenario with the most likely diagnosis.\n\nVignette 1: A 64-year-old man with severe alcoholic liver cirrhosis presents with a massive right-sided pleural effusion. Pleural fluid aspiration reveals clear fluid with a protein concentration of 18 g/L (reference <30 g/L), LDH of 85 U/L (normal), and Light's criteria are negative.",
        "options": [
            "Transudative Pleural Effusion (Hepatic Hydrothorax)",
            "Exudative Pleural Effusion (Parapneumonic)",
            "Malignant Mesothelioma",
            "Pancoast Tumour (Superior Sulcus Tumour)",
            "Obstructive Sleep Apnoea (OSAHS)",
            "Empyema",
            "Chylothorax",
            "Pleural Plaque"
        ],
        "correct_answer": "Transudative Pleural Effusion (Hepatic Hydrothorax)",
        "explanation": "Pleural fluid protein <30 g/L with negative Light's criteria defines a transudative effusion, caused by altered hydrostatic/oncotic forces (most commonly congestive cardiac failure, liver cirrhosis, or nephrotic syndrome)."
    },
    {
        "type": "emq",
        "category": "Respiratory",
        "scenario": "Theme: Pleural Disease and Thoracic Pathology. Match each scenario with the most likely diagnosis.\n\nVignette 2: A 48-year-old man being treated for severe bacterial pneumonia develops a worsening fever and pleuritic chest pain. Diagnostic pleural tap reveals cloudy fluid with protein 44 g/L, pleural LDH 1,200 U/L, pH 6.95 (<7.2), and low glucose 1.8 mmol/L. An urgent chest tube is inserted.",
        "options": [
            "Transudative Pleural Effusion (Hepatic Hydrothorax)",
            "Exudative Pleural Effusion (Parapneumonic)",
            "Malignant Mesothelioma",
            "Pancoast Tumour (Superior Sulcus Tumour)",
            "Obstructive Sleep Apnoea (OSAHS)",
            "Empyema",
            "Chylothorax",
            "Pleural Plaque"
        ],
        "correct_answer": "Empyema",
        "explanation": "A complicated parapneumonic effusion or empyema is indicated by pleural fluid acidosis (pH <7.2), low glucose, and high LDH; BTS guidelines mandate immediate tube drainage (chest drain) alongside IV antibiotics."
    },
    {
        "type": "emq",
        "category": "Respiratory",
        "scenario": "Theme: Pleural Disease and Thoracic Pathology. Match each scenario with the most likely diagnosis.\n\nVignette 3: A 72-year-old retired shipyard worker presents with persistent dull, aching chest wall pain, weight loss, and recurrent haemorrhagic pleural effusions. CT chest demonstrates nodular, diffuse, circumferential pleural thickening with mediastinal pleural involvement.",
        "options": [
            "Transudative Pleural Effusion (Hepatic Hydrothorax)",
            "Exudative Pleural Effusion (Parapneumonic)",
            "Malignant Mesothelioma",
            "Pancoast Tumour (Superior Sulcus Tumour)",
            "Obstructive Sleep Apnoea (OSAHS)",
            "Empyema",
            "Chylothorax",
            "Pleural Plaque"
        ],
        "correct_answer": "Malignant Mesothelioma",
        "explanation": "Diffuse nodular circumferential pleural thickening in a patient with past asbestos exposure presenting with relentless non-pleuritic chest wall pain is typical of malignant pleural mesothelioma."
    },
    {
        "type": "emq",
        "category": "Respiratory",
        "scenario": "Theme: Pleural Disease and Thoracic Pathology. Match each scenario with the most likely diagnosis.\n\nVignette 4: A 63-year-old smoker presents with severe unrelenting pain in his right shoulder radiating down the inner medial aspect of his right arm and hand (C8-T1 distribution). He has right-sided ptosis, miosis, and anhidrosis on his right forehead.",
        "options": [
            "Transudative Pleural Effusion (Hepatic Hydrothorax)",
            "Exudative Pleural Effusion (Parapneumonic)",
            "Malignant Mesothelioma",
            "Pancoast Tumour (Superior Sulcus Tumour)",
            "Obstructive Sleep Apnoea (OSAHS)",
            "Empyema",
            "Chylothorax",
            "Pleural Plaque"
        ],
        "correct_answer": "Pancoast Tumour (Superior Sulcus Tumour)",
        "explanation": "An apical lung tumour invading the cervical sympathetic chain (causing Horner's syndrome: ptosis, miosis, anhidrosis) and brachial plexus (C8-T1 hand wasting/radicular pain) is a Pancoast tumour."
    },
    {
        "type": "emq",
        "category": "Respiratory",
        "scenario": "Theme: Pleural Disease and Thoracic Pathology. Match each scenario with the most likely diagnosis.\n\nVignette 5: A 52-year-old HGV driver with a BMI of 38 kg/m2 presents with excessive daytime sleepiness, morning headaches, and an Epworth Sleepiness Scale score of 16/24. His partner reports loud habitual snoring and witnessed nocturnal choking episodes. Continuous Positive Airway Pressure (CPAP) is indicated.",
        "options": [
            "Transudative Pleural Effusion (Hepatic Hydrothorax)",
            "Exudative Pleural Effusion (Parapneumonic)",
            "Malignant Mesothelioma",
            "Pancoast Tumour (Superior Sulcus Tumour)",
            "Obstructive Sleep Apnoea (OSAHS)",
            "Empyema",
            "Chylothorax",
            "Pleural Plaque"
        ],
        "correct_answer": "Obstructive Sleep Apnoea (OSAHS)",
        "explanation": "Obstructive Sleep Apnoea/Hypopnoea Syndrome (OSAHS) presents with daytime hypersomnolence (elevated Epworth score), witnessed apnoeic episodes, and obesity. CPAP is the gold-standard treatment for moderate-to-severe symptomatic disease."
    },

    # =========================================================================
    # 12. PHARMACOLOGY (8 SBA + 5 EMQ)
    # =========================================================================
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 48-year-old woman with severe rheumatoid arthritis is initiated on oral Methotrexate 15 mg. Which critical counselling point and co-prescribing requirement is mandatory to minimize toxicity and avoid fatal overdoses?",
        "options": [
            "Methotrexate is taken strictly ONCE A WEEK on a fixed day, and Folic Acid 5 mg should be co-prescribed to be taken on a different day",
            "Methotrexate must be taken three times daily with meals",
            "Folic acid must be taken simultaneously with methotrexate at the exact same hour",
            "Avoid taking paracetamol while on methotrexate",
            "Routine monitoring of full blood count is only required once every 2 years"
        ],
        "correct_answer": "Methotrexate is taken strictly ONCE A WEEK on a fixed day, and Folic Acid 5 mg should be co-prescribed to be taken on a different day",
        "explanation": "Methotrexate is a dihydrofolate reductase inhibitor taken strictly ONCE WEEKLY. Daily administration causes fatal bone marrow suppression and gastrointestinal toxicity. Folic acid (e.g. 5 mg once weekly, taken 24-48 hours after methotrexate) must be co-prescribed to prevent stomatitis, nausea, and myelosuppression."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 74-year-old man taking Warfarin for atrial fibrillation presents with major gastrointestinal bleeding and haematemesis. Blood pressure is 88/54 mmHg, heart rate is 120 bpm, and his urgent INR is 8.6. What is the immediate treatment of choice to rapidly reverse his anticoagulation according to British Society for Haematology guidelines?",
        "options": [
            "Withhold Warfarin, administer Intravenous Phytomenadione (Vitamin K1) 5-10 mg, and give Four-Factor Prothrombin Complex Concentrate (PCC)",
            "Administer Fresh Frozen Plasma (FFP) alone",
            "Withhold Warfarin and observe for 24 hours without reversal agents",
            "Administer Protamine sulphate intravenously",
            "Administer Idarucizumab bolus"
        ],
        "correct_answer": "Withhold Warfarin, administer Intravenous Phytomenadione (Vitamin K1) 5-10 mg, and give Four-Factor Prothrombin Complex Concentrate (PCC)",
        "explanation": "In life-threatening major bleeding on warfarin, guidelines mandate immediate reversal using four-factor Prothrombin Complex Concentrate (PCC, containing factors II, VII, IX, and X), which restores haemostasis within minutes, alongside intravenous Vitamin K1 (Phytomenadione 5-10 mg) to stimulate sustained hepatic synthesis of clotting factors. FFP takes hours to infuse and has inferior efficacy."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "An 82-year-old woman with chronic kidney disease taking Digoxin 125 mcg daily presents with nausea, vomiting, confusion, and yellow-tinted visual disturbances ('xanthopsia'). Her ECG shows down-sloping 'reverse-tick' ST depressions, ventricular ectopics, and a heart rate of 42 bpm. Serum potassium is 6.2 mmol/L and serum digoxin level is 4.1 nmol/L (therapeutic range 0.6-1.3). What is the definitive antidote?",
        "options": [
            "Digoxin-specific antibody fragments (DigiFab / Digibind)",
            "Intravenous Atropine alone",
            "Intravenous Calcium chloride bolus",
            "Intravenous Amiodarone infusion",
            "Oral activated charcoal alone"
        ],
        "correct_answer": "Digoxin-specific antibody fragments (DigiFab / Digibind)",
        "explanation": "Digoxin toxicity presents with gastrointestinal symptoms, yellow-green visual halos (xanthopsia), life-threatening arrhythmias, and hyperkalaemia. Digoxin-specific antibody fragments (DigiFab) bind free intravascular digoxin and represent the definitive life-saving antidote for severe toxicity or hemodynamic instability. Note: IV calcium is contraindicated in digoxin toxicity due to risk of refractory cardiac arrest ('stone heart')."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 62-year-old woman is treated with once-daily intravenous Gentamicin for severe hospital-acquired sepsis. To prevent both irreversible ototoxicity (vestibular and cochlear hair cell damage) and acute nephrotoxicity, which pharmacokinetic measurement is most essential prior to the next scheduled dose?",
        "options": [
            "Pre-dose trough serum Gentamicin concentration",
            "Peak serum Gentamicin concentration 30 minutes after infusion",
            "Serum amylase level",
            "24-hour urinary clearance of gentamicin",
            "Serum albumin level"
        ],
        "correct_answer": "Pre-dose trough serum Gentamicin concentration",
        "explanation": "Aminoglycosides (Gentamicin, Amikacin) exhibit concentration-dependent killing and time-dependent toxicity. Trough levels (measured immediately prior to the next dose) reflect clearance and drug accumulation; elevated trough levels (>1 mg/L in once-daily dosing regimens) dramatically increase the risk of acute tubular necrosis and permanent sensorineural hearing loss/vestibulotoxicity."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 20-year-old woman is brought to the ED 3 hours after taking an intentional acute single overdose of forty 500 mg tablets of Paracetamol (20 g total). She has no vomiting and appears clinically well. According to the UK National Poisons Information Service (TOXBASE) guidelines, what is the correct protocol regarding paracetamol level testing and N-acetylcysteine (NAC)?",
        "options": [
            "Measure serum paracetamol concentration exactly at 4 hours post-ingestion, plot on the treatment nomogram, and commence IV N-Acetylcysteine if on or above the single treatment line",
            "Start intravenous N-Acetylcysteine immediately and do not measure paracetamol levels",
            "Perform gastric lavage immediately",
            "Measure paracetamol levels immediately at 3 hours and decide treatment based on that value",
            "Withhold all treatment until liver enzymes (ALT/AST) become elevated"
        ],
        "correct_answer": "Measure serum paracetamol concentration exactly at 4 hours post-ingestion, plot on the treatment nomogram, and commence IV N-Acetylcysteine if on or above the single treatment line",
        "explanation": "In single acute paracetamol ingestions, blood levels taken before 4 hours cannot be interpreted reliably against the paracetamol treatment nomogram due to ongoing absorption. The blood sample must be drawn at 4 hours post-ingestion (or immediately if presenting after 4 hours) and plotted on the single nomogram line (100 mg/L at 4 hours). If the level is at or above the line, IV N-acetylcysteine is commenced."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 56-year-old man with hypertension is commenced on Ramipril 5 mg. Six weeks later, his blood pressure is well-controlled at 126/80 mmHg, but he complains of an irritating, dry, non-productive nocturnal cough that keeps him awake. He has no dyspnoea, chest pain, or wheeze. What is the mechanism of this cough and the most appropriate management?",
        "options": [
            "Accumulation of bradykinin and substance P in the lungs; switch to an Angiotensin Receptor Blocker (ARB) such as Losartan",
            "Direct allergic bronchospasm; prescribe inhaled Salbutamol",
            "Secondary heart failure; add high-dose Furosemide",
            "Upper respiratory tract infection; prescribe oral Amoxicillin",
            "Pulmonary fibrosis; stop all antihypertensive therapy permanently"
        ],
        "correct_answer": "Accumulation of bradykinin and substance P in the lungs; switch to an Angiotensin Receptor Blocker (ARB) such as Losartan",
        "explanation": "Angiotensin-Converting Enzyme (ACE) is responsible for the degradation of both angiotensin I and bradykinin. ACE inhibitors lead to accumulation of bradykinin and substance P in the respiratory tract, causing a persistent dry cough in up to 15% of patients. The recommended management is switching to an Angiotensin Receptor Blocker (ARB, e.g. Losartan or Candesartan), which does not affect bradykinin breakdown."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 66-year-old man taking Atorvastatin 40 mg daily for secondary cardiovascular prevention develops severe community-acquired pneumonia. His GP prescribes a 7-day course of oral Clarithromycin. Four days later, he presents with profound generalized muscle aches, dark urine, and a serum CK of 26,000 U/L. What is the pharmacological basis for this adverse event?",
        "options": [
            "Clarithromycin potent inhibition of hepatic CYP3A4 significantly increases circulating atorvastatin concentrations, precipitating rhabdomyolysis",
            "Atorvastatin inhibits the renal tubular secretion of clarithromycin",
            "Clarithromycin induces cytochrome P450 enzymes causing rapid drug breakdown",
            "Direct immunological hypersensitivity between statins and macrolides",
            "Statin-induced competitive inhibition of macrolide protein synthesis"
        ],
        "correct_answer": "Clarithromycin potent inhibition of hepatic CYP3A4 significantly increases circulating atorvastatin concentrations, precipitating rhabdomyolysis",
        "explanation": "Atorvastatin and Simvastatin are extensively metabolized by cytochrome P450 enzyme CYP3A4. Macrolide antibiotics (Clarithromycin and Erythromycin) are potent CYP3A4 inhibitors. Co-administration dramatically increases statin plasma concentrations, greatly multiplying the risk of statin-induced myopathy and life-threatening rhabdomyolysis. The statin should be temporarily withheld during macrolide therapy."
    },
    {
        "type": "sba",
        "category": "Pharmacology",
        "scenario": "A 23-year-old woman with generalized tonic-clonic epilepsy presents to her GP. She is currently taking Sodium Valproate 500 mg twice daily. According to UK MHRA safety regulations and guidelines, what is the mandatory requirement regarding sodium valproate in female patients of childbearing potential?",
        "options": [
            "Sodium Valproate is contraindicated in women of childbearing potential unless enrolled in the Valproate Pregnancy Prevention Programme (Prevent) with highly effective contraception and annual specialist review",
            "Sodium Valproate can be freely prescribed provided high-dose oral Vitamin C is co-prescribed",
            "Valproate can only be prescribed if the patient is over 35 years old",
            "Valproate is completely safe during the first trimester of pregnancy",
            "No special precautions are required if liver function tests are normal"
        ],
        "correct_answer": "Sodium Valproate is contraindicated in women of childbearing potential unless enrolled in the Valproate Pregnancy Prevention Programme (Prevent) with highly effective contraception and annual specialist review",
        "explanation": "Sodium valproate is associated with a 10% risk of congenital malformations (neural tube defects, craniofacial clefts, cardiac defects) and a 30-40% risk of neurodevelopmental disorders/autism. UK MHRA guidelines mandate that valproate must NOT be used in females of childbearing potential unless conditions of the Pregnancy Prevention Programme ('Prevent') are met, including signed risk acknowledgement, specialist review, and highly effective contraception."
    },
    # Pharmacology EMQ Theme (5 scenarios)
    {
        "type": "emq",
        "category": "Pharmacology",
        "scenario": "Theme: Specific Toxicological Antidotes. Match each poisoning/toxicology scenario with the correct antidote.\n\nVignette 1: An unconscious 24-year-old known heroin user is brought to the ED by paramedics. Vitals: RR 6 breaths/min, oxygen saturation 82% on air, HR 52 bpm, and pupils are pinpoint (1 mm bilaterally). Intravenous administration of this opioid antagonist immediately restores respiratory drive.",
        "options": [
            "Naloxone",
            "Flumazenil",
            "Glucagon",
            "High-Flow Normobaric / Hyperbaric Oxygen",
            "Protamine Sulphate",
            "N-Acetylcysteine",
            "Pralidoxime",
            "Desferrioxamine"
        ],
        "correct_answer": "Naloxone",
        "explanation": "Naloxone is a competitive pure opioid receptor antagonist that rapidly reverses opioid-induced respiratory depression, central nervous system depression, and miosis."
    },
    {
        "type": "emq",
        "category": "Pharmacology",
        "scenario": "Theme: Specific Toxicological Antidotes. Match each poisoning/toxicology scenario with the correct antidote.\n\nVignette 2: A 42-year-old woman is admitted following an intentional overdose of 60 tablets of Diazepam. She is deeply comatose with normal pupil responses and mild hypoventilation. Which specific benzodiazepine receptor antagonist is reserved for severe acute toxicity or reversing procedural sedation?",
        "options": [
            "Naloxone",
            "Flumazenil",
            "Glucagon",
            "High-Flow Normobaric / Hyperbaric Oxygen",
            "Protamine Sulphate",
            "N-Acetylcysteine",
            "Pralidoxime",
            "Desferrioxamine"
        ],
        "correct_answer": "Flumazenil",
        "explanation": "Flumazenil is a competitive antagonist at the GABAA-benzodiazepine receptor complex; while it rapidly reverses sedation, it carries a risk of precipitating intractable seizures in chronic benzodiazepine users or mixed tricyclic antidepressant ingestions."
    },
    {
        "type": "emq",
        "category": "Pharmacology",
        "scenario": "Theme: Specific Toxicological Antidotes. Match each poisoning/toxicology scenario with the correct antidote.\n\nVignette 3: A 55-year-old man intentionally ingests 100 tablets of Propranolol. He presents in cardiogenic shock with a heart rate of 32 bpm, BP 68/40 mmHg, and blood glucose of 2.8 mmol/L refractory to atropine and fluid boluses. Which agent bypasses beta-adrenergic receptors by stimulating adenylate cyclase directly?",
        "options": [
            "Naloxone",
            "Flumazenil",
            "Glucagon",
            "High-Flow Normobaric / Hyperbaric Oxygen",
            "Protamine Sulphate",
            "N-Acetylcysteine",
            "Pralidoxime",
            "Desferrioxamine"
        ],
        "correct_answer": "Glucagon",
        "explanation": "Intravenous Glucagon (5-10 mg bolus followed by infusion) is the antidote of choice for refractory beta-blocker overdose, acting independently of beta-receptors to increase intracellular cyclic AMP and restore myocardial contractility and heart rate."
    },
    {
        "type": "emq",
        "category": "Pharmacology",
        "scenario": "Theme: Specific Toxicological Antidotes. Match each poisoning/toxicology scenario with the correct antidote.\n\nVignette 4: Two individuals are found confused and nauseated inside a poorly ventilated caravan containing a faulty paraffin heater. Arterial blood gas co-oximetry reveals a carboxyhaemoglobin (COHb) level of 28% (reference <3% in non-smokers). What is the mandatory immediate treatment?",
        "options": [
            "Naloxone",
            "Flumazenil",
            "Glucagon",
            "High-Flow Normobaric / Hyperbaric Oxygen",
            "Protamine Sulphate",
            "N-Acetylcysteine",
            "Pralidoxime",
            "Desferrioxamine"
        ],
        "correct_answer": "High-Flow Normobaric / Hyperbaric Oxygen",
        "explanation": "Carbon monoxide poisoning shifts the oxygen-haemoglobin dissociation curve to the left and impairs cellular respiration. 100% high-flow normobaric oxygen via a non-rebreather reservoir mask drastically shortens the half-life of carboxyhaemoglobin from 320 minutes to <80 minutes."
    },
    {
        "type": "emq",
        "category": "Pharmacology",
        "scenario": "Theme: Specific Toxicological Antidotes. Match each poisoning/toxicology scenario with the correct antidote.\n\nVignette 5: A patient undergoing renal replacement therapy receives an accidental massive overdose of intravenous Unfractionated Heparin, developing acute retroperitoneal haemorrhage. What is the specific basic peptide that binds and neutralizes heparin?",
        "options": [
            "Naloxone",
            "Flumazenil",
            "Glucagon",
            "High-Flow Normobaric / Hyperbaric Oxygen",
            "Protamine Sulphate",
            "N-Acetylcysteine",
            "Pralidoxime",
            "Desferrioxamine"
        ],
        "correct_answer": "Protamine Sulphate",
        "explanation": "Protamine sulphate is a strongly basic polycationic peptide that binds strongly to acidic unfractionated heparin, forming an inactive stable salt complex that completely reverses heparin's anticoagulant activity."
    }
]
