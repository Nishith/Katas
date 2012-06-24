#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    if(argc != 3){
	cout<<"Usage: ./across dictionary input";
	return 0;
    }

    vector <string> dict;
    ifstream in(argv[1]);
    string w;
    while(in.good()){
	in>>w;
	dict.push_back(w);
    }

    
    // Create the input grid
    ifstream input(argv[2]);
    int n;
    input>>n;
    string grid[n][5];
    for (int i = 0; i < n; ++i)
    {
	for (int j = 0; j < 5; ++j)
	{
	    input>>grid[i][j];
	}
    }

    string word;

    bool found = false;
    vector <string> words;
    vector <string>::iterator it;
    for (int i = 0; i < 5; ++i)
    {
	found = false;
	for (int j = 0; j < 5 && found == false; ++j)
	{
	    for (int k = 0; k < 5 && found == false; ++k)
	    {
		for (int l = 0; l < 5 && found == false; ++l)
		{
		    for (int m = 0; m < 5 && found == false; ++m)
		    {
			word = grid[i][0] + grid[j][1] + grid[k][2] + grid[l][3] + grid[m][4];
			it = find(dict.begin(), dict.end(), word);
			if(it != dict.end())
			{
			    grid[i][0] = "**";
			    grid[j][1] = "**";
			    grid[k][2] = "**";
			    grid[l][3] = "**";
			    grid[m][4] = "**";
			    words.push_back(word);
			    found = true;
			}
		    }
		}
	    }
	}
    }

    cout<<"Found words: ";
    for (int i = 0; i < words.size(); ++i)
    {
	cout<<words[i]<<", ";
    }

    cout<<endl;
    
    return 0;
}
