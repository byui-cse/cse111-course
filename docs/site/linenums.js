/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */

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
			let code = elem.nextElementSibling.innerHTML;
			let count = code.split(newline).length;
			let linenums = '';
			let sep = '';
			for (let n = 1;  n <= count;  ++n) {
				linenums += sep + '<span>' + n + '</span>';
				sep = '\n';
			}
			elem.innerHTML = linenums;
		}
	},

	addCrossRefs : function() {
		let getNumbers = function(target) {
			const space = /(\s|&nbsp;|<br>)+/g;

			// Notice the dash and en dash in the character class.
			const dash = /[-–]|&ndash;/;

			let text = target.innerText;
			let candidates = text.split(space);
			let numbers = [];
			for (let i = 0;  i < candidates.length;  ++i) {
				let candidate = candidates[i];
				if (dash.test(candidate)) {
					let limits = candidate.split(dash);
					let start = parseInt(limits[0]);
					let end = parseInt(limits[1]);
					if (! (Number.isNaN(start) || Number.isNaN(start))) {
						for (let j = start;  j <= end;  ++j) {
							numbers.push(j);
						}
					}
				}
				else {
					let linenum = parseInt(candidate);
					if (! Number.isNaN(linenum)) {
						numbers.push(linenum);
					}
				}
			}
			return numbers;
		};

		let getElements = function(target) {
			let refId = target.getAttribute('data-ref');
			let code = document.getElementById(refId);
			let linenums = code.previousElementSibling;
			return linenums.children;
		};

		let getByContent = function(elements, content) {
			let found;
			for (let i = 0;  i < elements.length;  ++i) {
				let elem = elements[i];
				if (elem.innerText == content) {
					found = elem;
					break;
				}
			}
			return found;
		};

		let on = function(event) {
			let target = event.target;
			let elements = getElements(target);
			let numbers = getNumbers(target);
			for (let i = 0;  i < numbers.length;  ++i) {
				let number = '' + numbers[i];
				let elem = getByContent(elements, number);
				elem.classList.add('hi');
			}
		};

		let off = function(event) {
			let target = event.target;
			let elements = getElements(target);
			for (let i = 0;  i < elements.length;  ++i) {
				elements[i].classList.remove('hi');
			}
		};

		let elems = document.getElementsByClassName('cross');
		for (let i = 0;  i < elems.length;  ++i) {
			let elem = elems[i];
			elem.addEventListener('mouseover', on);
			elem.addEventListener('mouseout', off);
		}
	}
};

window.addEventListener("DOMContentLoaded", cse111.linenums.addLineNumbers);
window.addEventListener("DOMContentLoaded", cse111.linenums.addCrossRefs);
