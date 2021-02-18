/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.url = {
	database : null,

	initFirebase : function() {
		let db = this.database;
		if (! db) {
			let config = {
				apiKey: 'AIzaSyAnFi9Z3H4V1yaC1JMDtxuuoNdMecLFw-k',
				authDomain: 'cse111.firebaseapp.com',
				projectId: 'cse111',
				storageBucket: 'cse111.appspot.com',
				messagingSenderId: '735777231553',
				appId: '1:735777231553:web:6579714c57ba923839ba40'
			};

			// Initialize Firebase realtime database.
			firebase.initializeApp(config);
			db = this.database = firebase.database();
		}
		return db;
	},


	readViews : function(id) {
		let self = this;
		let db = this.initFirebase();
		db.ref('/views').get().then(
		function(snapshot) {
			let urls = snapshot.val();
			let outer = document.getElementById(id);
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
	},


	symbols : {
		'%':'%25',
		' ':'%20', '!':'%21',  '#':'%23', '&':'%26',
		',':'%2c', '.':'%2e',  '/':'%2f',
		':':'%3a', ';':'%3b',  '=':'%3d', '?':'%3f',
		'[':'%5b', '\\':'%5c', ']':'%5d'
	},

	encodings : null,

	decode : function(url) {
		let encodings = this.encodings;
		if (! encodings) {
			encodings = {};
			for (let symbol in this.symbols) {
				let subst = this.symbols[symbol];
				encodings[subst] = symbol;
			}
			this.encodings = encodings;
		}

		for (let subst in encodings) {
			let symbol = encodings[subst];
			url = url.replaceAll(subst, symbol);
		}
		return url;
	}
};
