#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let y = 0; y < this.height; y++) {
        for (let x = 0; x < this.width; x++) {
          process.stdout.write(c);
        }
        console.log();
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
