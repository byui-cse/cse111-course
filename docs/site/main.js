/* Copyright 2022 by Brigham Young University - Idaho. All rights eeserved. */
'use strict';

if (! window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}


/** Contains all user visible strings so that translating them to
 * another language will be easier. */
cse111.strings = {
	byuiURL     : 'https://www.byui.edu',
	byuiHint    : 'BYU-Idaho Website',
	byuiLogoAlt : 'BYU-Idaho Logo',
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

	modified : 'Last modified',
	copyrightNotice : 'Copyright © 2019 Brigham Young University–Idaho. All rights reserved.'
};


/** Contains the filenames of all user visible icons and other files so
 * that changing them, if necessary, will be easier. */
cse111.filenames = {
	byuiLogo     : 'site/icons/byui-logo.svg',
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

	printStyle : 'site/print.css',

	contents : 'index.html',
	search   : 'index.html#search',
	help     : 'overview/help.html',
	solution : 'overview/solution.html',

	htmlFile : 'combined/cse111_prepare_content.html',
	pdfFile  : 'combined/cse111_prepare_content.pdf',
	zipFile  : 'combined/cse111_content.zip'
};


/** Creates an HTML element. */
cse111.createElement = function(tag, classes, attrs) {
	let elem = document.createElement(tag);
	if (classes) {
		for (let clss of classes) {
			elem.classList.add(clss);
		}
	}
	if (attrs) {
		for (name in attrs) {
			elem.setAttribute(name, attrs[name]);
		}
	}
	return elem;
};


cse111.common = {
	/** Contains the relative path to get up from the current
	 * webpage to the root directory of this website. */
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


	/** If the document body doesn't have a header element,
	 * this function adds a header to the body. */
	addHeader : function() {
		let header = document.body.querySelector('header');
		if (! header) {
			const strings = cse111.strings;
			const filenames = cse111.filenames;
			const createElem = cse111.createElement;

			/** Opens or closes the navigation menu. */
			function toggleNavMenu(event) {
				event.stopPropagation();
				let nav = document.body.querySelector('nav.menu');
				nav.classList.toggle('closed');
			}

			// Create the children of the header.
			let img = createElem('img', null,
					{alt : strings.byuiLogoAlt,
					src : filenames.byuiLogo});
			let byuiLogo = createElem('a', ['byuiLogo'],
					{title : strings.byuiHint,
					href : strings.byuiURL});
				byuiLogo.appendChild(img);
			let courseCode = createElem('a', null,
					{title : strings.courseHint,
					href : filenames.contents});
				courseCode.textContent =
					strings.courseCode + ' | ' + strings.courseTitle;
			let h2 = createElem('h2');
				h2.appendChild(courseCode);
			let menuIcon = createElem('img', ['menuIcon'],
					{title : strings.menuHint,
					alt : strings.menuHint,
					src : filenames.menuIcon});
				menuIcon.addEventListener('click', toggleNavMenu);

			// Create the header.
			header = createElem('header');
				header.appendChild(byuiLogo);
				header.appendChild(h2);
				header.appendChild(menuIcon);

			// Add the header to the document body.
			const body = document.body;
			const article = body.querySelector('article');
			body.insertBefore(header, article);
			body.addEventListener('click', this.closeNavMenu);

			this.addNavMenu(body, article);
		}
	},


	/** Creates and adds the navigation menu. */
	addNavMenu : function(body, article) {
		const self = this;
		const strings = cse111.strings;
		const filenames = cse111.filenames;
		const createElem = cse111.createElement;
		const ul = createElem('ul');

		/** Creates one menu item. */
		function addMenuItem(icon, text, hint, action, classes, down) {
			let img = createElem('img', null, {alt : hint, src : icon});
			let node = document.createTextNode(' ' + text);
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
		}

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

		if (document.location.protocol != 'file:') {
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
		if (nav) {
			nav.classList.add('closed');
		}
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


	/** Adds a copy character to each h2, h3, or h4 that has an id. */
	addURLCopyChars : function() {
		const strings = cse111.strings;
		const createElem = cse111.createElement;

		function copyFunc(event) {
			let span = event.currentTarget;
			let heading = span.parentElement;
			let url = window.location.href;
			let anchor =  '#' + heading.getAttribute('id');
			let newURL = url.replace(/#.*/, '') + anchor;

			// Copy the new URL to the clipboard.
			function listener(event) {
				event.clipboardData.setData('text/plain', newURL);
				event.preventDefault();
			}
			document.addEventListener('copy', listener);
			document.execCommand('copy');
			document.removeEventListener('copy', listener);

			// Load the new URL in the current browser window.
			window.location.assign(anchor);
		}

		let elements = document.body.querySelectorAll('h2[id], h3[id], h4[id]');
		for (let elem of elements) {
			let span = createElem('span', ['copy'], {title : strings.copyURL});
				span.addEventListener('click', copyFunc);
				span.textContent = strings.paraSymbol;
			elem.appendChild(span);
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
			const createElem = cse111.createElement;

			let div = createElem('div');
			const copyData = this.getCopyrightData();
			if (copyData.modified) {
				let mod = document.createTextNode(
						strings.modified + ' ' + copyData.modified);
				div.appendChild(mod);
			}
			div.appendChild(createElem('br'));
			if (copyData.notice) {
				let copy = document.createTextNode(copyData.notice);
				div.appendChild(copy);
			}

			let up = createElem('img', ['up'],
					{alt : strings.upHint,
					title : strings.upHint,
					src : filenames.upIcon});
			up.addEventListener('click', function() { window.scroll(0, 0); });

			footer = createElem('footer');
			footer.appendChild(div);
			footer.appendChild(up);

			body.appendChild(footer);
		}
	},


	/** Gets the copyright notice and the last modified date, from the
	 * search engine structured data in this document's head. Returns
	 * the two values in an object. */
	getCopyrightData : function() {
		const strings = cse111.strings;
		let notice = strings.copyrightNotice;
		let modified;
		const query = 'script[type="application/ld+json"]';
		const script = document.head.querySelector(query);
		if (script) {
			const object = JSON.parse(script.innerHTML);
			if (object.hasOwnProperty('copyrightNotice')) {
				notice = object.copyrightNotice;
			}
			if (object.hasOwnProperty('dateModified')) {
				modified = object.dateModified;
			}
		}
		return {notice: notice, modified: modified};
	},
};


cse111.linenums = {
	/* The line number functions in this object expect a source code
	 * example and its corresponding console div to be organized like
	 * this in their containing HTML document:
	 * <div class="example" id="ex#">
	 *     <pre class="linenums"></pre>
	 *     <pre class="python"> ... </pre>
	 *     <pre class="console"> ... </pre>
	 * </div>
	 */

	lineNumbersAdded : false,

	/** Adds line numbers to all <pre class="linenums"> elements. */
	addLineNumbers : function() {
		const newline = /<br>\n?|\n/g;
		let elements = document.body.querySelectorAll('pre.linenums');
		for (let pre of elements) {
			let code = pre.nextElementSibling.innerHTML;
			if (code.length > 0) {

				// If the pre.linenums element contains
				// any children nodes, remove them.
				pre.replaceChildren();

				let count = code.split(newline).length;
				for (let n = 1;  n <= count;  ++n) {
					let span = document.createElement('span');
					span.textContent = n.toString();
					pre.appendChild(span);
					pre.appendChild(document.createTextNode('\n'));
				}
			}
		}
		this.lineNumbersAdded = true;
	},


	/** Adds listeners for mouseover, mouseout, and click to all
	 * <span class="cross"> elements so that interacting with a
	 * <span class="cross"> element highlights the corresponding line
	 * numbers in a code example. */
	addCrossRefs : function() {
		function getReferences(target) {
			const space = /(\s|&nbsp;|<br>)+/g;

			// Notice the dash and en dash in the character class.
			const dash = /[-–]|&ndash;/;

			let text = target.textContent;
			let candidates = text.split(space);
			let references = [];
			for (let candidate of candidates) {
				if (dash.test(candidate)) {
					let limits = candidate.split(dash);
					let start = parseInt(limits[0]);
					let end = parseInt(limits[1]);
					if (! (Number.isNaN(start) || Number.isNaN(end))) {
						for (let n = start;  n <= end;  ++n) {
							references.push(n);
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
		}

		/** Returns a (list like) collection of all line number
		 * elements inside a <pre class="linenums"> element. */
		function getAllLineNumbers(target) {
			let refId = target.getAttribute('data-ref');
			let div = document.getElementById(refId);
			let lineNumPre = div.querySelector('pre.linenums');
			return lineNumPre.children;
		}

		function getLineNumber(lineNumbers, key) {
			// The line numbers begin with 1 at index 0 and are
			// sequential, so it's easy to find and return the
			// span with the desired line number.
			return lineNumbers[key - 1];
		}

		function on(event) {
			/** Turn on highlighting for one or more line numbers. */
			let target = event.target;
			let lineNumbers = getAllLineNumbers(target);
			let references = getReferences(target);
			for (let number of references) {
				let elem = getLineNumber(lineNumbers, number);
				elem.classList.add('hi');
			}
		}

		function off(event) {
			/** Turn off highlighting for one or more line numbers. */
			let target = event.target;
			let lineNumbers = getAllLineNumbers(target);
			let references = getReferences(target);
			for (let number of references) {
				let elem = getLineNumber(lineNumbers, number);
				elem.classList.remove('hi');
			}
		}

		const strings = cse111.strings;
		const offHint = strings.offHint;
		const onHint = strings.onHint;

		function toggle(event) {
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
				for (number of references) {
					let elem = getLineNumber(lineNumbers, number);
					elem.classList.remove('hi');
				}
				target.removeAttribute('data-on');
				target.addEventListener('mouseover', on);
				target.addEventListener('mouseout', off);
				target.setAttribute('title', onHint);
			}
		}

		// Add event handlers to each <span class="cross"> element.
		let targets = document.body.querySelectorAll('span.cross');
		for (let target of targets) {
			target.addEventListener('mouseover', on);
			target.addEventListener('mouseout', off);
			target.addEventListener('click', toggle);
			target.setAttribute('title', onHint);
		}
	},


	/** Adds a copy button to each <pre class="python"> element
	 * that is inside a <div class="example"> element. */
	addCodeCopyButtons : function() {
		function copyFunc(event) {
			let button = event.currentTarget;
			let pre = button.parentElement;
			let text = pre.textContent;

			// Copy the text to the clipboard.
			function listener(event) {
				event.clipboardData.setData('text/plain', text);
				event.preventDefault();
			}
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
		}

		const copyHint = cse111.strings.copyHint;
		const copyIcon = cse111.filenames.copyIcon;
		const createElem = cse111.createElement;

		// Add a copy button with a click listener to each
		// <div class="example"> element.
		let elements = document.body.querySelectorAll('div.example');
		for (let div of elements) {
			let image = createElem('img', null,
					{'src' : copyIcon, 'alt' : copyHint});
			let button = createElem('button', ['copy'],
					{'type' : 'button', 'title' : copyHint});
			button.appendChild(image);
			button.addEventListener('click', copyFunc);
			let pre = div.querySelector('pre.python, pre.csv, pre.sql');
			pre.appendChild(button);
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
		let elements = document.body.querySelectorAll('pre.console');
		for (let pre of elements) {
			pre.setAttribute('title', termHint);

			let spans = pre.querySelectorAll('span.input');
			for (let span of spans) {
				span.setAttribute('title', inputHint);
			}
		}
	}
};


cse111.solution = {
	/** Modifies all <a class="solution"> elements. */
	modifyLinks : function() {
		// Get all <a class="solution"> elements.
		let links = document.body.querySelectorAll('a.solution');

		// Is the user viewing the CSE 111 files
		// from the local hard drive?
		if (window.location.protocol == 'file:') {
			for (let link of links) {
				// Because the user is viewing the CSE 111 files from
				// the local hard drive, there is no reason to have both
				// a view and download link. A standard download link
				// will simply open the file for viewing, so a download
				// link is sufficient.
				link.setAttribute('download', '');
			}
		}
		else {
			const strings = cse111.strings;
			const viewText = cse111.strings.viewText + ' ';
			const downText = cse111.strings.downloadText + ' ';
			const createElem = cse111.createElement;

			for (let link of links) {
				// Get the absolute href.
				let absURL = link.href;

				// Get the relative href.
				let relpath = new URL(absURL).pathname.substring(1);
				let newHref = cse111.filenames.solution + '?file=' + relpath;

				let hrefAttr = link.getAttribute('href');
				link.setAttribute('title', viewText + hrefAttr);
				link.setAttribute('href', newHref);

				// Create a new <a download> element.
				let downlink = createElem('a', null,
						{download : '',
						title : downText + hrefAttr,
						href : hrefAttr});
				downlink.textContent = '[↓]';

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
		for (let elem of allDetails) {
			let isOpen = elem.hasAttribute(open);
			if (isOpen) {
				elem.setAttribute(dataWas, true);
			}
			else {
				elem.setAttribute(open, '');
			}
		}
	},

	collapseDetails : function() {
		const open = this.open;
		const dataWas = this.dataWas;
		let allDetails = document.body.querySelectorAll('details');
		for (let elem of allDetails) {
			let wasOpen = elem.hasAttribute(dataWas);
			if (wasOpen) {
				elem.removeAttribute(dataWas);
			}
			else {
				elem.removeAttribute(open);
			}
		}
	}
};


cse111.onDOMLoaded = function() {
	const common = cse111.common;
	const linenums = cse111.linenums;

	common.countLevels();
	common.addHeader();
	common.initBrightness();
	linenums.addLineNumbers();
	cse111.solution.modifyLinks();
	common.addFooter();

	common.addURLCopyChars();
	linenums.addCodeCopyButtons();
	linenums.addCrossRefs();
	cse111.consoles.addHints();
};


cse111.beforePrint = function() {
	cse111.common.closeNavMenu();
	cse111.print.expandDetails();
};

cse111.afterPrint = function() {
	cse111.print.collapseDetails();
};


window.addEventListener('DOMContentLoaded', cse111.onDOMLoaded);
window.addEventListener('beforeprint', cse111.beforePrint);
window.addEventListener('afterprint', cse111.afterPrint);
