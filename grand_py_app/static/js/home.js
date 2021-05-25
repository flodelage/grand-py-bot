
// -------------------- GOOGLE MAPS --------------------
function initMap(locationCoordinates, div) {
	/**
 	 * displays the map in the given div
	 * from the given coordinates
 	 */
	// Initialize and add the map to the given div
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
// --- user question ---
function userQuestionSpeech(usrQuestion) {
	/**
	 * return the user question
 	 */
	return usrQuestion;
}

function userQuestion(usrQuestion) {
	/**
	 * Creates <p> and adds the user question
 	 */
	const userQuestion = document.createElement("p");
	userQuestion.className = "chat-bubble-user";
	userQuestion.textContent = usrQuestion;
	return userQuestion;
}

// --- address ---
function addressSpeech(status, address) {
	/**
	 * Determines the bot's response about the address
	 * based on the API return
 	 */
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
	/**
	 * Creates <p> and adds the response about the story
 	 */
	const responseAddress = document.createElement("p");
	responseAddress.className = "chat-bubble-bot";
	responseAddress.textContent = adrSpeech;
	return responseAddress;
}

// --- extract ---
function extractSpeech(responseNb, extract) {
	/**
	 * Determines the bot's response about the story
	 * based on the API return
 	 */
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
	/**
	 * Creates <p> and adds the response about the story
 	 */
	const responseExtract = document.createElement("p");
	responseExtract.className = "chat-bubble-bot";
	responseExtract.textContent = extrSpeech;
	return responseExtract;
}

// --- wiki link ---
function wikiSpeech() {
	/**
	 * return the beginning of the answer about the url
 	 */
	return "Si jamais tu veux en savoir plus, n'hésite pas à cliquer sur ce lien vers ";
}

function responseUrl(wiki_url) {
	/**
	 * Creates <p> and adds the response about the url
	 * Creates <a> which sends to the url on a new web page
 	 */
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

// -------------------- DISPLAY RESPONSES --------------------
// --- user question ---
function displayUserQuestion(usrQuestion, userChatDiv) {
	/**
	 * add the user's icon and question into the dedicated div
 	 */
	const chatUserElement = document.getElementById(userChatDiv);
	const imgUser = new Image();
	imgUser.src = 'static/images/user.png';
	imgUser.className = "img-chat-user"
	const userQuest = userQuestion(usrQuestion);
	chatUserElement.prepend(imgUser, userQuest);
}

// --- address ---
function displayAddress(addressSpeech, botChatDiv) {
	/**
	 * add the bot's image and the address response into the dedicated div
 	 */
	const botUserElement = document.getElementById(botChatDiv);
	const imgBot1 = new Image();
	imgBot1.src = 'static/images/mini-bot.png';
	imgBot1.className = "img-chat-bot"
	const responseAddr = responseAddress(addressSpeech);
	botUserElement.prepend(imgBot1, responseAddr);
}

// --- extract ---
function displayStory(extractSpeech, botChatDiv) {
	/**
	 * add the bot's image and the story response into the dedicated div
 	 */
	const botUserElement = document.getElementById(botChatDiv);
	const imgBot2 = new Image();
	imgBot2.src = 'static/images/mini-bot.png';
	imgBot2.className = "img-chat-bot"
	const responseExtr = responseExtract(extractSpeech);
	botUserElement.appendChild(imgBot2);
	botUserElement.appendChild(responseExtr);
}

// --- wiki url ---
function displayWikiLink(wiki_url, botChatDiv) {
	/**
	 * add the bot's image and the wiki url response into the dedicated div
 	 */
	const botUserElement = document.getElementById(botChatDiv);
	const imgBot3 = new Image();
	imgBot3.src = 'static/images/mini-bot.png';
	imgBot3.className = "img-chat-bot"
	const responseLink = responseUrl(wiki_url);
	botUserElement.appendChild(imgBot3);
	botUserElement.appendChild(responseLink);
}

// -------------------- LOADER --------------------
function displayLoader(botChatDiv) {
	/**
	 * create a div containing a loader which precedes the bot responses
 	 */
	const botUserElement = document.getElementById(botChatDiv);
	const loader = document.createElement("div");
	loader.className = "loader";
	loader.setAttribute("id","loader");
	botUserElement.prepend(loader);
}

// -------------------- FINAL RESPONSES --------------------
function botResponses(usrQuestion, addressSpeech, extractSpeech, wiki_url,
					  locationCoordinates, mapsResp, wikiResp, mapsDiv,
					  userChatDiv, botChatDiv) {
	/**
	 * Set up all the dialogues between the user and
	 * the bot by adding a delay between each response
 	 */
	displayLoader(botChatDiv);
	if (mapsResp == "not_found") {
		displayUserQuestion(usrQuestion, userChatDiv);
		setTimeout(function() {displayAddress(addressSpeech, botChatDiv);},1500);
	} else {
		displayUserQuestion(usrQuestion, userChatDiv);
		setTimeout(function() {displayAddress(addressSpeech, botChatDiv);},1500);
		setTimeout(function() {initMap(locationCoordinates, mapsDiv);},2500);
		if (wikiResp != "none") {
			setTimeout(function() {displayStory(extractSpeech, botChatDiv);},3500);
			setTimeout(function() {displayWikiLink(wiki_url, botChatDiv);},4500);
		} else {
			setTimeout(function() {displayStory(extractSpeech, botChatDiv);},3500);
		}
	}
}

// -------------------- AJAX --------------------
const formElement = document.querySelector("form");

$(document).ready(function() {
	/**
	 * Select the user input form
 	 */
	formElement.addEventListener("submit", function(event) {
	/**
	 * When submitting, user input is sent to the process() view
 	 */
		$.ajax({
			url: '/process',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
				/**
				 * Set up the display of the dialogs from the process() view response
				 */
				const aSpeech = addressSpeech(status=response['infos']['maps_status'],
				                              address=response['infos']['maps_address']);
				const eSpeech = extractSpeech(responseNb=response['infos']['wiki_response_nb'],
											  extract=response['infos']['wiki_extract']);

				botResponses(
					usrQuestion= response['infos']['user_question'],
					addressSpeech=aSpeech,
					extractSpeech=eSpeech,
					wiki_url=response['infos']['wiki_url'],
					locationCoordinates={'lat':response['infos']['maps_lat'],'lng':response['infos']['maps_lng']},
					mapsResp=response['infos']['maps_status'],
					wikiResp=response['infos']['wiki_response_nb'],
					mapsDiv="map",
					userChatDiv="chat-user",
					botChatDiv="chat-bot"
				);

				setTimeout(function() {$('#loader').addClass("hide-loader");}, 1500);

			},
			error: function(error) {
				console.log(error);
			}
		});
		event.preventDefault();
	});

})
