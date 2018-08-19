import re
import random
from socket import *
import sys
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
# logging.getLogger().setLevel(logging.DEBUG)


def build_packet(field1, field2, field3, field4):
    return "data = {}  seq = {}  ack = {}  nack = {}".format(field1, field2, field3, field4)


def main():
    server_host = ''
    server_port = 50007
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print('The server is ready to receive ')

    try:
        seed_corruption = int(sys.argv[1])
        prob_corruption = float(sys.argv[2])
    except IndexError:
        print("Please provide assignment arguments when starting up the script.")
        return

    while True:
        random.seed(seed_corruption)
        prev_seq = -1
        packet_seq = 0
        seq = 0
        connection_id, addr = server_socket.accept()
        is_corrupt = False
        while True:
            # connection_id, addr = server_socket.accept()
            packet = connection_id.recv(1024).decode()
            if not packet:
                break

            logging.debug("Something happened to the packet: {}".format(packet))

            # check for corruption
            prob_corrupted = random.random()
            logging.debug("Corruption Probability Toleration: {}".format(prob_corruption))
            logging.debug("Packet Corruption: {}".format(prob_corrupted))
            if prob_corrupted < prob_corruption:
                # corrupted packet
                print("A Corrupted packet has just been received")
                print("A NACK is about to be sent")
                packet = build_packet(0, packet_seq, 0, 1)
                is_corrupt = True
            else:
                # uncorrupted packet
                seq = re.search(r"seq =\s+(\d+)", packet)
                if seq:
                    seq = int(seq.group(1))

                if prev_seq == seq:
                    print("A duplicate packet with sequence number {} has been received".format(seq))
                else:
                    print("A packet with sequence number {} has been received".format(seq))
                    is_corrupt = False

                print("Packet received contains: {}".format(packet))
                print("An ACK is about to be sent")
                packet = build_packet(0, packet_seq, 1, 0)

            print("Packet to send contains: {}".format(packet))

            connection_id.send(packet.encode())
            if not is_corrupt:
                prev_seq = seq
                if prev_seq == seq:
                    print("The receiver is moving to state WAIT FOR {} FROM BELOW".format((seq+1) % 2))
                    packet_seq = (seq+1) % 2
                else:
                    print("The receiver is moving to state WAIT FOR {} FROM BELOW".format((prev_seq+1) % 2))
                    packet_seq = (prev_seq + 1) % 2
            else:
                if prev_seq == seq:
                    print("The receiver is moving back to state WAIT FOR {} FROM BELOW".format((seq + 1) % 2))
                    packet_seq = (seq + 1) % 2
                else:
                    print("The receiver is moving back to state WAIT FOR {} FROM BELOW".format((prev_seq + 1) % 2))
                    packet_seq = (prev_seq + 1) % 2
            logging.debug("packet should have been sent")


if __name__ == "__main__":
    main()
