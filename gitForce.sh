#!/bin/bash

echo -n "Force: "
read force

echo -n  "Repository: "
read Repo


if [ "${force}" = "push" ]; then
	echo -n "Exclusively pushing a README.md? "
    read readme

	if [[ ${readme} = "yes" ]]; then
		echo $(git commit -m 'Update README.md')
		echo "README.md has been committing."

	elif [[ "${readme}" = "no" ]]; then
		echo $(git commit -m "Update")
		echo "Files are committed."

    echo $(git push ${Repo} master)
    echo "Force has been applied to ${Repo}."

    fi

elif [ "${force}" = "pull" ]; then
	echo $(git pull ${Repo} master)
	echo "Force has been applied to local repository."

elif [ -z "${force}" ] && [ -z "${Repo}" ]; then
    echo "Zero Newtons of force applied."

fi

