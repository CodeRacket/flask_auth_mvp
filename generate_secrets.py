import secrets
import string

def generate_secret(length=50):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_env_secrets():
    keys = {
        "SECRET_KEY": generate_secret(50),
        "POSTGRES_DB": "db",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PASSWORD": generate_secret(20),
        "PGADMIN_DEFAULT_EMAIL": "admin@example.com",
        "PGADMIN_DEFAULT_PASSWORD": generate_secret(20),
        "DATABASE_URL": "postgresql://postgresql:{}@db:5432/db".format(generate_secret(20))
    }

    with open('.env', 'w') as f:
        for key, value in keys.items():
            f.write(f"{key}={value}\n")

    print(".env file created with secure secrets")

if __name__ == '__main__':
    generate_env_secrets()
