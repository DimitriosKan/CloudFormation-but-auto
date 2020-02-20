from sample.s3_bucket import S3_Create, S3_Update, S3_Check
from sample.cloud_formation import CF_Create, CF_Update, CF_State
import os, time

bname = 'freshnewbucky'
stackname = 'newstack'

# check the files in the bucket
def check_bucket_file():
    bucket_fname = S3_Check.file_check(bname)
    return bucket_fname

# check what files you got avaiable locally
def check_local_file():
    upload_dir = os.path.dirname(os.path.abspath(__file__)) + '/files/'

    dir_files = [f for f in os.listdir(upload_dir) if os.path.isfile(os.path.join(upload_dir, f))]
    # print (f'File list: {dir_files}')

    return dir_files

def pick_file():
    no = 1
    dic = {}

    print ('File list: ')

    for file_name in check_local_file():
        local_fname = file_name
        print (f'[{no}]: {local_fname}')
        dic[no] = local_fname
        #print (dic)
        no += 1

    pick = int(input('Which file do you wanna upload?: '))

    for key, value in dic.items():
        if pick == key:
            fname = value
            print (fname)
            return fname

def do_check():
    return S3_Check.check_bucket(bname)

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

def create_bucket(fname):
    S3_Create.create_bucket(bname, fname)
    print (f'{bname} created !')

def create_cloudformation():
    CF_Create.create_stack(stackname, bname, fname)
    print (f'Stack {stackname} created !')

def update_bucket():
    S3_Update.update_files(bname, bucket_fname)
    print (f'Files updated to {bname} !')

def update_stack():
    CF_Update.update_stack(stackname, bname, bucket_fname)
    print (f'Stack {stackname} updated !')

if __name__ == "__main__":
    x = do_check()
    print ()

    if x is True:
        bucket_fname = check_bucket_file()
        dir_files = check_local_file()

        if bucket_fname in dir_files:
            # and file is same
            print ()
            update_bucket()
            print ()
            update_stack()
    elif x is False:
        fname = pick_file()

        print ()
        create_bucket(fname)
        
        bucket_fname = check_bucket_file()
        dir_files = check_local_file()

        if bucket_fname in dir_files:
            print ()
            create_cloudformation()
    else:
        print ('Well ... This is an exception')

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
        stack_state = check_state()
        # if the logical id matches the stackname and stack state becomes 'CREATE_COMPLETE'
        # print and break
        if stack_state[1] == stackname and stack_state[0][stackname] == 'CREATE_COMPLETE':
            print ('Stack has been created !')
            break
