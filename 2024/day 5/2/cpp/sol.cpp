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

vector<string> lines;
int rows, cols;
int word_len;
string word;

bool is_xmas(int x, int y);

int main() {
    ifstream inputFile("../../input.txt");

    for (string line; getline(inputFile, line);) {
        lines.push_back(line);
    }

    rows = lines.size();
    cols = lines[0].size();

    word = "MAS";
    word_len = word.size();

    int count = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (is_xmas(i, j)) {
                count++;
            }
        }
    }

    cout << count << endl;
}

bool is_xmas(int x, int y) {
    if (x - 1 < 0 || x + 1 >= rows || y - 1 < 0 || y + 1 >= cols) {
        return false;
    }

    string diag1;
    string diag2;

    for (int i = -1; i < word_len-1; i++) {
        diag1 += lines[x + i][y + i];
        diag2 += lines[x + i][y - i];
    }

    if ((diag1 == word || diag1 == string(word.rbegin(), word.rend())) and (diag2 == word || diag2 == string(word.rbegin(), word.rend()))) {
        return true;
    }

    return false;
}

//g++ sol.cpp -o sol; ./sol