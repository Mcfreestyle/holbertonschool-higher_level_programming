#!/usr/bin/node

const { argv } = require('process');
let iter = parseInt(argv[2]);

if (iter) for (; iter > 0; iter--) console.log('C is fun');
else console.log('Missing number of occurrences');
