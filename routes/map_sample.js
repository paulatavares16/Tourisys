function initMap() {
  var directionsDisplay = new google.maps.DirectionsRenderer();
  var directionsService = new google.maps.DirectionsService();
  var latLngWaypoints = getLatLng();
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: window.conf_origin
  });
  directionsDisplay.setMap(map);

  calculateAndDisplayRoute(
    directionsService,
    directionsDisplay,
    latLngWaypoints
  );
  document.getElementById("mode").addEventListener("change", function () {
    calculateAndDisplayRoute(
      directionsService,
      directionsDisplay,
      latLngWaypoints // estava faltando parametro
    );
  });
}

function calculateAndDisplayRoute(
  directionsService,
  directionsDisplay,
  latLngWaypoints
) {
  var selectedMode = document.getElementById("mode").value;
  // chamada API de rota
  directionsService.route(
    {
      origin: window.conf_origin,
      destination: window.conf_origin,
      waypoints: latLngWaypoints,
      travelMode: google.maps.TravelMode[selectedMode],
      optimizeWaypoints: true,
    },
    function (response, status) {
      if (status == "OK") {
        console.log(response)
        directionsDisplay.setDirections(response);
      } else {
        window.alert("Directions request failed due to " + status);
      }
    }
  );
}

// Formata wayPoints gerados via recomendacao
function getLatLng() {
  var list = [];
  window.waypoints.forEach(function (element) {
    loc = { location: new google.maps.LatLng(element.lat, element.lng) };
    list.push(loc);
  });
  return list;
}
