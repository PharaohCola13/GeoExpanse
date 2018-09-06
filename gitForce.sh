#!/bin/bash

read -p "Force: " force
read -p "Repository: " Repo

$Repo = geometry

if [$force == 'push']
then
	read -p 'Exclusively pushing a README.md? ' readme

	if (($readme == 'yes'))
	then
		git commit -m 'Update README.md'
		echo "README.md has been commiting"

	elif (($readme == 'no'))
	then
		read -p 'Message: ' message
		git commit -m "$message"
		echo "Files are commited"

git push $Repo master
echo "Files have been pushed tp $Repo"

if [$force == 'pull']
then
	git pull $Repo master
	echo "Files have been pulled from $Repo"
		


