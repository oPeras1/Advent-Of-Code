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
vector<pair<int, int>> directions;

bool is_valid(int x, int y, int dx, int dy);

int main() {
    ifstream inputFile("../../input.txt");

    for (string line; getline(inputFile, line);) {
        lines.push_back(line);
    }

    rows = lines.size();
    cols = lines[0].size();

    word = "XMAS";
    word_len = word.size();

    directions = {
        {0, 1}, 
        {0, -1},
        {1, 0},
        {-1, 0},
        {1, 1}, 
        {-1, -1},
        {1, -1}, 
        {-1, 1} 
    };

    int count = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            for (auto dir: directions) {
                int dx = dir.first;
                int dy = dir.second;
                count += is_valid(i, j, dx, dy);
            }
        }
    }

    cout << count << endl;
}

bool is_valid(int x, int y, int dx, int dy) {
    for (int i = 0; i < word_len; i++) {
        int nx = x + i * dx;
        int ny = y + i * dy;

        if (!(0 <= nx && nx < rows and 0 <= ny and ny < cols and lines[nx][ny] == word[i])) {
            return false;
        }
    }
    return true;
}

//g++ sol.cpp -o sol; ./sol