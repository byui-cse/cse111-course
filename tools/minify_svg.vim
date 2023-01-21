:set ff=unix
:%s/ xmlns:xlink="[^"]\+"//
:%s/'/"/g
:%s/" \+\([^ ]\+\) \+"/"\1"/g
:%s/, */ /g  # , -> space
:%s/  \+/ /g  # multiple spaces -> one space
:%s/"#\([0-9a-zA-Z]\)\1\{5\}"/"#\1\1\1"/g  # colors
:%s/\<0\+\.0\+\>/0/g  # 0.0 -> 0
:%s/-\(0[- 0-9]\)/\1/g  # unnecessary minus
:%s/\([^0-9.]\)0\([0-9]\)/\1/g  # leading zero (BROKEN)
:%s/\<0\././g  # leading zero
:%s/\.0\>//g  # trailing .0
:%s/ -/-/g  # unneccesary spaces
:%s/\(\.[0-9]\+\) \./\1./g  # unneccesary spaces

:set ff=unix:%s/ xmlns:xlink="[^"]\+"//:%s/"#\([0-9a-zA-Z]\)\1\{5\}"/"#\1\1\1"/g:%s/\<0\+\.0\+\>/0/g:%s/\<0\././g:%s/\.0\>//g:%s/ -/-/g:%s/\(\.[0-9]\+\) \./\1./g:%s/\(\.[0-9]\+\) \./\1./g:%s/\(\.[0-9]\+\) \./\1./g:%s/\(\.[0-9]\+\) \./\1./g:%s/\(\.[0-9]\+\) \./\1./g

