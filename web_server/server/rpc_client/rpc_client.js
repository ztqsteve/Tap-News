var jayson = require('jayson');

var client = jayson.client.http({
  port: 4040,
  hostname: 'localhost'
});

function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser',[user_id, page_num], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

module.exports = {
  getNewsSummariesForUser
}
