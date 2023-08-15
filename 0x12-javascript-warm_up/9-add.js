#!/usr/bin/node
const firstNum = process.argv[2];
const secondNum = process.argv[3];

function add (firstNum, secondNum) {
  return (firstNum + secondNum);
}
console.log(add(parseInt(firstNum), parseInt(secondNum)));
