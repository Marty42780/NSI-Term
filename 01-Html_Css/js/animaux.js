longeurPanier = 0
function ajouterAuPanier (name, price, image) {
    panierItems = document.querySelector('.items')
    longeurPanier += 1
    console.log(longeurPanier)
    panierItems.insertAdjacentHTML('beforeend', `<div class="item item` + longeurPanier + `">
    <img src="images/animaux/` + image + `"  class="animal">
    <h2>` + name + `</h2>
    <div><h3>` + price +  `</h3></div>
    <button><img src="images/trash_icon.png" class="trash-icon" onclick="enleverDuPanier(` + longeurPanier + `)"></button>
</div>`)
}
function enleverDuPanier (id) {
    document.querySelector(`.item` + id).remove()
}