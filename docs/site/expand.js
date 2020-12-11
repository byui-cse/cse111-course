/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty("cse111")) {
	window.cse111 = {};
}

cse111.expand = {
	addExpandHandlers : function() {
		const toggle = function(event) {
			let target = event.target;
			let parent = target.parentElement;
			let clist = parent.classList;
			let data = clist.contains('expand') ?
				{title:'Collapse', remove:'expand', add:'collaps'} :
				{title:'Expand', remove:'collaps', add:'expand'};
			clist.remove(data.remove);
			clist.add(data.add);
			target.setAttribute('title', data.title);
		};

        const elems = document.getElementsByClassName('expand');
        for (let e = 0;  e < elems.length;  ++e) {
            let elem = elems[e];
            let titles = elem.getElementsByClassName('title');
            for (let t = 0;  t < titles.length;  ++t) {
                let title = titles[t];
                title.setAttribute('title', 'Expand');
                title.addEventListener('click', toggle);
            }
        }
	}
};

window.addEventListener("DOMContentLoaded", cse111.expand.addExpandHandlers);
