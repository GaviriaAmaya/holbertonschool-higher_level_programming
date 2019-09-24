#!/usr/bin/node
// Square class, custom printable

const Squ = require('./5-square');
class Square extends Squ {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
