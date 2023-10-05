// Select the HTML elements
const list = jQuery('#my_list');
const addItemButton = jQuery('#add_item');
const removeItemButton = jQuery('#remove_item');
const clearListButton = jQuery('#clear_list');

addItemButton.click(() => {
  const newItem = jQuery('<li>Item</li>');
  list.append(newItem);
});

removeItemButton.click(() => {
  list.find('li:last').remove();
});

clearListButton.click(() => {
  list.empty();
});
