/**
 * Animated Reel Video Studio Module
 * Renders high-retention 9:16 vertical video with kinetic word reading,
 * cycling option spotlight with soft musical notes/boops, and answer reveal.
 * Exports video with synchronized audio directly in the browser via MediaRecorder.
 */

// --- Video Studio State ---
const videoState = {
  activeQuestion: null,
  isPlaying: false,
  currentTime: 0,
  totalDuration: 13.0,
  readingDuration: 5.0,
  cyclingDuration: 4.0, // Default 4.0s (1.0s deliberate review per option)
  postCyclingPause: 2.0, // Default 2.0s suspense pause after options cycling before answer pops up
  revealDuration: 3.5,
  wpm: 300,
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
}

const studioAudio = new StudioAudioEngine();

// --- Lifecycle & Initialization ---
document.addEventListener("DOMContentLoaded", () => {
  initStudioTabs();
  initVideoControls();
  initVideoThemeGrid();
});

// Tab Switcher (Static Carousel vs Animated Video)
function initStudioTabs() {
  const carouselTabBtn = document.getElementById("studio-tab-carousel");
  const videoTabBtn = document.getElementById("studio-tab-video");
  const carouselPane = document.getElementById("carousel-tab-pane");
  const videoPane = document.getElementById("video-tab-pane");

  if (!carouselTabBtn || !videoTabBtn) return;

  carouselTabBtn.addEventListener("click", () => {
    carouselTabBtn.classList.add("active");
    videoTabBtn.classList.remove("active");
    if (carouselPane) carouselPane.style.display = "block";
    if (videoPane) videoPane.style.display = "none";
    pauseVideoPlayback();
  });

  videoTabBtn.addEventListener("click", () => {
    videoTabBtn.classList.add("active");
    carouselTabBtn.classList.remove("active");
    if (carouselPane) carouselPane.style.display = "none";
    if (videoPane) videoPane.style.display = "block";
    syncVideoControlsWithInstaState();
    recalculateVideoTimeline();
    renderVideoFrameAt(0);
    playVideoPlayback();
  });
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
    explSlider.value = instaState.explanationFontSize;
    const label = document.getElementById("val-video-size-explanation");
    if (label) label.textContent = instaState.explanationFontSize;
  }

  const postCycleSlider = document.getElementById("video-post-cycle-pause-slider");
  if (postCycleSlider) {
    postCycleSlider.value = videoState.postCyclingPause;
    const label = document.getElementById("val-video-post-cycle-pause");
    if (label) label.textContent = Number(videoState.postCyclingPause).toFixed(1);
  }

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

  // Video Export Button
  const exportBtn = document.getElementById("video-export-btn");
  if (exportBtn) {
    exportBtn.addEventListener("click", () => {
      exportAnimatedVideo();
    });
  }
}

// --- Timeline Calculation ---
function recalculateVideoTimeline() {
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) return;

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

  // 4. Question Scenario Area (Kinetic Reading Reveal)
  const scenarioStartY = 260;
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
    drawExplanationCard(ctx, q, cardY + 10, width, cardWidth, paddingX);
    return cardY + 10 + (videoState.revealMode === "teaser" ? 130 : 160);
  }
  return cardY;
}

// Explanation Card during Reveal Phase
function drawExplanationCard(ctx, q, startY, width, cardWidth, paddingX) {
  const fontFam = (typeof FONT_MAP !== "undefined" && FONT_MAP[instaState.font]) || "'Outfit', sans-serif";

  if (videoState.revealMode === "teaser") {
    // Teaser Mode Card
    ctx.fillStyle = "rgba(245, 158, 11, 0.2)";
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 2;
    drawRoundedRect(ctx, paddingX, startY, cardWidth, 130, 20);
    ctx.fill();
    ctx.stroke();

    ctx.font = `700 26px ${fontFam}`;
    ctx.fillStyle = "#fcd34d";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("💬 Lock in your guess in the comments!", width / 2, startY + 45);

    ctx.font = `500 20px ${fontFam}`;
    ctx.fillStyle = "rgba(255, 255, 255, 0.9)";
    ctx.fillText("Full clinical rationale & 1000+ MSRA cases at " + (instaState.websiteUrl || "medqstudios.com"), width / 2, startY + 85);
  } else {
    // Full Learning Point Reveal
    const boxHeight = 160;
    ctx.fillStyle = "rgba(0, 0, 0, 0.4)";
    ctx.strokeStyle = "rgba(255, 255, 255, 0.18)";
    ctx.lineWidth = 1.5;
    drawRoundedRect(ctx, paddingX, startY, cardWidth, boxHeight, 20);
    ctx.fill();
    ctx.stroke();

    // Title
    ctx.font = `700 22px ${fontFam}`;
    ctx.fillStyle = "#34d399";
    ctx.textAlign = "left";
    ctx.textBaseline = "top";
    ctx.fillText("💡 Key Learning Point", paddingX + 24, startY + 20);

    // Explanation snippet wrapped
    ctx.font = `400 20px ${fontFam}`;
    ctx.fillStyle = "rgba(255, 255, 255, 0.9)";
    const explText = q.explanation || "Review the pathognomonic clinical signs and guidelines for this presentation.";
    drawWrappedParagraph(ctx, explText, paddingX + 24, startY + 56, cardWidth - 48, 28, 3);
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

// --- Video Export Engine (.mp4 / .webm with Synchronized Audio) ---
async function exportAnimatedVideo() {
  if (videoState.isExporting) return;
  const q = videoState.activeQuestion || instaState.activeQuestion;
  if (!q) {
    alert("No question available to export.");
    return;
  }

  pauseVideoPlayback();
  studioAudio.init();

  const exportBtn = document.getElementById("video-export-btn");
  const originalBtnHTML = exportBtn ? exportBtn.innerHTML : "";
  const statusInfo = document.getElementById("video-export-status");
  const progressContainer = document.getElementById("video-export-progress-bar-container");
  const progressBar = document.getElementById("video-export-progress-bar");

  videoState.isExporting = true;
  if (exportBtn) {
    exportBtn.disabled = true;
    exportBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Rendering Video...';
  }
  if (progressContainer) progressContainer.style.display = "block";
  if (progressBar) progressBar.style.width = "0%";
  if (statusInfo) statusInfo.innerHTML = '<span><i class="fa-solid fa-gear fa-spin"></i> Initializing video capture & audio stream...</span>';

  // 1. Prepare Canvas & Audio Stream
  const canvas = document.getElementById("video-preview-canvas");
  const fps = 30;
  const canvasStream = canvas.captureStream(fps);

  // Audio destination node for recording
  const audioDest = studioAudio.ctx.createMediaStreamDestination();
  // Master gain also outputs to audioDest during export
  studioAudio.masterGain.connect(audioDest);

  // Combined video & audio tracks
  const combinedStream = new MediaStream([
    ...canvasStream.getVideoTracks(),
    ...audioDest.stream.getAudioTracks(),
  ]);

  // Determine optimal MIME type
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
      videoBitsPerSecond: 6000000, // 6 Mbps high fidelity
    });
  } catch (err) {
    console.warn("High bitrate recorder init failed, falling back to standard:", err);
    recorder = new MediaRecorder(combinedStream);
  }

  const recordedChunks = [];
  recorder.ondataavailable = (e) => {
    if (e.data && e.data.size > 0) {
      recordedChunks.push(e.data);
    }
  };

  const filename = `${(q.exam || "msra").toLowerCase()}_${q.type}_reel_animated.${fileExt}`;

  // 2. Start recording loop
  recorder.start(100);

  const totalDuration = videoState.totalDuration;
  const startTime = performance.now();
  let exportTime = 0;
  let lastExportSoundStep = -1;
  let exportRevealPlayed = false;

  const renderExportStep = () => {
    if (!videoState.isExporting) return;

    const now = performance.now();
    exportTime = (now - startTime) / 1000;

    const pct = Math.min(100, (exportTime / totalDuration) * 100);
    if (progressBar) progressBar.style.width = `${pct.toFixed(0)}%`;
    if (statusInfo) {
      statusInfo.innerHTML = `<span><i class="fa-solid fa-spinner fa-spin"></i> Rendering Reel... ${pct.toFixed(0)}% (${exportTime.toFixed(1)}s / ${totalDuration.toFixed(1)}s)</span>`;
    }

    renderVideoFrameAt(exportTime);

    // Audio triggers during export:
    const readingEnd = videoState.readingDuration;
    const cyclingStart = readingEnd + 0.5;
    const cyclingEnd = cyclingStart + videoState.cyclingDuration;
    const revealStart = cyclingEnd + (videoState.postCyclingPause || 2.0);
    const optionsCount = (q.options || []).length || 4;

    if (exportTime >= cyclingStart && exportTime < cyclingEnd) {
      const elapsedInCycling = exportTime - cyclingStart;
      const totalSteps = optionsCount;
      const stepDuration = videoState.cyclingDuration / Math.max(1, totalSteps);
      const currentStep = Math.min(totalSteps - 1, Math.floor(elapsedInCycling / stepDuration));

      if (currentStep !== lastExportSoundStep) {
        lastExportSoundStep = currentStep;
        studioAudio.playCycleSound(currentStep, audioDest);
      }
    }

    if (exportTime >= revealStart && !exportRevealPlayed) {
      exportRevealPlayed = true;
      studioAudio.playRevealSound(audioDest);
    }

    if (exportTime < totalDuration) {
      requestAnimationFrame(renderExportStep);
    } else {
      // Completed!
      finishExport();
    }
  };

  const finishExport = () => {
    recorder.onstop = () => {
      // Disconnect export audio node
      try {
        studioAudio.masterGain.disconnect(audioDest);
      } catch (e) {}

      const blob = new Blob(recordedChunks, { type: mimeType });
      const downloadUrl = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = downloadUrl;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(downloadUrl);

      videoState.isExporting = false;
      if (exportBtn) {
        exportBtn.disabled = false;
        exportBtn.innerHTML = originalBtnHTML;
      }
      if (progressContainer) progressContainer.style.display = "none";
      if (statusInfo) {
        statusInfo.innerHTML = `<span><i class="fa-solid fa-circle-check" style="color: #10b981;"></i> Video saved! Check your downloads for <strong>${filename}</strong></span>`;
      }
      resetVideoToStart();
    };

    recorder.stop();
  };

  // Launch render loop
  requestAnimationFrame(renderExportStep);
}
