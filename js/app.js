/* ==========================================================
   OPTIONPILOT
   APP.JS v2
==========================================================*/

const body = document.body;

/* ==========================================
   Theme Engine
==========================================*/

const modeButtons = document.querySelectorAll(".mode");

const savedTheme = localStorage.getItem("theme") || "focus";

body.className = savedTheme;

modeButtons.forEach(button => {

    if (button.dataset.theme === savedTheme) {
        button.classList.add("active");
    }

    button.addEventListener("click", () => {

        modeButtons.forEach(btn => btn.classList.remove("active"));

        button.classList.add("active");

        body.className = button.dataset.theme;

        localStorage.setItem("theme", button.dataset.theme);

    });

});


/* ==========================================
   Elements
==========================================*/

const digitalClock = document.getElementById("digitalClock");
const todayDate = document.getElementById("todayDate");

const hourHand = document.getElementById("hourHand");
const minuteHand = document.getElementById("minuteHand");
const secondHand = document.getElementById("secondHand");


/* ==========================================
   Clock
==========================================*/

function updateClock() {

    const now = new Date();

    const indiaTime = new Date(

        now.toLocaleString("en-US", {
            timeZone: "Asia/Kolkata"
        })

    );

    digitalClock.textContent = indiaTime.toLocaleTimeString("en-IN", {
        hour12: false
    });

    const seconds = indiaTime.getSeconds();
    const minutes = indiaTime.getMinutes();
    const hours = indiaTime.getHours();

    secondHand.style.transform =
        `translateX(-50%) rotate(${seconds * 6}deg)`;

    minuteHand.style.transform =
        `translateX(-50%) rotate(${minutes * 6 + seconds * 0.1}deg)`;

    hourHand.style.transform =
        `translateX(-50%) rotate(${(hours % 12) * 30 + minutes * 0.5}deg)`;

}


/* ==========================================
   Backend Status
==========================================*/

async function loadStatus() {

    try {

        const response = await fetch(
            "https://optionpilot-ai.onrender.com/api/status"
        );

        const data = await response.json();

        document.getElementById("marketStatus").textContent =
            data.market.replace("_", " ");

        document.getElementById("marketCountdown").textContent =
            data.time;

        document.getElementById("todayDate").textContent =
            data.date;

    }

    catch (error) {

        console.error(error);

        document.getElementById("marketStatus").textContent =
            "OFFLINE";

    }

}


/* ==========================================
   Workspace Button
==========================================*/

document
.getElementById("workspaceBtn")
.addEventListener("click", () => {

    alert("Workspace coming soon.");

});


/* ==========================================
   Start
==========================================*/

updateClock();

loadStatus();

setInterval(updateClock, 1000);

setInterval(loadStatus, 5000);
