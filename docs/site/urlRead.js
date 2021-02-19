/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

cse111.url.setDate = function(id, date) {
	if (! date) {
		date = new Date();
	}
	let str = date.toISOString().replace(/T.*/, '');
	let picker = document.getElementById(id);
	picker.setAttribute('value', str);
};


cse111.url.readViews = function(startId, endId, listId) {
	let self = this;
	let db = this.initFirebase();
	db.ref('/views').get().then(
	function(snapshot) {
		let urls = snapshot.val();
		let outer = document.getElementById(listId);
		for (let url in urls) {
			let views = urls[url];

			url = self.decode(url);
			let link = document.createElement('a');
			link.setAttribute('href', url);
			link.appendChild(document.createTextNode(url));

			let inner = document.createElement('ol');
			for (let key in views) {
				let view = views[key];
				let when = new Date(view.when);
				when = document.createTextNode(when.toDateString()
						+ ', ' + when.toLocaleTimeString());
				let div = document.createElement('div');
				div.appendChild(when);

				if (view.referrer.length > 0) {
					let referrer = self.decode(view.referrer);
					let link = document.createElement('a');
					link.setAttribute('href', referrer);
					link.appendChild(document.createTextNode(referrer));

					div.appendChild(document.createElement('br'));
					div.appendChild(document.createTextNode('referrer: '));
					div.appendChild(link);
				}

				let li = document.createElement('li');
				li.appendChild(div);
				inner.appendChild(li);
			}

			let div = document.createElement('div');
			div.appendChild(link);
			div.appendChild(inner);
			let li = document.createElement('li');
			li.appendChild(div);
			outer.appendChild(li);
		}
	});
};
