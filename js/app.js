/* ==========================================================
   OPTIONPILOT
   APP.JS v1
==========================================================*/

const body = document.body;

/* ==========================================
   Theme Engine
==========================================*/

const modeButtons = document.querySelectorAll(".mode");

const savedTheme = localStorage.getItem("theme") || "focus";

body.className = savedTheme;

modeButtons.forEach(btn => {

    if(btn.dataset.theme === savedTheme){

        btn.classList.add("active");

    }

    btn.addEventListener("click",()=>{

        modeButtons.forEach(b=>b.classList.remove("active"));

        btn.classList.add("active");

        body.className = btn.dataset.theme;

        localStorage.setItem("theme",btn.dataset.theme);

    });

});


/* ==========================================
   Clock Elements
==========================================*/

const digitalClock = document.getElementById("digitalClock");
const todayDate = document.getElementById("todayDate");

const hourHand = document.getElementById("hourHand");
const minuteHand = document.getElementById("minuteHand");
const secondHand = document.getElementById("secondHand");

const marketStatus = document.getElementById("marketStatus");
const marketCountdown = document.getElementById("marketCountdown");


/* ==========================================
   Clock
==========================================*/

function updateClock(){

    const now = new Date();

    const indiaTime = new Date(

        now.toLocaleString("en-US",{

            timeZone:"Asia/Kolkata"

        })

    );

    const hours = indiaTime.getHours();

    const minutes = indiaTime.getMinutes();

    const seconds = indiaTime.getSeconds();

    digitalClock.textContent =

        indiaTime.toLocaleTimeString("en-IN",{

            hour12:false

        });

    todayDate.textContent =

        indiaTime.toLocaleDateString("en-IN",{

            weekday:"long",

            day:"numeric",

            month:"long",

            year:"numeric"

        });

    const secondDeg = seconds * 6;

    const minuteDeg = minutes * 6 + seconds * 0.1;

    const hourDeg = (hours % 12) * 30 + minutes * 0.5;

    secondHand.style.transform =
        `translateX(-50%) rotate(${secondDeg}deg)`;

    minuteHand.style.transform =
        `translateX(-50%) rotate(${minuteDeg}deg)`;

    hourHand.style.transform =
        `translateX(-50%) rotate(${hourDeg}deg)`;

    updateMarket(indiaTime);

}


/* ==========================================
   Indian Market Engine
==========================================*/

function updateMarket(now){

    const day = now.getDay();

    if(day === 0){

        marketStatus.textContent = "Weekend";

        marketStatus.className="market-status market-closed";

        marketCountdown.textContent="Market opens tomorrow at 09:15";

        return;

    }

    if(day === 6){

        marketStatus.textContent = "Weekend";

        marketStatus.className="market-status market-closed";

        marketCountdown.textContent="Market opens in 2 days";

        return;

    }

    const currentMinutes =

        now.getHours()*60 + now.getMinutes();

    const open = 9*60 + 15;

    const close = 15*60 + 30;

    if(currentMinutes < open){

        marketStatus.textContent="Pre Market";

        marketStatus.className="market-status market-wait";

        const diff = open-currentMinutes;

        const h=Math.floor(diff/60);

        const m=diff%60;

        marketCountdown.textContent=
        `Opens in ${h}h ${m}m`;

    }

    else if(currentMinutes < close){

        marketStatus.textContent="Market Live";

        marketStatus.className="market-status market-open";

        const diff = close-currentMinutes;

        const h=Math.floor(diff/60);

        const m=diff%60;

        marketCountdown.textContent=
        `Closes in ${h}h ${m}m`;

    }

    else{

        marketStatus.textContent="Market Closed";

        marketStatus.className="market-status market-closed";

        const tomorrowOpen=(24*60-currentMinutes)+open;

        const h=Math.floor(tomorrowOpen/60);

        const m=tomorrowOpen%60;

        marketCountdown.textContent=
        `Opens in ${h}h ${m}m`;

    }

}


/* ==========================================
   Fake Quotes (Temporary)
==========================================*/

async function loadStatus() {

    try {

        const response = await fetch(
            "https://optionpilot-ai.onrender.com/api/status"
        );

        const data = await response.json();

        document.getElementById("marketStatus").textContent =
            data.market;

        document.getElementById("marketCountdown").textContent =
            data.countdown;

    } catch (error) {

        console.error(error);

        document.getElementById("marketStatus").textContent =
            "Disconnected";

    }

}

loadStatus();

setInterval(loadStatus,5000);


/* ==========================================
   Workspace Button
==========================================*/

document.getElementById("workspaceBtn")
.addEventListener("click",()=>{

    alert("Workspace coming in Version 2");

});


/* ==========================================
   Start
==========================================*/

updateClock();

setInterval(updateClock,1000);
