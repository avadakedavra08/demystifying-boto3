import boto3

# default session
aws_mng_con = boto3.session.Session()

# Creating iam, ec2, s3
iam_con_cli = aws_mng_con.client(service_name='iam',region_name='us-east-1')

ec2_con_cli = aws_mng_con.client(service_name='ec2',region_name='us-east-1')

s3_con_cli = aws_mng_con.client(service_name='s3',region_name='us-east-1')

# List all iam users using client object
listing_users = iam_con_cli.list_users()
# First level operation is object level, rest of it referencing as dictionary is returned

# List of User and other relevant information in the form of dictionary
print(listing_users)

# Printing each user data separately
for i in listing_users['Users']:
    print(i)

print("---------------------------------------------------------")

# Listing ec2 instances
listing_ec2_instances = ec2_con_cli.describe_instances()
print(listing_ec2_instances)

# Fetching instances ID's
for i in listing_ec2_instances['Reservations']:
    # To get the instances check through documentation for valid keys required
    print(i)

# Go through documentation for fetching information related to S3 related API's
# For resource service, check "Service Request" tab for resource object services
