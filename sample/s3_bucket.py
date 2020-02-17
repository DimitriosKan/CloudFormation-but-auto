import boto3
import json

# resource works with create, but client is required by internal things like list and upload. Not sure exactly how that relates
s3 = boto3.resource('s3')
s3cli = boto3.client('s3')

class S3_Check:
    def check_bucket(bname):
        response  = s3cli.list_buckets()
        up_buckets = [bucket['Name'] for bucket in response ['Buckets']]

        # print (f'Buckets currently up: {up_buckets}')

        if bname in up_buckets:
            print ('Bucket located')
            return True
        else:
            print ('Bucket not found')
            return False

class S3_Delete:
    def delete_bucket(bname):
        # replaced with hard coded name so it doesn't demolish your infrastructure
        '''
        # fetch bucket name
        for bucket in s3.buckets.all():
            buck = bucket.name
            print (bucket.name)
        '''
        # check all things in bucket
        # works with multiple things in bucket 
        for file in s3.Bucket(bname).objects.all():
            fil = file.key
            print ()
            print (fil) 

            # check file versions
            version_resp = s3cli.list_object_versions(Bucket=bname)
            #print (f'List_obj_versions response: {version_resp}')

            # Below starts the decyphering of the response above
            # fetching what is avaialble for each item ...
            paginator = s3cli.get_paginator('list_object_versions')
            #print (f'paginator: {paginator}')
            response_iterator = paginator.paginate(Bucket=bname)
            #print (response_iterator)

            # this acts like a botocli call that gets
            # the full list of items 
            for response in response_iterator:
                #print ()
                #print (f'Full response: {response}')

                # just get the items and their actual properties
                # excluding the marked ones
                versions = response.get('Versions', [])
                #print ()
                #print (f'All items (- marked): {versions}')
                
                # think this adds the DeleteMarkers as a parameter/filter
                # and returnes all items plus the marked ones
                versions.extend(response.get('DeleteMarkers', []))
                #print ()
                #print (f'All items (+ marked): {versions}')
                
                # the delete marker tagged files (youll see them pop up)
                # if there's any
                marked = response.get('DeleteMarkers', [])
                #print ()
                #print (f'Get only marked: {marked}')

                
                # all this madness is because sometimes files are assigned
                # a null value as their ID
                # Not sure if it will work, but it might
                z = True
                while z is True:
                    things = []
                    for x in versions:
                        print (x['VersionId'])
                        things.append(x['VersionId'])
                    z = False

                # then we run through individual items
                for x in versions:
                    if len(things) > 1:
                        # filter them by below requirements
                        if x['Key'] == fil and x['VersionId'] != 'null':
                            # get the id string ...
                            version_id = x['VersionId']
                            print (f'Deleting {fil} version {version_id} ...')
                            # and delete them 
                            s3cli.delete_object(Bucket=bname, Key=fil, VersionId=version_id)
                    elif len(things) == 1:
                        # filter them by below requirements
                        if x['Key'] == fil and x['VersionId']:
                            # get the id string ...
                            version_id = x['VersionId']
                            print (f'Deleting {fil} version {version_id} ...')
                            # and delete them
                            s3cli.delete_object(Bucket=bname, Key=fil, VersionId=version_id)

        print ()
        print (f'Deleting bucket {bname} ...')

        # now this deletes the bucket
        s3cli.delete_bucket(Bucket=bname)

class S3_Create:
    def create_bucket(bname):
        print (f'Bucket {bname} is being created ...')

        # Bucket is the method to name your bucket, other one is to bypass error 
        response = s3cli.create_bucket(Bucket=bname)

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
        s3cli.put_bucket_policy(
            Bucket=bname,
            Policy=bucket_policy
        )

        # activate versioning for bucket
        s3cli.put_bucket_versioning(
            Bucket=bname,
            VersioningConfiguration= {
                'Status': 'Enabled'
            }
        )

        print ('Uploading template file ...')
        # syntac for uploading files [from which file] [which bucket] [to file]
        s3cli.upload_file('./files/bucket-cf.yaml', bname, 'bucket-cf.yaml')

        print ('Bucket URI (for manual CF use):')
        print (f'https://{bname}.s3.amazonaws.com/bucket-cf.yaml')

class S3_Update:
    def update_files(bname):
        print ('Updating files ...')

        s3cli.upload_file('./files/bucket-cf.yaml', bname, 'bucket-cf.yaml')
