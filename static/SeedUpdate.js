(function worker() {
	$.ajax({
	  url: '/update', 
	  success: function(data) {
		$('#table').html(data);
	  },
	  complete: function() {
		// Schedule the next request when the current one's complete
		setTimeout(worker, 1000);
	  }
	});
  })();