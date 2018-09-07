#!/usr/bin

echo -n "Object: "
read shape

echo "Rendering a ${shape}."

#if [ -n "${shape}" ]; then
dirPath = $(find ./ -name "${shape}*.py")

python "${dirPath}" "$@"
	
#elif [ -z "${shape}" ]; then
#	echo "Welp"
#fi 
