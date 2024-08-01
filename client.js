//Chanda Decker 
//CS361 Microservice (Client) for summation of groups of currency

// Code for App.js

// Function retrieves collection indexed to a particular user from Mongodb.
async function getUserCollection(whatever_user_is_logged_in) {
    var cursor = client.db(database_name).collection(collection_name).find({user: whatever_user_is_logged_in})
    if (await cursor.hasNext()) {
        return await cursor.next()
    }      
}

// Get request for webpage that displays summary of income and expenses.
app.get('/webpage with income and expense summaries', async function(req, res) {
    
    //Retrieving collection belonging to a particular user from Mongodb.
    var user_collection = await getUserCollection(whatever_user_is_logged_in)
    
    //Array of: "income document" (array of incomes) and "expenses document" (array of expenses)
    //This is an array of two arrays.
    var data_out = [user_collection.income, user_collection.expenses]
    
    //Declare array of final summations -  [0] is income, [1] is expenses.
    var summations = []
    
    // Loop through data_out (out to host) array of two items.
    for (let i=0; i < length.data_out; i++) {
        // Amounts out is array of incomes
        var amounts_out = data_out[i]

        const zmq = require('zeromq');

        async function runClient() { 

            const sock = new zmq.Request();
            sock.connect('tcp://localhost:5555');
            // Loop through array of incomes
            for (let i=0; i<amounts_out; i++) {
                // Send each individual amount to host.
                await sock.send(send_str(amounts_out[i]));
                // Get return message from host each time.
                let from_host = await sock.receive().toString('utf8');
                // Check if message from host is its error message.
                if (from_host = 'ERROR:invalid currency recieved') {
                    var summations = [null, null]
                }    
            }
            // Send string to host indicating the end of an array of amounts (incomes or expenses)
            await sock.send('end');
            // Recieve sum from host (income or expenses)
            var this_summation = await sock.receive().toString('utf8')
            //Push sum to summations array.
            summations.push(this_summation)
        }
        runClient();
    }
    // Render page with the two sums as local variables for the view.
    res.render('webpage with income and expense summaries', { sum_income: summations[0], sum_expenses: summations[1]})
})
