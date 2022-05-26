// Fetches and lists the title for all movies by using a URL.
// All movie titles must be list in a HTML tag
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = $('UL#list_movies');

$.get(url, ({ results }) => {
  for (const film of results) {
    const title = film.title;
    listMovies.append($('<li></li>').text(title));
  }
});
