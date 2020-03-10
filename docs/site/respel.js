/* Copyright 2018 by Rex A. Barzee. All rights reserved. */
"use strict";

let simpleSpel = {
	list : [
		['achieve', 'acheve', 's', 'd', '-e ing', 'ment'],
		['active', 'activ', 'ly'],
		['add', 'ad', 's', 'ed', 'ing'],
		['advertise', 'advertize', 's', 'd', '-e ing', 'ment'],
		['aesthetic', 'esthetic'],
		['aghast', 'agast'],
		['ahead', 'ahed'],
		['alpha', 'alfa', 'bet', 'bets', 'betic'],
		['already', 'alredy'],
		['although', 'altho'],
		['analyse', 'analize', 's', 'd', '-e ing'],
		['analysis', 'analisis', '-is es'],
		['analyze', 'analize', 's', 'd', '-e ing'],
		['answer', 'anser', 's', 'ed', 'ing'],
		['any', 'eny'],
		['architect', 'arcitect', 's', 'ure'],
		['are', 'ar', "n't"],

		['because', 'becaus'],
		['been', 'ben'],
		['befriend', 'befrend', 's', 'ed', 'ing'],
		['beleaguer', 'beleager', 'ed'],
		['belief', 'belefe', 's'],
		['believe', 'beleve', 's', 'd', '-e ing'],
		['bight', 'bite'],
		['bill', 'bil', 's', 'ed', 'ing'],
		['bless', 'bles'],
		['blight', 'blite'],
		['bluff', 'bluf', 's'],
		['bomb', 'bom', 's'],
		['bombed', 'bommed', '-ed ing'],
		['bough', 'bou', 's'],
		['bought', 'baut'],
		['breakfast', 'brekfast'],
		['breath', 'breth'],
		['bright', 'brite'],
		['brighten', 'briten', 'er', 'ed', 'ing'],
		['brought', 'braut'],
		['burlesque', 'burlesk'],

		['caffeine', 'caffene'],
		['campaign', 'campain', 's', 'ed', 'ing'],
		['catalogue', 'catalog', 's'],
		['catalogued', 'cataloged', '-ed ing'],
		['caught', 'caut'],
		['centre', 'center', 's'],
		['centred', 'centered'],
		['character', 'caracter', 's', 'ization'],
		['chemist', 'cemist', 's', 'ry'],
		['chimney', 'chimny'],
		['climb', 'clime'],
		['climbed', 'climed', '-ed ing'],
		['colour', 'color', 's', 'ed', 'ing'],
		['comb', 'coam', 's', 'ed', 'ing'],
		['conterfeit', 'conterfit', 's', 'ed', 'ing'],
		['cough', 'cauf', 'ed', 'ing'],
		['could', 'cud', "n't"],

		['daughter', 'dauter'],
		['debt', 'det', 's', 'or'],
		['deceive', 'deceve', 's', 'd', '-e ing'],
		['definite', 'definit', 'ly'],
		['delight', 'delite'],
		['demonstrate', 'demmonstrate', 's', 'd', '-e ing'],
		['do', 'du'],
		['doll', 'dol', 's'],
		['dough', 'doe'],
		['doughty', 'douty'],
		['draught', 'draft', 's', 'ed', 'ing'],
		['dumb', 'dum'],
		['dumber', 'dummer'],

		['egg', 'eg', 's'],
		['enlighten', 'enliten', 'ed', 'ing'],
		['enough', 'enuf'],
		['examine', 'examin', 's', 'ed'],
		['exceed', 'excede', 's', 'ed', 'ing'],

		['favourite', 'favorit', 's'],
		['fight', 'fite', 's'],
		['fighting', 'fiting'],
		['flavour', 'flavor', 's', 'ed', 'ing'],
		['flight', 'flite', 's'],
		['foetus', 'fetus'],
		['foreign', 'foren', 'er', 'ers'],
		['forfeit', 'forfit', 's', 'ed', 'ing'],
		['fought', 'faut'],
		['fraught', 'fraut'],
		['freeze', 'freze', 's', '-e ing'],
		['freight', 'frate'],
		['friend', 'frend', 's'],
		['fright', 'frite'],
		['frighten', 'friten', 'ed', 'ing'],
		['fulfill', 'fulfil'],

		['gauze', 'gauz'],
		['ghost', 'gost', 's', 'ed', 'ing'],
		['give', 'giv', 's'],
		['glass', 'glas', 'es', 'ed', 'ing'],
		['gone', 'gon'],
		['guard', 'gard', 's', 'ed', 'ing'],
		['guess', 'ges', 'es', 'er', 'ed', 'ing'],

		['have', 'hav', "n't"],
		['head', 'hed', 's', 'er', 'ed', 'ing'],
		['heart', 'hart'],
		['heifer', 'heffer', 's'],
		['height', 'hite', 's'],
		['hemorrhage', 'hemorage', 's', 'd', '-e ing'],
		['house', 'hous', 'hold'],

		['integer', 'intejer', 's'],
		['involve', 'involv', 's'],
		['island', 'iland', 's'],

		['jeopardy', 'jepardy'],

		['lamb', 'lam', 's'],
		['lambed', 'lammed', '-ed ing'],
		['laugh', 'laf', 's', 'ed', 'ing'],
		['league', 'leag', 's'],
		['learn', 'lern', 'er', 'ers', 'ed', 'ing'],
		['leave', 'leav', 's'],
		['leaven', 'levven', 'ing'],
		['less', 'les', 'er'],
		['light', 'lite', 's', 'er', 'ning'],
		['lighten', 'liten', 'ed', 'ing'],
		['limb', 'lim', 's'],
		['living', 'livving'],
		['loss', 'los'],

		['maneouver', 'manuver', 's', 'ed', 'ing'],
		['many', 'meny'],
		['masquerade', 'maskerade', 's', 'd', '-e ing'],
		['measure', 'mezyur', 's'],
		['measured', 'mezyured', '-ed ing'],
		['metre', 'meter', 's'],
		['might', 'mite', 'y'],
		['mischievous', 'mischivous'],
		['mortgage', 'morgage', 's', 'd', '-e ing'],

		['native', 'nativ', 's'],
		['night', 'nite', 's'],

		['opposite', 'opposit', 's'],
		['original', 'orijinal', 's'],
		['ought', 'aut', "n't"],

		['paradigm', 'paradime', 's'],
		['photo', 'foto', 's'],
		['photograph', 'fotograf', 's', 'ic', 'ically'],
		['physical', 'fisical'],
		['piece', 'pece', 's', 'd'],
		['plight', 'plite', 's'],
		['plough', 'plow', 's', 'ed', 'ing'],
		['practise', 'practis'],
		['proceed', 'procede'],
		['prologue', 'prolog', 's'],

		['ready', 'reddy', '-y ies', '-y ied'],
		['receipt', 'receit', 's'],
		['receive', 'receve', 's', 'd', '-e ing'],
		['restore', 'restor', 's'],
		['rhetoric', 'retoric'],
		['rhubarb', 'rubarb'],
		['rhyme', 'ryme'],
		['ridge', 'rij'],
		['ridges', 'rijjes', '-es ed'],
		['right', 'rite', 's'],
		['rough', 'ruf'],
		['roughen', 'ruffen', 'ed'],

		['said', 'sed'],
		['says', 'ses'],
		['scene', 'sene', 'ry', 'ries'],
		['school', 'scool', 's', 'ed', 'ing'],
		['scissor', 'sissor', 's'],
		['seize', 'seze', 's', 'd', '-e ing'],
		['serve', 'serv', 's'],
		['should', 'shud', "n't"],
		['sieve', 'siv', 's'],
		['sight', 'site', 's'],
		['sighted', 'sited', '-ed ing'],
		['sleeve', 'sleve', 's'],
		['sleight', 'sliet'],
		['slight', 'slite'],
		['some', 'som', 'thing'],
		['sovereign', 'sovren', 's'],
		['spell', 'spel', 's'],
		['spread', 'spred', 's', 'ding'],
		['spright', 'sprite', 'ly'],
		['store', 'stor'],
		['stores', 'stors'],
		['straight', 'strate'],
		['straighten', 'straten', 'ed', 'ing'],

		['telephone', 'telefone', 's', 'd'],
		['therefore', 'therefor'],
		['thorough', 'thero'],
		['though', 'tho'],
		['thought', 'thaut', 's'],
		['thread', 'thred', 's', 'ed', 'ing'],
		['through', 'thru'],
		['thumb', 'thum', 's'],
		['thumbed', 'thummed', '-ed ing'],
		['tight', 'tite', 's'],
		['to', 'tu'],
		['tongue', 'tung', 's'],
		['touch', 'tuch', 'es', 'ed', 'ing'],
		['tough', 'tuf'],
		['toughen', 'tuffen', 'ed'],
		['tread', 'tred', 's', 'ed', 'ing'],
		['treasure', 'trezyur', 's'],
		['treasured', 'trezyured', '-ed ing'],
		['trough', 'trof'],
		['type', 'tipe'],

		['use', 'uze', 's', 'd', '-e ing'],

		['wealth', 'welth', 'y'],
		['wednesday', 'wenesday'],
		['weight', 'wate', 's'],
		['were', 'wer', "n't"],
		['would', 'wud', "n't"],

		['yeoman', 'yoman', 's'],
		['you', 'yu', 'r'],
		['young', 'yung', 'ster', 'sters']
	],

	dict : null,

	makeDict : function() {
		let dict = {};
		this.list.forEach(function(elem) {
			dict[elem[0]] = elem[1];
			for (let i = 2;  i < elem.length;  ++i) {
				let word, reword;
				let suffix = elem[i];
				if (suffix[0] == '-') {
					let elem0 = elem[0];
					let elem1 = elem[1];
					let parts = suffix.split(' ');
					let remove = parts[0].substring(1);
					suffix = parts[1];
					let remlen = remove.length;
					word = elem0.substring(0, elem0.length - remlen) + suffix;
					reword = elem1.substring(0, elem1.length - remlen) + suffix;
				}
				else {
					word = elem[0] + suffix;
					reword = elem[1] + suffix;
				}
				dict[word] = reword;
			}
		});
/*
		this.list.sort(function(s1, s2){
			const w1 = s1[0];
			const w2 = s2[0];
			let r = 0;
			if (w1 < w2) {
				r = -1;
			}
			else if (w1 > w2) {
				r = 1;
			}
			return r;
		});
		document.open();
		document.write(JSON.stringify(this.list));
		document.close();
		return;

		document.open();
		document.write(JSON.stringify(Object.keys(dict)));
		document.close();
		return;

		document.open();
		document.write(JSON.stringify(dict));
		document.close();
		return;
*/
		delete this.list;
		this.dict = dict;
	},


	adRespelLink : function() {
		let link = document.createElement('A');
		link.id = 'respelLink';
		link.innerText = '[+]'
		link.setAttribute('title', 'Simplify the spelling in this document');
		link.addEventListener('click', simpleSpel.respelHandler);
		document.body.append(link);
	},

	restorHandler : function() { simpleSpel.restorDoc(); },
	respelHandler : function() { simpleSpel.respelDoc(); },


	orijinal : null,


	restorDoc : function() {
		let link = document.getElementById('respelLink');
		link.removeEventListener('click', this.restorHandler);

		const walker = document.createTreeWalker(document.body,
				NodeFilter.SHOW_TEXT, null, false);
		let i = 0;
		let next;
		while (next = walker.nextNode()) {
			let orij = this.orijinal[i];
			if (orij) {
				next.nodeValue = orij;
			}
			i++;
		}

		delete this.orijinal;
		link.innerText = '[+]';
		link.setAttribute('title', 'Simplify the spelling in this document');
		link.addEventListener('click', this.respelHandler);
	},


	respelDoc : function() {
		let link = document.getElementById('respelLink');
		link.removeEventListener('click', this.respelHandler);
		if (!this.dict) {
			this.makeDict();
		}

		let orijinal = [];
		const charPat = /[A-Za-z]/;
		const walker = document.createTreeWalker(document.body,
				NodeFilter.SHOW_TEXT, null, false);
		let next;
		while (next = walker.nextNode()) {
			let text = next.nodeValue;
			let retext;
			if (charPat.test(text)) {
				retext = this.respelText(text);
				if (retext != text) {
					orijinal.push(text);
					next.nodeValue = retext;
				}
			}

			if (!retext || retext == text) {
				orijinal.push(null);
			}
		}

		this.orijinal = orijinal;
		link.innerText = '[-]';
		link.setAttribute('title', 'Restor the spelling in this document');
		link.addEventListener('click', this.restorHandler);
	},


	respelText : function(text) {
		const pat = /([^A-Za-z]*)([A-Za-z]+)/g;
		let matches, remain;
		let retext = '';
		while ((matches = pat.exec(text)) != null) {
			retext += matches[1];
			let word = matches[2];
			let reword = this.respelWord(word);
			retext += reword;
			remain = pat.lastIndex;
		}
		retext += text.substring(remain);
		return retext;
	},


	respelWord : function(word) {
		let lower = word.toLowerCase();
		let reword = this.dict[lower];
		if (reword) {
			reword = this.matchCase(word, reword);
		}
		else {
			reword = word;
		}
		return reword;
	},


	matchCase : function(word, reword) {
		let cased = '';
		let limit = Math.min(word.length, reword.length);
		for (let i = 0;  i < limit;  ++i) {
			let c = word[i];
			let r = reword[i];
			if (c == c.toUpperCase()) {
				r = r.toUpperCase();
			}
			cased += r;
		}
		cased += reword.substring(limit);
		return cased;
	}
};

window.addEventListener('load', simpleSpel.adRespelLink);
