

def audit_iam_policies():
    iam = boto3.client('iam')
    policies = iam.list_policies(Scope='Local')['Policies']
    
    for policy in policies:
        policy_name = policy['PolicyName']
        policy_arn = policy['Arn']
        policy_version = iam.get_policy_version(
            PolicyArn=policy_arn,
            VersionId=policy['DefaultVersionId']
        )
        statements = policy_version['PolicyVersion']['Document']['Statement']
        
        for statement in statements:
            if statement['Effect'] == 'Allow' and statement['Action'] == '*':
                print(f"Policy {policy_name} allows all actions, which may be overly permissive.")

if __name__ == "__main__":
    audit_iam_policies()
