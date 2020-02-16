import boto3

s3 = boto3.client('s3')

bname = 'freshnewbucky'

#s3.upload_file('bucket-cf.yaml', bname, 'bucket-cf.yaml')

s3.upload_file('test.txt', bname, 'test.txt')

print ('File has been uploaded')
