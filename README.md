# 🏃 Run_Away

## 📝 Project Overview

**Run_Away** is a user-friendly web application designed to help runners track and log their running sessions. It provides an intuitive interface for recording distance and time, automatically calculating pace, and offering a personalized way to monitor running progress.

---

## ✨ Key Features

* **User Authentication:** Secure registration and login functionality to ensure personalized tracking.
* **Run Logging:** Users can easily log a new run by entering the date, distance, and time.
* **Automatic Pace Calculation:** The application instantly calculates and displays the user's running pace for each logged run.
* **Recent Activity Dashboard:** The home page dynamically displays a list of the user's most recent runs, offering a quick overview of recent activity.
* **Theming:** Includes a **dark/light mode** toggle for user comfort and preference.

---

## 🛠️ Technologies Used

| Category | Technology |
| :--- | :--- |
| **Backend** | **Python** (The primary language) |
| **Framework** | **Flask** (Used for routing, requests, and sessions) |
| **Database** | **SQLite** (`main.db` file) |
| **Frontend** | **HTML, CSS** |
| **Templating** | **Jinja** |
| **Interactivity** | **JavaScript (JS)** |

---

## 🚀 Installation and Setup

### Prerequisites

To run this project locally, you must have the following installed:

* **Python 3**
* **pip** (Python package installer)

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Sohan-Raj-Adhikari/Run_away/](https://github.com/Sohan-Raj-Adhikari/Run_away/)
    cd Run_away
    ```

2.  **Install Dependencies:**
    Install the required Python packages (including `Flask` and `CS50`) using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application:**
    Start the Flask development server. Since the database file (`main.db`) is already included in the repository, no manual initialization or setup is required:
    ```bash
    flask run
    ```
    The application should now be accessible in your web browser at `http://127.0.0.1:5000/`.

---

## 💡 Usage

1.  **Get Started:** Navigate to the `/register` route and create a new account.
2.  **Log In:** Access the application using your credentials at the `/login` route.
3.  **Log a Run:** Input the date, distance, and time of your run. The application will handle the pace calculation.
4.  **Monitor:** View your logged runs and pace metrics on the homepage dashboard.
5.  **Customize:** Toggle between light and dark modes based on your viewing preference.

---

## 🎥 CS50 Video Submission

* **Link to Project Demo Video:** **[To be inserted later]**
* *Note: This video provides a comprehensive walk-through of the application's functionality.*

---

## 🧑‍💻 Author

* **Sohan Raj Adhikari**
