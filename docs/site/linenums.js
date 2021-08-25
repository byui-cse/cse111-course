/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */

"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.linenums = {
	/** Resizes each pre.console[data-for] element so that its width is
	 * the same as the width of the div.pre > pre.python for which it
	 * shows user input and program output. Making their widths the same
	 * helps the reader to see that they go together. */
	resizeConsoles : function() {
		const consoles = document.querySelectorAll('pre.console[data-for]');
		for (let i = 0;  i < consoles.length;  ++i) {
			let console = consoles[i];
			let id = console.getAttribute('data-for');
			let divElem = document.getElementById(id);
			let width = window.getComputedStyle(divElem).getPropertyValue('width');
			console.style.width = width;
		}
	},


	/** Adds line numbers to all pre.linenums elements. */
	addLineNumbers : function() {
		const newline = /<br>|\n/g;
		const elems = document.querySelectorAll('pre.linenums');
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


	addCopyButtons : function() {
		const copyFunc = function(event) {
			const button = event.currentTarget;
			const div = button.parentElement;
			const elems = div.getElementsByTagName('pre');
			const pre = elems[elems.length - 1];
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

		const elems = document.querySelectorAll('div.pre');
		for (let i = 0;  i < elems.length;  ++i) {
			let image = document.createElement('img');
			image.setAttribute('src', '../site/copy.png');
			image.setAttribute('alt', 'Copy code to the clipboard');
			let button = document.createElement('button');
			button.setAttribute('type', 'button');
			button.setAttribute('title', 'Copy code to the clipboard');
			button.classList.add('copy')
			button.appendChild(image);
			button.addEventListener('click', copyFunc);
			elems[i].appendChild(button);
		}
	},


	addTitles : function() {
		const elems = document.querySelectorAll('pre.console');
		for (let i = 0;  i < elems.length;  ++i) {
			let pre = elems[i];
			pre.setAttribute('title', 'Terminal Window');

			const spans = pre.querySelectorAll('span.input');
			for (let i = 0;  i < spans.length;  ++i) {
				spans[i].setAttribute('title', 'User input');
			}
		}
	},


	addCrossRefs : function() {
		let getReferences = function(target) {
			const space = /(\s|&nbsp;|<br>)+/g;

			// Notice the dash and en dash in the character class.
			const dash = /[-–]|&ndash;/;

			let text = target.innerText;
			let candidates = text.split(space);
			let references = [];
			for (let i = 0;  i < candidates.length;  ++i) {
				let candidate = candidates[i];
				if (dash.test(candidate)) {
					let limits = candidate.split(dash);
					let start = parseInt(limits[0]);
					let end = parseInt(limits[1]);
					if (! (Number.isNaN(start) || Number.isNaN(end))) {
						for (let j = start;  j <= end;  ++j) {
							references.push(j);
						}
					}
				}
				else {
					let linenum = parseInt(candidate);
					if (! Number.isNaN(linenum)) {
						references.push(linenum);
					}
				}
			}
			return references;
		};

		let getAllLineNumbers = function(target) {
			let refId = target.getAttribute('data-ref');
			let preDiv = document.getElementById(refId);
			let lineNumDiv = preDiv.firstChild;
			return lineNumDiv.children;
		};

		let findLineNumber = function(lineNumbers, key) {
			// The line numbers begin with 1 at index 0 and are
			// sequential, so it's easy to find and return the
			// span with the desired line number.
			return lineNumbers[key - 1];
		};

		let on = function(event) {
			/** Turn on highlighting for one or more line numbers. */
			let target = event.target;
			let lineNumbers = getAllLineNumbers(target);
			let references = getReferences(target);
			for (let i = 0;  i < references.length;  ++i) {
				let number = references[i];
				let elem = findLineNumber(lineNumbers, number);
				elem.classList.add('hi');
			}
		};

		let off = function(event) {
			/** Turn off highlighting for one or more line numbers. */
			let target = event.target;
			let lineNumbers = getAllLineNumbers(target);
			let references = getReferences(target);
			for (let i = 0;  i < references.length;  ++i) {
				let number = references[i];
				let elem = findLineNumber(lineNumbers, number);
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
				let references = getReferences(target);
				for (let i = 0;  i < references.length;  ++i) {
					let number = references[i];
					let elem = findLineNumber(lineNumbers, number);
					elem.classList.remove('hi');
				}
				target.removeAttribute('data-on');
				target.addEventListener('mouseover', on);
				target.addEventListener('mouseout', off);
				target.setAttribute('title', 'Move mouse over to turn highlights on.\nClick to keep highlights on.');
			}
		};

		// Add event handlers to each span that has a class of 'cross'.
		let targets = document.querySelectorAll('span.cross');
		for (let i = 0;  i < targets.length;  ++i) {
			let target = targets[i];
			target.addEventListener('mouseover', on);
			target.addEventListener('mouseout', off);
			target.addEventListener('click', toggle);
			target.setAttribute('title', 'Move mouse over to turn highlights on.\nClick to keep highlights on.');
		}
	}
};

window.addEventListener('DOMContentLoaded', cse111.linenums.addLineNumbers);
window.addEventListener('DOMContentLoaded', cse111.linenums.addCopyButtons);
window.addEventListener('DOMContentLoaded', cse111.linenums.resizeConsoles);
window.addEventListener('DOMContentLoaded', cse111.linenums.addTitles);
window.addEventListener('DOMContentLoaded', cse111.linenums.addCrossRefs);
