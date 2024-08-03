# Author: Chanda Decker
# CS 361 Assignment 8 - Microservice for Teammate
# Python file contains code to create and use a host socket to receive sequences of currency data from the client, validate each datum,
# keep a running sum of each sequence, detect the end of each sequence, and send the sum of each sequence to the client.
# Last Modified: 8/2/2024

import zmq
import re

def main():
    # Create Context instance to create sockets.
    context = zmq.Context()

    # Create socket of type REP (allows only request/reply).
    socket = context.socket(zmq.REP)

    # Bind socket to port that uses TCP (local).
    socket.bind("tcp://*:5555")
    
    # Initialize sum to send to client.
    sum = 0;

    # Continually receive any requests from client and print them.
    while True:
        # Recieve an inidividual amount from client.
        client_msg = str(socket.recv(), 'utf-8')
        # check to see if client indicates the end of the sequence has been reached.
        if client_msg != 'end':
        # regex to check incoming amount is a number
            regex = r"(^([0-9]+)(.[0-9]*)?$)"
            if (re.search(regex, client_msg) != None) and ("," not in client_msg) and ("$" not in client_msg):
                # Add amount to running sum for this sequence
                sum = sum + float(client_msg)
                socket.send_string('valid currency received')
            else: 
                # If incoming amount is not a number, inform client
                socket.send_string('ERROR:invalid currency recieved')
        elif client_msg == 'end':
            # if client indicates end of sequence has been reached
            socket.send_string(f"{sum}")
            sum = 0

if __name__ == "__main__":
    main()