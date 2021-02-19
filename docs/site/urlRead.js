/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

cse111.url.signIn = function(successFunc) {
	const self = this;
	this.initFirebase();

	const provider = new firebase.auth.GoogleAuthProvider();
	firebase.auth().signInWithPopup(provider)
	.then(function(result) {
		// This gives you a Google Access Token. You can use
		// it to access the Google API.
		const token = result.credential.accessToken;

		// The signed-in user info.
		const user = result.user;
		if (user) {
			let msg =
				'Display Name: ' + user.displayName + '\n' +
				'Email: ' + user.email + ' ' +
				'Email Verified: ' + user.emailVerified + '\n' +
				'Photo URL: <a href="' + user.photoURL + '">' +
					user.photoURL + '</a>\n' +
				'Is Anonymous: ' + user.isAnonymous + '\n' +
				'User ID: ' + user.uid + '\n' +
				'Provider Data: ' + JSON.stringify(user.providerData);
			console.log(msg);
			self.getById('user').innerHTML = 'Welcome ' + user.displayName;
			self.getById('signIn').style.display = 'none';
			cse111.url.readViews('start', 'end', 'views');
		}
		else {
			self.getById('user').innerHTML = 'Not signed in';
		}
	})
	.catch(function(error) {
		let msg = 'Google sign in failed: ' + error.message;
		self.appendById('status', msg);
		console.log(msg);
	});
};


cse111.url.setDate = function(id, date) {
	if (! date) {
		date = new Date();
	}
	let str = date.toISOString().replace(/T.*/, '');
	let picker = this.getById(id);
	picker.setAttribute('value', str);
};


cse111.url.readViews = function(startId, endId, listId) {
	console.log('readViews(' + startid + ', ' + endId + ', ' + listId + ')');
	let self = this;
	console.log('this.initDatabase()');
	let db = this.initDatabase();
	console.log("db.ref('/views').get()");
	db.ref('/views').get().then(
	function(snapshot) {
		console.log('let urls = snapshot.val();');
		let urls = snapshot.val();
		let outer = this.getById(listId);
		for (let url in urls) {
			let views = urls[url];

			url = self.decode(url);
			let link = this.createElem('a');
			link.setAttribute('href', url);
			link.appendChild(this.createText(url));

			let inner = this.createElem('ol');
			for (let key in views) {
				let view = views[key];
				let when = new Date(view.when);
				when = this.createText(when.toDateString()
						+ ', ' + when.toLocaleTimeString());
				let div = this.createElem('div');
				div.appendChild(when);

				if (view.referrer.length > 0) {
					let referrer = self.decode(view.referrer);
					let link = this.createElem('a');
					link.setAttribute('href', referrer);
					link.appendChild(this.createText(referrer));

					div.appendChild(this.createElem('br'));
					div.appendChild(this.createText('referrer: '));
					div.appendChild(link);
				}

				let li = this.createElem('li');
				li.appendChild(div);
				inner.appendChild(li);
			}

			let div = this.createElem('div');
			div.appendChild(link);
			div.appendChild(inner);
			let li = this.createElem('li');
			li.appendChild(div);
			outer.appendChild(li);
		}
	})
	.catch(function(error) {
		let msg = 'Error: ' + error.message;
		self.appendById('status', msg);
		console.log(msg);
	});
};


cse111.url.createElem = function(tagName) {
	return document.createElement(tagName);
};

cse111.url.createText = function(text) {
	return document.createTextNode(text);
};

cse111.url.clearById = function(id) {
	this.getById(id).innerHTML += '';
};

cse111.url.writeById = function(id, msg) {
	this.getById(id).innerHTML = msg + '<br>\n';
};

cse111.url.appendById = function(id, msg) {
	this.getById(id).innerHTML += msg + '<br>\n';
};

cse111.url.getById = function(id) {
	return document.getElementById(id);
};
