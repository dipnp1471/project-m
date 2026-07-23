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
  handle: "@medqstudios",
  websiteUrl: "www.medqstudios.com",
  showWebsiteFooter: true,
  websiteFooterStyle: "pill", // "pill", "banner", "subfooter"
  showHeaderDomain: true,
  showLogo: true,
  ctaText: "Save this post & practice 1000+ questions on medqstudios.com",
  ratio: "1-1", // "1-1", "4-5", or "9-16"
  scenarioFontSize: 26,
  optionsFontSize: 20,
  explanationFontSize: 18,
  websiteFontSize: 20,
  headerFontSize: 18,
};

// Font Presets Mapping
const FONT_PRESETS = {
  compact: { scenario: 20, options: 16, explanation: 14, website: 16, header: 14 },
  default: { scenario: 26, options: 20, explanation: 18, website: 20, header: 18 },
  large: { scenario: 34, options: 26, explanation: 22, website: 24, header: 22 },
  xlarge: { scenario: 44, options: 32, explanation: 26, website: 28, header: 26 },
  max: { scenario: 56, options: 40, explanation: 32, website: 34, header: 30 },
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
  const reelsBtn = document.getElementById("insta-ratio-reels");
  if (squareBtn) {
    squareBtn.addEventListener("click", () => {
      instaState.ratio = "1-1";
      squareBtn.classList.add("active");
      if (portraitBtn) portraitBtn.classList.remove("active");
      if (reelsBtn) reelsBtn.classList.remove("active");
      document.getElementById("insta-preview-ratio-label").textContent = "1:1 Square";
      updateViewportRatio();
      rebuildAllSlides();
    });
  }
  if (portraitBtn) {
    portraitBtn.addEventListener("click", () => {
      instaState.ratio = "4-5";
      portraitBtn.classList.add("active");
      if (squareBtn) squareBtn.classList.remove("active");
      if (reelsBtn) reelsBtn.classList.remove("active");
      document.getElementById("insta-preview-ratio-label").textContent = "4:5 Portrait";
      updateViewportRatio();
      rebuildAllSlides();
    });
  }
  if (reelsBtn) {
    reelsBtn.addEventListener("click", () => {
      instaState.ratio = "9-16";
      reelsBtn.classList.add("active");
      if (squareBtn) squareBtn.classList.remove("active");
      if (portraitBtn) portraitBtn.classList.remove("active");
      document.getElementById("insta-preview-ratio-label").textContent = "9:16 Reels";
      updateViewportRatio();
      rebuildAllSlides();
    });
  }

  // Canva Export Handlers
  document.querySelectorAll(".copy-canva-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const slideNum = parseInt(btn.dataset.slide);
      copySlideToClipboard(slideNum);
    });
  });

  const openCanvaBtn = document.getElementById("insta-open-canva-btn");
  if (openCanvaBtn) {
    openCanvaBtn.addEventListener("click", () => {
      window.open("https://www.canva.com", "_blank");
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
      instaState.handle = handleInput.value || "@medqstudios";
      rebuildAllSlides();
    });
  }

  // Website Input
  const websiteInput = document.getElementById("insta-website-input");
  if (websiteInput) {
    websiteInput.addEventListener("input", () => {
      instaState.websiteUrl = websiteInput.value.trim() || "www.medqstudios.com";
      rebuildAllSlides();
    });
  }

  // Website Footer Style Select
  const styleSelect = document.getElementById("insta-website-style-select");
  if (styleSelect) {
    styleSelect.addEventListener("change", () => {
      instaState.websiteFooterStyle = styleSelect.value;
      rebuildAllSlides();
    });
  }

  // Website Footer Toggle
  const websiteToggle = document.getElementById("insta-website-toggle");
  if (websiteToggle) {
    websiteToggle.addEventListener("change", () => {
      instaState.showWebsiteFooter = websiteToggle.checked;
      rebuildAllSlides();
    });
  }

  // Header Domain Tag Toggle
  const headerDomainToggle = document.getElementById("insta-header-domain-toggle");
  if (headerDomainToggle) {
    headerDomainToggle.addEventListener("change", () => {
      instaState.showHeaderDomain = headerDomainToggle.checked;
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
    clearPresetButtons();
    rebuildAllSlides();
  });
  setupSlider("insta-size-options", "val-size-options", (val) => {
    instaState.optionsFontSize = val;
    clearPresetButtons();
    rebuildAllSlides();
  });
  setupSlider("insta-size-explanation", "val-size-explanation", (val) => {
    instaState.explanationFontSize = val;
    clearPresetButtons();
    rebuildAllSlides();
  });
  setupSlider("insta-size-website", "val-size-website", (val) => {
    instaState.websiteFontSize = val;
    clearPresetButtons();
    rebuildAllSlides();
  });
  setupSlider("insta-size-header", "val-size-header", (val) => {
    instaState.headerFontSize = val;
    clearPresetButtons();
    rebuildAllSlides();
  });

  // Font Size Preset Buttons
  document.querySelectorAll(".font-preset-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const presetKey = btn.dataset.preset;
      applyFontPreset(presetKey);
    });
  });

  // Copy Instagram Caption Button
  const copyCaptionBtn = document.getElementById("insta-copy-caption-btn");
  if (copyCaptionBtn) {
    copyCaptionBtn.addEventListener("click", copyInstagramCaption);
  }

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

function clearPresetButtons() {
  document.querySelectorAll(".font-preset-btn").forEach(btn => btn.classList.remove("active"));
}

function applyFontPreset(presetKey) {
  const preset = FONT_PRESETS[presetKey];
  if (!preset) return;

  instaState.scenarioFontSize = preset.scenario;
  instaState.optionsFontSize = preset.options;
  instaState.explanationFontSize = preset.explanation;
  instaState.websiteFontSize = preset.website;
  instaState.headerFontSize = preset.header;

  // Update slider inputs and labels
  updateSliderDOM("insta-size-scenario", "val-size-scenario", preset.scenario);
  updateSliderDOM("insta-size-options", "val-size-options", preset.options);
  updateSliderDOM("insta-size-explanation", "val-size-explanation", preset.explanation);
  updateSliderDOM("insta-size-website", "val-size-website", preset.website);
  updateSliderDOM("insta-size-header", "val-size-header", preset.header);

  // Update active preset button
  document.querySelectorAll(".font-preset-btn").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.preset === presetKey);
  });

  rebuildAllSlides();
}

function updateSliderDOM(sliderId, labelId, val) {
  const slider = document.getElementById(sliderId);
  const label = document.getElementById(labelId);
  if (slider) slider.value = val;
  if (label) label.textContent = val;
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
  const webInput = document.getElementById("insta-website-input");
  if (webInput) webInput.value = instaState.websiteUrl;
  const styleSelect = document.getElementById("insta-website-style-select");
  if (styleSelect) styleSelect.value = instaState.websiteFooterStyle;
  const webToggle = document.getElementById("insta-website-toggle");
  if (webToggle) webToggle.checked = instaState.showWebsiteFooter;
  const domainToggle = document.getElementById("insta-header-domain-toggle");
  if (domainToggle) domainToggle.checked = instaState.showHeaderDomain;

  document.getElementById("insta-logo-toggle").checked = instaState.showLogo;
  document.getElementById("insta-cta-input").value = instaState.ctaText;

  updateSliderDOM("insta-size-scenario", "val-size-scenario", instaState.scenarioFontSize);
  updateSliderDOM("insta-size-options", "val-size-options", instaState.optionsFontSize);
  updateSliderDOM("insta-size-explanation", "val-size-explanation", instaState.explanationFontSize);
  updateSliderDOM("insta-size-website", "val-size-website", instaState.websiteFontSize);
  updateSliderDOM("insta-size-header", "val-size-header", instaState.headerFontSize);

  // Reset active classes on ratio buttons
  const squareBtn = document.getElementById("insta-ratio-square");
  const portraitBtn = document.getElementById("insta-ratio-portrait");
  const reelsBtn = document.getElementById("insta-ratio-reels");
  if (squareBtn) squareBtn.classList.toggle("active", instaState.ratio === "1-1");
  if (portraitBtn) portraitBtn.classList.toggle("active", instaState.ratio === "4-5");
  if (reelsBtn) reelsBtn.classList.toggle("active", instaState.ratio === "9-16");
  
  const ratioLabel = document.getElementById("insta-preview-ratio-label");
  if (ratioLabel) {
    ratioLabel.textContent = instaState.ratio === "1-1" ? "1:1 Square" : (instaState.ratio === "4-5" ? "4:5 Portrait" : "9:16 Reels");
  }

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
  } else if (instaState.ratio === "9-16") {
    exportContainer.style.height = "1920px";
    previewContainer.style.transform = `scale(${360 / 1080})`;
  } else {
    exportContainer.style.height = "1080px";
    previewContainer.style.transform = `scale(${360 / 1080})`;
  }

  updateSlideControls();
}

function updateSlideControls() {
  const isReels = instaState.ratio === "9-16";
  
  // Update dots display
  const dots = document.querySelectorAll(".slide-dot");
  if (dots.length >= 3) {
    dots[2].style.display = isReels ? "none" : "block";
  }
  
  // If active index was 2, reset it
  if (isReels && instaState.activeSlideIndex > 1) {
    instaState.activeSlideIndex = 0;
  }
  
  // Update single download button for Slide 3
  const downloadBtn3 = document.querySelector(".download-single-btn[data-slide='3']");
  if (downloadBtn3) {
    downloadBtn3.style.display = isReels ? "none" : "inline-block";
  }

  // Update Canva copy button for Slide 3
  const copyBtn3 = document.getElementById("insta-copy-slide-3");
  if (copyBtn3) {
    copyBtn3.style.display = isReels ? "none" : "inline-block";
  }
}

// --- Slide Building ---
function rebuildAllSlides() {
  const q = instaState.activeQuestion;
  if (!q) return;

  const exportContainer = document.getElementById("instagram-export-container");
  exportContainer.innerHTML = "";

  const totalSlides = instaState.ratio === "9-16" ? 2 : 3;

  // Build slides into export container
  for (let i = 1; i <= totalSlides; i++) {
    const slideEl = buildSlideHTML(q, i);
    exportContainer.appendChild(slideEl);
  }

  // Refresh preview
  showPreviewSlide();
}

function buildSlideHTML(q, slideNumber) {
  const themeClass = `theme-${instaState.theme}`;
  const fontClass = `font-${instaState.font}`;
  const ratioClass = instaState.ratio === "4-5" ? "ratio-4-5" : (instaState.ratio === "9-16" ? "ratio-9-16" : "");
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

  // Domain Tag in Header
  const domainTagHTML = (instaState.showHeaderDomain && instaState.websiteUrl)
    ? `<span class="slide-tag domain"><i class="fa-solid fa-globe"></i> ${escapeHtml(instaState.websiteUrl)}</span>`
    : "";

  // --- Slide Header (shared across all slides) ---
  const logoHTML = instaState.showLogo
    ? `<div class="slide-logo">
         <div class="slide-logo-icon" style="width: ${Math.round(instaState.headerFontSize * 2.2)}px; height: ${Math.round(instaState.headerFontSize * 2.2)}px; font-size: ${Math.round(instaState.headerFontSize * 1.1)}px;">M</div>
         <span class="slide-logo-text" style="font-size: ${instaState.headerFontSize}px;">${escapeHtml(instaState.handle)}</span>
       </div>`
    : `<div class="slide-logo">
         <span class="slide-logo-text" style="font-size: ${instaState.headerFontSize}px;">${escapeHtml(instaState.handle)}</span>
       </div>`;

  const totalSlidesCount = instaState.ratio === "9-16" ? 2 : 3;
  const headerHTML = `
    <div class="slide-header">
      <div class="slide-header-top">
        ${logoHTML}
        <span class="slide-badge" style="font-size: ${Math.max(12, Math.round(instaState.headerFontSize * 0.7))}px;">${slideNumber}/${totalSlidesCount}</span>
      </div>
      <div class="slide-header-tags">
        <span class="slide-tag">${escapeHtml(q.exam || "MSRA")}</span>
        <span class="slide-tag specialty">${escapeHtml(q.category)}</span>
        <span class="slide-tag">${typeLabel}</span>
        ${domainTagHTML}
      </div>
    </div>
  `;

  // Website Footer Elements
  let websitePillHTML = "";
  let websiteBannerHTML = "";
  let subfooterLinkHTML = "";

  if (instaState.showWebsiteFooter && instaState.websiteUrl) {
    if (instaState.websiteFooterStyle === "pill") {
      websitePillHTML = `
        <div class="slide-website-pill" style="font-size: ${instaState.websiteFontSize}px;">
          <i class="fa-solid fa-globe"></i> ${escapeHtml(instaState.websiteUrl)}
        </div>`;
    } else if (instaState.websiteFooterStyle === "banner") {
      websiteBannerHTML = `
        <div class="slide-website-banner" style="font-size: ${instaState.websiteFontSize}px;">
          <i class="fa-solid fa-rocket"></i> Practice & track questions for free at ${escapeHtml(instaState.websiteUrl)}
        </div>`;
    } else if (instaState.websiteFooterStyle === "subfooter") {
      subfooterLinkHTML = `
        <span class="slide-subfooter-link" style="font-size: ${Math.max(14, Math.round(instaState.websiteFontSize * 0.9))}px; margin-left: 10px;">
          <i class="fa-solid fa-link"></i> ${escapeHtml(instaState.websiteUrl)}
        </span>`;
    }
  }

  if (instaState.ratio === "9-16") {
    // --- 9:16 REELS RATIO LAYOUT (2 Slides Total) ---
    if (slideNumber === 1) {
      // --- REELS SLIDE 1: QUESTION & OPTIONS ---
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
        ? "Rank the options:"
        : q.type === "selection"
        ? "Select the THREE most appropriate options:"
        : "Select the single best answer:";

      slide.innerHTML = `
        ${headerHTML}
        <div class="slide-content" style="gap: 24px; justify-content: flex-start; padding: 10px 0;">
          <div class="slide-scenario" style="font-size: ${instaState.scenarioFontSize}px; line-height: 1.5; margin-bottom: 5px;">
            ${escapeHtml(q.scenario)}
          </div>
          <div style="width: 100%; border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: 20px; margin-top: 5px;">
            <div class="slide-answer-title" style="margin-bottom: 12px; font-size: 0.85rem;">${escapeHtml(questionPrompt)}</div>
            <div class="slide-options-list" style="gap: 12px;">
              ${optionsHTML}
            </div>
          </div>
          ${websitePillHTML ? `<div style="text-align: center; margin-top: 15px;">${websitePillHTML}</div>` : ""}
        </div>
        <div class="slide-footer" style="font-size: ${instaState.headerFontSize}px;">
          <div class="slide-footer-left">${escapeHtml(instaState.handle)}${subfooterLinkHTML}</div>
          <div class="slide-footer-right">Swipe for answer <i class="fa-solid fa-chevron-right"></i></div>
        </div>
        ${websiteBannerHTML}
      `;
    } else if (slideNumber === 2) {
      // --- REELS SLIDE 2: ANSWER + EXPLANATION ---
      let answerBannerHTML = "";

      if (q.type === "sba" || q.type === "emq") {
        const correctIdx = q.options.indexOf(q.correct_answer);
        const correctLetter = correctIdx >= 0 ? String.fromCharCode(65 + correctIdx) : "✓";
        answerBannerHTML = `
          <div class="slide-answer-banner" style="font-size: ${instaState.optionsFontSize}px; margin-bottom: 20px; padding: 16px 20px;">
            <i class="fa-solid fa-circle-check"></i>
            <div><strong>${correctLetter}.</strong> ${escapeHtml(q.correct_answer)}</div>
          </div>`;
      } else if (q.type === "ranking") {
        answerBannerHTML = `<div class="slide-answer-banner" style="font-size: ${instaState.optionsFontSize - 2}px; flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 20px; padding: 16px 20px;">
          <div style="display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-circle-check"></i> <strong>Correct Ranking Order:</strong></div>
          ${q.correct_answer.map((opt, idx) => `<div style="padding-left: 36px;">${idx + 1}. ${escapeHtml(opt)}</div>`).join("")}
        </div>`;
      } else if (q.type === "selection") {
        answerBannerHTML = `<div class="slide-answer-banner" style="font-size: ${instaState.optionsFontSize - 2}px; flex-direction: column; align-items: flex-start; gap: 8px; margin-bottom: 20px; padding: 16px 20px;">
          <div style="display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-circle-check"></i> <strong>Correct Selections:</strong></div>
          ${q.correct_answer.map(opt => `<div style="padding-left: 36px;">• ${escapeHtml(opt)}</div>`).join("")}
        </div>`;
      }

      const ctaHTML = instaState.ctaText
        ? `<div style="text-align: center; font-size: ${Math.max(14, Math.round(instaState.explanationFontSize * 0.9))}px; opacity: 0.95; margin-top: 14px; font-style: italic; background: rgba(255,255,255,0.08); padding: 10px 16px; border-radius: 12px;">💡 ${escapeHtml(instaState.ctaText)}</div>`
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
          ${websitePillHTML ? `<div style="text-align: center; margin-top: 18px;">${websitePillHTML}</div>` : ""}
        </div>
        <div class="slide-footer" style="font-size: ${instaState.headerFontSize}px;">
          <div class="slide-footer-left">${escapeHtml(instaState.handle)}${subfooterLinkHTML}</div>
          <div class="slide-footer-right">Follow for more <i class="fa-solid fa-heart" style="animation: none; color: #ef4444;"></i></div>
        </div>
        ${websiteBannerHTML}
      `;
    }
  } else {
    // --- STANDARD 1:1 OR 4:5 LAYOUT (3 Slides Total) ---
    if (slideNumber === 1) {
      // --- SLIDE 1: HOOK / SCENARIO ---
      slide.innerHTML = `
        ${headerHTML}
        <div class="slide-content">
          <div class="slide-scenario" style="font-size: ${instaState.scenarioFontSize}px;">
            ${escapeHtml(q.scenario)}
          </div>
          ${websitePillHTML ? `<div style="text-align: center; margin-top: 24px;">${websitePillHTML}</div>` : ""}
        </div>
        <div class="slide-footer" style="font-size: ${instaState.headerFontSize}px;">
          <div class="slide-footer-left">${escapeHtml(instaState.handle)}${subfooterLinkHTML}</div>
          <div class="slide-footer-right">Swipe for options <i class="fa-solid fa-chevron-right"></i></div>
        </div>
        ${websiteBannerHTML}
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
          ${websitePillHTML ? `<div style="text-align: center; margin-top: 24px;">${websitePillHTML}</div>` : ""}
        </div>
        <div class="slide-footer" style="font-size: ${instaState.headerFontSize}px;">
          <div class="slide-footer-left">${escapeHtml(instaState.handle)}${subfooterLinkHTML}</div>
          <div class="slide-footer-right">Swipe for answer <i class="fa-solid fa-chevron-right"></i></div>
        </div>
        ${websiteBannerHTML}
      `;
    } else if (slideNumber === 3) {
      // --- SLIDE 3: ANSWER + EXPLANATION ---
      let answerBannerHTML = "";

      if (q.type === "sba" || q.type === "emq") {
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
        ? `<div style="text-align: center; font-size: ${Math.max(14, Math.round(instaState.explanationFontSize * 0.9))}px; opacity: 0.95; margin-top: 14px; font-style: italic; background: rgba(255,255,255,0.08); padding: 10px 16px; border-radius: 12px;">💡 ${escapeHtml(instaState.ctaText)}</div>`
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
          ${websitePillHTML ? `<div style="text-align: center; margin-top: 18px;">${websitePillHTML}</div>` : ""}
        </div>
        <div class="slide-footer" style="font-size: ${instaState.headerFontSize}px;">
          <div class="slide-footer-left">${escapeHtml(instaState.handle)}${subfooterLinkHTML}</div>
          <div class="slide-footer-right">Follow for more <i class="fa-solid fa-heart" style="animation: none; color: #ef4444;"></i></div>
        </div>
        ${websiteBannerHTML}
      `;
    }
  }

  return slide;
}

// --- Instagram Caption Copier with Website Link ---
function copyInstagramCaption() {
  const q = instaState.activeQuestion;
  if (!q) {
    alert("No active question found.");
    return;
  }

  const typeLabel = q.type === "sba" ? "SBA" :
                    q.type === "emq" ? "EMQ" :
                    q.type === "ranking" ? "Ranking" :
                    q.type === "selection" ? "Selection" : q.type.toUpperCase();

  const optionsList = (q.options || []).map((opt, idx) => {
    const letter = String.fromCharCode(65 + idx);
    return `${letter}) ${opt}`;
  }).join("\n");

  // Format Correct Answer Text
  let answerText = "";
  if (q.type === "sba" || q.type === "emq") {
    const correctIdx = (q.options || []).indexOf(q.correct_answer);
    const correctLetter = correctIdx >= 0 ? String.fromCharCode(65 + correctIdx) + ". " : "";
    answerText = `✅ Correct Answer:\n${correctLetter}${q.correct_answer}`;
  } else if (q.type === "ranking") {
    const rankingFormatted = Array.isArray(q.correct_answer)
      ? q.correct_answer.map((opt, i) => `${i + 1}. ${opt}`).join("\n")
      : q.correct_answer;
    answerText = `✅ Correct Answer (Ranking Order):\n${rankingFormatted}`;
  } else if (q.type === "selection") {
    const selectionFormatted = Array.isArray(q.correct_answer)
      ? q.correct_answer.map(opt => `• ${opt}`).join("\n")
      : q.correct_answer;
    answerText = `✅ Correct Answer (Selections):\n${selectionFormatted}`;
  } else {
    answerText = `✅ Correct Answer:\n${q.correct_answer}`;
  }

  // Format Explanation Text
  const explanationText = q.explanation ? `📖 Explanation:\n${q.explanation}` : "";

  const captionText = `🎯 MSRA Practice Question (${typeLabel}) - ${q.category || "General Medical"}

${q.scenario}

👇 Options:
${optionsList}

---
${answerText}

${explanationText}

---
🌐 Practice and track questions for free on our companion question bank website at:
👉 https://${instaState.websiteUrl} (Link in bio!)

#MSRA #MedicalExam #MedEd #NHS #JuniorDoctor #GPST #Revision ${instaState.handle}`;

  navigator.clipboard.writeText(captionText).then(() => {
    alert("Instagram Caption copied to clipboard!\n\nIncludes your question scenario, options, correct answer, explanation, website link (https://" + instaState.websiteUrl + "), and bio CTA.");
  }).catch(err => {
    console.error("Failed to copy caption:", err);
    alert("Could not copy caption to clipboard. Please allow clipboard permissions.");
  });
}

// --- Preview Navigation ---
function navigatePreview(direction) {
  let next = instaState.activeSlideIndex + direction;
  const maxIndex = instaState.ratio === "9-16" ? 1 : 2;
  if (next < 0) next = maxIndex;
  if (next > maxIndex) next = 0;
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
      height: instaState.ratio === "4-5" ? 1350 : (instaState.ratio === "9-16" ? 1920 : 1080),
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
    alert("Failed to export slide.\n\nError: " + (err.message || err));
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

  const totalSlides = instaState.ratio === "9-16" ? 2 : 3;

  try {
    for (let i = 1; i <= totalSlides; i++) {
      await downloadSlide(i);
      // Small delay between downloads to prevent browser blocking
      if (i < totalSlides) {
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

// --- Canva Export (Copy to Clipboard) Logic ---
async function copySlideToClipboard(slideNumber) {
  const slideEl = document.getElementById(`insta-export-slide-${slideNumber}`);
  if (!slideEl) {
    alert("Slide not found. Please try regenerating.");
    return;
  }

  const btn = document.getElementById(`insta-copy-slide-${slideNumber}`);
  const originalHTML = btn ? btn.innerHTML : "";
  if (btn) {
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Copying...';
    btn.disabled = true;
  }

  const exportContainer = document.getElementById("instagram-export-container");

  try {
    // Move the export container into visible layout so html2canvas can measure
    exportContainer.style.left = "0";
    exportContainer.style.opacity = "0";
    exportContainer.style.zIndex = "-1";
    exportContainer.style.pointerEvents = "none";

    // Allow a brief tick for browser to reflow
    await new Promise(resolve => setTimeout(resolve, 150));

    let height = 1080;
    if (instaState.ratio === "4-5") {
      height = 1350;
    } else if (instaState.ratio === "9-16") {
      height = 1920;
    }

    const canvas = await html2canvas(slideEl, {
      scale: 2,
      useCORS: true,
      allowTaint: true,
      backgroundColor: null,
      width: 1080,
      height: height,
      logging: false,
    });

    canvas.toBlob(async (blob) => {
      if (!blob) {
        alert("Failed to generate image.");
        if (btn) {
          btn.innerHTML = originalHTML;
          btn.disabled = false;
        }
        return;
      }

      try {
        // Write the blob to the system clipboard
        await navigator.clipboard.write([
          new ClipboardItem({
            [blob.type]: blob
          })
        ]);
        alert(`Slide ${slideNumber} copied to clipboard! You can now paste it directly into Canva (Ctrl+V) or any other tool.`);
      } catch (err) {
        console.error("Clipboard write failed:", err);
        alert("Failed to copy automatically. Please ensure clipboard permissions are enabled for this tab, or download the slide and upload it manually.");
      } finally {
        if (btn) {
          btn.innerHTML = originalHTML;
          btn.disabled = false;
        }
      }
    }, "image/png");

  } catch (err) {
    console.error("Copy error:", err);
    alert("Failed to copy slide.\n\nError: " + (err.message || err));
    if (btn) {
      btn.innerHTML = originalHTML;
      btn.disabled = false;
    }
  } finally {
    exportContainer.style.left = "-9999px";
    exportContainer.style.opacity = "";
    exportContainer.style.zIndex = "";
  }
}

// --- Utilities ---
function escapeHtml(text) {
  if (!text) return "";
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
