### Wireshark two two two

Can you find the flag? shark2.pcapng.

There are a lot of decoy flags in the capture, alluded to by __red__ shrimpand __herring__.com

eventually I noticed alot of this domain was prepended by strange strings, like

ZnR3X2Rl.reddshrimpandherring.com: type A, class IN

I remembered here of a C2 technique to exfiltrate data with encoded strings this way

I noticed that with DNS packets between 192.168.38.104 and 18.217.1.57, the strings actually decoded int b64

adding these together and decoding b64

cGljb0NuRntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==

picoCnF{dns_3xf1l_ftw_deadbeef}

I made a typo somewhere, oh well

picoCTF{dns_3xf1l_ftw_deadbeef}
