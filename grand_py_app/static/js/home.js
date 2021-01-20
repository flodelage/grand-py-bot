
// Initialize and add the map
function initMap(locationCoordinates, div) {
	const map = new google.maps.Map(document.getElementById(div), {
	  zoom: 15,
	  center: locationCoordinates,
	});
	// The marker, positioned at location_coordinates
	const marker = new google.maps.Marker({
	  position: locationCoordinates,
	  map: map,
	});
  }

// Initialize and add the bot response
function locationStory(title, extract, wiki_url) {
	const responseElement = document.getElementById("response");

	const responseTitle = document.createElement("p");
	responseTitle.className = "response-title";
	responseTitle.textContent = title;
	responseElement.appendChild(responseTitle);

	const responseExtract = document.createElement("p");
	responseExtract.className = "response-extract";
	responseExtract.textContent = extract;
	responseElement.appendChild(responseExtract);

	const responseUrl = document.createElement("p");
	responseUrl.className = "response-url";
	responseUrl.textContent = wiki_url;
	responseElement.appendChild(responseUrl);
}

// Ajax when user submits
$(document).ready(function() {
	$('#form-place').submit(function( event ) { //quand l utilisateur soumet sa saisie
		var place = $('#input_place').val(); //la saisie est stockée

		$.ajax({
			url: '/process',
			data: $('form').serialize(), //la saisie est envoyée à la méthode de l'url /process
			type: 'POST',
			success: function(response) {
				locationStory(response['location_infos']['title'], response['location_infos']['extract'], response['location_infos']['wiki_url']);
				initMap(response['location_coordinates'], "map")
			},
			error: function(error) {
				console.log(error);
			}
		});
		event.preventDefault();
	});

})
