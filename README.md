Transport Layer Network Protocol

<<<<<<< HEAD
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
=======
These two processes will exchange simple packets through the 
protocol. 

The contents of the packets your sender (client) and receiver
(server) sockets includes 4 values.
>>>>>>> master
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

Random numbers will be used to simulate random arrival time of packets. 

A second instance of the random number generator will be used to determine if packets that have just arrived
are corrupted. 

Inputs:
o The seed for the random number generator used for timing
o The number of packets to send
o The seed for the random number generator used for determining if ACKs or NACKs
have been corrupted.
o The probability that an ACK or NACK has been corrupted. Between [0 and 1)

If the packet is corrupt, the receiver sends a NACK. Otherwise, it sends an ACK.
If the sender receives a NACK or a corrupted response, the same packet is retransmitted.
