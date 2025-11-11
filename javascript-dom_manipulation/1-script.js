const Header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.addEventListener("click", () => {
    Header.style.color = '#FF0000';
});
