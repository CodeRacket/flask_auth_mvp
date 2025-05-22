# Flask Auth MVP

A secure and lightweight authentication system built with Python and Flask. Features include user registration, login/logout, and session management. Security is enforced through CSRF protection, secure password hashing, and route protection via Flask-Login.

## Features

- User Registration With Unique email and username validation.
- CSRF Protection using Flask-WTF
- Secure password hashing using Werkzeug
- Login and logout with session management via Flask-Login
- Flash messages for user feedback (success/error)
- Protected dashboard route requiring authentication 
- Modular route structure using Flask Blueprints 

## Tech Stack

- **Python 3.11.2+**
- **Flask 3.1.1** – Web framework for routing and handling HTTP requests
- **Flask-WTF 1.2.2** – Simplified form handling with CSRF protection
- **Flask-Login 0.6.3** – Session management and authentication
- **Werkzeug 3.1.3** – Secure password hashing
- **SQLite 2.0.40** – Lightweight relational database
- **Flask-SQLAlchemy 3.1.1** – ORM for database interaction
- **Jinja2 3.1.6** – Templating engine for rendering HTML

## Project Structure
```

Flask\_Auth\_MVP/
├── app/
│   ├── **init**.py          # App factory + extension initialization
│   ├── models.py            # SQLAlchemy User model with password methods
│   ├── routes.py            # All Flask routes using Blueprint
│   ├── forms.py             # Registration and login forms
│   └── templates/           # Jinja2 templates
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
├── run.py                   # Entry point for the app
├── requirements.txt
├── .env                     # Environment variables (SECRET\_KEY)
└── README.md
```

## Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/CodeRacket/Flask_Auth_MVP.git
cd Flask_Auth_MVP
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables:

Create a `.env` file in the root directory and add:

```
SECRET_KEY=your-secret-key
```
> Do not commit `.env` to version control.

### 5. Initialize the database(First Run):

```bash
python
>>> from app import create_app
>>> from app.models import db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
```

6. Run the application:

```bash
flask run
```


## Deployment

To deploy this project, configure environment variables and use a platform like:

* Render
* Fly.io
* Railway

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

---

## Full License (GPL v3)

The GNU General Public License (GPL) v3 applies to this project, and you are free to redistribute and modify the software under its terms. The full text of the license is available in the [LICENSE](LICENSE) file. Here is a brief summary:

1. **Freedom to Use**: You can use the software for any purpose.
2. **Freedom to Modify**: You can modify the software and adapt it to your needs.
3. **Freedom to Distribute**: You can redistribute the original or modified versions of the software, under the same license.
4. **Freedom to Contribute**: If you distribute modified versions, you must share the source code, and your changes must be documented.

This project comes with **NO WARRANTY**. See the LICENSE for full terms.


## Author

* Created by:  Nathaniel Andreano
* For contact or freelance inquiries: Contact@CodeRacket.com 
portfolio: https://coderacket.com/

