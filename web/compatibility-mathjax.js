// add Mathjax for compatibility (Opera is dead, Chrome is broken and IE is IE)
// inspired from from https://github.com/mathjax/MathJax/issues/182
function has_mathml()
{
	// official way to test MathML
	if (!document.implementation.hasFeature("org.w3c.dom.mathml", "2.0"))
		return false;

	// like, seriously?
	if (!document.createElement)
		return false;

	// unofficial way: test MathML fractions behaviour
	var div = document.createElement("div");
	div.style.position = "absolute";
	div.style.top = div.style.left = 0;
	div.style.visibility = "hidden";
	div.style.width = div.style.height = "auto";
	div.style.fontFamily = "serif";
	div.style.lineheight = "normal";
	div.innerHTML = "<math><mfrac><mi>xx</mi><mi>yy</mi></mfrac></math>";
	document.body.appendChild(div);

	return div.offsetHeight > div.offsetWidth;
}
function mathml_compat()
{
	if (has_mathml())
		return;

	var toc = document.getElementById('TOC');
	var warning = document.createElement('p');
	warning.style.fontWeight = 'bold';
	warning.style.padding = '1em';
	warning.style.borderLeft = '2px solid red';
	warning.style.borderRight = '2px solid red';
	warning.innerHTML = 'You may want to upgrade to an <a href="https://www.mozilla.org/en-US/firefox/new/">up-to-date browser</a> which supports <a href="https://en.wikipedia.org/wiki/MathML">MathML</a>.';
	toc.parentNode.insertBefore(warning, toc);

	var mathjax = document.createElement('script');
	mathjax.src = '/mathjax/MathJax.js?config=MML_HTMLorMML.js';
	document.head.appendChild(mathjax);
}
window.addEventListener('load', mathml_compat, false);
