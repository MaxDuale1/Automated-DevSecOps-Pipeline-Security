def run_safety_scan():
    import subprocess
    import json

    # Run the Safety scan
    result = subprocess.run(['safety', 'check', '--json'], capture_output=True, text=True)

    # Check if the scan was successful
    if result.returncode != 0:
        print("Safety scan failed.")
        return None

    # Parse the JSON output
    try:
        scan_results = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Failed to decode JSON from Safety scan output.")
        return None

    return scan_results


if __name__ == "__main__":
    results = run_safety_scan()
    if results:
        print(json.dumps(results, indent=4))