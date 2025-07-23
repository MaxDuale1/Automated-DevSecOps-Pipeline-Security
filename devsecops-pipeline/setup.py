from setuptools import setup, find_packages

setup(
    name='devsecops-pipeline',
    version='0.1.0',
    description='Automated DevSecOps Pipeline Security MVP',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'bandit==1.7.0',
        'semgrep==0.70.0',
        'safety==1.10.3',
        'trivy==0.20.0',
        'checkov==2.0.0',
        'detect-secrets==1.0.3',
        'slack-sdk==3.19.0',
    ],
    python_requires='>=3.9',
)