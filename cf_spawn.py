# can probs just drop the cf and file update modules here
# checking if the bucket exists ...
# - if it does: update files and then run update script
# - if it doesn't: create the bucket and run the boto script

# do these in a modular format ... independant and all

import boto3

client = boto3.client('cloudformation')

response = client.create_stack(
    StackName='freshstack',
    TemplateURL='https://freshnewbucky.s3.amazonaws.com/bucket-cf.yaml'
)

print (f'Stack created:\n{response}')
