var items_in_cart = 0;
			window.onload = function(event) {
				$(".jsFromLeft").attr("style", "margin-left: " + $(".content > .card:first").position().left + "px;");
				$(".jsFromRight").attr("style", "right: " + $(".content > .card:first").position().left + "px;");
				$(".jsGridWidth").attr("style", $(".jsGridWidth").attr("style") + "width: calc(100vw - (" + ($(".content > .card:first").position().left * 2) + "px));");
				$(".jsGridWidthPlus").attr("style", $(".jsGridWidthPlus").attr("style") + "width: calc(100vw - (" + (($(".content > .card:first").position().left * 2) - 15) + "px));");

				if(items_in_cart > 0){
					$(".cart_button__text").html("В корзине: " + items_in_cart);
				}
				else{
					$(".cart_button__text").html("Корзина пуста");
				}
			};

			window.onscroll = function() {
			  var scrolled = window.pageYOffset || document.documentElement.scrollTop;
			  var margin = 75 - scrolled;
			  if(margin < 0) margin = 0;
			  $(".menu").attr("style", "top: " + margin + "px");
			  console.log(scrolled);
			}

			window.onresize = function(event) {
				$(".jsFromLeft").attr("style", "margin-left: " + $(".content > .card:first").position().left + "px;");
				$(".jsFromRight").attr("style", "right: " + $(".content > .card:first").position().left + "px;");
				$(".jsGridWidthPlus").attr("style", $(".jsGridWidthPlus").attr("style") + "width: calc(100vw - (" + (($(".content > .card:first").position().left * 2) - 15) + "px));");
			};

			$(".add_to_cart").on("click", function(){
				if($(this).hasClass("selected")){
					$(this).removeClass("selected");
					items_in_cart--;
				}
				else{
					$(this).addClass("selected");
					items_in_cart++;
				}

				if(items_in_cart > 0){
					$(".cart_button__text").html("В корзине: " + items_in_cart);
				}
				else{
					$(".cart_button__text").html("Корзина пуста");
				}
			})