import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Speed Reader",
    layout="centered",
)

st.title("🧠 Speed Reading App")

html(
'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Speed Reader</title>

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
    margin: 0;
    background: var(--bg);
    color: var(--text);
}

.container {
    max-width: 900px;
    margin: auto;
    background: var(--panel);
    padding: 24px;
    border-radius: 12px;
}

/* BIG READER BOX */
.reader-box {
    height: 220px;
    background: #0f0f0f;
    border-top: 2px solid var(--border);
    border-bottom: 2px solid var(--border);
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 24px;
    overflow: hidden;
    position: relative;
}

.word {
    position: absolute;
    display: flex;
    font-size: 56px;
    font-family: "JetBrains Mono", monospace;
}

.char {
    color: var(--text);
}

.char.orp {
    color: var(--accent);
}

/* INPUT BELOW */
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

    <!-- OUTPUT -->
    <div class="reader-box">
        <div id="display" class="word"></div>
    </div>

    <!-- INPUT -->
    <textarea id="textInput" placeholder="Paste your text here..."></textarea>

    <div class="controls">
        <button onclick="play()">Play</button>
        <button onclick="pause()">Pause</button>
        <button onclick="reset()">Reset</button>

        <label>
            WPM
            <input type="range" min="100" max="1000" value="300" id="wpmSlider">
            <span id="wpmValue">300</span>
        </label>
    </div>
</div>

<script>
let words = [];
let index = 0;
let timer = null;
let paused = true;

const display = document.getElementById("display");
const slider = document.getElementById("wpmSlider");
const wpmValue = document.getElementById("wpmValue");

slider.oninput = () => wpmValue.innerText = slider.value;

function play() {
    if (!words.length) {
        const text = document.getElementById("textInput").value;
        words = text.trim().split(/\\s+/);
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
    display.innerHTML = "";
    display.style.transform = "translateX(0)";
}

function loop() {
    if (paused || index >= words.length) return;

    showWord(words[index]);

    let delay = 60000 / slider.value;
    if (/[.,!?]$/.test(words[index])) delay += 100;

    index++;
    timer = setTimeout(loop, delay);
}

function showWord(word) {
    display.innerHTML = "";

    const chars = word.split("");
    let orpIndex = 1;
    if (word.length <= 3) orpIndex = 1;
    else if (word.length <= 7) orpIndex = 2;
    else orpIndex = 3;

    chars.forEach((c, i) => {
        const span = document.createElement("span");
        span.className = "char" + (i === orpIndex ? " orp" : "");
        span.innerText = c;
        display.appendChild(span);
    });

    const orpChar = display.children[orpIndex];
    const box = display.parentElement;
    const boxCenter = box.offsetWidth / 2;
    const orpCenter = orpChar.offsetLeft + orpChar.offsetWidth / 2;

    display.style.transform = `translateX(${boxCenter - orpCenter}px)`;
}
</script>
</body>
</html>
''',
height=760
)
