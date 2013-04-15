(function($) {
  $.fn.fullBg = function(options){
    var bgImg = $(this);		
    console.log("w",bgImg.width());

    function resizeImg() {
      var imgwidth = bgImg.width();
      var imgheight = bgImg.height();
			
      var winwidth = $(window).width();
      var winheight = $(window).height();
		
      var widthratio = winwidth / imgwidth;
      var heightratio = winheight / imgheight;
			
      var widthdiff = heightratio * imgwidth;
      var heightdiff = widthratio * imgheight;
		
      if(heightdiff>winheight) {
        bgImg.css({
          width: winwidth+'px',
          height: heightdiff+'px'
        });
      } else {
        bgImg.css({
          width: widthdiff+'px',
          height: winheight+'px'
        });		
      }
    } 
    resizeImg();
    $(options.to).resize(function() {
      resizeImg();
    }); 
  };
})(jQuery)