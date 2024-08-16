### AWS Audit script

This is a CI Pipeline that triggers python scripts to retrieve audit logs on different AWS Services.

Currently, the scripts are on the /aws-audits directory
/aws-audits
│
├── iam_audit.py
├── s3_audit.py
└── sg_audit.py

Created a GitHub Actions workflow that calls each script and runs it.

This live in the .github/workflows/ directory

The CI Workflow is called: aws_audit.yml

## Explanation of the Workflow

name: AWS Audits: This is the name of your GitHub Actions workflow.

on: Defines the triggers for this workflow.

This example runs the workflow on every push to the main branch, on pull requests, and on a daily schedule.

jobs: This defines the jobs that will be executed in your pipeline.

setup job:

Runs on the latest Ubuntu environment.

Checks out the code from your repository.

Sets up Python and installs boto3.

iam-audit, s3-audit, sg-audit jobs:

Each job runs a specific script.

The needs: setup directive ensures that these jobs only run after the setup job has completed.

steps: Each job consists of a series of steps, such as checking out the code, setting up Python, installing dependencies, and running the specific audit script.

## Storing AWS Credentials

To allow your scripts to interact with AWS, you need to store your AWS credentials securely in GitHub Actions. You can do this by setting up secrets in your repository:

Go to your repository on GitHub.
Navigate to Settings > Secrets and variables > Actions.
Add your AWS credentials as secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION

## Commit and Push

Finally, commit your changes and push them to the repository. GitHub Actions will automatically trigger the pipeline based on the conditions you’ve defined (e.g., on push, pull requests, or on schedule).

## Monitor the Workflow

You can monitor the execution of your workflow in the "Actions" tab of your repository. It will show you the status of each job and the output from running each script.

By following these steps, you’ve created a GitHub Actions pipeline that automatically runs your AWS audit scripts. This setup ensures that your scripts are executed consistently and can be easily maintained within your repository.

## Explanation of the Scripts

IAM Policy Audit (iam_audit.py):

Lists all IAM policies within your AWS account.
Fetches the default version of each policy and checks if it allows all actions ("Action": "\*") with an Allow effect.
If any such permissive policies are found, they are printed as potential risks.

S3 Bucket Permissions Audit (s3_audit.py):

Lists all S3 buckets in your account.
Checks the Access Control List (ACL) of each bucket to determine if the bucket is publicly accessible (i.e., has AllUsers in the ACL).
Publicly accessible buckets are printed as potential risks.

Security Group Audit (sg_audit.py):

Lists all security groups in your account.
Checks each security group’s inbound rules to see if any rules allow traffic from any IP address (0.0.0.0/0).
If any such rules are found, they are printed as potential security risks.

How to Run the Scripts in GitHub Actions

Once you add these scripts to your repository (in the aws-audits directory as defined earlier).
The GitHub Actions pipeline will automatically execute them as part of your CI/CD process.
The output from these scripts will be visible in the GitHub Actions logs, allowing you to review any identified security issues.
