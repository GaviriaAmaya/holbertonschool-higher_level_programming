#!/usr/bin/node
// Define the square class, that inherits full rectangle

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
