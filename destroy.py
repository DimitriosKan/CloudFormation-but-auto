from sample.s3_bucket import S3_Delete
from sample.cloud_formation import CF_Delete, CF_State
import time

bname = 'freshnewbucky'
stackname = 'newstack'

def check_state():
    x = CF_State.get_stack_state(stackname)
    
    stack_state = {}
    stack_state[x[0]] = x[1]

    return stack_state

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

    stack_state = check_state()

    # what we getting at here is:
    # while first key is stackname and it's value is Not DELETE_COMPLETE
    while list(stack_state.keys())[0] == stackname and stack_state[stackname] != 'DELETE_COMPLETE':
        # if it becomes 'DELETE_COMPLETE' print and break
        time.sleep(5)
        stack_state = check_state()
        if stack_state[stackname] == 'DELETE_COMPLETE':
            check_state()
            print ('Stack has been deleted !')
            break
        else:
            print ('Probably deleted ...')
   
