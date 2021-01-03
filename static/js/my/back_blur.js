$('document').ready(function(){
	
	//<iframe  src="nosrcdoc.html"></iframe>
	
	function add_blur(name,connect){
		//var get_html = $('.site_full').html();
		//var get_head = $('head').html();
		
		//var input_code = `<iframe class="frame" srcdoc="<html><head>`+get_head+`</head><body><div class='blur'>`+get_html+`</div></body></html>" >error</iframe>`
		
		
		
		
		
		var input_code = `<div class="frame `+name+`"><div class='blur'></div></div>`
		//console.log(input_code)
		//console.log(get_html)
		//console.log(input_code)
		
		$(".site_copy_blur").append(input_code);
		$('.site_full').clone().appendTo('.'+name+' .blur');
		// repeat function
		function change_el() {
			// get css
			var pos_x = $(connect).offset().left
			var pos_y = $(connect).offset().top
			var size_x = $(connect).width()
			var size_y = $(connect).height()
			// check if change a element
			var check = false;
			if(cookie(name+'_top') != pos_y  || cookie(name+'_top') == undefined){
				cookie(name+'_top','give',pos_y);
				check = true;
			}
			if(cookie(name+'_left') != pos_x  || cookie(name+'_left') == undefined){
				cookie(name+'_left','give',pos_x);
				check = true;
			}
			if(cookie(name+'_width') != size_x  || cookie(name+'_width') == undefined){
				cookie(name+'_width','give',size_x);
				check = true;
			}
			if(cookie(name+'_height') != size_y  || cookie(name+'_height') == undefined){
				cookie(name+'_height','give',size_y);
				check = true;
			}
			// change elemetn
			if(check){
				$('.'+name).css({
					'height':size_y+'px',
					'width':size_x+'px',
					'top':pos_y+'px',
					'left':pos_x+'px',
				});
				$('.'+name+' > .blur').css({
					'top':(~pos_y + 1)+'px',
					'left':(~pos_x + 1)+'px',
				});
				
				
			}
		}
		
		
		setInterval(change_el, 10);
		
		
		
		
		
		
		//connect scroll
		$('body >.site_full').scroll(function() {
			var scrtop = $('body >.site_full').scrollTop();
			$('.'+name+' .site_full').scrollTop(scrtop)
		});
		
		
		
		
		
	}
	
	
	
	
	
	
	add_blur('header_blur','.header_absolute')
	add_blur('sidebar_blur','.sidebar_block')
	
	
	
	

	
	



	

	
});