from sample.s3_bucket import S3_Check

bname = 'freshnewbucky'

def do_check():
    return S3_Check.check_bucket(bname)

if __name__ == "__main__":
    x = do_check()
    if x is True:
        print (x)
    elif x is False:
        print (x)
    else:
        print ('Well ... This is an exception')
