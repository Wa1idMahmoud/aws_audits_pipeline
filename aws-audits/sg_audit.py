import boto3

def get_all_regions():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()['Regions']
    return [region['RegionName'] for region in regions]

def audit_security_groups():
    regions = get_all_regions()
    
    for region in regions:
        print(f"Auditing security groups in region: {region}")
        ec2 = boto3.client('ec2', region_name=region)
        security_groups = ec2.describe_security_groups()['SecurityGroups']
        
        for sg in security_groups:
            sg_name = sg['GroupName']
            sg_id = sg['GroupId']
            
            for permission in sg['IpPermissions']:
                if 'IpRanges' in permission:
                    for ip_range in permission['IpRanges']:
                        if ip_range['CidrIp'] == '0.0.0.0/0':
                            print(f"Security group {sg_name} ({sg_id}) in region {region} allows access from anywhere on port {permission.get('FromPort', 'All')}, which may pose a security risk.")

if __name__ == "__main__":
    audit_security_groups()
