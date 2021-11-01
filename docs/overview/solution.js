"use strict";

if (!window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}


cse111.sol = {
    readSolution : function() {
        const self = this;
        const href = this.getQueryValue('file');
        const regex = /^(.+)\/([^\/]+)\/([^\/]+)$/;
        const lesson = href.replace(regex, '$2');
        const filename = href.replace(regex, '$3');
        const heading = lesson + '/' + filename;

        document.title = filename;
        document.getElementsByClassName('title')[0].innerHTML = heading;

        fetch(href)
        .then(function(response) {
            if (response.ok) {
                response.text()
                .then(function(text) {
                    self.showCode(href, text);
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
    },


    /** Shows the code that was retrieved by the
     * readSolution function in a new tab. */
    showCode : function(href, code) {
        //this.writeView(window.location.href, href);

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

        const regex = /^(.+)\/([^\/]+)\/([^\/]+)$/;
        const base = href.replace(regex, '$1');
        const lesson = href.replace(regex, '$2');
        const filename = href.replace(regex, '$3');

        code = entityFromChar(code.trim());
		document.getElementsByClassName('python')[0].innerHTML = code;
		cse111.linenums.addLineNumbers();
		hljs.highlightAll();
    },


    getQueryValue : function(key) {
        let query = window.location.search.substring(1);
        let vars = query.split('&');
        for (let i = 0;  i < vars.length;  i++) {
            let pair = vars[i].split('=');
            if (pair[0] == key) {
                return pair[1];
            }
        }
        return null;
    }
};


window.addEventListener('DOMContentLoaded', function(){cse111.sol.readSolution();});

