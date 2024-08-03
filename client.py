# Author: Chanda Decker
# CS 361 Assignment 8 - Microservice for Teammate
# Python file contains code to create and use a client socket to send sequences of currency data to the host 
# for addition, to receive the sums of those sequences, and to return the sums to the driver in an array of sums.
# Last Modified: 8/2/2024

import zmq

def client_process(program_in):
    # Create Context instance to create sockets.
    context = zmq.Context()
    
    # Create socket of type REQ (allows only request/reply).
    socket = context.socket(zmq.REQ)
    
    # Connect to host socket that uses tcp ("remote").
    socket.connect("tcp://localhost:5555")
    
    #This is an array of two arrays(array_incomes, array_expenses).
    incomes_and_expenses = program_in
    
    #Declare array of final summations -  [0] is income, [1] is expenses.
    summations = []
    for each_array in incomes_and_expenses:
        for amount in each_array:
                # Send each individual amount to host.
                socket.send_string(f"{amount}")
                # Get return message from host each time.
                reply_msg = str(socket.recv(),'utf8');
                #Check if message from host is its error message.
                if (reply_msg == 'ERROR:invalid currency recieved'):
                    if len(summations) >= 1:
                        if (summations[0] != "Invalid Program Input to Microservice_: Sums may be Invalid"):
                            summations = ["Invalid Program Input to Microservice_: Sums may be Invalid"] + summations
                    else:
                         summations =  ["Invalid Program Input to Microservice_: Sums may be Invalid"] + summations
        # Send string to host indicating the end of an array of amounts (incomes or expenses)
        socket.send_string('end');
        # Recieve sum from host (income or expenses)
        host_sum = str(socket.recv(),'utf8')
        # Push host_sum to summations array.
        summations.append(host_sum)
        
    return summations

if __name__ == "__main__":
    client_process(arrays_in)