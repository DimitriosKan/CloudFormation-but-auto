from sample.s3_bucket import S3_Delete
from sample.cloud_formation import CF_Delete, CF_State
import time
from botocore.exceptions import ClientError

bname = 'freshnewbucky'
stackname = 'newstack'

def check_state():
    x = CF_State.get_stack_state(stackname)

    # this thing is the logical ID to check
    # when the id and stackname match
    thing = x['LogicalResourceId']

    # creating a nice dictionary to bundle
    # state and stack name together
    stack_state = {}
    stack_state[x['StackName']] = x['ResourceStatus']

    return stack_state, thing

def destroy_bucket():
    S3_Delete.delete_bucket(bname)
    print (f'Bucket {bname} deleted !')

def destroy_cloudformation():
    CF_Delete.delete_stack(stackname)
    print (f'Stack {stackname} deleted !')

if __name__ == "__main__":
    print ()
    destroy_bucket()
    print ()
    destroy_cloudformation()

    print ()

    print ('Stack deployment status ...')

    # First element is the dictionary with stackname (static) and state (dynamic)
    # Second element is the current LogicalID (dynamic)
    stack_state = check_state()
    # print (f'Stack/State: {stack_state[0]}')
    # print (f'Logical: {stack_state[1]}')

    # what we getting at here is:
    # while first key is stackname, check again ...
    while list(stack_state[0].keys())[0] == stackname:
        time.sleep(5)
        #print (list(stack_state[0].keys())[0])
        #print (stack_state[1])
        # check if check_state() runs
        # if it does, continue with loop
        try:
            stack_state = check_state()
        # if exception (aka stack has been deleted)
        # print and break
        except ClientError as e:
            #print (e)
            print (f'Stack {stackname}: DELETE_COMPLETE')
            print ()
            print(f"{stackname} has been deleted !")
            break
