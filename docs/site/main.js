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
	closeHint   : 'Click to close the navigation menu',
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

	section : '§',
	copyURL : 'Copy URL to the clipboard',

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


/** Contains the filenames of user visible icons and other files so
 * that changing them, if necessary, will be easier. */
cse111.filenames = {
	logoIcon : 'site/icons/logo.png',

	contents : 'index.html',
	search   : 'index.html#search',
	help     : 'overview/help.html',
	solution : 'overview/solution.html',

	htmlFile : 'combined/cse111_prepare_content.html',
	pdfFile  : 'combined/cse111_prepare_content.pdf',
	zipFile  : 'combined/cse111_content.zip'
};


cse111.svgCache =
'<svg xmlns="http://www.w3.org/2000/svg"><style>\
.stroke{stroke-width:8;stroke-linecap:round;stroke-linejoin:round;fill:none}\
.fill{stroke:none;fill:white}\
</style><defs>\
<g id="svgBYUILogo" viewBox="0 0 88.48 52.39">\
<path d="m2.45 2.02v21.07c0 .68 0 .92-.45 1.23a4.79 4.79 0 0 1-1.73.47c-.08 0-.06.32 0 .32h17c7.18 0 10.21-2.86 10.21-7.3 0-3.3-1.53-5.31-4.57-6.06a.05.05 0 0 1 0-.1c1.93-.6 3.72-2 3.72-5.43 0-4.64-3.15-6.21-10-6.21h-16.36c-.08 0-.09.3 0 .32a4.77 4.77 0 0 1 1.74.48c.49.3.44.53.44 1.22m8 17.68v-5a3.52 3.52 0 0 0 0-.6 4.18 4.18 0 0 0 .6.05h2.79c2.22 0 4.94 0 4.94 3.08 0 2.27-2 3.08-4.57 3.08h-3.16a4.92 4.92 0 0 0-.59 0 5.44 5.44 0 0 0 0-.6m0-10v-4.42a3.68 3.68 0 0 0 0-.6 4.18 4.18 0 0 0 .6.05h3.3c2.51 0 4 .39 4 2.67 0 1.48-.91 2.81-3.88 2.81h-3.4a4.92 4.92 0 0 0-.59 0 4.92 4.92 0 0 0 0-.59"/>\
<path d="m48 25.11c.09 0 .1-.3 0-.32a4.79 4.79 0 0 1-1.74-.47c-.48-.31-.45-.55-.45-1.23v-8l8.7-12.9a6.09 6.09 0 0 1 1.17-1.41 3 3 0 0 1 .32-.22 1.65 1.65 0 0 1 .94-.24c.08 0 .1-.31 0-.31h-11.68c-.1 0-.08.31 0 .32.58 0 1.28 0 1.16.83l-5.01 7.96-5.02-7.96c-.08-.99.59-.83 1.15-.83.09 0 .11-.32 0-.32h-12.3c-.08 0-.07.28 0 .31a3.24 3.24 0 0 1 1.43.32 1.41 1.41 0 0 1 .31.21 5.52 5.52 0 0 1 1.11 1.34l8.67 12.85v8.05c0 .68.05.92-.44 1.23a4.79 4.79 0 0 1-1.74.47c-.08 0-.06.32 0 .32z"/>\
<path d="m86.1 2.02c0-.69 0-.93.44-1.23a4.79 4.79 0 0 1 1.74-.47c.08 0 .07-.31 0-.31h-12.57c-.08 0-.1.3 0 .32a3.63 3.63 0 0 1 1.64.47c.48.3.44.55.44 1.23v12.66c0 2.89-1.66 5.11-4.94 5.11s-4.94-2.22-4.94-5.11v-12.67c0-.68 0-.93.45-1.23a4 4 0 0 1 1.64-.47c.08 0 .07-.31 0-.31h-11.87c-.09 0-.07.29 0 .31a1.53 1.53 0 0 1 1 .28c.39.33.46.73.46 1.42v12.45c0 6 3.28 11.09 13.24 11.09s13.25-5.1 13.25-11.09z"/>\
<path d="m88.02 31.15h-87.67a.36.36 0 0 1 0-.72h87.67a.36.36 0 0 1 0 .72"/>\
<path d="m.2 52.3c-.07 0-.07-.29 0-.32a5.59 5.59 0 0 0 1.88-.41c.28-.17.51-.59.51-5.38v-3.55c0-4.8-.23-5.24-.51-5.39a5.59 5.59 0 0 0-1.88-.41c-.1 0-.1-.32 0-.32h6.58c.07 0 .1.29 0 .32a5.49 5.49 0 0 0-1.85.41c-.31.15-.53.59-.53 5.39v3.55c0 4.79.22 5.21.53 5.38a5.49 5.49 0 0 0 1.85.41c.13 0 .1.32 0 .32z"/>\
<path d="m18.56 37.3c-1.46 0-2.07.19-2.24.41s-.37 1.27-.37 4.82v3.63c0 3.12.23 4.34.54 4.68s1 .63 2.27.63c4.76 0 7-2.27 7-6.85a7 7 0 0 0-7.16-7.32m6.87 12.56c-1.68 1.68-3.53 2.41-6.65 2.41-1.07 0-2.8-.05-3.7-.05s-2 .05-3.09.05c-.08 0-.1-.29 0-.31a3.87 3.87 0 0 0 1.65-.42c.32-.17.52-.58.52-5.38v-3.56c0-4.79-.2-5.23-.52-5.38a3.92 3.92 0 0 0-1.65-.41c-.12 0-.1-.32 0-.32 1.07 0 2.19.06 3.09.06s3.14-.06 4.23-.06c4.9 0 8.43 3.29 8.43 7.69a8.16 8.16 0 0 1-2.31 5.68"/>\
<path d="m38.3 39.47-2.09 5.83h4.31zm3 12.78c-.07 0-.1-.29 0-.31.75-.08 1.22-.22 1.22-.59s-.32-1.51-1.71-5h-5c-1.14 3.13-1.41 4.33-1.41 4.84s.34.66 1.39.76c.09 0 .07.31 0 .31h-5c-.07 0-.13-.29 0-.31a3.18 3.18 0 0 0 1.53-.47c.24-.19.68-.53 2.44-5.33l1.29-3.55c.75-2.05 1.55-4.17 2.16-6.06.06-.18.78-.18.83 0 .74 2.11 1.37 3.84 2.22 6.06l1.38 3.55c1.9 4.8 2.22 5.16 2.56 5.38a2.91 2.91 0 0 0 1.47.42c.09 0 .06.31 0 .31z"/>\
<path d="m61.94 52.3c-.09 0-.09-.29 0-.31a3.87 3.87 0 0 0 1.65-.42c.3-.17.52-.58.52-5.38v-1.51h-9.17v1.51c0 4.8.22 5.21.51 5.38a3.94 3.94 0 0 0 1.66.42c.12 0 .12.31.05.31h-6.22c-.08 0-.1-.29 0-.31a4 4 0 0 0 1.65-.42c.32-.17.51-.58.51-5.38v-3.55c0-4.8-.19-5.24-.51-5.39a4 4 0 0 0-1.65-.41c-.12 0-.1-.32 0-.32h6.18c.07 0 .07.3-.05.32a4 4 0 0 0-1.66.41c-.29.15-.51.59-.51 5.39v1.14h9.21v-1.14c0-4.8-.22-5.24-.52-5.39a3.92 3.92 0 0 0-1.65-.41c-.12 0-.12-.32 0-.32h6.17c.09 0 .09.3 0 .32a4.09 4.09 0 0 0-1.66.41c-.29.15-.51.59-.51 5.39v3.55c0 4.8.22 5.21.51 5.38a4 4 0 0 0 1.66.42c.12 0 .12.31 0 .31z"/>\
<path d="m79.82 37.23c-4.36 0-5.8 3.48-5.8 6.62 0 4 2.51 7.64 6.41 7.64 4.33 0 5.77-3.47 5.77-6.62 0-4-2.48-7.64-6.38-7.64m.12 15.17a7.7 7.7 0 0 1-7.94-7.84 8.22 8.22 0 0 1 8.28-8.23 7.68 7.68 0 0 1 7.94 7.83 8.21 8.21 0 0 1-8.28 8.24"/>\
</g>\
<symbol id="svgBars" viewBox="0 0 56 64"><path class="stroke" d="M4,12H52M4,32H52M4,52H52"/></symbol>\
<symbol id="svgClose" viewBox="0 0 56 64"><path class="stroke" d="M12,16L44,48M12,48L44,16"/></symbol>\
<symbol id="svgLeft" viewBox="0 0 64 64"><path class="stroke" d="M56,32H8M28,12L8,32L28,52"/></symbol>\
<symbol id="svgList" viewBox="0 0 64 64"><rect x="0" y="7" width="10" height="10" rx="2"/><rect x="0" y="27" width="10" height="10" rx="2"/><rect x="0" y="47" width="10" height="10" rx="2"/><path class="stroke" d="M24,12H60M24,32H60M24,52H60"/></symbol>\
<symbol id="svgMagnify" viewBox="0 0 64 64"><path class="stroke" d="M48,26A16,16 0 1 0 4,26A16,16 0 1 0 48,26M44,44L60,60"/></symbol>\
<symbol id="svgMoon" viewBox="0 0 64 64"><path class="fill" d="M38.4,6A26,26 0 1 0 54.4,50A26,26 0 0 1 38.4,6"/></symbol>\
<symbol id="svgQuestion" viewBox="0 0 64 64"><path class="stroke" d="M16,18A16,12 0 0 1 48,18A8,12 0 0 1 42,32C40,33 36,34.5 34,35.5C30,37.25 30,37.5 30,43"/><circle class="fill" cx="30" cy="57" r="5"/></symbol>\
<symbol id="svgRight" viewBox="0 0 64 64"><path class="stroke" d="M8,32H56M36,12L56,32L36,52"/></symbol>\
<symbol id="svgSun" viewBox="0 0 64 64" class="fill"><circle cx="32" cy="32" r="16"/><path d="M51.32,26.82A20,20 0 0 151.32,37.18L64,32ZM49.32,42A20,20 0 0 142,49.32L54.63,54.63ZM37.18,51.32A20,20 0 0 126.82,51.32L32,64ZM22,49.32A20,20 0 0 114.68,42L9.37,54.63ZM12.68,37.18A20,20 0 0 112.68,26.82L0,32ZM14.68,22A20,20 0 0 122,14.68L9.37,9.37ZM26.82,12.68A20,20 0 0 137.18,12.68L32,0ZM42,14.68A20,20 0 0 149.32,22L54.63,9.37Z"/></symbol>\
<symbol id="svgUp" viewBox="0 0 48 64"><path class="stroke" d="M24,60V4M8,20L24,4L40,20"/></symbol>\
\
<!--! Font Awesome Pro 6.2.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->\
<symbol id="svgCopy" viewBox="0 0 512 512"><path d="M502.6 70.63l-61.25-61.25C435.4 3.371 427.2 0 418.7 0H255.1c-35.35 0-64 28.66-64 64l.0195 256C192 355.4 220.7 384 256 384h192c35.2 0 64-28.8 64-64V93.25C512 84.77 508.6 76.63 502.6 70.63zM464 320c0 8.836-7.164 16-16 16H255.1c-8.838 0-16-7.164-16-16L239.1 64.13c0-8.836 7.164-16 16-16h128L384 96c0 17.67 14.33 32 32 32h47.1V320zM272 448c0 8.836-7.164 16-16 16H63.1c-8.838 0-16-7.164-16-16L47.98 192.1c0-8.836 7.164-16 16-16H160V128H63.99c-35.35 0-64 28.65-64 64l.0098 256C.002 483.3 28.66 512 64 512h192c35.2 0 64-28.8 64-64v-32h-47.1L272 448z"/></symbol>\
<symbol id="svgFilePDF" viewBox="0 0 384 512"><path d="M320 464C328.8 464 336 456.8 336 448V416H384V448C384 483.3 355.3 512 320 512H64C28.65 512 0 483.3 0 448V416H48V448C48 456.8 55.16 464 64 464H320zM256 160C238.3 160 224 145.7 224 128V48H64C55.16 48 48 55.16 48 64V192H0V64C0 28.65 28.65 0 64 0H229.5C246.5 0 262.7 6.743 274.7 18.75L365.3 109.3C377.3 121.3 384 137.5 384 154.5V192H336V160H256zM88 224C118.9 224 144 249.1 144 280C144 310.9 118.9 336 88 336H80V368C80 376.8 72.84 384 64 384C55.16 384 48 376.8 48 368V240C48 231.2 55.16 224 64 224H88zM112 280C112 266.7 101.3 256 88 256H80V304H88C101.3 304 112 293.3 112 280zM160 240C160 231.2 167.2 224 176 224H200C226.5 224 248 245.5 248 272V336C248 362.5 226.5 384 200 384H176C167.2 384 160 376.8 160 368V240zM192 352H200C208.8 352 216 344.8 216 336V272C216 263.2 208.8 256 200 256H192V352zM336 224C344.8 224 352 231.2 352 240C352 248.8 344.8 256 336 256H304V288H336C344.8 288 352 295.2 352 304C352 312.8 344.8 320 336 320H304V368C304 376.8 296.8 384 288 384C279.2 384 272 376.8 272 368V240C272 231.2 279.2 224 288 224H336z"/></symbol>\
<symbol id="svgFileZip" viewBox="0 0 384 512"><path d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0L64-.0001c-35.35 0-64 28.65-64 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h48V64h64V48.13h48.01L224 128c0 17.67 14.33 32 32 32h79.1V448zM176 96h-64v32h64V96zM176 160h-64v32h64V160zM176 224h-64l-30.56 116.5C73.51 379.5 103.7 416 144.3 416c40.26 0 70.45-36.3 62.68-75.15L176 224zM160 368H128c-8.836 0-16-7.164-16-16s7.164-16 16-16h32c8.836 0 16 7.164 16 16S168.8 368 160 368z"/></symbol>\
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


cse111.createSVG = function(id, classes, title) {
	const xmlns = 'http://www.w3.org/2000/svg';
	const symbol = document.getElementById(id);
	const viewBox = symbol.getAttributeNS(null, 'viewBox');

	let use = document.createElementNS(xmlns, 'use');
	use.setAttributeNS(null, 'href', '#' + id);

	let svg = document.createElementNS(xmlns, 'svg');
	svg.setAttributeNS(null, 'viewBox', viewBox);
	if (classes) {
		for (let clss of classes) {
			svg.classList.add(clss);
		}
	}
	if (title) {
		let child = document.createElementNS(xmlns, 'title');
		child.textContent = title;
		svg.appendChild(child);
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
			const createSVG = cse111.createSVG;

			// Add the SVG image cache to the document.
			const xmlns = 'http://www.w3.org/2000/svg';
			let cache = document.createElementNS(xmlns, 'svg');
				cache.classList.add('cache');
				cache.innerHTML = cse111.svgCache;
			document.body.appendChild(cache);

			// Create the children of the header.
			let svg = createSVG('svgBYUILogo', null, strings.byuiLogoAlt);
			let byuiLogo = createElem('a', ['byuiLogo'],
					{title : strings.byuiHint, href : strings.byuiURL});
				byuiLogo.appendChild(svg);
			let courseCode = createElem('a', null,
					{title : strings.courseHint, href : filenames.contents});
				courseCode.textContent =
					strings.courseCode + ' | ' + strings.courseTitle;
			let h2 = createElem('h2');
				h2.appendChild(courseCode);
			let menuOpen = createSVG('svgBars', ['menuIcon'], strings.menuHint);
				menuOpen.setAttribute('id', 'menuOpen');
				menuOpen.addEventListener('click', this.openNavMenu);
			let menuClose = createSVG('svgClose',
					['menuIcon', 'closed'], strings.closeHint);
				menuClose.setAttribute('id', 'menuClose');
				menuClose.addEventListener('click', this.closeNavMenu);

			// Create the header.
			header = createElem('header');
				header.appendChild(byuiLogo);
				header.appendChild(h2);
				header.appendChild(menuOpen);
				header.appendChild(menuClose);

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
		const createSVG = cse111.createSVG;
		const ul = createElem('ul');

		/** Creates one menu item. */
		function addMenuItem(id, text, hint, action, classes, download) {
			let svg = cse111.createSVG(id, null, hint);
			let node = document.createTextNode(' ' + text);
			let item = createElem('li', classes, {title : hint});
			if (typeof(action) == 'function') {
				item.appendChild(svg);
				item.appendChild(node);
				item.addEventListener('click', action);
			}
			else if (typeof(action) == 'string') {
				let anchor = createElem('a', null,
						download ?
						{download : '', href : action} : {href : action});
				anchor.appendChild(svg);
				anchor.appendChild(node);
				item.appendChild(anchor);
			}
			ul.appendChild(item);
		}

		// Create the menu items.
		addMenuItem('svgSun', strings.lightText,
				strings.lightHint,
				function() { self.setBrightness('light'); }, ['light']);
		addMenuItem('svgMoon', strings.darkText,
				strings.darkHint,
				function() { self.setBrightness('dark'); }, ['dark']);

		addMenuItem('svgList', strings.contentsText,
				strings.contentsHint, filenames.contents, ['first']);

		const head = document.head;
		const prev = head.querySelector('link[rel="prev"]');
		const next = head.querySelector('link[rel="next"]');
		if (prev) {
			addMenuItem('svgLeft', strings.prevText,
					strings.prevHint, prev.href);
		}
		if (next) {
			addMenuItem('svgRight', strings.nextText,
					strings.nextHint, next.href);
		}

		addMenuItem('svgMagnify', strings.searchText,
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


	/** Opens the navigation menu. */
	openNavMenu : function(event) {
		if (event) {
			event.stopPropagation();
		}
		let nav = document.body.querySelector('nav.menu');
		if (nav) {
			nav.classList.remove('closed');
			let menuOpen = document.getElementById('menuOpen');
			let menuClose = document.getElementById('menuClose');
			menuOpen.classList.add('closed');
			menuClose.classList.remove('closed');
		}
	},

	/** Closes the navigation menu. */
	closeNavMenu : function(event) {
		if (event) {
			event.stopPropagation();
		}
		let nav = document.body.querySelector('nav.menu');
		if (nav) {
			nav.classList.add('closed');
			let menuOpen = document.getElementById('menuOpen');
			let menuClose = document.getElementById('menuClose');
			menuClose.classList.add('closed');
			menuOpen.classList.remove('closed');
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
				span.textContent = strings.section;
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

			let svg = cse111.createSVG('svgUp', null, strings.upHint);
			let button = createElem('button', ['up'],
					{type : 'button', title : strings.upHint});
			button.appendChild(svg);
			button.addEventListener('click', function(){window.scroll(0, 0);});

			footer = createElem('footer');
			footer.appendChild(div);
			footer.appendChild(button);

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
			const object = JSON.parse(script.textContent);
			if (object.hasOwnProperty('copyrightNotice')) {
				notice = object.copyrightNotice;
			}
			if (object.hasOwnProperty('dateModified')) {
				modified = object.dateModified;
			}
		}
		return {notice : notice, modified : modified};
	}
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
			let code = pre.nextElementSibling.textContent;
			if (code.length > 0) {
				let start = 1;

				// If the HTML page author put a number in the
				// current <pre class="linenums"> element, use
				// that number as the starting number.
				let numbers = pre.textContent;
				if (numbers.length > 0) {
					start = parseInt(numbers);
					if (isNaN(start)) {
						start = 1;
					}
				}

				// If the pre.linenums element contains
				// any children nodes, remove them.
				pre.replaceChildren();

				let span = document.createElement('span');
				span.textContent = start.toString();
				pre.appendChild(span);
				let limit = start + code.split(newline).length;
				for (let n = start + 1;  n < limit;  ++n) {
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
			let image = createSVG('svgCopy', null, copyHint);
			let button = createElem('button', ['copy'],
					{type : 'button', title : copyHint});
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
