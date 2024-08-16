import boto3

def audit_security_groups():
    ec2 = boto3.client('ec2')
    security_groups = ec2.describe_security_groups()['SecurityGroups']
    
    for sg in security_groups:
        sg_name = sg['GroupName']
        sg_id = sg['GroupId']
        
        for permission in sg['IpPermissions']:
            if 'IpRanges' in permission:
                for ip_range in permission['IpRanges']:
                    if ip_range['CidrIp'] == '0.0.0.0/0':
                        print(f"Security group {sg_name} ({sg_id}) allows access from anywhere on port {permission.get('FromPort', 'All')}, which may pose a security risk.")

if __name__ == "__main__":
    audit_security_groups()
