// Updates the text color of the <header> element to red when the user clicks on the tag DIV#red_header
const header = $('header');
const div = $('#red_header');
div.on('click', () => {
  header.css('color', '#FF0000');
});
