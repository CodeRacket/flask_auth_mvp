#!/bin/bash

# Define a list of keywords used for storing SECRET
secret_identifiers=("SECRET_KEY" "PGADMIN_DEFAULT_PASSWORD" "POSTGRES_PASSWORD" "DATABASE_URL" )

for identifier in "${secret_identifiers[@]}"; do 
  echo "Searching for: $identifier"
  grep -Rn --exclude-dir=venv --exclude-dir=.venv --exclude-dir=.git "$identifier" .
done


