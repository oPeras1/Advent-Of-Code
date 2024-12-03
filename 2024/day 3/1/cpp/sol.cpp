#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <fstream>
#include <numeric>
#include <regex>


using namespace std;

int main() {
    ifstream inputFile("../../input.txt");

    string text;

    text.assign((istreambuf_iterator<char>(inputFile)), (istreambuf_iterator<char>()));

    //regex to put into a vector, everything that is inside "mul(x,y)"
    vector<string> v;
    regex reg("mul\\((\\d+),(\\d+)\\)");
    smatch match;

    std::string::const_iterator searchStart(text.cbegin());
    while (regex_search(searchStart, text.cend(), match, reg)) {
        v.push_back(match.str());
        searchStart = match.suffix().first;
    }

    int count = 0;
    for (auto s : v) {
        int n1 = stoi(s.substr(4, s.find(",") - 4));
        int n2 = stoi(s.substr(s.find(",") + 1, s.size() - s.find(",") - 2));
        count += n1 * n2;
    }

    inputFile.close();

    cout << count << endl;
}