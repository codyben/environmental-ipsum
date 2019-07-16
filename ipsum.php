<?php

header('Content-Type: application/json');

function generateParagraphs(Array $markov, int $numParagraphs, bool $cli, $lineBreaks = "<br><br>"):String
{
	$arr['request'] = true;

	$s = sizeof($markov)-1;

	$paragraph = "";

	for($i = 0; $i < $numParagraphs; $i++) {

		$sentence = "";
		$numSentences = mt_rand(3,5); //spice it up with a random number of sentences

		for ($j=0; $j <= $numSentences; $j++) { 

			if($i == 0)
				$sentence = $markov[mt_rand(1,$s)];
			else
				$sentence = " ".$markov[mt_rand(1,$s)]; //prepend a space for all other leading sentences.

			$paragraph .= str_replace("\n", " ", $sentence);
		}
		$paragraph .= $lineBreaks;
	}

	$arr['ipsum'] = $paragraph;

	if(!$cli){ //for future use
		return json_encode($arr);
	}

	return $paragraph;
}

function checkRange($r):bool //while I really didn't want to add a function call, I think it makes it cleaner.
{
	if($r > 15 || $r <= 0 || !is_numeric($r) || !isset($r))
		return false;
	return true;
}
//$r here is our return variable.

$m['request']  = false;
$r = json_encode($m);

if(array_key_exists('n', $_POST)) {

	/** Executes about x2 as fast, and uses roughly 1/3 less memory **/
	$sizeOfFile = filesize("clean_markov2.txt");
	$beginOffset = mt_rand(0, $sizeOfFile);
	$fH = fopen("clean_markov2.txt", "r");
	fseek($fH, $beginOffset, SEEK_SET);

	$f = explode("\n", stream_get_contents($fH));

	/** 

		The file() and explode() methods have similiar runtimes / mem usage, which is to be expected I guess.
		I'll have to take a look at the source, but I bet they're handled the same way under the hood, at least for default line delims. 
	
	$f = file("clean_markov2.txt"); 

	$f = explode("\n", file_get_contents("clean_markov2.txt"));

	**/

	$v = intval($_POST['n']);

	$rc = checkRange($v);

	if($rc && !array_key_exists('l',$_POST)) {

		$r = generateParagraphs($f, $v, false);

	} else if($rc) {

		$r = generateParagraphs($f, $v, false, "\n\n"); //kept in case I ever want to switch up the return value for cli calls. The only noticeable difference now is switching from <br> to new lines.
	}
}

echo $r;