from sample.s3_bucket import S3_Create, S3_Update, S3_Check
from sample.cloud_formation import CF_Create, CF_Update

bname = 'freshnewbucky'
stackname = 'newstack'

def do_check():
    return S3_Check.check_bucket(bname)

def create_bucket():
    S3_Create.create_bucket(bname)
    print (f'{bname} created !')

def create_cloudformation():
    CF_Create.create_stack(stackname, bname)
    print (f'Stack {stackname} created !')

def update_bucket():
    S3_Update.update_files(bname)
    print (f'Files updated to {bname} !')

def update_stack():
    CF_Update.update_stack(stackname, bname)
    print (f'Stack {stackname} updated !')

if __name__ == "__main__":
    x = do_check()
    if x is True:
        print ()
        update_bucket()
        print ()
        update_stack()
    elif x is False:
        print ()
        create_bucket()
        print ()
        create_cloudformation()
    else:
        print ('Well ... This is an exception')

