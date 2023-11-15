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

Please click [here](https://habitize-0cb9a976b845.herokuapp.com/) to view the live site. (please make sure to open this link in a separate tab)

If for any reason the above link does not work please copy and paste the following: (https://habitize-0cb9a976b845.herokuapp.com/)

## Table Of Contents

- [How to Use](#how-to-use)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Scope Plane](#scope-plane)
- [Data Models](#data-models)
- [Logic Map](#logic-map)
- [Wireframes](#wireframes)
- [Pages](#pages)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Design](#design)
- [Technologies Used](#technologies-used)
  - [Frameworks, Libraries, and Tools Used](#frameworks-libraries-and-tools-used)
- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Validator Testing](#validator-testing)
  - [Solved Bugs](#solved-bugs)
- [Deployment](#deployment)
  - [Local Development](#local-development)
- [Credits](#credits)

# How to Use

Welcome to Habitize! This section will guide you through the basic steps to get started with our habit-tracking and management app.

## 1. Sign Up for an Account

To begin your habit-tracking journey, you'll need to create an account:

1. Click on the "Sign Up" or "Register" button on the app's landing page.
2. Provide your registration details, including your email and a secure password.
3. Once your details are entered, click "Register."
4. Check your email for a confirmation message and follow the provided link to verify your account.

## 2. Log In to Your Account

After successfully registering, you can log in to your account:

1. Click on the "Log In" button.
2. Enter your registered email and password.
3. Click "Log In" to access your account.

## 3. Create and Manage Your Habits

Habitize empowers you to track and manage your habits. Here's how:

1. From your dashboard, navigate to "Habits" or a similar section.
2. Click on the "Add New Habit" button.
3. Define the name, details, target amount, and tracking frequency for the habit.
4. Confirm the addition of the new habit.

## 4. Edit or Delete Habits

If you ever need to make changes to your habits, it's easy:

1. Go to your "Habits" or "My Habits" section.
2. Select the habit you wish to edit.
3. Make the necessary changes, like the name or tracking frequency.
4. Save your edits, and the habit will be updated.

To delete a habit:

1. Access your habit list.
2. Select the habit you want to remove.
3. Confirm the deletion, and it will be removed from your list.

## 5. Log Habit Completions

As you make progress, you can log habit completions:

1. Go to your "Habits" or a related section.
2. Click on the habit you've completed for the day.
3. Mark it as completed, and your progress will be recorded.

## 6. Track Your Progress

Habitize provides you with tools to monitor your progress:

1. Check the "Progress Tracking" or similar section to view your overall habit completion summary.
2. Identify habits you haven't completed and track your performance.

## 7. Manage Your Profile

Customize your profile to make it truly yours:

1. Access your user profile by clicking on your name or profile picture.
2. Edit and update your user profile details, including your display name and profile picture.
3. Choose from different color themes to personalize your experience.

Habitize is designed to help you successfully track and achieve your daily habits. Use these steps to create and manage your habits, track your progress, and customize your experience.

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

The User Model in Habitize utilizes the built-in Django User Model extended with AllAuth for user authentication. It includes fields for username, email, password, and other authentication-related data. The User Model serves as the foundation for user registration and login processes.

![erd](/screenshots/erd.png)

[DrawSQL app](https://drawsql.app/) was used to create the ERD.


## Category

The `Category` model represents a category for habits.

### Fields

- `name`: A character field with a maximum length of 50 characters.

## Habit

The Habit Model is central to Habitize's core functionality. It represents the habits that users want to track. This model includes attributes such as habit name, description, and other habit-related data. It is directly connected to the User Model via a foreign key, allowing each user to have their set of habits.

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

In addition to the User Model, there's a custom User Profile Model. This model extends the user's profile information and allows users to personalize their experience by selecting different Color Themes. This model includes a field to store the chosen color theme, providing users with a way to customize the visual appearance of their interface.

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


## Logic Map

[Logic Map](https://www.figma.com/file/VjMGn71dAh1oFA959Chgv2/Untitled?type=whiteboard&node-id=0%3A1&t=7GxvzogChqdHBwz7-1)

![Logic Map](/screenshots/logic-map.png)

A logic map was developed to outline the comprehensive functionality and navigation flow of the system. This logic map serves as a visual guide, illustrating the logical sequence of actions and connections within the application, ensuring a structured and intuitive user experience.

I also used [Figma](https://www.figma.com/) to create this.

## Wireframes 

[Wireframe](https://www.figma.com/file/R6z2UxOhrRZt2lgCZuNo5l/Habitize?type=design&node-id=0%3A1&mode=design&t=GgmSyiNRLry0qZJB-1)

![Wireframe](/screenshots/wireframe.png)

Wireframes were created for every significant page, tailored to both mobile and tablet devices. These wireframes were designed with the primary goal of ensuring that the website is fully responsive, adapting seamlessly to various device sizes.

I used [Figma](https://www.figma.com/) for creating the wireframes.
# Pages

## Landing Page
The Landing Page serves as the initial entry point for users. It provides a welcoming introduction to the application, offering a glimpse of what the app is all about and encouraging users to explore further. Users can quickly grasp the purpose and appeal of the application from this page.
  ![Landing page](/screenshots/landing-page.gif)
## Login Page
The Login Page offers a secure gateway for registered users to access their accounts. Users can log in with their credentials, ensuring their data and habits are kept private. This page grants users control over their personalized habit tracking.
  ![Login](/screenshots/login.png)
## Signup Page
The Signup Page allows new users to join the application. By creating an account, users can start their habit-tracking journey. It offers a straightforward registration process to get them started quickly and effectively.
  ![Signup](/screenshots/signup.png)
## Help Page
The Help Page provides users with essential guidance and support. It serves as a valuable resource for understanding how to use the application effectively. Users can find answers to their questions, troubleshoot issues, and maximize their experience.
  ![Help Page](/screenshots/help-page.gif)
## Dashboard
The Dashboard is the central hub for users to manage and monitor their habits. It offers an at-a-glance overview of their progress and goals. Users can easily track and stay motivated to achieve their habits on this page.
  ![Dashboard](/screenshots/dashboard.png)
## Add Habits Page
The Add Habits Page empowers users to set and customize their habits. It allows them to define the name, details, tracking frequency, and completion goals for new habits. Users can personalize their habit tracking to align with their specific goals and preferences.
  ![Add Habits](/screenshots/add-habit-2.png)
## Edit Habits Page
The Edit Habits Page enables users to modify and fine-tune their existing habits. Users can update habit details, targets, and tracking options as they progress. This flexibility supports users in refining their tracking to better fit their evolving needs.
  ![Edit Habits](/screenshots/edit-habit.gif)
## View Profile Page
The View Profile Page allows users to discover and learn more about other users within the community. It fosters social interaction and engagement, encouraging users to connect, share experiences, and gain inspiration from others.
  ![View Profile](/screenshots/view-profile.png)
## Edit Profile Page
The Edit Profile Page puts users in control of their personal information. They can customize their profile, update their display name, and even change their profile picture. This page lets users tailor their public identity within the app to their liking.
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
   ![custom username](/screenshots/username-edit.png)
   - Change your profile picture.
   ![custom profile image](/screenshots/custom-profile-image.png)
   - Change your color theme.
   ![color theme](/screenshots/color-theme-change.png)

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
    - Users will also receive feedback messages for errors.
    ![Error Feedback Messages](/screenshots/file-to-large.png)

# Future Enhancements

There where a few features i would have like to implement in the future. I have left them on the kanban board as won't have user stories. 
The features I would like to add in future are:

 - [#59](https://github.com/jflets/Habitize/issues/59) Sending users notifications fit they have not completed habit or if they have not logged any habits in a time period.
 - [#60](https://github.com/jflets/Habitize/issues/60) Automated habit frequency breakdown, I would like to have a feature where when a weekly or monthly habit is added it breaks won into daily or weekly habits.
 - [#61](https://github.com/jflets/Habitize/issues/61) User streaks, I would want to allow users to track their consistency by seeing a streak of their habit completions for a month or longer.

 These features would need to be developed further in order to see wether they would be suitable.

# Design

In the development of Habitize, careful attention was given to the visual design and user interface. The color scheme was meticulously curated using the [Coolors](https://coolors.co/) palette generator, ensuring that it resonates with the brand and provides a refined and modern aesthetic. The chosen color scheme has been thoughtfully selected to maintain high contrast, prioritizing accessibility for all users.

![Colour Palette](/screenshots/color-palette.png)

Typography played a crucial role in enhancing the site's appearance. The **Playfair** font from Google Fonts was chosen for its refined and elegant look. This selection ensures that the site's content, including habit details and user interactions, is presented in a clear and sophisticated manner, adding to the overall user experience.

![Playfair](/screenshots/font.png)

Images used in Habitize primarily focus on maintaining a polished and modern interface. While there is one playful cartoon image that adds a touch of personality, the overall design remains sleek and sophisticated. The cartoon image, contributing to a friendly and approachable ambiance, complements the site's objective of helping users establish positive habits.

With visual elements that strike a balance between refinement and approachability, Habitize aims to provide an engaging and user-friendly environment for habit tracking and personal growth.


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

- **Templates:**
   - I used Jinja tempting to insert data from the database into the site pages.

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
  - [Tableconvert](https://tableconvert.com) for creating the markdown testing tables.

- **Testing and Quality Assurance:**
  - Jest and JSDom for frontend testing
  - Django's TestCase and Jest for automated testing
  - Chrome developer tools for checking errors, accessibility and responsiveness.

- **Email Send Integration**
   - Gmail

- **Database Management:**
  - Django ORM for database interactions
  - ElephantSQL for the PostgreSQL database in production
  - SQLite for local development and testing

- **Image Conversion**
  - [CloudConvert](https://cloudconvert.com/) for MOV to GIF
  - [Convertio](https://convertio.co/) for PNG to WebP

# Testing

**Testing Strategy**

For the development of the Habitize app, a comprehensive testing strategy was employed to ensure its functionality, reliability, and user satisfaction. This strategy encompassed manual and automated testing procedures, validation checks, and validation of user story acceptance criteria.

## Testing Overview

Testing procedures were systematically divided into different sections to ensure rigorous examination of all aspects of the application. Each section had test cases specifically designed to evaluate its functionality and compliance with industry standards.

## Testing Schedule Overview

Detailed testing procedures and methodologies can be found [here](testing.md). This document contains a comprehensive breakdown of testing methods and schedules for each language used in the project.

## Automated Testing
- **JS Testing:** Using Jest and JSDOM
  ![JS Testing](/screenshots/js-test.gif)

- **Python Testing:** Using Uni test
  ![Python Testing](/screenshots/python-test.gif)
## Validator Testing

The Habitize app underwent thorough validation testing to ensure code quality and adherence to industry best practices. Full validator testing and screenshots can be found [here](/testing.md). The following validators were used:

1. **W3C HTML Validator:** To Put my HTML through a validator with the jinja template i had top copy the HTML file from chrome developer tools and than had to manually paste the HTML into W3C HTML validator.

2. **W3C CSS Validator:** CSS files were validated using the W3C CSS Validator to confirm that they adhered to CSS standards and had no errors or warnings.

3. **JSHint:** For JavaScript files, JSHint was employed to identify potential errors and code quality issues. This step helped maintain clean and efficient JavaScript code.

4. **PEP 8 for Python Files:** Python files were checked for adherence to PEP 8, the Python Enhancement Proposal that defines coding conventions for the Python codebase. This ensured consistent and readable Python code.

## Solved Bugs
Throughout the development of Habitize, a few notable bugs were encountered and successfully resolved. When facing challenges, my approach involved seeking solutions through personal research, utilizing online resources like Stack Overflow, and referring to tutorials on platforms such as YouTube. Below, I'll provide details about these specific challenges and how they were effectively resolved:

1. **Bug: Image Upload Issue**

   - **Description**: During testing and with feedback from personal contacts, I became aware of an issue related to users' difficulties in uploading images for their habits. This issue had the potential to impact the overall user experience and the visual representation of their habits.

   - **Resolution**: I meticulously investigated the problem and applied a solution based on the insights I gathered from my personal research. This involved revamping the image upload feature, providing more user-friendly guidance, and improving error handling. These changes ensured that users could seamlessly add images to their habits, significantly enhancing their experience.

2. **Bug: Unauthorized Page Access via URL Path**

   - **Description**: A security concern arose when I observed that users could access specific pages and features by manually entering URL paths, even if they weren't authenticated. Addressing this potential vulnerability was a top priority.

   - **Resolution**: As a solo developer, I took the initiative to fortify the application's security by improving access control mechanisms. This entailed revising routing and authorization logic to guarantee that only authorized users could access specific areas. My research into middleware and access control checks led to the successful prevention of unauthorized access via URL paths, strengthening the application's security.

3. **Bug: Habit Ownership and User Association**

   - **Description**: A critical bug affecting the core functionality of Habitize came to light. It was discovered that habits were not correctly associated with specific users, resulting in habits being inadvertently shared among users.

   - **Resolution**: As the sole developer, I undertook a comprehensive analysis and identified that the issue stemmed from database schema misalignment. My research, combined with feedback from personal contacts, led to the restructuring of the database schema and habit creation process. This ensured that each habit was accurately linked to the user who created it, providing users with a personalized and secure experience.

## Known Bugs

As of the most recent release of Habitize, there is one known bug more so a css container setting. I have nested the habits within a container and the options button is nested in the habit, when a user clicks the option button within a habit the dropdown menu is partly hidden and requires the user to scroll down to see the full list of options. I have been unable to fix this without breaking the habit styling itself.

# Deployment

Habitize has been deployed to provide users with seamless access to their habit-tracking experience. The following steps outline how the project was deployed for public use.

**Project Deployment**

1. **Heroku Account**: To deploy Habitize, you need to have a Heroku account. Sign up or log in to Heroku if you don't have an account.

2. **Create a New App**: From the main Heroku Dashboard, select 'New' and then 'Create New App.' Choose a unique name for your app, e.g., Habitize, and select a suitable region. Click 'Create App' to continue.

3. **Heroku Postgres**: Navigate to the 'Resources' tab within your app's settings. In the 'Add-ons' section, search for 'Heroku Postgres,' select the package that appears, and add 'Heroku Postgres' as the database for your app.

4. **Database Configuration**: In the 'Settings' tab, under the 'Config Vars' section, you'll find the DATABASE_URL. Copy this value to your clipboard for later use in configuring Django.

5. **Environment Variables**: Create a new file in your Django app repository called `env.py`. Within this file, import the `os` library and set the environment variable for DATABASE_URL by pasting the link copied from Heroku. The line should appear as `os.environ["DATABASE_URL"] = "Paste the link in here."`

6. **Secret Key**: In the `env.py` file, add a secret key using `os.environ["SECRET_KEY"] = "your secret key goes here."` Don't forget to add this secret key to the Heroku Config Vars as `SECRET_KEY` for the KEY value and the secret key value you created as the VALUE.

7. **Django Configuration**: In the `settings.py` file within your Django app, make the following adjustments:
   - Import necessary libraries: `from pathlib import Path`, `import os`, and `import dj_database_url`.
   - Add the line: `if os.path.isfile("env.py"): import env`.
   - Replace the insecure default secret key with: `SECRET_KEY = os.environ.get('SECRET_KEY')`.
   - Replace the databases section with:
     ```python
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
     ```
     Ensure the correct indentation for Python is used.

8. **Migrate Models**: In your terminal, migrate the models to the new database connection.

9. **Cloudinary Configuration**: In a browser, navigate to Cloudinary. Log in or create an account and log in. From the dashboard, copy the CLOUDINARY_URL to your clipboard. In the `env.py` file, add `os.environ["CLOUDINARY_URL"] = "paste in the URL copied to the clipboard here."` Also, add the `KEY - DISABLE_COLLECTSTATIC` with the `Value - 1` to the Heroku Config Vars. Note that this key-value pair must be removed before the final deployment.

10. **Installed Apps**: Add the Cloudinary libraries to the list of installed apps. The order they are inserted is important. `'cloudinary_storage'` should go above `'django.contrib.staticfiles'`, and `'cloudinary'` should go below it.

11. **Static Files Configuration**: In the `settings.py` file, add the STATIC files settings, including the URL, storage path, directory path, root path, media URL, and default file storage path.

12. **Templates Directory**: Link the file to the templates directory in Heroku by adding: `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`. Change the templates directory to `TEMPLATES_DIR` under `'DIRS': [TEMPLATES_DIR]`.

13. **ALLOWED_HOSTS**: Add Heroku to the `ALLOWED_HOSTS` list. The format will be the app name given in Heroku when creating the app followed by `.herokuapp.com`.

14. **Top-Level Folders**: In your code editor, create three new top-level folders: `media`, `static`, and `templates`.

15. **Procfile**: Create a new file at the top-level directory named `Procfile`. Within the Procfile, add the following code: `web: gunicorn PROJECT_NAME.wsgi`.

16. **GitHub**: In the terminal, add the changed files, commit, and push to GitHub to ensure the latest code is available for deployment.

17. **Manual Deployment**: In Heroku, navigate to the 'Deployment' tab and deploy the branch manually. Watch the build logs for any errors.

Once the deployment process is complete, Heroku will display a 'Your App Was Successfully Deployed' message, along with a link to your Habitize app, making it accessible to users.

## Local Development

During the development of Habitize, a local development environment was set up to facilitate efficient coding, testing, and debugging. Local development offers several advantages, including improved development speed, offline accessibility, and enhanced testing capabilities. Here is an overview of the key aspects of local development for the Habitize application:

1. **Version Control with Git**: The project was managed using Git, a distributed version control system. Git allowed for effective collaboration, code tracking, and easy integration with online repositories, such as GitHub. All project code was maintained in Git repositories.

2. **Integrated Development Environment (IDE)**: An integrated development environment was used to streamline code writing and debugging. Popular IDEs, like Visual Studio Code, were chosen for their extensibility and compatibility with various programming languages and frameworks.

3. **Local Database Setup**: A local database, using SQLite, was configured for local development. SQLite is a lightweight, serverless database engine suitable for development and testing. It allows developers to work with a database without the need for a separate database server.

4. **Virtual Environments**: Python virtual environments were employed to isolate project dependencies. This ensured that the required packages and libraries were consistent and did not interfere with other Python projects. Virtual environments enhance project portability and maintain clean development environments.

5. **Requirements File**: A requirements.txt file was maintained to list all project dependencies. This file made it easy to install the necessary packages with a single command, ensuring that the project could be replicated in different environments.

6. **Debugging Tools**: Debugging tools, Django Debug Toolbar and print statements, were used extensively to identify and resolve issues within the application. These tools provided insights into the application's behavior and performance during local testing.

7. **Development Server**: Django's built-in development server was used to run the application locally. This server allows developers to preview the application in a browser and perform real-time testing and debugging.

8. **Local Database**: I used the built in Django database an automated testing database. This means there is some commented out code in my settings.py: 
   ``` 
   DATABASES = {
      'default': {
            'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
      }
   }
   ```
   As this is only used when running the automated tests.

# Credits
**Resources Used**

The development of Habitize was supported by various resources to ensure the successful implementation of features and functionalities.

1. **Django Documentation**: Extensive use of the Django documentation was made throughout the project. It served as a valuable reference for Django framework-related concepts, ensuring the project's robustness and adherence to best practices.

2. **Django AllAuth Documentation**: The Django AllAuth documentation played a crucial role in guiding the implementation of user authentication features. It provided a comprehensive guide for integrating the package into the project and achieving user account management capabilities.

3. **Cloudinary Documentation**: The Cloudinary documentation was an essential resource during development. It facilitated the setup and configuration of Cloudinary APIs within the Django application. This resource was particularly valuable in enabling media file management, including image uploads and storage.

4. **Code Institute Reference Material**: The Code Institute reference material was consulted as a general resource for aspects that had been previously covered during the course. It provided guidance and reference points to ensure the project's alignment with industry standards.

5. **Django Google Authentication Tutorial**: A helpful tutorial on implementing Google authentication using Django AllAuth was referenced during the development. You can find the tutorial [here](https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8). This resource assisted in setting up Google login functionality within Habitize.

6. **Django Email Sending Guide**: To ensure secure and efficient email functionality, the guide on how to send email with Django and Gmail in production was followed. You can access the guide [here](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab). This resource provided essential insights into configuring email sending with Gmail for production use, enhancing communication features within Habitize.

7. **Bootstrap Color Modes**: The project also incorporated color themes for users, allowing them to customize their experience. The [Bootstrap Color Modes](https://getbootstrap.com/docs/5.3/customize/color-modes/#dark-mode) documentation provided guidance on implementing dark mode and other color modes, enhancing user interface personalization within Habitize.

8. **Other Referenced Resources**: Any additional resources used during the project are appropriately referenced and acknowledged, ensuring transparency and credit to the respective sources.

9. **Acknowledgments**: Thank you to my tutor Graeme Taylor for all his guidance and support.