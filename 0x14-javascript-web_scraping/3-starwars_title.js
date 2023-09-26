#!/usr/bin/node

const request = require('request');
const number = process.argv[2];
const file = 'https://swapi-api.alx-tools.com/api/films/${number}';
request(file, function (err, response, body) {
	if (err) console.log(err);
	else { console.log(JSON.parse(body).title);}
});
