# Testing Schedule
## Application Settings

1. **Security Testing:**
   - Verify that unauthorized users cannot access restricted content.
   - Check the security measures in place, including authentication and authorization.

2. **Color Themes and Fonts:**
   - Confirm that user preferences for color themes are saved and applied consistently across the application.
   - Verify that fonts and colors match the design guidelines.

## Landing Page

1. **Security Testing:**
   - Ensure that unauthorized users cannot access restricted content.
   - Check if the navigation is secure.

2. **Navigation Testing:**
   - Test navigation links to other pages.

3. **Responsive Design:**
   - Check for responsive design on various devices.

| **Feature**       | **Expected Outcome**                                                       | **Testing Performed**                                            | **Result**                            | **Pass/Fail** |
|:-----------------:|:--------------------------------------------------------------------------:|:----------------------------------------------------------------:|:-------------------------------------:|:-------------:|
| Nav links         | Nav links should load the corresponding page                               | Click the nav links                                              | All links open the appropriate pages  | Pass          |
| Links             | Links should load the appropriate content                                  | Click the signup hero link                                       | Link loads the signup page            | Pass          |
| Logo link         | Logo should act as a home button, redirecting the user to the landing page | Click the logo                                                   | Link loads the landing page           | Pass          |
| Responsive design | Page should adapt to different screen sizes                                | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes | Pass          |


## Login Page

1. **Security Testing:**
   - Test user authentication by entering valid and invalid credentials.

2. **Error Handling:**
   - Check for appropriate error messages when entering incorrect login credentials.

3. **Password Reset:**
   - Test the "Forgot Password" feature for password recovery.

4. **Successful Login:**
   - Ensure successful redirection to the dashboard upon successful login.

| **Feature**                            | **Expected Outcome**                                                                                    | **Testing Performed**                                            | **Result**                                                             | **Pass/Fail** |
|:--------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------:|:----------------------------------------------------------------------:|:-------------:|
| Nav links                              | Nav links should load the corresponding page                                                            | Click the nav links                                              | All links open the appropriate pages                                   | Pass          |
| Logo link                              | Logo should act as a home button, redirecting the user to the landing page                              | Click the logo                                                   | Link loads the landing page                                            | Pass          |
| Google login link (confirmation page)  | Load confirmation to proceed to google login                                                            | Click google login link                                          | Loads confirm proceed to google login page                             | Pass          |
| Confirm proceed to google login button | Load the google login page                                                                              | Click google confirm button                                      | Loads google login page                                                | Pass          |
| Username input box                     | Allow user to type username                                                                             | Click on input box                                               | Allows user to type username                                           | Pass          |
| Password input box                     | Allow user to type password                                                                             | Click on input box                                               | Allows user to type password                                           | Pass          |
| Invalid user details                   | Error message should be displayed notifying user of invalid user details, no dashboard should be loaded | Type in invalid user details                                     | Error message is displayed and user is not redirected to any dashboard | Pass          |
| Sign in button                         | Signs user in and loads Dashboard page                                                                  | Click sign in                                                    | Loads user Dashboard                                                   | Pass          |
| Forgot password link                   | Loads the password reset page                                                                           | Click forgot password                                            | Loads password reset page                                              | Pass          |
| Responsive design                      | Page should adapt to different screen sizes                                                             | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                                  | Pass          |



## Signup Page

1. **Security Testing:**
   - Verify that only authorized users can register.
   - Check that user registration is secure.

2. **Validation Testing:**
   - Check for validation of required fields (email, password, and username).
   - Ensure that input validation works correctly.

3. **Registration Errors:**
   - Confirm that appropriate error messages are displayed for registration issues.

4. **Email Confirmation:**
   - Test the email confirmation process to ensure it works as expected.

| **Feature**                                   | **Expected Outcome**                                                                                    | **Testing Performed**                                            | **Result**                                                             | **Pass/Fail** |
|:---------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------:|:----------------------------------------------------------------------:|:-------------:|
| Nav links                                     | Nav links should load the corresponding page                                                            | Click the nav links                                              | All links open the appropriate pages                                   | Pass          |
| Logo link                                     | Logo should act as a home button, redirecting the user to the landing page                              | Click the logo                                                   | Link loads the landing page                                            | Pass          |
| Google login link (confirmation page)         | Load confirmation to proceed to google login                                                            | Click google login link                                          | Loads confirm proceed to google login page                             | Pass          |
| Confirm proceed to google login button        | Load the google login page                                                                              | Click google confirm button                                      | Loads google login page                                                | Pass          |
| Email input                                   | Allow user to input email                                                                               | Click on input box                                               | Allows user to input email                                             | Pass          |
| Existing user email                           | Check email is not in use currently, if so notify user                                                  | Type in email for existing user                                  | Notify's user that the email already belongs to an existing user       | Pass          |
| Username input box                            | Allow user to type username                                                                             | Click on input box                                               | Allows user to type username                                           | Pass          |
| Password input box                            | Allow user to type password                                                                             | Click on input box                                               | Allows user to type password                                           | Pass          |
| Password confirmation input box (match)       | Checks that password matches to confirm correct password input                                          | Click on input box and type password again                       | Confirms that passwords match                                          | Pass          |
| Password confirmation input box (don't match) | Notify the user that passwords do not match                                                             | Click on input box and type password again                       | Notify's that passwords don't match                                    | Pass          |
| Invalid user details                          | Error message should be displayed notifying user of invalid user details, no dashboard should be loaded | Type in invalid user details                                     | Error message is displayed and user is not redirected to any dashboard | Pass          |
| Sign up button                                | Signs user up and loads Dashboard page and send s email confirmation                                    | Click sign in                                                    | Loads user Dashboard and sends email confirmation email                | Pass          |
| Responsive design                             | Page should adapt to different screen sizes                                                             | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                                  | Pass          |

## Help Page

1. **Security Testing:**
   - Verify the security of the help page.

2. **Content Display:**
   - Verify that the help page loads with the content displayed correctly.

3. **Navigation Testing:**
   - Test navigation links to other sections.

4. **Responsive Design:**
   - Check the responsive design for readability and usability.

| **Feature**                      | **Expected Outcome**                                                       | **Testing Performed**                                            | **Result**                                                   | **Pass/Fail** |
|:--------------------------------:|:--------------------------------------------------------------------------:|:----------------------------------------------------------------:|:------------------------------------------------------------:|:-------------:|
| Nav links                        | Nav links should load the corresponding page                               | Click the nav links                                              | All links open the appropriate pages                         | Pass          |
| Logo link (unauthenticated user) | Logo should act as a home button, redirecting the user to the landing page | Click the logo                                                   | Link loads the landing page                                  | Pass          |
| Logo link (authenticated user)   | Logo should load the Dashboard page of the user                            | Click the logo                                                   | Link loads the Dashboard page for the user                   | Pass          |
| Contact us name input box        | Allow user to type a name                                                  | Click input box and type name                                    | Allows user to type name                                     | Pass          |
| Contact us email input box       | Allow user to type an email                                                | Click input box and type email                                   | Allows user to type email                                    | Pass          |
| Contact us message input box     | Allow user to type a message                                               | Click input box and type message                                 | Allows user to type message                                  | Pass          |
| Contact us submit button         | Sends user details and message to Habitize and loads thank you page        | Click submit button                                              | Loads thank you page confirming information sent to Habitize | Pass          |
| Contact form error handeling     | If user types invalid inputs, the user is notified                         | Type invalid inputs                                              | Notification is shown explaining the invalid input           | Pass          |
| Responsive design                | Page should adapt to different screen sizes                                | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                        | Pass          |


## Dashboard

1. **Security Testing:**
   - Verify that only authenticated users can access the dashboard.
   - Check the security measures in place to protect user data.

2. **Habit Tracking:**
   - Test the user's ability to view and track habits.
   - Ensure habit tracking functions correctly.

3. **Habit Display:**
   - Verify that the user's habits are displayed correctly, including titles, descriptions, and images.

4. **Responsive Design:**
   - Check for responsive design.

5. **Security of User Data:**
   - Ensure that user data is secured and not accessible by unauthorized users.

| **Feature**                         | **Expected Outcome**                                                                                              | **Testing Performed**                                            | **Result**                                                                                         | **Pass/Fail** |
|:-----------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|:-------------:|
| Nav links                           | Nav links should load the corresponding page                                                                      | Click the nav links                                              | All links open the appropriate pages                                                               | Pass          |
| Hello (user) link                   | Loads view profile page                                                                                           | Click hello (user) link                                          | Opens view profile page                                                                            | Pass          |
| Add button for habits               | Loads add habit page                                                                                              | Click add butotn                                                 | Opens add habit page                                                                               | Pass          |
| Habit options button                | Displays dropdown menu with options for habit                                                                     | Click options button                                             | Displays a dropdown menu of habit options                                                          | Pass          |
| Edit option button                  | Loads edit habit page                                                                                             | Click edit habit options button                                  | Loads edit habit page                                                                              | Pass          |
| Complete habit option button        | Changes the habit colour to green, adds the date of completion and changes the current amount to the goal amount  | Click complete habit option button                               | Habit changes to green, completion date is added and current amount is the same as the goal amount | Pass          |
| Delete habit option button          | Displays delete habit confirmation page                                                                           | Click delete habit option button                                 | Loads confirm habit completion page                                                                | Pass          |
| Delete habit confirmation (confirm) | Habit is deleted permanently                                                                                      | Click confirm delete                                             | Habit is deleted permanently                                                                       | Pass          |
| Delete habit confirmation (cancel)  | Redirects to the Dashboard page                                                                                   | Click cancel delete                                              | User is redirected to Dashboard page                                                               | Pass          |
| Habit filter dropdown               | Display dropdown menu of the different frequency options                                                          | Click frequency filter dropdown                                  | Dropdown menu is displayed with frequency options                                                  | Pass          |
| Apply filter button                 | Apples the frequency filter selected from the dropdown and only habits with selected frequency will be displayed  | Click apply filter                                               | Filter is applied to habit list and only habits with selected frequency are displayed              | Pass          |
| Responsive design                   | Page should adapt to different screen sizes                                                                       | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                                                              | Pass          |


## Add Habits Page

1. **Security Testing:**
   - Ensure that only authorized users can add new habits.
   - Verify the security of habit creation.

2. **Validation:**
   - Check for input validation, including titles, descriptions, and images.

3. **Error Handling:**
   - Verify that appropriate error messages are displayed for input issues.

|                        |                                                                             |                                                                  |                                                                            |               |
|------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------|---------------|
| **Feature**            | **Expected Outcome**                                                        | **Testing Performed**                                            | **Result**                                                                 | **Pass/Fail** |
| Nav links              | Nav links should load the corresponding page                                | Click the nav links                                              | All links open the appropriate pages                                       | Pass          |
| Category dropdown menu | Dropdown menu of categories should show                                     | Click on category dropdown                                       | Menu of categories drop down                                               | Pass          |
| Input boxes            | Allow user to input corresponding information                               | Click in put box and type information                            | Allows user to type information                                            | Pass          |
| Frequency dropdown     | Dropdown menu of frequency options should show                              | Click frequency dropdown                                         | Menu drops down with different frequency options                           | Pass          |
| Complete check box     | Allow user to tick checkbox to set habit as complete                        | Click complete checkbox                                          | Allows user to tick complete checkbox                                      | Pass          |
| Add habit button       | Redirects user back to dashboard and updates habits list with the new habit | Click add habit button                                           | Redirects user back to dashboard and new habit is displayed in habits list | Pass          |
| Cancel button          | Should not save habit and should redirect to dashboard                      | Click cancel button                                              | Redirects to dashboard and habit is not saved                              | Pass          |
| Responsive design      | Page should adapt to different screen sizes                                 | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                                      | Pass          |


## Edit Habits Page

1. **Security Testing:**
   - Ensure that only authorized users can edit habits.
   - Verify the security of habit editing.

2. **Habit Modification:**
   - Test the ability to edit existing habits, including titles, descriptions, and images.

3. **Changes Saved:**
   - Confirm that changes are saved and reflected on the dashboard.

## View Profile Page

1. **Security Testing:**
   - Verify that users can only view their own profiles.
   - Ensure the security of user profile access.

2. **User Profile Data:**
   - Test the user's ability to view their profile information.

3. **Navigation Testing:**
   - Test the navigation to edit the user's profile.

## Edit Profile Page

1. **Security Testing:**
   - Ensure that only authorized users can edit their profiles.
   - Verify the security of profile editing.

2. **Profile Modification:**
   - Test the ability to edit user profile information, such as display name or color theme.

3. **Changes Saved:**
   - Confirm that changes to the profile are saved.

## Password Reset

1. **Security Testing:**
   - Test the password reset feature to ensure that it is secure.

2. **Email Confirmation:**
   - Verify that users can reset their passwords if forgotten.

## Additional Testing

1. **Image Upload Testing:**
   - Test image uploads for user profiles and habits.
   - Check for compatibility and responsiveness with various file types and sizes.

2. **Security Vulnerability Testing:**
   - Perform security testing, including penetration testing, to identify vulnerabilities and ensure data security.

3. **Email Confirmation Testing:**
   - Test email confirmation for user registration and password reset.
   - Ensure that email links are generated and lead to the correct actions.

4. **Responsive Design Testing:**
   - Verify the responsiveness of the application on different devices and screen sizes.

