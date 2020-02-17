import boto3

client = boto3.client('cloudformation')

response = client.update_stack(
    StackName='freshstack',
    TemplateURL='https://freshnewbucky.s3.amazonaws.com/bucket-cf.yaml'
)

print (f'Stack updated:\n{response}')
