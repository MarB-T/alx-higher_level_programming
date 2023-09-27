#!/usr/bin/node

const request = require('request');
const file = process.argv[2];
request(file, function (err, response, body) {
	if (err) console.log(err);
	else {
		const tasks = JSON.parse(body);
		let completed = 0;
		for (const task in tasks) {
			if (task.completed == true) {
				completed++;
			}
		}
		console.log(completed);
	}
});
