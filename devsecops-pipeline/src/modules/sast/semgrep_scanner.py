def run_semgrep_scan():
    import subprocess
    import json

    # Define the command to run Semgrep
    command = ["semgrep", "--config", "path/to/semgrep/rules", "--json"]

    try:
        # Run the Semgrep command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Parse the JSON output
        output = json.loads(result.stdout)
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error running Semgrep: {e}")
        return None

def main():
    results = run_semgrep_scan()
    if results:
        # Output the results in SARIF format
        with open("semgrep_results.sarif", "w") as f:
            json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()