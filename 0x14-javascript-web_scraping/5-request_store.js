#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file */

const url = process.argv[2];
const file = process.argv[3];
const axios = require('axios');
const fs = require('fs');

axios.get(url)
  .then(res => {
    const content = res.data;
    fs.writeFile(file, content, 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  });
