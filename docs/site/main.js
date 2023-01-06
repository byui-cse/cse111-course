/* Copyright 2022 by Brigham Young University - Idaho. All rights eeserved. */
'use strict';

if (! window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}


/** Contains all user visible strings so that translating them to
 * another language will be easier. */
cse111.strings = {
	byuiEntity  : '&#xe000;',
	byuiURL     : 'https://www.byui.edu',
	byuiName    : 'Brigham Young University - Idaho',
	byuiHint    : 'BYU-Idaho Website',
	courseCode  : 'CSE 111',
	courseTitle : 'Programming with Functions',
	courseHint  : 'CSE 111 Content',

	lightText   : 'Light Mode',
	darkText    : 'Dark Mode',
	contentsText: 'Contents',
	prevText    : 'Previous Document',
	nextText    : 'Next Document',
	searchText  : 'Search',
	helpText    : 'Help',
	pdfText     : '.pdf File',
	zipText     : '.zip File',

	menuHint    : 'Click to open the navigation menu',
	lightHint   : 'Change to light mode',
	darkHint    : 'Change to dark mode',
	contentsHint: 'View list of contents for CSE 111',
	prevHint    : 'View previous document',
	nextHint    : 'View next document',
	searchHint  : 'Search the CSE 111 content',
	helpHint    : 'Get help for CSE 111',
	pdfHint     : 'Download a PDF that contains\nall CSE 111 HTML content',
	zipHint     : 'Download a zip file that\ncontains all CSE 111 content',
	upHint      : 'Scroll to the top of this document',

	paraSymbol : '¶',
	copyURL    : 'Copy URL to the clipboard',

	offHint : 'Click to turn highlights off.',
	onHint  : 'Move mouse over to turn highlights on.\n' +
			  'Click to keep highlights on.',

	copyHint  : 'Copy code to the clipboard',
	termHint  : 'Terminal Window',
	inputHint : 'User input',

	viewText     : 'View',
	downloadText : 'Download',

	copyright : 'Copyright © 2020–2022',
	rights    : 'All rights reserved.'
};


/** Contains the filenames of all user visible icons and other files so
 * that changing them, if necessary, will be easier. */
cse111.filenames = {
	logoIcon     : 'site/icons/logo.png',
	menuIcon     : 'site/icons/bars.svg',
	lightIcon    : 'site/icons/sun.svg',
	darkIcon     : 'site/icons/moon.svg',
	contentsIcon : 'site/icons/list.svg',
	prevIcon     : 'site/icons/arrow-left.svg',
	nextIcon     : 'site/icons/arrow-right.svg',
	upIcon       : 'site/icons/arrow-up-long.svg',
	searchIcon   : 'site/icons/magnify-glass.svg',
	helpIcon     : 'site/icons/question.svg',
	pdfIcon      : 'site/icons/file-pdf.svg',
	zipIcon      : 'site/icons/file-zip.svg',
	copyIcon     : 'site/icons/copy.png',

	contents : 'index.html',
	search   : 'index.html#search',
	help     : 'overview/help.html',
	solution : 'overview/solution.html',

	htmlFile : 'combined/cse111_content.html',
	pdfFile  : 'combined/cse111_content.pdf',
	zipFile  : 'combined/cse111_content.zip'
};


cse111.common = {
	/** Returns true if the current HTML document is a combined HTML
	 * file that is used for creating a combined PDF. */
	isCombined : function() {
		const getFilename = function(pathname) {
			let parts = pathname.split('/');
			return parts[parts.length - 1];
		};

		let expectedFilename = getFilename(cse111.filenames.htmlFile);
		let actualFilename = getFilename(document.location.pathname);
		return actualFilename == expectedFilename;
	},


	/** Contains the relative path to get up from the current webpage to
	 * the root directory of this website. */
	upsToRoot : '',

	countLevels : function() {
		let siteIcon = document.head.querySelector('link[rel="icon"]');
		if (siteIcon) {
			let href = siteIcon.getAttribute('href');
			let pathname = cse111.filenames.logoIcon;
			if (href.endsWith(pathname)) {
				let end = href.length - pathname.length;
				let upsToRoot = href.substring(0, end);

				// Change all filenames to be relative to the sub
				// directory of the current HTML document.
				let filenames = cse111.filenames;
				for (let key in filenames) {
					let subname = filenames[key]
					filenames[key] = upsToRoot + subname;
				}

				this.upsToRoot = upsToRoot;
			}
		}
	},

	makeRelPath : function(subpath) {
		return this.upsToRoot + subpath;
	},


	/** If the document body doesn't have a header element, this
	 * functions adds a header to the body. */
	addHeader : function() {
		let header = document.body.querySelector('header');
		if (! header) {
			const self = this;
			const strings = cse111.strings;
			const filenames = cse111.filenames;
			const createElem = self.createElement;
			const createText = self.createTextNode;

			/** Opens or closes the navigation menu. */
			const toggleNavMenu = function(event) {
				event.stopPropagation();
				let nav = document.body.querySelector('nav.menu');
				nav.classList.toggle('closed');
			};

			// Create the children of the header.
			let byuiLogo = createElem('a', ['byuiLogo'],
					{title : strings.byuiHint,
					href : strings.byuiURL});
				byuiLogo.innerHTML = strings.byuiEntity;
			let courseCode = createElem('a', null,
					{title : strings.courseHint,
					href : filenames.contents});
				courseCode.innerText =
					strings.courseCode + ' | ' + strings.courseTitle;
			let h2 = createElem('h2');
				h2.appendChild(courseCode);
			let menuIcon = createElem('img', ['menuIcon'],
					{title : strings.menuHint,
					alt : strings.menuHint,
					src : filenames.menuIcon});
				menuIcon.addEventListener('click', toggleNavMenu);

			// Create the header and add it to the document body.
			header = createElem('header');
				header.appendChild(byuiLogo);
				header.appendChild(h2);
				header.appendChild(menuIcon);
			const body = document.body;
			const article = body.querySelector('article');
			body.insertBefore(header, article);

			this.addNavMenu(body, article);
			body.addEventListener('click', self.closeNavMenu);
		}
	},


	/** Creates and adds the navigation menu. */
	addNavMenu : function(body, article) {
		const self = this;
		const strings = cse111.strings;
		const filenames = cse111.filenames;
		const createElem = self.createElement;
		const createText = self.createTextNode;
		const ul = createElem('ul');

		/** Creates one menu item. */
		const addMenuItem = function(icon, text, hint, action, classes, down) {
			let img = createElem('img', null, {alt : hint, src : icon});
			let node = createText(' ' + text);
			let item = createElem('li', classes, {title : hint});
			if (typeof(action) == 'function') {
				item.appendChild(img);
				item.appendChild(node);
				item.addEventListener('click', action);
			}
			else if (typeof(action) == 'string') {
				let anchor = createElem('a', null,
						down ?
						{download : '', href : action} :
						{href : action});
				anchor.appendChild(img);
				anchor.appendChild(node);
				item.appendChild(anchor);
			}
			ul.appendChild(item);
		};

		// Create the menu items.
		addMenuItem(filenames.lightIcon, strings.lightText,
				strings.lightHint,
				function() { self.setBrightness('light'); },
				['light']);
		addMenuItem(filenames.darkIcon, strings.darkText,
				strings.darkHint,
				function() { self.setBrightness('dark'); },
				['dark']);

		addMenuItem(filenames.contentsIcon, strings.contentsText,
				strings.contentsHint, filenames.contents, ['first']);

		const head = document.head;
		const prev = head.querySelector('link[rel="prev"]');
		const next = head.querySelector('link[rel="next"]');
		if (prev) {
			addMenuItem(filenames.prevIcon, strings.prevText,
					strings.prevHint, prev.href);
		}
		if (next) {
			addMenuItem(filenames.nextIcon, strings.nextText,
					strings.nextHint, next.href);
		}

		addMenuItem(filenames.searchIcon, strings.searchText,
				strings.searchHint, filenames.search, ['first']);
		addMenuItem(filenames.helpIcon, strings.helpText,
				strings.helpHint, filenames.help);

		if (document.location.protocol != "file:") {
			addMenuItem(filenames.pdfIcon, strings.pdfText,
					strings.pdfHint, filenames.pdfFile, ['first'], true);
			addMenuItem(filenames.zipIcon, strings.zipText,
					strings.zipHint, filenames.zipFile, null, true);
		}

		// Add the navigation menu to the document body.
		let nav = createElem('nav', ['menu', 'closed']);
		nav.appendChild(ul);
		body.insertBefore(nav, article);
	},


	/** Closes the navigation menu. */
	closeNavMenu : function() {
		let nav = document.body.querySelector('nav.menu');
		nav.classList.add('closed');
	},


	/** Initializes the brightness to the one most recently chosen by
	 * the user. */
	initBrightness : function() {
		let brightness = localStorage.getItem('brightness');
		if (! brightness) {
			let clist = document.body.classList;
			brightness = clist.contains('dark') ? 'dark' : 'light';
		}
		this.setBrightness(brightness);
	},

	/** Sets the brightness. */
	setBrightness : function(brightness) {
		// Store the chosen brightness (light or dark) in local storage.
		localStorage.setItem('brightness', brightness);

		// Change the classList for the document body.
		let remove = (brightness == 'dark' ? 'light' : 'dark');
		let clist = document.body.classList;
		clist.remove(remove);
		clist.add(brightness);
	},


	/** Creates an HTML element. */
	createElement : function(tag, classes, attrs) {
		let elem = document.createElement(tag);
		if (classes) {
			for (let i = 0;  i < classes.length;  ++i) {
				elem.classList.add(classes[i]);
			}
		}
		if (attrs) {
			for (name in attrs) {
				let value = attrs[name];
				elem.setAttribute(name, value);
			}
		}
		return elem;
	},

	/** Creates an HTML text node. */
	createTextNode : function(text) {
		return document.createTextNode(text);
	},


	/** Adds a copy character to each h2, h3, or h4 that has an id. */
	addAnchorCopyChar : function() {
		const strings = cse111.strings;
		const createElem = cse111.common.createElement;

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

		let elems = document.body.querySelectorAll('h2[id], h3[id], h4[id]');
		for (let i = 0;  i < elems.length;  ++i) {
			let span = createElem('span', ['copy'], {title : strings.copyURL});
				span.addEventListener('click', copyFunc);
				span.innerText = strings.paraSymbol;
			elems[i].appendChild(span);
		}
	},


	/** If the document body doesn't have a footer element, this
	 * function adds a footer to the body. */
	addFooter : function() {
		const body = document.body;
		let footer = body.querySelector('footer');
		if (! footer) {
			const strings = cse111.strings;
			const filenames = cse111.filenames;
			const createElem = cse111.common.createElement;
			const createText = cse111.common.createTextNode;

			let up = createElem('img', ['up'],
					{alt : strings.upHint,
					title : strings.upHint,
					src : filenames.upIcon});
			up.addEventListener('click', function() {window.scrollTo(0, 0);});

			let anchor = createElem('a', null,
					{title : strings.byuiHint, href : strings.byuiURL});
			anchor.innerText = strings.byuiName;
			let copy = createElem('div', ['copyright']);
			copy.appendChild(createText(strings.copyright + ', '));
			copy.appendChild(anchor);
			copy.appendChild(createText('. ' + strings.rights));

			footer = createElem('footer');
			footer.appendChild(up);
			footer.appendChild(copy);

			body.appendChild(footer);
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

	lineNumbersAdded : false,

	/** Adds line numbers to all <pre class="linenums"> elements. */
	addLineNumbers : function() {
		const newline = /<br>\n?|\n/g;
		const createElem = cse111.common.createElement;
		const createText = cse111.common.createTextNode;
		let elems = document.body.querySelectorAll('pre.linenums');
		for (let i = 0;  i < elems.length;  ++i) {
			let elem = elems[i];
			let code = elem.nextElementSibling.innerHTML;
			let count = code.split(newline).length;
			for (let n = 1;  n <= count;  ++n) {
				let span = createElem('span');
				span.innerText = n.toString();
				elem.appendChild(span);
				elem.appendChild(createText('\n'));
			}
		}
		this.lineNumbersAdded = true;
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

		/** Returns a (list like) collection of all line number
		 * elements inside a <pre class="linenums"> element. */
		const getAllLineNumbers = function(target) {
			let refId = target.getAttribute('data-ref');
			let preDiv = document.getElementById(refId);
			let lineNumPre = preDiv.querySelector('pre');
			return lineNumPre.children;
		};

		const getLineNumber = function(lineNumbers, key) {
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
				let elem = getLineNumber(lineNumbers, number);
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
				let elem = getLineNumber(lineNumbers, number);
				elem.classList.remove('hi');
			}
		};

		const strings = cse111.strings;
		const offHint = strings.offHint;
		const onHint = strings.onHint;

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
				target.setAttribute('title', offHint);
			}
			else {
				// Highlights are on because the user clicked on the
				// target. The user has now clicked on the target again,
				// so turn the highlights off.
				let lineNumbers = getAllLineNumbers(target);
				let references = getReferences(target);
				for (let i = 0;  i < references.length;  ++i) {
					let number = references[i];
					let elem = getLineNumber(lineNumbers, number);
					elem.classList.remove('hi');
				}
				target.removeAttribute('data-on');
				target.addEventListener('mouseover', on);
				target.addEventListener('mouseout', off);
				target.setAttribute('title', onHint);
			}
		};

		// Add event handlers to each <span class="cross"> element.
		let targets = document.body.querySelectorAll('span.cross');
		for (let i = 0;  i < targets.length;  ++i) {
			let target = targets[i];
			target.addEventListener('mouseover', on);
			target.addEventListener('mouseout', off);
			target.addEventListener('click', toggle);
			target.setAttribute('title', onHint);
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
		const copyHint = cse111.strings.copyHint;
		const copyIcon = cse111.filenames.copyIcon;
		const createElem = cse111.common.createElement;
		let elems = document.body.querySelectorAll('div.pre');
		for (let i = 0;  i < elems.length;  ++i) {
			let image = document.createElement('img');
			image.setAttribute('src', copyIcon);
			image.setAttribute('alt', copyHint);
			let button = document.createElement('button');
			button.setAttribute('type', 'button');
			button.setAttribute('title', copyHint);
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
	addHints : function() {
		const termHint = cse111.strings.termHint;
		const inputHint = cse111.strings.inputHint;
		let elems = document.body.querySelectorAll('pre.console');
		for (let i = 0;  i < elems.length;  ++i) {
			let pre = elems[i];
			pre.setAttribute('title', termHint);

			let spans = pre.querySelectorAll('span.input');
			for (let i = 0;  i < spans.length;  ++i) {
				spans[i].setAttribute('title', inputHint);
			}
		}
	},


	/** Resizes each <pre class="console" data-for="..."> element so
	 * that its width is the same as the width of the div.pre >
	 * pre.python for which it shows user input and program output.
	 * Making their widths the same helps the reader to see that they go
	 * together. */
	resizeConsoles : function() {
		let consoles = document.body.querySelectorAll('pre.console[data-for]');
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
	/** Modifies all <a class="solution"> elements. */
	modifyHyperlinks : function() {
		// Get all <a class="solution"> elements.
		let links = document.body.querySelectorAll('a.solution');

		// Is the user viewing the CSE 111 files
		// from the local hard drive?
		if (window.location.protocol == 'file:') {
			for (let i = 0;  i < links.length;  ++i) {
				let link = links[i];

				// Because the user is viewing the CSE 111 files from
				// the local hard drive, there is no reason to have both
				// a view and download link. A standard download link
				// will simply open the file for viewing, so a download
				// link is sufficient.
				link.setAttribute('download', '');
			}
		}
		else {
			const splitURL = /^.+\/([^\/]+\/[^\/]+)$/;
			const strings = cse111.strings;
			const viewText = cse111.strings.viewText + ' ';
			const downText = cse111.strings.downloadText + ' ';
			const createElem = cse111.common.createElement;

			for (let i = 0;  i < links.length;  ++i) {
				let link = links[i];

				// Get the absolute href.
				let absURL = link.href;

				// Get the relative href.
				// It would be great if we could use the window.URL
				// class, but it isn't in Internet Explorer, and it's
				// possible that international students are still using
				// Internet Explorer.
				//let relpath = new URL(absURL).pathname.substring(1);
				let relpath = absURL.replace(splitURL, '$1');

				let newHref = cse111.filenames.solution + '?file=' + relpath;

				let hrefAttr = link.getAttribute('href');
				link.setAttribute('title', viewText + hrefAttr);
				link.setAttribute('href', newHref);

				// Create a new <a download> element.
				let downlink = createElem('a', null,
						{download : '',
						title : downText + hrefAttr,
						href : hrefAttr});
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


cse111.print = {
	open : 'open',
	dataWas : 'data-was-open',

	expandDetails : function() {
		const open = this.open;
		const dataWas = this.dataWas;
		let allDetails = document.body.querySelectorAll('details');
		for (let i = 0;  i < allDetails.length;  ++i) {
			let detailsElem = allDetails[i];
			let isOpen = detailsElem.hasAttribute(open);
			if (isOpen) {
				detailsElem.setAttribute(dataWas, true);
			}
			else {
				detailsElem.setAttribute(open, '');
			}
		}
	},

	collapseDetails : function() {
		const open = this.open;
		const dataWas = this.dataWas;
		let allDetails = document.body.querySelectorAll('details');
		for (let i = 0;  i < allDetails.length;  ++i) {
			let detailsElem = allDetails[i];
			let wasOpen = detailsElem.hasAttribute(dataWas);
			if (wasOpen) {
				detailsElem.removeAttribute(dataWas);
			}
			else {
				detailsElem.removeAttribute(open);
			}
		}
	}
};


cse111.onDOMLoaded = function() {
	const common = cse111.common;
	const linenums = cse111.linenums;

	if (common.isCombined()) {
		linenums.addLineNumbers();
	}
	else {
		common.countLevels();
		common.addHeader();
		common.initBrightness();
		linenums.addLineNumbers();
		cse111.solution.modifyHyperlinks();
		common.addFooter();

		common.addAnchorCopyChar();
		linenums.addCopyButtons();
		linenums.addCrossRefs();
		cse111.consoles.addHints();
	}
};

cse111.onFullDocLoaded = function() {
	if (! cse111.common.isCombined()) {
		let attempts = 20;
		const checkLineNumbers = function() {
			if (cse111.linenums.lineNumbersAdded) {
				// Without a delay, the consoles are resized before the
				// line numbers are generated which makes the consoles
				// narrower than their corresponding example code.
				window.setTimeout(function() {
					cse111.consoles.resizeConsoles();
				}, 100);
			}
			else if (--attempts > 0) {
				window.setTimeout(checkLineNumbers(), 100);
			}
		}
		checkLineNumbers();
	}
};

cse111.beforePrint = function() {
	cse111.common.closeNavMenu();
	cse111.print.expandDetails();
};

cse111.afterPrint = function() {
	cse111.print.collapseDetails();
};


window.addEventListener('DOMContentLoaded', cse111.onDOMLoaded);
window.addEventListener('load', cse111.onFullDocLoaded);
window.addEventListener('beforeprint', cse111.beforePrint);
window.addEventListener('afterprint', cse111.afterPrint);
