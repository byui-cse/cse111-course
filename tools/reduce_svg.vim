20 minutes

:%s;><;><;g
:%s; \(stroke-\(linecap\|linejoin\|miterlimit\)\|\(clip\|fill\)-rule\)="[^"]\+";;g
:g/ fill-opacity="0.0"/d
:%s/ fill="#000000" stroke="#000000" stroke-width="1.0"/ class="tip"/
:%s/ fill="#85200c" stroke="#85200c" stroke-width="1.0"/ class="red tip"/
:%s/ fill="#6aa84f" stroke="#6aa84f" stroke-width="1.0"/ class="green tip"/
:%s/ fill="#0076b6" stroke="#0076b6" stroke-width="1.0"/ class="blue tip"/
:%s/ fill="#666666" stroke="#666666" stroke-width="1.0"/ class="gray tip"/
:%s/ stroke="#000000" stroke-width="1.0" stroke-dasharray="4.0,3.0"/ class="return"/
:%s/ stroke="#85200c" stroke-width="1.0" stroke-dasharray="4.0,3.0"/ class="red return"/
:%s/ stroke="#6aa84f" stroke-width="1.0" stroke-dasharray="4.0,3.0"/ class="green return"/
:%s/ stroke="#0076b6" stroke-width="1.0" stroke-dasharray="4.0,3.0"/ class="blue return"/
:%s/ stroke="#666666" stroke-width="1.0" stroke-dasharray="4.0,3.0"/ class="gray return"/
:%s/ stroke="#000000" stroke-width="1.0"/ class="call"/
:%s/ stroke="#85200c" stroke-width="1.0"/ class="red shaft"/
:%s/ stroke="#6aa84f" stroke-width="1.0"/ class="green shaft"/
:%s/ stroke="#0076b6" stroke-width="1.0"/ class="blue shaft"/
:%s/ stroke="#666666" stroke-width="1.0"/ class="gray shaft"/
:%s/ fill="#fce5cd"/ class="user"/
:%s/ fill="#cfe2f3"/ class="std"/

:44,$s;\(d="m\)\([^ ]\);\1 \2;
:44,$s;\([0-9.]\)\([acl]\)\([-.0-9]\);\1 \2 \3;g
:44,$s;\([^ ]\)\(z\?"/>\);\1 \2;

:44,$s;\([^ ]\)\(-\);\1 \2;g
:44,$s;-\.;-0.;g
:44,$s;\(\.[0-9]\+\)\.\([0-9]\+\);\1 0.\2;

:44,$s; \?\([mcl]\) ;\1 ;g
:44,$s; \?\(z\?"/>\); \1;
:g/^[mcl] /s/ /	/g


:%s/\s\+$//
:44,$s/	/ /g
:44,$s/\([- ]\)0\(\.[0-9]\)/\1\2/g
:44,$s/ \(-[.0-9]\)/\1/g
:44,$s/\([0-9]\) \./\1./g
:44,$s/\(^[mcl]\) \([-.0-9]\)/\1\2/
Jx
:44,$s;\(<path\) \(class="\(call\|return\)"\);</g><g \2>\1 class="shaft";
