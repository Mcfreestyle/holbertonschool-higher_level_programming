#!/usr/bin/node
/* prints all characters of a Star Wars movie in the order of the list "characters" in the /films/ response */

const idMovie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/';
const axios = require('axios');

const getName = async (url) => {
  const charac = await axios.get(url);
  const name = charac.data.name;
  return (name);
};

const getCharacters = async (api, idMovie) => {
  const film = await axios.get(api + idMovie);
  const characters = film.data.characters;

  for (const charc of characters) {
    const name = await getName(charc);
    console.log(name);
  }
};
getCharacters(api, idMovie);
