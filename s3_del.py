import boto3

s3 = boto3.resource('s3')
s3cli = boto3.client('s3')

# replaced with hard coded name so it doesn't demolish your infrastructure
'''
# fetch bucket name
for bucket in s3.buckets.all():
    buck = bucket.name
    print (bucket.name)
'''
buck = 'freshnewbucky'

# check all things in bucket
# works with multiple things in bucket 
for file in s3.Bucket(buck).objects.all():
    fil = file.key
    print ()
    print (fil) 

    # check file versions
    version_resp = s3cli.list_object_versions(Bucket=buck)
    #print (f'List_obj_versions response: {version_resp}')

    # Below starts the decyphering of the response above
    # fetching what is avaialble for each item ...
    paginator = s3cli.get_paginator('list_object_versions')
    #print (f'paginator: {paginator}')
    response_iterator = paginator.paginate(Bucket=buck)
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

        # then we run through individual items
        for x in versions:
            # filter them by below requirements
            if x['Key'] == fil and x['VersionId'] != 'null':
                # get the id string ...
                version_id = x['VersionId']
                print (f'Deleting {fil} version {version_id}')
                # and delete them 
                s3cli.delete_object(Bucket=buck, Key=fil, VersionId=version_id)

# this removes All items inside bucket, not bucket itself
#s3.Bucket(buck).objects.all().delete()

# now this deletes the bucket
s3cli.delete_bucket(Bucket=buck)
