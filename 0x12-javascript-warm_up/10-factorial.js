#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return (1);
  } else {
  return (x * factorial(x - 1));
  }
}
console.log(factorial(num));
