import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="CogniRead", layout="centered")
st.title("🧠 CogniRead – Speed Reading Aid")

html(
'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">

<style>
:root {
    --bg: #121212;
    --panel: #1e1e1e;
    --text: #eaeaea;
    --accent: #ff4d4d;
    --border: #3a3a3a;
}

* {
    box-sizing: border-box;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

body {
    background: var(--bg);
    color: var(--text);
    margin: 0;
}

.container {
    max-width: 900px;
    margin: auto;
    background: var(--panel);
    padding: 24px;
    border-radius: 12px;
}

/* ===== READER ===== */
.reader-box {
    height: 240px;
    background: #0f0f0f;
    border-top: 2px solid var(--border);
    border-bottom: 2px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
}

.reader-word {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    align-items: center;
    width: 100%;
    font-size: 56px;
    font-family: "JetBrains Mono", monospace;
}

.left {
    text-align: right;
    padding-right: 6px;
}

.center {
    color: var(--accent);
    text-align: center;
    min-width: 1ch;
}

.right {
    text-align: left;
    padding-left: 6px;
}

/* ===== INPUT ===== */
textarea {
    width: 100%;
    height: 120px;
    background: #111;
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px;
    resize: vertical;
}

/* ===== CONTROLS ===== */
.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 16px;
}

button {
    background: #2a2a2a;
    color: var(--text);
    border: 1px solid var(--border);
    padding: 10px 16px;
    border-radius: 6px;
    cursor: pointer;
}

button:hover {
    background: #333;
}

label {
    display: flex;
    align-items: center;
    gap: 8px;
}
</style>
</head>

<body>
<div class="container">

    <div class="reader-box">
        <div id="reader" class="reader-word">
            <div class="left"></div>
            <div class="center"></div>
            <div class="right"></div>
        </div>
    </div>

    <textarea id="textInput" placeholder="Paste your text here..."></textarea>

    <div class="controls">
        <button onclick="play()">Play</button>
        <button onclick="pause()">Pause</button>
        <button onclick="reset()">Reset</button>

        <label>
            WPM
            <input type="range" min="100" max="1000" value="300" id="wpm">
            <span id="wpmVal">300</span>
        </label>
    </div>
</div>

<script>
let words = [];
let index = 0;
let timer = null;
let paused = true;

const reader = document.getElementById("reader");
const left = reader.children[0];
const center = reader.children[1];
const right = reader.children[2];
const wpmSlider = document.getElementById("wpm");
const wpmVal = document.getElementById("wpmVal");

wpmSlider.oninput = () => wpmVal.innerText = wpmSlider.value;

function play() {
    if (!words.length) {
        const text = document.getElementById("textInput").value.trim();
        if (!text) return;
        words = text.split(/\\s+/);
        index = 0;
    }
    paused = false;
    loop();
}

function pause() {
    paused = true;
    clearTimeout(timer);
}

function reset() {
    pause();
    words = [];
    index = 0;
    left.textContent = "";
    center.textContent = "";
    right.textContent = "";
}

function loop() {
    if (paused || index >= words.length) return;

    renderWord(words[index]);

    let delay = 60000 / wpmSlider.value;
    if (/[.,!?]$/.test(words[index])) delay += 120;

    index++;
    timer = setTimeout(loop, delay);
}

function renderWord(word) {
    const clean = word.replace(/[^a-zA-Z0-9]/g, "");
    const len = clean.length;

    let orp = 0;
    if (len >= 2 && len <= 3) orp = 1;
    else if (len >= 4 && len <= 7) orp = 2;
    else if (len >= 8) orp = 3;
    orp = Math.min(orp, len - 1);

    left.textContent = clean.slice(0, orp);
    center.textContent = clean.charAt(orp) || "";
    right.textContent = clean.slice(orp + 1);
}
</script>
</body>
</html>
''',
height=780
)
