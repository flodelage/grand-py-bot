
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
function userRequestSpeech(user_request) {
	return "Je connais " + user_request + " !";
}

function titleSpeech(address) {
	return "Je sais plein de choses sur " + address + " !";
}

function extractSpeech(extract) {
	return "Laisse moi te raconter... " + extract;
}

function wikiSpeech() {
	return "Si tu veux en savoir plus n'hésite pas à consulter cette page ";
}

function locationStory(address, extract, wiki_url) {
	const responseElement = document.getElementById("response");

	const responseAddress = document.createElement("p");
	responseAddress.className = "response-address";
	responseAddress.textContent = titleSpeech(address);
	responseElement.appendChild(responseAddress);

	const responseExtract = document.createElement("p");
	responseExtract.className = "response-extract";
	responseExtract.textContent = extractSpeech(extract);
	responseElement.appendChild(responseExtract);

	const responseUrl = document.createElement("p");
	responseUrl.className = "response-url";
	const urlLink = document.createElement("a");
	urlLink.className = "url-link";
	const urlLinkText = document.createTextNode("Wikipédia");
	urlLink.setAttribute('href', wiki_url);
	urlLink.setAttribute('target', '_blank')
	urlLink.appendChild(urlLinkText);
	responseUrl.textContent = wikiSpeech();
	responseUrl.appendChild(urlLink);
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
				locationStory(response['infos']['maps_address'], response['infos']['wiki_extract'], response['infos']['wiki_url']);
				initMap({'lat':response['infos']['maps_lat'],'lng':response['infos']['maps_lng']}, "map")
			},
			error: function(error) {
				console.log(error);
			}
		});
		event.preventDefault();
	});

})
