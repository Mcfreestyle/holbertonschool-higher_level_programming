#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let { width, height } = this;
      while (height--) console.log(c.repeat(width));
    } else this.print();
  }
}

module.exports = Square;
