def generate_report(scan_results):
    """
    Generates a Markdown report from the provided scan results.

    Args:
        scan_results (dict): A dictionary containing the results of various scans.

    Returns:
        str: A Markdown formatted report.
    """
    report_lines = []

    report_lines.append("# Automated DevSecOps Pipeline Security Report\n")
    report_lines.append("## Summary\n")
    report_lines.append(f"Total Scans: {len(scan_results)}\n")

    for module, results in scan_results.items():
        report_lines.append(f"### {module.capitalize()} Results\n")
        if results.get("critical_issues"):
            report_lines.append("**Critical Issues Found:**\n")
            for issue in results["critical_issues"]:
                report_lines.append(f"- {issue}\n")
        else:
            report_lines.append("**No Critical Issues Found.**\n")
        
        report_lines.append("\n")

    return "\n".join(report_lines)

def check_for_critical_issues(scan_results):
    """
    Checks if there are any critical issues in the scan results.

    Args:
        scan_results (dict): A dictionary containing the results of various scans.

    Returns:
        bool: True if critical issues are found, False otherwise.
    """
    for results in scan_results.values():
        if results.get("critical_issues"):
            return True
    return False