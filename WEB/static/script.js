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

function bouton_parametre(variable){
    fetch("/button", {method:'POST',headers:{'Accept': 'application/json', 'Content-Type': 'application/json'}, body:JSON.stringify(variable)} )    
}


setInterval(humeurs, 1000)
setInterval(etats, 1000)
setInterval(batterie, 1000)
setInterval(temperature, 1000)