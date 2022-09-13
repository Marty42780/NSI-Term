// Menu Div
const menuDiv = document.querySelector('#menuDiv');
const menuButton = document.querySelector('#menuButton');

menuDiv.style.display = "block"; // Securité si le js ne se charge pas

function showMenu() {
    if (menuDiv.classList.contains('showed')) {
        menuDiv.classList.remove('showed');
        menuButton.innerHTML = "Tout voir";
        menuButton.classList.remove('showed');
        
    } else {
        menuDiv.classList.add('showed');
        menuButton.innerHTML = "Cacher";
        menuButton.classList.add('showed');
    }
}