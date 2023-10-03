function updateProgressBars() {
    const progressBars = document.querySelectorAll(".progress-bar");
    progressBars.forEach(function (progressBar) {
        const progress = progressBar.getAttribute("data-progress");
        progressBar.style.width = progress + "%";
    });
}

document.addEventListener("DOMContentLoaded", updateProgressBars);