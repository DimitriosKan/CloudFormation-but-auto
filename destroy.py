from sample.s3_bucket import S3_Delete
from sample.cloud_formation import CF_Delete

bname = 'freshnewbucky'
stackname = 'newstack'

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
