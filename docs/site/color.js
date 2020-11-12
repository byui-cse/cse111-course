/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */

/** This JavaScript code allows users to click a moon or sun symbol to
 * toggle the colors of an HTML document between dark and light mode. To
 * use this code in an HTML document, the document must do the following:
 *
 * 1. Import this file:  <script src="../site/color.js"></script>
 *
 * 2. Contain at least one div with class="colorCtrl":
 *    <div class="colorCtrl">&nbsp;</div>
 *    This div will contain the moon or sun symbol that the user will
 *    click to toggle dark and light modes.
 */

"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.color = {
	addSchemeHandler : function() {
		let dark = 'dark';
		let light = 'light';
		let schemeData = {
			dark: {remove:light, symbol:'\u263c', title:'Change to light mode'},
			light: {remove:dark, symbol:'\u263e', title:'Change to dark mode'}
		};

		/** Sets the color scheme. */
		let set = function(clist, scheme) {
			let data = schemeData[scheme];

			// Store the chosen color scheme
			// (light or dark) in local storage.
			localStorage.setItem('colorScheme', scheme);

			// Change the classList for the document body.
			clist.remove(data.remove);
			clist.add(scheme);

			// Change the title and symbol for
			// all color controls in the document.
			let ctrls = document.getElementsByClassName('colorCtrl');
			for (let c = 0;  c < ctrls.length;  ++c) {
				let elem = ctrls[c];
				elem.setAttribute('title', data.title);
				elem.innerHTML = data.symbol;
			}
		};

		/** Toggles the color scheme from light to dark and vice versa. */
		let toggle = function(event) {
			let clist = document.body.classList;
			let scheme = clist.contains(dark) ? light : dark;
			set(clist, scheme);
		};

		// Set the color scheme to the one
		// most recently chosen by the user.
		let clist = document.body.classList;
		let scheme = localStorage.getItem('colorScheme');
		if (!scheme) {
			scheme = clist.contains(dark) ? dark : light;
		}
		set(clist, scheme);

		// Add the toggle function as a click handler
		// to all color controls in the document.
		let ctrls = document.getElementsByClassName('colorCtrl');
		for (let c = 0;  c < ctrls.length;  ++c) {
			ctrls[c].addEventListener('click', toggle);
		}
	}
};

window.addEventListener("DOMContentLoaded", cse111.color.addSchemeHandler);
