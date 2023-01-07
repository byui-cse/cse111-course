#!/usr/bin/bash

declare -a FOLDERS=("combined"
		"lesson01" "lesson02" "lesson03" "lesson04"
		"lesson05" "lesson06" "lesson07" "lesson08"
		"lesson09" "lesson10" "lesson11" "lesson11wwb"
		"lesson12" "lesson12wwb" "lesson13" "lesson13wwb"
		"lesson14" "overview")

for FOLDER in ${FOLDERS[@]}
do
	echo
	echo ${FOLDER}
	for FILE in ${FOLDER}/*.html
	do
		echo "${FILE}"
		D=$(git log $(git log --pretty="format:%H" ${FILE} | tail -1) \
			--pretty="format:%ci" ${FILE})
		echo "\"datePublished\": \"${D}\""
		D=$(git log -1 --pretty="format:%ci" ${FILE})
		echo "\"dateModified\": \"${D}\""
	done
done

exit 0
