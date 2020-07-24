/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.color = {
	addSchemeHandlers : function() {
		let setScheme = function(off, on) {
			localStorage.setItem('colorScheme', on);
			let clist = document.body.classList;
			clist.remove(off);
			clist.add(on);
		};
		let makeClosure = function(off, on) {
			return function() { setScheme(off, on); };
		};
		let dark = makeClosure('light', 'dark');
		let light = makeClosure('dark', 'light');

		let ctrls = document.getElementsByClassName('colorCtrls');
		for (let c = 0;  c < ctrls.length;  ++c) {
			let spans = ctrls[c].getElementsByTagName('span');
			for (let s = 0;  s < spans.length;  ++s) {
				let span = spans[s];
				let attr = span.getAttribute('name');
				if (attr == 'dark') {
					span.addEventListener('click', dark);
					span.setAttribute('title', 'Dark mode');
				}
				else if (attr == 'light') {
					span.addEventListener('click', light);
					span.setAttribute('title', 'Light mode');
				}
			}
		}

		let clist = document.body.classList;
		let scheme = localStorage.getItem('colorScheme');
		if (!scheme) {
			scheme = (clist.contains('dark') ? 'dark' : 'light');
		}
		clist.add(scheme);
	}
};
