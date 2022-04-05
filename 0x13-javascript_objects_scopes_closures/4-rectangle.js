#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let { width, height } = this;
    while (height--) console.log('X'.repeat(width));
  }

  rotate () {
    const { width, height } = this;
    this.width = height;
    this.height = width;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
