
// --------------- GOOGLE MAP ---------------
function initMap(locationCoordinates, div) {
	// Initialize and add the map
	const map = new google.maps.Map(document.getElementById(div), {
	  zoom: 17,
	  center: locationCoordinates,
	});
	// The marker, positioned at location_coordinates
	const marker = new google.maps.Marker({
	  position: locationCoordinates,
	  map: map,
	});
}

// --------------- BOT'S RESPONSES ---------------
function userRequestSpeech(user_request) {
	return "Je connais " + user_request + " !";
}
// address
function addressSpeech(status, address) {
	switch (status) {
		case "accurate":
			return "Voici l'adresse: " + address + " !";
		case "approximate":
			return "C'est un peu vague";
		case "not_found":
			return "Désolé mais je ne trouve pas";
	}
}

function responseAddress(speech) {
	const responseAddress = document.createElement("p");
	responseAddress.className = "response-address";
	responseAddress.textContent = speech;
	return responseAddress;
}
// extract
function extractSpeech(extract) {
	return "Je t'ai déjà parlé de ce quartier ? " + extract;
}

function responseExtract(extract) {
	const responseExtract = document.createElement("p");
	responseExtract.className = "response-extract";
	responseExtract.textContent = extractSpeech(extract);
	return responseExtract;
}
// wiki link
function wikiSpeech() {
	return "Si tu veux en savoir plus n'hésite pas à consulter cette page ";
}

function responseUrl(wiki_url) {
	const responseUrl = document.createElement("p");
	responseUrl.className = "response-url";
	const urlLink = document.createElement("a");
	urlLink.className = "url-link";
	const urlLinkText = document.createTextNode("Wikipédia");
	urlLink.setAttribute('href', wiki_url);
	urlLink.setAttribute('target', '_blank');
	urlLink.appendChild(urlLinkText);
	responseUrl.textContent = wikiSpeech();
	responseUrl.appendChild(urlLink);
	return responseUrl;
}
// all responses
function botResponses(speech, extract, wiki_url, locationCoordinates, mapsDiv, responsesDiv) {
	initMap(locationCoordinates, mapsDiv);
	const responseElement = document.getElementById(responsesDiv);
	const responseAddr = responseAddress(speech);
	const responseExtr = responseExtract(extract);
	const responseLink = responseUrl(wiki_url);

	responseElement.prepend(responseAddr);
	responseElement.appendChild(responseExtr);
	responseElement.appendChild(responseLink);
}

// --------------- AJAX ---------------
const formElement = document.querySelector("form");

$(document).ready(function() {

	formElement.addEventListener("submit", function(event) { //quand l utilisateur soumet sa saisie

		var place = $('#input_place').val(); //la saisie est stockée

		$.ajax({
			url: '/process',
			data: $('form').serialize(), //la saisie est envoyée à la méthode de l'url /process
			type: 'POST',
			success: function(response) {
				const adrsSpeech = addressSpeech(status=response['infos']['maps_status'],address=response['infos']['maps_address']);
				botResponses(speech=adrsSpeech,
							 extract=response['infos']['wiki_extract'],
							 wiki_url=response['infos']['wiki_url'],
							 locationCoordinates={'lat':response['infos']['maps_lat'],'lng':response['infos']['maps_lng']},
							 mapsDiv="map",
							 responsesDiv="response");
			},
			error: function(error) {
				console.log(error);
			}
		});
		event.preventDefault();
	});

})
