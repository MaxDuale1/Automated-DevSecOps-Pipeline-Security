import json
import sys
from modules.sast.bandit_scanner import run_bandit_scan
from modules.sast.semgrep_scanner import run_semgrep_scan
from modules.dependency.safety_scanner import run_safety_scan
from modules.container.trivy_scanner import run_trivy_scan
from modules.iac.checkov_scanner import run_checkov_scan
from modules.secrets.detect_secrets_scanner import run_detect_secrets_scan
from report.generator import generate_report
from utils.json_helper import load_json

def main():
    # Load configuration and thresholds
    config = load_json('src/config/config.json')
    thresholds = load_json('src/config/thresholds.json')

    # Initialize results dictionary
    results = {
        'bandit': None,
        'semgrep': None,
        'safety': None,
        'trivy': None,
        'checkov': None,
        'detect_secrets': None
    }

    # Run scans
    results['bandit'] = run_bandit_scan()
    results['semgrep'] = run_semgrep_scan()
    results['safety'] = run_safety_scan()
    results['trivy'] = run_trivy_scan(config['container_image'])
    results['checkov'] = run_checkov_scan()
    results['detect_secrets'] = run_detect_secrets_scan()

    # Generate report
    report = generate_report(results)

    # Check for critical issues based on thresholds
    critical_issues_found = False
    for key, result in results.items():
        if result and result.get('vulnerabilities', 0) > thresholds.get(key, {}).get('max_vulnerabilities', float('inf')):
            critical_issues_found = True

    # Output report
    print(report)

    # Exit with nonzero status if critical issues are found
    if critical_issues_found:
        sys.exit(1)

if __name__ == "__main__":
    main()