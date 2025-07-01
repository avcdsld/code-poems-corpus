function adjustPlayerHeights(){
	if( Foundation.MediaQuery.atLeast('medium') ) {
		var left = $('div#amplitude-left').width();
		var bottom = $('div#player-left-bottom').outerHeight();
		$('#amplitude-right').css('height', ( left + bottom )+'px');
	}else{
		$('#amplitude-right').css('height', 'initial');
	}
}