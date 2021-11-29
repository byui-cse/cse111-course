/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (! window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}


cse111.url = {
	/** Modifies all <a class="solutions"> tags (links). */
	modifyLinks : function() {
		// Process all <a class="solution"> elements.
		const links = document.querySelectorAll('a.solution');

		const isLocal = /^file:\/\/\//.test(window.location);
		if (isLocal) {
			for (let i = 0;  i < links.length;  ++i) {
				const link = links[i];

				// If the user is viewing the CSE 111 files from his
				// local hard drive, there is no reason to have both a
				// view and download link. A standard download link will
				// simply open the file for viewing, so a download link
				// is sufficient.
				link.setAttribute('download', '');
			}
		}
		else {
			const splitURL = /^.+\/([^\/]+\/[^\/]+)$/;

			for (let i = 0;  i < links.length;  ++i) {
				const link = links[i];

				// Get the relative href.
				const hrefAttr = link.getAttribute('href');
				const absURL = link.href;
				const relpath = absURL.replace(splitURL, '$1');
				const newHref = '../overview/solution.html?file=' + relpath;

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
			}
		}
	},


	onLoad : function() {
		cse111.url.modifyLinks();
	}
};


window.addEventListener('DOMContentLoaded', cse111.url.onLoad);
