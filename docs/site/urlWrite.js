/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

cse111.url.openDoc = function() {
	cse111.url.writeView(document.referrer, window.location.href);
};


cse111.url.modifyLinks = function() {
	let links = document.getElementsByTagName('a');
	for (let i = 0, len = links.length;  i < len;  ++i) {
		let link = links[i];
		let href = link.href;
		if (href.startsWith('http')) {
			href = 'javascript:cse111.url.openLink("' + href + '")';
			link.setAttribute('href', href);
		}
	}
};

cse111.url.openLink = function(url) {
	cse111.url.writeView(window.location.href, url);
	window.open(url, '_blank');
};


cse111.url.writeView = function(source, target) {
	try {
		source = this.encode(source);
		target = this.encode(target);

		let db = this.initFirebase();
		let ref = db.ref('/views/' + target);
		let obj = {
			'referrer':source,
			'when':firebase.database.ServerValue.TIMESTAMP
		};
		ref.push(obj);
		setTimeout(function() { db.goOffline(); }, 2000);
	}
	catch (ex) {
		console.log(JSON.stringify(ex));
	}
};


window.addEventListener('DOMContentLoaded', cse111.url.openDoc);
window.addEventListener('DOMContentLoaded', cse111.url.modifyLinks);
