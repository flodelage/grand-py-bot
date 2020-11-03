
$(function(){
	$('button').click(function(){
		var place = $('#input_place').val();
		$.ajax({
			url: '/place',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});