import boto3

client = boto3.client('cloudformation')

class CF_Delete:
    def delete_stack(stackname):
        print (f'Deleting stack {stackname}')

        response = client.delete_stack(
            StackName=stackname
        )

        # print (f'Stack deleted:\n{response}')

class CF_Create:
    def create_stack(stackname, bname, fname):
        print (f'Creating stack {stackname} from template in {bname}')
        
        response = client.create_stack(
            StackName=stackname,
            TemplateURL=f'https://{bname}.s3.amazonaws.com/{fname}'
        )

        # print (f'Stack created:\n{response}')

class CF_Update:
    def update_stack(stackname, bname, fname):
        print (f'Updating stack {stackname} from template in {bname}')
        
        response = client.update_stack(
            StackName=stackname,
            TemplateURL=f'https://{bname}.s3.amazonaws.com/{fname}'
        )

        # print (f'Stack updated:\n{response}')

class CF_State:
    def get_stack_state(stackname):
        # drop this at the end of the create, del and update scripts
        # with a timer of 20 or some seconds so it doesnt spam, but updates nicely
        # and have it up for a few minutes
        # OR *better idea* update it every time the state changes
        # 
        response = client.describe_stack_events(
            StackName=stackname
        )

        for stack_id in response['StackEvents']:
            print (f"Stack '{stack_id['StackName']}': {stack_id['ResourceStatus']}")
            return stack_id['ResourceStatus']
        # would be great if I can get the resources displayed as well
        '''
            if stack_id['ResourceProperties'] == str:
                print (f"{stack_id['ResourceProperties']}")
            else:
                continue
        '''
