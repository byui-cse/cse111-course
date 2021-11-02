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
	this.writeView(document.referrer, window.location.href);
};


cse111.url.byuicse = /(file:\/\/\/.+\/docs\/|https:\/\/byui-cse\.github\.io\/cse111-course\/)/;
cse111.url.protocol = /[^:]+:\/+/;


/** Records that a user viewed a document. */
cse111.url.writeView = function(source, target) {
	try {
		const byuicse = this.byuicse;
		const protocol = this.protocol;

		const abbreviate = function(url) {
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
		console.log('Error: ' + ex.toString());
	}
};


/** Modifies all <a> tags (links) so that they perform as described at
 * the top of this file. */
cse111.url.modifyLinks = function() {
	const self = this;

	const openSolutionLink = function(event) {
		// Cancel the default action of the <a> tag.
		event.preventDefault();

		const link = event.currentTarget;
		const href = link.href;  // Get the absolute href.
		self.writeView(window.location.href, href);
		window.open(href, '_blank');

		// Cancel the default action of the <a> tag.
		return false;
	};

	const openDownloadLink = function(event) {
		// Cancel the default action of the <a> tag.
		event.preventDefault();

		const link = event.currentTarget;
		const href = link.href;  // Get the absolute href.
		self.writeView(window.location.href, href);
		window.open(href);

		// Cancel the default action of the <a> tag.
		return false;
	};

	const openExternalLink = function(event) {
		// Cancel the default action of the <a> tag.
		event.preventDefault();

		const link = event.currentTarget;
		const href = link.href;  // Get the absolute href.
		self.writeView(window.location.href, href);
		window.open(href, '_blank');

		// Cancel the default action of the <a> tag.
		return false;
	};

	const openOtherLink = function(event) {
		// Cancel the default action of the <a> tag.
		event.preventDefault();

		const link = event.currentTarget;
		const href = link.href;  // Get the absolute href.
		window.open(href, '_blank');

		// Cancel the default action of the <a> tag.
		return false;
	};

	const isLocal = /^file:\/\/\//.test(window.location);
	const splitURL = /^[^\/]+\/([^\/]+\/[^\/]+)$/;

	// document.getElementsByTagName returns a live list of elements.
	const links = document.getElementsByTagName('a');

	for (let i = 0;  i < links.length;  ++i) {
		const link = links[i];
		const href = link.href;  // Get the absolute href.

		if (link.classList.contains('solution')) {
			// Process an <a class="solution"> element.

			if (isLocal) {
				// If the user is viewing the CSE 111 files from his
				// local hard drive, there is no reason to have both a
				// view and download link. A standard download link with
				// simply open the file for viewing, so a download link
				// is sufficient.
				link.setAttribute('download', '');
				link.addEventListener('click', openDownloadLink);
			}
			else {
				// Get the relative href.
				const hrefAttr = link.getAttribute('href');
				const absURL = link.href;
				const relpath = absURL.replace(splitURL, '$1');
				const newHref = '../overview/solution.html?file=../' + relpath;
				console.log(newHref);

				link.addEventListener('click', openSolutionLink);
				link.setAttribute('title', 'View ' + hrefAttr);
				link.setAttribute('href', newHref);

				// Create a new <a download> element.
				let downlink = document.createElement('a');
				downlink.setAttribute('download', '');
				downlink.setAttribute('title', 'Download ' + hrefAttr);
				downlink.setAttribute('href', hrefAttr);
				downlink.innerHTML = '[&darr;]';

				// Insert the new element after the current
				// <a class="solution"> element.
				let parent = link.parentNode;
				let next = link.nextSibling;
				parent.insertBefore(document.createTextNode(' '), next);
				parent.insertBefore(downlink, next);

				// document.getElementsByTagName returns a live list of
				// elements. This means that the newly created element
				// will be processed the next time through this loop.
				// The next time through this loop, the code in this
				// loop will add the openDownloadLink function as a
				// click listener to the newly created element.
			}
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


cse111.url.onLoad = function() {
	cse111.url.openDoc();
	cse111.url.modifyLinks();
};


window.addEventListener('DOMContentLoaded', cse111.url.onLoad);
