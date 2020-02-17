import boto3
import json

# resource works with create, but client is required by internal things like list and upload. Not sure exactly how that relates
s3 = boto3.client('s3')

bname = 'freshnewbucky'

# Bucket is the method to name your bucket, other one is to bypass error 
response = s3.create_bucket(Bucket=bname)

policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:*",
        "Resource": "arn:aws:s3:::%s/*" % bname
    }]
}

bucket_policy = json.dumps(policy)

# assign above defined policies
s3.put_bucket_policy(
    Bucket=bname,
    Policy=bucket_policy
)

# activate versioning for bucket
s3.put_bucket_versioning(
    Bucket=bname,
    VersioningConfiguration= {
        'Status': 'Enabled'
    }
)

# list buckets (so far it lsits all details on the ones available)
print (s3.list_buckets())

# syntac for uploading files [from which file] [which bucket] [to file]
s3.upload_file('./files/bucket-cf.yaml', bname, 'bucket-cf.yaml')


# * remove after test *
file_up_resp = s3.upload_file('./files/test.txt', bname, 'test.txt')

f = open('./files/test.txt', 'a')
f.write('Good stuff')
f.close()

s3.upload_file('./files/test.txt', bname, 'test.txt')
# * remove after test *


print (f'https://{bname}.s3.amazonaws.com/bucket-cf.yaml')

