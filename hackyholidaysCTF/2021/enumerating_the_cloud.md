# Enumerating The cloud

## challenge information

The spaceship that you will use in SPACE RACE is almost ready. One of the last steps is to verify that all of the systems are operational. Unfortunately, the AI controlling the system information decided to take a personal time off for a few days, leaving you without an easy access to the spaceship systems. This is not a problem because, as the cyber security specialist in the ship, you know the spaceship cloud infrastructure like the back of your hand.

### flag 1

[25 points]
Spaceship external information endpoint

Your spaceship is located here, can you find the external information panel?
http://planet-bucket-43b2a07.s3-website-eu-west-1.amazonaws.com/

---

trying to get the listing for the bucket planet-bucket-43b2a07 directly we get access denied 


http://planet-bucket-43b2a07.s3.amazonaws.com/
```xml
<Error>
<Code>AccessDenied</Code>
<Message>Access Denied</Message>
<RequestId>BEHXGK6RTGM6CMWW</RequestId>
<HostId>
r02/ZX476f9JPu2euDBorTudyOYtXwYbDMmTrgDuSerLOehIfZ0gD08Oc4uUJKMrY0polYsRvKc=
</HostId>
</Error>
```

examining the source of the original webpage, wee see the rocket logo is loaded from a different bucket

https://rocket-bucket-723aa76.s3.amazonaws.com/rocket_bucket.png

viewing this bucket we see the listing is public!

```xml
<ListBucketResult>
<Name>rocket-bucket-723aa76</Name>
<Prefix/>
<Marker/>
<MaxKeys>1000</MaxKeys>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>external-information-panel.txt</Key>
<LastModified>2021-06-24T19:24:39.000Z</LastModified>
<ETag>"d18c834974b76e5e2a02d27b5f5f2a67"</ETag>
<Size>60</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
<Contents>
<Key>flag.txt</Key>
<LastModified>2021-06-24T19:24:39.000Z</LastModified>
<ETag>"ebfd1e6eb5d2bd7daf1facf9f81c2689"</ETag>
<Size>45</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
<Contents>
<Key>rocket_bucket.png</Key>
<LastModified>2021-06-24T19:24:38.000Z</LastModified>
<ETag>"2b6e9f2e40e4ba07e6530f4e8dff83bb"</ETag>
<Size>31428</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
</ListBucketResult>
```


flag 1: CTF{0841862f273fd2ca20ea3b94a645781071ab19d7}

### flag 2


[25 points]
Obtaining the spaceship access keys

You have gained access to the external infromation endpoint. Can you access the spaceship logs to obtain the access keys?

---

downloading external-information-panel.txt we see

https://g0341x75tb.execute-api.eu-west-1.amazonaws.com/logs

inspecting the page we see "405 Request method 'GET' not allowed"

how about other methods? I caught the request in Burp and send it to repeater, trying HEAD, POST and then striking gold with PUT

```
HTTP/1.1 200 OK
Date: Sat, 03 Jul 2021 15:10:12 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 7752
Connection: close
Apigw-Requestid: B5iZKhKmjoEEPmQ=

The periscope data is optimal. Have a flag for your effort: CTF{9177a9c8bb1cd5c85934}.<br>
[
    {
        "Id": "dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a",
        "Created": "2021-06-24T17:33:58.623969048Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 154123,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-06-24T17:33:59.110711065Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },

        ...
```

flag 2: CTF{9177a9c8bb1cd5c85934}
