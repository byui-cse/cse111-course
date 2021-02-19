/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.url = {
	initFirebase : function() {
		if (! firebase.apps.length) {
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
		}
	},

	database : null,

	initDatabase : function() {
		let db = this.database;
		if (! db) {
			this.initFirebase();
			db = this.database = firebase.database();
		}
		db.goOnline();
		return db;
	},


	symbols : {
		'%':'%25',
		' ':'%20', '!':'%21',  '#':'%23', '&':'%26',
		',':'%2c', '.':'%2e',  '/':'%2f',
		':':'%3a', ';':'%3b',  '=':'%3d', '?':'%3f',
		'[':'%5b', '\\':'%5c', ']':'%5d'
	},

	encodings : null,

	makeEncodings : function() {
		let encodings = this.encodings;
		if (! encodings) {
			encodings = {};
			let symbols = this.symbols;
			for (let symbol in symbols) {
				encodings[symbols[symbol]] = symbol;
			}
			this.encodings = encodings;
		}
	},

	encode : function(url) {
		return this.translate(url, this.symbols);
	},

	decode : function(url) {
		return this.translate(url, this.encodings);
	},

	translate : function(url, dict) {
		for (let key in dict) {
			url = url.replaceAll(key, dict[key]);
		}
		return url;
	}
};


cse111.url.makeEncodings();
