/*
My code cookie
Why I save all code in the hidden textarea?
Sometine the browser does not read cookie files.
I don't know why.
*/

$('body').append('<textarea style="display:none;" id="cookie">{}</textarea>');
function cookie(key,order='get',code=false){
	var obj = $('#cookie').val();
	if(obj){
		obj = JSON.parse(obj);
		if(order=='get'){
			return obj[key];
		}else if(order=='give'){
			obj[key] = code;
			$('#cookie').val(JSON.stringify(obj));
		}else if(order='del'){
			delete obj[key];
			$('#cookie').val(JSON.stringify(obj));
			
		}
	}
	
}
	// cookie('test','give','sdfsdfsdfsdf');
	// console.log(cookie('test'));
	// cookie('test','del');
	// console.log(cookie('test'));

