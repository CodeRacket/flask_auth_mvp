# Flask Auth MVP

A secure and lightweight authentication system built with Python and Flask, containerized with Docker. Features include user registration, login/logout, and session management. Security is enforced through CSRF protection, secure password hashing, and route protection via Flask-Login. 

## Features

- User Registration with Unique email and username validation.
- CSRF Protection using Flask-WTF
- Secure password hashing using Werkzeug
- Login and logout with session management via Flask-Login
- Flash messages for user feedback (success/error)
- Protected dashboard route requiring authentication 
- Modular route structure using Flask Blueprints 
- Docker: a cross-platform solution for developing and deploying applications

## Tech Stack

- **Language**: Python 3.11
- **Framework**: Flask 3.1.1
- **Auth**: Flask-Login, Flask-Bcrypt, bcrypt
- **Forms & Validation**: Flask-WTF, WTForms, email-validator
- **Secure Password Hashing**: werkzeug
- **ORM**: SQLAlchemy, Flask-SQLAlchemy
- **Migrations**: Flask-Migrate
- **Database**: PostgreSQL (via psycopg2)
- **Templating**: Jinja2
- **Pythonic WSGI Server**: Gunicorn
- **Environment Management**: python-dotenv
- **Containerization**: Docker
- **Web Server**: NginX


## Project Structure

```
flask_auth_mvp/
├── app/
│   ├── __init__.py            # App factory and extension initialization
│   ├── models.py              # SQLAlchemy models with auth methods
│   ├── routes.py              # Flask blueprint routes
│   ├── forms.py               # WTForms for login/registration
│   ├── custom_commands.py     # Custom CLI commands (e.g. test runner)
│   └── templates/             # Jinja2 HTML templates
│       ├── base.html
│       └── ... (dashboard, login, register, etc.)
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── ... (other unit tests)
├── migrations/                # Alembic database migrations
├── compose.yaml              # Docker Compose configuration
├── Dockerfile                # Docker build instructions
├── env_example               # Example .env file
├── generate_secrets.py       # Script to generate .env secrets
├── manage.py                 # DB initialization script
├── run.py                    # Flask app entry point
├── setup_docker.sh           # Setup helper script
├── scan_secrets.sh           # Secret scanning script
├── nginx.conf                # Nginx reverse proxy config
├── pyproject.toml            # Poetry project file
├── poetry.lock               # Locked dependency versions
├── mypy.ini                  # Type checking config
├── LICENSE                   # GNU-GPL License
└── README.md                 # Project documentation
```

## Getting Started
### 1. Clone the Repository

```bash

git clone https://github.com/CodeRacket/flask_auth_mvp
cd flask_auth_mvp
```

### 2. Create .env environmental variables 
```bash
python3 generate_secrets.py
```

add the below lines to the .env file This uses environmental variables so the system can differentiate between development and production modes. 
```bash
FLASK_APP=wsgi.py       # For integrating Flask migrations
# Developer mode is not full setup as of now. 
FLASK_ENV=development   # For setting developer mode or production
```
> Note: If using `.env` locally without Docker, ensure it's loaded before running `flask` or `python run.py` (use `python-dotenv` or `source .env`).

> Do not commit .env to version control

### 3.)Install Dependencies
    *Consult the Docker documentation for installing docker on your machine*
    **Security Precaution**: 
    - After installing Docker, add your user to the docker group to avoid needing `sudo`.
Example(Linux):
```bash
sudo usermod -aG docker $USER
```
>Then signout and back into your user account or restart the terminal to apply new permissions.

### 4.)Run the app in Docker & initialize the database
```bash
docker compose up --build
```

### 5.)Initialize the Database(Flask-Migrate via Docker)
Once your containers are running:

```bash
docker compose exec web flask db init           # one time setup
docker compose exec web flask db migrate -m "Initial schema"
docker compose exec web flask db upgrade        # Applies changes to the actual DB
```

**Database Migrations Overview**
- One-time setup(creates the migrations/ directory)
```bash
docker compose exec web flask db init   
```

Create migration (after updating models)
```bash
docker compose exec web flask db migrate -m "Initial migration"
```

Apply migration to the database:
```bash
docker compose exec web flask db upgrade
```
> Always Review auto-generated migration scripts in `migrations/versions/` before running `flask db upgrade`, especially if you are removing or renaming fields. 


## Note: Due to recent updates this app now depends on at least developer certs for TLS. 

### 1.) Install mkcert for your system

### 2.) mkdir flask_auth_mvp/ssl && cd flask_auth/ssl

### 3.) run the following commands to generate the certificate 
```bash 
mkcert -install # installs them on your system as trusted certificates
mkcert localhost 127.0.0.1 ::1
```
**This generates 2 .pem files**
*localhost+2.pem and locahost+2-key.pem*
The configurations have already been added to nginx.conf and compose.yaml

 
## Deployment   

To deploy this project, configure environment variables and use a platform like:

* Render
* Fly.io
* Railway

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
* Portfolio: https://coderacket.com/
