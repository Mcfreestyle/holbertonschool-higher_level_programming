// Adds a <li> element to a list when the user clicks on the tag DIV#add_item
const myList = $('UL.my_list');
const li = $('<li>Item</li>');
const addItem = $('DIV#add_item');

addItem.click(() => {
  myList.append(li);
});
