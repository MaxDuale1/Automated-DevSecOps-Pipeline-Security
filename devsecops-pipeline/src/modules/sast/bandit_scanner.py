import json
import subprocess

def run_bandit_scan(target_directory):
    """Run Bandit scan on the specified directory."""
    try:
        result = subprocess.run(['bandit', '-r', target_directory, '-f', 'json'], capture_output=True, text=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error running Bandit scan: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    target_dir = "path/to/your/codebase"  # Replace with the actual path
    scan_results = run_bandit_scan(target_dir)
    if scan_results:
        print(json.dumps(scan_results, indent=4))  # Output results in JSON format