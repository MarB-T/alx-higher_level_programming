#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
let content1 = '';
let content2 = '';

fs.readFile(file1, function (err, data) {
  if (err) {
    throw err;
  }
  content1 = data.toString();
  fs.appendFile(file3, content1, function (err) {
    if (err) {
      throw err;
    }
  });
});

fs.readFile(file2, function (err, data) {
  if (err) {
    throw err;
  }
  content2 = data.toString();
  fs.appendFile(file3, content2, function (err) {
    if (err) {
      throw err;
    }
  });
});
