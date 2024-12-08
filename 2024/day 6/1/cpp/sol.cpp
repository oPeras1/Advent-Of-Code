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

map<char, pair<int, int>> directions = {
    {'^', {-1, 0}}, {'>', {0, 1}}, {'v', {1, 0}}, {'<', {0, -1}}
};

map<char, char> turnRight = {
    {'^', '>'}, {'>', 'v'}, {'v', '<'}, {'<', '^'}
};

vector<string> lines;

pair<char, pair<int, int>> getpos() {
    for (int i = 0; i < lines.size(); i++) {
        for (int j = 0; j < lines[i].size(); j++) {
            if (directions.find(lines[i][j]) != directions.end()) {
                return {lines[i][j], {i, j}};
            }
        }
    }
    return {'^', {0, 0}};
}

int main() {
    ifstream inputFile("../../input.txt");

    for (string line; getline(inputFile, line);) {
        lines.push_back(line);
    }

    inputFile.close();

    pair<char, pair<int, int>> pos = getpos();
    char dir = pos.first;
    int x = pos.second.second;
    int y = pos.second.first;

    while (true) {
        pair<int, int> direction = directions[dir];
        pair<int, int> new_pos = {y + direction.first, x + direction.second};

        if (new_pos.first < 0 || new_pos.first >= lines.size() || new_pos.second < 0 || new_pos.second >= lines[0].size()) {
            break;
        }

        if (lines[new_pos.first][new_pos.second] == '#') {
            dir = turnRight[dir];
        } else {
            y = new_pos.first;
            x = new_pos.second;
        }

        lines[y][x] = 'X';
    }

    int count = 0;
    for (int i = 0; i < lines.size(); i++) {
        for (int j = 0; j < lines[i].size(); j++) {
            if (lines[i][j] == 'X') {
                count++;
            }
        }
    }

    cout << count << endl;

}