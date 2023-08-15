#!/usr/bin/node
const times = process.argv[2];
if (!parseInt(times)) {
  console.log('Missing number of occurrences');
} else {
  let i =0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
}
