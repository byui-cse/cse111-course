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
		const symbols = this.symbols;
		return url.replace(this.symbolsRegex,
				function(match0) { return symbols[match0]; });
	},

	decodeURL : function(url) {
		const encodings = this.encodings;
		return url.replace(this.encodingsRegex,
				function(match0) { return encodings[match0]; });
	}
};


cse111.url.makeEncodings();
