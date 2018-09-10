#!/usr/bin

read -p "Object: " shape


if [ -n "${shape}" ]; then
	echo "Rendering a ${shape}."

	place=$(find ./ -name "${shape}*")
	echo $(python ${place} $@)

elif [ -z "${shape}" ]; then
	echo "Welp"

fi
