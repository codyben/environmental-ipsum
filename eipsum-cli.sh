#!/bin/bash

which jq > /dev/null;
rVal=$?;

if [ $rVal ]; then
	if [[ $1 ]]; then
		if [[ $1 -gt "15" ]]; then
			echo "$1 was too large";
		else
			echo -e "\n";
			curl -s 'https://www.environmental-ipsum.com/ipsum.php' --data "n=$1&l=true" --compressed | jq -r '.ipsum';
		fi
	else
		echo "usage: $0 (number)";
	fi
else
	echo "jq doesn't appear to be installed."; #I'm still iffy I want to use jq or just modify the backend to not return json for cli calls
	echo "install it via apt: sudo apt install jq";
fi