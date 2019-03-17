function initMap() {
  var directionsDisplay = new google.maps.DirectionsRenderer();
  var directionsService = new google.maps.DirectionsService();
  var latLngWaypoints = getLatLng();
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: { lat: -12.8996, lng: -38.4035924 }
  });
  directionsDisplay.setMap(map);

  calculateAndDisplayRoute(
    directionsService,
    directionsDisplay,
    latLngWaypoints
  );
  document.getElementById("mode").addEventListener("change", function() {
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
      destination: { lat: -13.00792144, lng: -38.51707822 },
      waypoints: latLngWaypoints,
      travelMode: google.maps.TravelMode[selectedMode],
      optimizeWaypoints: true,
    },
    function(response, status) {
      if (status == "OK") {
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
  waypoints.forEach(function(element) {
    loc = { location: new google.maps.LatLng(element.lat, element.lng) };
    list.push(loc);
  });
  return list;
}
