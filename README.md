# Lain Notes — Personal Notes Manager

*A personal space for thoughts, memories, and ideas. Inspired by the atmosphere of Serial Experiments Lain and The Wired.*

## About the Project

Lain Notes is a web-based personal notes application built using **Python, Flask, and MySQL**.

The application allows users to create and manage their personal notes through an account-based system. Each user has their own collection of notes, stored in a MySQL database and associated with their account.

The project focuses on combining backend development concepts with a minimal, atmospheric interface inspired by the digital world of *Serial Experiments Lain*.

## Features

- **User Registration:** Create an account using an email address and username.
- **User Authentication:** Login and logout using Flask sessions.
- **Password Security:** Passwords are stored as hashes using Werkzeug's password hashing utilities.
- **Create Notes:** Add notes with a title and content.
- **Edit Notes:** Update existing notes.
- **Delete Notes:** Remove notes from your archive.
- **Personal Notes:** Notes are associated with individual users.
- **Timestamps:** Notes include creation timestamps and an optional edited timestamp.
- **MySQL Database:** Store user accounts and notes persistently.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and routing |
| MySQL | Database management |
| MySQL Connector | Python–MySQL connectivity |
| HTML | Page structure |
| CSS | User interface and styling |
| Werkzeug | Password hashing |
| python-dotenv | Environment variable management |

## Database Structure

The application uses two main tables:

### 1. Users

Stores registered user information.

| Column | Description |
|---|---|
| `user_id` | Primary key |
| `gmail` | User email |
| `hash_password` | Hashed password |
| `username` | Username |

### 2. Notes

Stores notes created by users.

| Column | Description |
|---|---|
| `id` | Primary key |
| `title` | Note title |
| `content` | Note content |
| `created_at` | Note creation timestamp |
| `edited` | Optional edited timestamp, default NULL |
| `user_id` | Foreign key referencing Users |

**Relationship:** One user can have multiple notes. Each note belongs to one user through the `user_id` foreign key.

## Project Structure

```text
Lain-Notes/
│
├── app.py
├── database_services.py
├── .env
├── .gitignore
│
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── add_notes.html
│   ├── edit.html
│   └── about.html
│
└── static/
    ├── css/
    │   └── style.css
    └── images/
        └── wired-bg.jpg
```

*Adjust the structure above if your actual filenames or folders differ.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/lain-notes.git
cd lain-notes
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask mysql-connector-python python-dotenv werkzeug
```

### 4. Configure environment variables

Create a `.env` file and configure your Flask secret key and the MySQL connection settings required by `database_services.py`.

Example:

```env
secret_key=your_secret_key_here
```

Do not upload your actual `.env` file or database credentials to GitHub.

### 5. Set up MySQL

Create a MySQL database and configure the two tables described in the Database Structure section. Make sure the `Notes.user_id` foreign key references `Users.user_id`.

### 6. Run the application

```bash
python app.py
```

Open the local address shown in your terminal:

```text
http://127.0.0.1:5000/
```

## What I Learned

Building this project helped me practice:

- Flask routing and handling GET and POST requests.
- Working with HTML forms and Jinja templates.
- Connecting Python applications to MySQL.
- Designing relational database tables and foreign keys.
- Implementing registration and login functionality.
- Hashing and verifying passwords.
- Using Flask sessions for user authentication.
- Organizing database operations into separate service functions.

## Future Improvements

- Search and filter notes.
- Add categories or tags.
- Improve responsive design.
- Deploy the application publicly.
- Add stronger ownership checks for note editing and deletion.
- Add additional account and session security.

---

**Project Status:** Development

**Built with:** Python, Flask, MySQL, HTML & CSS.
