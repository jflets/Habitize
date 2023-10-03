const { goalAmountButtons, valueButtons } = require('./edit.js');

// Create a mock HTML structure to simulate the buttons and input fields
document.body.innerHTML = `
    <input type="number" id="id_goal_amount" value="5" />
    <button class="decrement-button">Decrement</button>
    <button class="increment-button">Increment</button>
    <input type="number" id="id_value" value="10" />
    <button class="decrement-value-button">Decrement Value</button>
    <button class="increment-value-button">Increment Value</button>
`;

describe('goalAmountButtons', () => {
    beforeEach(() => {
        goalAmountButtons(); // Initialize the event listeners before each test
    });

    test('Decrement button decreases goal amount', () => {
        const decrementButton = document.querySelector('.decrement-button');
        const goalInput = document.querySelector('#id_goal_amount');

        decrementButton.click();

        expect(goalInput.value).toBe('4');
    });

    test('Increment button increases goal amount', () => {
        const incrementButton = document.querySelector('.increment-button');
        const goalInput = document.querySelector('#id_goal_amount');

        incrementButton.click();

        expect(goalInput.value).toBe('6');
    });

});

describe('valueButtons', () => {
    beforeEach(() => {
        valueButtons(); // Initialize the event listeners before each test
    });

    test('Decrement Value button decreases value', () => {
        const decrementValueButton = document.querySelector('.decrement-value-button');
        const valueInput = document.querySelector('#id_value');

        decrementValueButton.click();

        expect(valueInput.value).toBe('9');
    });

    test('Increment Value button increases value', () => {
        const incrementValueButton = document.querySelector('.increment-value-button');
        const valueInput = document.querySelector('#id_value');

        incrementValueButton.click();

        expect(valueInput.value).toBe('11');
    });

});
