import os
import json
from dotenv import dotenv_values

# 1. Read .env
env_vars = dotenv_values(".env")

# 2. Read serviceAccountKey.json
with open("serviceAccountKey.json", "r") as f:
    service_account = json.load(f)
    # Compact JSON string
    env_vars["FIREBASE_SERVICE_ACCOUNT"] = json.dumps(service_account)

# 3. Write to env_vars.yaml
# We'll write it manually to avoid dependency issues if PyYAML isn't installed
# YAML format:
# KEY: "VALUE"
with open("env_vars.yaml", "w") as f:
    for key, value in env_vars.items():
        # Simple YAML escaping: wrap in quotes, escape existing quotes
        if value:
            # Escape double quotes and backslashes
            safe_value = value.replace('\\', '\\\\').replace('"', '\\"')
            f.write(f'{key}: "{safe_value}"\n')

print("env_vars.yaml created successfully.")
