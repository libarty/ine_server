function hover_info(id,text=false,first="."){
	$('.footer').append('<div class="footer_content '+id+'_info" style="display:none;" >'+text+'</div>')
	$(first+id).hover(
	  function() {
		$('.footer_content').hide()
		$('.'+id+'_info').show()
	  }, function() {
		$('.footer_content').hide()
		$('.footer_standart').show()
	  }
	);
}


