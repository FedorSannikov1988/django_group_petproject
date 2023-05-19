/* -------------------------------------------------------------------------------- /
	
	Magentech jQuery
	Created by Magentech
	v1.0 - 20.9.2016
	All rights reserved.
	
/ -------------------------------------------------------------------------------- */

"use strict"

	// Cart add remove functions
	var cart = {
		'add': function(product_id, quantity) {
			addProductNotice('Product added to Cart', '<img src="img/demo/shop/product/e11.jpg" alt="">', '<h3><a href="product.html">Apple Cinema 30"</a> added to <a href="cart.html">shopping cart</a>!</h3>', 'success');
		}
	}

	var wishlist = {
		'add': function(product_id) {
			addProductNotice('Product added to Wishlist', '<img src="img/demo/shop/product/e11.jpg" alt="">', '<h3>You must <a href="login.html">login</a>  to save <a href="product.html">Apple Cinema 30"</a> to your <a href="wishlist.html">wish list</a>!</h3>', 'success');
		}
	}
	var compare = {
		'add': function(product_id) {
			addProductNotice('Product added to compare', '<img src="img/demo/shop/product/e11.jpg" alt="">', '<h3>Success: You have added <a href="product.html">Apple Cinema 30"</a> to your <a href="compare.html">product comparison</a>!</h3>', 'success');
		}
	}

	/* ---------------------------------------------------
		jGrowl – jQuery alerts and message box
	-------------------------------------------------- */
	function addProductNotice(title, thumb, text, type) {
		$.jGrowl.defaults.closer = false;
		//Stop jGrowl
		//$.jGrowl.defaults.sticky = true;
		var tpl = thumb + '<h3>'+text+'</h3>';
		$.jGrowl(tpl, {		
			life: 4000,
			header: title,
			speed: 'slow',
			theme: type
		});
	}

