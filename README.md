Transport Layer Network Protocol
Date: Summer 2018  

Authors:  
Greyson Wang  
Anthony Tran  
Jonathon Mo

These two processes will exchange simple packets through the 
protocol. 

The contents of the packets the sender (client) and receiver
(server) sockets includes 4 values.

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
