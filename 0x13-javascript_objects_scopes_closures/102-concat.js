#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

const data1 = fs.readFileSync(argv[2]);
const data2 = fs.readFileSync(argv[3]);

fs.writeFileSync(argv[4], data1 + data2);
