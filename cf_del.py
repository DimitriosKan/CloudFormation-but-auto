import boto3

client = boto3.client('cloudformation')

response = client.delete_stack(
    StackName='freshstack'
)

print (f'Stack deleted:\n{response}')
