#!/usr/bin/node

const { argv } = require('process');
const szSquare = parseInt(argv[2]);

if (szSquare) {
  for (let i = 0; i < szSquare; i++) {
    console.log('X'.repeat(szSquare));
  }
} else console.log('Missing size');
