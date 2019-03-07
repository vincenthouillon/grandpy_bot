/* Make an AJAX GET call
Takes into parameters the target URL and callback function called on success */
function ajaxGet(url, callback) {
    var req = new XMLHttpRequest();
    req.open("GET", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Calls the callback function by passing the response of the request
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Network error with URL " + url);
    });
    req.send(null);
};

function myMap(lat, lng) {
    var latlng = new google.maps.LatLng(lat, lng);
    /* Object containing properties with predefined identifiers in Google Maps 
    to define options for displaying our map */

    var options = {
        center: latlng,
        zoom: 19,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googlemaps"), options);

    // Marker creation
    var marqueur = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        map: map

    });
};

function scrollBottom() {
    var messaging = document.getElementById('messaging');
    messaging.scrollTop = messaging.scrollHeight;
}

function botMsg(content, showGMap = false) {
    // Create a div and define the class attribute 'incoming_msg'
    var newMsg = document.createElement('div');
    newMsg.setAttribute('class', 'outgoing_msg');
    // Create a div and define the class attribute 'human' and add this to 'outgoing_msg'
    var type = document.createElement('div');
    type.setAttribute('class', 'bot');
    type.appendChild(document.createTextNode(timeNow() + 'GrandPy :'));
    newMsg.appendChild(type);
    // Create a paragraph and add this to 'outgoing_msg'
    var paragraph = document.createElement('p');
    paragraph.appendChild(document.createTextNode(content));
    newMsg.appendChild(paragraph);
    // Option display Google Maps
    var showGMap = showGMap;
    if (showGMap === true) {
        var showMap = document.createElement('div');
        showMap.id = 'googlemaps';
        newMsg.appendChild(showMap);
        ajaxGet('/get_json', function (response) {
            var data = JSON.parse(response);
            // var lat = data['latitude'];
            // var lng = data['longitude'];
            var kw = data['keyword'];
            // var address = data['address'];
            var history = data['history'];

            console.log(kw,': ',history);
            // myMap(lat, lng);
        });
    }
        // Insert 'outgoing_msg' before div'id=new_msg'
        var msg = document.getElementById('new_msg');
        var parentDiv = msg.parentNode;
        parentDiv.insertBefore(newMsg, msg);
        scrollBottom();
    }

function humanMsg(content) {
    var newMsg = document.createElement('div');
    newMsg.setAttribute('class', 'incoming_msg');
    var type = document.createElement('div');
    type.setAttribute('class', 'human');
    type.appendChild(document.createTextNode(timeNow() + 'Vous :'));
    newMsg.appendChild(type);
    var paragraph = document.createElement('p');
    paragraph.appendChild(document.createTextNode(content));
    newMsg.appendChild(paragraph);
    var msg = document.getElementById('new_msg');
    var parentDiv = msg.parentNode;
    parentDiv.insertBefore(newMsg, msg);
    scrollBottom()
}

function timeNow() {
    let time = new Date();
    var hour = time.getHours();
    if (hour < 10) {
        hour = "0" + hour;
    }
    var minutes = time.getMinutes();
    if (minutes < 10) {
        minutes = "0" + minutes
    }
    return '[' + hour + ':' + minutes + '] '
}


botMsg("Que voulez-vous savoir ?")
humanMsg("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassroms ?")
botMsg('Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris', true)
botMsg("Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]")
