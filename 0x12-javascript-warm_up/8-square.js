#!/usr/bin/node

const { argv } = require('process');
const szSquare = parseInt(argv[2]);
let row;

if (szSquare) {
  for (let i = 0; i < szSquare; i++) {
    row = '';
    for (let j = 0; j < szSquare; j++) row += 'X';
    console.log(row);
  }
} else console.log('Missing size');
