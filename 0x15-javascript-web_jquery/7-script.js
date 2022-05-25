// Fetches the character name from a URL and display it in a HTML tag
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = $('DIV#character');

$.get(url, ({ name }) => {
  character.text(name);
});
