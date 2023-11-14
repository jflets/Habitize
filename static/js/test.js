const {
  goalAmountButtons,
  valueButtons,
  toggleAdvancedSettings,
} = require('./edit.js');

// Initialize HTML structure before each test
document.body.innerHTML = `
  <input type="number" id="id_goal_amount" value="5" />
  <button class="decrement-button">Decrement</button>
  <button class="increment-button">Increment</button>
  <input type="number" id="id_value" value="10" />
  <button class="decrement-value-button">Decrement Value</button>
  <button class="increment-value-button">Increment Value</button>
  <div id="advanced-settings" style="display: none"></div>
  <button id="toggle-advanced-settings">Show Advanced Settings</button>
`;

// Test suite for goalAmountButtons function
describe('goalAmountButtons', () => {
  beforeEach(() => {
      goalAmountButtons();
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

      expect(goalInput.value).toBe('5');
  });
});

// Test suite for valueButtons function
describe('valueButtons', () => {
  beforeEach(() => {
      valueButtons();
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

      expect(valueInput.value).toBe('10');
  });
});

// Test suite for toggleAdvancedSettings function
describe('toggleAdvancedSettings', () => {
  let advancedSettings;
  let showAdvancedButton;

  beforeEach(() => {
      // Create the necessary HTML structure before each test
      document.body.innerHTML = `
          <div id="advanced-settings" style="display: none"></div>
          <button id="toggle-advanced-settings">Show Advanced Settings</button>
      `;
      advancedSettings = document.querySelector('#advanced-settings');
      showAdvancedButton = document.querySelector('#toggle-advanced-settings');
      toggleAdvancedSettings(); // Initialize the event listeners before each test
  });

  test('Show Advanced Settings button shows advanced settings', () => {
      // Mock window.confirm to return true
      window.confirm = jest.fn(() => true);

      showAdvancedButton.click();
      expect(advancedSettings.style.display).toBe('block');
      expect(showAdvancedButton.textContent).toBe('Hide Advanced Settings');

      // Restore the original window.confirm function
      window.confirm.mockRestore();
  });

  test('Hide Advanced Settings button hides advanced settings', () => {
      // Simulate advanced settings being shown
      advancedSettings.style.display = 'block';

      // Mock window.confirm to return true
      window.confirm = jest.fn(() => true);

      showAdvancedButton.click();
      expect(advancedSettings.style.display).toBe('none');
      expect(showAdvancedButton.textContent).toBe('Show Advanced Settings');

      // Restore the original window.confirm function
      window.confirm.mockRestore();
  });
});
