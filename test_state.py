from sample.cloud_formation import CF_State
import time

stackname = 'newstack'

# put this bad boy in the delete and apply scripts,
# so we exit after everything has been setup/deleted

def check_state():
    x = CF_State.get_stack_state(stackname)
    
    stack_state = {}
    stack_state[x[0]] = x[1]

    return stack_state

if __name__ == "__main__":
    stack_state = check_state()
    
    # what we getting at here is:
    # while first key is stackname and it's value is Not CREATE_COMPLETE
    while list(stack_state.keys())[0] == stackname and stack_state[stackname] != 'CREATE_COMPLETE':
        # if it becomes 'CREATE_COMPLETE' print and break
        time.sleep(5)
        stack_state = check_state()
        if stack_state[stackname] == 'CREATE_COMPLETE':
            check_state()
            break

    print ('Stack has been ... !')
