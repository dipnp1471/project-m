/**
 * MedBank Studio - Main Application Logic
 * Offline-first medical question bank with local persistence, mock simulator, and editor.
 */

// Application State
const state = {
  questions: [],          // Combined array of base + custom questions
  customQuestions: [],    // Questions created by the user or imported
  activeExam: "MSRA",     // Active exam filter
  
  // User Session / Stats (Persisted in LocalStorage)
  answeredQuestionIds: [], // List of IDs that have been solved
  questionAttempts: {},   // Map of ID -> { attempts: count, correct: boolean }
  bookmarkedIds: [],      // Bookmarked question IDs
  flaggedQuestions: {},   // Map of ID -> reason string (reported questions)
  mockHistory: [],        // Records of completed mock exams
  
  // Active Practice Session State
  activePractice: {
    questions: [],
    currentIndex: 0,
    answers: {},          // Map of index -> user selection/ranking
    submitted: {},        // Map of index -> boolean (has submitted answer)
  },
  
  // Active Exam Simulator State
  activeExamSim: {
    mode: "pd",           // "pd", "cps", "full"
    questions: [],
    currentIndex: 0,
    answers: {},          // Map of index -> user selection/ranking
    timer: null,
    secondsRemaining: 0,
    totalSeconds: 0,
    startTime: null,
  }
};

// --- INITIALIZATION ---
document.addEventListener("DOMContentLoaded", async () => {
  setupTheme();
  loadProgressFromStorage();
  await loadQuestionsDatabase();
  initEventListeners();
  renderDashboard();
});

// Theme Management (Dark/Light)
function setupTheme() {
  const themeToggle = document.getElementById("theme-toggle");
  const storedTheme = localStorage.getItem("theme");
  const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  
  const activeTheme = storedTheme || (systemPrefersDark ? "dark" : "light");
  document.documentElement.setAttribute("data-theme", activeTheme);
  updateThemeToggleIcon(activeTheme);
  
  themeToggle.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateThemeToggleIcon(newTheme);
  });
}

function updateThemeToggleIcon(theme) {
  const icon = document.querySelector("#theme-toggle i");
  if (theme === "dark") {
    icon.className = "fa-solid fa-sun";
  } else {
    icon.className = "fa-solid fa-moon";
  }
}

// Load user progress and customization from LocalStorage
function loadProgressFromStorage() {
  try {
    state.customQuestions = JSON.parse(localStorage.getItem("custom_questions")) || [];
    state.answeredQuestionIds = JSON.parse(localStorage.getItem("answered_question_ids")) || [];
    state.questionAttempts = JSON.parse(localStorage.getItem("question_attempts")) || {};
    state.bookmarkedIds = JSON.parse(localStorage.getItem("bookmarked_ids")) || [];
    state.flaggedQuestions = JSON.parse(localStorage.getItem("flagged_questions")) || {};
    state.mockHistory = JSON.parse(localStorage.getItem("mock_history")) || [];
    state.activeExam = localStorage.getItem("active_exam") || "MSRA";
  } catch (e) {
    console.error("Error loading progress from LocalStorage:", e);
  }
}

// Save specific state properties to LocalStorage
function saveStateToStorage(key) {
  try {
    if (key === "custom_questions") localStorage.setItem("custom_questions", JSON.stringify(state.customQuestions));
    if (key === "answered_question_ids") localStorage.setItem("answered_question_ids", JSON.stringify(state.answeredQuestionIds));
    if (key === "question_attempts") localStorage.setItem("question_attempts", JSON.stringify(state.questionAttempts));
    if (key === "bookmarked_ids") localStorage.setItem("bookmarked_ids", JSON.stringify(state.bookmarkedIds));
    if (key === "flagged_questions") localStorage.setItem("flagged_questions", JSON.stringify(state.flaggedQuestions));
    if (key === "mock_history") localStorage.setItem("mock_history", JSON.stringify(state.mockHistory));
    if (key === "active_exam") localStorage.setItem("active_exam", state.activeExam);
  } catch (e) {
    console.error(`Error saving ${key} to LocalStorage:`, e);
  }
}

// Fetch base questions and merge with custom questions, letting custom overrides take priority
async function loadQuestionsDatabase() {
  try {
    const response = await fetch("questions.json");
    if (!response.ok) throw new Error("Could not fetch base questions database.");
    const baseQuestions = await response.json();
    
    // Filter base questions that have custom overrides or have been deleted
    const customIds = state.customQuestions.map(q => q.id);
    const deletedBaseIds = JSON.parse(localStorage.getItem("deleted_base_ids")) || [];
    
    const uniqueBase = baseQuestions.filter(q => 
      !customIds.includes(q.id) && !deletedBaseIds.includes(q.id)
    );
    
    state.questions = [...uniqueBase, ...state.customQuestions];
  } catch (e) {
    console.warn("Base questions.json not found or empty. Relying on custom questions:", e);
    state.questions = [...state.customQuestions];
  }
  
  populateExamSelector();
  populateSpecialtyFilters();
  populateAdminFilters();
}

// Populate the Exam drop-down in the header
function populateExamSelector() {
  const selector = document.getElementById("exam-selector");
  // Extract unique exams
  const exams = [...new Set(state.questions.map(q => q.exam))];
  
  if (exams.length === 0 && !exams.includes("MSRA")) {
    exams.push("MSRA");
  }
  
  selector.innerHTML = "";
  exams.forEach(exam => {
    const option = document.createElement("option");
    option.value = exam;
    option.textContent = `${exam} Examination`;
    if (exam === state.activeExam) option.selected = true;
    selector.appendChild(option);
  });
  
  selector.addEventListener("change", (e) => {
    state.activeExam = e.target.value;
    saveStateToStorage("active_exam");
    populateSpecialtyFilters();
    renderDashboard();
    // Close practice or exam rooms if open
    document.getElementById("practice-room").style.display = "none";
    document.querySelector(".practice-config").style.display = "flex";
    document.getElementById("exam-simulation-screen").style.display = "none";
    document.getElementById("exam-intro-screen").style.display = "flex";
    document.getElementById("exam-results-screen").style.display = "none";
  });
}

// Populate clinical specialties filters dynamically based on loaded exam questions
function populateSpecialtyFilters() {
  const categorySelector = document.getElementById("practice-category-select");
  const currentExamQuestions = state.questions.filter(q => q.exam === state.activeExam);
  const categories = [...new Set(currentExamQuestions.map(q => q.category))];
  
  categorySelector.innerHTML = '<option value="all">All Domains / Specialties</option>';
  categories.forEach(cat => {
    const option = document.createElement("option");
    option.value = cat;
    option.textContent = cat;
    categorySelector.appendChild(option);
  });
}

// --- EVENT LISTENERS ---
function initEventListeners() {
  // Navigation Tabs
  const navButtons = document.querySelectorAll(".nav-tabs button");
  navButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      // Toggle tab buttons
      navButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      
      // Toggle panels
      const targetPanelId = btn.getAttribute("data-tab");
      document.querySelectorAll(".tab-panel").forEach(panel => {
        panel.classList.remove("active");
      });
      document.getElementById(targetPanelId).classList.add("active");
      
      // Refresh views on switch
      if (targetPanelId === "dashboard-panel") renderDashboard();
      if (targetPanelId === "bookmarks-panel") renderBookmarks();
      if (targetPanelId === "admin-panel") {
        setupCreatorFormOptions();
        setupAdminTabPanelNavigation();
        renderAdminManageQuestionsList();
        renderAdminFlaggedQuestionsList();
      }
    });
  });
  
  // Dashboard Buttons
  document.getElementById("reset-stats-btn").addEventListener("click", resetUserStats);
  document.getElementById("quick-start-practice").addEventListener("click", () => {
    // Quick practice of 10 questions of any type/category
    document.getElementById("practice-category-select").value = "all";
    document.getElementById("practice-type-select").value = "all";
    document.getElementById("practice-count-select").value = "10";
    document.getElementById("tab-practice").click();
    document.getElementById("start-practice-btn").click();
  });
  document.getElementById("quick-start-mock").addEventListener("click", () => {
    document.getElementById("tab-exam").click();
  });
  
  // Import/Export Database Modal Controls
  const importModal = document.getElementById("import-modal");
  const fileInput = document.getElementById("import-json-file");
  const importFilename = document.getElementById("import-filename-display");
  const confirmImportBtn = document.getElementById("confirm-import-btn");
  
  document.getElementById("open-import-modal").addEventListener("click", () => {
    importModal.style.display = "flex";
  });
  document.getElementById("close-import-modal").addEventListener("click", () => {
    importModal.style.display = "none";
    fileInput.value = "";
    importFilename.textContent = "No file selected";
    confirmImportBtn.disabled = true;
  });
  
  fileInput.addEventListener("change", (e) => {
    if (e.target.files.length > 0) {
      importFilename.textContent = e.target.files[0].name;
      confirmImportBtn.disabled = false;
    }
  });
  
  confirmImportBtn.addEventListener("click", handleFileImport);
  document.getElementById("export-questions-btn").addEventListener("click", handleDatabaseExport);
  
  // Practice Room Session Controls
  document.getElementById("start-practice-btn").addEventListener("click", startPracticeSession);
  document.getElementById("prev-question-btn").addEventListener("click", showPrevPracticeQuestion);
  document.getElementById("next-question-btn").addEventListener("click", showNextPracticeQuestion);
  document.getElementById("submit-answer-btn").addEventListener("click", submitPracticeAnswer);
  document.getElementById("bookmark-question-btn").addEventListener("click", toggleActiveQuestionBookmark);
  document.getElementById("flag-question-btn").addEventListener("click", toggleActiveQuestionFlag);
  document.getElementById("end-practice-session").addEventListener("click", endPracticeSession);
  
  // Exam Simulator controls
  document.getElementById("start-exam-sim-btn").addEventListener("click", startExamSimulation);
  document.getElementById("sim-prev-question-btn").addEventListener("click", showPrevSimQuestion);
  document.getElementById("sim-next-question-btn").addEventListener("click", showNextSimQuestion);
  document.getElementById("submit-exam-sim-btn").addEventListener("click", confirmSubmitExamSim);
  document.getElementById("abandon-exam-sim-btn").addEventListener("click", abandonExamSim);
  document.getElementById("sim-bookmark-question-btn").addEventListener("click", toggleSimQuestionBookmark);
  document.getElementById("sim-flag-question-btn").addEventListener("click", toggleSimQuestionFlag);
  document.getElementById("close-results-btn").addEventListener("click", () => {
    document.getElementById("exam-results-screen").style.display = "none";
    document.getElementById("exam-intro-screen").style.display = "flex";
    document.getElementById("tab-dashboard").click();
  });
  
  // Question Creator Form Controls
  document.getElementById("creator-type").addEventListener("change", setupCreatorFormOptions);
  document.getElementById("creator-add-option-btn").addEventListener("click", addNewCreatorOptionRow);
  document.getElementById("clear-creator-form-btn").addEventListener("click", clearCreatorForm);
  document.getElementById("question-creator-form").addEventListener("submit", saveCreatedQuestion);
}

// --- DASHBOARD LOGIC ---
function renderDashboard() {
  const currentExamQuestions = state.questions.filter(q => q.exam === state.activeExam);
  const totalQs = currentExamQuestions.length;
  
  // Solved count for this exam
  const examQuestionIds = currentExamQuestions.map(q => q.id);
  const solvedQs = state.answeredQuestionIds.filter(id => examQuestionIds.includes(id)).length;
  
  // Average Score for this exam
  let totalScorePercent = 0;
  let attemptsCount = 0;
  let correctAttempts = 0;
  
  examQuestionIds.forEach(id => {
    if (state.questionAttempts[id]) {
      attemptsCount++;
      if (state.questionAttempts[id].correct) correctAttempts++;
    }
  });
  
  const avgAccuracy = attemptsCount > 0 ? Math.round((correctAttempts / attemptsCount) * 100) : 0;
  
  // Bookmarks count for this exam
  const bookmarksCount = state.bookmarkedIds.filter(id => examQuestionIds.includes(id)).length;
  
  // Update UI Stats
  document.getElementById("stat-total-questions").textContent = totalQs;
  document.getElementById("stat-answered-questions").textContent = `${solvedQs} (${Math.round((solvedQs / (totalQs || 1)) * 100)}%)`;
  document.getElementById("stat-average-score").textContent = `${avgAccuracy}%`;
  document.getElementById("stat-bookmarked-count").textContent = bookmarksCount;
  
  // Render Performance list
  const perfList = document.getElementById("specialty-performance-list");
  perfList.innerHTML = "";
  
  const specialties = [...new Set(currentExamQuestions.map(q => q.category))];
  
  if (specialties.length === 0) {
    perfList.innerHTML = '<p style="grid-column: span 2; text-align: center; color: var(--text-tertiary);">No questions loaded yet for this exam.</p>';
    return;
  }
  
  specialties.forEach(spec => {
    const specQuestions = currentExamQuestions.filter(q => q.category === spec);
    const specIds = specQuestions.map(q => q.id);
    
    // Solved in this specialty
    const specSolved = state.answeredQuestionIds.filter(id => specIds.includes(id)).length;
    const specAttempts = specIds.filter(id => state.questionAttempts[id]);
    const specCorrect = specAttempts.filter(id => state.questionAttempts[id].correct).length;
    
    const accuracy = specAttempts.length > 0 ? Math.round((specCorrect / specAttempts.length) * 100) : 0;
    const solvedPercent = Math.round((specSolved / (specQuestions.length || 1)) * 100);
    
    const perfItem = document.createElement("div");
    perfItem.className = "perf-item";
    perfItem.innerHTML = `
      <div class="perf-header">
        <span class="perf-name" title="${spec}">${spec}</span>
        <span class="perf-val">${accuracy}% Accuracy (${specSolved}/${specQuestions.length})</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: ${solvedPercent}%;"></div>
      </div>
    `;
    perfList.appendChild(perfItem);
  });
}

function resetUserStats() {
  if (confirm("Are you sure you want to reset all practice stats, bookmarks, and mock exam history for all exams? This cannot be undone.")) {
    state.answeredQuestionIds = [];
    state.questionAttempts = {};
    state.bookmarkedIds = [];
    state.mockHistory = [];
    
    saveStateToStorage("answered_question_ids");
    saveStateToStorage("question_attempts");
    saveStateToStorage("bookmarked_ids");
    saveStateToStorage("mock_history");
    
    renderDashboard();
    alert("Stats reset successfully!");
  }
}

// --- IMPORT & EXPORT UTILITIES ---
function handleFileImport() {
  const fileInput = document.getElementById("import-json-file");
  const file = fileInput.files[0];
  if (!file) return;
  
  const reader = new FileReader();
  reader.onload = function(e) {
    try {
      const importedData = JSON.parse(e.target.result);
      if (!Array.isArray(importedData)) throw new Error("File content must be a JSON array of questions.");
      
      // Validate schema of first few questions to make sure it's valid
      const requiredKeys = ["id", "exam", "type", "category", "scenario", "options", "correct_answer", "explanation"];
      importedData.slice(0, 5).forEach(q => {
        requiredKeys.forEach(key => {
          if (!(key in q)) throw new Error(`Missing required key '${key}' in imported questions.`);
        });
      });
      
      // Merge with custom questions, checking for duplicates by ID
      let mergeCount = 0;
      importedData.forEach(importedQ => {
        const index = state.customQuestions.findIndex(q => q.id === importedQ.id);
        if (index > -1) {
          // Overwrite existing
          state.customQuestions[index] = importedQ;
        } else {
          // Append new
          state.customQuestions.push(importedQ);
          mergeCount++;
        }
      });
      
      saveStateToStorage("custom_questions");
      loadQuestionsDatabase();
      
      alert(`Import Successful! Merged/Added ${mergeCount} questions into the local database.`);
      document.getElementById("close-import-modal").click();
      renderDashboard();
    } catch (err) {
      alert(`Import Failed: ${err.message}`);
    }
  };
  reader.readAsText(file);
}

function handleDatabaseExport() {
  try {
    const dataStr = JSON.stringify(state.questions, null, 2);
    const dataBlob = new Blob([dataStr], { type: "application/json" });
    const url = URL.createObjectURL(dataBlob);
    
    const downloadAnchor = document.createElement("a");
    downloadAnchor.href = url;
    downloadAnchor.download = "questions_database.json";
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    
    document.body.removeChild(downloadAnchor);
    URL.revokeObjectURL(url);
  } catch (err) {
    alert("Export Failed: Could not create download package.");
  }
}

// --- PRACTICE SESSION LOGIC ---
function startPracticeSession() {
  const catFilter = document.getElementById("practice-category-select").value;
  const typeFilter = document.getElementById("practice-type-select").value;
  const countFilter = document.getElementById("practice-count-select").value;
  
  // Filter questions for current exam
  let filtered = state.questions.filter(q => q.exam === state.activeExam);
  
  if (catFilter !== "all") {
    filtered = filtered.filter(q => q.category === catFilter);
  }
  if (typeFilter !== "all") {
    filtered = filtered.filter(q => q.type === typeFilter);
  }
  
  if (filtered.length === 0) {
    alert("No questions found matching the selected filters. Please choose another combination.");
    return;
  }
  
  // Shuffle and slice
  filtered = [...filtered].sort(() => 0.5 - Math.random());
  
  const limit = countFilter === "all" ? filtered.length : parseInt(countFilter);
  state.activePractice.questions = filtered.slice(0, limit).map(q => {
    return {
      ...q,
      options: [...q.options].sort(() => 0.5 - Math.random())
    };
  });
  state.activePractice.currentIndex = 0;
  state.activePractice.answers = {};
  state.activePractice.submitted = {};
  
  // UI Switch
  document.querySelector(".practice-config").style.display = "none";
  document.getElementById("practice-room").style.display = "grid";
  
  renderPracticeQuestion();
  renderPracticeProgressPanel();
}

function renderPracticeQuestion() {
  const pState = state.activePractice;
  const q = pState.questions[pState.currentIndex];
  
  // Meta
  document.getElementById("question-index-display").textContent = `Question ${pState.currentIndex + 1} of ${pState.questions.length}`;
  document.getElementById("question-category-display").textContent = q.category;
  
  const bookmarkBtn = document.getElementById("bookmark-question-btn");
  bookmarkBtn.className = state.bookmarkedIds.includes(q.id) ? "question-bookmark active" : "question-bookmark";
  
  const flagBtn = document.getElementById("flag-question-btn");
  flagBtn.className = state.flaggedQuestions[q.id] ? "question-flag active" : "question-flag";
  
  // EMQ specific elements
  const emqThemeBanner = document.getElementById("emq-theme-banner");
  if (q.type === "emq" && q.emq_theme) {
    emqThemeBanner.style.display = "block";
    document.getElementById("emq-theme-title").textContent = `Theme: ${q.emq_theme}`;
  } else {
    emqThemeBanner.style.display = "none";
  }
  
  // Scenario
  document.getElementById("question-scenario-display").textContent = q.scenario;
  
  // Options Container
  const container = document.getElementById("question-inputs-container");
  container.innerHTML = "";
  
  const isSubmitted = pState.submitted[pState.currentIndex];
  const explanationPanel = document.getElementById("question-explanation-display");
  explanationPanel.style.display = isSubmitted ? "block" : "none";
  if (isSubmitted) {
    document.getElementById("question-explanation-text").textContent = q.explanation;
  }
  
  // Adjust control buttons
  document.getElementById("prev-question-btn").disabled = pState.currentIndex === 0;
  
  if (isSubmitted) {
    document.getElementById("submit-answer-btn").style.display = "none";
    document.getElementById("next-question-btn").style.display = "block";
    if (pState.currentIndex === pState.questions.length - 1) {
      document.getElementById("next-question-btn").textContent = "Finish Practice Session";
    } else {
      document.getElementById("next-question-btn").innerHTML = 'Next <i class="fa-solid fa-chevron-right"></i>';
    }
  } else {
    document.getElementById("submit-answer-btn").style.display = "block";
    document.getElementById("next-question-btn").style.display = "none";
  }
  
  // Render options inputs according to question type
  if (q.type === "sba" || q.type === "emq") {
    // Single Choice list
    const optionsList = document.createElement("div");
    optionsList.className = "options-list";
    
    q.options.forEach((opt, idx) => {
      const char = String.fromCharCode(65 + idx); // A, B, C...
      const card = document.createElement("div");
      card.className = "option-card";
      
      // Select state
      const userAns = pState.answers[pState.currentIndex];
      if (userAns === opt) card.classList.add("selected");
      
      // Submission validation state styling
      if (isSubmitted) {
        if (opt === q.correct_answer) {
          card.className = "option-card correct";
        } else if (userAns === opt) {
          card.className = "option-card incorrect";
        }
      }
      
      card.innerHTML = `
        <div class="option-badge">${char}</div>
        <div class="option-text">${opt}</div>
      `;
      
      if (!isSubmitted) {
        card.addEventListener("click", () => {
          document.querySelectorAll(".option-card").forEach(c => c.classList.remove("selected"));
          card.classList.add("selected");
          pState.answers[pState.currentIndex] = opt;
        });
      }
      
      optionsList.appendChild(card);
    });
    container.appendChild(optionsList);
    
  } else if (q.type === "ranking") {
    // SJT Drag-and-Drop Ranking list
    const rankingIntro = document.createElement("p");
    rankingIntro.style.cssText = "font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px;";
    rankingIntro.textContent = isSubmitted ? "Result ranking (from top: 1st, 2nd, etc.):" : "Drag and reorder options into your preferred appropriateness rank (1st at the top, last at the bottom):";
    container.appendChild(rankingIntro);
    
    const rankingContainer = document.createElement("div");
    rankingContainer.className = "ranking-container";
    
    // Use user ordered list or default shuffled list
    let currentOrder = pState.answers[pState.currentIndex];
    if (!currentOrder) {
      currentOrder = [...q.options];
      pState.answers[pState.currentIndex] = currentOrder;
    }
    
    currentOrder.forEach((opt, idx) => {
      const item = document.createElement("div");
      item.className = "ranking-item";
      if (!isSubmitted) {
        item.setAttribute("draggable", "true");
      } else {
        // Color items based on position deviation
        const targetPos = q.correct_answer.indexOf(opt);
        const diff = Math.abs(idx - targetPos);
        if (diff === 0) {
          item.style.borderLeft = "6px solid var(--success)";
        } else if (diff <= 1) {
          item.style.borderLeft = "6px solid var(--warning)";
        } else {
          item.style.borderLeft = "6px solid var(--danger)";
        }
      }
      
      item.innerHTML = `
        <div class="ranking-num">${idx + 1}</div>
        <div class="ranking-text" style="flex: 1;">${opt}</div>
        ${!isSubmitted ? '<div style="color: var(--text-tertiary);"><i class="fa-solid fa-grip-vertical"></i></div>' : ''}
      `;
      
      if (!isSubmitted) {
        setupDragAndDropEvents(item, idx, currentOrder, rankingContainer);
      }
      
      rankingContainer.appendChild(item);
    });
    
    container.appendChild(rankingContainer);
    
  } else if (q.type === "selection") {
    // SJT Selection list (select 3 of 8)
    const selectionIntro = document.createElement("p");
    selectionIntro.style.cssText = "font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px;";
    selectionIntro.textContent = "Select exactly THREE choices that combined form the best course of action:";
    container.appendChild(selectionIntro);
    
    const optionsList = document.createElement("div");
    optionsList.className = "options-list";
    
    let userSelections = pState.answers[pState.currentIndex] || [];
    
    q.options.forEach((opt, idx) => {
      const card = document.createElement("div");
      card.className = "option-card";
      
      const char = String.fromCharCode(65 + idx);
      const isSelected = userSelections.includes(opt);
      if (isSelected) card.classList.add("selected");
      
      if (isSubmitted) {
        const isCorrect = q.correct_answer.includes(opt);
        if (isCorrect) {
          card.className = "option-card correct";
        } else if (isSelected) {
          card.className = "option-card incorrect";
        }
      }
      
      card.innerHTML = `
        <div class="option-badge">${char}</div>
        <div style="flex: 1;">${opt}</div>
        <div>
          <input type="checkbox" ${isSelected ? "checked" : ""} ${isSubmitted ? "disabled" : ""} style="width: 18px; height: 18px; cursor: pointer;">
        </div>
      `;
      
      if (!isSubmitted) {
        card.addEventListener("click", (e) => {
          // Prevent multiple trigger on checkbox clicking
          if (e.target.tagName === "INPUT") {
            toggleSelectionOption(opt, card);
            return;
          }
          const checkbox = card.querySelector('input[type="checkbox"]');
          checkbox.checked = !checkbox.checked;
          toggleSelectionOption(opt, card);
        });
      }
      
      optionsList.appendChild(card);
    });
    
    container.appendChild(optionsList);
  }
}

// Drag and drop helper function
function setupDragAndDropEvents(item, index, listArray, containerElement) {
  item.addEventListener("dragstart", () => {
    item.classList.add("dragging");
  });
  
  item.addEventListener("dragend", () => {
    item.classList.remove("dragging");
    // Recalculate options
    const items = [...containerElement.querySelectorAll(".ranking-item")];
    const newOrder = items.map(el => el.querySelector(".ranking-text").textContent);
    state.activePractice.answers[state.activePractice.currentIndex] = newOrder;
    renderPracticeQuestion();
  });
  
  containerElement.addEventListener("dragover", (e) => {
    e.preventDefault();
    const draggingItem = containerElement.querySelector(".dragging");
    const siblings = [...containerElement.querySelectorAll(".ranking-item:not(.dragging)")];
    
    const nextSibling = siblings.find(sibling => {
      return e.clientY <= sibling.getBoundingClientRect().top + sibling.getBoundingClientRect().height / 2;
    });
    
    containerElement.insertBefore(draggingItem, nextSibling);
  });
}

// Checkbox selection helper for 3 of 8 selection SJTs
function toggleSelectionOption(optionText, cardElement) {
  const pState = state.activePractice;
  let selected = pState.answers[pState.currentIndex] || [];
  
  if (selected.includes(optionText)) {
    selected = selected.filter(item => item !== optionText);
    cardElement.classList.remove("selected");
  } else {
    if (selected.length >= 3) {
      alert("You can only select up to 3 options. Deselect another option first.");
      // Uncheck checkbox
      const checkbox = cardElement.querySelector('input[type="checkbox"]');
      if (checkbox) checkbox.checked = false;
      return;
    }
    selected.push(optionText);
    cardElement.classList.add("selected");
  }
  
  pState.answers[pState.currentIndex] = selected;
}

// Render the right navigation dots grid in practice
function renderPracticeProgressPanel() {
  const pState = state.activePractice;
  const grid = document.getElementById("session-nav-grid");
  grid.innerHTML = "";
  
  // Progress Bar
  const progressPercent = Math.round((Object.keys(pState.submitted).length / pState.questions.length) * 100);
  document.getElementById("session-progress-fill").style.width = `${progressPercent}%`;
  
  pState.questions.forEach((q, idx) => {
    const dot = document.createElement("div");
    dot.className = "nav-dot";
    if (idx === pState.currentIndex) dot.classList.add("active");
    
    const isSubmitted = pState.submitted[idx];
    if (isSubmitted) {
      dot.classList.add("answered");
      // Style color according to correct or incorrect
      const accuracy = calculateQuestionAccuracy(q, pState.answers[idx]);
      if (accuracy === 100) {
        dot.style.backgroundColor = "var(--success-light)";
        dot.style.color = "var(--success)";
        dot.style.borderColor = "var(--success)";
      } else if (accuracy > 0) {
        dot.style.backgroundColor = "var(--warning-light)";
        dot.style.color = "var(--warning)";
        dot.style.borderColor = "var(--warning)";
      } else {
        dot.style.backgroundColor = "var(--danger-light)";
        dot.style.color = "var(--danger)";
        dot.style.borderColor = "var(--danger)";
      }
    }
    
    dot.textContent = idx + 1;
    dot.addEventListener("click", () => {
      pState.currentIndex = idx;
      renderPracticeQuestion();
      renderPracticeProgressPanel();
    });
    
    grid.appendChild(dot);
  });
}

// Verify correctness of answer for analytics
function calculateQuestionAccuracy(question, userAns) {
  if (!userAns) return 0;
  
  if (question.type === "sba" || question.type === "emq") {
    return userAns === question.correct_answer ? 100 : 0;
  }
  
  if (question.type === "selection") {
    const correctCount = userAns.filter(opt => question.correct_answer.includes(opt)).length;
    return Math.round((correctCount / 3) * 100); // percentage correct
  }
  
  if (question.type === "ranking") {
    // Check rank match exactly or compute difference
    let totalDelta = 0;
    userAns.forEach((opt, idx) => {
      const correctIdx = question.correct_answer.indexOf(opt);
      totalDelta += Math.abs(idx - correctIdx);
    });
    // Perfect: delta = 0 -> 100%. Max delta is 12 for 5 elements (e.g. 54321 vs 12345).
    // Let's compute a simple accuracy mapping
    const pct = Math.max(0, 100 - (totalDelta * 10));
    return Math.round(pct);
  }
  
  return 0;
}

// Action: Submit Answer in Practice
function submitPracticeAnswer() {
  const pState = state.activePractice;
  const idx = pState.currentIndex;
  const q = pState.questions[idx];
  const ans = pState.answers[idx];
  
  if (!ans || (q.type === "selection" && ans.length !== 3)) {
    alert(q.type === "selection" ? "Please select exactly 3 actions before submitting." : "Please select an answer first.");
    return;
  }
  
  // Submit state
  pState.submitted[idx] = true;
  
  // Save answer to records
  const accuracy = calculateQuestionAccuracy(q, ans);
  const isCorrect = accuracy >= 70; // 70%+ represents a pass/correct threshold
  
  if (!state.answeredQuestionIds.includes(q.id)) {
    state.answeredQuestionIds.push(q.id);
  }
  
  state.questionAttempts[q.id] = {
    attempts: (state.questionAttempts[q.id]?.attempts || 0) + 1,
    correct: isCorrect
  };
  
  saveStateToStorage("answered_question_ids");
  saveStateToStorage("question_attempts");
  
  renderPracticeQuestion();
  renderPracticeProgressPanel();
}

function showNextPracticeQuestion() {
  const pState = state.activePractice;
  if (pState.currentIndex < pState.questions.length - 1) {
    pState.currentIndex++;
    renderPracticeQuestion();
    renderPracticeProgressPanel();
  } else {
    // End practice session
    alert("Practice session completed! Reviewing statistics on Dashboard.");
    endPracticeSession();
  }
}

function showPrevPracticeQuestion() {
  const pState = state.activePractice;
  if (pState.currentIndex > 0) {
    pState.currentIndex--;
    renderPracticeQuestion();
    renderPracticeProgressPanel();
  }
}

function toggleActiveQuestionBookmark() {
  const q = state.activePractice.questions[state.activePractice.currentIndex];
  if (!q) return;
  
  toggleBookmark(q.id);
  renderPracticeQuestion();
}

function toggleBookmark(qId) {
  if (state.bookmarkedIds.includes(qId)) {
    state.bookmarkedIds = state.bookmarkedIds.filter(id => id !== qId);
  } else {
    state.bookmarkedIds.push(qId);
  }
  saveStateToStorage("bookmarked_ids");
}

function endPracticeSession() {
  document.getElementById("practice-room").style.display = "none";
  document.querySelector(".practice-config").style.display = "flex";
  renderDashboard();
}

// --- BOOKMARKS LOGIC ---
function renderBookmarks() {
  const container = document.getElementById("bookmark-list-container");
  container.innerHTML = "";
  
  const currentExamQuestions = state.questions.filter(q => q.exam === state.activeExam);
  const examBookmarks = currentExamQuestions.filter(q => state.bookmarkedIds.includes(q.id));
  
  if (examBookmarks.length === 0) {
    container.innerHTML = '<p style="text-align: center; padding: 40px 0; color: var(--text-tertiary);">No bookmarks saved for this exam. While practicing, click the bookmark icon to save questions here.</p>';
    return;
  }
  
  examBookmarks.forEach((q, idx) => {
    const card = document.createElement("div");
    card.className = "glass-panel";
    card.style.cssText = "display: flex; flex-direction: column; gap: 12px; margin-bottom: 16px;";
    
    // Options text rendering for display
    let optionsText = "";
    if (q.options && q.options.length > 0) {
      optionsText = `<div style="font-size: 0.85rem; color: var(--text-secondary); margin: 6px 0;"><strong>Options:</strong> ${q.options.join(", ")}</div>`;
    }
    
    let answerText = Array.isArray(q.correct_answer) ? q.correct_answer.join(" ➔ ") : q.correct_answer;
    
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="question-category">${q.category} (${q.type.toUpperCase()})</span>
        <button class="btn btn-secondary btn-danger btn-sm remove-bookmark-btn" data-id="${q.id}" style="padding: 4px 8px; font-size: 0.8rem;">
          <i class="fa-solid fa-trash-can"></i> Remove
        </button>
      </div>
      <div style="font-weight: 600; line-height: 1.5; color: var(--text-primary);">${q.scenario}</div>
      ${optionsText}
      <div style="font-size: 0.9rem; color: var(--success); font-weight: 600;">
        <i class="fa-solid fa-circle-check"></i> Correct Answer: ${answerText}
      </div>
      <div style="font-size: 0.85rem; background-color: var(--bg-tertiary); padding: 10px 14px; border-radius: var(--border-radius-sm); border-left: 3px solid var(--primary);">
        <strong>Explanation:</strong> ${q.explanation}
      </div>
    `;
    
    card.querySelector(".remove-bookmark-btn").addEventListener("click", () => {
      toggleBookmark(q.id);
      renderBookmarks();
    });
    
    container.appendChild(card);
  });
}

// --- EXAM SIMULATION (MOCKS) ---
function startExamSimulation() {
  const mode = document.getElementById("exam-mode-select").value;
  const currentExamQuestions = state.questions.filter(q => q.exam === state.activeExam);
  
  let examQuestions = [];
  let durationMins = 0;
  
  if (mode === "pd") {
    // Professional Dilemma Mock: load ranking and selection questions
    examQuestions = currentExamQuestions.filter(q => q.type === "ranking" || q.type === "selection");
    durationMins = 95;
  } else if (mode === "cps") {
    // Clinical Problem Solving Mock: load sba and emq questions
    examQuestions = currentExamQuestions.filter(q => q.type === "sba" || q.type === "emq");
    durationMins = 75;
  } else {
    // Full combined mock
    examQuestions = [...currentExamQuestions];
    durationMins = 170;
  }
  
  if (examQuestions.length === 0) {
    alert("No questions available in database to simulate this sub-paper. Load more questions first.");
    return;
  }
  
  // Shuffle questions for simulation
  examQuestions = [...examQuestions].sort(() => 0.5 - Math.random());
  
  // Cap questions to match actual numbers if database size permits, else use all
  const qCap = mode === "pd" ? 50 : (mode === "cps" ? 97 : 147);
  state.activeExamSim.questions = examQuestions.slice(0, qCap).map(q => {
    return {
      ...q,
      options: [...q.options].sort(() => 0.5 - Math.random())
    };
  });
  state.activeExamSim.mode = mode;
  state.activeExamSim.currentIndex = 0;
  state.activeExamSim.answers = {};
  state.activeExamSim.secondsRemaining = durationMins * 60;
  state.activeExamSim.totalSeconds = durationMins * 60;
  state.activeExamSim.startTime = new Date();
  
  // UI Switch
  document.getElementById("exam-intro-screen").style.display = "none";
  document.getElementById("exam-simulation-screen").style.display = "grid";
  
  // Start Timer
  startExamSimTimer();
  renderSimQuestion();
  renderSimProgressPanel();
}

function startExamSimTimer() {
  if (state.activeExamSim.timer) clearInterval(state.activeExamSim.timer);
  
  const timerVal = document.getElementById("sim-timer-value");
  const timerBox = document.getElementById("sim-timer-display");
  timerBox.classList.remove("warning");
  
  state.activeExamSim.timer = setInterval(() => {
    state.activeExamSim.secondsRemaining--;
    
    const minutes = Math.floor(state.activeExamSim.secondsRemaining / 60);
    const seconds = state.activeExamSim.secondsRemaining % 60;
    
    timerVal.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    
    // Warning at 5 minutes
    if (state.activeExamSim.secondsRemaining <= 300) {
      timerBox.classList.add("warning");
    }
    
    if (state.activeExamSim.secondsRemaining <= 0) {
      clearInterval(state.activeExamSim.timer);
      alert("Time is up! Your exam simulation will be submitted automatically.");
      submitExamSimulation();
    }
  }, 1000);
}

function renderSimQuestion() {
  const sim = state.activeExamSim;
  const q = sim.questions[sim.currentIndex];
  
  document.getElementById("sim-question-index-display").textContent = `Question ${sim.currentIndex + 1} of ${sim.questions.length}`;
  document.getElementById("sim-question-category-display").textContent = q.category;
  
  // Bookmark button
  const bookmarkBtn = document.getElementById("sim-bookmark-question-btn");
  bookmarkBtn.className = state.bookmarkedIds.includes(q.id) ? "question-bookmark active" : "question-bookmark";
  
  const flagBtn = document.getElementById("sim-flag-question-btn");
  flagBtn.className = state.flaggedQuestions[q.id] ? "question-flag active" : "question-flag";
  
  // EMQ
  const emqThemeBanner = document.getElementById("sim-emq-theme-banner");
  if (q.type === "emq" && q.emq_theme) {
    emqThemeBanner.style.display = "block";
    document.getElementById("sim-emq-theme-title").textContent = `Theme: ${q.emq_theme}`;
  } else {
    emqThemeBanner.style.display = "none";
  }
  
  document.getElementById("sim-question-scenario-display").textContent = q.scenario;
  
  const container = document.getElementById("sim-question-inputs-container");
  container.innerHTML = "";
  
  document.getElementById("sim-prev-question-btn").disabled = sim.currentIndex === 0;
  
  if (sim.currentIndex === sim.questions.length - 1) {
    document.getElementById("sim-next-question-btn").textContent = "Review & Submit";
  } else {
    document.getElementById("sim-next-question-btn").innerHTML = 'Next Question <i class="fa-solid fa-chevron-right"></i>';
  }
  
  // Inputs per type (No correct/incorrect feedback shown during exam)
  if (q.type === "sba" || q.type === "emq") {
    const optionsList = document.createElement("div");
    optionsList.className = "options-list";
    
    q.options.forEach((opt, idx) => {
      const card = document.createElement("div");
      card.className = "option-card";
      
      const char = String.fromCharCode(65 + idx);
      const userAns = sim.answers[sim.currentIndex];
      if (userAns === opt) card.classList.add("selected");
      
      card.innerHTML = `
        <div class="option-badge">${char}</div>
        <div class="option-text">${opt}</div>
      `;
      
      card.addEventListener("click", () => {
        document.querySelectorAll(".option-card").forEach(c => c.classList.remove("selected"));
        card.classList.add("selected");
        sim.answers[sim.currentIndex] = opt;
        renderSimProgressPanel();
      });
      
      optionsList.appendChild(card);
    });
    container.appendChild(optionsList);
    
  } else if (q.type === "ranking") {
    const rankingIntro = document.createElement("p");
    rankingIntro.style.cssText = "font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px;";
    rankingIntro.textContent = "Drag and reorder options (1st at the top, last at the bottom):";
    container.appendChild(rankingIntro);
    
    const rankingContainer = document.createElement("div");
    rankingContainer.className = "ranking-container";
    
    let currentOrder = sim.answers[sim.currentIndex];
    if (!currentOrder) {
      currentOrder = [...q.options];
      sim.answers[sim.currentIndex] = currentOrder;
    }
    
    currentOrder.forEach((opt, idx) => {
      const item = document.createElement("div");
      item.className = "ranking-item";
      item.setAttribute("draggable", "true");
      
      item.innerHTML = `
        <div class="ranking-num">${idx + 1}</div>
        <div class="ranking-text" style="flex: 1;">${opt}</div>
        <div style="color: var(--text-tertiary);"><i class="fa-solid fa-grip-vertical"></i></div>
      `;
      
      // Setup drag events
      item.addEventListener("dragstart", () => item.classList.add("dragging"));
      item.addEventListener("dragend", () => {
        item.classList.remove("dragging");
        const items = [...rankingContainer.querySelectorAll(".ranking-item")];
        const newOrder = items.map(el => el.querySelector(".ranking-text").textContent);
        sim.answers[sim.currentIndex] = newOrder;
        renderSimQuestion();
        renderSimProgressPanel();
      });
      
      rankingContainer.addEventListener("dragover", (e) => {
        e.preventDefault();
        const draggingItem = rankingContainer.querySelector(".dragging");
        const siblings = [...rankingContainer.querySelectorAll(".ranking-item:not(.dragging)")];
        const nextSibling = siblings.find(sibling => e.clientY <= sibling.getBoundingClientRect().top + sibling.getBoundingClientRect().height / 2);
        rankingContainer.insertBefore(draggingItem, nextSibling);
      });
      
      rankingContainer.appendChild(item);
    });
    container.appendChild(rankingContainer);
    
  } else if (q.type === "selection") {
    const selectionIntro = document.createElement("p");
    selectionIntro.style.cssText = "font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px;";
    selectionIntro.textContent = "Select exactly THREE choices:";
    container.appendChild(selectionIntro);
    
    const optionsList = document.createElement("div");
    optionsList.className = "options-list";
    
    let userSelections = sim.answers[sim.currentIndex] || [];
    
    q.options.forEach((opt, idx) => {
      const card = document.createElement("div");
      card.className = "option-card";
      
      const char = String.fromCharCode(65 + idx);
      const isSelected = userSelections.includes(opt);
      if (isSelected) card.classList.add("selected");
      
      card.innerHTML = `
        <div class="option-badge">${char}</div>
        <div style="flex: 1;">${opt}</div>
        <div>
          <input type="checkbox" ${isSelected ? "checked" : ""} style="width: 18px; height: 18px; cursor: pointer;">
        </div>
      `;
      
      const selectHandler = (e) => {
        if (e.target.tagName === "INPUT") {
          toggleSimSelectionOption(opt, card);
          return;
        }
        const checkbox = card.querySelector('input[type="checkbox"]');
        checkbox.checked = !checkbox.checked;
        toggleSimSelectionOption(opt, card);
      };
      
      card.addEventListener("click", selectHandler);
      optionsList.appendChild(card);
    });
    container.appendChild(optionsList);
  }
}

function toggleSimSelectionOption(optionText, cardElement) {
  const sim = state.activeExamSim;
  let selected = sim.answers[sim.currentIndex] || [];
  
  if (selected.includes(optionText)) {
    selected = selected.filter(item => item !== optionText);
    cardElement.classList.remove("selected");
  } else {
    if (selected.length >= 3) {
      alert("You can only select up to 3 options. Deselect another first.");
      const checkbox = cardElement.querySelector('input[type="checkbox"]');
      if (checkbox) checkbox.checked = false;
      return;
    }
    selected.push(optionText);
    cardElement.classList.add("selected");
  }
  
  sim.answers[sim.currentIndex] = selected;
  renderSimProgressPanel();
}

function renderSimProgressPanel() {
  const sim = state.activeExamSim;
  const grid = document.getElementById("sim-nav-grid");
  grid.innerHTML = "";
  
  const answeredCount = Object.keys(sim.answers).filter(idx => {
    const q = sim.questions[idx];
    const ans = sim.answers[idx];
    if (q.type === "selection") return ans && ans.length === 3;
    return ans !== undefined;
  }).length;
  
  const progressPercent = Math.round((answeredCount / sim.questions.length) * 100);
  document.getElementById("sim-progress-fill").style.width = `${progressPercent}%`;
  
  sim.questions.forEach((q, idx) => {
    const dot = document.createElement("div");
    dot.className = "nav-dot";
    if (idx === sim.currentIndex) dot.classList.add("active");
    
    // Checked if answered
    const ans = sim.answers[idx];
    const isAnswered = q.type === "selection" ? (ans && ans.length === 3) : (ans !== undefined);
    if (isAnswered) {
      dot.classList.add("answered");
    }
    
    dot.textContent = idx + 1;
    dot.addEventListener("click", () => {
      sim.currentIndex = idx;
      renderSimQuestion();
      renderSimProgressPanel();
    });
    
    grid.appendChild(dot);
  });
}

function showNextSimQuestion() {
  const sim = state.activeExamSim;
  if (sim.currentIndex < sim.questions.length - 1) {
    sim.currentIndex++;
    renderSimQuestion();
    renderSimProgressPanel();
  } else {
    confirmSubmitExamSim();
  }
}

function showPrevSimQuestion() {
  const sim = state.activeExamSim;
  if (sim.currentIndex > 0) {
    sim.currentIndex--;
    renderSimQuestion();
    renderSimProgressPanel();
  }
}

function toggleSimQuestionBookmark() {
  const q = state.activeExamSim.questions[state.activeExamSim.currentIndex];
  if (!q) return;
  
  toggleBookmark(q.id);
  renderSimQuestion();
}

function confirmSubmitExamSim() {
  const sim = state.activeExamSim;
  const total = sim.questions.length;
  
  const answered = Object.keys(sim.answers).filter(idx => {
    const q = sim.questions[idx];
    const ans = sim.answers[idx];
    if (q.type === "selection") return ans && ans.length === 3;
    return ans !== undefined;
  }).length;
  
  const unanswered = total - answered;
  
  let msg = "Are you sure you want to submit your exam?";
  if (unanswered > 0) {
    msg += ` You have ${unanswered} unanswered questions left.`;
  }
  
  if (confirm(msg)) {
    submitExamSimulation();
  }
}

function abandonExamSim() {
  if (confirm("Are you sure you want to abandon this exam simulator session? All progress for this mock will be discarded.")) {
    clearInterval(state.activeExamSim.timer);
    document.getElementById("exam-simulation-screen").style.display = "none";
    document.getElementById("exam-intro-screen").style.display = "flex";
  }
}

// Main scoring engine for sub-papers
function submitExamSimulation() {
  const sim = state.activeExamSim;
  clearInterval(sim.timer);
  
  let earnedScore = 0;
  let maxScore = 0;
  
  // Category score breakdowns
  const categoryBreakdown = {};
  
  sim.questions.forEach((q, idx) => {
    const userAns = sim.answers[idx];
    let score = 0;
    let maxVal = 0;
    
    if (q.type === "sba" || q.type === "emq") {
      maxVal = 1;
      score = userAns === q.correct_answer ? 1 : 0;
      
    } else if (q.type === "selection") {
      // Selection (3 of 8): 1 point max. 1/3 point per correct match.
      maxVal = 1;
      if (userAns && Array.isArray(userAns)) {
        const matches = userAns.filter(opt => q.correct_answer.includes(opt)).length;
        score = matches / 3;
      }
      
    } else if (q.type === "ranking") {
      // Professional Dilemma UK SJT scoring. Max 20 points per scenario (5 items).
      // Each item is scored: 4 - (distance from model answer position)
      maxVal = 20;
      if (userAns && Array.isArray(userAns)) {
        userAns.forEach((opt, pos) => {
          const modelPos = q.correct_answer.indexOf(opt);
          const distance = Math.abs(pos - modelPos);
          score += Math.max(0, 4 - distance);
        });
      }
    }
    
    // Accumulate total scores
    earnedScore += score;
    maxScore += maxVal;
    
    // Accumulate category statistics
    if (!categoryBreakdown[q.category]) {
      categoryBreakdown[q.category] = { earned: 0, max: 0 };
    }
    categoryBreakdown[q.category].earned += score;
    categoryBreakdown[q.category].max += maxVal;
    
    // Save attempts in global tracking stats
    const isPass = maxVal > 0 && (score / maxVal) >= 0.7;
    if (!state.answeredQuestionIds.includes(q.id)) {
      state.answeredQuestionIds.push(q.id);
    }
    state.questionAttempts[q.id] = {
      attempts: (state.questionAttempts[q.id]?.attempts || 0) + 1,
      correct: isPass
    };
  });
  
  saveStateToStorage("answered_question_ids");
  saveStateToStorage("question_attempts");
  
  // Calculate results metadata
  const overallPercent = Math.round((earnedScore / (maxScore || 1)) * 100);
  const timeTakenSecs = sim.totalSeconds - sim.secondsRemaining;
  const mins = Math.floor(timeTakenSecs / 60);
  const secs = timeTakenSecs % 60;
  const timeStr = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  
  // Save to history
  const record = {
    date: new Date().toLocaleDateString(),
    mode: sim.mode,
    score: overallPercent,
    time: timeStr
  };
  state.mockHistory.push(record);
  saveStateToStorage("mock_history");
  
  // Update Results Screen UI
  document.getElementById("result-score-percent").textContent = `${overallPercent}%`;
  
  const answeredCount = Object.keys(sim.answers).filter(idx => {
    const q = sim.questions[idx];
    const ans = sim.answers[idx];
    if (q.type === "selection") return ans && ans.length === 3;
    return ans !== undefined;
  }).length;
  document.getElementById("result-answered-ratio").textContent = `${answeredCount} / ${sim.questions.length}`;
  document.getElementById("result-time-taken").textContent = timeStr;
  
  const breakdownDiv = document.getElementById("exam-score-breakdown");
  breakdownDiv.innerHTML = '<h3 style="font-size: 1rem; margin-bottom: 12px;">Score Breakdown by Category</h3>';
  
  Object.keys(categoryBreakdown).forEach(cat => {
    const data = categoryBreakdown[cat];
    const accuracy = Math.round((data.earned / (data.max || 1)) * 100);
    const progressEl = document.createElement("div");
    progressEl.style.cssText = "margin-bottom: 14px;";
    progressEl.innerHTML = `
      <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 600; margin-bottom: 4px;">
        <span>${cat}</span>
        <span>${accuracy}% (${Math.round(data.earned * 10) / 10} / ${data.max} pts)</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: ${accuracy}%;"></div>
      </div>
    `;
    breakdownDiv.appendChild(progressEl);
  });
  
  // UI Switch
  document.getElementById("exam-simulation-screen").style.display = "none";
  document.getElementById("exam-results-screen").style.display = "flex";
}

// --- QUESTION CREATOR WIZARD ---
function setupCreatorFormOptions() {
  const type = document.getElementById("creator-type").value;
  const container = document.getElementById("creator-options-container");
  container.innerHTML = "";
  
  const addBtn = document.getElementById("creator-add-option-btn");
  const themeGroup = document.getElementById("creator-theme-group");
  themeGroup.style.display = "none"; // Emqs not supported in basic form yet
  
  if (type === "sba") {
    addBtn.style.display = "block";
    container.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-weight: 600; font-size: 0.9rem;">Option Text</span>
        <span style="font-weight: 600; font-size: 0.9rem; margin-right: 10px;">Is Correct?</span>
      </div>
    `;
    // Spawn 5 default option rows
    for (let i = 0; i < 5; i++) {
      addNewCreatorOptionRow("sba", i === 0);
    }
  } else if (type === "selection") {
    addBtn.style.display = "block";
    container.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-weight: 600; font-size: 0.9rem;">Option Text (provide 8 choices)</span>
        <span style="font-weight: 600; font-size: 0.9rem; margin-right: 10px;">Select exactly 3</span>
      </div>
    `;
    for (let i = 0; i < 8; i++) {
      addNewCreatorOptionRow("selection", i < 3);
    }
  } else if (type === "ranking") {
    // For ranking, correct answer is defined by the top-to-bottom order of options
    addBtn.style.display = "block";
    container.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-weight: 600; font-size: 0.9rem;">Arrange options in correct ranking order (from 1st to last):</span>
      </div>
    `;
    for (let i = 0; i < 5; i++) {
      addNewCreatorOptionRow("ranking");
    }
  }
}

function addNewCreatorOptionRow(typeOverride, shouldCheck = false) {
  const type = typeOverride || document.getElementById("creator-type").value;
  const container = document.getElementById("creator-options-container");
  
  const rowCount = container.querySelectorAll(".option-builder-row").length;
  const row = document.createElement("div");
  row.className = "option-builder-row";
  
  let inputType = "radio";
  if (type === "selection") inputType = "checkbox";
  
  if (type === "sba" || type === "selection") {
    row.innerHTML = `
      <input type="text" class="form-control option-text-input" placeholder="Option text..." required style="flex: 1;">
      <input type="${inputType}" name="creator-correct-selector" class="correct-marker-input" ${shouldCheck ? "checked" : ""} style="margin-left: 20px;">
    `;
  } else if (type === "ranking") {
    row.innerHTML = `
      <span style="font-weight: 700; color: var(--primary);">${rowCount + 1}.</span>
      <input type="text" class="form-control option-text-input" placeholder="Ranked option text..." required style="flex: 1;">
    `;
  }
  
  container.appendChild(row);
}

function clearCreatorForm() {
  document.getElementById("question-creator-form").reset();
  setupCreatorFormOptions();
}

function saveCreatedQuestion(e) {
  e.preventDefault();
  
  const exam = document.getElementById("creator-exam-name").value.trim().toUpperCase();
  const category = document.getElementById("creator-category").value.trim();
  const type = document.getElementById("creator-type").value;
  const scenario = document.getElementById("creator-scenario").value.trim();
  const explanation = document.getElementById("creator-explanation").value.trim();
  
  const optionRows = document.querySelectorAll(".option-builder-row");
  const options = [];
  let correct_answer = null;
  
  if (type === "sba") {
    let correctIndex = -1;
    optionRows.forEach((row, idx) => {
      const text = row.querySelector(".option-text-input").value.trim();
      options.push(text);
      if (row.querySelector(".correct-marker-input").checked) correctIndex = idx;
    });
    
    if (correctIndex === -1) {
      alert("Please mark one option as the correct answer.");
      return;
    }
    correct_answer = options[correctIndex];
    
  } else if (type === "selection") {
    const selectedOptions = [];
    optionRows.forEach(row => {
      const text = row.querySelector(".option-text-input").value.trim();
      options.push(text);
      if (row.querySelector(".correct-marker-input").checked) {
        selectedOptions.push(text);
      }
    });
    
    if (selectedOptions.length !== 3) {
      alert("Please select exactly 3 options as correct answers.");
      return;
    }
    correct_answer = selectedOptions;
    
  } else if (type === "ranking") {
    optionRows.forEach(row => {
      const text = row.querySelector(".option-text-input").value.trim();
      options.push(text);
    });
    // For ranking, correct order is the order defined in the options
    correct_answer = [...options];
    
    // Shuffled version for options display
    options.sort(() => 0.5 - Math.random());
  }

  const editingId = document.getElementById("creator-editing-id").value;
  
  if (editingId) {
    // Update existing question
    const updatedQuestion = {
      id: editingId,
      exam,
      type,
      category,
      scenario,
      options,
      correct_answer,
      explanation
    };
    
    // Check if it's in customQuestions
    const customIdx = state.customQuestions.findIndex(q => q.id === editingId);
    if (customIdx > -1) {
      state.customQuestions[customIdx] = updatedQuestion;
      saveStateToStorage("custom_questions");
    } else {
      // It's a base question from questions.json! Save custom overrides in LocalStorage.
      state.customQuestions.push(updatedQuestion);
      saveStateToStorage("custom_questions");
    }
    
    // Clear flag if editing a flagged question
    if (state.flaggedQuestions[editingId]) {
      delete state.flaggedQuestions[editingId];
      saveStateToStorage("flagged_questions");
    }
    
    alert(`Successfully updated question ${editingId}!`);
    document.getElementById("creator-editing-id").value = "";
    document.getElementById("creator-panel-title").textContent = "Create New Practice Question";
    document.getElementById("creator-submit-btn").innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Save Question to Database';
  } else {
    // Save new question
    const newQuestion = {
      id: `q_custom_${Date.now()}`,
      exam,
      type,
      category,
      scenario,
      options,
      correct_answer,
      explanation
    };
    
    state.customQuestions.push(newQuestion);
    saveStateToStorage("custom_questions");
    alert(`Successfully added question to database for ${exam}!`);
  }
  
  // Reload database
  loadQuestionsDatabase();
  clearCreatorForm();
  document.getElementById("tab-dashboard").click();
}

// --- USER FLAGGING SYSTEM ---
function toggleActiveQuestionFlag() {
  const pState = state.activePractice;
  const q = pState.questions[pState.currentIndex];
  if (!q) return;
  toggleFlag(q.id);
  renderPracticeQuestion();
}

function toggleSimQuestionFlag() {
  const sim = state.activeExamSim;
  const q = sim.questions[sim.currentIndex];
  if (!q) return;
  toggleFlag(q.id);
  renderSimQuestion();
}

function toggleFlag(qId) {
  if (state.flaggedQuestions[qId]) {
    // Already flagged, resolve/remove flag
    delete state.flaggedQuestions[qId];
    alert("Question unflagged.");
  } else {
    // Prompt for flagging reason
    const reason = prompt("Please describe the issue with this question (e.g. spelling error, incorrect answer, confusing explanation):");
    if (reason === null) return; // User cancelled
    state.flaggedQuestions[qId] = reason.trim() || "Flagged for review (no reason provided).";
    alert("Question flagged for admin review. Thank you!");
  }
  saveStateToStorage("flagged_questions");
  updateAdminFlaggedBadge();
}

function updateAdminFlaggedBadge() {
  const flaggedCount = Object.keys(state.flaggedQuestions).length;
  const badge = document.getElementById("admin-flagged-badge");
  if (badge) badge.textContent = flaggedCount;
}

// --- ADMIN PORTAL SUB-TABS & NAV ---
function setupAdminTabPanelNavigation() {
  const subTabs = document.querySelectorAll(".admin-sub-tabs button");
  subTabs.forEach(btn => {
    // Clean and replace listener
    const newBtn = btn.cloneNode(true);
    btn.parentNode.replaceChild(newBtn, btn);
  });
  
  const freshSubTabs = document.querySelectorAll(".admin-sub-tabs button");
  freshSubTabs.forEach(btn => {
    btn.addEventListener("click", () => {
      freshSubTabs.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      
      const targetSectionId = btn.getAttribute("data-admin-tab");
      document.querySelectorAll(".admin-tab-panel").forEach(panel => {
        panel.style.display = "none";
      });
      document.getElementById(targetSectionId).style.display = "block";
      
      if (targetSectionId === "admin-manage-section") renderAdminManageQuestionsList();
      if (targetSectionId === "admin-flagged-section") renderAdminFlaggedQuestionsList();
    });
  });
  
  // Search and filter listeners
  const searchInput = document.getElementById("admin-search-input");
  const catFilter = document.getElementById("admin-category-filter");
  const typeFilter = document.getElementById("admin-type-filter");
  
  searchInput.oninput = renderAdminManageQuestionsList;
  catFilter.onchange = renderAdminManageQuestionsList;
  typeFilter.onchange = renderAdminManageQuestionsList;
  
  updateAdminFlaggedBadge();
}

function populateAdminFilters() {
  const catFilter = document.getElementById("admin-category-filter");
  if (!catFilter) return;
  
  const currentExamQuestions = state.questions.filter(q => q.exam === state.activeExam);
  const categories = [...new Set(currentExamQuestions.map(q => q.category))];
  
  catFilter.innerHTML = '<option value="all">All Categories</option>';
  categories.forEach(cat => {
    const option = document.createElement("option");
    option.value = cat;
    option.textContent = cat;
    catFilter.appendChild(option);
  });
}

// --- ADMIN QUESTION INVENTORY MANAGER ---
function renderAdminManageQuestionsList() {
  const container = document.getElementById("admin-questions-list-container");
  if (!container) return;
  
  container.innerHTML = "";
  
  const query = document.getElementById("admin-search-input").value.toLowerCase();
  const catVal = document.getElementById("admin-category-filter").value;
  const typeVal = document.getElementById("admin-type-filter").value;
  
  let filtered = state.questions.filter(q => q.exam === state.activeExam);
  
  if (catVal !== "all") filtered = filtered.filter(q => q.category === catVal);
  if (typeVal !== "all") filtered = filtered.filter(q => q.type === typeVal);
  
  if (query) {
    filtered = filtered.filter(q => 
      q.scenario.toLowerCase().includes(query) || 
      q.explanation.toLowerCase().includes(query) ||
      q.id.toLowerCase().includes(query)
    );
  }
  
  if (filtered.length === 0) {
    container.innerHTML = '<p style="text-align: center; padding: 40px 0; color: var(--text-tertiary);">No questions match the current filters.</p>';
    return;
  }
  
  // Render list (latest first)
  const sorted = [...filtered].reverse();
  
  sorted.forEach(q => {
    const card = document.createElement("div");
    card.className = "admin-question-card";
    
    const isCustom = q.id.startsWith("q_custom_");
    const badgeText = isCustom ? "Custom" : "Base";
    
    card.innerHTML = `
      <div class="admin-question-card-header">
        <div style="flex: 1;">
          <div class="admin-question-info" style="margin-bottom: 6px;">
            <span class="admin-question-badge" style="background-color: var(--primary-light); color: var(--primary);">${q.id}</span>
            <span class="admin-question-badge">${q.category}</span>
            <span class="admin-question-badge" style="text-transform: uppercase;">${q.type}</span>
            <span class="admin-question-badge" style="background-color: var(--success-light); color: var(--success);">${badgeText}</span>
          </div>
          <div class="admin-question-text">${q.scenario}</div>
        </div>
        <div class="admin-question-actions">
          <button class="btn btn-secondary btn-sm edit-q-btn" data-id="${q.id}" style="padding: 6px 12px; font-size: 0.8rem;">
            <i class="fa-solid fa-pen"></i> Edit
          </button>
          <button class="btn btn-secondary btn-danger btn-sm delete-q-btn" data-id="${q.id}" style="padding: 6px 12px; font-size: 0.8rem;">
            <i class="fa-solid fa-trash-can"></i> Delete
          </button>
        </div>
      </div>
    `;
    
    card.querySelector(".edit-q-btn").addEventListener("click", () => editQuestion(q.id));
    card.querySelector(".delete-q-btn").addEventListener("click", () => deleteQuestion(q.id));
    
    container.appendChild(card);
  });
}

// --- ADMIN FLAGGED SCENARIOS REVIEW ---
function renderAdminFlaggedQuestionsList() {
  const container = document.getElementById("admin-flagged-list-container");
  if (!container) return;
  
  container.innerHTML = "";
  
  const flaggedIds = Object.keys(state.flaggedQuestions);
  
  if (flaggedIds.length === 0) {
    container.innerHTML = '<p style="text-align: center; padding: 40px 0; color: var(--text-tertiary);">No flagged questions currently reported by users.</p>';
    return;
  }
  
  flaggedIds.forEach(id => {
    const q = state.questions.find(item => item.id === id);
    if (!q) return; // In case question was deleted
    
    const reason = state.flaggedQuestions[id];
    const card = document.createElement("div");
    card.className = "admin-flagged-card";
    
    card.innerHTML = `
      <div class="admin-question-card-header">
        <div style="flex: 1;">
          <div class="admin-question-info" style="margin-bottom: 6px;">
            <span class="admin-question-badge" style="background-color: var(--warning-light); color: #b45309; border-color: rgba(245,158,11,0.2);">${q.id}</span>
            <span class="admin-question-badge">${q.category}</span>
            <span class="admin-question-badge" style="text-transform: uppercase;">${q.type}</span>
          </div>
          <div style="font-weight: 600; line-height: 1.5; color: var(--text-primary); margin-bottom: 8px;">${q.scenario}</div>
          
          <div class="flagged-reason-box">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <div><strong>Flag Reason:</strong> ${reason}</div>
          </div>
        </div>
        
        <div class="admin-question-actions" style="flex-direction: column;">
          <button class="btn btn-secondary btn-sm resolve-flag-btn" data-id="${q.id}" style="padding: 6px 12px; font-size: 0.8rem; background-color: var(--success-light); color: var(--success); border-color: var(--success);">
            <i class="fa-solid fa-circle-check"></i> Resolve Flag
          </button>
          <button class="btn btn-secondary btn-sm edit-flagged-q-btn" data-id="${q.id}" style="padding: 6px 12px; font-size: 0.8rem;">
            <i class="fa-solid fa-pen"></i> Edit Question
          </button>
          <button class="btn btn-secondary btn-danger btn-sm delete-flagged-q-btn" data-id="${q.id}" style="padding: 6px 12px; font-size: 0.8rem;">
            <i class="fa-solid fa-trash-can"></i> Delete
          </button>
        </div>
      </div>
    `;
    
    card.querySelector(".resolve-flag-btn").addEventListener("click", () => resolveFlag(q.id));
    card.querySelector(".edit-flagged-q-btn").addEventListener("click", () => editQuestion(q.id));
    card.querySelector(".delete-flagged-q-btn").addEventListener("click", () => deleteQuestion(q.id));
    
    container.appendChild(card);
  });
}

function resolveFlag(qId) {
  if (state.flaggedQuestions[qId]) {
    delete state.flaggedQuestions[qId];
    saveStateToStorage("flagged_questions");
    updateAdminFlaggedBadge();
    renderAdminFlaggedQuestionsList();
    alert(`Resolved flag for question ${qId}.`);
  }
}

// Delete question completely from database
function deleteQuestion(qId) {
  if (!confirm(`Are you sure you want to delete question ${qId}? This will remove it from the active question bank.`)) {
    return;
  }
  
  // Remove from customQuestions
  state.customQuestions = state.customQuestions.filter(q => q.id !== qId);
  saveStateToStorage("custom_questions");
  
  // Exclusions track for base questions
  let deletedBaseIds = JSON.parse(localStorage.getItem("deleted_base_ids")) || [];
  if (!qId.startsWith("q_custom_") && !deletedBaseIds.includes(qId)) {
    deletedBaseIds.push(qId);
    localStorage.setItem("deleted_base_ids", JSON.stringify(deletedBaseIds));
  }
  
  // If flagged, clear flag
  if (state.flaggedQuestions[qId]) {
    delete state.flaggedQuestions[qId];
    saveStateToStorage("flagged_questions");
  }
  
  // Reload database
  loadQuestionsDatabase();
  
  // Refresh lists
  renderAdminManageQuestionsList();
  renderAdminFlaggedQuestionsList();
  updateAdminFlaggedBadge();
  renderDashboard();
  
  alert(`Question ${qId} deleted successfully! Click 'Export Current Database' on the Dashboard if you want to download the updated JSON file.`);
}

// Edit Question - Pre-fills the form and focuses it
function editQuestion(qId) {
  const q = state.questions.find(item => item.id === qId);
  if (!q) return;
  
  // Click the Admin Panel tab
  const adminTabBtn = document.getElementById("tab-admin");
  if (adminTabBtn) adminTabBtn.click();
  
  // Switch to "Add Question" sub-tab in Admin Panel
  const createSubTabBtn = document.querySelector('[data-admin-tab="admin-create-section"]');
  if (createSubTabBtn) createSubTabBtn.click();
  
  // Pre-fill Form fields
  document.getElementById("creator-editing-id").value = q.id;
  document.getElementById("creator-exam-name").value = q.exam;
  document.getElementById("creator-category").value = q.category;
  document.getElementById("creator-type").value = q.type;
  document.getElementById("creator-scenario").value = q.scenario;
  document.getElementById("creator-explanation").value = q.explanation;
  
  // Configure options builder
  setupCreatorFormOptions();
  
  // Pre-fill Options
  const container = document.getElementById("creator-options-container");
  const textInputs = container.querySelectorAll(".option-text-input");
  const markers = container.querySelectorAll(".correct-marker-input");
  
  if (q.type === "sba") {
    while (q.options.length > textInputs.length) {
      addNewCreatorOptionRow("sba");
    }
    const freshInputs = container.querySelectorAll(".option-text-input");
    const freshMarkers = container.querySelectorAll(".correct-marker-input");
    
    q.options.forEach((opt, idx) => {
      freshInputs[idx].value = opt;
      freshMarkers[idx].checked = (opt === q.correct_answer);
    });
  } else if (q.type === "selection") {
    while (q.options.length > textInputs.length) {
      addNewCreatorOptionRow("selection");
    }
    const freshInputs = container.querySelectorAll(".option-text-input");
    const freshMarkers = container.querySelectorAll(".correct-marker-input");
    
    q.options.forEach((opt, idx) => {
      freshInputs[idx].value = opt;
      freshMarkers[idx].checked = q.correct_answer.includes(opt);
    });
  } else if (q.type === "ranking") {
    while (q.correct_answer.length > textInputs.length) {
      addNewCreatorOptionRow("ranking");
    }
    const freshInputs = container.querySelectorAll(".option-text-input");
    q.correct_answer.forEach((opt, idx) => {
      freshInputs[idx].value = opt;
    });
  }
  
  // Change form header and submit button
  document.getElementById("creator-panel-title").textContent = `Editing Question ${qId}`;
  document.getElementById("creator-submit-btn").innerHTML = '<i class="fa-solid fa-circle-check"></i> Update Question Details';
  
  // Scroll to form
  document.getElementById("admin-panel").scrollIntoView({ behavior: "smooth" });
}
