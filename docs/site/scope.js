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
	attributes : {
		scope : 'data-scope',
		def   : 'data-varDef',
		use   : 'data-varUse'
	},


	addScopeHandlers : function(/* HTML ID's as strings */) {
		const selectors = this.selectors;
		for (let i = 0;  i < arguments.length;  ++i) {
			let div = $('#' + arguments[i]);
			div.find(selectors.def)
				.mouseover(this.showScope)
				.mouseout(this.hideScope);
		}
	},

	addVarHandlers : function(/* HTML ID's as strings */) {
		const selectors = this.selectors;
		const attrs = this.attributes;
		for (let i = 0;  i < arguments.length;  ++i) {
			let div = $('#' + arguments[i]);
			div.find(selectors.def)
				.each(function(index, elem) {
					let span = $(elem);
					let text = span.text();
					span.attr(attrs.def, text);
				})
				.mouseover(this.showVars)
				.mouseout(this.hideVars);
			div.find(selectors.use)
				.each(function(index, elem) {
					let span = $(elem);
					let text = span.text();
					span.attr(attrs.use, text);
				})
				.mouseover(this.showVars)
				.mouseout(this.hideVars);
		}
	},


	showScope : function(event) {
		const selectors = cse111.scope.selectors;
		const classes = cse111.scope.classes;
		// span holds a variable definition.
		let span = $(event.target);
		span.addClass(classes.hiDef);
		span.closest(selectors.scope).addClass(classes.hiScope);
	},

	hideScope : function(event) {
		const selectors = cse111.scope.selectors;
		const classes = cse111.scope.classes;
		// span holds a variable definition.
		let span = $(event.target);
		span.removeClass(classes.hiDef);
		span.closest(selectors.scope).removeClass(classes.hiScope);
	},


	showVars : function(event) {
		const classes = cse111.scope.classes;
		// span holds a variable definition or use.
		let span = $(event.target);
		let def = cse111.scope.findDefinition(span);
		if (def.length > 0) {
			let uses = cse111.scope.findUses(def);
			def.addClass(classes.hiDef);
			uses.addClass(classes.hiUse);
		}
		else {
			span.addClass(classes.hiErr);
		}
	},

	hideVars : function(event) {
		const classes = cse111.scope.classes;
		// span holds a variable definition or use.
		let span = $(event.target);
		let def = cse111.scope.findDefinition(span);
		if (def.length > 0) {
			let uses = cse111.scope.findUses(def);
			def.removeClass(classes.hiDef);
			uses.removeClass(classes.hiUse);
		}
		else {
			span.removeClass(classes.hiErr);
		}
	},


	/** Finds and returns the variable definition for the variable
	 * that is inside span. span contains a definition or a use. */
	findDefinition : function(span) {
		const selectors = this.selectors;
		const attrs = this.attributes;

		let def = span.closest(selectors.def);
		if (def.length > 0) {
			def = def.first();
		}
		else {
			span = span.closest(selectors.use);
			const name = span.attr(attrs.use);
			const selDef = '[' + attrs.def + '="' + name + '"]';
			let scope = span;
			do {
				scope = scope.parent().closest(selectors.scope);

				// Find all definitions of variables with name.
				def = scope.find(selDef);

				// Remove definitions that are within a different scope.
				scope.find(selectors.scope).each(function(index, elem) {
					let childScope = $(elem);
					def = def.not(childScope.find(selDef));
				});
			} while (scope.length > 0 && def.length == 0);
		}
		return def;
	},

	/** Finds and returns a list of spans that contain
	 * a use of the variable that is defined in def. */
	findUses : function(def) {
		const selectors = this.selectors;
		const attrs = this.attributes;

		def = def.closest(selectors.def);
		let name = def.attr(attrs.def);
		let scope = def.closest(selectors.scope);
		const selDef = '[' + attrs.def + '="' + name + '"]';
		const selUse = '[' + attrs.use + '="' + name + '"]';

		// Find all uses of variables with name.
		let uses = scope.find(selUse);

		// Remove uses for variables that are
		// defined within a different scope.
		scope.find(selectors.scope).each(function(index, elem) {
			let childScope = $(elem);
			if (childScope.find(selDef).length > 0) {
				uses = uses.not(childScope.find(selUse));
			}
		});

		return uses;
	}
};
