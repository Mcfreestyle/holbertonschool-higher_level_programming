// Fetches from a URL and displays the value of hello from that fetch in a HTML tag
$(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const divHello = $('DIV#hello');

  $.get(url, ({ hello }) => {
    divHello.text(hello);
  });
});
