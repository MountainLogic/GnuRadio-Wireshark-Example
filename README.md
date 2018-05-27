# GnuRadio-Wireshark-Example
Simple example to show how to capture ZigBee/IEEE 802.15.4 and send it to WireShark wpan using RFtap under GnuRadio

In wireshark udp setup use rftap lower case Listen port must match GNU rfTAP, but sometimes (under OSX at least) Wireshark leaves the socket open when it crashes and you have to either reboot or move to another socket number in BOTH gnu and shark.
Wireshark sometimes fails to close a socket (??) when closing so you have to inc the socket number in both GnuRadio and Wireshark or reboot - may no tbe an issue under different non-OSX - YMMV.

From wireshark startview (config dialog): Wireshark  - Interface Options:UDP Listener UDP remore capture:udpdump
  Listen Port should match what is in GmuRadio:Socket PDU Port number, such as 52006
  Payload Type: rftap

In GnuRadio/RFtap Encapulation use:
Type=Custom dissector, Data Link Type = -1, Disector=wpan   NOTE lower case wpan is the id of IEEE 802.15.4
