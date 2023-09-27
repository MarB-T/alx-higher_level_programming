#!/usr/bin/node
/*
 * compute completed tasks
 */
const request = require('request');
const file = process.argv[2];
request(file, function (err, response, body) {
	if (err) console.log(err);
	else {
	    let results = {};
    let json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      let task = json[i];
      if (task['completed'] === true) {
        if (results[task['userId']] !== undefined) {
          results[task['userId']] += 1;
        } else {
          results[task['userId']] = 1;
        }
      }
    }
    console.log(results);
  }
});
