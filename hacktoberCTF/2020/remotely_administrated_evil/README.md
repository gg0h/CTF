### Remotely Administrated Evil

after extracting pcap from archive

run `tcpdump -ttttnr RATPack.pcap | grep .exe` bash

```
reading from file RATPack.pcap, link-type EN10MB (Ethernet)
2020-07-24 21:51:14.820854 IP 172.16.1.219.53227 > 45.40.135.135.80: Flags [P.], seq 1:72, ack 1, win 64240, length 71: HTTP: GET /ot/solut.exe HTTP/1.1
```

flag{solut.exe}