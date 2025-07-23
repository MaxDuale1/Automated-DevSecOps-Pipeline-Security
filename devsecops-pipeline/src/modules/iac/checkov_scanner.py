def checkov_scan(directory):
    import checkov
    from checkov.runner_filter import RunnerFilter
    from checkov.terraform.runner import Runner as TerraformRunner
    from checkov.kubernetes.runner import Runner as KubernetesRunner

    # Initialize the Checkov runner for Terraform and Kubernetes
    terraform_runner = TerraformRunner()
    kubernetes_runner = KubernetesRunner()

    # Run the scans
    terraform_results = terraform_runner.run(root_folder=directory)
    kubernetes_results = kubernetes_runner.run(root_folder=directory)

    # Combine results
    results = {
        "terraform": terraform_results,
        "kubernetes": kubernetes_results
    }

    return results

def output_results(results):
    import json

    # Output the results in JSON format
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python checkov_scanner.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    scan_results = checkov_scan(directory)
    output_results(scan_results)