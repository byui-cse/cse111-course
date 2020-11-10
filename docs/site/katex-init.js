/* Startup scripts for katex rendering */
renderMathInElement(document.body,
{
	delimiters: [
		{left: "$$", right: "$$", display: true},
		{left: "$", right: "$", display: false},
	]
});