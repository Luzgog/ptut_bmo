function temperature(){
    
    fetch("/temperature")//on fait une requete a /message
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("TEMP")//variable html type : id

        valeur.innerText = j["TEMPE"]//varriable python
    })
}

function batterie(){
    
    fetch("/batterie")//on fait une requete a /message
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("BATT")

        valeur.innerText = j["BATTE"]
    })
}

function etats(){
    
    fetch("/etats")//on fait une requete a /message
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("STAT")

        valeur.innerText = j["STATS"]
    })
}

function humeurs(){
    
    fetch("/humeurs")//on fait une requete a /message
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("MOOD")

        valeur.innerText = j["HUMER"]
    })
}
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

function PARAM_METEO(){
    
    fetch("/PARAMETRE_METEO")//on fait une requete a la fonction python : /fsefuysbfuza
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("PARAM_METEO")//valeur de l'id HTML

        valeur.innerText = j["Valeur_PARAMETRE_METEO"]
    })
}
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
function PARAM_EMO_METEO(){
    
    fetch("/PARAMETRE_EMO_METEO")//on fait une requete a /message
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("PARAM_EMO_METEO")

        valeur.innerText = j["Valeur_PARAMETRE_EMO_METEO"]
    })
}
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
function PARAM_RECO_FACIAL(){
    
    fetch("/PARAMETRE_RECO_FACIAL")//on fait une requete a /message
    .then( data => {console.log(data);return data.json()})//on prend ce que ca nous renvoie et on retourne le json
    .then( j =>{//avec le json on va modifier la valeur pour la changer
        console.log(j);
        var valeur = document.getElementById("PARAM_RECO_FACIAL")

        valeur.innerText = j["Valeur_PARAMETRE_RECO_FACIAL"]
    })
}
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
function bouton_parametre(variable){
    fetch("/button", {method:'POST',headers:{'Accept': 'application/json', 'Content-Type': 'application/json'}, body:JSON.stringify(variable)} )    
}
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
//oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

setInterval(PARAM_METEO, 1000)
setInterval(PARAM_EMO_METEO, 1000)
setInterval(PARAM_RECO_FACIAL, 1000)

setInterval(humeurs, 1000)
setInterval(etats, 1000)
setInterval(batterie, 1000)
setInterval(temperature, 1000)