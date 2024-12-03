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
#include <iterator>


using namespace std;

int main() {
    ifstream inputFile("../../input.txt");

    string text;

    text.assign((istreambuf_iterator<char>(inputFile)), (istreambuf_iterator<char>()));

    regex combined_pattern(R"((mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\)))");
    smatch match;

    vector<int> v;
    bool doo = true;

    string::const_iterator searchStart(text.cbegin());
    while (regex_search(searchStart, text.cend(), match, combined_pattern)) {
        if (match[1].matched) {
            if (doo) {
                int n1 = stoi(match[2].str());
                int n2 = stoi(match[3].str());
                v.push_back(n1 * n2);
            }
        } else if (match[4].matched) {
            doo = true;
        } else if (match[5].matched) {
            doo = false;
        }
        searchStart = match.suffix().first;
    }

    int count = 0;
    for (auto s : v) {
        count += s;
    }

    inputFile.close();

    cout << count << endl;
}