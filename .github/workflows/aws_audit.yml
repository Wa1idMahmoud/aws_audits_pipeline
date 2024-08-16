name: AWS Audits

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: "0 11 * * *"  # Runs daily at noon UK time

jobs:
  setup:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      # Set up Python 3.x environment
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      # Install boto3 using pip
      - name: Install boto3
        run: |
          python3 -m pip install --upgrade pip  # Upgrade pip to the latest version
          python3 -m pip install boto3          # Install boto3
          python3 -m pip show boto3             # Verify boto3 installation

      # Configure AWS credentials from GitHub secrets
      - name: Configure AWS credentials
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}
        run: |
          aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
          aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
          aws configure set default.region $AWS_DEFAULT_REGION

  iam-audit:
    runs-on: ubuntu-latest
    needs: setup

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      # Run the IAM audit script using the Python environment where boto3 is installed
      - name: Run IAM audit
        run: |
          python3 /home/runner/work/aws_audits_pipeline/aws_audits_pipeline/aws-audits/iam_audit.py

  s3-audit:
    runs-on: ubuntu-latest
    needs: setup

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      # Run the S3 audit script using the Python environment where boto3 is installed
      - name: Run S3 audit
        run: |
          python3 /home/runner/work/aws_audits_pipeline/aws_audits_pipeline/aws-audits/s3_audit.py

  sg-audit:
    runs-on: ubuntu-latest
    needs: setup

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      # Run the Security Group audit script using the Python environment where boto3 is installed
      - name: Run Security Group audit across all regions
        run: |
          python3 /home/runner/work/aws_audits_pipeline/aws_audits_pipeline/aws-audits/sg_audit.py
