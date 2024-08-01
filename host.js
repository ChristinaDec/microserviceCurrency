//Chanda Decker 
//CS361 Microservice (Host) for summation of groups of currency

// Program running continuously on host

// Array of accumulating amounts to sum.
let recieve_amounts = [];

// Initialize sum to send to client.
let sum = 0;

const zmq = require('zeromq');

async function runServer() {

const sock = new zmq.Reply();

try {
    await sock.bind('tcp://*:5555');
    for await (const [msg] of sock) {
        // regex to check incoming currency format $[1-5 digits].[only two digits]
        let reg = new RegExp(/^\$([1-9]{1,5})(\.[0-9]{2})$/)
        // if message from client does NOT indicate to stop and calculate sum...
        if (msg.toString('utf8') != 'end') {
            let str_msg = msg.toString('utf8');
            // If input is of the regex enforced format
            if (reg.test(str_msg)) {
                // Push input onto array.
                recieve_amounts.push(msg)
                // Keep up running sum.
                sum = sum + msg 
                // Send message to client for each valid input.
                await sock.send('valid currency recieved');     
            } else {
                // If input is not of the regex enforced format
                await sock.send('ERROR:invalid currency recieved')
            }
        // If message from client indicates the end of input 
        } else if (msg.toString('utf8') = 'end') { 
            // Send running sum to client.
            await sock.send(sum); 
        } 
    }
} catch (err) {
    console.error(err);
}};

runServer();
