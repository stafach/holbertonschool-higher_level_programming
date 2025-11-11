const li = document.querySelector('#add_item');
const ul = document.querySelector('.my_list');

li.addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  ul.appendChild(newLi);
});
