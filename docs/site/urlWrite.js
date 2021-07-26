/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

/* The url object modifies all <a> tags (links) so that
 * 1. Visits to external links and links with the download attribute are
 * recorded when the user clicks them. All other links (links to
 * internal, non-downloaded documents) are recorded when the document
 * loads.
 * 2. All links except ones with the download attribute open in a new
 * window. */

cse111.url.openDoc = function() {
	console.log('openDoc()');
	this.writeView(document.referrer, window.location.href);
};


cse111.url.byuicse = /(file:\/\/\/.+\/docs\/|https:\/\/byui-cse\.github\.io\/cse111-course\/)/;
cse111.url.protocol = /[^:]+:\/+/;


/** Records that a user viewed a document. */
cse111.url.writeView = function(source, target) {
	console.log('writeView(' + source + ', ' + target + ')');
	try {
		const byuicse = this.byuicse;
		const protocol = this.protocol;

		const abbreviate = function(url) {
			console.log('    abbreviate(' + url + ')');
			let remove = byuicse.test(url) ? byuicse : protocol;
			let abbrev = url.replace(remove, '');
			return abbrev;
		};

		source = this.encodeURL(abbreviate(source));
		target = this.encodeURL(abbreviate(target));
		const tzo = new Date().getTimezoneOffset();

		let db = this.initDatabase();
		let ref = db.ref('/views/' + target);
		let obj = {
			'referrer':source,
			'when':firebase.database.ServerValue.TIMESTAMP,
			'tzo':tzo
		};
		ref.push(obj);
		setTimeout(function() { db.goOffline(); }, 2000);
	}
	catch (ex) {
		console.log('Error: ' + JSON.stringify(ex));
	}
};


/** Modifies all <a> tags (links) so that they perform as described at
 * the top of this file. */
cse111.url.modifyLinks = function() {
	console.log('modifyLinks()');
	const self = this;

	const openSolutionLink = function(event) {
		const link = event.currentTarget;
		const href = link.getAttribute('href');
		self.openSolutionLink(href);
		// Cancel the default action of the <a> tag.
		event.preventDefault();
		return false;
	};

	const openDownloadLink = function(event) {
		const link = event.currentTarget;
		const href = link.getAttribute('href');
		console.log('openDownloadLink(' + href + ')');
		self.writeView(window.location.href, href);
		window.open(href);
		// Cancel the default action of the <a> tag.
		event.preventDefault();
		return false;
	};

	const openExternalLink = function(event) {
		const link = event.currentTarget;
		const href = link.getAttribute('href');
		console.log('openExternalLink(' + href + ')');
		self.writeView(window.location.href, href);
		window.open(href, '_blank');
		// Cancel the default action of the <a> tag.
		event.preventDefault();
		return false;
	};

	const openOtherLink = function(event) {
		const link = event.currentTarget;
		const href = link.getAttribute('href');
		console.log('openOtherLink(' + href + ')');
		window.open(href, '_blank');
		// Cancel the default action of the <a> tag.
		event.preventDefault();
		return false;
	};

	const links = document.getElementsByTagName('a');
	for (let i = 0, len = links.length;  i < len;  ++i) {
		const link = links[i];
		const href = link.href;

		if (link.classList.contains('solution')) {
			// Process an <a class="solution"> element.
			const filename = this.getFilename(href);

			link.addEventListener('click', openSolutionLink);
			link.setAttribute('title', 'View ' + filename);

			let downlink = document.createElement('a');
			downlink.setAttribute('download', '');
			downlink.setAttribute('title', 'Download ' + filename);
			downlink.addEventListener('click', openDownloadLink);
			downlink.setAttribute('href', href);
			downlink.innerHTML = '[&darr;]';

			let parent = link.parentNode;
			let next = link.nextSibling;
			parent.insertBefore(document.createTextNode(' '), next);
			parent.insertBefore(downlink, next);
		}
		else if (link.hasAttribute('download')) {
			// Process an <a download> element.
			link.addEventListener('click', openDownloadLink);
		}
		else if (!this.byuicse.test(href) && this.protocol.test(href)) {
			// Process an <a> element that links to an external document.
			link.addEventListener('click', openExternalLink);
		}
		else {
			// Process any other <a> element.
			link.addEventListener('click', openOtherLink);
		}
	}
};


cse111.url.openSolutionLink = function(href) {
	console.log('openSolutionLink(' + href + ')');
	const self = this;
	fetch(href)
	.then(function(response) {
		response.text()
		.then(function(text) {
			self.showCode(href, text);
		})
		.catch(function(error) {
			console.log(JSON.stringify(error));
		});
	})
	.catch(function(error) {
		console.log(JSON.stringify(error));
	});
};


/** Shows the code that was retrieved by the
 * openSolutionLink function in a new tab. */
cse111.url.showCode = function(href, code) {
	console.log('showCode(' + href + ', )');

	/** Converts the characters &, <, and > to HTML entities and
	 * converts non-ascii charaters to HTML entity sequences. */
	const entityFromChar = function(plain) {
		const symbols = {
			'&':'&amp;', '<':'&lt;', '>':'&gt;',
			'\u2018':'&lsquo;', '\u2019':'&rsquo;',
			'\u201c':'&ldquo;', '\u201d':'&rdquo;'
		};
		const keys = Object.keys(symbols).join('');
		const regex = new RegExp('[' + keys + ']', 'g');

		// Encode characters in symbols as HTML entities.
		let intermed = plain.replace(regex,
				function(match0) { return symbols[match0]; });

		// Encode non-ascii characters as HTML entities.
		let encoded = intermed.replace(/[^\t\n\r -~]/g,
				function(match0) {
					var pt = match0.charCodeAt(0);
					var hex = pt.toString(16);
					return '&#x' + '0000'.substring(hex.length) + hex + ';';
				});

		return encoded;
	};

	const filename = this.getFilename(href);
	code = entityFromChar(code.trim());

	const loc = window.location.href;
	const base = loc.replace(/\/[^\/]+\/[^\/]+$/, '');
	const icon = base + '/site/icon.png';
	const style = base + '/site/style.css';
	const codestyle = base + '/site/hljs/vscode.css';
	const color = base + '/site/color.js';
	const linenums = base + '/site/linenums.js';
	const hljs = base + '/site/hljs/highlight.pack.js';

	const html =
['<!DOCTYPE html>',
'<!-- Copyright 2020, Brigham Young University - Idaho. All rights reserved. -->',
'<html lang="en-us">',
'<head>',
'\t<meta charset="UTF-8">',
'\t<title>' + filename + '</title>',
'\t<link rel="icon" type="image/png" href="' + icon + '">',
'\t<link rel="stylesheet" type="text/css" href="' + style + '">',
'\t<link rel="stylesheet" type="text/css" href="' + codestyle + '">',
'\t<script src="' + color + '"><\x2fscript>',
'\t<script src="' + linenums + '"><\x2fscript>',
'\t<script src="' + hljs + '"><\x2fscript>',
'\t',
'</head>',
'',
'<body>',
'<header>',
'\t<div class="colorCtrl">&nbsp;</div>',
'\t<div class="logo">',
'\t\t<div class="upper">BYU</div>',
'\t\t<div class="lower">Idaho</div>',
'\t</div>',
'\t<h2>CSE 111 | <span>Programming with Functions</span></h2>',
'</header>',
'',
'<article class="solution">',
'\t<h1>' + filename + ' <a download title="Download ' + filename + '" href="' + href + '">[&darr;]</a></h1>',
'\t<div class="pre">',
'<pre class="linenums"></pre>',
'<pre class="python">' + code + '</pre>',
'\t</div>',
'</article>',
'',
'<footer>',
'\t<small>Copyright &copy; 2020, Brigham Young University - Idaho. All',
'\trights reserved.</small>',
'</footer>',
'</body>',
'</html>'].join('\n');
	let win = window.open();
	let doc = win.document;
	doc.write(html);
	doc.close();
};


cse111.url.getFilename = function(path) {
	return path.substring(path.lastIndexOf('/') + 1);
};


window.addEventListener('DOMContentLoaded', function(){cse111.url.openDoc();});
window.addEventListener('DOMContentLoaded', function(){cse111.url.modifyLinks();});
