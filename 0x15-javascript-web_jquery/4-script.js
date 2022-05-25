// Toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
const header = $('header');
const toggleHeader = $('DIV#toggle_header');

toggleHeader.click(() => {
  header.toggleClass('green red');
});
