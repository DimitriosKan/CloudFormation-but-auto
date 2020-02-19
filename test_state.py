from sample.cloud_formation import CF_State
import time

stackname = 'newstack'

# put this bad boy in the delete and apply scripts,
# so we exit after everything has been setup/deleted

def check_state():
    x = CF_State.get_stack_state(stackname)
    return x

if __name__ == "__main__":
    x = check_state()
    # add a check if the stack itself has been marked complete
    # while x (where you should have both stackid and state returned)
    while x != 'CREATE_COMPLETE':
        time.sleep(5)
        x = check_state()
        # if stackid == 'stack id' and state == create_complete
        if x == 'CREATE_COMPLETE':
            print ('waiting ...')
            time.sleep(10)
            check_state()

    # or
    # list of the status values being updated on change
