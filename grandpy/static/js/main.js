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
        console.error("Network error with URL " + url);
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
    var map = new google.maps.Map(document.getElementsByClassName("googlemaps")[number], options);

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

function showMsg(content, bot = true, wikiUrl) {
    var newMsg = document.createElement('div');
    if (bot == false) {
        newMsg.setAttribute('class', 'incoming_msg');
        var type = document.createElement('div');
        type.setAttribute('class', 'human');
        type.appendChild(document.createTextNode(timeNow() + 'Vous :'));
    } else {
        newMsg.setAttribute('class', 'oucoming_msg');
        var type = document.createElement('div');
        type.setAttribute('class', 'bot');
        type.appendChild(document.createTextNode(timeNow() + 'Grandpy :'));
    }

    newMsg.appendChild(type);
    var paragraph = document.createElement('p');
    paragraph.appendChild(document.createTextNode(content));
    newMsg.appendChild(paragraph);

    if (typeof wikiUrl !== 'undefined') {
        url_elt = document.createElement('a');
        url_elt.href = wikiUrl;
        url_elt.appendChild(document.createTextNode(" [En savoir plus sur wikipedia]"));
        url_elt.setAttribute('target', '_blank');
        paragraph.appendChild(url_elt);
    }
    var reply = document.getElementsByClassName('msg_reply')[0];
    reply.appendChild(newMsg);
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

var number = 0;
var form = document.querySelector('form');
form.addEventListener('submit', function (event) {
    event.preventDefault();
    var user_input = document.getElementById('queryTxt').value;
    if (user_input == "") {
        showMsg("Hum! Veuillez saisir une question !")
    } else {
        document.getElementById('loading').style.display = 'block';
        var data = new FormData(form);
        ajaxPost('/get_json', data, function (response) {
            var json_data = JSON.parse(response);
            var lat = json_data['latitude'];
            var lng = json_data['longitude'];
            showMsg(json_data['sentence'], false);
            if (json_data['history'] == null) {
                showMsg(json_data['error_msg']);
                document.getElementById('loading').style.display = 'none';
                form.reset();
            } else {
                showMsg(json_data['address_msg'] + json_data['address']);
                // Option display Google Maps
                var showMap = document.createElement('div');
                showMap.className = 'googlemaps';
                document.getElementsByClassName('msg_reply')[0].appendChild(showMap);
                myMap(lat, lng);
                (function () { number += 1; })();

                showMsg(json_data['summary_msg'] + json_data['history'], true, json_data['wikilink']);
                document.getElementById('loading').style.display = 'none';
                form.reset();
                scrollBottom();
            }
        })
    }
})

showMsg("Que voulez-vous savoir ?");
