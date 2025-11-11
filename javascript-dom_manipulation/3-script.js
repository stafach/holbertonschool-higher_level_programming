const Header = document.querySelector('header');
const toggle = document.querySelector('#toggle_header');

toggle.addEventListener('click', () => {
  if (Header.classList.length === 0) {
    Header.classList.add('green');
  } else if (Header.classList.contains('green')) {
    Header.classList.replace('green', 'red');
  } else {
    Header.classList.replace('red', 'green');
  }
});
