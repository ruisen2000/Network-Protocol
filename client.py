from socket import *
import sys
import random
import time
import re
import math
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
# logging.getLogger().setLevel(logging.DEBUG)


def random_from_state(state, upper):
    random.setstate(state)
    new_number = random.random() * upper
    return new_number, random.getstate()


def build_packet(field1, field2, field3, field4):
    return "data = {}  seq = {}  ack = {}  nack = {}".format(field1, field2, field3, field4)


def main():
    server_name = 'localhost'
    server_port = 50007
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    print("connected to: " + str(server_name) + str(server_port))

    delay_upper = 5
    prob_upper = 1

    try:
        seed_timing = int(sys.argv[1])
        packet_num = int(sys.argv[2])
        seed_ack = int(sys.argv[3])
        prob_ack = float(sys.argv[4])
    except IndexError:
        print("Please provide assignment arguments when starting up the script.")
        return

    random.seed(seed_timing)
    delay_state = random.getstate()

    random.seed(seed_ack)
    ack_state = random.getstate()

    # Initiate packet delay variable
    packet_delay = time.time()
    for packet_number in range(0, packet_num):
        logging.debug("Packet Number: {}".format(packet_number))
        resend = False
        flag = True

        field1 = 123 + packet_number
        field2 = packet_number % 2
        field3 = 0
        field4 = 0

        # Starting protocol
        print("The sender is moving to state WAIT FOR CALL {} FROM ABOVE".format(field2))
        while flag:
            packet = build_packet(field1, field2, field3, field4)
            if resend:
                print("A packet with sequence number {} is about to be resent".format(field2))
            else:
                print("A packet with sequence number {} is about to be sent".format(field2))

            print("Packet to send contains: {}".format(packet))

            # Sending packet
            current_time = time.time()
            if packet_delay > current_time:
                logging.debug("Packet delay time is {} seconds".format(packet_delay-current_time))
                time.sleep(packet_delay-current_time)
            client_socket.send(packet.encode())
            # get delay time before new data arrives for next packet
            packet_delay, delay_state = random_from_state(delay_state, delay_upper)
            packet_delay = time.time() + math.ceil(packet_delay)

            logging.debug("Delay time: {}".format(packet_delay))

            if resend:
                print("The sender is moving back to state WAIT FOR ACK OR NACK")
            else:
                print("The sender is moving to state WAIT FOR ACK OR NACK")
            packet = client_socket.recv(1024).decode()
            logging.debug("some message was received.")
            ack_check = re.search(r"ack =\s+(\d+)", packet)
            nack_check = re.search(r"nack =\s+(\d+)", packet)

            # determine corruption value
            prob_corrupted, ack_state = random_from_state(ack_state, prob_upper)

            # check for corruption
            logging.debug("Probability of Corruption: {}".format(prob_ack))
            logging.debug("Packet Corruption: {}".format(prob_corrupted))
            if prob_corrupted < prob_ack:
                print("A Corrupted ACK or NACK packet has just been received")
                resend = True
                continue

            # not corrupted case
            if ack_check and ack_check.group(1) == "1":
                print("An ACK packet has just been received")
                resend = False
                flag = False
            if nack_check and nack_check.group(1) == "1":
                print("A NACK packet has just been received")
                resend = True
            print("Packet received contains: {}".format(packet))
    client_socket.close()


if __name__ == "__main__":
    main()
