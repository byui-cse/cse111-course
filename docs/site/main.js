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
	pdfHint     : 'Download a PDF that contains all\nCSE 111 HTML preparation content',
	zipHint     : 'Download a zip file that\ncontains all CSE 111 content',
	upHint      : 'Scroll to the top of this document',

	paraSymbol : '¶',
	copyURL    : 'Copy URL to the clipboard',

	offHint : 'Click to turn off highlights.',
	onHint  : 'Move mouse over to turn on highlights.\n' +
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

	contents : 'index.html',
	search   : 'index.html#search',
	help     : 'overview/help.html',
	solution : 'overview/solution.html',

	htmlFile : 'combined/cse111_prepare_content.html',
	pdfFile  : 'combined/cse111_prepare_content.pdf',
	zipFile  : 'combined/cse111_content.zip'
};


cse111.svgCache =
'<svg xmlns="http://www.w3.org/2000/svg"><defs><!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->\
<symbol id="svgArrowLeft" viewBox="0 0 448 512"><path d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"/></symbol>\
<symbol id="svgArrowRight" viewBox="0 0 448 512"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></symbol>\
<symbol id="svgArrowUp" viewBox="0 0 384 512"><path d="M214.6 9.4c-12.5-12.5-32.8-12.5-45.3 0l-128 128c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 109.3V480c0 17.7 14.3 32 32 32s32-14.3 32-32V109.3l73.4 73.4c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-128-128z"/></symbol>\
<symbol id="svgBars" viewBox="0 0 448 512"><path d="M0 96C0 78.3 14.3 64 32 64H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 128 0 113.7 0 96zM0 256c0-17.7 14.3-32 32-32H416c17.7 0 32 14.3 32 32s-14.3 32-32 32H32c-17.7 0-32-14.3-32-32zM448 416c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H416c17.7 0 32 14.3 32 32z"/></symbol>\
<symbol id="svgClose" viewBox="0 0 320 512"><path d="M310.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L160 210.7 54.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L114.7 256 9.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 301.3 265.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L205.3 256 310.6 150.6z"/></symbol>\
<symbol id="svgCopy" viewBox="0 0 512 512"><path d="M502.6 70.63l-61.25-61.25C435.4 3.371 427.2 0 418.7 0H255.1c-35.35 0-64 28.66-64 64l.0195 256C192 355.4 220.7 384 256 384h192c35.2 0 64-28.8 64-64V93.25C512 84.77 508.6 76.63 502.6 70.63zM464 320c0 8.836-7.164 16-16 16H255.1c-8.838 0-16-7.164-16-16L239.1 64.13c0-8.836 7.164-16 16-16h128L384 96c0 17.67 14.33 32 32 32h47.1V320zM272 448c0 8.836-7.164 16-16 16H63.1c-8.838 0-16-7.164-16-16L47.98 192.1c0-8.836 7.164-16 16-16H160V128H63.99c-35.35 0-64 28.65-64 64l.0098 256C.002 483.3 28.66 512 64 512h192c35.2 0 64-28.8 64-64v-32h-47.1L272 448z"/></symbol>\
<symbol id="svgFilePDF" viewBox="0 0 384 512"><path d="M320 464C328.8 464 336 456.8 336 448V416H384V448C384 483.3 355.3 512 320 512H64C28.65 512 0 483.3 0 448V416H48V448C48 456.8 55.16 464 64 464H320zM256 160C238.3 160 224 145.7 224 128V48H64C55.16 48 48 55.16 48 64V192H0V64C0 28.65 28.65 0 64 0H229.5C246.5 0 262.7 6.743 274.7 18.75L365.3 109.3C377.3 121.3 384 137.5 384 154.5V192H336V160H256zM88 224C118.9 224 144 249.1 144 280C144 310.9 118.9 336 88 336H80V368C80 376.8 72.84 384 64 384C55.16 384 48 376.8 48 368V240C48 231.2 55.16 224 64 224H88zM112 280C112 266.7 101.3 256 88 256H80V304H88C101.3 304 112 293.3 112 280zM160 240C160 231.2 167.2 224 176 224H200C226.5 224 248 245.5 248 272V336C248 362.5 226.5 384 200 384H176C167.2 384 160 376.8 160 368V240zM192 352H200C208.8 352 216 344.8 216 336V272C216 263.2 208.8 256 200 256H192V352zM336 224C344.8 224 352 231.2 352 240C352 248.8 344.8 256 336 256H304V288H336C344.8 288 352 295.2 352 304C352 312.8 344.8 320 336 320H304V368C304 376.8 296.8 384 288 384C279.2 384 272 376.8 272 368V240C272 231.2 279.2 224 288 224H336z"/></symbol>\
<symbol id="svgFileZip" viewBox="0 0 384 512"><path d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0L64-.0001c-35.35 0-64 28.65-64 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h48V64h64V48.13h48.01L224 128c0 17.67 14.33 32 32 32h79.1V448zM176 96h-64v32h64V96zM176 160h-64v32h64V160zM176 224h-64l-30.56 116.5C73.51 379.5 103.7 416 144.3 416c40.26 0 70.45-36.3 62.68-75.15L176 224zM160 368H128c-8.836 0-16-7.164-16-16s7.164-16 16-16h32c8.836 0 16 7.164 16 16S168.8 368 160 368z"/></symbol>\
<symbol id="svgList" viewBox="0 0 512 512"><path d="M40 48C26.7 48 16 58.7 16 72v48c0 13.3 10.7 24 24 24H88c13.3 0 24-10.7 24-24V72c0-13.3-10.7-24-24-24H40zM192 64c-17.7 0-32 14.3-32 32s14.3 32 32 32H480c17.7 0 32-14.3 32-32s-14.3-32-32-32H192zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32H480c17.7 0 32-14.3 32-32s-14.3-32-32-32H192zm0 160c-17.7 0-32 14.3-32 32s14.3 32 32 32H480c17.7 0 32-14.3 32-32s-14.3-32-32-32H192zM16 232v48c0 13.3 10.7 24 24 24H88c13.3 0 24-10.7 24-24V232c0-13.3-10.7-24-24-24H40c-13.3 0-24 10.7-24 24zM40 368c-13.3 0-24 10.7-24 24v48c0 13.3 10.7 24 24 24H88c13.3 0 24-10.7 24-24V392c0-13.3-10.7-24-24-24H40z"/></symbol>\
<symbol id="svgMagnifyGlass" viewBox="0 0 512 512"><path d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352c79.5 0 144-64.5 144-144s-64.5-144-144-144S64 128.5 64 208s64.5 144 144 144z"/></symbol>\
<symbol id="svgMoon" viewBox="0 0 512 512"><path d="M421.6 379.9c-.6641 0-1.35 .0625-2.049 .1953c-11.24 2.143-22.37 3.17-33.32 3.17c-94.81 0-174.1-77.14-174.1-175.5c0-63.19 33.79-121.3 88.73-152.6c8.467-4.812 6.339-17.66-3.279-19.44c-11.2-2.078-29.53-3.746-40.9-3.746C132.3 31.1 32 132.2 32 256c0 123.6 100.1 224 223.8 224c69.04 0 132.1-31.45 173.8-82.93C435.3 389.1 429.1 379.9 421.6 379.9zM255.8 432C158.9 432 80 353 80 256c0-76.32 48.77-141.4 116.7-165.8C175.2 125 163.2 165.6 163.2 207.8c0 99.44 65.13 183.9 154.9 212.8C298.5 428.1 277.4 432 255.8 432z"/></symbol>\
<symbol id="svgQuestion" viewBox="0 0 320 512"><path d="M96 96c-17.7 0-32 14.3-32 32s-14.3 32-32 32s-32-14.3-32-32C0 75 43 32 96 32h97c70.1 0 127 56.9 127 127c0 52.4-32.2 99.4-81 118.4l-63 24.5 0 18.1c0 17.7-14.3 32-32 32s-32-14.3-32-32V301.9c0-26.4 16.2-50.1 40.8-59.6l63-24.5C240 208.3 256 185 256 159c0-34.8-28.2-63-63-63H96zm48 384c-22.1 0-40-17.9-40-40s17.9-40 40-40s40 17.9 40 40s-17.9 40-40 40z"/></symbol>\
<symbol id="svgSun" viewBox="0 0 512 512"><path d="M505.2 324.8l-47.73-68.78l47.75-68.81c7.359-10.62 8.797-24.12 3.844-36.06c-4.969-11.94-15.52-20.44-28.22-22.72l-82.39-14.88l-14.89-82.41c-2.281-12.72-10.76-23.25-22.69-28.22c-11.97-4.936-25.42-3.498-36.12 3.844L256 54.49L187.2 6.709C176.5-.6016 163.1-2.039 151.1 2.896c-11.92 4.971-20.4 15.5-22.7 28.19l-14.89 82.44L31.15 128.4C18.42 130.7 7.854 139.2 2.9 151.2C-2.051 163.1-.5996 176.6 6.775 187.2l47.73 68.78l-47.75 68.81c-7.359 10.62-8.795 24.12-3.844 36.06c4.969 11.94 15.52 20.44 28.22 22.72l82.39 14.88l14.89 82.41c2.297 12.72 10.78 23.25 22.7 28.22c11.95 4.906 25.44 3.531 36.09-3.844L256 457.5l68.83 47.78C331.3 509.7 338.8 512 346.3 512c4.906 0 9.859-.9687 14.56-2.906c11.92-4.969 20.4-15.5 22.7-28.19l14.89-82.44l82.37-14.88c12.73-2.281 23.3-10.78 28.25-22.75C514.1 348.9 512.6 335.4 505.2 324.8zM456.8 339.2l-99.61 18l-18 99.63L256 399.1L172.8 456.8l-18-99.63l-99.61-18L112.9 255.1L55.23 172.8l99.61-18l18-99.63L256 112.9l83.15-57.75l18.02 99.66l99.61 18L399.1 255.1L456.8 339.2zM256 143.1c-61.85 0-111.1 50.14-111.1 111.1c0 61.85 50.15 111.1 111.1 111.1s111.1-50.14 111.1-111.1C367.1 194.1 317.8 143.1 256 143.1zM256 319.1c-35.28 0-63.99-28.71-63.99-63.99S220.7 192 256 192s63.99 28.71 63.99 63.1S291.3 319.1 256 319.1z"/></symbol>\
</defs></svg>';


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


cse111.createSVG = function(id, clss, attrs) {
	const xmlns = 'http://www.w3.org/2000/svg';
	const symbol = document.getElementById(id);
	const viewBox = symbol.getAttributeNS(null, 'viewBox');

	let use = document.createElementNS(xmlns, 'use');
	use.setAttributeNS(null, 'href', '#' + id);

	let svg = document.createElementNS(xmlns, 'svg');
	svg.setAttributeNS(null, 'viewBox', viewBox);
	if (clss) {
		svg.classList.add(clss);
	}
	if (attrs) {
		for (name in attrs) {
			svg.setAttribute(name, attrs[name]);
		}
	}
	svg.appendChild(use);

	return svg;
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

			// Add the SVG image cache to the document.
			const xmlns = 'http://www.w3.org/2000/svg';
			let cache = document.createElementNS(xmlns, 'svg');
				cache.classList.add('cache');
				cache.innerHTML = cse111.svgCache;
			document.body.appendChild(cache);

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
			let menuIcon = cse111.createSVG('svgBars', 'menuIcon',
					{title : strings.menuHint, alt : strings.menuHint});
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
		function addMenuItem(id, text, hint, action, classes, down) {
			let svg = cse111.createSVG(id);
			let node = document.createTextNode(' ' + text);
			let item = createElem('li', classes, {title : hint});
			if (typeof(action) == 'function') {
				item.appendChild(svg);
				item.appendChild(node);
				item.addEventListener('click', action);
			}
			else if (typeof(action) == 'string') {
				let anchor = createElem('a', null,
						down ?
						{download : '', href : action} :
						{href : action});
				anchor.appendChild(svg);
				anchor.appendChild(node);
				item.appendChild(anchor);
			}
			ul.appendChild(item);
		}

		// Create the menu items.
		addMenuItem('svgSun', strings.lightText,
				strings.lightHint,
				function() { self.setBrightness('light'); },
				['light']);
		addMenuItem('svgMoon', strings.darkText,
				strings.darkHint,
				function() { self.setBrightness('dark'); },
				['dark']);

		addMenuItem('svgList', strings.contentsText,
				strings.contentsHint, filenames.contents, ['first']);

		const head = document.head;
		const prev = head.querySelector('link[rel="prev"]');
		const next = head.querySelector('link[rel="next"]');
		if (prev) {
			addMenuItem('svgArrowLeft', strings.prevText,
					strings.prevHint, prev.href);
		}
		if (next) {
			addMenuItem('svgArrowRight', strings.nextText,
					strings.nextHint, next.href);
		}

		addMenuItem('svgMagnifyGlass', strings.searchText,
				strings.searchHint, filenames.search, ['first']);
		addMenuItem('svgQuestion', strings.helpText,
				strings.helpHint, filenames.help);

		if (document.location.protocol != 'file:') {
			addMenuItem('svgFilePDF', strings.pdfText,
					strings.pdfHint, filenames.pdfFile, ['first'], true);
			addMenuItem('svgFileZip', strings.zipText,
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

			let up = cse111.createSVG('svgArrowUp', 'up',
					{alt : strings.upHint, title : strings.upHint});
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

				let span = document.createElem('span');
				pre.appendChild(span);
				let count = code.split(newline).length;
				for (let n = 2;  n <= count;  ++n) {
					pre.appendChild(document.createTextNode('\n'));
					span = document.createElement('span');
					span.textContent = n.toString();
					pre.appendChild(span);
				}
			}
		}
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
		const createSVG = cse111.createSVG;
		const createElem = cse111.createElement;

		// Add a copy button with a click listener to each
		// <div class="example"> element.
		let elements = document.body.querySelectorAll('div.example');
		for (let div of elements) {
			let image = createSVG('svgCopy', null, {'alt' : copyHint});
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
			const splitURL = /^.+\/([^\/]+\/[^\/]+)$/;
			const strings = cse111.strings;
			const viewText = cse111.strings.viewText + ' ';
			const downText = cse111.strings.downloadText + ' ';
			const createElem = cse111.createElement;

			for (let link of links) {
				// Get the absolute href.
				let absURL = link.href;

				// Get the relative href.
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
