# GnuRadio-Wireshark-Example
Simple example to show how to capture ZigBee/IEEE 802.15.4 and send it to WireShark wpan using RFtap under GnuRadio.

This lacks an install, but nce you have RFtap and other need dependencies installed all you really need is the .GRC file.  GR should build all the python from just the .GRC.  See https://rftap.github.io/ for installing RFtap.

It works amazingly well for such a simple implimentation. Using a basic dipole I have to crank up the rf/if gain and turn town the BB gain, but once you get it dialed in the packets com in like magic. In Wireshark it is easy to add a packet dissector to parse the payload data or use the built-in ZigBee example. I have this working on a Mac/OSX. My next step will be to move this to the Lime/GnuRadio driver.

In wireshark udp setup use rftap (lower case) Listen udp:port must match GNU rfTAP, but sometimes (under OSX at least) Wireshark leaves the socket open when it crashes and you have to either reboot or move to another socket number in BOTH gnu and shark.
Wireshark sometimes fails to close a socket (??) when closing so you have to inc the socket number in both GnuRadio and Wireshark or reboot - may not be an issue under different non-OSX - YMMV.

From wireshark startview (config dialog): Wireshark  - Interface Options:UDP Listener UDP remore capture:udpdump
  Listen Port should match what is in GmuRadio:Socket PDU Port number, such as 52006
  Payload Type: rftap

In GnuRadio/RFtap Encapulation use:
Type=Custom dissector, Data Link Type = -1, Disector=wpan   NOTE lower case wpan is the id of IEEE 802.15.4  <b>N.B. this is different from the RFtap example as Data Link Type 195 did not work for me</b> 

Example uses Lime SDR as the source, but other SDRs in the 2.4 GHz band should work.  (Sorry the $10 euro DTV dongles will not reach up to this freq).

This is mostly based on the very good example at https://rftap.github.io/blog/2016/09/04/rftap-zigbee.html, https://github.com/rftap/gr-rftap/tree/master/examples and http://www.ccs-labs.org/bib/bloessl2013gnu/bloessl2013gnu.pdf. My initial commit of the LQI EPY block is all their code.  The demod component is described at https://static1.squarespace.com/static/543ae9afe4b0c3b808d72acd/t/55dcd9a0e4b0eeb6c002b24f/1440536992248/8.+wunsch_felix-IEEE_802.15.4+2015-08-25.pdf.  I hope to expand it to be more Lime SDR driver centric in the future.  Thank you RFtap and GR-IEEE_802.15.4 teams. 

Please contact me with questions or enter an issue  -scott.
