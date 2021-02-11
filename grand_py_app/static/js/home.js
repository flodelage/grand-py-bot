
// -------------------- GOOGLE MAP --------------------
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

// -------------------- INITIALIZE RESPONSES --------------------
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
			return "Voici l'adresse exacte: " + address + " !";
		case "approximate":
			return "C'est un peu vague mais voilà où ça se trouve: " + address;
		case "not_found":
			return "Désolé mais je ne connais pas cet endroit.";
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
			return "C'est rare, mais là je dois reconnaitre que je n'ai rien à te raconter sur ce coin là !";
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

// --------------- DISPLAY RESPONSES ---------------
function displayUserQuestion(usrQuestion, userChatDiv) {
		const chatUserElement = document.getElementById(userChatDiv);
		const imgUser = new Image();
		imgUser.src = 'static/images/user.png';
		imgUser.className = "img-chat-user"
		const userQuest = userQuestion(usrQuestion);
		chatUserElement.prepend(imgUser, userQuest);
}

function displayAddress(addressSpeech, botChatDiv) {
	const botUserElement = document.getElementById(botChatDiv);
	const imgBot1 = new Image();
	imgBot1.src = 'static/images/mini-bot.png';
	imgBot1.className = "img-chat-bot"
	const responseAddr = responseAddress(addressSpeech);
	botUserElement.prepend(imgBot1, responseAddr);
}

function displayStory(extractSpeech, botChatDiv) {
	const botUserElement = document.getElementById(botChatDiv);
	const imgBot2 = new Image();
	imgBot2.src = 'static/images/mini-bot.png';
	imgBot2.className = "img-chat-bot"
	const responseExtr = responseExtract(extractSpeech);
	botUserElement.appendChild(imgBot2);
	botUserElement.appendChild(responseExtr);
}

function displayWikiLink(wiki_url, botChatDiv) {
	const botUserElement = document.getElementById(botChatDiv);
	const imgBot3 = new Image();
	imgBot3.src = 'static/images/mini-bot.png';
	imgBot3.className = "img-chat-bot"
	const responseLink = responseUrl(wiki_url);
	botUserElement.appendChild(imgBot3);
	botUserElement.appendChild(responseLink);
}

// -------------------- FINAL RESPONSES --------------------
function botResponses(usrQuestion, addressSpeech, extractSpeech, wiki_url,
					  locationCoordinates, mapsResp, wikiResp, mapsDiv,
					  userChatDiv, botChatDiv) {
	if (mapsResp == "not_found") {
		displayUserQuestion(usrQuestion, userChatDiv);
		displayAddress(addressSpeech, botChatDiv);
	} else {
		initMap(locationCoordinates, mapsDiv);
		displayUserQuestion(usrQuestion, userChatDiv);
		displayAddress(addressSpeech, botChatDiv);
		if (wikiResp != "none") {
			displayStory(extractSpeech, botChatDiv);
			displayWikiLink(wiki_url, botChatDiv);
		} else {
			displayStory(extractSpeech, botChatDiv);
		}
	}
}

// -------------------- AJAX --------------------
const formElement = document.querySelector("form");

$(document).ready(function() {

	formElement.addEventListener("submit", function(event) { //quand l utilisateur soumet sa saisie

		var place = $('#input_place').val(); //la saisie est stockée

		$.ajax({
			url: '/process',
			data: $('form').serialize(), //la saisie est envoyée à la méthode de l'url /process
			type: 'POST',
			success: function(response) {
				const aSpeech = addressSpeech(status=response['infos']['maps_status'],
				                              address=response['infos']['maps_address']);
				const eSpeech = extractSpeech(responseNb=response['infos']['wiki_response_nb'],
											  extract=response['infos']['wiki_extract']);
				botResponses(usrQuestion= response['infos']['user_question'],
							 addressSpeech=aSpeech,
							 extractSpeech=eSpeech,
							 wiki_url=response['infos']['wiki_url'],
							 locationCoordinates={'lat':response['infos']['maps_lat'],'lng':response['infos']['maps_lng']},
							 mapsResp=response['infos']['maps_status'],
							 wikiResp=response['infos']['wiki_response_nb'],
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
