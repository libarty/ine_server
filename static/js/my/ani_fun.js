//my function for smooth hiding block
function ani_shhi(name, show=true,haight=true){
	var scroll_size;
	if (show){
		$(name).css('border-width', '');
		if (haight){
			scroll_size = $(name).get(0).scrollHeight;
			$(name).css('height', scroll_size);
			
		} else {
			scroll_size = $(name).get(0).scrollWidth;
			$(name).css('width', scroll_size);
		}
	} else {
		$(name).css('border-width', '0px');
		if (haight){
			$(name).css('height', 0);
		} else {
			$(name).css('width', 0);
		}
	}
}


//my button for action css
function click_act(name, act=[], set_name=false,switch_as=false){
	if (act.length) {
		set_name = set_name || act[0];
	} else {
		act = [name];
		set_name = set_name || name;
	}
	$('.'+name).on('click', function(e){
		if(!act){
			act = name;
		}
		$.each(act, function(key, value ) {
			$('.'+act).toggleClass(set_name+'_act')
			if(switch_as){
				if($('.'+act).hasClass(set_name+'_act')){
					$('.'+act).removeClass(set_name+'_pas')
				} else {
					$('.'+act).addClass(set_name+'_pas')
				}
			}
		});
		
	})
}


//my function check browser width or height change
function check_win(type=false, size=1000){
	var curent_size=(type)?window.innerHeight:window.innerWidth;
	return (curent_size <= size)?true:false
}