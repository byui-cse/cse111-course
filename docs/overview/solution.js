"use strict";

if (! window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}


cse111.show = {
    readCode : function() {
        const self = this;

		const getQueryValue = function(key) {
			let query = window.location.search.substring(1);
			let vars = query.split('&');
			for (let i = 0;  i < vars.length;  i++) {
				let pair = vars[i].split('=');
				if (pair[0] == key) {
					return pair[1];
				}
			}
			return null;
		};

        let href = getQueryValue('file');
        const heading = href;
		const splitURL = /^([^\/]+)\/([^\/]+)$/;
        const lesson = href.replace(this.splitURL, '$1');
        const filename = href.replace(this.splitURL, '$2');
		href = "../" + href;

        document.title = heading;
        document.getElementsByClassName('title')[0].innerHTML = heading;

		const isPython = /^.+\.py$/;
		const isCSV = /^.+\.csv$/;
		const isTxt = /^.+\.txt$/;
		let className = null;
		if (isPython.test(filename)) {
			className = "python";
		}
		else if (isCSV.test(filename)) {
			className = "csv";
		}
		else if (isTxt.test(filename)) {
			className = "text";
		}

		if (className) {
			document.getElementById('code').classList.add(className);

			const links = document.querySelectorAll('a[download]');
			for (let i = 0;  i < links.length;  ++i) {
				let link = links[i];
				link.setAttribute('href', href);
				link.setAttribute('title', 'Download ' + href);
			}

			fetch(href)
			.then(function(response) {
				if (response.ok) {
					response.text()
					.then(function(text) {
						self.showCode(text);
					})
					.catch(function(error) {
						console.log('Error: ' + error);
					});
				}
				else {
					throw Error(response.statusText);
				}
			})
			.catch(function(error) {
				console.log('Error: ' + error);
			});
		}
    },


    /** Shows the code that was retrieved by the
     * readCode function in a new tab. */
    showCode : function(code) {

        /** Converts the characters &, <, and > to HTML entities and
         * converts non-ascii charaters to HTML entity sequences. */
        const entityFromChar = function(plain) {
            const symbols = {
                '&':'&amp;', '<':'&lt;', '>':'&gt;',
                '\u2018':'&lsquo;', '\u2019':'&rsquo;',
                '\u201c':'&ldquo;', '\u201d':'&rdquo;'
            };
            const keys = Object.keys(symbols).join('');
            const regex = new RegExp('[' + keys + ']', 'g');

            // Encode characters in symbols as HTML entities.
            let intermed = plain.replace(regex,
                    function(match0) { return symbols[match0]; });

            // Encode non-ascii characters as HTML entities.
            let encoded = intermed.replace(/[^\t\n\r -~]/g,
                    function(match0) {
                        var pt = match0.charCodeAt(0);
                        var hex = pt.toString(16);
                        return '&#x' + '0000'.substring(hex.length) + hex + ';';
                    });

            return encoded;
        };

        code = entityFromChar(code.trim());
		document.getElementById('code').innerHTML = code;
		cse111.linenums.addLineNumbers();
		hljs.highlightAll();
    },


	onLoad : function() {
		cse111.show.readCode();
	}
};


window.addEventListener('DOMContentLoaded', cse111.show.onLoad);
