
$(document).ready(function() {

	$('#form-place').submit(function( event ) { //quand l utilisateur soumet sa saisie
		var place = $('#input_place').val(); //la saisie est stockée

		$.ajax({
			url: '/process',
			data: $('form').serialize(), //la saisie est envoyée à la méthode de l'url /process
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
		event.preventDefault();
	});

});
