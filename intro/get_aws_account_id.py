import boto3
import pprint

# Fetching Account level details using AWS STS
mgmt_console = boto3.session.Session()
sts_service_cli = mgmt_console.client(service_name='sts',region_name='us-east-1')

# Using STS client to get the required account details
# STS -> Security Service Token
pprint.pprint(sts_service_cli.get_caller_identity())

