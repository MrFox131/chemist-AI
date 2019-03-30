var items_in_cart = [];

if(typeof $.cookie('cart') !== "undefined"){
    items_in_cart = JSON.parse($.cookie('cart'));
    for(let i = 0; i < items_in_cart.length; i++){
		$(".add_to_cart[itemID='" + items_in_cart[i][0] + "']").addClass("selected");
	}
}
else{
    $.cookie('cart', JSON.stringify(items_in_cart), {expires: 1});
}

window.onload = function(event) {
	onResizeWindow();
	if(items_in_cart.length > 0){
		$(".cart_button__text").html("В корзине: " + items_in_cart.length);
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
}

window.onresize = function(event) {
	onResizeWindow();
};

function onResizeWindow(){
	if($(".jsFromLeft").length){
		if($(".content > .card:first").length){
			$(".jsFromLeft").attr("style", "margin-left: " + $(".content > .card:first").position().left + "px;");
		}
		if($(".content--cart > .items_in_cart").length){
			$(".jsFromLeft").attr("style", "margin-left: " + $(".content--cart > .items_in_cart").position().left + "px;");
		}
	}
	if($(".jsFromRight").length){
		if($(".content > .card:first").length){
			$(".jsFromRight").attr("style", "right: " + $(".content > .card:first").position().left + "px;");
		}
		if($(".content--cart > .items_in_cart").length){
			$(".jsFromRight").attr("style", "right: " + $(".content--cart > .items_in_cart").position().left + "px;");
		}
	}
	if($(".jsGridWidthPlus").length){
		if($(".content > .card:first").length){
			$(".jsGridWidthPlus").attr("style", $(".jsGridWidthPlus").attr("style") + "width: calc(100vw - (" + (($(".content > .card:first").position().left * 2) - 15) + "px));");
		}
	}

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
		deleteFromCart($(this).attr("itemID"));
	}
	else{
		$(this).addClass("selected");
		addToCart($(this).attr("itemID"));
	}
	if(items_in_cart.length > 0){
		$(".cart_button__text").html("В корзине: " + items_in_cart.length);
	}
	else{
		$(".cart_button__text").html("Корзина пуста");
	}
})

function addToCart(id){
	let ifExist = false;
	items_in_cart = JSON.parse($.cookie('cart'));

	for(let i = 0; i < items_in_cart.length; i++){
		if(items_in_cart[i][0] == id){
			items_in_cart[i][1]++;
			ifExist = true;
		}
	}
	if(!ifExist){
		items_in_cart.push([id, 1]);
	}

	$.cookie('cart', JSON.stringify(items_in_cart), {expires: 1});
}
function removeFromCart(id){
	items_in_cart = JSON.parse($.cookie('cart'));

	for(let i = 0; i < items_in_cart.length; i++){
		if(items_in_cart[i][0] == id){
			items_in_cart[i][1]--;
		}
		if(items_in_cart[i][1] < 1){
			items_in_cart.splice(i, 1);
		}
	}

	$.cookie('cart', JSON.stringify(items_in_cart), {expires: 1});
}
function deleteFromCart(id){
	items_in_cart = JSON.parse($.cookie('cart'));

	for(let i = 0; i < items_in_cart.length; i++){
		if(items_in_cart[i][0] == id){
			items_in_cart.splice(i, 1);
		}
	}

	$.cookie('cart', JSON.stringify(items_in_cart), {expires: 1});
}

function getAmountInCart(id){
	items_in_cart = JSON.parse($.cookie('cart'));

	for(let i = 0; i < items_in_cart.length; i++){
		if(items_in_cart[i][0] == id){
			return items_in_cart[i][1];
		}
	}
}