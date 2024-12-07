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

bool simulate_with_obstruction(const vector<string>& map_data, pair<int, int> new_obstruction) {
    vector<string> grid = map_data;
    grid[new_obstruction.first][new_obstruction.second] = '#';

    auto pos = getpos();
    char dir = pos.first;
    int x = pos.second.second;
    int y = pos.second.first;

    set<pair<pair<int, int>, char>> visited_states;
    int rows = grid.size(), cols = grid[0].size();

    while (true) {
        auto state = make_pair(make_pair(y, x), dir);

        if (visited_states.find(state) != visited_states.end()) {
            return true;
        }
        visited_states.insert(state);

        pair<int, int> direction = directions[dir];
        pair<int, int> new_pos = {y + direction.first, x + direction.second};

        if (new_pos.first < 0 || new_pos.first >= rows || new_pos.second < 0 || new_pos.second >= cols) {
            break;
        }

        if (grid[new_pos.first][new_pos.second] == '#') {
            dir = turnRight[dir];
        } else {
            y = new_pos.first;
            x = new_pos.second;
        }
    }

    return false;
}

int main() {
    ifstream inputFile("../../input.txt");

    for (string line; getline(inputFile, line);) {
        lines.push_back(line);
    }

    inputFile.close();

    int rows = lines.size();
    int cols = lines[0].size();
    int possible_positions = 0;

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (lines[r][c] == '.') {
                if (simulate_with_obstruction(lines, {r, c})) {
                    possible_positions++;
                }
            }
        }
    }

    cout << possible_positions << endl;

    return 0;
}