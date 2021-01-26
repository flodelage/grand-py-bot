
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
function title_speech(address) {
	return "Je sais plein de choses sur " + address + " !";
}

function extract_speech(extract) {
	return "Laisse moi te raconter... " + extract;
}

function wiki_speech(wiki_link) {
	return "Si tu veux en savoir plus n'hésites pas à consulter cette page " + wiki_link;
}

function locationStory(address, extract, wiki_url) {
	const responseElement = document.getElementById("response");

	const responseAddress = document.createElement("p");
	responseAddress.className = "response-address";
	responseAddress.textContent = title_speech(address);
	responseElement.appendChild(responseAddress);

	const responseExtract = document.createElement("p");
	responseExtract.className = "response-extract";
	responseExtract.textContent = extract_speech(extract);
	responseElement.appendChild(responseExtract);

	const responseUrl = document.createElement("p");
	responseUrl.className = "response-url";
	const urlLink = document.createElement("a");
	urlLink.className = "url-link";
	const urlLinkText = document.createTextNode("Wikipédia");
	urlLink.setAttribute('href', wiki_url);
	responseUrl.textContent = wiki_speech(urlLink);
	responseElement.appendChild(responseUrl);
	responseElement.appendChild(urlLinkText);
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
				locationStory(response['address'], response['location_infos']['extract'], response['location_infos']['wiki_url']);
				initMap(response['location_coordinates'], "map")
			},
			error: function(error) {
				console.log(error);
			}
		});
		event.preventDefault();
	});

})
