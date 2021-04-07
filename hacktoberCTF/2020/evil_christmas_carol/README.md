### Evil Christmas Carol

after extracting the file I knew to look for a .dll, so I analysed in tcpdump and greped for the line with .dll

`tcpdump -ttttnr HolyNight.pcap | grep .dll`

reading from file HolyNight.pcap, link-type EN10MB (Ethernet)
2020-07-25 00:48:16.973500 IP 10.0.0.163.49686 > 205.185.125.104.80: Flags [P.], seq 222:701, ack 786, win 65535, length 479: HTTP: GET /files/july22.dll HTTP/1.1

the flag is the ip address of the sender

flag{205.185.125.104}