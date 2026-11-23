# 🏥 MedBank Studio

**MedBank Studio** is an offline-first medical examination practice platform, purpose-built for UK doctors preparing for the **MSRA (Multi-Specialty Recruitment Assessment)** and other postgraduate medical exams.

Built as a lightweight, single-page web application — no server, no accounts, no subscriptions. Everything runs locally in your browser.

---

## ✨ Features

### 📊 Dashboard
- Real-time stats: total questions, answered count, accuracy %, and bookmarks
- Performance breakdown by clinical specialty with progress bars
- Quick-launch buttons for practice and mock exam sessions

### 📝 Practice Mode
- Filter by **specialty** (Cardiovascular, Paediatrics, Psychiatry, etc.) and **question format**
- Configurable session length (10, 20, 50, or all available questions)
- Immediate answer feedback with detailed clinical explanations
- Bookmark and flag questions for later review

### ⏱️ Exam Simulator
- Timed mock exams replicating the real MSRA format:
  - **Clinical Problem Solving (CPS)** — 97 questions in 75 minutes
  - **Professional Dilemmas (PD)** — 50 questions in 95 minutes
  - **Full Combined Mock** — 147 questions in 170 minutes
- Question navigator with progress tracking
- Score report with domain-level breakdown on completion

### 🔖 Bookmarks
- Save and revisit flagged questions
- Quick-access panel for targeted revision

### 🛠️ Admin Panel
- **Create** custom questions with a graphical editor (SBA, Ranking, Selection formats)
- **Manage** the full question inventory — search, filter, edit, and delete
- **Review flagged questions** reported during practice

### 🎬 Direct-to-Instagram Reel Studio (No Canva Required — Runs on Vercel or Locally)
- **Two Reel Modes:**
  - **Animated Reel:** Kinetic word reading, 1-pass option spotlighting, synthesized soft audio, and answer reveal
  - **Static Reel (No Animations):** Clean static 9:16 video with configurable length (`3s–30s`) and layout (*Question + Options Only* or *With Highlighted Answer & Pearl*)
- **Browser-Native H.264/AAC MP4 Export (WebCodecs + `mp4-muxer`):** Encodes Instagram-compliant `.mp4` directly in Chrome/Edge in ~1–3 seconds — zero FFmpeg and zero Canva needed
- **1-Click "Post Reel"** button directly on Practice, Bookmarks, and Admin question cards with auto-saved preferences (`localStorage`) and live 2,200-char caption editor
- **Cloud-Ready on Vercel:** Uses direct client upload to **Vercel Blob** (bypassing Vercel's 4.5 MB API cap) + stateless serverless functions (`api/ig-create.js`, `api/ig-publish.js`) that auto-delete temp videos after publishing

### 📸 Instagram Carousel Generator
- Auto-generate social media carousels from any practice question
- Customisable themes, fonts, aspect ratios (1:1, 4:5, 9:16)
- Download as images or copy directly to Canva

---

## 📂 Project Structure

```
project-m/
├── index.html                  # Main application HTML
├── styles.css                  # Full design system & styles
├── app.js                      # Core application logic
├── app_instagram.js            # Instagram carousel generator & caption builder
├── app_video.js                # 9:16 Animated & Static Reel Studio + WebCodecs MP4 + direct IG publisher
├── api/                        # Vercel Serverless Functions (Option 1 Cloud Deployment)
│   ├── _ig.js                  # Shared Meta Graph API & passcode helpers
│   ├── status.js               # GET  /api/status
│   ├── blob-upload.js          # POST /api/blob-upload (Vercel Blob client upload signer)
│   ├── ig-test.js              # POST /api/ig-test (Verify Meta credentials & passcode)
│   ├── ig-create.js            # POST /api/ig-create (Create Reel container with video_url + caption)
│   └── ig-publish.js           # POST /api/ig-publish (Poll status, publish Reel, delete temp Blob)
├── package.json                # @vercel/blob dependency for Vercel functions
├── vercel.json                 # Vercel serverless function configuration
├── server.py                   # Optional local zero-dependency server (FFmpeg + Instagram Graph API)
├── start_studio.bat            # Optional Windows 1-click local launcher
├── questions.json              # Curated question bank
├── generate_questions.py       # Master script to assemble and output questions.json
├── clinical_questions.py       # High-Yield Pathognomonic Clinical Questions (60 questions)
├── additional_questions.py     # Additional Clinical & Professional Dilemmas (40 questions)
├── verify_questions.py         # Validation script for question schema
├── .gitignore
└── README.md
```

---

## ☁️ Deploying to Vercel (Recommended — Zero Local Server Needed)

1. **Push this repo to GitHub** and import it into [vercel.com](https://vercel.com/) (Framework Preset: **Other** / leave Build Command blank).
2. **Enable Vercel Blob Storage:**
   - In your Vercel project → **Storage** tab → **Create Database** → **Blob** → connect it to your project.
   - Vercel automatically adds `BLOB_READ_WRITE_TOKEN` to your project.
3. **Add Environment Variables** in Vercel → **Settings → Environment Variables**:
   - `IG_USER_ID` — your Instagram Business/Creator numeric Account ID
   - `IG_ACCESS_TOKEN` — your Meta Unified Login access token (`instagram_basic` + `instagram_content_publish`)
   - `ADMIN_PASSCODE` — any private password/PIN you choose (prevents public visitors from posting to your Instagram)
   - `IG_USERNAME` *(optional)* — e.g. `medqstudios` (shown in the green status pill)
   - `IG_API_VERSION` *(optional, defaults to `v21.0`)*
4. **Redeploy** so the env vars take effect.
5. Open your live Vercel URL in Chrome/Edge → click **Studio** → **Instagram API Setup** → enter your `ADMIN_PASSCODE` → click **Save & Test Connection**.
6. Click **Post Reel** on any question to encode, upload, and publish directly to Instagram!

---

## 🚀 Running Locally (Optional Alternative to Vercel)

1. Double-click **`start_studio.bat`** on Windows, or run `python server.py` and open `http://127.0.0.1:8080`.
2. Open **Studio → Instagram API Setup**, paste your **IG User ID** and **Access Token**, and click **Save & Test Connection** (saved locally to git-ignored `ig_config.json`).

---

## 🧪 Question Bank

The curated question bank contains **100 verified MSRA-format questions** across 12 clinical domains and Professional Dilemmas (zero category duplication):

| Domain / Category | Question Types | Questions |
|-------------------|----------------|-----------|
| Cardiovascular | SBA | 7 |
| Dermatology / Ophthalmology / ENT | SBA | 7 |
| Endocrinology / Metabolic | SBA | 7 |
| Gastroenterology / Clinical Nutrition | SBA | 7 |
| Infectious Diseases / Haematology / Immunology / Allergies / Genetics | SBA | 7 |
| Musculoskeletal | SBA | 7 |
| Paediatrics | SBA | 7 |
| Psychiatry / Neurology | SBA | 7 |
| Renal / Urology | SBA | 7 |
| Reproductive / Obstetrics & Gynaecology | SBA | 7 |
| Respiratory | SBA | 7 |
| Pharmacology | SBA | 7 |
| Professional Dilemmas | Ranking, Selection | 16 |

### Regenerating the Question Bank

If you want to modify or regenerate the base question bank:

```bash
python generate_questions.py
```

This outputs a fresh `questions.json` by assembling the questions from `clinical_questions.py` and `additional_questions.py`.

### Validating Questions

```bash
python verify_questions.py
```

Checks that all questions in `questions.json` conform to the expected schema.

---

## 💾 Data Persistence

All user data is stored in **browser LocalStorage** — nothing leaves your machine:

- Practice stats and accuracy per question
- Bookmarked and flagged questions
- Custom questions created via the Admin Panel
- Mock exam history
- Theme preference (dark/light)

### Importing & Exporting

- **Import**: Load a custom `.json` question bank via the Dashboard → *Import Questions JSON*
- **Export**: Download the full current database (base + custom) via *Export Current Database*

---

## 🎨 Customisation

### Themes
- **Light** and **Dark** modes — toggle via the header icon
- Automatically respects your OS preference on first visit

### Question Formats Supported
| Format | Description |
|--------|-------------|
| **SBA** | Single Best Answer — pick one correct option |
| **Ranking** | Drag-and-drop items into order of appropriateness |
| **Selection** | Choose 3 of 8 options that best address the scenario |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-questions`)
3. Commit your changes (`git commit -m 'Add new cardiology questions'`)
4. Push to the branch (`git push origin feature/new-questions`)
5. Open a Pull Request

### Adding New Questions

The easiest way to add questions is through the **Admin Panel → Add Question** tab in the app itself. Alternatively, add entries directly to `generate_questions.py` and regenerate.

---

## 📄 License

This project is for educational purposes. Please ensure any clinical content is reviewed by a qualified medical professional before use in formal examination preparation.

---

## 🙏 Acknowledgements

- Question content aligned with **NICE Guidelines**, **BNF**, and **Oxford Handbook of Clinical Medicine**
- Built with vanilla HTML, CSS, and JavaScript — no frameworks, no dependencies
- Icons by [Font Awesome](https://fontawesome.com/)
- Typography by [Google Fonts](https://fonts.google.com/) (Inter, Outfit, Playfair Display, Roboto Mono)
