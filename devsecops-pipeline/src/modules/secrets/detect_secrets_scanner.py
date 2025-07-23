# Contents of /devsecops-pipeline/devsecops-pipeline/src/modules/secrets/detect_secrets_scanner.py

import os
import json
import subprocess

def run_detect_secrets(scan_path):
    """Run detect-secrets on the specified path."""
    try:
        result = subprocess.run(
            ['detect-secrets', 'scan', scan_path],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running detect-secrets: {e}")
        return {}

def main():
    scan_path = os.getcwd()  # Scan the current working directory
    secrets_report = run_detect_secrets(scan_path)
    
    # Output the results in JSON format
    print(json.dumps(secrets_report, indent=4))

if __name__ == "__main__":
    main()