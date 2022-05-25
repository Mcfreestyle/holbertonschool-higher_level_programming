// Adds the class `red` to the <header> element when the user clicks on the tag DIV#red_header
const header = $('header');
const div = $('#red_header');

div.click(() => {
  header.addClass('red');
});
