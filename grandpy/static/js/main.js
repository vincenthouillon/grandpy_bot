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


ajaxGet('/get_json', function (response) {
    let coordinates = JSON.parse(response);
    var lat = coordinates['latitude'];
    var lng = coordinates['longitude'];
    myMap(lat, lng)
});


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
