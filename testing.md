# Table Of Contents
- [Testing Schedule](#testing-schedule)
   - [Landing Page](#landing-page)
   - [login Page](#login-page)
   - [Signup page](#signup-page)
   - [help Page](#help-page)
   - [Dashboard](#dashboard)
   - [Add Habits Page](#add-habits-page)
   - [Edit Habits Page](#edit-habits-page)
   - [View Profile Page](#view-profile-page)
   - [Edit Profile Page](#edit-profile-page)
   - [Password Reset](#password-reset)
- [Validator Testing](#validator-testing-screenshots)
   - [PEP8](#pep8)
   - [JSHint](#jshint)
   - [W3C CSS](#w3c-css)
   - [W3C HTML]()
- [Accessibility Testing](#accessability-testing)
- [Error Pages](#error-pages)

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

|                                    |                                                                                                                                         |                                                                                    |                                                                                                                                      |               |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------|
| **Feature**                        | **Expected Outcome**                                                                                                                    | **Testing Performed**                                                              | **Result**                                                                                                                           | **Pass/Fail** |
| Nav links                          | Nav links should load the corresponding page                                                                                            | Click the nav links                                                                | All links open the appropriate pages                                                                                                 | Pass          |
| Edit habit button from option menu | Should open edit habit page and have habit information                                                                                  | Click edit habit button from option menu                                           | Opens edit habit page and displays habit information                                                                                 | Pass          |
| Habit name input                   | Should display habits name and allow user to change information                                                                         | Click habit name                                                                   | Displays habit name and allows user to change information                                                                            | Pass          |
| Current amount input               | Should display the current amount                                                                                                       | Open edit page                                                                     | Displays current amount                                                                                                              | Pass          |
| Current amount increase button     | Should allow user to increase amount until goal amount is reached                                                                       | Click increase button until goal amount was reached, then clicked a few more times | Allowed user to increase amount up to the goal amount but not passed                                                                 | Pass          |
| Current amount decrease button     | Should allow user to decrease current amount but not lower than 0                                                                       | Click decrease button to 0 then click a few more times                             | Allows user to decrease current amount down to 0 but not less                                                                        | Pass          |
| Complete checkbox                  | Allow user to tick checkbox to set habit as complete                                                                                    | Click complete checkbox                                                            | Allows user to tick complete checkbox                                                                                                | Pass          |
| Update habit button                | Should have the update made by the user and redirect the user back to the dash board and updates should be displayed in the habits list | Click update habit                                                                 | Habit saves the user changes and then redirects the user back to the dashboard and the updated habit is displayed in the habits list | Pass          |
| Show advanced settings             | Should trigger a popup to ask user to confirm show advanced settings                                                                    | Click show advanced settings                                                       | A popup is displayed asking to confirm or cancel my choice                                                                           | Pass          |
| Confirm show advanced settings     | Should load the hidden settings and display the information in the edit page                                                            | Click confirm                                                                      | Hidden settings are displayed in edit habit page                                                                                     | Pass          |
| Cancel show advanced settings      | Should close the popup and not show any advanced settings                                                                               | Click cancel                                                                       | Popup closes and no advanced settings are shown                                                                                      | Pass          |
| Category dropdown menu	            | Dropdown menu of categories should show	                                                                                                | Click on category dropdown	                                                        | Menu of categories drop down                                                                                                         | Pass          |
| Frequency dropdown                 | Dropdown menu of frequency options should show	                                                                                         | Click frequency dropdown	                                                          | Menu drops down with different frequency options                                                                                     | Pass          |
| Goal amount input                  | Display the goal amount and allow user to increase and decrease amount                                                                  | Increase and decrease goal amount                                                  | Gola amount is shown and user can increase and decrease amount                                                                       | Pass          |
| Responsive design                  | Page should adapt to different screen sizes                                                                                             | Using Chrome dev tools, scale the page to different screen sizes                   | Page adapts to different screen sizes                                                                                                | Pass          |


## View Profile Page

1. **Security Testing:**
   - Verify that users can only view their own profiles.
   - Ensure the security of user profile access.

2. **User Profile Data:**
   - Test the user's ability to view their profile information.

3. **Navigation Testing:**
   - Test the navigation to edit the user's profile.

|                                       |                                              |                                                                  |                                       |               |
|---------------------------------------|----------------------------------------------|------------------------------------------------------------------|---------------------------------------|---------------|
| **Feature**                           | **Expected Outcome**                         | **Testing Performed**                                            | **Result**                            | **Pass/Fail** |
| Nav links                             | Nav links should load the corresponding page | Click the nav links                                              | All links open the appropriate pages  | Pass          |
| User image displayed (image added)    | Image is displayed                           | Open view profile page                                           | Profile image is displayed            | Pass          |
| User image displayed (no image added) | Profile icon displayed                       | Open view profile page                                           | Icon image is displayed               | Pass          |
| User name displayed                   | User should be displayed below profile image | Open view profile page                                           | Username is displayed                 | Pass          |
| Edit profile button                   | Should load edit profile page                | Click button                                                     | Opens edit profile page               | Pass          |
| Responsive design                     | Page should adapt to different screen sizes  | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes | Pass          |


## Edit Profile Page

1. **Security Testing:**
   - Ensure that only authorized users can edit their profiles.
   - Verify the security of profile editing.

2. **Profile Modification:**
   - Test the ability to edit user profile information, such as display name or color theme.

3. **Changes Saved:**
   - Confirm that changes to the profile are saved.

|                                               |                                                                                                            |                                                                  |                                                                           |               |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------|---------------|
| **Feature**                                   | **Expected Outcome**                                                                                       | **Testing Performed**                                            | **Result**                                                                | **Pass/Fail** |
| Nav links                                     | Nav links should load the corresponding page                                                               | Click the nav links                                              | All links open the appropriate pages                                      | Pass          |
| User name displayed                           | User should be displayed and allow user to change name                                                     | Type new username                                                | Username is changed once update is saved                                  | Pass          |
| User profile image displayed (image added)    | Image is displayed                                                                                         | Open view profile page                                           | Profile image is displayed                                                | Pass          |
| User profile image displayed (no image added) | Profile icon displayed                                                                                     | Open view profile page                                           | Icon image is displayed                                                   | Pass          |
| User profile image upload                     | User should be able to upload new profile image                                                            | Click choose file button and upload image                        | Profile image is successfully uploaded                                    | Pass          |
| Color theme radio buttons                     | Button should display the color inside the button and should change the color theme of the site when saved | Click color theme buttons and save update                        | Color theme for the site has changed                                      | Pass          |
| Update button                                 | Should apply and save changes made by user                                                                 | Click update button                                              | User changes have been applied and saved                                  | Pass          |
| Cancel button                                 | Should not save any changes and should redirect the user back to the view profile page                     | Click cancel button                                              | No changes are saved and user is redirected back to the view profile page | Pass          |
| Responsive design                             | Page should adapt to different screen sizes                                                                | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                                     | Pass          |

## Password Reset

1. **Security Testing:**
   - Test the password reset feature to ensure that it is secure.

2. **Email Confirmation:**
   - Verify that users can reset their passwords if forgotten.

|                       |                                                                             |                                                                  |                                                                     |               |
|-----------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|---------------|
| **Feature**           | **Expected Outcome**                                                        | **Testing Performed**                                            | **Result**                                                          | **Pass/Fail** |
| Nav links             | Nav links should load the corresponding page                                | Click the nav links                                              | All links open the appropriate pages                                | Pass          |
| Email input           | Should allow user to input their email and validate that the email is valid | Type email in input box                                          | User can input their email and if email is invalid user is notified | Pass          |
| Reset password button | Should send email to user with reset link                                   | Click reset email button                                         | Email is sent to user with password reset link                      | Pass          |
| Responsive design     | Page should adapt to different screen sizes                                 | Using Chrome dev tools, scale the page to different screen sizes | Page adapts to different screen sizes                               | Pass          |

## Additional Testing
 **Responsive Design Testing:**
   - Verify the responsiveness of the application on different devices and screen sizes.

# Validator testing screenshots

## Pep8
### Habitize
habitize-settings.py
![habitize-settings.py](/screenshots/pep8/habitize/habitize-settings.png)

habitize-urls.py
![habitize-urls-py](/screenshots/pep8/habitize/habitize-urls.png)

habitize-views.py
![habitize-views.py](/screenshots/pep8/habitize/habitize-views.png)

habitize-wsgi.py
![habitize-wsgi.py](/screenshots/pep8/habitize/habitize-wsgi.png)

habitize-asgi.py
![habitize-asgi.py](/screenshots/pep8/habitize/hbitize-asgi.png)

### Dashboard

dashboard-admin.py
 ![dashboard-admin.py](/screenshots/pep8/dashboard/dashboard-admin.png)

 dashboard-apps.py
 ![dashboard-apps.py](/screenshots/pep8/dashboard/dashboard-apps.png)

 dashboard-forms.py
 ![dashboard-forms.py](/screenshots/pep8/dashboard/dashboard-forms.png)

 dashboard-models.py
 ![dashboard-models.py](/screenshots/pep8/dashboard/dashboard-models.png)

 dashboard-tests.py
 ![dashboard-tests.py](/screenshots/pep8/dashboard/dashboard-tests.png)

 dashboard-urls.py
 ![dashboard-urls.py](/screenshots/pep8/dashboard/dashboard-urls.png)

 dashboard-views.py
 ![dashboard-views.py](/screenshots/pep8/dashboard/dashboard-views.png)

### Landing page
landing-page-apps.py
![landing-page-apps.py](/screenshots/pep8/landing-page/landing-page-apps.png)

landing-page-tests.py
![landing-page-tests.py](/screenshots/pep8/landing-page/landing-page-tests.png)

landing-page-urls.py
![landing-page-urls.py](/screenshots/pep8/landing-page/landing-page-urls.png)

landing-page-views.py
![landing-page-views.py](/screenshots/pep8/landing-page/landing-page-views.png)

### User profile
user-profile-admin.py
![user-profile-admin.py](/screenshots/pep8/user-profile/user-profile-admin.png)

user-profile-forms.py
![user-profile-forms.py](/screenshots/pep8/user-profile/user-profile-apps.png)

user-profile-models.py
![user-profile-models.py](/screenshots/pep8/user-profile/user-profile-models.png)

user-profile-tests.py
![user-profile-tests.py](/screenshots/pep8/user-profile/user-profile-tests.png)

user-profile-urls.py
![user-profile-urls.py](/screenshots/pep8/user-profile/user-profile-urls.png)

user-profile-views.py
![user-profile-views.py](/screenshots/pep8/user-profile/user-profile-views.png)

## JSHint
edit.js
![edit.js](/screenshots/jshint/edit.png)

index.js
![index.js](/screenshots/jshint/index.png)

tests.js
![tests.js](/screenshots/jshint/test.png)

## W3C CSS

The warnings in the following style sheets are due to the (vendor extensions) I have used.

style.css
![style.css](/screenshots/w3css/style-css.png)

dashboard.css
![dashboard.css](/screenshots/w3css/dashboard-css.png)

turquoise-theme.css
![turquoise-theme.css](/screenshots/w3css/turquoise-theme-css.png)

blue-theme.css
![blue-theme.css](/screenshots/w3css/blue-theme-css.png)

purple-theme.css
![purple-theme.css](/screenshots/w3css/purple-theme-css.png)

pink-theme.css
![pink-theme.css](/screenshots/w3css/pink-theme-css.png)

brown-theme.css
![brown-theme.css](/screenshots/w3css/brown-theme-css.png)

green-theme.css
![green-theme.css](/screenshots/w3css/green-theme-css.png)

## W3C HTML

landing page
![landing-page.html](/screenshots/w3c-html/landing-page-html.png)

signup page
![signup.html](/screenshots/w3c-html/signup-html.png)

login page
![login.html](/screenshots/w3c-html/login-html.png)

logout page
![logout.html](/screenshots/w3c-html/logout-html.png)

forgot password page
![forgot-password.html](/screenshots/w3c-html/forgot-password-html.png)

dashboard page (The error on this page is due to the jinja template link and the warning is for an aria label that i feel is necessary for the accessibility of the page.)
![dashboard.html](/screenshots/w3c-html/dashboard-html.png)

add habit page
![add-habit.html](/screenshots/w3c-html/add-habit-html.png)

edit habit page
![edit-habit.html](/screenshots/w3c-html/edit-habit-html.png)

delete habit page
![delete-habit.html](/screenshots/w3c-html/delete-habit-html.png)

view profile page
![view-profile.html](/screenshots/w3c-html/view-profile-html.png)

edit profile page
![edt-profile.html](/screenshots/w3c-html/edit-profile-html.png)

help page
![help.html](/screenshots/w3c-html/help-html.png)


# Accessability Testing

The reason the accessability is not 100% is due to the lack of contrast in the footer, but this was by design as I have purposely muted the footer text to make it less distracting to the user.

Landing Page
![landing page](/screenshots/accessibility/lp-access.png)

Signup Page
![signup page](/screenshots/accessibility/signup-access.png)

Login Page  
![login page](/screenshots/accessibility/login-access.png)

Help Page   
![help page](/screenshots/accessibility/help-access.png)

Dashboard   
![dashboard page](/screenshots/accessibility/dash-access.png)

Add Habit Page
![add habit page](/screenshots/accessibility/add-hab-access.png)

Edit Habit Page
![edit habit page](/screenshots/accessibility/edit-hab-access.png)

Delete Habit Page
![delete habit page](/screenshots/accessibility/delete-hab-access.png)

View Profile Page
![view profile page](/screenshots/accessibility/view-pro-access.png)

Edit profile page
![edit profile page](/screenshots/accessibility/edit-pro-access.png)

Logout Page  
![logout page](/screenshots/accessibility/logout-access.png)

Password Reset Page
![password reset page](/screenshots/accessibility/pass-reset-access.png)

# Error Pages

### 404
![404 error page](/screenshots/error-pages/404-page.png)

### 403
![403 error page](/screenshots/error-pages/404-page.png)

### 500
![500 error page](/screenshots/error-pages/500-error.png)