# CloudFormation-but-auto
So this is a Python script that ideally deploys a CloudFormation template with one click ... Not Clickbait

## So far we have ...

#### Spawn script (*s3_spawn.py*):
- Spawns bucket
- Sets up the versioning funct
- Puts file in bucket
- ... TBC
(Here comes adding that fancy CloudFormation stack)

#### Del script (*s3_del.py*):
- Finds bucket by name
- Runs through files, checking all versions available
- Does some magic to sort out what is Mared and unmarked
- Then deletes file versions and bucket
