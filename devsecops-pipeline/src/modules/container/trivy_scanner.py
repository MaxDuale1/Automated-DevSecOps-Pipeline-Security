def run_trivy_scan(image_name):
    import subprocess
    import json

    try:
        # Run the Trivy scan command
        result = subprocess.run(
            ["trivy", "image", "--format", "json", image_name],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the JSON output
        scan_results = json.loads(result.stdout)
        return scan_results

    except subprocess.CalledProcessError as e:
        print(f"Error running Trivy scan: {e.stderr}")
        return None

if __name__ == "__main__":
    # Example usage
    image = "your-container-image:latest"
    results = run_trivy_scan(image)
    if results:
        print(json.dumps(results, indent=2))