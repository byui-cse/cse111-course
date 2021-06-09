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

		let getAllLineNumbers = function(target) {
			let refId = target.getAttribute('data-ref');
			let code = document.getElementById(refId);
			let lineNumDiv = code.previousElementSibling;
			return lineNumDiv.children;
		};

		let getLineNumber = function(lineNumbers, content) {
			let found;
			for (let i = 0;  i < lineNumbers.length;  ++i) {
				let elem = lineNumbers[i];
				if (elem.innerText == content) {
					found = elem;
					break;
				}
			}
			return found;
		};

		let on = function(event) {
			let target = event.target;
			let lineNumbers = getAllLineNumbers(target);
			let numbers = getNumbers(target);
			for (let i = 0;  i < numbers.length;  ++i) {
				let number = '' + numbers[i];
				let elem = getLineNumber(lineNumbers, number);
				elem.classList.add('hi');
			}
		};

		let off = function(event) {
			let target = event.target;
			let lineNumbers = getAllLineNumbers(target);
			let numbers = getNumbers(target);
			for (let i = 0;  i < numbers.length;  ++i) {
				let number = '' + numbers[i];
				let elem = getLineNumber(lineNumbers, number);
				elem.classList.remove('hi');
			}
		};

		let toggle = function(event) {
			let target = event.target;
			let state = target.getAttribute('data-on');
			if (state == null) {
				// Highlights are on because the user moved the mouse
				// into the target before clicking on it. Because the
				// user clicked on the target, set the highlights to
				// stay on after the user moves out of the target.
				target.removeEventListener('mouseover', on);
				target.removeEventListener('mouseout', off);
				target.setAttribute('data-on', 'true');
				target.setAttribute('title', 'Click to turn highlights off.');
			}
			else {
				// Highlights are on because the user clicked on the
				// target. The user has now clicked on the target again,
				// so turn the highlights off.
				let lineNumbers = getAllLineNumbers(target);
				let numbers = getNumbers(target);
				for (let i = 0;  i < numbers.length;  ++i) {
					let number = '' + numbers[i];
					let elem = getLineNumber(lineNumbers, number);
					elem.classList.remove('hi');
				}
				target.removeAttribute('data-on');
				target.addEventListener('mouseover', on);
				target.addEventListener('mouseout', off);
				target.setAttribute('title', 'Move mouse over to turn highlights on.\nClick to keep highlights on.');
			}
		};

		// Add event handlers to each span that has a class of 'cross'.
		let targets = document.getElementsByClassName('cross');
		for (let i = 0;  i < targets.length;  ++i) {
			let target = targets[i];
			target.addEventListener('mouseover', on);
			target.addEventListener('mouseout', off);
			target.addEventListener('click', toggle);
			target.setAttribute('title', 'Move mouse over to turn highlights on.\nClick to keep highlights on.');
		}
	},


	addCopyButtons : function() {
		const copyFunc = function(event) {
			const button = event.currentTarget;
			const div = button.parentElement;
			const pre = div.getElementsByClassName('python')[0];
			const text = pre.textContent;

			// Copy the text to the clipboard.
			const listener = function(event) {
				event.clipboardData.setData('text/plain', text);
				event.preventDefault();
			};
			document.addEventListener('copy', listener);
			document.execCommand('copy');
			document.removeEventListener('copy', listener);
		};

		const elems = document.getElementsByClassName('pre');
		for (let i = 0;  i < elems.length;  ++i) {
			let image = document.createElement('img');
			image.setAttribute('src', '../site/copy.png');
			image.setAttribute('alt', 'Copy code to the clipboard');
			image.style.width = '2em';
			let button = document.createElement('button');
			button.setAttribute('type', 'button');
			button.setAttribute('title', 'Copy code to the clipboard');
			button.classList.add('copy')
			button.appendChild(image);
			button.addEventListener('click', copyFunc);
			elems[i].appendChild(button);
		}
	}
};

window.addEventListener('DOMContentLoaded', cse111.linenums.addLineNumbers);
window.addEventListener('DOMContentLoaded', cse111.linenums.addCrossRefs);
window.addEventListener('DOMContentLoaded', cse111.linenums.addCopyButtons);
