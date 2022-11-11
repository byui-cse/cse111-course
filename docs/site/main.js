/* Copyright 2020 by Brigham Young University - Idaho. All rights eeserved. */
"use strict";

if (! window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}


cse111.header = {
	addHeader : function() {
		let header = document.createElement('header');
		header.innerHTML =
'<div class="controls">\n' +
'\t<span class="brightness"></span>\n' +
'\t<div class="combined">\n' +
'\t\t<a download title="Download a PDF that contains all CSE 111 HTML content"'+
' href="../combined/cse111_content.pdf">[pdf]</a>\n' +
'\t\t<a download title="Download a zip file that contains all CSE 111 content"'+
' href="../combined/cse111_content.zip">[zip]</a>\n' +
'\t</div>\n' +
'</div>\n' +
'<a class="byui-logo" title="BYU-Idaho Website" href="https://www.byui.edu">&#xe000;</a>\n' +
'<h2><a title="I-Learn" href="https://byui.instructure.com">CSE 111</a> |\n' +
'\t<a title="CSE 111 Content" href="../index.html">Programming with Functions</a></h2>';
		let body = document.body;
		let article = body.getElementsByTagName('article')[0];
		body.insertBefore(header, article);
	},


	/** The <span class="brightness"> element allows a user to click a
	 * moon or sun symbol to toggle the brightness of an HTML document
	 * between dark and light mode. */
	addBrightnessHandler : function() {
		const dark = 'dark';
		const light = 'light';
		const brightnessData = {
			dark: {remove:light, symbol:'\u263c', title:'Change to light mode'},
			light: {remove:dark, symbol:'\u263e', title:'Change to dark mode'}
		};

		/** Sets the brightness. */
		const set = function(clist, brightness) {
			let data = brightnessData[brightness];

			// Store the chosen brightness
			// (light or dark) in local storage.
			localStorage.setItem('brightness', brightness);

			// Change the classList for the document body.
			clist.remove(data.remove);
			clist.add(brightness);

			// Change the title and symbol for all
			// brightness controls in the document.
			let ctrls = document.getElementsByClassName('brightness');
			for (let i = 0;  i < ctrls.length;  ++i) {
				let elem = ctrls[i];
				elem.setAttribute('title', data.title);
				elem.innerHTML = data.symbol;
			}
		};

		/** Toggles the brightness from light to dark and vice versa. */
		const toggle = function(event) {
			let clist = document.body.classList;
			let brightness = clist.contains(dark) ? light : dark;
			set(clist, brightness);
		};

		// Set the brightness to the one
		// most recently chosen by the user.
		let clist = document.body.classList;
		let brightness = localStorage.getItem('brightness');
		if (! brightness) {
			brightness = clist.contains(dark) ? dark : light;
		}
		set(clist, brightness);

		// Add the toggle function as a click handler
		// to all brightness controls in the document.
		let ctrls = document.getElementsByClassName('brightness');
		for (let i = 0;  i < ctrls.length;  ++i) {
			ctrls[i].addEventListener('click', toggle);
		}
	}
};


cse111.linenums = {
	/* The line number functions in this object expect a source code
	 * example and its corresponding console div to be organized like
	 * this in their containing HTML document:
	 * <div class="pre" id="exN">
	 *     <pre class="linenums"></pre>
	 *     <pre class="python"> ... </pre>
	 * </div>
	 * <pre class="console" date-for="exN"> ... </pre>
	 */

	/** Adds line numbers to all <pre class="linenums"> elements. */
	addLineNumbers : function() {
		const newline = /<br>\n?|\n/g;
		let elems = document.querySelectorAll('pre.linenums');
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


	/** Adds listeners for mouseover, mouseout, and click to all
	 * <span class="cross"> elements so that interacting with a
	 * <span class="cross"> element highlights the corresponding line
	 * numbers in a code example. */
	addCrossRefs : function() {
		const getReferences = function(target) {
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

		const getAllLineNumbers = function(target) {
			let refId = target.getAttribute('data-ref');
			let preDiv = document.getElementById(refId);
			let lineNumPre = preDiv.getElementsByTagName('pre')[0];
			return lineNumPre.children;
		};

		const findLineNumber = function(lineNumbers, key) {
			// The line numbers begin with 1 at index 0 and are
			// sequential, so it's easy to find and return the
			// span with the desired line number.
			return lineNumbers[key - 1];
		};

		const on = function(event) {
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

		const off = function(event) {
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

		const offTitle = 'Click to turn highlights off.';
		const onTitle = 'Move mouse over to turn highlights on.\n' +
			'Click to keep highlights on.';

		const toggle = function(event) {
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
				target.setAttribute('title', offTitle);
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
				target.setAttribute('title', onTitle);
			}
		};

		// Add event handlers to each <span class="cross"> element.
		let targets = document.querySelectorAll('span.cross');
		for (let i = 0;  i < targets.length;  ++i) {
			let target = targets[i];
			target.addEventListener('mouseover', on);
			target.addEventListener('mouseout', off);
			target.addEventListener('click', toggle);
			target.setAttribute('title', onTitle);
		}
	},


	/** Adds a copy button to each <div class="pre"> element. */
	addCopyButtons : function() {
		const copyFunc = function(event) {
			let button = event.currentTarget;
			let div = button.parentElement;
			let elems = div.getElementsByTagName('pre');
			let pre = elems[elems.length - 1];
			let text = pre.textContent;

			// Copy the text to the clipboard.
			const listener = function(event) {
				event.clipboardData.setData('text/plain', text);
				event.preventDefault();
			};
			document.addEventListener('copy', listener);
			document.execCommand('copy');
			document.removeEventListener('copy', listener);

			// Select the text as a hint to the user that it was
			// copied to the clipboard. Selecting the text is not
			// necessary for copying the text to the clipboard.
			// Selecting the text is simply feedback to the user.
			let select = window.getSelection();
			let range = document.createRange();
			range.selectNodeContents(pre);
			select.removeAllRanges();
			select.addRange(range);
		};

		// Add a copy button with a click listener to each
		// <div class="pre"> element.
		let elems = document.querySelectorAll('div.pre');
		for (let i = 0;  i < elems.length;  ++i) {
			let image = document.createElement('img');
			image.setAttribute('src', '../site/icons/copy.png');
			image.setAttribute('alt', 'Copy code to the clipboard');
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


cse111.consoles = {
	/** Adds title attributes to consoles and user inputs. Most browsers
	 * will use the titles as small tool tips that display when the user
	 * holds the mouse pointer over an HTML element. */
	addTitles : function() {
		let elems = document.querySelectorAll('pre.console');
		for (let i = 0;  i < elems.length;  ++i) {
			let pre = elems[i];
			pre.setAttribute('title', 'Terminal Window');

			let spans = pre.querySelectorAll('span.input');
			for (let i = 0;  i < spans.length;  ++i) {
				spans[i].setAttribute('title', 'User input');
			}
		}
	},


	/** Resizes each pre.console[data-for] element so that its width is
	 * the same as the width of the div.pre > pre.python for which it
	 * shows user input and program output. Making their widths the same
	 * helps the reader to see that they go together. */
	resizeConsoles : function() {
		let consoles = document.querySelectorAll('pre.console[data-for]');
		for (let i = 0;  i < consoles.length;  ++i) {
			let console = consoles[i];

			// Get the computed style width of the pre.python element
			// that corresponds to the current pre.console element.
			let id = console.getAttribute('data-for');
			let style = window.getComputedStyle(document.getElementById(id));
			let width = parseFloat(style.getPropertyValue('width'));

			// The element width returned by getPropertyValue does not
			// include the border width, but the element.style.width
			// property does include the border width. In order to use
			// element.style.width to set the width of the console div,
			// we must first add the border width to the computed width.
			style = window.getComputedStyle(console);
			let left = parseFloat(style.getPropertyValue('border-left-width'));
			let right= parseFloat(style.getPropertyValue('border-right-width'));
			width += left + right;

			// Set the width of the current pre.console element to match
			// the width of its corresponding pre.python element.
			console.style.width = width + 'px';
		}
	}
};


cse111.solution = {
	/** Add a copy character to each h2, h3, or h4 that has an id. */
	addAnchorCopyChar : function() {
		const copyFunc = function(event) {
			let span = event.currentTarget;
			let heading = span.parentElement;
			let url = window.location.href;
			let anchor =  '#' + heading.getAttribute('id');
			let newURL = url.replace(/#.*/, '') + anchor;

			// Copy the new URL to the clipboard.
			const listener = function(event) {
				event.clipboardData.setData('text/plain', newURL);
				event.preventDefault();
			};
			document.addEventListener('copy', listener);
			document.execCommand('copy');
			document.removeEventListener('copy', listener);

			// Load the new URL in the current browser window.
			window.location.assign(anchor);
		};

		let elems = document.querySelectorAll('h2[id], h3[id], h4[id]');
		for (let i = 0;  i < elems.length;  ++i) {
			let span = document.createElement('span');
			span.classList.add('copy');
			span.setAttribute('title', 'Copy URL to the clipboard');
			span.addEventListener('click', copyFunc);
			span.innerText = '¶';

			let heading = elems[i];
			heading.appendChild(span);
		}
	},


	/** Modifies all <a class="solution"> elements. */
	modifyHyperlinks : function() {
		// Get all <a class="solution"> elements.
		let links = document.querySelectorAll('a.solution');

		// Is the user viewing the CSE 111 files
		// from his local hard drive?
		let isLocal = /^file:\/\/\//.test(window.location);
		if (isLocal) {
			for (let i = 0;  i < links.length;  ++i) {
				let link = links[i];

				// Because the user is viewing the CSE 111 files from
				// his local hard drive, there is no reason to have both
				// a view and download link. A standard download link
				// will simply open the file for viewing, so a download
				// link is sufficient.
				link.setAttribute('download', '');
			}
		}
		else {
			const splitURL = /^.+\/([^\/]+\/[^\/]+)$/;

			for (let i = 0;  i < links.length;  ++i) {
				let link = links[i];

				// Get the relative href.
				let hrefAttr = link.getAttribute('href');
				let absURL = link.href;
				let relpath = absURL.replace(splitURL, '$1');
				let newHref = '../overview/solution.html?file=' + relpath;

				link.setAttribute('title', 'View ' + hrefAttr);
				link.setAttribute('href', newHref);

				// Create a new <a download> element.
				let downlink = document.createElement('a');
				downlink.setAttribute('download', '');
				downlink.setAttribute('title', 'Download ' + hrefAttr);
				downlink.setAttribute('href', hrefAttr);
				downlink.innerHTML = '[&darr;]';

				// Insert the new <a download> element after
				// the current <a class="solution"> element.
				let parent = link.parentNode;
				let next = link.nextSibling;
				parent.insertBefore(document.createTextNode(' '), next);
				parent.insertBefore(downlink, next);
			}
		}
	}
};


cse111.onDOMLoaded = function() {
	cse111.header.addHeader();  // Not for PDF
	cse111.header.addBrightnessHandler(); // "
	cse111.solution.addAnchorCopyChar();  // "
	cse111.solution.modifyHyperlinks();
	cse111.linenums.addLineNumbers();
	cse111.linenums.addCopyButtons();     // "
	cse111.linenums.addCrossRefs();
	cse111.consoles.addTitles();          // "
};

cse111.onFullDocLoaded = function() {
	// Without a delay, the consoles are resized before the line
	// numbers are generated which makes the consoles narrower than
	// their corresponding example code.
	window.setTimeout(function() {
		cse111.consoles.resizeConsoles();
	}, 400);
};

window.addEventListener('DOMContentLoaded', cse111.onDOMLoaded);
window.addEventListener('load', cse111.onFullDocLoaded);  // Not for PDF
