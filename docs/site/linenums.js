/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */

/** This JavaScript code allows users to click a moon or sun symbol to
 * toggle the colors of an HTML document between dark and light mode. To
 * use this code in an HTML document, the document must do the following:
 *
 * 1. Import this file:  <script src="../site/linenums.js"></script>
 *
 * 2. Contain at least one pre with class="linenums":
 *    <pre class="linenums"></pre>
 */

"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.linenums = {
	addLineNumbers : function() {
		const newline = /<br>|\n/g;
		const elems = document.getElementsByClassName('linenums');
		for (let i = 0;  i < elems.length;  ++i) {
			let elem = elems[i];
			let text = elem.nextElementSibling.innerHTML;
			let count = text.split(newline).length;
			let linenums = '';
			let sep = '';
			for (let n = 1;  n <= count;  ++n) {
				linenums += sep + n;
				sep = '\n';
			}
			elem.innerText = linenums;
		}
	}
};

window.addEventListener("DOMContentLoaded", cse111.linenums.addLineNumbers);
