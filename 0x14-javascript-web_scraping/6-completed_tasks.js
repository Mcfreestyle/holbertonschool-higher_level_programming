#!/usr/bin/node
/* computes the numbers of tasks completed by user id */

const api = process.argv[2];
const axios = require('axios');
const result = {};

axios.get(api, { responseType: 'json' })
  .then(res => {
    const tasks = res.data;

    for (const task of tasks) {
      if (task.completed === true) {
        if (result[task.userId] === undefined) {
          result[task.userId] = 1;
        } else {
          result[task.userId]++;
        }
      }
    }
    console.log(result);
  })
  .catch(err => {
    console.error(err);
  });
