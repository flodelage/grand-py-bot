
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
// user question
function userQuestionSpeech(usrQuestion) {
	return usrQuestion;
}

function userQuestion(usrQuestion) {
	const userQuestion = document.createElement("p");
	userQuestion.className = "chat-bubble-user";
	userQuestion.textContent = usrQuestion;
	return userQuestion;
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

function responseAddress(adrSpeech) {
	const responseAddress = document.createElement("p");
	responseAddress.className = "chat-bubble-bot";
	responseAddress.textContent = adrSpeech;
	return responseAddress;
}

// extract
function extractSpeech(responseNb, extract) {
	switch (responseNb) {
		case "many":
			return "Je connais pas mal d'histoires sur ce quartier, par exemple: " + extract;
		case "one":
			return "Je connais une histoire sur ce quartier: " + extract;
		case "none":
			return "Désolé mais je ne connais pas du tout ce coin là !";
	}
}

function responseExtract(extrSpeech) {
	const responseExtract = document.createElement("p");
	responseExtract.className = "chat-bubble-bot";
	responseExtract.textContent = extrSpeech;
	return responseExtract;
}

// wiki link
function wikiSpeech() {
	return "Si jamais tu veux en savoir plus, n'hésite pas à cliquer sur ce lien vers ";
}

function responseUrl(wiki_url) {
	const responseUrl = document.createElement("p");
	responseUrl.className = "chat-bubble-bot";
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
function botResponses(usrQuestion, addressSpeech, extractSpeech, wiki_url, locationCoordinates, mapsDiv, userChatDiv, botChatDiv) {
	initMap(locationCoordinates, mapsDiv);

	const chatUserElement = document.getElementById(userChatDiv);
	const userQuest = userQuestion(usrQuestion);
	chatUserElement.appendChild(userQuest);

	const imgBot1 = new Image();
	imgBot1.src = 'static/images/mini-bot.png';
	imgBot1.className = "img-chat-bot"
	const botUserElement = document.getElementById(botChatDiv);
	const responseAddr = responseAddress(addressSpeech);
	botUserElement.prepend(imgBot1, responseAddr);

	const imgBot2 = new Image();
	imgBot2.src = 'static/images/mini-bot.png';
	imgBot2.className = "img-chat-bot"
	const responseExtr = responseExtract(extractSpeech);
	botUserElement.appendChild(imgBot2);
	botUserElement.appendChild(responseExtr);

	const imgBot3 = new Image();
	imgBot3.src = 'static/images/mini-bot.png';
	imgBot3.className = "img-chat-bot"
	const responseLink = responseUrl(wiki_url);
	botUserElement.appendChild(imgBot3);
	botUserElement.appendChild(responseLink);
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
				const aSpeech = addressSpeech(status=response['infos']['maps_status'],address=response['infos']['maps_address']);
				const eSpeech = extractSpeech(responseNb=response['infos']['wiki_response_nb'],extract=response['infos']['wiki_extract']);
				botResponses(usrQuestion= response['infos']['user_question'],
							 addressSpeech=aSpeech,
							 extractSpeech=eSpeech,
							 wiki_url=response['infos']['wiki_url'],
							 locationCoordinates={'lat':response['infos']['maps_lat'],'lng':response['infos']['maps_lng']},
							 mapsDiv="map",
							 userChatDiv="chat-user",
							 botChatDiv="chat-bot");
			},
			error: function(error) {
				console.log(error);
			}
		});
		event.preventDefault();
	});

})
