/* This script properly aligns equation numbers */

function $(query)
{
	// shorthand to select DOM nodes
	return document.querySelectorAll(query);
}

function foreach(list, fun)
{
	// apply fun() on each element of the list
	for (var i = 0; i < list.length; i++)
		fun(list[i]);
}

function remove(element)
{
	// remove DOM node element
	element.parentNode.removeChild(element);
}

function DOMnew(parent, tag, children=[])
{
	// create new DOM element of type tag with given children
	var element = document.createElement(tag);
	foreach(children, function(child){
		element.appendChild(child);
	});
	parent.appendChild(element);
	return element;
}

function bbox(element)
{
	// return bounding box of element in document coordinates
	var rect = element.getBoundingClientRect()
	return {
		'top':    rect.top     + document.documentElement.scrollTop,
		'bottom': rect.bottom  + document.documentElement.scrollTop,
		'left':   rect.left    + document.documentElement.scrollLeft,
		'right':  rect.right   + document.documentElement.scrollLeft,
		'width':  rect.width,
		'height': rect.height,
	};
}

var references;

function references_init()
{
	// find references locations
	references = [];
	foreach($('math a'), function(anchor){
		// find math context
		var math = anchor;
		while (math.tagName != 'math')
			math = math.parentNode;

		// save anchor information
		anchor.padding = 0;
		anchor.offsetTop = bbox(anchor).top - bbox(math).top;

		// move anchor to new MathML context
		remove(anchor);
		var newmath = DOMnew(document.body, 'math', [anchor]);
		newmath.setAttribute('display', 'block');

		// save reference for later udpating
		references.push([math, newmath, anchor]);
	});

	// do first update
	references_update();
}

function references_update()
{
	// update reference positions
	foreach(references, function(reference){
		var [oldmath, newmath, anchor] = reference;

		// add padding so that the anchor points to the top of oldmath
		anchor.padding = .5 * parseFloat(getComputedStyle(anchor).fontSize);
		anchor.setAttribute('style', 'display: inline-block; padding: ' + anchor.padding + 'px 0');

		// update position
		var right = bbox(document.documentElement).width - bbox(oldmath).right;
		var top = bbox(oldmath).top + anchor.offsetTop - anchor.padding;
		newmath.setAttribute('style',
			'position: absolute;' +
			'right: ' + right + 'px;' +
			'top: ' + top + 'px;'
		);
	});
}

window.addEventListener('load', references_init, false);
window.addEventListener('resize', references_update, false);
