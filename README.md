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
├── app_instagram.js            # Instagram carousel generator module
├── questions.json              # Base question bank (~880 KB)
├── generate_questions.py       # Python script to generate the question bank
├── additional_questions.py     # Supplementary question definitions
├── verify_questions.py         # Validation script for question schema
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, Safari)
- No build tools, no package manager, no server required

### Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/project-m.git
   cd project-m
   ```

2. **Open the app**

   Simply open `index.html` in your browser, or use a local dev server:
   ```bash
   # Using Python
   python -m http.server 8080

   # Using Node.js (npx)
   npx serve .
   ```

3. **Navigate to** `http://localhost:8080`

> **Note:** The app loads `questions.json` via `fetch()`, so opening `index.html` directly as a file may be blocked by CORS in some browsers. Use a local server for best results.

---

## 🧪 Question Bank

The default question bank contains **880+ MSRA-format questions** across 12 clinical domains:

| Domain | Question Types |
|--------|---------------|
| Cardiovascular | SBA |
| Dermatology / Ophthalmology / ENT | SBA |
| Endocrinology / Metabolic | SBA |
| Gastroenterology / Clinical Nutrition | SBA |
| Infectious Diseases / Haematology / Immunology | SBA |
| Musculoskeletal | SBA |
| Paediatrics | SBA |
| Psychiatry / Neurology | SBA |
| Renal / Urology | SBA |
| Reproductive / Sexual Health | SBA |
| Respiratory | SBA |
| Professional Dilemmas | Ranking, Selection |

### Regenerating the Question Bank

If you want to modify or regenerate the base question bank:

```bash
python generate_questions.py
```

This outputs a fresh `questions.json` using the templates defined in `generate_questions.py` and `additional_questions.py`.

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
