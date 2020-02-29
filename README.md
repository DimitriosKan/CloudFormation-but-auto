# CloudFormation-but-auto
So this is a Python script that ideally deploys a CloudFormation template with one click ... Not Clickbait
_Note: CloudFormation deals with a select set of regions. If you are not in one of those, it will error._

## How to run:
#### If you want to change the name of the bucket (Advised to do so):  
Up top in the _**apply.py**_ and _**destroy.py**_ files
 
#### If you have your own template file:  
Drop it in the _**files**_ folder (It will be accessible on apply)
 
#### Initial setup - After manual fiddling with the namings, just run _**apply.py**_:  
Will be prompted to pick a file from the directory (you have your template in there)
  
#### To update:  
Just run _**apply.py**_ again after you have changed your template file.  
_Important: update the file you picked first, the script scans the bucket and updates  
the file that has the same name as the one uploaded._
  
#### To delete:  
Just run _**delete.py**_ ...


## So far we have ...

#### Behind the madness:
Everything is pretty straight forward, mostly in **_sample_** folder.  
The code is often commented quite in depth (for personal sake) so feel free to dive.  
If service is straight forward, it jsut is.

#### Spawn script (*s3_spawn.py*):
- Spawns bucket
- Sets up the versioning funct
- Puts file in bucket
- Then you can pick what file you wanna deal with
(Here comes adding that fancy CloudFormation stack)

#### Del script (*s3_del.py*):
- Finds bucket by name
- Runs through files, checking all versions available
- Does some magic to sort out what is Mared and unmarked
- Then deletes file versions and bucket

#### Convenient upload file script (*update.py*) :
- Run it to version a file (So far it's set up only for a txt file)
- It'll be fancy in pushing an update to CloudFormation
