(function($) {

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	// loader
	var loader = function() {
		setTimeout(function() { 
			if($('#ftco-loader').length > 0) {
				$('#ftco-loader').removeClass('show');
			}
		}, 1);
	};
	loader();
	var carousel = function() {
		$('.home-slider').owlCarousel({
			loop:true,
			autoplay: true,
			margin:0,
			animateOut: 'fadeOut',
			animateIn: 'fadeIn',
			nav:false,
			autoplayHoverPause: false,
			items: 1,
			navText : ["<span class='ion-md-arrow-back'></span>","<span class='ion-chevron-right'></span>"],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:1
				},
				1000:{
					items:1
				}
			}
		});
	}; 

	carousel();

})(jQuery);
