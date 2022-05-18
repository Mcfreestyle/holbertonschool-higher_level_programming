#!/usr/bin/node
/* prints all characters of a Star Wars movie */

const idMovie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/';
const axios = require('axios');

axios.get(api + idMovie, { responseType: 'json' })
  .then(res => {
    const characters = res.data.characters;
    for (const charc of characters) {
      axios.get(charc)
        .then(res => {
          console.log(res.data.name);
        })
        .catch(err => {
          console.log(err.response.status);
        });
    }
  })
  .catch(err => {
    console.log(err.response.status);
  });
