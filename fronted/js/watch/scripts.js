let display = document.getElementById("display-text");
let start = document.getElementById("start");
let pause = document.getElementById("pause");
let reset = document.getElementById("reset");

let progressCircle = document.getElementById("progress-circle");

let min = 25;
let sec = 0;

let totalTime = 25 * 60;

let timer;
let is_activate = false;

function update(min, sec) {

    if (min < 10) {
        min = "0" + min;
    }

    if (sec < 10) {
        sec = "0" + sec;
    }

    display.textContent = `${min}:${sec}`;
}

function updateProgress() {

    let currentTime = (min * 60) + sec;

    let progress =
        (754 * currentTime) / totalTime;

    progressCircle.style.strokeDashoffset = 754 - progress;
}

update(min, sec);
updateProgress();

start.addEventListener("click", () => {

    if (is_activate) {
        return;
    }

    is_activate = true;

    timer = setInterval(() => {

        if (sec === 0) {

            if (min === 0) {
                clearInterval(timer);
                is_activate = false;
                return;
            }

            min--;
            sec = 59;

        } else {
            sec--;
        }

        update(min, sec);
        updateProgress();

    }, 1000);

});

pause.addEventListener("click", () => {

    clearInterval(timer);
    is_activate = false;

});

reset.addEventListener("click", () => {

    clearInterval(timer);

    min = 25;
    sec = 0;

    is_activate = false;

    update(min, sec);
    updateProgress();

});