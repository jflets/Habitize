function goalAmountButtons() {
    const decrementButton = document.querySelector(".decrement-button");
    const incrementButton = document.querySelector(".increment-button");
    const goalInput = document.querySelector("#id_goal_amount"); // Update the selector to target the existing input

    decrementButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default button behavior
        let currentValue = parseInt(goalInput.value);
        if (!isNaN(currentValue) && currentValue > 0) {
            goalInput.value = currentValue - 1;
        }
    });

    incrementButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default button behavior
        let currentValue = parseInt(goalInput.value);
        if (!isNaN(currentValue)) {
            goalInput.value = currentValue + 1;
        }
    });
}

document.addEventListener("DOMContentLoaded", goalAmountButtons);

function valueButtons() {
    const decrementValueButton = document.querySelector(".decrement-value-button");
    const incrementValueButton = document.querySelector(".increment-value-button");
    const valueInput = document.querySelector("#id_value"); // Update the selector to target the existing input

    decrementValueButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default button behavior
        let currentValue = parseInt(valueInput.value);
        if (!isNaN(currentValue) && currentValue > 0) {
            valueInput.value = currentValue - 1;
        }
    });

    incrementValueButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default button behavior
        let currentValue = parseInt(valueInput.value);
        if (!isNaN(currentValue)) {
            valueInput.value = currentValue + 1;
        }
    });
}

document.addEventListener("DOMContentLoaded", valueButtons);