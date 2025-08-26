import secrets

def generate_env_secrets():
    keys = {}

    with open('.env', 'w') as f:
        for key, value in keys.items():
            f.write(f"{key}={value}\n")
        
        print(".env file created with secure secrets")
if __name__ == '__main__':
    generate_env_secrets()

