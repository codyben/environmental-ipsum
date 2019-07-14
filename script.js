function switchItBack()
{
	$("#e").css('visibility', 'hidden');	
}

function copyMe()
{
	var snackbarContainer = document.querySelector('#demo-toast-example');
	var showToastButton = document.querySelector('#demo-show-toast'); //copy pasta code from getmdl.io
	var data = {message: 'Successfully copied ipsum to clipboard'};
    snackbarContainer.MaterialSnackbar.showSnackbar(data);
}

$( document ).ready(function(){
	
	new ClipboardJS("#c");

	$("#sB").click(function() {
		n = $("#nP").val();
		$.post( "ipsum.php", {"n":n},function( data ) {
		  if(data.request) {
		  	$("#eI").empty().append(data.ipsum);
		  	$(".returnContent").css('visibility','visible');
		  	$("#e").css('visibility', 'hidden');
		  }
		  else {
		  	$("#e").css('visibility', 'visible');
		  	setTimeout(switchItBack,500);
		  }
		});
	});
});