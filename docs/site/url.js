/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.url = {
	openDoc : function() {
		cse111.url.reportView(document.referrer, window.location.href);
	},

	modifyLinks : function() {
		let links = document.getElementsByTagName('a');
		for (let i = 0, len = links.length;  i < len;  ++i) {
			let link = links[i];
			let href = link.href;
			if (href.startsWith('http')) {
				href = 'javascript:cse111.url.openLink("' + href + '")';
				link.setAttribute('href', href);
			}
		}
	},

	openLink : function(url) {
		cse111.url.reportView(window.location.href, url);
		window.open(url, '_blank');
	},


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
		db.goOnline();
		return db;
	},


	reportView : function(source, target) {
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
	},


	symbols : {
		'%':'%25',
		' ':'%20', '!':'%21',  '#':'%23', '&':'%26',
		',':'%2c', '.':'%2e',  '/':'%2f',
		':':'%3a', ';':'%3b',  '=':'%3d', '?':'%3f',
		'[':'%5b', '\\':'%5c', ']':'%5d'
	},

	encode : function(url) {
		for (let symbol in this.symbols) {
			let subst = this.symbols[symbol];
			url = url.replaceAll(symbol, subst);
		}
		return url;
	}
};


window.addEventListener('DOMContentLoaded', cse111.url.openDoc);
window.addEventListener('DOMContentLoaded', cse111.url.modifyLinks);
