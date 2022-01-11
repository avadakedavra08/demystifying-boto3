import boto3

# For Default session created using aws configure or default session created by boto3 for usage in the background
mng_console_var = boto3.session.Session()

# Checking list of users in an account using 'resource' concept
service_con_resource = mng_console_var.resource('iam')

'''
    All the method, objects that can be referred or called from any object can be determined by using 'dir'
    Here,
        dir(service_con_resource) -> Gives the list of all the variables and methods that can be referred by it
'''

# service_con_resource.users.all() -> can use groups instead of users
for each_user in service_con_resource.users.all():
    print(each_user)