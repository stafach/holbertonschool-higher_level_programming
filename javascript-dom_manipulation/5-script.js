const Header = document.querySelector('header');
const update = document.querySelector('#update_header');

update.addEventListener('click', () => {
  Header.textContent = 'New Header!!!';
});
