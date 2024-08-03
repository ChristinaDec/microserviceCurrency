# Author: Chanda Decker
# CS 361 Assignment 8 - Microservice for Teammate
# Driver runs client method using program input.
# Last Modified: 8/2/2024

from client import *


# Input from program goes here: [[incomes][expenses]] 
# Commas and dollar signs are not valid inputs.
program_input_1 = [["40000", "34.56", "0"], ["", "23.", "56"]]

program_input_2 = [["$23", "34", "54"], ["1", "23", "56,000"]]

# Call client 
client_output = client_process(program_input_1)
#client_output = client_process(program_input_2)

# Substantive output: array with two sums [income sum, expense sum]
microservice_output = client_output[-2:]
print(f"{microservice_output}")

# Error output: Will exist if error.
if (len(client_output) == 3): 
    microservice_error_output = client_output[-3]
    print(f"{microservice_error_output}")
