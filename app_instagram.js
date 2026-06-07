/**
 * Instagram Carousel Generator Module
 * Generates beautiful 3-slide carousel images from any question in the bank.
 * Exports high-resolution PNGs via html2canvas.
 */

// --- Instagram Generator State ---
const instaState = {
  activeQuestion: null,
  activeSlideIndex: 0, // 0, 1, 2
  theme: "indigo-dusk",
  font: "Outfit",
  handle: "@medbank.studio",
  showLogo: true,
  ctaText: "Save this post for later!",
  ratio: "1-1", // "1-1" or "4-5"
  scenarioFontSize: 26,
  optionsFontSize: 20,
  explanationFontSize: 18,
};

// Theme Definitions
const INSTA_THEMES = [
  { id: "indigo-dusk", label: "Indigo Dusk", gradient: "linear-gradient(135deg, #110c2c 0%, #1e1b4b 40%, #312e81 80%, #4338ca 100%)" },
  { id: "midnight-emerald", label: "Midnight Emerald", gradient: "linear-gradient(135deg, #011c15 0%, #022c22 40%, #064e3b 80%, #0f766e 100%)" },
  { id: "crimson-sunset", label: "Crimson Sunset", gradient: "linear-gradient(135deg, #320311 0%, #4c0519 40%, #881337 80%, #be123c 100%)" },
  { id: "deep-space", label: "Deep Space", gradient: "linear-gradient(135deg, #090d16 0%, #0f172a 40%, #1e293b 80%, #334155 100%)" },
  { id: "royal-plum", label: "Royal Plum", gradient: "linear-gradient(135deg, #1c0a3c 0%, #2e1065 40%, #581c87 80%, #7e22ce 100%)" },
  { id: "vibrant-coral", label: "Vibrant Coral", gradient: "linear-gradient(135deg, #4f1d0b 0%, #7c2d12 40%, #9a3412 80%, #ea580c 100%)" },
];

// Font Mapping
const FONT_MAP = {
  "Outfit": "'Outfit', sans-serif",
  "Inter": "'Inter', sans-serif",
  "Playfair": "'Playfair Display', serif",
  "Mono": "'Roboto Mono', monospace",
};

// --- Initialization ---
document.addEventListener("DOMContentLoaded", () => {
  initThemeGrid();
  initInstaEventListeners();
});

function initThemeGrid() {
  const grid = document.getElementById("insta-theme-grid");
  if (!grid) return;

  INSTA_THEMES.forEach(theme => {
    const swatch = document.createElement("div");
    swatch.className = `theme-swatch${theme.id === instaState.theme ? " active" : ""}`;
    swatch.style.background = theme.gradient;
    swatch.title = theme.label;
    swatch.dataset.themeId = theme.id;
    swatch.addEventListener("click", () => {
      grid.querySelectorAll(".theme-swatch").forEach(s => s.classList.remove("active"));
      swatch.classList.add("active");
      instaState.theme = theme.id;
      rebuildAllSlides();
    });
    grid.appendChild(swatch);
  });
}

function initInstaEventListeners() {
  // Close modal
  const closeBtn = document.getElementById("close-instagram-modal");
  if (closeBtn) {
    closeBtn.addEventListener("click", closeInstagramModal);
  }

  // Close on overlay click
  const overlay = document.getElementById("instagram-modal");
  if (overlay) {
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) closeInstagramModal();
    });
  }

  // Preview navigation
  const prevBtn = document.getElementById("insta-prev-slide-btn");
  const nextBtn = document.getElementById("insta-next-slide-btn");
  if (prevBtn) prevBtn.addEventListener("click", () => navigatePreview(-1));
  if (nextBtn) nextBtn.addEventListener("click", () => navigatePreview(1));

  // Slide dots
  document.querySelectorAll(".slide-dot").forEach(dot => {
    dot.addEventListener("click", () => {
      const idx = parseInt(dot.dataset.index);
      instaState.activeSlideIndex = idx;
      showPreviewSlide();
    });
  });

  // Aspect ratio buttons
  const squareBtn = document.getElementById("insta-ratio-square");
  const portraitBtn = document.getElementById("insta-ratio-portrait");
  if (squareBtn) {
    squareBtn.addEventListener("click", () => {
      instaState.ratio = "1-1";
      squareBtn.classList.add("active");
      portraitBtn.classList.remove("active");
      document.getElementById("insta-preview-ratio-label").textContent = "1:1 Square";
      updateViewportRatio();
      rebuildAllSlides();
    });
  }
  if (portraitBtn) {
    portraitBtn.addEventListener("click", () => {
      instaState.ratio = "4-5";
      portraitBtn.classList.add("active");
      squareBtn.classList.remove("active");
      document.getElementById("insta-preview-ratio-label").textContent = "4:5 Portrait";
      updateViewportRatio();
      rebuildAllSlides();
    });
  }

  // Font selector
  const fontSelect = document.getElementById("insta-font-select");
  if (fontSelect) {
    fontSelect.addEventListener("change", () => {
      instaState.font = fontSelect.value;
      rebuildAllSlides();
    });
  }

  // Handle input
  const handleInput = document.getElementById("insta-handle-input");
  if (handleInput) {
    handleInput.addEventListener("input", () => {
      instaState.handle = handleInput.value || "@medbank.studio";
      rebuildAllSlides();
    });
  }

  // Logo toggle
  const logoToggle = document.getElementById("insta-logo-toggle");
  if (logoToggle) {
    logoToggle.addEventListener("change", () => {
      instaState.showLogo = logoToggle.checked;
      rebuildAllSlides();
    });
  }

  // CTA input
  const ctaInput = document.getElementById("insta-cta-input");
  if (ctaInput) {
    ctaInput.addEventListener("input", () => {
      instaState.ctaText = ctaInput.value;
      rebuildAllSlides();
    });
  }

  // Font size sliders
  setupSlider("insta-size-scenario", "val-size-scenario", (val) => {
    instaState.scenarioFontSize = val;
    rebuildAllSlides();
  });
  setupSlider("insta-size-options", "val-size-options", (val) => {
    instaState.optionsFontSize = val;
    rebuildAllSlides();
  });
  setupSlider("insta-size-explanation", "val-size-explanation", (val) => {
    instaState.explanationFontSize = val;
    rebuildAllSlides();
  });

  // Download buttons
  const downloadAllBtn = document.getElementById("insta-download-all");
  if (downloadAllBtn) {
    downloadAllBtn.addEventListener("click", downloadAllSlides);
  }
  document.querySelectorAll(".download-single-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const slideNum = parseInt(btn.dataset.slide);
      downloadSlide(slideNum);
    });
  });
}

function setupSlider(sliderId, labelId, onChange) {
  const slider = document.getElementById(sliderId);
  const label = document.getElementById(labelId);
  if (!slider || !label) return;

  slider.addEventListener("input", () => {
    const val = parseInt(slider.value);
    label.textContent = val;
    onChange(val);
  });
}

// --- Modal Open/Close ---
function openInstagramModal(questionId) {
  const q = state.questions.find(item => item.id === questionId);
  if (!q) {
    alert("Question not found in database.");
    return;
  }

  instaState.activeQuestion = q;
  instaState.activeSlideIndex = 0;

  // Reset controls to match current state
  document.getElementById("insta-font-select").value = instaState.font;
  document.getElementById("insta-handle-input").value = instaState.handle;
  document.getElementById("insta-logo-toggle").checked = instaState.showLogo;
  document.getElementById("insta-cta-input").value = instaState.ctaText;
  document.getElementById("insta-size-scenario").value = instaState.scenarioFontSize;
  document.getElementById("val-size-scenario").textContent = instaState.scenarioFontSize;
  document.getElementById("insta-size-options").value = instaState.optionsFontSize;
  document.getElementById("val-size-options").textContent = instaState.optionsFontSize;
  document.getElementById("insta-size-explanation").value = instaState.explanationFontSize;
  document.getElementById("val-size-explanation").textContent = instaState.explanationFontSize;

  // Build slides
  updateViewportRatio();
  rebuildAllSlides();
  showPreviewSlide();

  // Show modal
  document.getElementById("instagram-modal").style.display = "flex";
}

function closeInstagramModal() {
  document.getElementById("instagram-modal").style.display = "none";
}

// --- Viewport Ratio Handling ---
function updateViewportRatio() {
  const viewport = document.getElementById("insta-preview-viewport");
  const previewContainer = document.getElementById("insta-preview-slide-container");
  const exportContainer = document.getElementById("instagram-export-container");

  viewport.className = `preview-viewport ratio-${instaState.ratio}`;
  previewContainer.className = `preview-slide-container ratio-${instaState.ratio}`;

  if (instaState.ratio === "4-5") {
    exportContainer.style.height = "1350px";
    previewContainer.style.transform = `scale(${360 / 1080})`;
  } else {
    exportContainer.style.height = "1080px";
    previewContainer.style.transform = `scale(${360 / 1080})`;
  }
}

// --- Slide Building ---
function rebuildAllSlides() {
  const q = instaState.activeQuestion;
  if (!q) return;

  const exportContainer = document.getElementById("instagram-export-container");
  exportContainer.innerHTML = "";

  // Build 3 slides into export container
  for (let i = 1; i <= 3; i++) {
    const slideEl = buildSlideHTML(q, i);
    exportContainer.appendChild(slideEl);
  }

  // Refresh preview
  showPreviewSlide();
}

function buildSlideHTML(q, slideNumber) {
  const themeClass = `theme-${instaState.theme}`;
  const fontClass = `font-${instaState.font}`;
  const ratioClass = instaState.ratio === "4-5" ? "ratio-4-5" : "";
  const fontFamily = FONT_MAP[instaState.font] || "'Outfit', sans-serif";

  const slide = document.createElement("div");
  slide.className = `instagram-slide ${themeClass} ${fontClass} ${ratioClass}`;
  slide.id = `insta-export-slide-${slideNumber}`;
  slide.style.fontFamily = fontFamily;

  // Format question type label
  const typeLabel = q.type === "sba" ? "SBA" :
                    q.type === "emq" ? "EMQ" :
                    q.type === "ranking" ? "Ranking" :
                    q.type === "selection" ? "Selection" : q.type.toUpperCase();

  // Correct answer text (handles arrays)
  const correctText = Array.isArray(q.correct_answer)
    ? q.correct_answer.join(" → ")
    : q.correct_answer;

  // --- Slide Header (shared across all slides) ---
  const logoHTML = instaState.showLogo
    ? `<div class="slide-logo">
         <div class="slide-logo-icon">M</div>
         <span class="slide-logo-text">${escapeHtml(instaState.handle)}</span>
       </div>`
    : `<div class="slide-logo">
         <span class="slide-logo-text">${escapeHtml(instaState.handle)}</span>
       </div>`;

  const headerHTML = `
    <div class="slide-header">
      <div class="slide-header-top">
        ${logoHTML}
        <span class="slide-badge">${slideNumber}/3</span>
      </div>
      <div class="slide-header-tags">
        <span class="slide-tag">${escapeHtml(q.exam || "MSRA")}</span>
        <span class="slide-tag specialty">${escapeHtml(q.category)}</span>
        <span class="slide-tag">${typeLabel}</span>
      </div>
    </div>
  `;

  if (slideNumber === 1) {
    // --- SLIDE 1: HOOK / SCENARIO ---
    const footerText = `Slide 1 of 3`;
    slide.innerHTML = `
      ${headerHTML}
      <div class="slide-content">
        <div class="slide-scenario" style="font-size: ${instaState.scenarioFontSize}px;">
          ${escapeHtml(q.scenario)}
        </div>
      </div>
      <div class="slide-footer">
        <div class="slide-footer-left">${escapeHtml(instaState.handle)}</div>
        <div class="slide-footer-right">Swipe for options <i class="fa-solid fa-chevron-right"></i></div>
      </div>
    `;
  } else if (slideNumber === 2) {
    // --- SLIDE 2: OPTIONS ---
    let optionsHTML = "";

    if (q.type === "sba" || q.type === "emq") {
      optionsHTML = q.options.map((opt, idx) => {
        const letter = String.fromCharCode(65 + idx);
        return `
          <div class="slide-option-card">
            <div class="slide-option-badge">${letter}</div>
            <div style="flex: 1; font-size: ${instaState.optionsFontSize}px;">${escapeHtml(opt)}</div>
          </div>`;
      }).join("");
    } else if (q.type === "ranking") {
      optionsHTML = q.options.map((opt, idx) => {
        return `
          <div class="slide-option-card">
            <div class="slide-option-badge">${idx + 1}</div>
            <div style="flex: 1; font-size: ${instaState.optionsFontSize}px;">${escapeHtml(opt)}</div>
          </div>`;
      }).join("");
    } else if (q.type === "selection") {
      optionsHTML = q.options.map((opt, idx) => {
        const letter = String.fromCharCode(65 + idx);
        return `
          <div class="slide-option-card">
            <div class="slide-option-badge">${letter}</div>
            <div style="flex: 1; font-size: ${instaState.optionsFontSize}px;">${escapeHtml(opt)}</div>
          </div>`;
      }).join("");
    }

    const questionPrompt = q.type === "ranking"
      ? "Rank the following options from most to least appropriate:"
      : q.type === "selection"
      ? "Select the THREE most appropriate options:"
      : "Which of the following is the single best answer?";

    slide.innerHTML = `
      ${headerHTML}
      <div class="slide-content">
        <div class="slide-answer-title" style="margin-bottom: 16px;">${escapeHtml(questionPrompt)}</div>
        <div class="slide-options-list">
          ${optionsHTML}
        </div>
      </div>
      <div class="slide-footer">
        <div class="slide-footer-left">${escapeHtml(instaState.handle)}</div>
        <div class="slide-footer-right">Swipe for answer <i class="fa-solid fa-chevron-right"></i></div>
      </div>
    `;
  } else if (slideNumber === 3) {
    // --- SLIDE 3: ANSWER + EXPLANATION ---
    let answerBannerHTML = "";

    if (q.type === "sba" || q.type === "emq") {
      // Find letter for the correct answer
      const correctIdx = q.options.indexOf(q.correct_answer);
      const correctLetter = correctIdx >= 0 ? String.fromCharCode(65 + correctIdx) : "✓";
      answerBannerHTML = `
        <div class="slide-answer-banner" style="font-size: ${instaState.optionsFontSize}px;">
          <i class="fa-solid fa-circle-check"></i>
          <div><strong>${correctLetter}.</strong> ${escapeHtml(q.correct_answer)}</div>
        </div>`;
    } else if (q.type === "ranking") {
      answerBannerHTML = `<div class="slide-answer-banner" style="font-size: ${instaState.optionsFontSize - 2}px; flex-direction: column; align-items: flex-start; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-circle-check"></i> <strong>Correct Ranking Order:</strong></div>
        ${q.correct_answer.map((opt, idx) => `<div style="padding-left: 36px;">${idx + 1}. ${escapeHtml(opt)}</div>`).join("")}
      </div>`;
    } else if (q.type === "selection") {
      answerBannerHTML = `<div class="slide-answer-banner" style="font-size: ${instaState.optionsFontSize - 2}px; flex-direction: column; align-items: flex-start; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-circle-check"></i> <strong>Correct Selections:</strong></div>
        ${q.correct_answer.map(opt => `<div style="padding-left: 36px;">• ${escapeHtml(opt)}</div>`).join("")}
      </div>`;
    }

    const ctaHTML = instaState.ctaText
      ? `<div style="text-align: center; font-size: 0.85rem; opacity: 0.7; margin-top: 8px; font-style: italic;">💡 ${escapeHtml(instaState.ctaText)}</div>`
      : "";

    slide.innerHTML = `
      ${headerHTML}
      <div class="slide-content">
        <div class="slide-answer-title">Correct Answer</div>
        ${answerBannerHTML}
        <div class="slide-explanation-title">Key Learning Points</div>
        <div class="slide-explanation-box" style="font-size: ${instaState.explanationFontSize}px;">
          ${escapeHtml(q.explanation)}
        </div>
        ${ctaHTML}
      </div>
      <div class="slide-footer">
        <div class="slide-footer-left">${escapeHtml(instaState.handle)}</div>
        <div class="slide-footer-right">Follow for more <i class="fa-solid fa-heart" style="animation: none; color: #ef4444;"></i></div>
      </div>
    `;
  }

  return slide;
}

// --- Preview Navigation ---
function navigatePreview(direction) {
  let next = instaState.activeSlideIndex + direction;
  if (next < 0) next = 2;
  if (next > 2) next = 0;
  instaState.activeSlideIndex = next;
  showPreviewSlide();
}

function showPreviewSlide() {
  const previewContainer = document.getElementById("insta-preview-slide-container");
  const exportContainer = document.getElementById("instagram-export-container");
  const slideNum = instaState.activeSlideIndex + 1;

  // Clone the correct export slide into preview
  const sourceSlide = document.getElementById(`insta-export-slide-${slideNum}`);
  if (!sourceSlide) return;

  previewContainer.innerHTML = "";
  const clone = sourceSlide.cloneNode(true);
  clone.id = ""; // Avoid duplicate IDs
  previewContainer.appendChild(clone);

  // Update slide number display
  document.getElementById("insta-preview-slide-num").textContent = slideNum;

  // Update dots
  document.querySelectorAll(".slide-dot").forEach(dot => {
    dot.classList.toggle("active", parseInt(dot.dataset.index) === instaState.activeSlideIndex);
  });
}

// --- Download Logic ---
async function downloadSlide(slideNumber) {
  const slideEl = document.getElementById(`insta-export-slide-${slideNumber}`);
  if (!slideEl) {
    alert("Slide not found. Please try regenerating.");
    return;
  }

  const q = instaState.activeQuestion;
  const filename = `${(q.exam || "msra").toLowerCase()}_${q.type}_slide_${slideNumber}.png`;

  const exportContainer = document.getElementById("instagram-export-container");

  try {
    // Move the export container into visible layout so html2canvas can measure
    // and paint it. Keep it visually hidden with opacity:0 and behind everything.
    exportContainer.style.left = "0";
    exportContainer.style.opacity = "0";
    exportContainer.style.zIndex = "-1";
    exportContainer.style.pointerEvents = "none";

    // Allow a brief tick for the browser to reflow / fonts to apply
    await new Promise(resolve => setTimeout(resolve, 150));

    const canvas = await html2canvas(slideEl, {
      scale: 2,
      useCORS: true,
      allowTaint: true,
      backgroundColor: null,
      width: 1080,
      height: instaState.ratio === "4-5" ? 1350 : 1080,
      logging: false,
    });

    canvas.toBlob((blob) => {
      if (!blob) {
        alert("Failed to generate image. Please try again.");
        return;
      }
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, "image/png", 1.0);
  } catch (err) {
    console.error("Download error:", err);
    alert("Failed to export slide. Check console for details.");
  } finally {
    // Always restore the container to its off-screen position
    exportContainer.style.left = "-9999px";
    exportContainer.style.opacity = "";
    exportContainer.style.zIndex = "";
  }
}

async function downloadAllSlides() {
  const btn = document.getElementById("insta-download-all");
  const originalText = btn.innerHTML;
  btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Generating...';
  btn.disabled = true;

  try {
    for (let i = 1; i <= 3; i++) {
      await downloadSlide(i);
      // Small delay between downloads to prevent browser blocking
      if (i < 3) {
        await new Promise(resolve => setTimeout(resolve, 600));
      }
    }
  } catch (err) {
    console.error("Download all error:", err);
  } finally {
    btn.innerHTML = originalText;
    btn.disabled = false;
  }
}

// --- Utilities ---
function escapeHtml(text) {
  if (!text) return "";
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
