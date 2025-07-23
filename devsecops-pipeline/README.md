# Automated DevSecOps Pipeline Security MVP

## Overview
The Automated DevSecOps Pipeline Security project aims to integrate security scanning into the CI/CD pipeline, ensuring that code is continuously monitored for vulnerabilities and compliance issues. This project implements various scanning modules for static application security testing (SAST), dependency checks, container security, infrastructure-as-code (IaC) analysis, and secret detection.

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/devsecops-pipeline.git
   cd devsecops-pipeline
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the project:**
   - Update `src/config/config.json` with your Slack webhook URL and security thresholds.
   - Modify `src/config/thresholds.json` to set the maximum allowed vulnerabilities for different scans.

## MVP Success Criteria
- Successful integration of all scanning modules.
- Generation of a comprehensive report summarizing scan results.
- Notifications sent to Slack for critical issues detected during scans.
- CI pipeline defined and operational, triggering scans on code changes.

## Usage
To run the orchestrator script and execute all scans, use the following command:
```bash
python src/orchestrator.py
```

This will run all configured scans and generate a report based on the results.