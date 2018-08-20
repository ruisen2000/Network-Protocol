Network Protocol

Authors:
Greyson Wang
Anthony Tran
Jonathon Mo

These two processes will exchange simple packets that are used to implement the
protocol. Please note that the form of the packets has been changed from the example in
your textbook. This means that the arguments of the makepkt function in the figures must
be changed to a list of the variables in the fields of the packets described below. The
arguments of makepkt should be in the order Field1, Field2, Field3, Field4.
Your programs must run on the Linux machines in the CSIL labs. If your programs do not run
in the Linux environment in CSIL you will receive a 0 for this problem. Beware socket
programs are often not easily portable between operating systems.
The contents of the simple packets you send between your sender (client) and receiver
(server) sockets will include 4 values.
• Field 1: Packet contents: a 32 bit integer.
The integer cannot be assumed to follow any pattern
Packet contents for an ACK or NACK packets is 0
• Field 2: Sequence Number: a Boolean
Value is True if sequence number is 1
Value is False if sequence number is 0
• Field 3: Is this an ACK? Boolean
True if the packet is an ACK, False if the packet is not an ACK
• Field 4: Is this a NACK? Boolean
True if the packet is a NACK, False if the packet is not a NACK
For ACK and NACK packets the values in Field1 should be 0
In your sender program you will
• Use one instance of a pseudo random number generator random( ) to produce uniformly
distributed random floating point numbers in the range [0.0, 5.0). These pseudo random
numbers will be used to simulate random arrival time of packets. When a packet is sent,
the send is followed immediately by a call to this random number generator. The pseudo
random number returned will be interpreted as the delay in seconds before the next
packet will be generated.
As discussed in class: before sending the first packet you should find the current time
(use time.time() to get a number of ticks, 1 tick = 1 second). The expected arrival time is
set to the current time. Next send the first packet.
After sending a packet use the random number generator to get a random time between
1 and 5 seconds (round the random number up to the nearest integer). Add the random
time to the expected arrival time, you now have the expected arrival time of the data for
the next packet. When you want to generate the next packet you will check the time 
again using time.time() and see if the value is smaller than the expected arrival time, if it
is you need to wait until the time reaches the expected arrival time before you send the
packet, otherwise you can send the packet immediately.
• Use a second instance of a pseudo random number generator random() to generate
random number that will be used to determine if an ACK and NACK that has just arrived
has been corrupted. This instance of the pseudo random number generator random
should generate uniformly distributed pseudo random numbers between [0.0 and 1.0).
If the number generated is less that the input value of the probability that an ACK or NACK
packet has been be corrupted, then the ACK or NACK packet that has just arrived will be
considered to be corrupted.
• Read the values of the following quantities used in your program at the start of your
program. You will not read any quantities not in this list into your program. You will read
the specified quantities in the order they are specified below.
o The seed for the random number generator used for timing
o The number of packets to send
o The seed for the random number generator used for determining if ACKs or NACKs
have been corrupted.
o The probability that an ACK or NACK has been corrupted. Between [0 and 1)
• Print the following messages immediately before a packet is sent.
o One of the first four messages should be sent followed by the fifth message.
o You must print the messages exactly as given, with the sole exception of items in
bold which will contain actual data values.
 A packet with sequence number 0 is about to be sent
 A packet with sequence number 1 is about to be sent
 A packet with sequence number 0 is about to be resent
 A packet with sequence number 1 is about to be resent
 Packet to send contains: data = 123 seq = 0 ack = 0 nack = 0
• Print the following messages immediately after an uncorrupted ACK or NACK packet is
received.
o Either an ACK or a NACK will be received. Print the message for the packet received
followed by the third message.
o You must print the messages exactly as given below, with the sole exception of
items in bold which will contain actual data values.
 An ACK packet has just been received
 A NACK packet has just been received
 Packet received contains: data = 0 seq = 1 ack = 0 nack = 1
• Print the following message immediately after a corrupted packet is received.
o You must print the message exactly as given below.
 A Corrupted ACK or NACK packet has just been received
• Print the following messages immediately before the sender moves to another state or
returns to the same state.
o Only the appropriate one of the following messages should be printed for each
transition. 
o These messages must be printed exactly as given below.
 The sender is moving to state WAIT FOR CALL 0 FROM ABOVE
 The sender is moving to state WAIT FOR CALL 1 FROM ABOVE
 The sender is moving back to state WAIT FOR CALL 0 FROM ABOVE
 The sender is moving back to state WAIT FOR CALL 1 FROM ABOVE
 The sender is moving to state WAIT FOR ACK OR NACK
 The sender is moving back to state WAIT FOR ACK OR NACK
 In your receiver program you will
• Use an instance of a pseudo random number generator random() to generate uniformly
distributed pseudo random numbers between [0.0 and 1.0). These pseudo random
numbers will be used to determine if a packet that has just arrived has been corrupted.
If the pseudo random number generated is less that the input value of the probability that
the packet has been be corrupted, then the packet that has just arrived will be considered
to be corrupted.
• Read the values of the following quantities used in your program at the start of your
program. You will not read any quantities not in this list into your program. You will read
the specified quantities in the order they are specified below.
o The seed for the random number generator used for determining if ACKs or NACKs
have been corrupted.
o The probability that an ACK or NACK has been corrupted
• Print the following messages immediately before an ACK or NACK is sent.
o One of the first two messages should be sent followed by the third message.
o You must print the messages exactly as given, with the sole exception of items in
bold which will contain actual data values.
 An ACK is about to be sent
 A NACK is about to be sent
 Packet to send contains: data = 0 seq = 0 ack = 1 nack = 0
• Print the following messages immediately after an uncorrupted packet is received.
o One of the first four messages should be sent followed by the fifth message,
including the actual contents of the packet just received
o You must print the messages exactly as given, with the sole exception of items in
bold which will contain actual data values.
 A packet with sequence number 0 has been received
 A packet with sequence number 1 has been received
 A duplicate packet with sequence number 0 has been received
 A duplicate packet with sequence number 1 has been received
 Packet received contains: data 333 seq = 1 ack = 0 nack = 1
• Print the following message immediately after a corrupted packet is received.
You must print the message exactly as given. 
 A Corrupted packet has just been received
• Print the following messages Immediately before the sender moves to another state or
returns to the same state
o the appropriate one of the following messages should be printed
 The receiver is moving back to state WAIT FOR 0 FROM BELOW
 The receiver is moving back to state WAIT FOR 1 FROM BELOW
 The receiver is moving to state WAIT FOR 0 FROM BELOW
 The receiver is moving to state WAIT FOR 1 FROM BELOW 