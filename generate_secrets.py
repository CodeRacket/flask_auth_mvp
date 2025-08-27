#!/usr/bin/python3
#
# Generates a secure .env file with random secrets 
# Useful for setting up Flask apps with PostgreSQL

import secrets # Cryptographically secure random generator
import string   
from urllib.parse import quote_plus # Encodes special chars for URLs

# Random string generator letters, digits, (default length: 50 )
def generate_secret(length=50):
    alphabet = string.ascii_letters + string.digits + "-_"
    return ''.join(secrets.choice(alphabet) for _ in range(length))



def generate_env_secrets():
    # Setup PostgreSQL variables 
    postgres_user = "postgres"
    postgres_db = "db"
    postgres_passwd_raw = generate_secret(20)
    postgres_passwd_encoded = quote = quote_plus(postgres_passwd_raw)
    
    # Define environmental variables for Flask + PostgreSQL w/ pgAdmin
    keys = {
        "SECRET_KEY": generate_secret(50),  #Flask/Django secret key for session management
        "POSTGRES_DB": postgres_db,
        "POSTGRES_USER": postgres_user,
        "POSTGRES_PASSWORD": postgres_passwd_raw,
        "PGADMIN_DEFAULT_EMAIL": "admin@example.com",
        "PGADMIN_DEFAULT_PASSWORD": generate_secret(20),
        "DATABASE_URL": f"postgresql://{postgres_user}:{postgres_passwd_encoded}@db:5432/{postgres_db}" # URL encoded for PostgreSQL DB
    }

    # output to a file named .env
    with open('.env', 'w') as f:
        for key, value in keys.items():
            f.write(f"{key}={value}\n")

    print(".env file created with secure secrets")

if __name__ == '__main__':
    generate_env_secrets()
