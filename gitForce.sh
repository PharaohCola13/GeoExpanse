#!/bin/bash

echo -n "Force: "
read force

echo -n  "Repository: "
read Repo

echo -n "Project Name: "
read proj

if [ "${force}" = "push" ]; then
	echo -n "Exclusively pushing a README.md? "
    read readme

	if [[ ${readme} = "yes" ]]; then
	    echo $(git status)
	    echo -n "Files to add: "
	    read add

	    echo $(git add ${add})
        echo $(cp -rp ~/PycharmProjects/Research/${proj}/README.md ~/PycharmProjects/Research/${proj}/_include)

        echo $(cp -rp ~/PycharmProjects/Research/${proj}/_config.yml ~/PycharmProjects/Research/${proj}/_include)

		echo $(git commit -m 'Update README.md')
		echo "README.md has been committing."

		echo $(git push ${Repo} master)
		echo "A force has been applied to ${Repo}"

	elif [[ "${readme}" = "no" ]]; then
		echo $(git commit -m "Update")
		echo "Files are committed."

        echo $(git push ${Repo} master)
        echo "A force has been applied to ${Repo}."

    fi

elif [ "${force}" = "pull" ]; then
	echo $(git pull ${Repo} master)
	echo "Force has been applied to local repository."

elif [ -z "${force}" ] && [ -z "${Repo}" ]; then
    echo "Zero Newtons of force applied."

fi

