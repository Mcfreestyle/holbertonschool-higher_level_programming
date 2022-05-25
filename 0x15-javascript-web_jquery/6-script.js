// Updates the text of the <header> element to New Header!!!
const header = $('header');
const updateHeader = $('DIV#update_header');

updateHeader.click(() => {
  header.text('New Header!!!');
});
