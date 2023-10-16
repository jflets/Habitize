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
- [Target Audience](#target-audience)
  - [User Stories](#user-stories)
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

## Target Audience

### User Stories

1. [User Story 1]
   - As a [type of user], I want to [perform an action] so that [benefit or reason].

2. [User Story 2]
   - As a [type of user], I want to [perform an action] so that [benefit or reason].

[Add more user stories if needed.]

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
   ![Edit Habits](/screenshots/edit-habit.png)
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
    ![Help Page](/screenshots/help-htu.png)
    ![Contact Form](/screenshots/help-cu.png)

10. **Admin Dashboard:**
    - Admin panel for managing user accounts (for admin users).
    ![Admin Panel](/screenshots/admin.png)


# Technologies Used
# Frameworks, Libraries, and Tools Used
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
