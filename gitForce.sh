#!/bin/bash

echo -n "Force: "
read force

echo -n  "Repository: "
read Repo

if [ "${force}" = "push" ]; then
    echo $(git status)
	echo -n "Files to add: "
	read add

	echo $(git add ${add})

	echo -n "Exclusively pushing a README.md or _config.yml? [y/n] "
    read readme

	if [[ ${readme} = "y" ]]; then
        echo $(cp -rp $(pwd)/README.md $(pwd)/_include)
        echo "README.md has been updated in _include/"

        echo $(cp -rp $(pwd)/_config.yml $(pwd)/_include)
        echo "_config.yml has been updated in _include/"

		echo $(git commit -m 'Update README.md')
		echo "README.md has been committing."

		echo $(git push ${Repo} master)
		echo "A force has been applied to ${Repo}"

	elif [[ "${readme}" = "n" ]]; then
		echo $(git commit -m "Update")
		echo "Files are committed."

        echo $(git push ${Repo} master)
        echo "A force has been applied to ${Repo}."

    elif [[ -z ${readme} ]]; then
        echo ""
    fi

elif [ "${force}" = "pull" ]; then
	echo $(git pull ${Repo} master)
	echo "Force has been applied to local repository."

elif [ "${force}" = "fetch" ]; then
    echo $(git fetch ${Repo} master)
    echo "The frisbee has been caught."

elif [ -z "${force}" ] && [ -z "${Repo}" ]; then
    echo "Zero Newtons of force applied."

fi

