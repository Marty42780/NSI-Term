try {if (acceuil[1] === "disable") {title = "Accueil"}} catch (e) {acceuil = ["index.html", "enable"]}    
try {if (themes1ere[1] === "disable") {title = "Thèmes 1ère"}} catch (e) {themes1ere = ["themes1ere.html", "enable"]}    
try {if (themesTerm[1] === "disable") {title = "Thèmes Terminale"}} catch (e) {themesTerm = ["themesTerm.html", "enable"]}
try {if (animaux[1] === "disable") {title = "Promenade des Animaux"}} catch (e) {animaux = ["animaux.html", "enable"]}  
try {if (expose[1] === "disable") {title = "Exposé"}} catch (e) {expose = ["expose.html", "enable"]}

document.write(`
<link rel="stylesheet" href="css/navigation.css" />
<section id="top-bar">
    <h1>NSI - ` + title + `</h1>
    <ul id="menu">
        <a href="` + acceuil[0] + `" class="` + acceuil[1] + ` accueil">
            <li>Accueil</li>
        </a>
        <a href="` + themes1ere[0] + `" class="` + themes1ere[1] + ` themes1ere">
            <li>Thèmes de 1ère</li>
        </a>
        <a href="` + themesTerm[0] + `" class="` + themesTerm[1] + ` themesTerm">
            <li>Thèmes de Terminale</li>
        </a>
        <a href="` + animaux[0] + `" class="` + animaux[1] + ` animaux"> 
            <li>Animaux</li> 
        </a>
        <a href="` + expose[0] + `" class="` + expose[1] + ` expose"> 
            <li>Exposé</li> 
        </a>
        <button id="menuButton" onclick="showMenu()">Tout voir</button>
    </ul>
</section>
<div id="menuDiv">
<div class="grid">
    <a href="` + acceuil[0] + `">
        <div class="` + acceuil[1] + ` accueil">
            <img src="images/peppapig.png" alt="" />
            <h2>Acceuil</h2>
            <h1>Introduction</h1>
        </div>
    </a>
    <a href="` + themes1ere[0] + `">
        <div class="` + themes1ere[1] + ` themes1ere">
            <img src="01-Html_Css/images/accueil-vscode_logo.png" alt="" />
            <h2>Thèmes</h2>
            <h1>Thèmes de NSI</h1>
        </div>
    </a>
    <a href="` + themesTerm[0] + `">
        <div class="` + themesTerm[1] + ` themesTerm">
            <img src="images/binaire.png" alt="" />
            <h2>Thèmes</h2>
            <h1>Thèmes de NSI</h1>
        </div>
    </a>
    <a href="` + animaux[0] + `">
        <div class="` + animaux[1] + ` animaux">
            <img src="images/animaux/panda.jpg" alt="" />
            <h2>Animaux</h2>
            <h1>Promenade avec les animaux</h1>
        </div>
    </a>
    <a href="` + expose[0] + `">
        <div class="` + expose[1] + ` expose">
            <img src="images/algobox-dev.png" alt="" />
            <h2>Exposé</h2>
            <h1>Les languages de programation</h1>
        </div>
    </a>
</div>
</div>
`);

