longeurPanier = 0
function ajouterAuPanier (name, price, image) {
    let panierItems = document.querySelector('.items');
    document.querySelector(".empty-cart").classList.add("hidden");
    panierItems.style.alignItems = "unset";
    longeurPanier += 1;
    console.log(longeurPanier);
    panierItems.insertAdjacentHTML('beforeend', `<div class="item item` + longeurPanier + `">
    <img src="images/animaux/` + image + `"  class="animal">
    <h2>` + name + `</h2>
    <div><h3>` + price +  `</h3></div>
    <button onclick="enleverDuPanier(` + longeurPanier + `)"><img src="images/trash_icon.png" class="trash-icon"></button>
    </div>`);
}
function enleverDuPanier (id) {
    document.querySelector(`.item` + id).remove();
    longeurPanier -= 1;
    if (longeurPanier === 0) {
        console.log(longeurPanier)
        document.querySelector(".empty-cart").classList.remove("hidden");
        
    }
}