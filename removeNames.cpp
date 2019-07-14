#include <string>
#include<iostream>
#include<fstream>

using namespace std;
//usage: ./removeNames > output_file.txt
int main(int argc, char const *argv[])
{
	string of;
	ifstream myReadFile;
	string out;
	int c = 0;

 	myReadFile.open("markov_initial2.txt");
 	
 	if(myReadFile.is_open()){
 		while(getline(myReadFile, out)){
 			c = 0;
 			for(int i = 0; i < out.size(); i++){
 				if(isupper(out.at(i)))
 					c++;
 				if(c > 1) //break directly out of the loop once we hit two capitals
 					break;
 			}
 			if(c > 1) //I couldn't think of a better way to handle this, like a continue 2; from PHP, so continue while loop
 				continue;
 			else
 				of += out+"\n"; //If it only has one capital (the beginning of a sentence) append to output.
 		}

 	}
 	cout << of; 
 	myReadFile.close();
	return 0;
}