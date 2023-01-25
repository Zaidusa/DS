import boto3
import pandas as pd
class access:

    def acc(self):
        s3 = boto3.resource(
            service_name='s3',
            region_name='us-east-2',
            aws_access_key_id='AKIAZFFZXIGGP4CZAQ7C',
            aws_secret_access_key='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'
        )

        # Print out bucket names
        for bucket in s3.buckets.all():
            bucketname=bucket.name
        a=bucketname
        print(a)
        path=f's3://{a}/Testdata.csv'
        print(path)
        df3=pd.read_csv(path)
        print(df3)
a=access()
a.acc()
