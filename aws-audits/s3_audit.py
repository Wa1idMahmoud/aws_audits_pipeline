import boto3

def audit_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    
    for bucket in buckets:
        bucket_name = bucket['Name']
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        
        for grant in acl['Grants']:
            if grant['Grantee']['Type'] == 'Group' and 'AllUsers' in grant['Grantee']['URI']:
                print(f"Bucket {bucket_name} is publicly accessible, which may pose a security risk.")

if __name__ == "__main__":
    audit_s3_buckets()
