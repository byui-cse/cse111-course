/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.color = {
	addSchemeHandler : function() {
		let schemeData = {
			dark : {remove:'light', add:'dark',
					symbol:'\u263c', title:'Change to light mode'},
			light : {remove:'dark', add:'light',
					symbol:'\u263e', title:'Change to dark mode'}
		};

		let set = function(clist, scheme) {
			let data = schemeData[scheme];
			localStorage.setItem('colorScheme', data.add);
			clist.remove(data.remove);
			clist.add(data.add);
			let ctrls = document.getElementsByClassName('colorCtrl');
			for (let c = 0;  c < ctrls.length;  ++c) {
				let elem = ctrls[c];
				elem.setAttribute('title', data.title);
				elem.innerHTML = data.symbol;
			}
		};

		let toggle = function(event) {
			let clist = document.body.classList;
			let scheme = clist.contains('dark') ? 'light' : 'dark';
			set(clist, scheme);
		};

		let clist = document.body.classList;
		let scheme = localStorage.getItem('colorScheme');
		if (!scheme) {
			scheme = clist.contains('dark') ? 'dark' : 'light';
		}
		set(clist, scheme);
		let ctrls = document.getElementsByClassName('colorCtrl');
		for (let c = 0;  c < ctrls.length;  ++c) {
			ctrls[c].addEventListener('click', toggle);
		}
	}
};
