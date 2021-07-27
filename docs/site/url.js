/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.url = {
	initFirebase : function() {
		console.log("initFirebase()");
		if (! firebase.apps.length) {
			console.log("    initFirebase() 2");
			let config = {
				apiKey: 'AIzaSyAnFi9Z3H4V1yaC1JMDtxuuoNdMecLFw-k',
				authDomain: 'cse111.firebaseapp.com',
				projectId: 'cse111',
				storageBucket: 'cse111.appspot.com',
				messagingSenderId: '735777231553',
				appId: '1:735777231553:web:6579714c57ba923839ba40'
			};

			console.log("    initFirebase() 3");
			// Initialize Firebase realtime database.
			firebase.initializeApp(config);
			console.log("    initFirebase() 4");
		}
	},

	database : null,

	initDatabase : function() {
		console.log("initDatabase()");
		let db = this.database;
		if (! db) {
			this.initFirebase();
			console.log("    initDatabase() 2");
			db = this.database = firebase.database();
		}
		console.log("    initDatabase() 3");
		db.goOnline();
		console.log("    initDatabase() 4");
		return db;
	},


	symbols : {
		'%':'%25',
		' ':'%20', '!':'%21',  '#':'%23', '&':'%26',
		',':'%2c', '.':'%2e',  '/':'%2f',
		':':'%3a', ';':'%3b',  '=':'%3d', '?':'%3f',
		'[':'%5b', '\\':'%5c', ']':'%5d'
	},
	symbolsRegex : null,
	encodings : null,
	encodingsRegex : null,

	makeEncodings : function() {
		let encodings = this.encodings;
		if (! encodings) {
			const keys = Object.keys(this.symbols).join('');
			this.symbolsRegex = new RegExp('[' + keys + ']', 'g');

			encodings = {};
			let values = [];
			let symbols = this.symbols;
			for (let symbol in symbols) {
				let value = symbols[symbol];
				encodings[value] = symbol;
				values.push(value.replace('%', ''));
			}
			this.encodings = encodings;
			this.encodingsRegex = new RegExp('%('+ values.join('|') +')', 'g');
		}
	},

	encodeURL : function(url) {
		//return this.translate(url, this.symbols);
		const symbols = this.symbols;
		return url.replace(this.symbolsRegex,
				function(match0) { return symbols[match0]; });
	},

	decodeURL : function(url) {
		//return this.translate(url, this.encodings);
		const encodings = this.encodings;
		return url.replace(this.encodingsRegex,
				function(match0) { return encodings[match0]; });
	}

	//translate : function(url, dict) {
	//	for (let key in dict) {
	//		url = url.replaceAll(key, dict[key]);
	//	}
	//	return url;
	//}
};


cse111.url.makeEncodings();
