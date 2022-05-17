#!/usr/bin/node
/* Writes a string to a file */

const { argv } = require('process');
const fs = require('fs');
const file = argv[2];
const content = argv[3];

fs.writeFile(file, content, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
