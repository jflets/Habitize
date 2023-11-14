// Function to update progress bars based on data-progress attribute
function updateProgressBars() {
    // Select all elements with the class "progress-bar"
    const progressBars = document.querySelectorAll(".progress-bar");

    // Iterate through each progress bar element
    progressBars.forEach(function (progressBar) {
        // Get the progress percentage from the data-progress attribute
        const progress = progressBar.getAttribute("data-progress");

        // Set the width of the progress bar based on the progress percentage
        progressBar.style.width = progress + "%";
    });
}

// Event listener to execute the updateProgressBars function when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", updateProgressBars);
