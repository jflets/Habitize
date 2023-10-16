function goalAmountButtons() {
    const decrementButton = document.querySelector(".decrement-button");
    const incrementButton = document.querySelector(".increment-button");
    const goalInput = document.querySelector("#id_goal_amount");
    let isButtonDisabled = false;
    let isAdvancedSettingsOpen = false;

    function handleButtonClick(event, increment) {
        event.preventDefault();
        if (!isButtonDisabled) {
            if (!isAdvancedSettingsOpen) {
                isButtonDisabled = true;
                let currentValue = parseInt(goalInput.value);
                if (!isNaN(currentValue)) {
                    if (increment) {
                        goalInput.value = currentValue + 1;
                    } else {
                        if (currentValue > 0) {
                            goalInput.value = currentValue - 1;
                        }
                    }
                    setTimeout(() => {
                        isButtonDisabled = false;
                    }, 500);
                }
            }
        }
    }

    decrementButton.addEventListener("click", (event) => handleButtonClick(event, false));
    incrementButton.addEventListener("click", (event) => handleButtonClick(event, true));
}

function valueButtons() {
    const decrementValueButton = document.querySelector(".decrement-value-button");
    const incrementValueButton = document.querySelector(".increment-value-button");
    const valueInput = document.querySelector("#id_value");
    let isButtonDisabled = false;
    let isAdvancedSettingsOpen = false;

    function handleButtonClick(event, increment) {
        event.preventDefault();
        if (!isButtonDisabled) {
            if (!isAdvancedSettingsOpen) {
                isButtonDisabled = true;
                let currentValue = parseInt(valueInput.value);
                if (!isNaN(currentValue)) {
                    if (increment) {
                        valueInput.value = currentValue + 1;
                    } else {
                        if (currentValue > 0) {
                            valueInput.value = currentValue - 1;
                        }
                    }
                    setTimeout(() => {
                        isButtonDisabled = false;
                    }, 500);
                }
            }
        }
    }

    decrementValueButton.addEventListener("click", (event) => handleButtonClick(event, false));
    incrementValueButton.addEventListener("click", (event) => handleButtonClick(event, true));
}

function toggleAdvancedSettings() {
    const advancedSettings = document.getElementById("advanced-settings");
    const toggleButton = document.getElementById("toggle-advanced-settings");

    toggleButton.addEventListener("click", function () {
        if (advancedSettings.style.display === "none") {
            const confirmation = window.confirm("Are you sure you want to make changes to this habit?");
            if (confirmation) {
                advancedSettings.style.display = "block";
                isAdvancedSettingsOpen = true;
                toggleButton.textContent = "Hide Advanced Settings";
            }
        } else {
            advancedSettings.style.display = "none";
            isAdvancedSettingsOpen = false;
            toggleButton.textContent = "Show Advanced Settings";
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    goalAmountButtons();
    valueButtons();
    toggleAdvancedSettings();
});

module.exports = { goalAmountButtons, valueButtons, toggleAdvancedSettings };
