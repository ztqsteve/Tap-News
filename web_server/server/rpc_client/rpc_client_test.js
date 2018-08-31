var client = require('./rpc_client');

client.add(1, 2, (response) => {
  console.assert(response == 3);
})
