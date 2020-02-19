from sample.s3_bucket import S3_Check
import os

bname = 'freshnewbucky'

'''
goal:
    - for upload: allow the user to pick the file
    - for update: compate file in bucket to file in list and upload That file in list
'''

# check the files in the bucket
print ('Check files residing in bucket')
bucket_fname = S3_Check.file_check(bname)


# check what files you got avaiable
print ()
print ('Check files available for upload:')

upload_dir = os.path.dirname(os.path.abspath(__file__)) + '/files/'

dir_files = [f for f in os.listdir(upload_dir) if os.path.isfile(os.path.join(upload_dir, f))]
print (f'File list: {dir_files}')

for file_name in dir_files:
    local_fname = file_name
    print (f'Just the file: {local_fname}')


# check if thing is in files list and update
print ()
if bucket_fname in dir_files:
    print ('True')
else:
    print ('False')
