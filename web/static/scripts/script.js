var items_in_cart = 0;
			window.onload = function(event) {
				onResizeWindow();

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
				onResizeWindow();
			};

			function onResizeWindow(){
				$(".jsFromLeft").attr("style", "margin-left: " + $(".content > .card:first").position().left + "px;");
				$(".jsFromRight").attr("style", "right: " + $(".content > .card:first").position().left + "px;");
				$(".jsGridWidthPlus").attr("style", $(".jsGridWidthPlus").attr("style") + "width: calc(100vw - (" + (($(".content > .card:first").position().left * 2) - 15) + "px));");
				
				//Set the width and margin-left of the recommendation block
				if($(window).width() < 1450){
					$(".jsCenterForRecomend").attr("style", "min-width: 0;");
				}
				else{
					$(".jsCenterForRecomend").attr("style", "min-width: calc((250px + 15px) * 5);");
				}

				if($(window).width() < 1450){
					$(".jsCenterForRecomend").attr("style", $(".jsCenterForRecomend").attr("style") + "width: " + ($(window).width() - 120) + "px;");
					$(".jsCenterForRecomend > .horizontal_scroll").attr("style", "");
				}
				else{
					$(".jsCenterForRecomend").attr("style", $(".jsCenterForRecomend").attr("style") + "display: flex;justify-content: center;");
					$(".jsCenterForRecomend > .horizontal_scroll").attr("style", "padding-right: 0px;");
				}

				$(".jsCenterForRecomend").attr("style", $(".jsCenterForRecomend").attr("style") + "margin-left: calc(50vw - " + ($(".jsCenterForRecomend").width() / 2) + "px);");
			}

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