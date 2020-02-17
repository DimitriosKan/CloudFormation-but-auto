# drop this at the end of the create, del and update scripts
# with a timer of 20 or some seconds so it doesnt spam, but updates nicely
# and have it up for a few minutes
# OR *better idea* update it every time the state changes
# 

import boto3

client = boto3.client ('cloudformation')

response = client.describe_stack_events(
    StackName='freshstack'
)

for stack_id in response['StackEvents']:
    print (f"Stack '{stack_id['StackName']}': {stack_id['ResourceStatus']}")

# would be great if I can get the resources displayed
'''
    if stack_id['ResourceProperties'] == str:
        print (f"{stack_id['ResourceProperties']}")
    else:
        continue
'''
