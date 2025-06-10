# This script is meant to act as a Entrypoint for the launch of the Application, Allowing for a "Cleaner Run".
# run.py

from app import create_app

app = create_app()

# remove the first 3 lines below after debugging or dont include in production
print("Registered Routes:")
for rule in app.url_map.iter_rules():
    print(rule)  # debugging purposes
if __name__ == "__main__":
    app.run(debug=True)
