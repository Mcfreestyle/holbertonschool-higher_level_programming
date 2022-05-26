// Adds, removes and clears LI elements from a list when the user clicks
$(() => {
  const myList = $('UL.my_list');
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');

  addItem.click(() => myList.append($('<li>Item</li>')));
  removeItem.click(() => $('li').last().remove());
  clearList.click(() => myList.empty());
});
