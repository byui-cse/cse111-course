/* Copyright 2020 by Brigham Young University - Idaho. All rights reserved. */
"use strict";

if (! window.hasOwnProperty('cse111')) {
	window.cse111 = {};
}

cse111.scope = {
	classes : {
		def : 'varDef',
		use : 'varUse',
		hiScope : 'hiScope',
		hiDef   : 'hiVarDef',
		hiUse   : 'hiVarUse',
		hiErr   : 'hiError'
	},
	selectors : {
		scope : '[data-scope]',
		def   : '.varDef',
		use   : '.varUse'
	},
	attribNames : {
		scope : 'data-scope',
		def   : 'data-varDef',
		use   : 'data-varUse'
	},


	addScopeHandlers : function(/* HTML ID's as strings */) {
		const showScope = this.showScope;
		const hideScope = this.hideScope;

		function setupSpans(div, selector, attrName) {
			let spans = div.querySelectorAll(selector);
			for (let i = 0;  i < spans.length;  ++i) {
				let span = spans[i];
				span.addEventListener('mouseover', showScope);
				span.addEventListener('mouseout', hideScope);
			}
		}

		const varDef = this.selectors.def;
		for (let i = 0;  i < arguments.length;  ++i) {
			let div = document.getElementById(arguments[i]);
			setupSpans(div, varDef);
		}
	},


	addVarHandlers : function(/* HTML ID's as strings */) {
		const showVars = this.showVars;
		const hideVars = this.hideVars;

		function setupSpans(div, selector, attrName) {
			let spans = div.querySelectorAll(selector);
			for (let i = 0;  i < spans.length;  ++i) {
				let span = spans[i];
				let text = span.textContent;
				span.setAttribute(attrName, text);
				span.addEventListener('mouseover', showVars);
				span.addEventListener('mouseout', hideVars);
			}
		}

		const selectors = this.selectors;
		const attribNames = this.attribNames;
		for (let i = 0;  i < arguments.length;  ++i) {
			let div = document.getElementById(arguments[i]);
			setupSpans(div, selectors.def, attribNames.def);
			setupSpans(div, selectors.use, attribNames.use);
		}
	},


	showScope : function(event) {
		const selectors = cse111.scope.selectors;
		const classes = cse111.scope.classes;
		// span holds a variable definition.
		let span = event.target;
		span.classList.add(classes.hiDef);
		let ancestor = span.closest(selectors.scope);
		ancestor.classList.add(classes.hiScope);
	},

	hideScope : function(event) {
		const selectors = cse111.scope.selectors;
		const classes = cse111.scope.classes;
		// span holds a variable definition.
		let span = event.target;
		span.classList.remove(classes.hiDef);
		let ancestor = span.closest(selectors.scope);
		ancestor.classList.remove(classes.hiScope);
	},


	showVars : function(event) {
		const classes = cse111.scope.classes;
		// span holds a variable definition or use.
		let span = event.target;
		let varDef = cse111.scope.findDefinition(span);
		if (varDef) {
			let varUses = cse111.scope.findUses(varDef);
			varDef.classList.add(classes.hiDef);
			varUses.forEach(function(varUse) {
				varUse.classList.add(classes.hiUse);
			});
		}
		else {
			span.classList.add(classes.hiErr);
		}
	},

	hideVars : function(event) {
		const classes = cse111.scope.classes;
		// span holds a variable definition or use.
		let span = event.target;
		let varDef = cse111.scope.findDefinition(span);
		if (varDef) {
			let varUses = cse111.scope.findUses(varDef);
			varDef.classList.remove(classes.hiDef);
			varUses.forEach(function(varUse) {
				varUse.classList.remove(classes.hiUse);
			});
		}
		else {
			span.classList.remove(classes.hiErr);
		}
	},


	/** Finds and returns the variable definition
	 * for the variable that is inside span.
	 * span must contain a variable definition or use. */
	findDefinition : function(span) {
		const selectors = this.selectors;
		let varDef = span.closest(selectors.def);
		if (! varDef) {
			span = span.closest(selectors.use);
			const attribNames = this.attribNames;
			const name = span.getAttribute(attribNames.use);
			const selDef = '[' + attribNames.def + '="' + name + '"]';
			const selScope = selectors.scope;
			const removeAll = this.removeAll;
			let varDefs;
			let scope = span;
			do {

				// Get the parent scope.
				scope = scope.parentNode.closest(selScope);
				if (scope) {

					// Within the parent scope, search for the variable
					// definition.
					varDefs = Array.from(scope.querySelectorAll(selDef));
					if (varDefs.length > 0) {

						// Remove definitions that are within a different scope.
						let childScopes = scope.querySelectorAll(selScope);
						for (let i = 0;  i < childScopes.length;  ++i) {
							let childScope = childScopes[i];
							let otherDefs = childScope.querySelectorAll(selDef);
							removeAll(varDefs, otherDefs);
						}
					}
				}
			} while (scope && varDefs.length == 0);
			varDef = varDefs.length == 1 ? varDefs[0] : null;
		}
		return varDef;
	},


	/** Finds and returns an array of spans that contain
	 * a use of the variable that is defined in varDef. */
	findUses : function(varDef) {
		const selectors = this.selectors;
		const attribNames = this.attribNames;

		varDef = varDef.closest(selectors.def);
		let name = varDef.getAttribute(attribNames.def);
		let scope = varDef.closest(selectors.scope);
		const selDef = '[' + attribNames.def + '="' + name + '"]';
		const selUse = '[' + attribNames.use + '="' + name + '"]';
		const selScope = selectors.scope;

		// Find all uses of variables with name.
		let varUses = Array.from(scope.querySelectorAll(selUse));
		if (varUses.length > 0) {
			const removeAll = this.removeAll;

			// Remove uses for variables that are
			// defined within a different scope.
			let childScopes = scope.querySelectorAll(selScope);
			for (let i = 0;  i < childScopes.length;  ++i) {
				let childScope = childScopes[i];
				let otherDefs = childScope.querySelectorAll(selDef);
				if (otherDefs.length > 0) {
					let otherUses = childScope.querySelectorAll(selUse);
					removeAll(varUses, otherUses);
				}
			}
		}
		return varUses;
	},


	removeAll : function(array, toRemove) {
		for (let i = 0;  i < toRemove.length;  ++i) {
			let index = array.indexOf(toRemove[i]);
			if (index != -1) {
				array.splice(index, 1);
			}
		}
	}
};
