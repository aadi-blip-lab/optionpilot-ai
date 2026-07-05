/* ======================================
   OPTIONPILOT UI ENGINE
====================================== */

const body = document.body;

const modes = document.querySelectorAll(".mode");

modes.forEach(button => {

    button.addEventListener("click", () => {

        modes.forEach(btn => btn.classList.remove("active"));

        button.classList.add("active");

        const mode = button.textContent.trim().toLowerCase();

        body.classList.remove("focus","chill","learn");

        body.classList.add(mode);

        localStorage.setItem("theme",mode);

    });

});

const savedTheme = localStorage.getItem("theme");

if(savedTheme){

    body.classList.remove("focus","chill","learn");

    body.classList.add(savedTheme);

    modes.forEach(btn=>{

        btn.classList.remove("active");

        if(btn.textContent.trim().toLowerCase()==savedTheme){

            btn.classList.add("active");

        }

    });

}

const enterButton=document.querySelector(".primary");

enterButton.addEventListener("click",()=>{

    alert("Workspace coming in the next update 🚀");

});
