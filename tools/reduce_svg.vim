:%s;><;><;g
:%s; \(stroke-\(linecap\|linejoin\|miterlimit\)\|\(clip\|fill\)-rule\)="[^"]\+";;g
:g/ fill-opacity="0.0"/d
:%s/ fill="#000000" stroke="#000000" stroke-width="1.0"/ class="tip"/
:%s/ stroke="#000000" stroke-width="1.0" stroke-dasharray="4.0,3.0"/ class="return"/
:%s/ stroke="#000000" stroke-width="1.0"/ class="call"/

:50,$s;\(d="m\)\([^ ]\);\1 \2;
:50,$s;\([0-9.]\)\([acl]\)\([-.0-9]\);\1 \2 \3;g
:50,$s;\([^ ]\)\(z\?"/>\);\1 \2;

:50,$s;\([^ ]\)\(-\);\1 \2;g
:50,$s;-\.;-0.;g
:50,$s;\(\.[0-9]\+\)\.\([0-9]\+\);\1 0.\2;

:50,$s; \?\([mcl]\) ;\1 ;g
:50,$s; \?\(z\?"/>\); \1;
:g/^[mcl] /s/ /	/g


:%s/\s\+$//
:50,$s/	/ /g
:50,$s/\([- ]\)0\(\.[0-9]\)/\1\2/g
:50,$s/ \(-[.0-9]\)/\1/g
:50,$s/\([0-9]\) \./\1./g
:50,$s/\(^[mcl]\) \([-.0-9]\)/\1\2/
Jx
:50,$s;\(<path\) \(class="\(call\|return\)"\);</g><g \2>\1 class="shaft";
