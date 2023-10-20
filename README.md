# Habitize

![Landing page](/screenshots/landing-page.gif)

**Habitize** is a web-based habit tracking and goal management application designed to help users build and maintain positive habits. With Habitize, you can create a personalized dashboard to track your habits, set achievable goals, and measure your progress over time. The application offers a user-friendly interface and a range of features to empower users in their journey to form lasting habits.

## Key Features

- **User-Friendly Dashboard:** Create and customize your dashboard to display the habits that matter most to you.
- **Goal Setting:** Set specific goals for each habit and track your progress towards achieving them.
- **Habit Tracking:** Log your habits with ease and view your streaks and completion rates.
- **Visual Analytics:** Gain insights into your habits with visual statistics.
- **Account Management:** Securely manage your account and personal habit data.

Habitize is built using modern web technologies, making it accessible across various devices and platforms. Start your habit-building journey today with Habitize!

## Demo

[Provide a link to a live demo or hosted version of your project if applicable.]

## Table Of Contents

- [How to Use](#how-to-use)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Scope Plane](#scope-plane)
- [Data Models](#data-model)
  - [Logic Map](#logic-map)
- [Wireframes](#wireframes)
- [Features](#features)
  - [Feature 1](#feature-1)
  - [Feature 2](#feature-2)
- [Technologies Used](#technologies-used)
  - [Frameworks, Libraries, and Tools Used](#frameworks-libraries-and-tools-used)
- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Validator Testing](#validator-testing)
  - [Solved Bugs](#solved-bugs)
  - [Bugs](#bugs)
  - [Testing User Stories](#testing-user-stories)
- [Deployment](#deployment)
  - [Local Development](#local-development)
- [Credits](#credits)
  - [Inspiration](#inspiration)
  - [Code References](#code-references)

# How to Use

[Explain how to use your project, including setup instructions and any necessary prerequisites.]
# UX
The Strategy Plane
Habitize is designed as a user-friendly platform where individuals can effectively track and manage their habits. The overall user experience focuses on simplicity and accessibility, making it easy for users to create, monitor, and achieve their goals. The graphical elements and design aim to create a motivating and productive environment.

**The Site's Ideal User**
- Individuals interested in self-improvement
- Goal-oriented users looking to establish and maintain habits
- Users seeking a digital tool for habit tracking
- Anyone motivated to create a consistent routine

**Site Goals**
- Enable users to track and manage their habits
- Assist users in achieving personal and lifestyle goals
- Foster a productive and consistent user routine
- Provide a digital platform for habit tracking and self-improvement

**Epics**
A total of 12 epics have been identified, each with its set of user stories aimed at enhancing the Habitize app. For a detailed breakdown of each epic and its associated user stories, please refer to the project [Kanban Board](https://github.com/users/jflets/projects/3).

1. **Initial Django & Deployment Setup**
   - This epic focuses on the initial setup of the Django framework and deployment of the application.

2. **Manage Users**
   - This epic involves user management, including registration and profile management.

3. **Admin Access**
   - Admin-specific features and privileges for managing the application.

4. **Goals**
   - Setting and tracking goals for habit completion.

5. **User Profile**
   - Viewing and personalizing user profiles.

6. **Habit Progress Tracking**
   - Monitoring and visualizing habit progress.

7. **Habit Tracking**
   - Logging and tracking habit completion.

8. **Habit Deletion**
   - Deletion of habits from the tracking list.

9. **Habit Editing**
   - Editing and customizing habit details.

10. **Habit Creation**
    - Adding new habits to the tracking list.

11. **User Login**
    - User authentication and login features.

12. **User Registration**
    - User registration for accessing habit tracking.


## User Stories
From the Epics, 45 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have, or Won't Have. Each story was also assigned user story points based on your best estimation for the time/difficulty of completing each story. The full list of User Stories, separated by those completed and those pushed to a future release, is available on the project [Kanban Board](https://github.com/users/jflets/projects/3).

**[#62](https://github.com/jflets/Habitize/issues/62) Initial Django & Deployment Setup**
  -  Create Django apps for the project.
  -  Implement security measures for secret key protection.
  -  Early deployment of the site to Heroku for development purposes.

**[#1](https://github.com/jflets/Habitize/issues/1) User Registration**
- [#58](https://github.com/jflets/Habitize/issues/58) USER STORY: Complete the Registration Process to Access My Dashboard Must Have Story Points: 2
- [#57](https://github.com/jflets/Habitize/issues/57) USER STORY: Receive a Confirmation Email for Account Verification Should Have Story Points: 3
- [#56](https://github.com/jflets/Habitize/issues/56) USER STORY: Provide Registration Details and Create a Password Must Have Story Points: 2
- [#55](https://github.com/jflets/Habitize/issues/55) USER STORY: Sign Up for a New Account on the Platform Must Have Story Points: 3

**[#2](https://github.com/jflets/Habitize/issues/2) User Login**
- [#54](https://github.com/jflets/Habitize/issues/54) USER STORY: Reset My Password If I Forget It Must Have Story Points: 3
- [#53](https://github.com/jflets/Habitize/issues/53) USER STORY: Use Single Sign-On (SSO) Methods Like Google Login Should Have Story Points: 5
- [#52](https://github.com/jflets/Habitize/issues/52) USER STORY: Authenticate Using Email and Password Must Have Story Points: 3
- [#51](https://github.com/jflets/Habitize/issues/51) USER STORY: Enter My Login Credentials Must Have Story Points: 3

**[#3](https://github.com/jflets/Habitize/issues/3) Habit Creation**
- [#50](https://github.com/jflets/Habitize/issues/50) USER STORY: Confirm the Addition of a New Habit Must Have Story Points: 2
- [#49](https://github.com/jflets/Habitize/issues/49) USER STORY: Choose the Target Frequency for Tracking Must Have Story Points: 3
- [#48](https://github.com/jflets/Habitize/issues/48) USER STORY: Specify the Target Amount for Habit Completion Must Have Story Points: 2
- [#47](https://github.com/jflets/Habitize/issues/47) USER STORY: Define the Name and Details of the Habit Must Have Story Points: 2
- [#46](https://github.com/jflets/Habitize/issues/46) USER STORY: Add a New Habit to My Tracking List Must Have Story Points: 3

**[#4](https://github.com/jflets/Habitize/issues/4) Habit Editing**
- [#45](https://github.com/jflets/Habitize/issues/45) USER STORY: Save Habit Edits and See Updated Information Must Have Story Points: 2
- [#44](https://github.com/jflets/Habitize/issues/44) USER STORY: Adjust the Target Frequency for Tracking Must Have Story Points: 2
- [#43](https://github.com/jflets/Habitize/issues/43) USER STORY: Modify the Target Amount for Habit Completion Should Have Story Points: 2
- [#42](https://github.com/jflets/Habitize/issues/42) USER STORY: Edit the Name and Details of a Habit Must Have Story Points: 3

**[#5](https://github.com/jflets/Habitize/issues/5) Habit Deletion**
- [#41](https://github.com/jflets/Habitize/issues/41) USER STORY: Confirm Deletion of a Habit Must Have Story Points: 3
- [#40](https://github.com/jflets/Habitize/issues/40) USER STORY: Delete a Habit Must Have Story Points: 2

**[#6](https://github.com/jflets/Habitize/issues/6) Habit Tracking**
- [#39](https://github.com/jflets/Habitize/issues/39) USER STORY: Mark Habits as Completed Must Have Story Points: 2
- [#38](https://github.com/jflets/Habitize/issues/38) USER STORY: Log Habit Completion Should Have Story Points: 3

**[#7](https://github.com/jflets/Habitize/issues/7) Habit Progress Tracking**
- [#37](https://github.com/jflets/Habitize/issues/37) USER STORY: Get a Summary of Overall Habit Completion Must Have Story Points: 3
- [#36](https://github.com/jflets/Habitize/issues/36) USER STORY: Identify Habits I Haven't Completed Must Have Story Points: 3
- [#35](https://github.com/jflets/Habitize/issues/35) USER STORY: See the Progress of Each Habit Must Have Story Points: 5
- [#34](https://github.com/jflets/Habitize/issues/34) USER STORY: View a List of Habits Must Have Story Points: 3

**[#8](https://github.com/jflets/Habitize/issues/8) User Profile**
- [#33](https://github.com/jflets/Habitize/issues/33) USER STORY: Set Colour Themes Should Have Story Points: 5
- [#32](https://github.com/jflets/Habitize/issues/32) USER STORY: Set a Personalised Display Name Should Have Story Points: 2
- [#31](https://github.com/jflets/Habitize/issues/31) USER STORY: Change Profile Picture Should Have Story Points: 3
- [#30](https://github.com/jflets/Habitize/issues/30) USER STORY: Edit and Update User Profile Must Have Story Points: 3
- [#29](https://github.com/jflets/Habitize/issues/29) USER STORY: View User Profile Information Must Have Story Points: 3

**[#9](https://github.com/jflets/Habitize/issues/9) Goals**
- [#28](https://github.com/jflets/Habitize/issues/28) USER STORY: Track Habit Completion Status Must Have Story Points: 2
- [#27](https://github.com/jflets/Habitize/issues/27) USER STORY: View My Goals and Progress Must Have Story Points: 5
- [#26](https://github.com/jflets/Habitize/issues/26) USER STORY: Update or Modify Goals Must Have Story Points: 2
- [#25](https://github.com/jflets/Habitize/issues/25) USER STORY: Set Goals for Specific Habits Must Have Story Points: 2

**[#10](https://github.com/jflets/Habitize/issues/10) Admin Access**
- [#24](https://github.com/jflets/Habitize/issues/24) USER STORY: Perform Administrative Tasks Should Have Story Points: 1
- [#23](https://github.com/jflets/Habitize/issues/23) USER STORY: Monitor User Activity and Habits Should Have Story Points: 1
- [#22](https://github.com/jflets/Habitize/issues/22) USER STORY: Manage User Accounts from the Admin Panel Must Have Story Points: 1
- [#21](https://github.com/jflets/Habitize/issues/21) USER STORY: Access Admin-Specific Features Must Have Story Points: 1
- [#20](https://github.com/jflets/Habitize/issues/20) USER STORY: Log in to the Admin Panel Must Have Story Points: 1

**[#11](https://github.com/jflets/Habitize/issues/11) Manage Users**
- [#19](https://github.com/jflets/Habitize/issues/19) USER STORY: Enable/Disable User Accounts Must Have Story points: 1
- [#18](https://github.com/jflets/Habitize/issues/18) USER STORY: Sort User List Must Have Story points: 1
- [#17](https://github.com/jflets/Habitize/issues/17) USER STORY: Filter Users Must Have Story points: 1
- [#16](https://github.com/jflets/Habitize/issues/16) USER STORY: Search for Users Must Have Story points: 1
- [#15](https://github.com/jflets/Habitize/issues/15) USER STORY: Access User Registration Details Must Have Story points: 1
- [#14](https://github.com/jflets/Habitize/issues/14) USER STORY: View Registered Users Must Have Story points: 1

## Scope Plane

In the scope of the Habitize app, we aim to deliver a set of essential features to provide users with a comprehensive habit-tracking and management experience. Below are the key features planned:

1. **User Registration and Authentication**
   - Users can sign up for a new account on the platform.
   - Users provide registration details and create a secure password.
   - Users receive a confirmation email for account verification.
   - Users can log in to their accounts using their credentials.
   - Users can use single sign-on (SSO) methods like Google Login.
   - Users can reset their password if they forget it.
   - Users can log out of their accounts.

2. **Habit Creation and Management**
   - Users can add new habits to their tracking list.
   - Users define the name and details of each habit.
   - Users specify the target amount for habit completion.
   - Users choose the target frequency for tracking each habit.
   - Users confirm the addition of a new habit to their list.

3. **Habit Editing**
   - Users can edit the name and details of existing habits.
   - Users can modify the target amount for habit completion.
   - Users can adjust the target frequency for habit tracking.
   - Users save habit edits and see updated information.

4. **Habit Deletion**
   - Users can delete habits they no longer wish to track.
   - Users have the option to confirm the deletion of a habit.

5. **Habit Tracking**
   - Users can mark habits as completed when they are done.
   - Users can log habit completions, providing valuable tracking data.

6. **Habit Progress Tracking**
   - Users can view a summary of their overall habit completion.
   - Users can identify habits they haven't completed.
   - Users can see the progress of each habit.
   - Users can view a list of all their habits.

7. **User Profile Management**
   - Users can view their own profile information.
   - Users can edit and update their user profile.
   - Users can change their profile picture.
   - Users can set a personalized display name.
   - Users can choose from different color themes.

8. **Goals and Progress**
   - Users can set goals for specific habits.
   - Users can track their habit completion status.
   - Users can view their goals and progress over time.

9. **Admin Access**
   - Admin users can perform administrative tasks.
   - Admin users can monitor user activity and habits.
   - Admin users can manage user accounts from the admin panel.
   - Admin users can access admin-specific features.
   - Admin users can log in to the admin panel.

10. **Responsive Design**
    - The app will be fully responsive to ensure a seamless experience across various devices and screen sizes.

11. **Alternative Color Modes**
    - Users have the option to select from different color modes to customize the app's appearance.

# Data Models

## Category

The `Category` model represents a category for habits.

### Fields

- `name`: A character field with a maximum length of 50 characters.

## Habit

The `Habit` model represents a habit that users can track.

### Fields

- `name`: A character field with a maximum length of 50 characters.
- `date_created`: A DateTime field that auto-generates the creation date.
- `completed`: A Boolean field to indicate if the habit is completed.
- `value`: A PositiveIntegerField representing the current value of the habit.
- `goal_amount`: A PositiveIntegerField representing the maximum value for the habit.
- `category`: A ForeignKey to the `Category` model, allowing habits to be associated with categories.
- `frequency`: A choice field for habit frequency with options: 'day', 'week', 'month'.
- `last_reset`: A DateTime field to store the last reset date of the habit.
- `units`: A character field with a maximum length of 10 characters.
- `date_completed`: A DateField to store the date when the habit was completed.
- `user`: A ForeignKey to the `User` model for user association.

### Methods

- `reset_habit()`: Resets the habit's value and last reset time based on the habit's frequency.
- `save()`: Overrides the default `save()` method to reset the habit before saving.

### Meta

- `ordering`: Specifies the default ordering for habits.

## UserProfile

The `UserProfile` model represents user profiles.

### Fields

- `user`: A OneToOneField to the `User` model.
- `color_theme`: A choice field for user color themes.
- `selected_color_theme`: A character field for the selected color theme.
- `profile_image`: A CloudinaryField for storing profile images.
- `profile_image_public_id`: A character field to store the public ID of the profile image.

### Methods

- `__str__()`: Returns the username of the associated user.

## Allauth

`allauth` is a Django app for authentication and account management.

### Included Models

- `Account`: Represents a user account with fields like email, username, and password.


### Logic Map

[Logic Map](https://www.figma.com/file/VjMGn71dAh1oFA959Chgv2/Untitled?type=whiteboard&node-id=0%3A1&t=7GxvzogChqdHBwz7-1)

## Wireframes 

[Wireframe](https://www.figma.com/file/R6z2UxOhrRZt2lgCZuNo5l/Habitize?type=design&node-id=0%3A1&mode=design&t=GgmSyiNRLry0qZJB-1)

# Pages

## Landing Page
  ![Landing page](/screenshots/landing-page.gif)
## Login Page
  ![Login](/screenshots/login.png)
## Signup Page
  ![Signup](/screenshots/signup.png)
## Help Page
  ![Help Page](/screenshots/help-page.gif)
## Dashboard
  ![Dashboard](/screenshots/dashboard.png)
## Add Habits Page
  ![Add Habits](/screenshots/add-habit.png)
## Edit Habits Page
  ![Edit Habits](/screenshots/edit-habit.gif)
## View Profile Page
  ![View Profile](/screenshots/view-profile.png)
## Edit Profile Page
  ![Edit Profile](/screenshots/edit-profile.png)



# Features


1. **User Registration and Authentication:**
   - Create a secure account with a unique username and password.
   - Log in and protect your personal data.
   - Use third-party login like Google to create an account and log in.
   ![Login](/screenshots/login.png)
   ![Signup](/screenshots/signup.png)
   ![Google Sign in](/screenshots/google-login.png)

2. **User Profile Management:**
   - Change your username.
   - Change your profile picture.
   - Change your color theme.
   ![View Profile](/screenshots/view-profile.png)
   ![Edit Profile](/screenshots/edit-profile.png)

3. **Dashboard:**
   - Get a personalized dashboard displaying your habits and goals.
   ![Dashboard](/screenshots/dashboard.png)

4. **Habit Management:**
   - Create and customize new habits.
   - Set daily, weekly or monthly goals for each habit.
   - Edit or delete existing habits.
   ![Add Habits](/screenshots/add-habit.png)
   ![Edit Habits](/screenshots/edit-habit.gif)
   ![Habit Options](/screenshots/habit-options.png)
   ![Confirm Delete](/screenshots/confirm-delete.png)

5. **Goal Management:**
   - Define specific goals for your habits.
   - Track and update goals.
   - Monitor your progress toward goals.
   ![Completed Habits](/screenshots/goal-progress.png)

6. **Habit Tracking:**
   - Easily track your habit's progress.
   - See the habit completion date.
   ![Habit Progress](/screenshots/habit-progress.png)
   ![Complete Habit](/screenshots/completed-habit.png)

7. **Responsive Design:**
   - Enjoy a responsive and accessible app across various devices.
   ![Responsive Design](/screenshots/responsive.gif)

8. **Sharing and Social Features:**
   - Share your progress on social media.
   - Connect with others for motivation.
   ![Social Links](/screenshots/social.png)

9. **Help and Support:**
    - Access help and contact support.
    - Help page with app instructions.
    ![Help Page](/screenshots/help-page.gif)

10. **Admin Dashboard:**
    - Admin panel for managing user accounts (for admin users).
    ![Admin Panel](/screenshots/admin.png)

11. **User Feedback Messages**
    - Users will receive feedback messages whenever they make any changes or perform actions.
    ![User Feedback Messages](/screenshots/user-feedback.gif)


# Technologies Used
## Frameworks, Libraries, and Tools Used
- **Libraries from requirements file**
  - asgiref==3.7.2
  - certifi==2023.7.22
  - cffi==1.15.1
  - charset-normalizer==3.2.0
  - cloudinary==1.34.0
  - cryptography==41.0.3
  - defusedxml==0.7.1
  - dj-database-url==0.5.0
  - dj3-cloudinary-storage==0.0.6
  - Django==3.2.21
  - django-allauth==0.56.1
  - django-storages==1.14
  - gunicorn==21.2.0
  - idna==3.4
  - oauthlib==3.2.2
  - packaging==23.1
  - Pillow==10.0.1
  - psycopg2==2.9.7
  - pycparser==2.21
  - PyJWT==2.8.0
  - python3-openid==3.2.0
  - pytz==2023.3.post1
  - requests==2.31.0
  - requests-oauthlib==1.3.1
  - six==1.16.0
  - sqlparse==0.4.4
  - urllib3==1.26.16

- **Frontend:**
  - HTML, CSS, JavaScript
  - Bootstrap for grid and styling
  - Chrome dev tools for responsive design for various screen sizes
  - Font Awesome for icons
  - Google Fonts for text fonts

- **Image Storage**
  - Cloudinary for storing statics files and user images.

- **Backend:**
  - Django for the backend framework
  - ElephantSQL for the PostgreSQL database
  - Python for server-side logic

- **Authentication and Authorization:**
  - Django's built-in `csrf_token` for Cross-Site Request Forgery protection
  - Django-allauth for user authentication and account management

- **Deployment:**
  - Hosting on Heroku for cloud-based deployment

- **Development Tools:**
  - Visual Studio Code as the code editor
  - Git and GitHub for version control

- **Testing and Quality Assurance:**
  - Jest and JSDom for frontend testing
  - Django's TestCase and Jest for automated testing

- **Database Management:**
  - Django ORM for database interactions
  - ElephantSQL for the PostgreSQL database in production
  - SQLite for local development and testing

- **Image Conversion**
  - [CloudConvert](https://cloudconvert.com/) for MOV to GIF
  - [Convertio](https://convertio.co/) for PNG to WebP

# Testing

## Automated Testing
- **JS Testing:**
  ![JS Testing](/screenshots/js-test.gif)

- **Python Testing:**
  ![Python Testing](/screenshots/python-test.gif)


## Validator Testing

- [Describe any validation tools used and the results.]

## Solved Bugs

1. [Bug description and how it was resolved.]

2. [Bug description and how it was resolved.]

[Add more resolved bugs if needed.]

## Bugs

[Describe any known bugs or issues in your project.]

## Testing User Stories

1. [User Story 1 Testing]
   - [Describe the test scenario and the result.]

2. [User Story 2 Testing]
   - [Describe the test scenario and the result.]

[Add more testing scenarios for user stories if needed.]

# Deployment

[Explain how your project can be deployed or hosted.]

## Local Development

[Provide instructions for local development, including how to clone the repository and set up the development environment.]

# Credits

## Inspiration

[Credit any sources or inspirations that influenced your project.]

## Code References

[List any code references or tutorials that were helpful in developing your project.]
