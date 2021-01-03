//get mouse pos
window.addEventListener('mousemove', function(e)
{
	cur_x = e.clientX
	cur_y = e.clientY
})

// my function exist value in object or array 
function is_obj(s_arr,s_val) {
	var stop = false;
	function cycle(c_arr) {
		$.each(c_arr, function(k, v ) {
		if(!stop){
			if (typeof(v) == 'object'){
				cycle(v,s_val)
			} else {
				if(s_val == v){
					stop = true;
				}
			}
		} 
		});
	}
	cycle(s_arr)
	return stop;
}


function change_time(time,num,type){
	if(type=='dd'){
		time.setDate(time.getDate() + num); //day
	} else if(type=='ddd') {
		time.setDate(time.getDate() + num); //day
	} else if(type=='mm') {
		time.setMonth(time.getMonth() + num); //Month
	} else if(type=='yyyy') {
		time.setFullYear(time.getFullYear() + num); //Year
	} else if(type=='HH') {
		time.setHours(time.getHours() + num); //Hours
	} else if(type=='MM') {
		time.setMinutes(time.getMinutes() + num); //Minutes
	} else if(type=='ss') {
		time.setSeconds(time.getSeconds() + num); //Seconds
	}
	return time;
}








// my function walking around the array
function endless_circle(min,cur,max){
	var prev = cur - 1
	var next = cur + 1
	if (next>max){
		next = min;
	}
	if (prev<min){
		prev=max;
	}
	return [prev,next];
}

function add_icon(icon='system-none',add=false,withdraw=false,id="",){
	// fix against duplicates
	if(id != ""){
		if($("#"+id).length != 0){
			id = id + "-" + $("#"+id).length
		}
	}
html =  '<div id="'+id+'" class="'+id+' icon_block"><a class="'+icon+' "></a></div>';
	if(withdraw){
		return html;
	} else if(add){
		$(add).append(html);
	}
}

// example syntax
//var get_val = 'red[blue,-yellow]purple{<green,gray,-pink>}-black(white)brown,33';

function add_field(add,id,arr_search=false,only_arr=false,icon_name=false){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	//create html 
	var html = '';
	//var start_list = JSON.stringify({});
	html = html + '<div id="'+id+'" class="field_block"><input name="'+id+'" class="'+id+' search_field_arr" type="text" value="{}" />';
	if(icon_name){
	html = html + add_icon(icon_name,false,true);
	
	}

	html = html + '<div class="search_field_block"><div class="'+id+' cloud_tags search_field_content">';
	html = html + '<input id="'+id+'_val" class="'+id+' search_field_val" type="text" /></div><select class="'+id+' search_field_select" size="3"></select></div></div>';
	//add html
	$(add).append(html)
	//hide prompt for fast enter
	$("."+id+".search_field_select").hide()
	ani_shhi("."+id+".search_field_select",false);
	$("."+id+".search_field_select").show()




	// add a tag in array
	function get_word(){
		var get_arr = JSON.parse($("."+id+".search_field_arr").val());
		var get_val = $("."+id+".search_field_val").val();

		
		//clear and filter the line
		var text_default = get_val.match(/(?<=^|\)|]|})[^\(|[|{]+/g);
		var text_tag = get_val.match(/(?<=\[).+?(?=\])/g);
		var text_title = get_val.match(/(?<=\{).+?(?=\})/g);
		var text_author = get_val.match(/(?<=\().+?(?=\))/g);
		
		
		
		// function filter curent line
		function lvl3(way,val,connect){
			// add only those elements that are in the array arr_search
			var glitch_check = true;
			if(only_arr){
				if (arr_search.indexOf(val) != -1){
					glitch_check = true;
					} else {
					glitch_check = false;
				}
			}
			
			
			//check if already exists element in array and arr_search or if value is number
			if ((!get_arr.hasOwnProperty(val) && glitch_check) || !isNaN(Number(val)) ){
				var is_number = false;
				if (!isNaN(Number(val))){
					is_number = true
				} 
				// assemble object
				var name_key = way[1];
				var obj2 = {'type':way[0],'not':way[2],'byid':is_number};
				
				
				
				var connect_arr = [];
				//validity connect arr
				$.each(connect, function(i, v) {
					if ((!get_arr.hasOwnProperty(v) && glitch_check) || !isNaN(Number(v)) ){
						connect_arr.push(v.replace(/[^A-Za-z0-9_]/g, ""));
					}
				})
				obj2[name_key] = connect_arr;
				get_arr[val] = obj2;
				//add html
				$("#"+id+" .search_field_val").before(
					'<div id='+val+' class="'+id+' '+way[0]+' '+name_key+' not_'+way[2]+' byid_'+is_number+' tag_block"><a class="'+val+' delete_tag">X</a><a class="'+val+' text_tag">'+val+'</a></div>'
				)
				//clean field
				$("."+id+".search_field_val").val('');
			}
		}
		
		function lvl2(way,arr){
			$.each(arr, function(index2, value2 ) {
				$.each(value2.split(','), function(index22, value22 ) {
					var add_arr = value2.split(',')
					//delete duplicate
					add_arr.splice( $.inArray(value22, add_arr), 1 );
					var first = value22.slice(0,1)
					//validity value
					var word = value22.replace(/[^A-Za-z0-9_]/g, "");
					if(first=='-'){
						lvl3([way[0],way[1],true],word,add_arr);
					}
					else{
						lvl3([way[0],way[1],false],word,add_arr);
					}
				});
			});
		}

		function lvl1(way,arr){
			$.each(arr, function(index, value ) {
				var and_arr = value.match(/(?<=^|\>)[^\<]+/g);
				if(and_arr!=null){
					lvl2([way,'tag_and'],and_arr);
				}
				var or_arr = value.match(/(?<=\<).+?(?=\>)/g);
				if(or_arr!=null){
					lvl2([way,'tag_or'],or_arr);
				}
			});
		}

		// check are something
		if(text_default!=null){
			lvl1('default_name',text_default);
		}
		if(text_title!=null){
			lvl1('tag_title',text_title);
		}
		if(text_author!=null){
			lvl1('tag_author', text_author);
		}
		if(text_tag!=null){
			lvl1('tag_tag',text_tag);
		}
		
		
		//hide
		ani_shhi("."+id+".search_field_select",false);
		//save arr
		$("."+id+".search_field_arr").val(JSON.stringify(get_arr));
		console.log(get_arr);
	}


	// Action select for fast typing
	function search_val(){
		var get_val = $("."+id+".search_field_val").val();
		var first = get_val.slice(0,1)
		var word = get_val.replace(/[^A-Za-z0-9_]/g, "");
		
		var type = "";
		var opt_html = '';
		//check minus or plus
		if(first=='-'){
			type = first;
		}

		// function for find word
		var find = function (arr, find) {
		  return arr.filter(function (value) {
			 return (value + "").indexOf(find) != -1;
		  });
		};

		var find_arr = find(arr_search, word)
		// add html
		$.each(find_arr, function(index, value ) {
		opt_html = opt_html +'<option value="'+type+value+'">'+value+'</option>'
		});

		$("."+id+".search_field_select").html(opt_html);

	}

	// run adding tags
	var get_element = document.getElementById(id+'_val');
	get_element.addEventListener('keydown', function(e){
		
		// width relative to font size
		var font_size = Number($("."+id+".search_field_val").css('font-size').replace(/[^0-9]/g, ""));
		var sum = font_size * 0.55;
		var len =  $("."+id+".search_field_val").val().length;
		// Input is delayed by one symbol
		if (e.keyCode == 8){
			// delete prev tag
			if (len == 0){
				var get_id = $("."+id+".search_field_val").prev().attr('id')
				if (get_id != undefined){
					$('#'+get_id+' .delete_tag').click();
				}
			}
			len = len - 1
		} else {
			len = len + 1
		}
		var result =  len * sum;
		$("."+id+".search_field_val").css({'width':result+'px'});
		if (e.keyCode == 32 || e.keyCode == 13){
			get_word();
		} else {
			ani_shhi("."+id+".search_field_select",true);
			
			
			
			
			
			
			
			
			
			
			
			search_val();
		}
	})

	// select fast val
	$("body" ).on('change', "."+id+".search_field_select", function(e) {
		$("."+id+".search_field_val").val($(this).val());
		get_word();
		$(this).html('');
	})
	
	// click near element
	jQuery(function($){
		$(document).mouseup(function (e){ 
			var div = $("#"+id);  
			if (!div.is(e.target)  
				&& div.has(e.target).length === 0) { 
				get_word();
				
			} 
		});
	});
	
	// delete tag
	$( "body" ).on('click', '#'+id+' .delete_tag', function() {
		var class_arr = $(this).attr('class').split(' ') // get class array
		var get_arr = JSON.parse($("."+id+".search_field_arr").val());// convert in array 
		delete get_arr[class_arr[0]];
		$("."+id+".search_field_arr").val(JSON.stringify(get_arr));
		$( "#"+id+" #"+class_arr[0] ).remove();
	});
	
	// select field
	$( "body" ).on('click', '#'+id+' .search_field_block', function() {
		$('#'+id+' .search_field_val').focus()
	});
	
	
	
	
}














// function for find word
var find = function (arr, find) {
  return arr.filter(function (value) {
	 return (value['text'] + "").indexOf(find) != -1;
  });
};



function add_select(add,id, options,icon=false,search=true){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	var html = '';
	html = html + '<div id="'+id+'" class="select_block" ><select name="'+id+'" class="hide_sekect"></select><div class="show_selected_block">';
	if(icon){
		html = html + add_icon(icon,false,true);
	}
	html = html + '<div class="select_content"><div class="show_selected"></div><div class="sel_span"></div></div></div></div>';
	$(add).append(html);
	
	var show_selected ;
	var html1='',html2='',html3='';
	
	if(search){
		html2 = html2 + '<div class="search_select_block"><input  class="search_select" type="text"/></div>';
	}
	
	
	
	
	$.each(options, function(key, value) {
		
		
		
		
		var selected = '';
			if(value['selected']){
				selected = 'selected'
				show_selected = {
					'text':value['text'],
					'icon':value['icon'],
					'val': key, 
					'selected':selected   
				}
			}
		html1 = html1 + '<option '+selected+' value="'+key+'">'+value['text']+'</option>'
		
		html2 = html2 + '<div class="sel_option '+key+' sel_'+selected+'" >';
		if(value['icon']!=undefined){
			html2 = html2 + add_icon(value['icon'],false,true);
			
			
			
		}
		html2 = html2 + '<div class="sel_text">'+value['text']+'</div></div>';
	});
	
	$('#'+id+' .hide_sekect').append(html1);
	$('#'+id+' .sel_span').append(html2);
	if(show_selected!=undefined){
		if(show_selected['icon']!=undefined)
		{
			var html3 = add_icon(show_selected['icon'],false,true);
			
		}
		var html3 = html3+'<div class="sel_text">'+show_selected['text']+'</div>';
		$('#'+id+' .show_selected').append(html3);
	}
	$( "#"+id+' .sel_span' ).hide();
	ani_shhi( "#"+id+' .sel_span' ,false);
	$( "#"+id+' .sel_span' ).show();
	
	
	$( "#"+id ).hover(
	  function() {
		ani_shhi( "#"+id+' .sel_span' ,true);
	  }, function() {
		ani_shhi( "#"+id+' .sel_span' ,false);
	  }
	);
	$( "body" ).on('click', '#'+id+' .sel_option', function() {
		var class_arr = $(this).attr('class').split(' ') // get class array
		$('#'+id+' .show_selected').html($('#'+id+' .'+class_arr[0]+'.'+class_arr[1]).html())
		
		$('#'+id+' .sel_option').removeClass('sel_selected');
		$(this).addClass('sel_selected');
		$('#'+id+' .hide_sekect').val(class_arr[1]);
		
		$('#'+id+' .sel_option').show();
	});
	
	if(search){
		var get_element = $('#'+id+' .search_select').get(0);
		get_element.addEventListener('keydown', function(e){
			var word;
			if (e.keyCode == 8){
				word = $(this).val().slice(-1)
			} else {
				word = $(this).val() + e.key
			}
			
			var get_options = Object.keys(options).filter(function (el) {
			  if(options[el]['text'].indexOf(word) != -1){
				return el
			  }
			});
			
			$('#'+id+' .sel_option').hide();
			$.each(get_options, function(key, value) {
				$('#'+id+' .sel_option.'+value).show();
			});
			
			
			
			
			
		});
	}
	
	
	
}

 





















function add_checkbox(id,icon,add=false,cur=0){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	// replace icon
	icon[1] = icon[1] || icon[0] ;
	// html generation
	var html = `<div id="`+id+`" class="block_checkbox">`
	// Add icon
	$.each(icon, function(i, v ) {
		var style = (v != icon[cur]) ? `style="display:none;"` : '' ;
		html = html + `
			<div `+ style +` class="each_checkbox">
				<input class="radio_hide checkbox-`+v+`" type="radio" name="`+id+`"/>
				<div class="icon_block checkbox_icon_block block-`+v+`"><a class="`+v+`"></a></div>
			</div>
		`;
	});
	html = html + `</div>`;
	
	if(add){
		$(add).append(html);
	} else {
		return html;
	}
}
//Actions
$('document').ready(function(){
	$( "body" ).on('click', '.checkbox_icon_block', function() {
			var cur = $(this).closest('.each_checkbox');
			var next = cur.next();
			cur.hide();
			if(next.length == 0){
				var first = $(this).closest('.block_checkbox').find('.each_checkbox').first();
				first.show()
				first.find('.radio_hide').prop('checked', true);
			} else {
				next.show()
				next.find('.radio_hide').prop('checked', true);
			}
	});
});


















function add_range(add,id,min=0,max=10,step=1,icon=false,range_double=true){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	var html = '<div id="'+id+'" class="range_block">';
	if(icon){
		html = html + add_icon(icon,false,true);
		
	}
	html = html + '<div class="range_align"><div class="range_line"></div><input name="'+id+'_prev" class="range_hide range_prev" type="range" min="'+min+'" max="'+max+'" value="'+min+'" step="'+step+'" />';
	if(range_double){
		var html = html + '<input name="'+id+'_next" class="range_hide range_next" type="range" min="'+min+'" max="'+max+'" step="'+step+'" value="'+max+'" />';
	}
	html = html + '</div></div>';
	$(add).append(html);
	
	
	
	$( "body" ).on('change', '#'+id+' .range_hide', function() {
		var prev = $('#'+id+' .range_hide.range_prev') 
		var next = $('#'+id+' .range_hide.range_next')
		var prev_val = Number(prev.val());
		var next_val = Number(next.val());
		if(prev_val>=next_val){
			if($(this).hasClass('range_prev')){
				next.val(prev_val)
			} else {
				prev.val(next_val);
			}
		}
	});
}



function add_number(add,id,min=0,max=10,step=1,icon=false,range_double=true){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	var html = '<div id="'+id+'" class="number_main">';
	if(icon){
		html = html + add_icon(icon,false,true);
		
	}
	html = html + '<div class="number_content">';
	
		var html = html + '<input name="'+id+'_min" class="number_val min_number" type="number" min="'+min+'" max="'+max+'" step="'+step+'" value="'+min+'" />';
	if(range_double){
		var html = html + '<input name="'+id+'_max" class="number_val max_number" type="number" min="'+min+'" max="'+max+'" step="'+step+'" value="'+max+'" />';
	}
	html = html + '</div></div>';
	$(add).append(html);
	
	
	
	$( "body" ).on('change', '#'+id+' .number_val', function() {
		var prev = $('#'+id+' .number_val.min_number') 
		var next = $('#'+id+' .number_val.max_number')
		var prev_val = Number(prev.val());
		var next_val = Number(next.val());
		if(prev_val>=next_val){
			if($(this).hasClass('min_number')){
				next.val(prev_val)
			} else {
				prev.val(next_val);
			}
		}
	});
}

























function add_slider(add,id,windows,icon=false,cur=0,mini_buttons=true,width_pos=true,height='',position_top=true,mose_not_move=false){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	if (icon){
		icon[1] = icon[1] || icon[0] ;
	}
	
	
	
	var html = '<div id="'+id+'"class="slider_block"><div class="slider_windows">';
	$.each(windows, function(i, v ) {
		if(v['content']==undefined){
			v['content'] = '';
		}
		
		
		html = html + '<div style="height:'+height+';" id="'+v['id']+'"class="slider_window '+v['id']+'">'+v['content']+'</div>';
	});
	
	
	if(position_top){}else{}
	
	
	
	if (icon){
		
		var style_next, style_prev;
		if(position_top){
			style_next = `
				position:absolute;
				top: 50%;
				transform: translate(0%, -50%);
				right:0px;
			`;
			style_prev = `
				position:absolute;
				top: 50%;
				transform: translate(0%, -50%);
				left:0px;
			`;
		}else{
			style_next = `
				position:absolute;
				left: 50%;
				transform: translate(-50%, 0) rotate(-90deg);
				top:0px;
			`;
			style_prev = `
				position:absolute;
				left: 50%;
				transform: translate(-50%, 0) rotate(-90deg);
				bottom: 0px;
			`;
		}
		
		
		
		
		
		
		
		
		
		
		html = html + '<div style="'+style_prev+'" class="slider_but slider_prev">';
		html = html + add_icon(icon[0],false,true);
		html = html + '</div>';
		html = html + '<div style="'+style_next+'" class="slider_but slider_next">';
		html = html + add_icon(icon[1],false,true);
		html = html + '</div>';
	
	
	}
	
	
	
	
	
	
	
 
	
	
	
	
	
	
	
	html = html + '</div>';
	
	
	

	

	
	if(mini_buttons){
		html = html + '<div class="slider_buttons_block"><div class="top_scroll" ><div class="top_scroll_content"></div></div><div class="slider_buttons"><div class="slider_mini_buttons">';
		
		$.each(windows, function(i, v ) {
			var style = '';
			if(v['image']!=undefined){
				style = 'style="background-image:url('+v['image']+');"';
			}
			
			
			html = html + '<div '+style+' class="'+v['id']+' slider_mini_but">';
			if(v['icon']!=undefined){
				html = html + add_icon(v['icon'],false,true);
			} else {
				html = html + '<div class="number_slider">'+(i+1)+'</div>';
			}
			
			html = html + '<div class="click_hover"></div>';
			html = html + '</div>';
		})
		html = html + '</div></div></div>';
	}
	
	

	
	
	html = html + '</div>';
	
	$(add).append(html);
	
	var now_cur=cur
	
	var n_p = endless_circle(0,cur,windows.length-1);
	
	$('#'+id+' > div >.slider_window').hide();
	$('#'+id+' > div > #'+windows[now_cur]['id']).show();
	
	

	$( "body" ).on('click', '#'+id+' > div > .slider_but', function() {
		n_p = endless_circle(0,now_cur,windows.length-1);
		var get_class = $(this).attr('class').split(' ');
		if($(this).hasClass('slider_prev')){
			now_cur = n_p[0];
		}else if ($(this).hasClass('slider_next')){
			now_cur = n_p[1]
		}
		$('#'+id+' > div >.slider_window').hide();
		$('#'+id+' > div > #'+windows[now_cur]['id']).show();
		
	});
	$( "body" ).on('click', '#'+id+' > div > div > div > .slider_mini_but', function() {
		var cur_class = $(this).attr('class').split(' ');
		now_cur = $(this).index();
		$('#'+id+' > div >.slider_window').hide();
		$('#'+id+' > div > #'+cur_class[0]).show();
	});
	
	
	// move slider mouse
	var mouse = false;
	var intervalId, widget_size,pos;
	$( "body" ).on('mousedown', '#'+id+' > div >.slider_window ', function(e) {
		var allow_run = true;
		$.each(mose_not_move, function(i, v ) {
			if($(e.target).hasClass(v)){
			allow_run = false;
			}
		});
		if (allow_run){
			var i = $(this).attr('id');
			var m = [e.pageX,e.pageY]
			intervalId = setInterval( function() { mousedown_act(i,m); }, 100 );
			mouse = true;
		}
	})
	$( "body" ).mouseup(function(e) {
		$('#'+id+' > div >.slider_window').css({'transform':'translate(0px, 0px)'});
		if (mouse){
			clearInterval(intervalId);
			if ( widget_size > widget_size - Math.abs(poss)){
				if (poss >= 0){
					$('#'+id+' '+class_n_p[1]).click();
				} else {
					$('#'+id+' '+class_n_p[0]).click();
				}
			}
			mouse = false;
		}
	})
	
	
	
	function mousedown_act(now_id,cur_arr){
		if(width_pos){
			class_n_p = ['.slider_next','.slider_prev']
			poss=cur_x - cur_arr[0];
			widget_size = $('#'+id+' #'+now_id).width();
			$('#'+id+' #'+now_id).css({'transform':'translate('+poss+'px, 0px)'});
			
		}else {
			class_n_p = ['.slider_prev','.slider_next']
			poss=cur_y - cur_arr[1]
			widget_size = $('#'+id+' #'+now_id).height();
			$('#'+id+' #'+now_id).css({'transform':'translate(0px, '+poss+'px)'});
		}
		
		
	}
	
	if(mini_buttons){
		var scroll_width = $('#'+id+'> div > div  >.slider_mini_buttons').get(0).scrollWidth;
		$('#'+id+' > div > div > .top_scroll_content').width(scroll_width);
		$(function() {
		  $('#'+id+'> div > .top_scroll').scroll(function() {
			$('#'+id+'> div > .slider_buttons').scrollLeft($('#'+id+'> div > .top_scroll').scrollLeft());
		  });
		  $('#'+id+'> div > .slider_buttons').scroll(function() {
			$('#'+id+'> div > .top_scroll').scrollLeft($('#'+id+'> div > .slider_buttons').scrollLeft());
		  });
		});
		
		
		
		
		
		
	}
	
	
}


function add_date(add,id,time,have=[],icon=false,display='block', size=10){ 
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}

	// crate main widget
	var html = `
		<div id="`+id+`" class="date_block">
		
	`;
	
	if(icon){
		html = html + add_icon(icon,false,true);
	}
	
	html = html + '<div class="time_content"><input style="display:'+display+';" class="hide_date" type="text" /><div class="time_block"></div></div></div>';
	$(add).append(html);
	
	

	
	// settings for switching
	var tree_arr = ['prev','cur','next']
	var now = 0;
	
	$.each(have, function(i, v ) {
		var cur_format = time.format(v);
		// change format for week
		var type = "number"
		if (v=="ddd"){
		type = "text"
		}
		
		// add slider for switching between widgets
		//add,id,windows,icon=false,cur=0,mini_buttons=true,width_pos=true,height='auto',position_top=false
		add_slider(
			'#'+id+' .time_block',
			id+'-'+v,
			[{
			'id':tree_arr[0],
			'content':'<input value="'+cur_format+'" type="'+type+'" class="time_val"/>',
			},
			{
			'id':tree_arr[1],
			'content':'<input value="'+cur_format+'" type="'+type+'" class="time_val"/>',
			},
			{
			'id':tree_arr[2],
			'content':'<input value="'+cur_format+'" type="'+type+'" class="time_val"/>',
			}
			],
			['system-back-v2','system-next-v2'],
			now,
			false,
			false,
			'',
			false
		);
		// Save time for sending
		var save_time = time.format("yyyy-mm-dd HH:MM:ss");
		$('#'+id+' .hide_date').val(save_time)
		// Run change time
		$( "body" ).on('click', '#'+id+'-'+v+' .slider_but', function() {
			var num;
			if($(this).hasClass('slider_prev')){
				num = -1;
			}else if ($(this).hasClass('slider_next')){
				num = 1;
			}
			//save time
			var now_time = change_time(time,num,v)
			$('#'+id+' .hide_date').val(now_time.format("yyyy-mm-dd HH:MM:ss")).change();
		});
	});
	//var cur = tree_arr[0];
	// show widgets with time
	$( "body" ).on('change', '#'+id+' .hide_date', function() {
		var my_val = $(this).val();
		var new_time = new Date(my_val);
		$.each(have, function(i, v ) {
			$('#'+id+'-'+v+' .time_val').val(new_time.format(v));
			//var n_p = endless_circle(0,now,tree_arr.length-1);
		});
	});
	
	
}






















//Buttons
function add_button(add=false,id="",icon=false,name="", val="", class_name=""){ 
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	var html = '<button name="'+name+'" value="'+val+'" id="'+id+'" class="but_block '+class_name+'">';
	if(icon){
		html = html + add_icon(icon,false,true);
	} else {
		html = html + 'click';
	}
	html = html + '</button>';
	if(add){
		$(add).append(html);
	} else {
		return html;
	}
}

//Textarea
function add_textarea(add,id){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
// add start html
	var html, html_but;
	html = `
		<div id="`+id+`" class="text_edit_block">
			<div class="text_buttons_before"></div>
			<div class="text_content_block">
				<div class="show_text_edit">Text</div>
				<textarea class="hide_text_edit" name="`+id+`"></textarea>
			</div>
			<div class="text_buttons_after"></div>
		</div>
	`;
	$(add).append(html);
	// function add panel for buttons
	function add_panel_but(add_but,id_but){
		html_but = `
			<div id="`+id_but+`" class="text_but">
				<div class="text_but_title"></div>
				<div class="text_but_content">
				</div>
			</div>
		`
		$(add_but).append(html_but);
	}
	// a path where to add the panel
	var add_buts = '#'+id+' .text_buttons_before';
	// add panel
	add_panel_but(add_buts,'text_font_style');
	$(add_buts).append('<div id="size_block"></div>');
	add_panel_but(add_buts,'text_color');
	add_panel_but(add_buts,'text_algin');
	add_panel_but(add_buts,'text_case');
	add_panel_but(add_buts,'text_list');
	add_panel_but(add_buts,'text_indent');
	add_panel_but(add_buts,'sup_sub');
	add_panel_but(add_buts,'text_add');
	// object for add buttons
	var obj = {
		"ed_clean1":{"ql":"clean","icon":"user-surname-v2","add":'#'+id+' #text_font_style .text_but_title'},
			"ed_but_bold":{"ql":"bold","icon":"edit_text-bold","add":'#'+id+' #text_font_style .text_but_content'},
			"ed_but_italic":{"ql":"italic","icon":"edit_text-italic","add":'#'+id+' #text_font_style .text_but_content'},
			"ed_but_underline":{"ql":"underline","icon":"edit_text-underline","add":'#'+id+' #text_font_style .text_but_content'},
			"ed_but_strike":{"ql":"strike","icon":"edit_text-strike","add":'#'+id+' #text_font_style .text_but_content'},
		"ed_clean2":{"ql":"clean","icon":"edit_text-color","add":'#'+id+' #text_color .text_but_title'},
			"ed_but_color":{"ql":"color","icon":"edit_text-color_text","add":'#'+id+' #text_color .text_but_content',"value":"red"},
			"ed_but_background":{"ql":"background","icon":"edit_text-color_back","add":'#'+id+' #text_color .text_but_content',"value":"red"},
		"ed_clean3":{"ql":"clean","icon":"edit_text-sup_sub","add":'#'+id+' #sup_sub .text_but_title'},
			"ed_but_script1":{"ql":"script","icon":"edit_text-sub","add":'#'+id+' #sup_sub .text_but_content',"value":"sub"},
			"ed_but_script2":{"ql":"script","icon":"edit_text-sup","add":'#'+id+' #sup_sub .text_but_content',"value":"super"},
		"ed_but_size":{"ql":"size","icon":"edit_text-size","add":'#'+id+' #size_block',"value":"10px"},
		"ed_clean4":{"ql":"clean","icon":"format-FONT","add":'#'+id+' #text_case .text_but_title'},
			"ed_but_blockquote":{"ql":"blockquote","icon":"edit_text-quote","add":'#'+id+' #text_case .text_but_content'},
			"ed_but_code-block":{"ql":"code-block","icon":"edit_text-terminal","add":'#'+id+' #text_case .text_but_content'},
		"ed_clean5":{"ql":"clean","icon":"edit_text-list","add":'#'+id+' #text_list .text_but_title'},
			"ed_but_list1":{"ql":"list","icon":"edit_text-list_ordered","add":'#'+id+' #text_list .text_but_content',"value":"ordered"},
			"ed_but_list2":{"ql":"list","icon":"edit_text-list_bullet","add":'#'+id+' #text_list .text_but_content',"value":"bullet"},
		"ed_clean6":{"ql":"clean","icon":"edit_text-indent","add":'#'+id+' #text_indent .text_but_title'},
			"ed_but_indent1":{"ql":"indent","icon":"system-next-v2","add":'#'+id+' #text_indent .text_but_content',"value":"+1"},
			"ed_but_indent2":{"ql":"indent","icon":"system-back-v2","add":'#'+id+' #text_indent .text_but_content',"value":"-1"},
		"ed_align_justify":{"ql":"align","icon":"edit_text-paragraph","add":'#'+id+' #text_algin .text_but_title',"value":"justify"},
			"ed_align_center":{"ql":"align","icon":"edit_text-paragraph_center","add":'#'+id+' #text_algin .text_but_content',"value":"center"},
			"ed_align_right":{"ql":"align","icon":"edit_text-paragraph_right","add":'#'+id+' #text_algin .text_but_content',"value":"right"},
			"ed_align_left":{"ql":"align","icon":"edit_text-paragraph_left","add":'#'+id+' #text_algin .text_but_content',"value":""},
		"ed_clean7":{"ql":"clean","icon":"system-add","add":'#'+id+' #text_add .text_but_title'},
			"ed_link":{"ql":"link","icon":"info-link","add":'#'+id+' #text_add .text_but_content'},
			"ed_image":{"ql":"image","icon":"format-IMAGE","add":'#'+id+' #text_add .text_but_content'},
			"ed_video":{"ql":"video","icon":"format-ANIMATED","add":'#'+id+' #text_add .text_but_content'},
	};
	


	// conect to Quill
	var Size = Quill.import('attributors/style/size');
	var BlockEmbed = Quill.import('blots/block/embed');

	
	// generate html buttons
	$.each(obj, function(key, value ) {
		var get_icon = add_icon(value['icon'],false,true);
		var get_html = '<div id="'+key+'" class="text_but_block" ><button  class="text_edit_button ql-'+value['ql']+'">'+get_icon+'</button></div>';
		$(value['add']).append(get_html);
		// check exist value
		if(value['value'] !== undefined){
			$('#'+id+' #'+key+' .text_edit_button').val(value['value']);
			$('#'+id+' #'+key).append('<div class="'+key+' text_edit_val" ><input value="'+value['value']+'" /></div>');
			$( "body" ).on('change', '#'+id+' #'+key+' .text_edit_val > input', function() {
				$('#'+id+' #'+key+' .text_edit_button').val($(this).val());
				if(value['ql'] == "size"){
					Size.whitelist = [$(this).val()];
				}
			});
		}
	});
	// conect Quill to block
	Quill.register(Size, true);  
	var quill = new Quill('#'+id+'   .show_text_edit', {
		modules: { toolbar: '#'+id+'   .text_buttons_before' }
	});
	// add another buttons
	add_button('#'+id+' #text_add .text_but_content','text_add_tag','post-tags')
	add_button('#'+id+' #text_add .text_but_content','text_add_user','user-user')
	add_button('#'+id+' #text_add .text_but_content','text_add_post','system-page')
	add_button('#'+id+' #text_case .text_but_content','text_spoiler','edit_text-spoiler_off')
	
	
	add_checkbox(
		'text_show_textarea',
		['info-views_off','info-views_on'],
		'#'+id+' .text_buttons_after'
	);
	add_button('#'+id+' .text_buttons_after','text_run_textarea','system-send-v3',"text_edit_run_but")
	// Actions
	// add html code to textarea
	$('#'+id).on('click',  '#text_show_textarea, #text_run_textarea', function() {
		var val_html = $('#'+id+' .ql-editor').html();
		$('#'+id+' .hide_text_edit').val(val_html)
		
		if($(this).is( "#text_show_textarea" )){
			$('#'+id+' .hide_text_edit').toggleClass('hide_text_edit'+'_act');
			$('#'+id+' .show_text_edit').toggleClass('show_text_edit'+'_act');
		}
	});
	// Widget with castom html
	class GHTML extends BlockEmbed { 
		static create(value) {
			let node = super.create();
			node.innerHTML = value[0];
			node.setAttribute('class', value[1]);
			return node;
		}
		static value(node) {
			return node.innerHTML;
		}
	} 
	GHTML.blotName = 'ghtml';
	GHTML.tagName = 'div';
	Quill.register(GHTML);
	
	
	
	// botton action add to ql-editor
	$('#'+id).on('click',  '#text_spoiler, #text_add_tag, #text_add_user, #text_add_post' , function(e) {
		// off buttons
		e.preventDefault();
		e.stopPropagation();
		var my_html ;
		// check selected text
		let range = quill.getSelection();
		if (range) {
			if (range.length == 0) {
				console.log('NO INDEX', range.index);
			} else {
				// get selected text
				var get_text = quill.getText(range.index, range.length);
				
				
				my_html = get_text; 
				if($(this).is("#text_add_tag")){
					my_class = 'tag_block_cast';
				} else if($(this).is("#text_add_user")){
					my_class = 'user_block_cast';
				} else if($(this).is("#text_add_post")){
					my_class = 'post_block_cast';
				}
				else if($(this).is("#text_spoiler")){
					// enter title
					var title = prompt('Enter title');
					// get checkbox
					var icon_spoiler = add_checkbox(
						'icon_spoiler',
						['info-views_off','info-views_on'],
					);
					// create html
					my_html = icon_spoiler+'<div class="spoiler_title">'+title+'</div><div class="spoiler_content" style="height:0px;">'+get_text+'</div>';
					my_class = 'spoiler_block';
				}  
				
				// delete old text
				quill.deleteText(range.index, range.length);
				
				
				//add html
				quill.insertEmbed(
					range.index, //INDEX_WHERE_YOU_TO_INSERT_THE_CONTENT, 
					'ghtml',//THE NAME OF YOUR CUSTOM TAG
					[my_html,my_class]// THE CONTENT YOUR TO INSERT 
				);
				
				
				
			}
		} else {
			console.log('NO TEXT');
		}
		
	})
	
	
	
	
}
$('document').ready(function(){
	$( "body" ).on('click', '#icon_spoiler', function() {
		var cur_text  = $(this).closest('.spoiler_block').find('.spoiler_content');
		cur_text.toggleClass('spoiler_content_act');
		if(cur_text.hasClass( "spoiler_content_act" )){
			ani_shhi(cur_text,true);
		} else {
			ani_shhi(cur_text,false);
		}
	});
});





//castom input
function add_input(add,id,type="text",name="",val="",icon_name=false,but_icon=false){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	var html = '<div id="'+id+'" class="s_input_block">';
	if(icon_name){
	html = html + add_icon(icon_name,false,true);
	}
	html = html + '<input value="'+val+'"name="'+name+'" type="'+type+'">';
	if(but_icon){
	html = html + add_button(false,"but_field",but_icon,name+'_but', 'val')
	}
	html = html + '</div>';
	
	$(add).append(html);
}



//show block
function add_show_block(add=false,id="",icon_header=false,content="",icon_footer=false){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	var html = '<div id="'+id+'"class="show_block">';
		//show header show
		html = html + '<div class="show_header">';
			if(icon_header){
				html = html + add_icon(icon_header,false,true);
			}else{
				html = html + 'click';
			}
		html = html + "</div>"
		// show content
		html = html + '<div class="show_content" style="height:0px;">';
			html = html + content;
		html = html + "</div>"
		// show footer
		html = html + '<div class="show_footer">';
			if(icon_footer){
				html = html + add_icon(icon_footer,false,true);
			}
		html = html + "</div>"
	html = html + "</div>"
	
	if(add){
		$(add).append(html);
	} else{
		return html;
	}
	
	
	$( "body" ).on('click', '.show_header', function() {
		var this_el = $(this).closest('.show_block').find('.show_content');
		this_el.toggleClass('show_header_act');
		if(this_el.hasClass( "show_header_act" )){
			ani_shhi(this_el,true);
		} else {
			ani_shhi(this_el,false);
		}
	});
}










function add_exradio(add,id,select_html,name,class_name, size=[100],selected=false,color=false){
	// fix against duplicates
	if($("#"+id).length != 0){
		id = id + "-" + $("#"+id).length
	}
	size[1] = size[1] || size[0];


	var html = '<div id="'+id+'" class="'+id+' exs_main"><div class="hid_select">'+select_html+'</div>';
	if(color){
		var colors = color.split(',');
		colors[1] = colors[1] || '#22222e';
		html = html + `
		<div class="color_change_select">
			<input value="`+colors[0]+`" name="`+name+`_text" class="color_select_text" type="color" />
			<input value="`+colors[1]+`" name="`+name+`_back" class="color_select_back" type="color" />
		</div>`;
	}
	html = html + '<div class="hid_radio"></div></div>';
	$(add).append(html);



			
			
			
			
	$("#"+id+' .hid_select option').each(function( index ) {
		var val = $(this).val();
		var id_radio = id+"-"+val;
		
		var check = '';

		if(selected){
			if(selected==val){
				check = 'checked';
			}
		}else{
			if ($(this).prop('selected') == true) {
				check = 'checked';
			}
		}
		
		
		
		var rad_html = `
		<div>
			<input `+check+` id="`+id_radio+`" class="hide_radio" name="`+name+`" type="radio" value="`+val+`" />
			<label style="width:`+size[0]+`px;height:`+size[1]+`px;font-size:`+size[0]+`px;" for="`+id_radio+`" class="front_label `+class_name+val+`">
			<div class="background_label_color"></div>
			</label>
		</div>
		`;
		$("#"+id+' .hid_radio').append(rad_html);
	});


}

$('document').ready(function(){
	$("body" ).on('change', ".color_select_text", function(e) {
		$(this).closest('.exs_main').find('.front_label').css('color',$(this).val());
	});
	$("body" ).on('change', ".color_select_back", function(e) {
		console.log($(this).val());
		$(this).closest('.exs_main').find('.front_label').css('background',$(this).val());
	});
});




//id = id + "-" + $("#"+id).length









