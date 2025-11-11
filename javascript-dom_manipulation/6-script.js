const Name = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    Name.textContent = data.name;
  })
  .catch(error => {
    console.error('Erreur :', error);
  });
