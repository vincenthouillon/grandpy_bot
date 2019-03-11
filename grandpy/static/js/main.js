/* AJAX POST */
function ajaxPost(url, data, callback) {
    var b = true;
    var req = new XMLHttpRequest();
    req.open("POST", url);

    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Calls the callback function by passing the response of the request
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });

    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });

    req.send(data);
}


function myMap(lat, lng) {
    var latlng = new google.maps.LatLng(lat, lng);
    /* Object containing properties with predefined identifiers in Google Maps 
    to define options for displaying our map */

    var options = {
        center: latlng,
        zoom: 18,
        disableDefaultUI: true,
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

function botMsg(content, showGMap = false, toto) {
    console.log(toto)
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
    };

    if (typeof toto !== 'undefined') {
        url_elt = document.createElement('a');
        url_elt.href = toto;
        url_elt.appendChild(document.createTextNode(" [En savoir plus sur wikipedia]"));
        url_elt.setAttribute('target', '_blank');
        paragraph.appendChild(url_elt);
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


var form = document.querySelector('form');
form.addEventListener('submit', function (event) {
    event.preventDefault();
    var data = new FormData(form);
    if (data.entries().next().value[1]) {
        document.getElementById('loading').style.display='block';
        ajaxPost('/get_json', data, function (response) {
            var json_data = JSON.parse(response);
            var lat = json_data['latitude'];
            var lng = json_data['longitude'];
            humanMsg(json_data['sentence']);
            if (json_data['history'] == null) {
                botMsg(json_data['error_msg']);
                document.getElementById('loading').style.display='none';
            } else {
                botMsg(json_data['address_msg'] + json_data['address'], true);
                myMap(lat, lng);
                botMsg(json_data['summary_msg'] + json_data['history'], false, json_data['wikilink']);
                document.getElementById('loading').style.display='none';
                form.reset();
            }
        })
    } else {
        botMsg("Hum! Veuillez saisir une question !")
    }
});


botMsg("Que voulez-vous savoir ?", false);
