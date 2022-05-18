#!/usr/bin/node
/* prints the number of movies where the character "Wedge Antilles" is present, his id is 18 */

const axios = require('axios');
const api = process.argv[2];
const charac = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(api, { responseType: 'json' })
  .then(res => {
    const films = res.data.results;
    let count = 0;

    for (const film of films) {
      for (const c of film.characters) {
        if (charac === c) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(err => {
    console.log('Error:', err.response.status);
  });
