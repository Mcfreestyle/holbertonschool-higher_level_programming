#!/usr/bin/node
/* prints the title of a Star Wars movie where the episode number matches a given integer */

const axios = require('axios');
const idMovie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/' + idMovie;

axios.get(api, { responseType: 'json' })
  .then(res => {
    console.log(res.data.title);
  });
