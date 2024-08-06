Currency Summation Microservice

Provides the sums of two lists of unknown length containing currency amounts, allowing users of the connected main program to view and benefit from these sums.

Note: This microservice is written for use with main programs written in Python.  It can be used with programs written in other languages, but preparation of input and handling output will be significantly more involved than the sample client.py code provided.

—------------------------------------------------------------------------------------------------------------------

Starting off:

Ensure you've downloaded and installed Python and have verified this with the following command:

python3 --version

Ensure you've installed the Python extension for your IDE.

Add the main program, as well as microservice files client.py and host.py to your project.

Configure a Python virtual environment for your project to use the latest version of Python and also include the ZeroMQ Module for Python using the following command:

python3 -m pip install zmq

Incorporate the sample client code or other means of sending data to and receiving data from the microservice into the main program.  When the microservice is integrated with the main program, proceed with the following guidance:

—------------------------------------------------------------------------------------------------------------------

How to programmatically REQUEST data:

Within the main program:

Prior to microservice call, ensure input from main program is in the proper format, which is:  One array containing two arrays, assigned to the variable program_input.  The first inner array must contain any number of income values separated by commas.  The second inner array must contain any number of expense values separated by commas.

Each value within the inner arrays must abide by the following:
–  string format
–  no empty strings
–  no dollar signs
–  no commas

Each input should be a string of digits which can, but does not have to, include a decimal point followed by more digits

Call to microservice client:
Call function client_process() with the program input array as an argument.  Assign function return to client_output to capture the output of the microservice.

Example driver (for inclusion in Python main program):


from client import *

program_input = [["40000", "34.56", "0"], ["1", "23.", "56"]]

client_output = client_process(program_input)

—------------------------------------------------------------------------------------------------------------------

How to programmatically RECEIVE data:

Within the main program:

The microservice output from the client is assigned to the variable microservice_output which contains the following:

One array called client_output with at least two elements and an optional third element containing the following:

Two elements occupying the last two indexes, that is [-2] and[-1] contain the sum of incomes  and the sum of expenses, respectively.
Sums of incomes are decimals.

Another, third element will be included with the output only if an error has been generated by the host due to receiving input values that do not meet the stated criteria.  In that case, the outputs may be incorrect, and this caveat is communicated via the client to the main program via this optional third element.  If this element is included, it will occupy the first index of the array[-3].

Output is organized into variables as follows:
microservice_output is assigned to the last two indexes of client output.
microservice_error_output is assigned to the first optional index of client output to capture error information, but microservice_error_output is only assigned to this value if the index exists in the client_output array (if there is an error).  Otherwise microservice_error_output  will have no value.


Example collection of output (for inclusion in Python main program):

microservice_output = client_output[-2:]
print(f"{microservice_output}")


if (len(client_output) == 3):
   microservice_error_output = client_output[-3]
   print(f"{microservice_error_output}")


If you need support using this microservice please contact the developer at deckecha@oregonstate.edu.

UML Diagram for Microservice:
https://github.com/ChristinaDec/microserviceCurrency/blob/main/UML%20Diagram.png




