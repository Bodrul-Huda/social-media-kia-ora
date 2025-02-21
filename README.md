# Social Media Application (DJA01 - BRD)

## Table of Contents
1. Introduction
2. Objectives
3. Scope
4. Functional Requirements
5. Non-Functional Requirements
6. Technology Stack
7. Constraints & Timeline
8. Deliverables
9. Evaluation Criteria
10. Summary

---

## 1. Introduction
This project is a simple social media application built using Django (backend) and HTML, CSS, and JavaScript (frontend). The application mimics a basic version of Facebook by providing features such as:
- A homepage displaying posts from all users.
- A profile page displaying only the logged-in user’s posts with options to edit or delete them.
- A simple navbar and footer for navigation.

---

## 2. Objectives
- **Django Proficiency:** Implement Django models, views, forms, template inheritance, and authentication.
- **User Experience:** Provide a clean and intuitive UI using Bootstrap or Tailwind.
- **CRUD Operations:** Implement Create, Read, Update, and Delete functionalities for posts.
- **User-Specific Views:** Separate global feed and user-specific profile pages.

---

## 3. Scope
### Core Features
#### User Management
- **Registration:** User registration form using Django’s built-in user model.
- **Authentication:** Login and logout functionality.
- **Password Management (Bonus):** Password reset and change options.

#### Post Management
- **Homepage (Global Feed):** Displays posts from all users.
- **User Profile Page:** Displays only the logged-in user’s posts with edit/delete options.
- **Create Post:** Allows users to create posts with text and an optional image.
- **Update & Delete Post:** Users can edit or delete only their posts, with a confirmation before deletion.

#### User Interaction & Layout
- **Navbar & Footer:** Navigation bar for easy access to different sections.
- **Feedback:** Use Django’s message framework to display notifications.

### Additional Considerations
- **Template Inheritance:** Consistent layout across all pages.
- **Query Optimization:** Use `select_related` and `prefetch_related` where applicable.
- **Security:** Protect restricted pages using `LoginRequiredMixin` or `login_required` decorator.

---

## 4. Functional Requirements
### User Management
- Registration with fields: `username`, `email`, `password`, and `confirm password`.
- Login and logout with Django’s built-in authentication.
- Access control to restrict post creation/editing/deletion to authenticated users.

### Post Management
- **Global Feed:** Displays all posts.
- **User Profile Page:** Displays only the logged-in user’s posts with edit/delete options.
- **Create Post Form:** Allows users to submit text content and optionally upload an image.
- **Update & Delete Post:** Only the post owner can edit or delete a post, with a confirmation prompt before deletion.

### Layout & Navigation
- **Navbar:** Includes links to homepage, profile, login/logout, and registration pages.
- **Footer:** Displays basic site information.
- **Feedback:** Utilizes Django’s messages framework for user notifications.

---

## 5. Non-Functional Requirements
- **Simplicity:** Easy to use and test.
- **Code Quality:** Follows Django best practices and is well-documented.
- **Usability:** Provides an intuitive and accessible interface.
- **Performance:** Uses optimized database queries.
- **Documentation:** Includes a README with setup instructions and project details.

---

## 6. Technology Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default for Django)
- **Version Control:** Git (GitHub recommended)
- **User Authentication:** Django’s built-in user model and authentication views

---

## 7. Constraints & Timeline
- **Deadline:** As specified on the Ostad platform.
- **Scope:** Focus on core features; avoid unnecessary complexity.
- **Testing:** Ensure manual testing of all features before submission.

---

## 8. Deliverables
- **Source Code:** GitHub repository with well-organized and commented code.
- **README File:**
  - Sample user credentials for testing.
  - Setup and installation instructions.
  - Summary of implemented features.
- **ER Diagram:** Image file illustrating the database structure.
- **Testing Credentials:** At least two sample user accounts.
- **(Optional) Video Demonstration:** A short walkthrough showcasing the application’s functionality.

---

## 9. Evaluation Criteria
- **Functionality:** Does the application meet the core requirements?
- **Code Quality:** Is the code structured and following best practices?
- **User Interface:** Is the design clean and intuitive?
- **Documentation:** Are setup instructions and project details clear and complete?

---

## 10. Summary
This Django-based social media application demonstrates backend and frontend development skills. The key features include:
- A homepage with posts from all users.
- A profile page displaying user-specific posts with edit/delete options.
- A simple and consistent UI with a navbar and footer.

Focus on implementing the core requirements to ensure a functional and testable project. Best of luck!

