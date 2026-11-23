/**
 * Animated Reel Video Studio Module
 * Renders high-retention 9:16 vertical video with kinetic word reading,
 * cycling option spotlight with soft musical notes/boops, and answer reveal.
 * Exports video with synchronized audio directly in the browser via MediaRecorder.
 */

// --- Video Studio State ---
const videoState = {
  activeQuestion: null,
  videoMode: "animated", // "animated" | "static"
  staticDuration: 7, // Default 7s for Static Reel (3-30s)
  staticLayout: "question-only", // "question-only" | "with-answer"
  isPlaying: false,
  currentTime: 0,
  totalDuration: 13.0,
  readingDuration: 5.0,
  cyclingDuration: 4.0, // Default 4.0s (1.0s deliberate review per option)
  postCyclingPause: 2.0, // Default 2.0s suspense pause after options cycling before answer pops up
  revealDuration: 3.5,
  wpm: 300,
  explanationFontSize: 24, // Video explanation font size
  readingStyle: "kinetic-glow", // "kinetic-glow", "word-fade", "typewriter"
  deliberationStyle: "single-pass-pill", // "single-pass-pill", "minimal-timer", "elimination"
  cycleSound: "soft-piano", // "soft-piano", "marimba-boop", "zen-chime", "digital-blip", "mute", "custom"
  revealSound: "success-chime", // "success-chime", "piano-resolve", "gentle-bell", "mute"
  customCycleBuffer: null,
  customCycleFileName: "",
  volume: 0.45, // Velvet background volume
  isMuted: false,
  revealMode: "full", // "full", "teaser"
  showPausePrompt: true,
  pausePromptText: "⏸️ Pause to solve • Answer in 3s",
  showCommentPrompt: true,
  commentPromptText: "💬 Full rationale & guidelines in caption 👇",
  lastSoundStep: -1,
  revealSoundPlayed: false,
  isExporting: false,
  exportProgress: 0,
  animationReqId: null,
  lastFrameTimestamp: null,
};

// --- Web Audio Synthesizer & Sound Engine ---
class StudioAudioEngine {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
  }

  init() {
    if (!this.ctx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContextClass();
      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.setValueAtTime(videoState.isMuted ? 0 : videoState.volume, this.ctx.currentTime);
      this.masterGain.connect(this.ctx.destination);
    }
    if (this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  }

  setVolume(val) {
    if (this.masterGain && this.ctx) {
      const targetGain = videoState.isMuted ? 0 : Math.max(0, Math.min(1, val));
      this.masterGain.gain.setValueAtTime(targetGain, this.ctx.currentTime);
    }
  }

  playCycleSound(stepIndex, destNode = null) {
    if (videoState.isMuted || videoState.cycleSound === "mute") return;
    this.init();
    const dest = destNode || this.masterGain;
    const now = this.ctx.currentTime;

    if (videoState.cycleSound === "custom" && videoState.customCycleBuffer) {
      try {
        const source = this.ctx.createBufferSource();
        source.buffer = videoState.customCycleBuffer;
        source.connect(dest);
        source.start(now);
      } catch (err) {
        console.warn("Custom sound play error:", err);
      }
      return;
    }

    if (videoState.cycleSound === "marimba-boop") {
      this.synthesizeMarimbaBoop(stepIndex, dest, now);
    } else if (videoState.cycleSound === "zen-chime") {
      this.synthesizeZenChime(dest, now);
    } else if (videoState.cycleSound === "digital-blip") {
      this.synthesizeDigitalBlip(dest, now);
    } else {
      // Default: Soft Ambient Piano
      this.synthesizeSoftPiano(stepIndex, dest, now);
    }
  }

  // Soft Ambient Piano with warm pentatonic notes & prolonged lush sustain
  synthesizeSoftPiano(stepIndex, dest, now) {
    // Pentatonic scale: C4, E4, G4, B4, C5 (warm, elegant clinical progression)
    const pentatonicFreqs = [261.63, 329.63, 392.00, 493.88, 523.25];
    const freq = pentatonicFreqs[stepIndex % pentatonicFreqs.length];

    const osc1 = this.ctx.createOscillator();
    const osc2 = this.ctx.createOscillator();
    const noteGain = this.ctx.createGain();

    // Biquad Lowpass filter for buttery soft warmth (cuts any harsh high frequencies)
    const filter = this.ctx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(800, now);
    filter.frequency.exponentialRampToValueAtTime(320, now + 1.2);

    osc1.type = "sine";
    osc1.frequency.setValueAtTime(freq, now);

    // Warm octave overtone at very gentle amplitude
    osc2.type = "sine";
    osc2.frequency.setValueAtTime(freq * 2, now);

    // Gentle 45ms attack linear ramp (eliminates clicks/harsh transients), prolonged 1.4s decay
    noteGain.gain.setValueAtTime(0, now);
    noteGain.gain.linearRampToValueAtTime(0.20, now + 0.045);
    noteGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.4);

    osc1.connect(noteGain);
    osc2.connect(noteGain);
    noteGain.connect(filter);
    filter.connect(dest);

    osc1.start(now);
    osc2.start(now);
    osc1.stop(now + 1.45);
    osc2.stop(now + 1.45);
  }

  // Warm Acoustic Marimba / Soft Boop (velvet mallet tone with smooth decay)
  synthesizeMarimbaBoop(stepIndex, dest, now) {
    const freqs = [261.63, 329.63, 392.00, 493.88, 523.25];
    const freq = freqs[stepIndex % freqs.length];

    const osc = this.ctx.createOscillator();
    const noteGain = this.ctx.createGain();
    const filter = this.ctx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(650, now);

    osc.type = "triangle";
    osc.frequency.setValueAtTime(freq * 1.02, now);
    osc.frequency.exponentialRampToValueAtTime(freq, now + 0.05);

    noteGain.gain.setValueAtTime(0, now);
    noteGain.gain.linearRampToValueAtTime(0.22, now + 0.035);
    noteGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.1);

    osc.connect(noteGain);
    noteGain.connect(filter);
    filter.connect(dest);

    osc.start(now);
    osc.stop(now + 1.15);
  }

  // Gentle Zen Chime (Soft bell with 1.8s shimmering tail)
  synthesizeZenChime(dest, now) {
    const osc = this.ctx.createOscillator();
    const noteGain = this.ctx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(783.99, now); // G5 (velvety soft frequency)

    noteGain.gain.setValueAtTime(0, now);
    noteGain.gain.linearRampToValueAtTime(0.18, now + 0.05);
    noteGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.8);

    osc.connect(noteGain);
    noteGain.connect(dest);

    osc.start(now);
    osc.stop(now + 1.85);
  }

  // Subtle Water Drop / Pop
  synthesizeDigitalBlip(dest, now) {
    const osc = this.ctx.createOscillator();
    const noteGain = this.ctx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(600, now);
    osc.frequency.exponentialRampToValueAtTime(320, now + 0.06);

    noteGain.gain.setValueAtTime(0, now);
    noteGain.gain.linearRampToValueAtTime(0.18, now + 0.02);
    noteGain.gain.exponentialRampToValueAtTime(0.0001, now + 0.45);

    osc.connect(noteGain);
    noteGain.connect(dest);

    osc.start(now);
    osc.stop(now + 0.48);
  }

  // Answer Reveal Chime / Chord (triumphant major chord arpeggio)
  playRevealSound(destNode = null) {
    if (videoState.isMuted || videoState.revealSound === "mute") return;
    this.init();
    const dest = destNode || this.masterGain;
    const now = this.ctx.currentTime;

    if (videoState.revealSound === "piano-resolve") {
      // Soft resolved chord: C4, G4, C5 together
      [261.63, 392.00, 523.25].forEach((freq) => {
        const osc = this.ctx.createOscillator();
        const noteGain = this.ctx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(freq, now);
        noteGain.gain.setValueAtTime(0, now);
        noteGain.gain.linearRampToValueAtTime(0.2, now + 0.02);
        noteGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.2);
        osc.connect(noteGain);
        noteGain.connect(dest);
        osc.start(now);
        osc.stop(now + 1.25);
      });
      return;
    }

    if (videoState.revealSound === "gentle-bell") {
      const osc = this.ctx.createOscillator();
      const noteGain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(1046.5, now);
      noteGain.gain.setValueAtTime(0, now);
      noteGain.gain.linearRampToValueAtTime(0.35, now + 0.015);
      noteGain.gain.exponentialRampToValueAtTime(0.0001, now + 1.0);
      osc.connect(noteGain);
      noteGain.connect(dest);
      osc.start(now);
      osc.stop(now + 1.05);
      return;
    }

    // Default: Success Chime Major Triad Arpeggio (C5, E5, G5, C6)
    const chord = [523.25, 659.25, 783.99, 1046.50];
    chord.forEach((freq, idx) => {
      const noteTime = now + idx * 0.06;
      const osc = this.ctx.createOscillator();
      const noteGain = this.ctx.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, noteTime);

      noteGain.gain.setValueAtTime(0, noteTime);
      noteGain.gain.linearRampToValueAtTime(0.25, noteTime + 0.015);
      noteGain.gain.exponentialRampToValueAtTime(0.0001, noteTime + 0.85);

      osc.connect(noteGain);
      noteGain.connect(dest);

      osc.start(noteTime);
      osc.stop(noteTime + 0.9);
    });
  }

  // Render full deterministic stereo 48kHz AudioBuffer offline (for fast WebCodecs MP4 export)
  async renderOfflineAudioBuffer(q, totalDuration, sampleRate = 48000) {
    const numFrames = Math.max(sampleRate, Math.ceil(totalDuration * sampleRate));
    const offlineCtx = new OfflineAudioContext(2, numFrames, sampleRate);
    const masterGain = offlineCtx.createGain();
    const vol = videoState.isMuted ? 0 : Math.max(0, Math.min(1, videoState.volume ?? 0.45));
    masterGain.gain.setValueAtTime(vol, 0);
    masterGain.connect(offlineCtx.destination);

    // Static Reel mode or muted -> clean silent stereo AAC track (required for smooth IG Reels ingestion)
    if (videoState.videoMode === "static" || videoState.isMuted || vol <= 0) {
      return await offlineCtx.startRendering();
    }

    const prevCtx = this.ctx;
    this.ctx = offlineCtx;
    try {
      const readingEnd = videoState.readingDuration;
      const cyclingStart = readingEnd + 0.5;
      const cyclingEnd = cyclingStart + videoState.cyclingDuration;
      const revealStart = cyclingEnd + (videoState.postCyclingPause || 2.0);
      const optionsCount = (q && q.options ? q.options.length : 4) || 4;
      const stepDuration = videoState.cyclingDuration / Math.max(1, optionsCount);

      if (videoState.cycleSound !== "mute") {
        for (let step = 0; step < optionsCount; step++) {
          const t = cyclingStart + step * stepDuration;
          if (t >= totalDuration) break;
          if (videoState.cycleSound === "custom" && videoState.customCycleBuffer) {
            try {
              const src = offlineCtx.createBufferSource();
              src.buffer = videoState.customCycleBuffer;
              src.connect(masterGain);
              src.start(t);
            } catch (e) {}
          } else if (videoState.cycleSound === "marimba-boop") {
            this.synthesizeMarimbaBoop(step, masterGain, t);
          } else if (videoState.cycleSound === "zen-chime") {
            this.synthesizeZenChime(masterGain, t);
          } else if (videoState.cycleSound === "digital-blip") {
            this.synthesizeDigitalBlip(masterGain, t);
          } else {
            this.synthesizeSoftPiano(step, masterGain, t);
          }
        }
      }

      if (videoState.revealSound !== "mute" && revealStart < totalDuration) {
        this.scheduleRevealSoundAt(masterGain, revealStart);
      }
    } finally {
      this.ctx = prevCtx;
    }

    return await offlineCtx.startRendering();
  }

  scheduleRevealSoundAt(dest, t) {
    if (videoState.revealSound === "piano-resolve") {
      [261.63, 392.0, 523.25].forEach((freq) => {
        const osc = this.ctx.createOscillator();
        const noteGain = this.ctx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(freq, t);
        noteGain.gain.setValueAtTime(0, t);
        noteGain.gain.linearRampToValueAtTime(0.2, t + 0.02);
        noteGain.gain.exponentialRampToValueAtTime(0.0001, t + 1.2);
        osc.connect(noteGain);
        noteGain.connect(dest);
        osc.start(t);
        osc.stop(t + 1.25);
      });
      return;
    }
    if (videoState.revealSound === "gentle-bell") {
      const osc = this.ctx.createOscillator();
      const noteGain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(1046.5, t);
      noteGain.gain.setValueAtTime(0, t);
      noteGain.gain.linearRampToValueAtTime(0.35, t + 0.015);
      noteGain.gain.exponentialRampToValueAtTime(0.0001, t + 1.0);
      osc.connect(noteGain);
      noteGain.connect(dest);
      osc.start(t);
      osc.stop(t + 1.05);
      return;
    }
    const chord = [523.25, 659.25, 783.99, 1046.5];
    chord.forEach((freq, idx) => {
      const noteTime = t + idx * 0.06;
      const osc = this.ctx.createOscillator();
      const noteGain = this.ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, noteTime);
      noteGain.gain.setValueAtTime(0, noteTime);
      noteGain.gain.linearRampToValueAtTime(0.25, noteTime + 0.015);
      noteGain.gain.exponentialRampToValueAtTime(0.0001, noteTime + 0.85);
      osc.connect(noteGain);
      noteGain.connect(dest);
      osc.start(noteTime);
      osc.stop(noteTime + 0.9);
    });
  }
}

const studioAudio = new StudioAudioEngine();

const VIDEO_PREFS_KEY = "medbank_reel_prefs_v1";
const VERCEL_PASSCODE_KEY = "medbank_vercel_passcode_v1";
const igServerState = {
  checked: false,
  mode: "offline", // "vercel" | "local" | "offline"
  online: false,
  ffmpegAvailable: false,
  ffmpegPath: "",
  blobConfigured: false,
  passcodeRequired: false,
  igConfigured: false,
  igUsername: "",
  shareToFeed: true,
  saveLocalCopy: true,
};

function getStoredPasscode() {
  try {
    return localStorage.getItem(VERCEL_PASSCODE_KEY) || "";
  } catch (e) {
    return "";
  }
}

function setStoredPasscode(val) {
  try {
    if (val) localStorage.setItem(VERCEL_PASSCODE_KEY, val);
    else localStorage.removeItem(VERCEL_PASSCODE_KEY);
  } catch (e) {}
}

function loadVideoPreferences() {
  try {
    const raw = localStorage.getItem(VIDEO_PREFS_KEY);
    if (!raw) return;
    const prefs = JSON.parse(raw);
    if (!prefs || typeof prefs !== "object") return;

    const videoKeys = [
      "videoMode",
      "staticDuration",
      "staticLayout",
      "cyclingDuration",
      "postCyclingPause",
      "revealDuration",
      "wpm",
      "explanationFontSize",
      "readingStyle",
      "deliberationStyle",
      "cycleSound",
      "revealSound",
      "volume",
      "revealMode",
      "showPausePrompt",
      "pausePromptText",
      "showCommentPrompt",
      "commentPromptText",
    ];
    videoKeys.forEach((k) => {
      if (prefs[k] !== undefined && prefs[k] !== null) {
        if (k === "cycleSound" && prefs[k] === "custom") return;
        videoState[k] = prefs[k];
      }
    });

    if (typeof instaState !== "undefined") {
      const instaKeys = [
        "theme",
        "font",
        "handle",
        "websiteUrl",
        "scenarioFontSize",
        "optionsFontSize",
        "explanationFontSize",
      ];
      instaKeys.forEach((k) => {
        if (prefs[k] !== undefined && prefs[k] !== null) {
          instaState[k] = prefs[k];
        }
      });
    }

    if (typeof prefs.shareToFeed === "boolean") {
      igServerState.shareToFeed = prefs.shareToFeed;
    }
  } catch (err) {
    console.warn("Could not load saved Reel preferences:", err);
  }
}

function saveVideoPreferences() {
  try {
    const prefs = {
      videoMode: videoState.videoMode,
      staticDuration: videoState.staticDuration,
      staticLayout: videoState.staticLayout,
      cyclingDuration: videoState.cyclingDuration,
      postCyclingPause: videoState.postCyclingPause,
      revealDuration: videoState.revealDuration,
      wpm: videoState.wpm,
      explanationFontSize: videoState.explanationFontSize,
      readingStyle: videoState.readingStyle,
      deliberationStyle: videoState.deliberationStyle,
      cycleSound: videoState.cycleSound === "custom" ? "soft-piano" : videoState.cycleSound,
      revealSound: videoState.revealSound,
      volume: videoState.volume,
      revealMode: videoState.revealMode,
      showPausePrompt: videoState.showPausePrompt,
      pausePromptText: videoState.pausePromptText,
      showCommentPrompt: videoState.showCommentPrompt,
      commentPromptText: videoState.commentPromptText,
      shareToFeed: igServerState.shareToFeed,
    };
    if (typeof instaState !== "undefined") {
      prefs.theme = instaState.theme;
      prefs.font = instaState.font;
      prefs.handle = instaState.handle;
      prefs.websiteUrl = instaState.websiteUrl;
      prefs.scenarioFontSize = instaState.scenarioFontSize;
      prefs.optionsFontSize = instaState.optionsFontSize;
    }
    localStorage.setItem(VIDEO_PREFS_KEY, JSON.stringify(prefs));
  } catch (err) {
    console.warn("Could not save Reel preferences:", err);
  }
}

function updateCaptionCharCount() {
  const textarea = document.getElementById("video-caption-textarea");
  const counter = document.getElementById("video-caption-char-count");
  if (!textarea || !counter) return;
  const len = textarea.value.length;
  counter.textContent = `${len.toLocaleString()} / 2,200`;
  counter.style.color = len > 2200 ? "#f87171" : "var(--text-tertiary)";
}

function populateVideoCaption(q) {
  const textarea = document.getElementById("video-caption-textarea");
  if (!textarea || !q) return;
  if (typeof buildInstagramCaption === "function") {
    textarea.value = buildInstagramCaption(q);
    updateCaptionCharCount();
  }
}

function applyVideoModeUI() {
  const isStatic = videoState.videoMode === "static";
  const animBtn = document.getElementById("video-mode-animated-btn");
  const staticBtn = document.getElementById("video-mode-static-btn");
  const staticBox = document.getElementById("video-static-settings");
  const animControls = document.getElementById("video-animated-only-controls");
  const delibWrapper = document.getElementById("video-deliberation-format-wrapper");

  if (animBtn) animBtn.classList.toggle("active", !isStatic);
  if (staticBtn) staticBtn.classList.toggle("active", isStatic);
  if (staticBox) staticBox.style.display = isStatic ? "block" : "none";
  if (animControls) animControls.style.display = isStatic ? "none" : "grid";
  if (delibWrapper) delibWrapper.style.display = isStatic ? "none" : "block";

  const durSlider = document.getElementById("video-static-duration-slider");
  if (durSlider) durSlider.value = videoState.staticDuration;
  const durVal = document.getElementById("val-video-static-duration");
  if (durVal) durVal.textContent = videoState.staticDuration;

  const layoutSel = document.getElementById("video-static-layout-select");
  if (layoutSel) layoutSel.value = videoState.staticLayout;
}

// --- Lifecycle & Initialization ---
document.addEventListener("DOMContentLoaded", () => {
  loadVideoPreferences();
  initStudioTabs();
  initVideoControls();
  initVideoThemeGrid();
  initIgDirectSetupUI();
  checkLocalServerStatus();
});

// Switch between Static Carousel and Animated Reel Video tabs
function switchStudioTab(tabName, opts = {}) {
  const carouselTabBtn = document.getElementById("studio-tab-carousel");
  const videoTabBtn = document.getElementById("studio-tab-video");
  const carouselPane = document.getElementById("carousel-tab-pane");
  const videoPane = document.getElementById("video-tab-pane");

  if (!carouselTabBtn || !videoTabBtn) return;

  if (tabName === "video") {
    videoTabBtn.classList.add("active");
    carouselTabBtn.classList.remove("active");
    if (carouselPane) carouselPane.style.display = "none";
    if (videoPane) videoPane.style.display = "block";
    syncVideoControlsWithInstaState();
    recalculateVideoTimeline();
    renderVideoFrameAt(0);
    if (opts.autoPlay !== false) {
      playVideoPlayback();
    }
    checkLocalServerStatus();
  } else {
    carouselTabBtn.classList.add("active");
    videoTabBtn.classList.remove("active");
    if (carouselPane) carouselPane.style.display = "block";
    if (videoPane) videoPane.style.display = "none";
    pauseVideoPlayback();
  }
}

// Tab Switcher (Static Carousel vs Animated Video)
function initStudioTabs() {
  const carouselTabBtn = document.getElementById("studio-tab-carousel");
  const videoTabBtn = document.getElementById("studio-tab-video");

  if (!carouselTabBtn || !videoTabBtn) return;

  carouselTabBtn.addEventListener("click", () => switchStudioTab("carousel"));
  videoTabBtn.addEventListener("click", () => switchStudioTab("video", { autoPlay: true }));
}

// Populate Theme Grid in Video Studio
function initVideoThemeGrid() {
  const grid = document.getElementById("video-theme-grid");
  if (!grid || typeof INSTA_THEMES === "undefined") return;

  grid.innerHTML = "";
  INSTA_THEMES.forEach((theme) => {
    const swatch = document.createElement("div");
    swatch.className = `theme-swatch${theme.id === instaState.theme ? " active" : ""}`;
    swatch.style.background = theme.gradient;
    swatch.title = theme.label;
    swatch.dataset.themeId = theme.id;
    swatch.addEventListener("click", () => {
      grid.querySelectorAll(".theme-swatch").forEach((s) => s.classList.remove("active"));
      swatch.classList.add("active");
      instaState.theme = theme.id;

      // Sync carousel swatches too
      const carGrid = document.getElementById("insta-theme-grid");
      if (carGrid) {
        carGrid.querySelectorAll(".theme-swatch").forEach((s) => {
          s.classList.toggle("active", s.dataset.themeId === theme.id);
        });
      }
      if (typeof rebuildAllSlides === "function") rebuildAllSlides();
      saveVideoPreferences();
      renderVideoFrameAt(videoState.currentTime);
    });
    grid.appendChild(swatch);
  });
}

// Sync controls when opening Video Studio
function syncVideoControlsWithInstaState() {
  videoState.activeQuestion = instaState.activeQuestion;

  const fontSelect = document.getElementById("video-font-select");
  if (fontSelect) fontSelect.value = instaState.font;

  const handleInput = document.getElementById("video-handle-input");
  if (handleInput) handleInput.value = instaState.handle;

  const webInput = document.getElementById("video-website-input");
  if (webInput) webInput.value = instaState.websiteUrl;

  const scenarioSlider = document.getElementById("video-size-scenario");
  if (scenarioSlider) {
    scenarioSlider.value = instaState.scenarioFontSize;
    const label = document.getElementById("val-video-size-scenario");
    if (label) label.textContent = instaState.scenarioFontSize;
  }

  const optionsSlider = document.getElementById("video-size-options");
  if (optionsSlider) {
    optionsSlider.value = instaState.optionsFontSize;
    const label = document.getElementById("val-video-size-options");
    if (label) label.textContent = instaState.optionsFontSize;
  }

  const explSlider = document.getElementById("video-size-explanation");
  if (explSlider) {
    const curVal = videoState.explanationFontSize || instaState.explanationFontSize || 24;
    videoState.explanationFontSize = curVal;
    explSlider.value = curVal;
    const label = document.getElementById("val-video-size-explanation");
    if (label) label.textContent = curVal;
  }

  const readStyleSel = document.getElementById("video-reading-style-select");
  if (readStyleSel) readStyleSel.value = videoState.readingStyle;

  const delibStyleSel = document.getElementById("video-deliberation-style-select");
  if (delibStyleSel) delibStyleSel.value = videoState.deliberationStyle;

  const speedSlider = document.getElementById("video-speed-slider");
  if (speedSlider) {
    speedSlider.value = videoState.wpm;
    const label = document.getElementById("val-video-speed");
    if (label) label.textContent = videoState.wpm;
  }

  const cycleDurSlider = document.getElementById("video-cycling-duration-slider");
  if (cycleDurSlider) {
    cycleDurSlider.value = videoState.cyclingDuration;
    const label = document.getElementById("val-video-cycling-duration");
    if (label) label.textContent = Number(videoState.cyclingDuration).toFixed(1);
  }

  const postCycleSlider = document.getElementById("video-post-cycle-pause-slider");
  if (postCycleSlider) {
    postCycleSlider.value = videoState.postCyclingPause;
    const label = document.getElementById("val-video-post-cycle-pause");
    if (label) label.textContent = Number(videoState.postCyclingPause).toFixed(1);
  }

  const cycleSoundSel = document.getElementById("video-cycling-sound-select");
  if (cycleSoundSel) cycleSoundSel.value = videoState.cycleSound;

  const revealSoundSel = document.getElementById("video-reveal-sound-select");
  if (revealSoundSel) revealSoundSel.value = videoState.revealSound;

  const volSlider = document.getElementById("video-volume-slider");
  if (volSlider) {
    const volPct = Math.round((videoState.volume ?? 0.45) * 100);
    volSlider.value = volPct;
    const label = document.getElementById("val-video-volume");
    if (label) label.textContent = volPct;
  }

  const revealModeSel = document.getElementById("video-reveal-mode-select");
  if (revealModeSel) revealModeSel.value = videoState.revealMode;

  const revealDurSlider = document.getElementById("video-reveal-duration-slider");
  if (revealDurSlider) {
    revealDurSlider.value = videoState.revealDuration;
    const label = document.getElementById("val-video-reveal-duration");
    if (label) label.textContent = Number(videoState.revealDuration).toFixed(1);
  }

  const togglePause = document.getElementById("video-toggle-pause-prompt");
  if (togglePause) togglePause.checked = Boolean(videoState.showPausePrompt);

  const pauseText = document.getElementById("video-pause-prompt-text");
  if (pauseText) pauseText.value = videoState.pausePromptText || "";

  const toggleComment = document.getElementById("video-toggle-comment-prompt");
  if (toggleComment) toggleComment.checked = Boolean(videoState.showCommentPrompt);

  const commentText = document.getElementById("video-comment-prompt-text");
  if (commentText) commentText.value = videoState.commentPromptText || "";

  const shareFeedToggle = document.getElementById("video-share-to-feed-toggle");
  if (shareFeedToggle) shareFeedToggle.checked = Boolean(igServerState.shareToFeed);

  applyVideoModeUI();

  // Update active swatch
  const grid = document.getElementById("video-theme-grid");
  if (grid) {
    grid.querySelectorAll(".theme-swatch").forEach((s) => {
      s.classList.toggle("active", s.dataset.themeId === instaState.theme);
    });
  }
}

// --- Video Studio Controls Listeners ---
function initVideoControls() {
  // Play / Pause Viewport Click
  const viewport = document.getElementById("video-viewport");
  if (viewport) {
    viewport.addEventListener("click", () => {
      studioAudio.init();
      if (videoState.isPlaying) {
        pauseVideoPlayback();
      } else {
        playVideoPlayback();
      }
    });
  }

  // Play / Pause Button
  const playBtn = document.getElementById("video-play-pause-btn");
  if (playBtn) {
    playBtn.addEventListener("click", () => {
      studioAudio.init();
      if (videoState.isPlaying) {
        pauseVideoPlayback();
      } else {
        playVideoPlayback();
      }
    });
  }

  // Restart Button
  const restartBtn = document.getElementById("video-restart-btn");
  if (restartBtn) {
    restartBtn.addEventListener("click", () => {
      studioAudio.init();
      resetVideoToStart();
      playVideoPlayback();
    });
  }

  // Scrubber Slider
  const scrubber = document.getElementById("video-scrubber");
  if (scrubber) {
    scrubber.addEventListener("input", (e) => {
      const pct = parseFloat(e.target.value);
      videoState.currentTime = (pct / 100) * videoState.totalDuration;
      videoState.lastSoundStep = -1;
      videoState.revealSoundPlayed = videoState.currentTime >= (videoState.readingDuration + 0.5 + videoState.cyclingDuration + (videoState.postCyclingPause || 2.0));
      renderVideoFrameAt(videoState.currentTime);
      updateScrubberUI();
    });
  }

  // Mute / Unmute Button
  const muteBtn = document.getElementById("video-mute-btn");
  if (muteBtn) {
    muteBtn.addEventListener("click", () => {
      videoState.isMuted = !videoState.isMuted;
      muteBtn.innerHTML = videoState.isMuted
        ? '<i class="fa-solid fa-volume-xmark" style="color: var(--danger);"></i>'
        : '<i class="fa-solid fa-volume-high"></i>';
      studioAudio.setVolume(videoState.volume);
    });
  }

  // Reading Style Select
  const styleSelect = document.getElementById("video-reading-style-select");
  if (styleSelect) {
    styleSelect.addEventListener("change", (e) => {
      videoState.readingStyle = e.target.value;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Reading Speed Slider (WPM)
  const speedSlider = document.getElementById("video-speed-slider");
  if (speedSlider) {
    speedSlider.addEventListener("input", (e) => {
      const val = parseInt(e.target.value);
      videoState.wpm = val;
      const valLabel = document.getElementById("val-video-speed");
      if (valLabel) valLabel.textContent = val;

      const descLabel = document.getElementById("val-video-speed-label");
      if (descLabel) {
        if (val < 250) descLabel.textContent = "Relaxed Pace";
        else if (val <= 330) descLabel.textContent = "Optimal Flow & High Retention";
        else descLabel.textContent = "Ultra Fast / High Energy";
      }

      recalculateVideoTimeline();
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Deliberation Format Select
  const delibSelect = document.getElementById("video-deliberation-style-select");
  if (delibSelect) {
    delibSelect.addEventListener("change", (e) => {
      videoState.deliberationStyle = e.target.value;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Option Cycling Duration Slider (Deliberation Timer)
  const cycleDurSlider = document.getElementById("video-cycling-duration-slider");
  if (cycleDurSlider) {
    cycleDurSlider.addEventListener("input", (e) => {
      const val = parseFloat(e.target.value);
      videoState.cyclingDuration = val;
      const label = document.getElementById("val-video-cycling-duration");
      if (label) label.textContent = val.toFixed(1);

      const desc = document.getElementById("val-video-cycling-desc");
      if (desc) {
        const q = videoState.activeQuestion || instaState.activeQuestion;
        const optCount = (q && q.options ? q.options.length : 4) || 4;
        desc.textContent = `${(val / optCount).toFixed(1)}s deliberate review per option (1 pass only)`;
      }

      recalculateVideoTimeline();
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Post-Cycle Suspense Pause Slider
  const postCycleSlider = document.getElementById("video-post-cycle-pause-slider");
  if (postCycleSlider) {
    postCycleSlider.addEventListener("input", (e) => {
      const val = parseFloat(e.target.value);
      videoState.postCyclingPause = val;
      const label = document.getElementById("val-video-post-cycle-pause");
      if (label) label.textContent = val.toFixed(1);
      recalculateVideoTimeline();
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Option Cycling Sound Select
  const soundSelect = document.getElementById("video-cycling-sound-select");
  const customSoundRow = document.getElementById("video-custom-sound-row");
  if (soundSelect) {
    soundSelect.addEventListener("change", (e) => {
      videoState.cycleSound = e.target.value;
      if (customSoundRow) {
        customSoundRow.style.display = e.target.value === "custom" ? "block" : "none";
      }
      studioAudio.init();
      studioAudio.playCycleSound(0);
    });
  }

  // Test Sound Button
  const testSoundBtn = document.getElementById("video-test-sound-btn");
  if (testSoundBtn) {
    testSoundBtn.addEventListener("click", () => {
      studioAudio.init();
      studioAudio.playCycleSound(1);
    });
  }

  // Custom Audio File Input
  const customAudioInput = document.getElementById("video-custom-audio-file");
  if (customAudioInput) {
    customAudioInput.addEventListener("change", async (e) => {
      const file = e.target.files[0];
      if (!file) return;

      const filenameLabel = document.getElementById("video-custom-audio-filename");
      if (filenameLabel) filenameLabel.textContent = `Loading ${file.name}...`;

      try {
        studioAudio.init();
        const arrayBuffer = await file.arrayBuffer();
        studioAudio.ctx.decodeAudioData(
          arrayBuffer,
          (decodedBuffer) => {
            videoState.customCycleBuffer = decodedBuffer;
            videoState.customCycleFileName = file.name;
            if (filenameLabel) filenameLabel.textContent = `✓ Loaded: ${file.name}`;
            studioAudio.playCycleSound(0);
          },
          (err) => {
            console.error("Audio decode error:", err);
            if (filenameLabel) filenameLabel.textContent = "Error decoding audio file.";
          }
        );
      } catch (err) {
        console.error("Audio file read error:", err);
      }
    });
  }

  // Reveal Sound Select
  const revealSoundSelect = document.getElementById("video-reveal-sound-select");
  if (revealSoundSelect) {
    revealSoundSelect.addEventListener("change", (e) => {
      videoState.revealSound = e.target.value;
      studioAudio.init();
      studioAudio.playRevealSound();
    });
  }

  // Volume Slider
  const volSlider = document.getElementById("video-volume-slider");
  if (volSlider) {
    volSlider.addEventListener("input", (e) => {
      const val = parseInt(e.target.value);
      videoState.volume = val / 100;
      const label = document.getElementById("val-video-volume");
      if (label) label.textContent = val;
      studioAudio.setVolume(videoState.volume);
    });
  }

  // Reveal Ending Mode Select
  const revealModeSelect = document.getElementById("video-reveal-mode-select");
  if (revealModeSelect) {
    revealModeSelect.addEventListener("change", (e) => {
      videoState.revealMode = e.target.value;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Reveal Duration Slider
  const revealDurSlider = document.getElementById("video-reveal-duration-slider");
  if (revealDurSlider) {
    revealDurSlider.addEventListener("input", (e) => {
      const val = parseFloat(e.target.value);
      videoState.revealDuration = val;
      const label = document.getElementById("val-video-reveal-duration");
      if (label) label.textContent = val.toFixed(1);
      recalculateVideoTimeline();
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Font Select
  const fontSelect = document.getElementById("video-font-select");
  if (fontSelect) {
    fontSelect.addEventListener("change", (e) => {
      instaState.font = e.target.value;
      const carFont = document.getElementById("insta-font-select");
      if (carFont) carFont.value = e.target.value;
      if (typeof rebuildAllSlides === "function") rebuildAllSlides();
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Handle Input
  const handleInput = document.getElementById("video-handle-input");
  if (handleInput) {
    handleInput.addEventListener("input", (e) => {
      instaState.handle = e.target.value || "@medqstudios";
      const carHandle = document.getElementById("insta-handle-input");
      if (carHandle) carHandle.value = instaState.handle;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Website Input
  const webInput = document.getElementById("video-website-input");
  if (webInput) {
    webInput.addEventListener("input", (e) => {
      instaState.websiteUrl = e.target.value.trim() || "www.medqstudios.com";
      const carWeb = document.getElementById("insta-website-input");
      if (carWeb) carWeb.value = instaState.websiteUrl;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Scenario Font Size
  const sizeScen = document.getElementById("video-size-scenario");
  if (sizeScen) {
    sizeScen.addEventListener("input", (e) => {
      const val = parseInt(e.target.value);
      instaState.scenarioFontSize = val;
      const label = document.getElementById("val-video-size-scenario");
      if (label) label.textContent = val;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Options Font Size
  const sizeOpt = document.getElementById("video-size-options");
  if (sizeOpt) {
    sizeOpt.addEventListener("input", (e) => {
      const val = parseInt(e.target.value);
      instaState.optionsFontSize = val;
      const label = document.getElementById("val-video-size-options");
      if (label) label.textContent = val;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Explanation Font Size
  const sizeExpl = document.getElementById("video-size-explanation");
  if (sizeExpl) {
    sizeExpl.addEventListener("input", (e) => {
      const val = parseInt(e.target.value);
      videoState.explanationFontSize = val;
      instaState.explanationFontSize = val;
      const label = document.getElementById("val-video-size-explanation");
      if (label) label.textContent = val;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Toggle Pause Prompt
  const togglePause = document.getElementById("video-toggle-pause-prompt");
  if (togglePause) {
    togglePause.addEventListener("change", (e) => {
      videoState.showPausePrompt = e.target.checked;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Pause Prompt Text Input
  const pauseTextInput = document.getElementById("video-pause-prompt-text");
  if (pauseTextInput) {
    pauseTextInput.addEventListener("input", (e) => {
      videoState.pausePromptText = e.target.value;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Toggle Comment Prompt
  const toggleComment = document.getElementById("video-toggle-comment-prompt");
  if (toggleComment) {
    toggleComment.addEventListener("change", (e) => {
      videoState.showCommentPrompt = e.target.checked;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Comment Prompt Text Input
  const commentTextInput = document.getElementById("video-comment-prompt-text");
  if (commentTextInput) {
    commentTextInput.addEventListener("input", (e) => {
      videoState.commentPromptText = e.target.value;
      renderVideoFrameAt(videoState.currentTime);
    });
  }

  // Reel Mode Toggle: Animated vs Static (No Animations)
  const modeAnimBtn = document.getElementById("video-mode-animated-btn");
  const modeStaticBtn = document.getElementById("video-mode-static-btn");
  if (modeAnimBtn) {
    modeAnimBtn.addEventListener("click", () => {
      videoState.videoMode = "animated";
      applyVideoModeUI();
      saveVideoPreferences();
      recalculateVideoTimeline();
      renderVideoFrameAt(videoState.currentTime);
    });
  }
  if (modeStaticBtn) {
    modeStaticBtn.addEventListener("click", () => {
      videoState.videoMode = "static";
      applyVideoModeUI();
      saveVideoPreferences();
      recalculateVideoTimeline();
      renderVideoFrameAt(0);
    });
  }

  // Static Reel Duration Slider (3-30s)
  const staticDurSlider = document.getElementById("video-static-duration-slider");
  if (staticDurSlider) {
    staticDurSlider.addEventListener("input", (e) => {
      const val = parseInt(e.target.value, 10) || 7;
      videoState.staticDuration = Math.max(3, Math.min(30, val));
      const label = document.getElementById("val-video-static-duration");
      if (label) label.textContent = videoState.staticDuration;
      recalculateVideoTimeline();
      renderVideoFrameAt(0);
    });
  }

  // Static Reel Content Layout Select
  const staticLayoutSel = document.getElementById("video-static-layout-select");
  if (staticLayoutSel) {
    staticLayoutSel.addEventListener("change", (e) => {
      videoState.staticLayout = e.target.value;
      renderVideoFrameAt(0);
    });
  }

  // Caption character counter
  const captionTextarea = document.getElementById("video-caption-textarea");
  if (captionTextarea) {
    captionTextarea.addEventListener("input", updateCaptionCharCount);
  }

  // Share to Feed Toggle
  const shareFeedToggle = document.getElementById("video-share-to-feed-toggle");
  if (shareFeedToggle) {
    shareFeedToggle.addEventListener("change", (e) => {
      igServerState.shareToFeed = e.target.checked;
      saveVideoPreferences();
    });
  }

  // Reset Caption Button
  const resetCaptionBtn = document.getElementById("video-reset-caption-btn");
  if (resetCaptionBtn) {
    resetCaptionBtn.addEventListener("click", () => {
      const q = videoState.activeQuestion || instaState.activeQuestion;
      if (q) populateVideoCaption(q);
    });
  }

  // Copy Caption Button (inside Video Tab)
  const copyCaptionBtn = document.getElementById("video-copy-caption-btn");
  if (copyCaptionBtn) {
    copyCaptionBtn.addEventListener("click", () => {
      const captionEl = document.getElementById("video-caption-textarea");
      const text = captionEl ? captionEl.value.trim() : "";
      if (typeof copyInstagramCaption === "function") {
        copyInstagramCaption(text);
      }
    });
  }

  // Auto-save any Reel preference changes in the Video Controls panel
  const controlsPanel = document.querySelector(".video-controls-section");
  if (controlsPanel) {
    let saveTimer = null;
    const scheduleSave = (e) => {
      if (e.target && (e.target.id === "video-caption-textarea" || e.target.id === "video-custom-audio-file")) {
        return;
      }
      clearTimeout(saveTimer);
      saveTimer = setTimeout(() => saveVideoPreferences(), 120);
    };
    controlsPanel.addEventListener("change", scheduleSave);
    controlsPanel.addEventListener("input", scheduleSave);
  }

  // Video Export Button (Saves IG-ready MP4)
  const exportBtn = document.getElementById("video-export-btn");
  if (exportBtn) {
    exportBtn.addEventListener("click", () => {
      exportAnimatedVideo();
    });
  }

  // Direct Publish to Instagram Button
  const publishBtn = document.getElementById("video-publish-ig-btn");
  if (publishBtn) {
    publishBtn.addEventListener("click", () => {
      publishReelToInstagram();
    });
  }
}

// --- Timeline Calculation ---
function recalculateVideoTimeline() {
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) return;

  if (videoState.videoMode === "static") {
    videoState.totalDuration = Math.max(3, Math.min(30, Number(videoState.staticDuration) || 7));
    if (videoState.currentTime > videoState.totalDuration) {
      videoState.currentTime = 0;
    }
    updateScrubberUI();
    return;
  }

  const words = (q.scenario || "").split(/\s+/).filter(Boolean);
  const wordCount = Math.max(1, words.length);

  // Question reading duration based on WPM:
  // e.g. 25 words at 300 WPM = (25 / 300) * 60 = 5.0 seconds
  const rawReadingTime = (wordCount / videoState.wpm) * 60;
  videoState.readingDuration = Math.max(3.2, Math.min(12.0, rawReadingTime));

  const pauseBeforeOptions = 0.5;
  const postPause = typeof videoState.postCyclingPause === "number" ? videoState.postCyclingPause : 2.0;
  videoState.totalDuration = videoState.readingDuration + pauseBeforeOptions + videoState.cyclingDuration + postPause + videoState.revealDuration;

  updateScrubberUI();
}

function updateScrubberUI() {
  const scrubber = document.getElementById("video-scrubber");
  const timeDisplay = document.getElementById("video-time-display");
  const phaseBadge = document.getElementById("video-phase-badge");

  const cur = Math.max(0, Math.min(videoState.totalDuration, videoState.currentTime));
  const tot = videoState.totalDuration;

  if (scrubber) {
    scrubber.value = ((cur / tot) * 100).toFixed(1);
  }

  if (timeDisplay) {
    timeDisplay.textContent = `${cur.toFixed(1)}s / ${tot.toFixed(1)}s`;
  }

  if (phaseBadge) {
    if (videoState.videoMode === "static") {
      phaseBadge.textContent = `🖼️ Static Reel (${tot.toFixed(0)}s • No Animations)`;
      phaseBadge.style.color = "#38bdf8";
      phaseBadge.style.background = "rgba(56, 189, 248, 0.2)";
      return;
    }

    const readingEnd = videoState.readingDuration;
    const cyclingStart = readingEnd + 0.5;
    const cyclingEnd = cyclingStart + videoState.cyclingDuration;
    const revealStart = cyclingEnd + (videoState.postCyclingPause || 2.0);

    if (cur < cyclingStart) {
      phaseBadge.textContent = "⚡ Question Reading";
      phaseBadge.style.color = "#818cf8";
      phaseBadge.style.background = "rgba(99, 102, 241, 0.2)";
    } else if (cur < cyclingEnd) {
      phaseBadge.textContent = "🎵 Options Cycling";
      phaseBadge.style.color = "#38bdf8";
      phaseBadge.style.background = "rgba(56, 189, 248, 0.2)";
    } else if (cur < revealStart) {
      phaseBadge.textContent = "⏳ Final Thinking Pause";
      phaseBadge.style.color = "#f59e0b";
      phaseBadge.style.background = "rgba(245, 158, 11, 0.2)";
    } else {
      phaseBadge.textContent = videoState.revealMode === "full" ? "🟢 Answer Reveal" : "❓ Teaser Callout";
      phaseBadge.style.color = "#34d399";
      phaseBadge.style.background = "rgba(52, 211, 153, 0.2)";
    }
  }
}

// --- Video Playback Engine ---
function playVideoPlayback() {
  if (videoState.isPlaying) return;
  videoState.isPlaying = true;
  videoState.lastFrameTimestamp = performance.now();

  const viewport = document.getElementById("video-viewport");
  if (viewport) viewport.classList.remove("paused");

  const playBtn = document.getElementById("video-play-pause-btn");
  if (playBtn) playBtn.innerHTML = '<i class="fa-solid fa-pause"></i> Pause';

  videoLoop(performance.now());
}

function pauseVideoPlayback() {
  videoState.isPlaying = false;
  if (videoState.animationReqId) {
    cancelAnimationFrame(videoState.animationReqId);
    videoState.animationReqId = null;
  }

  const viewport = document.getElementById("video-viewport");
  if (viewport) viewport.classList.add("paused");

  const playBtn = document.getElementById("video-play-pause-btn");
  if (playBtn) playBtn.innerHTML = '<i class="fa-solid fa-play"></i> Play';
}

function resetVideoToStart() {
  videoState.currentTime = 0;
  videoState.lastSoundStep = -1;
  videoState.revealSoundPlayed = false;
  updateScrubberUI();
  renderVideoFrameAt(0);
}

function videoLoop(now) {
  if (!videoState.isPlaying) return;

  const deltaSeconds = (now - videoState.lastFrameTimestamp) / 1000;
  videoState.lastFrameTimestamp = now;

  videoState.currentTime += deltaSeconds;

  if (videoState.currentTime >= videoState.totalDuration) {
    videoState.currentTime = 0;
    videoState.lastSoundStep = -1;
    videoState.revealSoundPlayed = false;
  }

  renderVideoFrameAt(videoState.currentTime);
  checkAndPlayAudioTriggers(videoState.currentTime);
  updateScrubberUI();

  videoState.animationReqId = requestAnimationFrame(videoLoop);
}

function checkAndPlayAudioTriggers(time, destNode = null) {
  if (videoState.videoMode === "static") return;
  const readingEnd = videoState.readingDuration;
  const cyclingStart = readingEnd + 0.5;
  const cyclingEnd = cyclingStart + videoState.cyclingDuration;
  const revealStart = cyclingEnd + (videoState.postCyclingPause || 2.0);

  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) return;
  const optionsCount = (q.options || []).length || 4;

  // Check Deliberation sound triggers (1 pass only across options):
  if (time >= cyclingStart && time < cyclingEnd) {
    const elapsedInCycling = time - cyclingStart;
    const totalSteps = optionsCount; // Exactly 1 deliberate pass
    const stepDuration = videoState.cyclingDuration / Math.max(1, totalSteps);
    const currentStep = Math.min(totalSteps - 1, Math.floor(elapsedInCycling / stepDuration));

    if (currentStep !== videoState.lastSoundStep) {
      videoState.lastSoundStep = currentStep;
      studioAudio.playCycleSound(currentStep, destNode);
    }
  }

  // Check Reveal sound trigger (after post-cycling suspense pause):
  if (time >= revealStart && !videoState.revealSoundPlayed) {
    videoState.revealSoundPlayed = true;
    studioAudio.playRevealSound(destNode);
  }
}

// --- Canvas Rendering Core (1080x1920 Native Resolution) ---
function renderVideoFrameAt(time) {
  const canvas = document.getElementById("video-preview-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) {
    ctx.fillStyle = "#090d16";
    ctx.fillRect(0, 0, 1080, 1920);
    return;
  }

  drawReelFrame(ctx, q, time, 1080, 1920);
}

function drawReelFrame(ctx, q, time, width, height) {
  ctx.save();
  ctx.clearRect(0, 0, width, height);

  // 1. Background Theme Gradient
  const currentTheme = (typeof INSTA_THEMES !== "undefined"
    ? INSTA_THEMES.find((t) => t.id === instaState.theme)
    : null) || {
    gradient: "linear-gradient(135deg, #110c2c 0%, #1e1b4b 40%, #312e81 80%, #4338ca 100%)",
  };
  drawThemeBackground(ctx, currentTheme.id, width, height);

  // 2. Decorative Border & Vignette
  ctx.strokeStyle = "rgba(255, 255, 255, 0.12)";
  ctx.lineWidth = 2;
  drawRoundedRect(ctx, 45, 45, width - 90, height - 90, 32);
  ctx.stroke();

  // 3. Header Section (Logo, Handle, Badges)
  const headerY = 90;
  drawHeaderSection(ctx, q, headerY, width);

  // 4. Static Reel Mode (Zero Animations) vs Animated Reel Mode
  const scenarioStartY = 260;
  if (videoState.videoMode === "static") {
    // Draw full crisp scenario immediately (no word highlight or fade)
    const scenarioBottomY = drawScenarioText(ctx, q.scenario, scenarioStartY, width, 99999, 1);
    const optionsStartY = scenarioBottomY + 40;
    const showAnswer = videoState.staticLayout === "with-answer";

    if (showAnswer) {
      const optionsBottomY = drawOptionsSection(ctx, q, optionsStartY, width, 99999, 1, 2, 3);
      drawEngagementPrompts(ctx, q, 99999, 1, 2, 3, optionsBottomY, width, height);
    } else {
      const optionsBottomY = drawOptionsSection(ctx, q, optionsStartY, width, 0, 99999, 99999, 99999);
      // Show clean caption callout pill in Static Question-Only mode
      if (videoState.showCommentPrompt) {
        const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";
        const promptY = Math.min(height - 230, Math.max(optionsBottomY + 28, height - 290));
        const commentText = videoState.commentPromptText || "💬 Drop your answer below • Full rationale in caption 👇";
        ctx.font = `600 20px ${fontFam}`;
        const textW = ctx.measureText(commentText).width;
        const pillW = Math.min(width - 120, textW + 48);
        const pillH = 48;
        const pillX = (width - pillW) / 2;

        ctx.fillStyle = "rgba(0, 0, 0, 0.35)";
        ctx.strokeStyle = "rgba(255, 255, 255, 0.26)";
        ctx.lineWidth = 1.5;
        drawRoundedRect(ctx, pillX, promptY, pillW, pillH, 24);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "rgba(255, 255, 255, 0.96)";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(commentText, width / 2, promptY + pillH / 2);
      }
    }

    drawFooterSection(ctx, q, height - 120, width);
    ctx.restore();
    return;
  }

  // Animated Reel Mode: Kinetic Reading + Option Deliberation + Reveal
  const readingEnd = videoState.readingDuration;
  const scenarioBottomY = drawScenarioText(ctx, q.scenario, scenarioStartY, width, time, readingEnd);

  // 5. Options Spotlight & Deliberation
  const cyclingStart = readingEnd + 0.5;
  const cyclingEnd = cyclingStart + videoState.cyclingDuration;
  const revealStart = cyclingEnd + (videoState.postCyclingPause || 2.0);
  const optionsStartY = scenarioBottomY + 40;

  const optionsBottomY = drawOptionsSection(ctx, q, optionsStartY, width, time, cyclingStart, cyclingEnd, revealStart);

  // 6. Viewer Engagement & Pause Prompts (Safe Zone)
  drawEngagementPrompts(ctx, q, time, cyclingStart, cyclingEnd, revealStart, optionsBottomY, width, height);

  // 7. Footer (Website Pill & CTA Handle)
  drawFooterSection(ctx, q, height - 120, width);

  ctx.restore();
}

// Background gradient helper
function drawThemeBackground(ctx, themeId, width, height) {
  let grad = ctx.createLinearGradient(0, 0, width, height);
  if (themeId === "midnight-emerald") {
    grad.addColorStop(0, "#011c15");
    grad.addColorStop(0.4, "#022c22");
    grad.addColorStop(0.8, "#064e3b");
    grad.addColorStop(1, "#0f766e");
  } else if (themeId === "crimson-sunset") {
    grad.addColorStop(0, "#320311");
    grad.addColorStop(0.4, "#4c0519");
    grad.addColorStop(0.8, "#881337");
    grad.addColorStop(1, "#be123c");
  } else if (themeId === "deep-space") {
    grad.addColorStop(0, "#090d16");
    grad.addColorStop(0.4, "#0f172a");
    grad.addColorStop(0.8, "#1e293b");
    grad.addColorStop(1, "#334155");
  } else if (themeId === "royal-plum") {
    grad.addColorStop(0, "#1c0a3c");
    grad.addColorStop(0.4, "#2e1065");
    grad.addColorStop(0.8, "#581c87");
    grad.addColorStop(1, "#7e22ce");
  } else if (themeId === "vibrant-coral") {
    grad.addColorStop(0, "#4f1d0b");
    grad.addColorStop(0.4, "#7c2d12");
    grad.addColorStop(0.8, "#9a3412");
    grad.addColorStop(1, "#ea580c");
  } else {
    // Default: Indigo Dusk
    grad.addColorStop(0, "#110c2c");
    grad.addColorStop(0.4, "#1e1b4b");
    grad.addColorStop(0.8, "#312e81");
    grad.addColorStop(1, "#4338ca");
  }

  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, width, height);
}

// Header Section Drawing
function drawHeaderSection(ctx, q, startY, width) {
  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";

  // MedBank 'M' Logo Circle
  ctx.fillStyle = "#6366f1";
  ctx.beginPath();
  ctx.arc(90, startY + 20, 26, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#ffffff";
  ctx.font = `700 24px ${fontFam}`;
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("M", 90, startY + 20);

  // Handle Text
  ctx.textAlign = "left";
  ctx.font = `600 24px ${fontFam}`;
  ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
  ctx.fillText(instaState.handle || "@medqstudios", 130, startY + 20);

  // Badges row: Exam, Category, Type
  const badgesY = startY + 68;
  let curX = 64;

  const badges = [
    { text: q.exam || "MSRA", bg: "rgba(99, 102, 241, 0.3)", border: "#6366f1" },
    { text: q.category || "Clinical", bg: "rgba(236, 72, 153, 0.25)", border: "#ec4899" },
    { text: (q.type || "SBA").toUpperCase(), bg: "rgba(255, 255, 255, 0.12)", border: "rgba(255,255,255,0.25)" },
  ];

  ctx.font = `600 18px ${fontFam}`;
  badges.forEach((b) => {
    const textWidth = ctx.measureText(b.text).width;
    const badgeW = textWidth + 24;
    const badgeH = 34;

    ctx.fillStyle = b.bg;
    ctx.strokeStyle = b.border;
    ctx.lineWidth = 1.5;
    drawRoundedRect(ctx, curX, badgesY, badgeW, badgeH, 17);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#ffffff";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(b.text, curX + badgeW / 2, badgesY + badgeH / 2);

    curX += badgeW + 12;
  });
}

// Kinetic Scenario Text Drawing
function drawScenarioText(ctx, scenario, startY, width, time, readingEnd) {
  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";
  const fontSize = Math.max(24, Math.round(instaState.scenarioFontSize * 1.25));
  ctx.font = `500 ${fontSize}px ${fontFam}`;
  ctx.textBaseline = "top";

  const paddingX = 70;
  const maxContentWidth = width - paddingX * 2;
  const lineHeight = fontSize * 1.52;

  // Split scenario into words
  const words = (scenario || "").split(/\s+/).filter(Boolean);
  const totalWords = words.length;

  // Build wrapped lines with word positions
  const lines = [];
  let currentLine = [];
  let currentLineWidth = 0;
  const spaceWidth = ctx.measureText(" ").width;

  words.forEach((word, idx) => {
    const wordWidth = ctx.measureText(word).width;
    if (currentLineWidth + wordWidth > maxContentWidth && currentLine.length > 0) {
      lines.push(currentLine);
      currentLine = [];
      currentLineWidth = 0;
    }
    currentLine.push({
      text: word,
      index: idx,
      width: wordWidth,
    });
    currentLineWidth += wordWidth + spaceWidth;
  });
  if (currentLine.length > 0) {
    lines.push(currentLine);
  }

  // Draw words with kinetic illumination
  let curY = startY;
  lines.forEach((line) => {
    let curX = paddingX;
    line.forEach((item) => {
      // Calculate word timing:
      const wordStartTime = (item.index / totalWords) * readingEnd;
      const wordEndTime = ((item.index + 1) / totalWords) * readingEnd;

      const isRead = time >= wordEndTime;
      const isActive = time >= wordStartTime && time < wordEndTime;

      if (isActive) {
        // Active word: glowing backdrop pill and bright highlight
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
        drawRoundedRect(ctx, curX - 4, curY - 2, item.width + 8, lineHeight - 6, 6);
        ctx.fill();

        ctx.fillStyle = "#38bdf8"; // Neon light cyan
        ctx.shadowColor = "#38bdf8";
        ctx.shadowBlur = 10;
        ctx.font = `700 ${fontSize}px ${fontFam}`;
      } else if (isRead) {
        // Read word: crisp white
        ctx.fillStyle = "rgba(255, 255, 255, 0.96)";
        ctx.shadowBlur = 0;
        ctx.font = `500 ${fontSize}px ${fontFam}`;
      } else {
        // Unread word: dimmed/translucent
        ctx.fillStyle = "rgba(255, 255, 255, 0.28)";
        ctx.shadowBlur = 0;
        ctx.font = `500 ${fontSize}px ${fontFam}`;
      }

      ctx.textAlign = "left";
      ctx.fillText(item.text, curX, curY);

      // Reset shadow
      ctx.shadowBlur = 0;
      curX += item.width + spaceWidth;
    });
    curY += lineHeight;
  });

  return curY;
}

// Options Spotlight & Countdown Section Drawing
function drawOptionsSection(ctx, q, startY, width, time, cyclingStart, cyclingEnd, revealStart) {
  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";
  const options = q.options || [];
  const paddingX = 70;
  const cardWidth = width - paddingX * 2;
  const isSBA = q.type === "sba" || q.type === "emq" || !q.type;

  // Phase flags:
  const isCycling = time >= cyclingStart && time < cyclingEnd;
  const isSuspense = time >= cyclingEnd && time < revealStart;
  const isRevealed = time >= revealStart;

  // Prompt Line
  ctx.font = `700 20px ${fontFam}`;
  ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
  ctx.textAlign = "left";
  ctx.textBaseline = "middle";
  let promptText = q.type === "ranking" ? "RANK THE OPTIONS:" : "SELECT THE SINGLE BEST ANSWER:";
  if (isSuspense) {
    promptText = "LOCK IN YOUR FINAL GUESS:";
  } else if (isRevealed) {
    promptText = videoState.revealMode === "full" ? "CORRECT ANSWER:" : "CAN YOU SOLVE THIS CASE?";
  }
  ctx.fillText(promptText, paddingX, startY);

  // Timer Bar under prompt during cycling & suspense pause
  if (isCycling) {
    const elapsed = time - cyclingStart;
    const progress = Math.max(0, Math.min(1, elapsed / videoState.cyclingDuration));
    const timerW = cardWidth * (1 - progress);

    ctx.fillStyle = "rgba(255, 255, 255, 0.15)";
    drawRoundedRect(ctx, paddingX, startY + 22, cardWidth, 6, 3);
    ctx.fill();

    ctx.fillStyle = "#38bdf8";
    drawRoundedRect(ctx, paddingX, startY + 22, timerW, 6, 3);
    ctx.fill();
  } else if (isSuspense) {
    const pauseDur = Math.max(0.1, videoState.postCyclingPause || 2.0);
    const elapsed = time - cyclingEnd;
    const progress = Math.max(0, Math.min(1, elapsed / pauseDur));
    const timerW = cardWidth * (1 - progress);

    ctx.fillStyle = "rgba(255, 255, 255, 0.15)";
    drawRoundedRect(ctx, paddingX, startY + 22, cardWidth, 6, 3);
    ctx.fill();

    // Warm amber bar for suspense countdown
    ctx.fillStyle = "#f59e0b";
    drawRoundedRect(ctx, paddingX, startY + 22, timerW, 6, 3);
    ctx.fill();
  }

  // Calculate active option during deliberate scan (1 pass only across options):
  const totalOptions = options.length;
  const stepDuration = videoState.cyclingDuration / Math.max(1, totalOptions);
  let activeIndex = -1;
  if (isCycling) {
    const elapsed = time - cyclingStart;
    activeIndex = Math.min(totalOptions - 1, Math.floor(elapsed / stepDuration));
  }

  // Correct answer index
  const correctIdx = options.indexOf(q.correct_answer);

  // Draw Option Cards
  let cardY = startY + 45;
  const cardHeight = Math.min(110, Math.max(85, Math.round(instaState.optionsFontSize * 3.4)));
  const cardSpacing = 16;
  const optFontSize = Math.max(20, Math.round(instaState.optionsFontSize * 1.2));

  options.forEach((opt, idx) => {
    const isThisActive = isCycling && activeIndex === idx;
    const hasCycledThrough = (isCycling && idx < activeIndex) || isSuspense;
    const isThisCorrect = isRevealed && (idx === correctIdx || opt === q.correct_answer);

    // Card background & border
    if (isThisCorrect && videoState.revealMode === "full") {
      // Emerald Green Highlight for correct answer
      ctx.fillStyle = "rgba(16, 185, 129, 0.28)";
      ctx.strokeStyle = "#10b981";
      ctx.lineWidth = 3;
      ctx.shadowColor = "rgba(16, 185, 129, 0.5)";
      ctx.shadowBlur = 20;
    } else if (isThisActive) {
      // Spotlighted Option (Velvety Indigo/Cyan Glow)
      ctx.fillStyle = "rgba(99, 102, 241, 0.22)";
      ctx.strokeStyle = "#818cf8";
      ctx.lineWidth = 2.5;
      ctx.shadowColor = "rgba(99, 102, 241, 0.5)";
      ctx.shadowBlur = 16;
    } else if (hasCycledThrough) {
      // Already Cycled Through (Evaluated Option - Changed pill & card color!)
      ctx.fillStyle = "rgba(168, 85, 247, 0.12)";
      ctx.strokeStyle = "rgba(168, 85, 247, 0.45)";
      ctx.lineWidth = 1.6;
      ctx.shadowBlur = 0;
    } else if (isRevealed && videoState.revealMode === "full") {
      // Non-correct options dim when answer is revealed
      ctx.fillStyle = "rgba(255, 255, 255, 0.03)";
      ctx.strokeStyle = "rgba(255, 255, 255, 0.06)";
      ctx.lineWidth = 1;
      ctx.shadowBlur = 0;
    } else {
      // Pending option (not yet evaluated)
      ctx.fillStyle = "rgba(255, 255, 255, 0.06)";
      ctx.strokeStyle = "rgba(255, 255, 255, 0.12)";
      ctx.lineWidth = 1.2;
      ctx.shadowBlur = 0;
    }

    drawRoundedRect(ctx, paddingX, cardY, cardWidth, cardHeight, 18);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0; // Reset shadow

    // Badge circle / Pill (Letter A, B, C, D)
    const badgeX = paddingX + 34;
    const badgeY = cardY + cardHeight / 2;
    const badgeR = 24;

    ctx.beginPath();
    ctx.arc(badgeX, badgeY, badgeR, 0, Math.PI * 2);

    if (isThisCorrect && videoState.revealMode === "full") {
      // Correct: Green Checkmark
      ctx.fillStyle = "#10b981";
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = `700 24px ${fontFam}`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText("✓", badgeX, badgeY);
    } else if (isThisActive) {
      // Active: Spotlighted Indigo Pill
      ctx.fillStyle = "#6366f1";
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = `700 22px ${fontFam}`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(String.fromCharCode(65 + idx), badgeX, badgeY);
    } else if (hasCycledThrough) {
      // Cycled through: Evaluated Soft Purple/Amethyst Pill (Changed Color!)
      ctx.fillStyle = "rgba(168, 85, 247, 0.45)";
      ctx.fill();
      ctx.strokeStyle = "#c084fc";
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.fillStyle = "#f3e8ff";
      ctx.font = `600 20px ${fontFam}`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(String.fromCharCode(65 + idx), badgeX, badgeY);
    } else {
      // Pending: Translucent pill
      ctx.fillStyle = "rgba(255, 255, 255, 0.12)";
      ctx.fill();
      ctx.fillStyle = isRevealed && videoState.revealMode === "full" ? "rgba(255,255,255,0.3)" : "rgba(255,255,255,0.75)";
      ctx.font = `600 20px ${fontFam}`;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(String.fromCharCode(65 + idx), badgeX, badgeY);
    }

    // Option Text
    ctx.font = `600 ${optFontSize}px ${fontFam}`;
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";

    if (isThisCorrect && videoState.revealMode === "full") {
      ctx.fillStyle = "#ffffff";
    } else if (isThisActive) {
      ctx.fillStyle = "#ffffff";
    } else if (isRevealed && videoState.revealMode === "full") {
      ctx.fillStyle = "rgba(255, 255, 255, 0.45)";
    } else {
      ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
    }

    const textX = paddingX + 74;
    const maxOptTextWidth = cardWidth - 90;
    drawWrappedSingleLine(ctx, opt, textX, badgeY, maxOptTextWidth);

    cardY += cardHeight + cardSpacing;
  });

  // 7. Reveal Box (Learning Point / Teaser Callout)
  if (isRevealed) {
    const cardH = drawExplanationCard(ctx, q, cardY + 10, width, cardWidth, paddingX);
    return cardY + 10 + cardH;
  }
  return cardY;
}

// Explanation Card during Reveal Phase
function drawExplanationCard(ctx, q, startY, width, cardWidth, paddingX) {
  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";

  if (videoState.revealMode === "teaser") {
    // Teaser Mode Card
    const boxHeight = 150;
    ctx.save();
    ctx.fillStyle = "rgba(245, 158, 11, 0.18)";
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2.5;
    ctx.shadowColor = "rgba(245, 158, 11, 0.4)";
    ctx.shadowBlur = 18;
    drawRoundedRect(ctx, paddingX, startY, cardWidth, boxHeight, 22);
    ctx.fill();
    ctx.stroke();
    ctx.restore();

    ctx.font = `700 28px ${fontFam}`;
    ctx.fillStyle = "#fcd34d";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("💬 Lock in your guess in the comments!", width / 2, startY + 50);

    ctx.font = `600 22px ${fontFam}`;
    ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
    ctx.fillText("Full clinical rationale & 1000+ MSRA cases at " + (instaState.websiteUrl || "medqstudios.com"), width / 2, startY + 98);

    return boxHeight;
  } else {
    // Full Learning Point Reveal
    const baseSize = videoState.explanationFontSize || instaState.explanationFontSize || 24;
    const explFontSize = Math.max(26, Math.round(baseSize * 1.25));
    const lineHeight = Math.round(explFontSize * 1.48);
    const textMaxWidth = cardWidth - 64;

    const explText = q.explanation || "Review the pathognomonic clinical signs and guidelines for this presentation.";

    // Measure and wrap explanation lines
    ctx.font = `500 ${explFontSize}px ${fontFam}`;
    const words = explText.split(/\s+/).filter(Boolean);
    const lines = [];
    let currentLine = "";

    for (let i = 0; i < words.length; i++) {
      const testLine = currentLine + words[i] + " ";
      const testWidth = ctx.measureText(testLine).width;
      if (testWidth > textMaxWidth && i > 0) {
        lines.push(currentLine.trim());
        currentLine = words[i] + " ";
      } else {
        currentLine = testLine;
      }
    }
    if (currentLine.trim().length > 0) {
      lines.push(currentLine.trim());
    }

    // Limit to 4 lines with ellipsis if necessary
    const maxLines = 4;
    if (lines.length > maxLines) {
      lines.length = maxLines;
      let lastLine = lines[maxLines - 1];
      while (ctx.measureText(lastLine + "...").width > textMaxWidth && lastLine.length > 3) {
        lastLine = lastLine.slice(0, -1);
      }
      lines[maxLines - 1] = lastLine.trim() + "...";
    }

    const headerHeight = 56;
    const paddingY = 24;
    const contentHeight = lines.length * lineHeight;
    const boxHeight = Math.max(160, headerHeight + contentHeight + paddingY * 2);

    // High-contrast, rich dark card background with emerald accent glow
    ctx.save();
    const grad = ctx.createLinearGradient(paddingX, startY, paddingX + cardWidth, startY + boxHeight);
    grad.addColorStop(0, "rgba(10, 16, 30, 0.94)");
    grad.addColorStop(1, "rgba(5, 8, 16, 0.98)");
    ctx.fillStyle = grad;

    ctx.strokeStyle = "rgba(52, 211, 153, 0.50)"; // Radiant Emerald Border
    ctx.lineWidth = 2.5;
    ctx.shadowColor = "rgba(16, 185, 129, 0.35)";
    ctx.shadowBlur = 18;
    drawRoundedRect(ctx, paddingX, startY, cardWidth, boxHeight, 22);
    ctx.fill();
    ctx.stroke();
    ctx.restore();

    // Emerald Header Accent Pill
    const pillY = startY + 20;
    const pillH = 36;
    ctx.font = `700 20px ${fontFam}`;
    const headerTitle = "💡 KEY CLINICAL PEARL";
    const titleWidth = ctx.measureText(headerTitle).width;
    const pillW = titleWidth + 30;

    ctx.fillStyle = "rgba(16, 185, 129, 0.22)";
    ctx.strokeStyle = "#10b981";
    ctx.lineWidth = 1.5;
    drawRoundedRect(ctx, paddingX + 24, pillY, pillW, pillH, 18);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#34d399";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(headerTitle, paddingX + 24 + pillW / 2, pillY + pillH / 2);

    // Subtle divider line under header
    ctx.strokeStyle = "rgba(255, 255, 255, 0.12)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(paddingX + 24, startY + headerHeight + 8);
    ctx.lineTo(paddingX + cardWidth - 24, startY + headerHeight + 8);
    ctx.stroke();

    // Render explanation text lines (crisp pure white, 500 semi-bold, high readability)
    ctx.font = `500 ${explFontSize}px ${fontFam}`;
    ctx.fillStyle = "#ffffff";
    ctx.textAlign = "left";
    ctx.textBaseline = "top";

    let lineY = startY + headerHeight + 20;
    lines.forEach((l) => {
      ctx.fillText(l, paddingX + 28, lineY);
      lineY += lineHeight;
    });

    return boxHeight;
  }
}

// Viewer Engagement & Pause Prompts (Safe Zone directly below options/explanation)
function drawEngagementPrompts(ctx, q, time, cyclingStart, cyclingEnd, revealStart, optionsBottomY, width, height) {
  if (!videoState.showPausePrompt && !videoState.showCommentPrompt) return;

  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";
  const isDeliberating = time >= cyclingStart && time < cyclingEnd;
  const isSuspense = time >= cyclingEnd && time < revealStart;
  const isRevealed = time >= revealStart;

  // Only appear once options are active / visible (deliberation, suspense, or reveal phase)
  if (!isDeliberating && !isSuspense && !isRevealed) return;

  // Safe vertical placement above the bottom UI overlay
  let promptY = Math.min(height - 230, Math.max(optionsBottomY + 24, height - 320));

  // 1. Pause Callout Pill
  if (videoState.showPausePrompt) {
    let pauseText;
    if (isDeliberating) {
      pauseText = videoState.pausePromptText || "⏸️ Pause to solve • Answer in 3s";
    } else if (isSuspense) {
      pauseText = "⏸️ Final chance to pause • Revealing answer!";
    } else {
      pauseText = "⏸️ Tap screen to pause & read key points";
    }

    ctx.font = `700 20px ${fontFam}`;
    const textW = ctx.measureText(pauseText).width;
    const pillW = Math.min(width - 120, textW + 52);
    const pillH = 48;
    const pillX = (width - pillW) / 2;

    if (isDeliberating || isSuspense) {
      // Warm amber urgent pulse
      ctx.fillStyle = "rgba(245, 158, 11, 0.22)";
      ctx.strokeStyle = "rgba(245, 158, 11, 0.75)";
      ctx.shadowColor = "rgba(245, 158, 11, 0.45)";
      ctx.shadowBlur = 14;
    } else {
      // Emerald green learning pulse
      ctx.fillStyle = "rgba(16, 185, 129, 0.22)";
      ctx.strokeStyle = "rgba(16, 185, 129, 0.75)";
      ctx.shadowColor = "rgba(16, 185, 129, 0.45)";
      ctx.shadowBlur = 14;
    }

    ctx.lineWidth = 2;
    drawRoundedRect(ctx, pillX, promptY, pillW, pillH, 24);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    ctx.fillStyle = "#ffffff";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(pauseText, width / 2, promptY + pillH / 2);

    promptY += pillH + 12;
  }

  // 2. Caption & Comments Engagement Prompt
  if (videoState.showCommentPrompt) {
    const commentText = (isDeliberating || isSuspense)
      ? "💬 Drop your answer below • Full case in caption 👇"
      : (videoState.commentPromptText || "💬 Full rationale & guidelines in caption 👇");

    ctx.font = `600 18px ${fontFam}`;
    const textW = ctx.measureText(commentText).width;
    const pillW = Math.min(width - 120, textW + 44);
    const pillH = 42;
    const pillX = (width - pillW) / 2;

    ctx.fillStyle = "rgba(0, 0, 0, 0.35)";
    ctx.strokeStyle = "rgba(255, 255, 255, 0.22)";
    ctx.lineWidth = 1.2;
    drawRoundedRect(ctx, pillX, promptY, pillW, pillH, 21);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "rgba(255, 255, 255, 0.95)";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(commentText, width / 2, promptY + pillH / 2);
  }
}

// Footer Section Drawing
function drawFooterSection(ctx, q, startY, width) {
  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";

  // Website Pill Badge
  if (instaState.websiteUrl) {
    const pillText = `🌐 Practice free at ${instaState.websiteUrl}`;
    ctx.font = `700 20px ${fontFam}`;
    const textW = ctx.measureText(pillText).width;
    const pillW = textW + 36;
    const pillH = 44;
    const pillX = (width - pillW) / 2;

    ctx.fillStyle = "rgba(255, 255, 255, 0.12)";
    ctx.strokeStyle = "rgba(255, 255, 255, 0.3)";
    ctx.lineWidth = 1.5;
    drawRoundedRect(ctx, pillX, startY - 10, pillW, pillH, 22);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#ffffff";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(pillText, width / 2, startY + 12);
  }

  // Handle + CTA
  ctx.font = `500 18px ${fontFam}`;
  ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(`Save this reel • ${instaState.handle || "@medqstudios"}`, width / 2, startY + 54);
}

// Helper: Rounded Rectangle
function drawRoundedRect(ctx, x, y, width, height, radius) {
  ctx.beginPath();
  ctx.moveTo(x + radius, y);
  ctx.lineTo(x + width - radius, y);
  ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
  ctx.lineTo(x + width, y + height - radius);
  ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
  ctx.lineTo(x + radius, y + height);
  ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
  ctx.lineTo(x, y + radius);
  ctx.quadraticCurveTo(x, y, x + radius, y);
  ctx.closePath();
}

// Helper: Wrapped single line (truncates if too long)
function drawWrappedSingleLine(ctx, text, x, y, maxWidth) {
  let truncated = text;
  if (ctx.measureText(truncated).width > maxWidth) {
    while (ctx.measureText(truncated + "...").width > maxWidth && truncated.length > 3) {
      truncated = truncated.slice(0, -1);
    }
    truncated += "...";
  }
  ctx.fillText(truncated, x, y);
}

// Helper: Wrapped paragraph with max lines
function drawWrappedParagraph(ctx, text, x, y, maxWidth, lineHeight, maxLines) {
  const words = text.split(" ");
  let line = "";
  let lineCount = 0;
  let curY = y;

  for (let i = 0; i < words.length; i++) {
    const testLine = line + words[i] + " ";
    const testWidth = ctx.measureText(testLine).width;
    if (testWidth > maxWidth && i > 0) {
      ctx.fillText(line, x, curY);
      line = words[i] + " ";
      curY += lineHeight;
      lineCount++;
      if (lineCount >= maxLines - 1 && i < words.length - 1) {
        let remaining = line + words.slice(i + 1).join(" ");
        if (ctx.measureText(remaining).width > maxWidth) {
          while (ctx.measureText(remaining + "...").width > maxWidth && remaining.length > 3) {
            remaining = remaining.slice(0, -1);
          }
          remaining += "...";
        }
        ctx.fillText(remaining, x, curY);
        return;
      }
    } else {
      line = testLine;
    }
  }
  ctx.fillText(line, x, curY);
}

// --- Helper: UTF-8 safe Base64 JSON header encoding ---
function encodeReelMetaHeader(metaObj) {
  const jsonStr = JSON.stringify(metaObj);
  const bytes = new TextEncoder().encode(jsonStr);
  let binary = "";
  bytes.forEach((b) => {
    binary += String.fromCharCode(b);
  });
  return btoa(binary);
}

// --- Direct-to-Instagram Backend Status (Vercel Cloud or Local server.py) ---
async function checkLocalServerStatus() {
  const serverPill = document.getElementById("ig-status-server-pill");
  const ffmpegPill = document.getElementById("ig-status-ffmpeg-pill");
  const accountPill = document.getElementById("ig-status-account-pill");

  const webCodecsReady = typeof VideoEncoder !== "undefined" && typeof VideoFrame !== "undefined";

  try {
    const resp = await fetch("/api/status", { cache: "no-store" });
    if (!resp.ok) throw new Error("Not available");
    const data = await resp.json();

    igServerState.checked = true;
    igServerState.mode = data.mode || (data.server ? "local" : "offline");
    igServerState.online = igServerState.mode === "vercel" || Boolean(data.server);
    igServerState.ffmpegAvailable = Boolean(data.ffmpeg_available);
    igServerState.ffmpegPath = data.ffmpeg_path || "";
    igServerState.blobConfigured = Boolean(data.blob_configured);
    igServerState.passcodeRequired = Boolean(data.passcode_required);
    igServerState.igConfigured = Boolean(data.ig_configured);
    igServerState.igUsername = data.ig_username || "";
    igServerState.saveLocalCopy = data.save_local_copy !== false;

    if (igServerState.mode === "vercel") {
      if (serverPill) {
        serverPill.className = "ig-pill ig-pill-ok";
        serverPill.innerHTML = '<i class="fa-solid fa-cloud"></i> Vercel Cloud: Online';
      }
      if (ffmpegPill) {
        if (igServerState.blobConfigured && webCodecsReady) {
          ffmpegPill.className = "ig-pill ig-pill-ok";
          ffmpegPill.innerHTML = '<i class="fa-solid fa-bolt"></i> MP4 + Blob: Ready';
        } else if (!igServerState.blobConfigured) {
          ffmpegPill.className = "ig-pill ig-pill-warn";
          ffmpegPill.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Vercel Blob: Setup Needed';
        } else {
          ffmpegPill.className = "ig-pill ig-pill-warn";
          ffmpegPill.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Use Chrome/Edge for MP4';
        }
      }
      if (accountPill) {
        if (igServerState.igConfigured) {
          const label = igServerState.igUsername ? `@${igServerState.igUsername}` : "Env Connected";
          accountPill.className = "ig-pill ig-pill-ok";
          accountPill.innerHTML = `<i class="fa-brands fa-instagram"></i> Instagram: ${label}`;
        } else {
          accountPill.className = "ig-pill ig-pill-warn";
          accountPill.innerHTML = '<i class="fa-brands fa-instagram"></i> Instagram: Add Env Vars';
        }
      }
    } else {
      if (serverPill) {
        serverPill.className = "ig-pill ig-pill-ok";
        serverPill.innerHTML = '<i class="fa-solid fa-server"></i> Local Server: Online';
      }
      if (ffmpegPill) {
        if (webCodecsReady) {
          ffmpegPill.className = "ig-pill ig-pill-ok";
          ffmpegPill.innerHTML = '<i class="fa-solid fa-bolt"></i> Browser MP4: Ready';
        } else if (igServerState.ffmpegAvailable) {
          ffmpegPill.className = "ig-pill ig-pill-ok";
          ffmpegPill.innerHTML = '<i class="fa-solid fa-film"></i> FFmpeg: Ready (IG MP4)';
        } else {
          ffmpegPill.className = "ig-pill ig-pill-warn";
          ffmpegPill.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> FFmpeg: Not Installed';
        }
      }
      if (accountPill) {
        if (igServerState.igConfigured) {
          const label = igServerState.igUsername ? `@${igServerState.igUsername}` : "Configured";
          accountPill.className = "ig-pill ig-pill-ok";
          accountPill.innerHTML = `<i class="fa-brands fa-instagram"></i> Instagram: ${label}`;
        } else {
          accountPill.className = "ig-pill ig-pill-warn";
          accountPill.innerHTML = '<i class="fa-brands fa-instagram"></i> Instagram: Setup Needed';
        }
      }
    }
  } catch (err) {
    igServerState.checked = true;
    igServerState.mode = "offline";
    igServerState.online = false;
    igServerState.ffmpegAvailable = false;
    igServerState.igConfigured = false;

    if (serverPill) {
      serverPill.className = "ig-pill ig-pill-warn";
      serverPill.innerHTML = '<i class="fa-solid fa-plug-circle-xmark"></i> Offline (Deploy to Vercel or run server.py)';
    }
    if (ffmpegPill) {
      if (webCodecsReady) {
        ffmpegPill.className = "ig-pill ig-pill-ok";
        ffmpegPill.innerHTML = '<i class="fa-solid fa-bolt"></i> Browser MP4: Ready';
      } else {
        ffmpegPill.className = "ig-pill ig-pill-muted";
        ffmpegPill.innerHTML = '<i class="fa-solid fa-film"></i> MP4 Encoder: Fallback';
      }
    }
    if (accountPill) {
      accountPill.className = "ig-pill ig-pill-muted";
      accountPill.innerHTML = '<i class="fa-brands fa-instagram"></i> Direct Publish: Offline';
    }
  }
  return igServerState;
}

function initIgDirectSetupUI() {
  const openBtn = document.getElementById("open-ig-setup-btn");
  const closeBtn = document.getElementById("close-ig-setup-modal");
  const overlay = document.getElementById("ig-setup-modal");
  const saveBtn = document.getElementById("ig-setup-save-btn");
  const testBtn = document.getElementById("ig-setup-test-btn");

  if (openBtn) openBtn.addEventListener("click", openIgSetupModal);
  if (closeBtn) closeBtn.addEventListener("click", closeIgSetupModal);
  if (overlay) {
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) closeIgSetupModal();
    });
  }
  if (saveBtn) saveBtn.addEventListener("click", () => saveIgConfig(false));
  if (testBtn) testBtn.addEventListener("click", () => saveIgConfig(true));
}

async function openIgSetupModal() {
  const modal = document.getElementById("ig-setup-modal");
  const warning = document.getElementById("ig-setup-server-warning");
  const resultBox = document.getElementById("ig-setup-test-result");
  const vercelSection = document.getElementById("ig-setup-vercel-section");
  const localSection = document.getElementById("ig-setup-local-section");
  const passcodeInput = document.getElementById("ig-vercel-passcode");

  if (resultBox) resultBox.style.display = "none";

  await checkLocalServerStatus();
  if (warning) warning.style.display = igServerState.online ? "none" : "block";

  if (igServerState.mode === "vercel") {
    if (vercelSection) vercelSection.style.display = "flex";
    if (localSection) localSection.style.display = "none";
    if (passcodeInput) passcodeInput.value = getStoredPasscode();
  } else {
    if (vercelSection) vercelSection.style.display = "none";
    if (localSection) localSection.style.display = "flex";

    if (igServerState.online) {
      try {
        const resp = await fetch("/api/config", { cache: "no-store" });
        if (resp.ok) {
          const cfg = await resp.json();
          const userIdEl = document.getElementById("ig-config-user-id");
          const tokenEl = document.getElementById("ig-config-token");
          const tokenHint = document.getElementById("ig-token-hint");
          const apiVerEl = document.getElementById("ig-config-api-version");
          const ffmpegEl = document.getElementById("ig-config-ffmpeg-path");
          const shareFeedEl = document.getElementById("ig-config-share-feed");
          const saveLocalEl = document.getElementById("ig-config-save-local");

          if (userIdEl) userIdEl.value = cfg.ig_user_id || "";
          if (tokenEl) tokenEl.value = "";
          if (tokenHint) {
            tokenHint.textContent = cfg.has_token
              ? `(Saved: ${cfg.token_preview} — leave blank to keep)`
              : "(Required)";
          }
          if (apiVerEl) apiVerEl.value = cfg.api_version || "v21.0";
          if (ffmpegEl) ffmpegEl.value = cfg.ffmpeg_path || "";
          if (shareFeedEl) shareFeedEl.checked = cfg.share_to_feed !== false;
          if (saveLocalEl) saveLocalEl.checked = cfg.save_local_copy !== false;
        }
      } catch (e) {}
    }
  }

  if (modal) modal.style.display = "flex";
}

function closeIgSetupModal() {
  const modal = document.getElementById("ig-setup-modal");
  if (modal) modal.style.display = "none";
}

async function saveIgConfig(runTest) {
  const resultBox = document.getElementById("ig-setup-test-result");
  const showResult = (ok, html) => {
    if (!resultBox) return;
    resultBox.style.display = "block";
    resultBox.style.background = ok ? "rgba(16, 185, 129, 0.14)" : "rgba(239, 68, 68, 0.14)";
    resultBox.style.border = ok ? "1px solid rgba(16, 185, 129, 0.45)" : "1px solid rgba(239, 68, 68, 0.45)";
    resultBox.style.color = ok ? "#10b981" : "#f87171";
    resultBox.innerHTML = html;
  };

  if (!igServerState.online) {
    showResult(false, "Backend not detected. Deploy to Vercel or start <code>python server.py</code> locally.");
    return;
  }

  const testBtn = document.getElementById("ig-setup-test-btn");
  const saveBtn = document.getElementById("ig-setup-save-btn");
  if (testBtn) testBtn.disabled = true;
  if (saveBtn) saveBtn.disabled = true;

  try {
    // Vercel Cloud mode: store passcode in localStorage and verify via /api/ig-test
    if (igServerState.mode === "vercel") {
      const passcode = (document.getElementById("ig-vercel-passcode")?.value || "").trim();
      setStoredPasscode(passcode);

      if (!runTest) {
        showResult(true, '<i class="fa-solid fa-circle-check"></i> Passcode saved in this browser.');
        return;
      }

      const resp = await fetch("/api/ig-test", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Admin-Passcode": passcode,
        },
        body: JSON.stringify({}),
      });
      const data = await resp.json();
      if (!resp.ok || !data.ok) {
        throw new Error(data.error || "Connection test failed.");
      }

      await checkLocalServerStatus();
      const uname = data.profile?.username ? `@${data.profile.username}` : data.profile?.id || "Instagram";
      const accountPill = document.getElementById("ig-status-account-pill");
      if (accountPill) {
        accountPill.className = "ig-pill ig-pill-ok";
        accountPill.innerHTML = `<i class="fa-brands fa-instagram"></i> Instagram: ${uname}`;
      }
      showResult(
        true,
        `<i class="fa-solid fa-circle-check"></i> Connected to <strong>${uname}</strong> via Vercel! Ready for 1-click Reel publishing.`
      );
      return;
    }

    // Local server.py mode: save to ig_config.json and optionally test
    const userId = (document.getElementById("ig-config-user-id")?.value || "").trim();
    const rawToken = (document.getElementById("ig-config-token")?.value || "").trim();
    const apiVer = (document.getElementById("ig-config-api-version")?.value || "v21.0").trim();
    const ffmpegPath = (document.getElementById("ig-config-ffmpeg-path")?.value || "").trim();
    const shareToFeed = Boolean(document.getElementById("ig-config-share-feed")?.checked);
    const saveLocalCopy = Boolean(document.getElementById("ig-config-save-local")?.checked);

    const payload = {
      ig_user_id: userId,
      access_token: rawToken ? rawToken : "__KEEP__",
      api_version: apiVer,
      ffmpeg_path: ffmpegPath,
      share_to_feed: shareToFeed,
      save_local_copy: saveLocalCopy,
    };

    const endpoint = runTest ? "/api/test-connection" : "/api/config";
    const resp = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await resp.json();

    if (!resp.ok || !data.ok) {
      throw new Error(data.error || "Failed to save configuration.");
    }

    await checkLocalServerStatus();
    if (runTest && data.profile) {
      const uname = data.profile.username ? `@${data.profile.username}` : data.profile.id;
      showResult(
        true,
        `<i class="fa-solid fa-circle-check"></i> Connected to <strong>${uname}</strong>! You can now publish Reels directly to Instagram in 1 click.`
      );
    } else {
      showResult(true, '<i class="fa-solid fa-circle-check"></i> Settings saved to <code>ig_config.json</code>.');
    }
  } catch (err) {
    showResult(false, `<i class="fa-solid fa-circle-xmark"></i> ${err.message}`);
  } finally {
    if (testBtn) testBtn.disabled = false;
    if (saveBtn) saveBtn.disabled = false;
  }
}

// --- Browser-Native Instagram MP4 Encoder (WebCodecs + mp4-muxer, Zero FFmpeg Needed!) ---
let _mp4MuxerModule = null;
async function loadMp4Muxer() {
  if (!_mp4MuxerModule) {
    _mp4MuxerModule = await import("https://cdn.jsdelivr.net/npm/mp4-muxer@5.2.2/build/mp4-muxer.mjs");
  }
  return _mp4MuxerModule;
}

let _vercelBlobClientModule = null;
async function loadVercelBlobClient() {
  if (!_vercelBlobClientModule) {
    _vercelBlobClientModule = await import("https://esm.sh/@vercel/blob@0.27.3/client");
  }
  return _vercelBlobClientModule;
}

async function selectSupportedAvcCodec(width, height, fps) {
  if (typeof VideoEncoder === "undefined") return null;
  const candidates = [
    "avc1.64002a", // H.264 High Profile Level 4.2
    "avc1.640028", // H.264 High Profile Level 4.0
    "avc1.4d002a", // H.264 Main Profile Level 4.2
    "avc1.42E028", // H.264 Baseline Level 4.0
  ];
  for (const codec of candidates) {
    try {
      const support = await VideoEncoder.isConfigSupported({
        codec,
        width,
        height,
        bitrate: 5_000_000,
        framerate: fps,
      });
      if (support && support.supported) return codec;
    } catch (e) {}
  }
  return null;
}

async function isAacEncodingSupported(sampleRate = 48000, numberOfChannels = 2) {
  if (typeof AudioEncoder === "undefined") return false;
  try {
    const support = await AudioEncoder.isConfigSupported({
      codec: "mp4a.40.2",
      sampleRate,
      numberOfChannels,
      bitrate: 128_000,
    });
    return Boolean(support && support.supported);
  } catch (e) {
    return false;
  }
}

async function encodeReelWithWebCodecs(onProgress) {
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) throw new Error("No question available to render.");

  pauseVideoPlayback();
  recalculateVideoTimeline();

  const canvas = document.getElementById("video-preview-canvas");
  const width = canvas.width || 1080;
  const height = canvas.height || 1920;
  const fps = 30;
  const totalDuration = Math.max(3, videoState.totalDuration);
  const totalFrames = Math.ceil(totalDuration * fps);

  const avcCodec = await selectSupportedAvcCodec(width, height, fps);
  if (!avcCodec) {
    throw new Error("WEBCODECS_UNSUPPORTED");
  }

  const { Muxer, ArrayBufferTarget } = await loadMp4Muxer();
  const sampleRate = 48000;
  const channels = 2;
  const includeAudio = await isAacEncodingSupported(sampleRate, channels);

  const target = new ArrayBufferTarget();
  const muxerOpts = {
    target,
    video: {
      codec: "avc",
      width,
      height,
    },
    fastStart: "in-memory",
    firstTimestampBehavior: "offset",
  };
  if (includeAudio) {
    muxerOpts.audio = {
      codec: "aac",
      numberOfChannels: channels,
      sampleRate,
    };
  }
  const muxer = new Muxer(muxerOpts);

  let videoErr = null;
  const videoEncoder = new VideoEncoder({
    output: (chunk, meta) => muxer.addVideoChunk(chunk, meta),
    error: (e) => {
      videoErr = e;
    },
  });
  videoEncoder.configure({
    codec: avcCodec,
    width,
    height,
    bitrate: videoState.videoMode === "static" ? 3_500_000 : 5_500_000,
    framerate: fps,
  });

  // 1. Encode Video Frames (Static Reel draws once and reuses frame; Animated steps at exact 30fps!)
  const isStatic = videoState.videoMode === "static";
  if (isStatic) {
    renderVideoFrameAt(0);
  }

  const frameDurationUs = Math.round(1_000_000 / fps);
  for (let i = 0; i < totalFrames; i++) {
    if (!videoState.isExporting) {
      throw new Error("Export cancelled.");
    }
    if (videoErr) throw videoErr;

    const t = i / fps;
    if (!isStatic) {
      renderVideoFrameAt(t);
    }

    const timestampUs = Math.round((i * 1_000_000) / fps);
    const frame = new VideoFrame(canvas, {
      timestamp: timestampUs,
      duration: frameDurationUs,
    });
    videoEncoder.encode(frame, { keyFrame: i % (fps * 2) === 0 });
    frame.close();

    // Prevent encoder queue overflow & keep browser UI responsive
    if (videoEncoder.encodeQueueSize > 8) {
      await new Promise((r) => setTimeout(r, 8));
    } else if (i % 6 === 0) {
      await new Promise((r) => setTimeout(r, 0));
    }

    if (typeof onProgress === "function" && (i % 3 === 0 || i === totalFrames - 1)) {
      const pct = ((i + 1) / totalFrames) * (includeAudio ? 88 : 100);
      onProgress(pct, t, totalDuration);
    }
  }

  await videoEncoder.flush();
  videoEncoder.close();
  if (videoErr) throw videoErr;

  // 2. Render & Encode Synchronized AAC Audio Offline (48kHz Stereo, 128kbps)
  if (includeAudio) {
    let audioErr = null;
    const audioEncoder = new AudioEncoder({
      output: (chunk, meta) => muxer.addAudioChunk(chunk, meta),
      error: (e) => {
        audioErr = e;
      },
    });
    audioEncoder.configure({
      codec: "mp4a.40.2",
      sampleRate,
      numberOfChannels: channels,
      bitrate: 128_000,
    });

    const audioBuffer = await studioAudio.renderOfflineAudioBuffer(q, totalDuration, sampleRate);
    const ch0 = audioBuffer.getChannelData(0);
    const ch1 = audioBuffer.numberOfChannels > 1 ? audioBuffer.getChannelData(1) : ch0;
    const totalSamples = audioBuffer.length;
    const chunkFrames = 4096;

    for (let offset = 0; offset < totalSamples; offset += chunkFrames) {
      if (audioErr) throw audioErr;
      const count = Math.min(chunkFrames, totalSamples - offset);
      const planar = new Float32Array(count * 2);
      planar.set(ch0.subarray(offset, offset + count), 0);
      planar.set(ch1.subarray(offset, offset + count), count);

      const audioData = new AudioData({
        format: "f32-planar",
        sampleRate,
        numberOfFrames: count,
        numberOfChannels: 2,
        timestamp: Math.round((offset * 1_000_000) / sampleRate),
        data: planar,
      });
      audioEncoder.encode(audioData);
      audioData.close();

      if (audioEncoder.encodeQueueSize > 12) {
        await new Promise((r) => setTimeout(r, 4));
      }
    }

    await audioEncoder.flush();
    audioEncoder.close();
    if (audioErr) throw audioErr;
  }

  if (typeof onProgress === "function") {
    onProgress(100, totalDuration, totalDuration);
  }

  muxer.finalize();
  const blob = new Blob([target.buffer], { type: "video/mp4" });
  const modeTag = isStatic ? `static_${Math.round(totalDuration)}s` : "animated";
  const baseFilename = `${(q.exam || "msra").toLowerCase()}_${q.id || q.type}_${modeTag}_reel`;
  return {
    blob,
    mimeType: "video/mp4",
    fileExt: "mp4",
    baseFilename,
    isInstagramReadyMp4: true,
  };
}

// --- Fallback Real-Time MediaRecorder Capture (for browsers without WebCodecs) ---
async function recordVideoToBlob(onProgress) {
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) throw new Error("No question available to render.");

  pauseVideoPlayback();
  studioAudio.init();
  if (studioAudio.ctx && studioAudio.ctx.state === "suspended") {
    try {
      await studioAudio.ctx.resume();
    } catch (e) {}
  }

  recalculateVideoTimeline();
  videoState.currentTime = 0;
  videoState.lastSoundStep = -1;
  videoState.revealSoundPlayed = false;
  renderVideoFrameAt(0);

  const canvas = document.getElementById("video-preview-canvas");
  const fps = 30;
  const canvasStream = canvas.captureStream(fps);

  const audioDest = studioAudio.ctx.createMediaStreamDestination();
  studioAudio.masterGain.connect(audioDest);

  const ghostOsc = studioAudio.ctx.createOscillator();
  const ghostGain = studioAudio.ctx.createGain();
  ghostGain.gain.setValueAtTime(0.00001, studioAudio.ctx.currentTime);
  ghostOsc.connect(ghostGain);
  ghostGain.connect(audioDest);
  try {
    ghostOsc.start();
  } catch (e) {}

  const combinedStream = new MediaStream([
    ...canvasStream.getVideoTracks(),
    ...audioDest.stream.getAudioTracks(),
  ]);

  let mimeType = "video/webm;codecs=vp9";
  let fileExt = "webm";
  if (MediaRecorder.isTypeSupported("video/mp4;codecs=avc1")) {
    mimeType = "video/mp4;codecs=avc1";
    fileExt = "mp4";
  } else if (MediaRecorder.isTypeSupported("video/mp4")) {
    mimeType = "video/mp4";
    fileExt = "mp4";
  } else if (MediaRecorder.isTypeSupported("video/webm;codecs=vp9,opus")) {
    mimeType = "video/webm;codecs=vp9,opus";
    fileExt = "webm";
  } else if (MediaRecorder.isTypeSupported("video/webm")) {
    mimeType = "video/webm";
    fileExt = "webm";
  }

  let recorder;
  try {
    recorder = new MediaRecorder(combinedStream, {
      mimeType: mimeType,
      videoBitsPerSecond: 6000000,
    });
  } catch (err) {
    recorder = new MediaRecorder(combinedStream);
  }

  const recordedChunks = [];
  recorder.ondataavailable = (e) => {
    if (e.data && e.data.size > 0) recordedChunks.push(e.data);
  };

  recorder.start(100);
  await new Promise((resolve) => setTimeout(resolve, 150));
  renderVideoFrameAt(0);

  const totalDuration = videoState.totalDuration;
  const startTime = performance.now();
  let lastExportSoundStep = -1;
  let exportRevealPlayed = false;

  return new Promise((resolve, reject) => {
    const cleanupAudio = () => {
      try {
        ghostOsc.stop();
        ghostOsc.disconnect();
        ghostGain.disconnect();
      } catch (e) {}
      try {
        studioAudio.masterGain.disconnect(audioDest);
      } catch (e) {}
    };

    recorder.onerror = (e) => {
      cleanupAudio();
      reject(new Error(e?.error?.message || "MediaRecorder error during video capture."));
    };

    recorder.onstop = () => {
      cleanupAudio();
      const blob = new Blob(recordedChunks, { type: mimeType });
      const modeTag = videoState.videoMode === "static" ? `static_${Math.round(totalDuration)}s` : "animated";
      const baseFilename = `${(q.exam || "msra").toLowerCase()}_${q.id || q.type}_${modeTag}_reel`;
      resolve({ blob, mimeType, fileExt, baseFilename, isInstagramReadyMp4: false });
    };

    const renderStep = () => {
      if (!videoState.isExporting) {
        try {
          recorder.stop();
        } catch (e) {}
        return;
      }

      const exportTime = (performance.now() - startTime) / 1000;
      const pct = Math.min(100, (exportTime / totalDuration) * 100);
      if (typeof onProgress === "function") {
        onProgress(pct, exportTime, totalDuration);
      }

      renderVideoFrameAt(exportTime);

      if (videoState.videoMode !== "static") {
        const readingEnd = videoState.readingDuration;
        const cyclingStart = readingEnd + 0.5;
        const cyclingEnd = cyclingStart + videoState.cyclingDuration;
        const revealStart = cyclingEnd + (videoState.postCyclingPause || 2.0);
        const optionsCount = (q.options || []).length || 4;

        if (exportTime >= cyclingStart && exportTime < cyclingEnd) {
          const elapsedInCycling = exportTime - cyclingStart;
          const stepDuration = videoState.cyclingDuration / Math.max(1, optionsCount);
          const currentStep = Math.min(optionsCount - 1, Math.floor(elapsedInCycling / stepDuration));
          if (currentStep !== lastExportSoundStep) {
            lastExportSoundStep = currentStep;
            studioAudio.playCycleSound(currentStep, audioDest);
          }
        }

        if (exportTime >= revealStart && !exportRevealPlayed) {
          exportRevealPlayed = true;
          studioAudio.playRevealSound(audioDest);
        }
      }

      if (exportTime < totalDuration) {
        requestAnimationFrame(renderStep);
      } else {
        recorder.stop();
      }
    };

    requestAnimationFrame(renderStep);
  });
}

// Automatically picks fast WebCodecs MP4 encoder, falling back to MediaRecorder if unsupported
async function renderReelVideo(onProgress) {
  try {
    return await encodeReelWithWebCodecs(onProgress);
  } catch (err) {
    if (err && err.message === "Export cancelled.") throw err;
    console.warn("WebCodecs MP4 unavailable, falling back to MediaRecorder:", err);
    return await recordVideoToBlob(onProgress);
  }
}

function setVideoActionButtonsDisabled(disabled) {
  const exportBtn = document.getElementById("video-export-btn");
  const publishBtn = document.getElementById("video-publish-ig-btn");
  if (exportBtn) exportBtn.disabled = disabled;
  if (publishBtn) publishBtn.disabled = disabled;
}

// --- Export Instagram-Ready MP4 Locally (Fast WebCodecs MP4 in Browser, Zero Canva!) ---
async function exportAnimatedVideo() {
  if (videoState.isExporting) return;
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) {
    alert("No question available to export.");
    return;
  }

  const exportBtn = document.getElementById("video-export-btn");
  const originalBtnHTML = exportBtn ? exportBtn.innerHTML : "";
  const statusInfo = document.getElementById("video-export-status");
  const progressContainer = document.getElementById("video-export-progress-bar-container");
  const progressBar = document.getElementById("video-export-progress-bar");

  videoState.isExporting = true;
  setVideoActionButtonsDisabled(true);
  if (exportBtn) exportBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Encoding MP4...';
  if (progressContainer) progressContainer.style.display = "block";
  if (progressBar) progressBar.style.width = "0%";
  if (statusInfo) statusInfo.innerHTML = '<span><i class="fa-solid fa-bolt fa-fade"></i> Encoding Instagram-ready H.264 MP4...</span>';

  try {
    const { blob, mimeType, fileExt, baseFilename, isInstagramReadyMp4 } = await renderReelVideo((pct, cur, tot) => {
      if (progressBar) progressBar.style.width = `${pct.toFixed(0)}%`;
      if (statusInfo) {
        statusInfo.innerHTML = `<span><i class="fa-solid fa-spinner fa-spin"></i> Encoding MP4... ${pct.toFixed(0)}% (${cur.toFixed(1)}s / ${tot.toFixed(1)}s)</span>`;
      }
    });

    let finalBlob = blob;
    let finalFilename = `${baseFilename}.${fileExt}`;

    // Only run local FFmpeg fallback if WebCodecs wasn't available
    if (!isInstagramReadyMp4 && igServerState.mode === "local" && igServerState.ffmpegAvailable) {
      if (progressBar) progressBar.style.width = "90%";
      if (statusInfo) {
        statusInfo.innerHTML = '<span><i class="fa-solid fa-wand-magic-sparkles fa-spin"></i> Converting to Instagram H.264 MP4 via FFmpeg...</span>';
      }
      const resp = await fetch("/api/transcode", {
        method: "POST",
        headers: {
          "Content-Type": mimeType,
          "X-Reel-Meta": encodeReelMetaHeader({ filename: baseFilename }),
        },
        body: blob,
      });
      if (!resp.ok) {
        const errData = await resp.json().catch(() => ({}));
        throw new Error(errData.error || "FFmpeg conversion failed.");
      }
      finalBlob = await resp.blob();
      finalFilename = `${baseFilename}.mp4`;
    }

    const downloadUrl = URL.createObjectURL(finalBlob);
    const a = document.createElement("a");
    a.href = downloadUrl;
    a.download = finalFilename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(downloadUrl);

    const captionText = (document.getElementById("video-caption-textarea")?.value || "").trim();
    if (captionText && navigator.clipboard) {
      navigator.clipboard.writeText(captionText).catch(() => {});
    }

    if (progressBar) progressBar.style.width = "100%";
    if (statusInfo) {
      statusInfo.innerHTML = `<span><i class="fa-solid fa-circle-check" style="color: #10b981;"></i> Saved <strong>${finalFilename}</strong> & copied caption to clipboard!</span>`;
    }
  } catch (err) {
    console.error("Video export error:", err);
    if (statusInfo) {
      statusInfo.innerHTML = `<span style="color: #f87171;"><i class="fa-solid fa-circle-xmark"></i> Export error: ${err.message}</span>`;
    }
  } finally {
    videoState.isExporting = false;
    setVideoActionButtonsDisabled(false);
    if (exportBtn) exportBtn.innerHTML = originalBtnHTML;
    setTimeout(() => {
      if (progressContainer && !videoState.isExporting) progressContainer.style.display = "none";
    }, 1500);
    resetVideoToStart();
  }
}

// --- 1-Click Publish Reel Directly to Instagram (Vercel Cloud OR Local server.py) ---
async function publishReelToInstagram() {
  if (videoState.isExporting) return;
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) {
    alert("No question selected to publish.");
    return;
  }

  const statusInfo = document.getElementById("video-export-status");
  const progressContainer = document.getElementById("video-export-progress-bar-container");
  const progressBar = document.getElementById("video-export-progress-bar");
  const publishBtn = document.getElementById("video-publish-ig-btn");
  const originalBtnHTML = publishBtn ? publishBtn.innerHTML : "";

  await checkLocalServerStatus();
  if (!igServerState.online) {
    if (statusInfo) {
      statusInfo.innerHTML = `<span style="color: #f59e0b;"><i class="fa-solid fa-triangle-exclamation"></i> Backend not detected. Deploy to Vercel or start <code>python server.py</code> locally.</span>`;
    }
    openIgSetupModal();
    return;
  }

  if (!igServerState.igConfigured) {
    if (statusInfo) {
      statusInfo.innerHTML = `<span style="color: #f59e0b;"><i class="fa-solid fa-key"></i> Configure your Instagram credentials first.</span>`;
    }
    openIgSetupModal();
    return;
  }

  if (igServerState.mode === "vercel") {
    if (!igServerState.blobConfigured) {
      if (statusInfo) {
        statusInfo.innerHTML = `<span style="color: #f59e0b;"><i class="fa-solid fa-database"></i> Enable a <strong>Vercel Blob Store</strong> in your Vercel project's Storage tab first (adds <code>BLOB_READ_WRITE_TOKEN</code>).</span>`;
      }
      return;
    }
    if (igServerState.passcodeRequired && !getStoredPasscode()) {
      if (statusInfo) {
        statusInfo.innerHTML = `<span style="color: #f59e0b;"><i class="fa-solid fa-lock"></i> Enter your Vercel publishing passcode once to unlock 1-click posting.</span>`;
      }
      openIgSetupModal();
      return;
    }
  }

  // Ensure caption is never empty — use edited textarea or fall back to generated caption
  const captionEl = document.getElementById("video-caption-textarea");
  let caption = (captionEl && captionEl.value.trim()) || (typeof buildInstagramCaption === "function" ? buildInstagramCaption(q) : "");
  if (caption.length > 2200) {
    caption = caption.slice(0, 2197) + "...";
  }
  const shareFeedEl = document.getElementById("video-share-to-feed-toggle");
  const shareToFeed = shareFeedEl ? shareFeedEl.checked : igServerState.shareToFeed;

  videoState.isExporting = true;
  setVideoActionButtonsDisabled(true);
  if (publishBtn) publishBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Publishing...';
  if (progressContainer) progressContainer.style.display = "block";
  if (progressBar) progressBar.style.width = "4%";
  if (statusInfo) {
    const modeLabel = videoState.videoMode === "static" ? `Static Reel (${videoState.staticDuration}s)` : "Animated Reel";
    statusInfo.innerHTML = `<span><i class="fa-solid fa-bolt fa-fade" style="color: #ec4899;"></i> Step 1/4: Encoding ${modeLabel} to Instagram H.264 MP4...</span>`;
  }

  try {
    // 1. Encode Reel in browser (0% -> 40%)
    const { blob, mimeType, baseFilename, isInstagramReadyMp4 } = await renderReelVideo((pct, cur, tot) => {
      const uiPct = Math.round(pct * 0.4);
      if (progressBar) progressBar.style.width = `${uiPct}%`;
      if (statusInfo) {
        statusInfo.innerHTML = `<span><i class="fa-solid fa-spinner fa-spin" style="color: #ec4899;"></i> Step 1/4: Encoding MP4... ${pct.toFixed(0)}% (${cur.toFixed(1)}s / ${tot.toFixed(1)}s)</span>`;
      }
    });

    // === VERCEL CLOUD FLOW (Direct Blob Upload -> video_url JSON -> Stateless Poll/Publish) ===
    if (igServerState.mode === "vercel") {
      if (!isInstagramReadyMp4 && mimeType !== "video/mp4") {
        throw new Error("Your browser does not support native H.264 MP4 encoding (WebCodecs). Please use Chrome or Edge for Vercel cloud publishing.");
      }

      const passcode = getStoredPasscode();

      // Step 2: Direct client upload to Vercel Blob (bypasses Vercel's 4.5 MB API limit!)
      if (progressBar) progressBar.style.width = "45%";
      if (statusInfo) {
        statusInfo.innerHTML = `<span><i class="fa-solid fa-cloud-arrow-up fa-fade" style="color: #8b5cf6;"></i> Step 2/4: Uploading MP4 (${(blob.size / (1024 * 1024)).toFixed(1)} MB) to Vercel Blob...</span>`;
      }

      const { upload } = await loadVercelBlobClient();
      const mp4File = new File([blob], `${baseFilename}.mp4`, { type: "video/mp4" });
      const uploadedBlob = await upload(`reels/${baseFilename}.mp4`, mp4File, {
        access: "public",
        handleUploadUrl: "/api/blob-upload",
        clientPayload: JSON.stringify({ passcode }),
        onUploadProgress: (evt) => {
          const rawPct = evt && typeof evt.percentage === "number" ? evt.percentage : 0;
          const norm = rawPct > 1 ? rawPct / 100 : rawPct;
          const uiPct = Math.round(45 + norm * 18);
          if (progressBar) progressBar.style.width = `${Math.min(63, uiPct)}%`;
        },
      });

      // Step 3: Create Instagram Reel container with video_url + JSON caption
      if (progressBar) progressBar.style.width = "68%";
      if (statusInfo) {
        statusInfo.innerHTML = '<span><i class="fa-brands fa-instagram fa-fade" style="color: #ec4899;"></i> Step 3/4: Sending video & description to Instagram...</span>';
      }

      const createResp = await fetch("/api/ig-create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Admin-Passcode": passcode,
        },
        body: JSON.stringify({
          video_url: uploadedBlob.url,
          caption: caption,
          share_to_feed: shareToFeed,
        }),
      });
      const createData = await createResp.json();
      if (!createResp.ok || !createData.ok || !createData.container_id) {
        throw new Error(createData.error || "Failed to create Instagram Reel container.");
      }

      // Step 4: Poll Instagram processing & publish as soon as FINISHED (also cleans up Blob!)
      const containerId = createData.container_id;
      let done = false;
      let attempts = 0;
      while (!done && attempts < 45) {
        attempts++;
        await new Promise((r) => setTimeout(r, 3000));

        const pubResp = await fetch("/api/ig-publish", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-Admin-Passcode": passcode,
          },
          body: JSON.stringify({
            container_id: containerId,
            blob_url: uploadedBlob.url,
          }),
        });
        const pubData = await pubResp.json();
        if (!pubResp.ok && pubData.status !== "processing") {
          throw new Error(pubData.error || "Instagram publishing failed.");
        }

        if (pubData.status === "done") {
          done = true;
          if (progressBar) progressBar.style.width = "100%";
          const linkHtml = pubData.permalink
            ? ` <a href="${pubData.permalink}" target="_blank" rel="noopener" style="color: #38bdf8; font-weight: 700; text-decoration: underline; margin-left: 6px;">View Live Reel ↗</a>`
            : "";
          if (statusInfo) {
            statusInfo.innerHTML = `<span style="color: #10b981;"><i class="fa-solid fa-circle-check"></i> <strong>Published live to Instagram with description!</strong>${linkHtml}</span>`;
          }
        } else {
          const uiPct = Math.min(95, 70 + Math.round((attempts / 45) * 25));
          if (progressBar) progressBar.style.width = `${uiPct}%`;
          if (statusInfo) {
            statusInfo.innerHTML = `<span><i class="fa-solid fa-spinner fa-spin" style="color: #8b5cf6;"></i> Step 4/4: Instagram is processing your Reel (${pubData.status_code || "IN_PROGRESS"})...</span>`;
          }
        }
      }
      if (!done) {
        throw new Error("Timed out waiting for Instagram to finish processing your Reel.");
      }
      return;
    }

    // === LOCAL server.py FLOW ===
    if (progressBar) progressBar.style.width = "45%";
    if (statusInfo) {
      statusInfo.innerHTML = '<span><i class="fa-solid fa-cloud-arrow-up fa-fade" style="color: #8b5cf6;"></i> Step 2/4: Sending to local Instagram publisher...</span>';
    }

    const startResp = await fetch("/api/publish-reel", {
      method: "POST",
      headers: {
        "Content-Type": mimeType,
        "X-Reel-Meta": encodeReelMetaHeader({
          filename: baseFilename,
          caption: caption,
          share_to_feed: shareToFeed,
          already_ig_mp4: isInstagramReadyMp4,
        }),
      },
      body: blob,
    });
    const startData = await startResp.json();
    if (!startResp.ok || !startData.ok || !startData.job_id) {
      throw new Error(startData.error || "Failed to start Instagram publish job.");
    }

    const jobId = startData.job_id;
    let done = false;
    while (!done) {
      await new Promise((r) => setTimeout(r, 1500));
      const jobResp = await fetch(`/api/job/${jobId}`, { cache: "no-store" });
      const job = await jobResp.json();
      if (!jobResp.ok) throw new Error(job.error || "Lost connection to publish job.");

      const uiPct = Math.min(100, Math.round(40 + (job.progress || 0) * 0.6));
      if (progressBar) progressBar.style.width = `${uiPct}%`;

      if (job.status === "done") {
        done = true;
        if (progressBar) progressBar.style.width = "100%";
        const linkHtml = job.permalink
          ? ` <a href="${job.permalink}" target="_blank" rel="noopener" style="color: #38bdf8; font-weight: 700; text-decoration: underline; margin-left: 6px;">View Live Reel ↗</a>`
          : "";
        if (statusInfo) {
          statusInfo.innerHTML = `<span style="color: #10b981;"><i class="fa-solid fa-circle-check"></i> <strong>Published live to Instagram with description!</strong>${linkHtml}</span>`;
        }
      } else if (job.status === "error") {
        throw new Error(job.error || job.message || "Publishing failed.");
      } else {
        if (statusInfo) {
          statusInfo.innerHTML = `<span><i class="fa-solid fa-spinner fa-spin" style="color: #8b5cf6;"></i> ${job.message || "Publishing to Instagram..."}</span>`;
        }
      }
    }
  } catch (err) {
    console.error("Direct Instagram publish failed:", err);
    if (statusInfo) {
      statusInfo.innerHTML = `<span style="color: #f87171;"><i class="fa-solid fa-circle-xmark"></i> ${err.message}</span>`;
    }
  } finally {
    videoState.isExporting = false;
    setVideoActionButtonsDisabled(false);
    if (publishBtn) publishBtn.innerHTML = originalBtnHTML;
    resetVideoToStart();
  }
}
