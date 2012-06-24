#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in(argv[1]);
    ofstream out("words");
    string s;
    string w;
    while(in.good()) {
	in>>w;
	out<<w<<"\n";
	getline(in, s);
    }
    return 0;
}
