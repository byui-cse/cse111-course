/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (!window.hasOwnProperty('cse111')) {
    window.cse111 = {};
}

cse111.solution = {
    modifyLinks : function() {
		const getFilename = cse111.solution.getFilename;

        let links = document.getElementsByTagName('a');
        for (let i = 0, len = links.length;  i < len;  ++i) {
            let link = links[i];
            if (link.classList.contains('solution')) {
                let href = link.href;
				let filename = getFilename(href);
                let call = 'javascript:cse111.solution.getCode("' + href + '")';
                link.setAttribute('href', call);

				let downlink = document.createElement('a');
				downlink.className = 'download';
				downlink.setAttribute('download', '');
				downlink.setAttribute('title', 'Download ' + filename);
				downlink.setAttribute('href', href);
				downlink.innerHTML = '[&darr;]';

				let parent = link.parentNode;
				let next = link.nextSibling;
				parent.insertBefore(document.createTextNode(' '), next);
				parent.insertBefore(downlink, next);
            }
        }
    },


    getCode : function(href) {
		const getFilename = cse111.solution.getFilename;

        const showCode = function(href, code) {
            const filename = getFilename(href);
            code = entityFromChar(code.trim());

            const base = window.location.origin + '/site/';
            const icon = base + 'icon.png';
            const style = base + 'style.css';
            const codestyle = base + 'hljs/vscode.css';
            const color = base + 'color.js';
            const linenums = base + 'linenums.js';
            const hljs = base + 'hljs/highlight.pack.js';

            const html =
['<!DOCTYPE html>',
'<!-- Copyright 2020, Brigham Young University - Idaho. All rights reserved. -->',
'<html lang="en-us">',
'<head>',
'\t<meta charset="UTF-8">',
'\t<title>' + filename + '</title>',
'\t<link rel="icon" type="image/png" href="' + icon + '">',
'\t<link rel="stylesheet" type="text/css" href="' + style + '">',
'\t<link rel="stylesheet" type="text/css" href="' + codestyle + '">',
'\t<script src="' + color + '"><\x2fscript>',
'\t<script src="' + linenums + '"><\x2fscript>',
'\t<script src="' + hljs + '"><\x2fscript>',
'\t',
'</head>',
'',
'<body>',
'<header>',
'\t<div class="colorCtrl">&nbsp;</div>',
'\t<div class="logo">',
'\t\t<div class="upper">BYU</div>',
'\t\t<div class="lower">Idaho</div>',
'\t</div>',
'\t<h1>CSE 111 | <span>Programming with Functions</span></h1>',
'</header>',
'',
'<article class="solution">',
'\t<h1>' + filename + ' <a download title="Download ' + filename + '" href="' + href + '">[&darr;]</a></h1>',
'\t<div class="pre">',
'<pre class="linenums"></pre>',
'<pre class="python">' + code + '</pre>',
'\t</div>',
'</article>',
'',
'<footer>',
'\t<small>Copyright &copy; 2020, Brigham Young University - Idaho. All',
'\trights reserved.</small>',
'</footer>',
'</body>',
'</html>'].join('\n');
            let win = window.open('text/html', true);
            let doc = win.document;
            doc.write(html);
            doc.close();
        };


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

        fetch(href)
        .then(function(response) {
            response.text()
            .then(function(text) {
                showCode(href, text);
            })
            .catch(function(error) {
                console.log(JSON.stringify(error));
            });
        })
        .catch(function(error) {
            console.log(JSON.stringify(error));
        });
    },


	getFilename : function(path) {
		return path.substring(path.lastIndexOf('/') + 1);
	}
};


window.addEventListener('DOMContentLoaded', cse111.solution.modifyLinks);
