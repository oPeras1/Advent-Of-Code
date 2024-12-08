#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Function to split a string by a delimiter
vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to convert a vector of strings to a vector of integers
vector<int> toIntVector(const vector<string>& strVec) {
    vector<int> intVec;
    for (const string& s : strVec) {
        intVec.push_back(stoi(s));
    }
    return intVec;
}

int main() {
    ifstream inputFile("../../input.txt");


    string data((istreambuf_iterator<char>(inputFile)), istreambuf_iterator<char>());
    inputFile.close();

    size_t separator = data.find("\n\n");
    string part1 = data.substr(0, separator);
    string part2 = data.substr(separator + 2);

    vector<pair<int, int>> rules;
    istringstream part1Stream(part1);
    string line;
    while (getline(part1Stream, line)) {
        vector<string> ruleParts = split(line, '|');
        rules.emplace_back(stoi(ruleParts[0]), stoi(ruleParts[1]));
    }

    vector<vector<int>> updates;
    istringstream part2Stream(part2);
    while (getline(part2Stream, line)) {
        vector<string> updateParts = split(line, ',');
        updates.push_back(toIntVector(updateParts));
    }

    int count = 0;
    for (const auto& update : updates) {
        bool valid = true;

        for (const auto& rule : rules) {
            int val1 = rule.first;
            int val2 = rule.second;

            auto it1 = find(update.begin(), update.end(), val1);
            auto it2 = find(update.begin(), update.end(), val2);

            if (it1 != update.end() && it2 != update.end()) {
                int index1 = distance(update.begin(), it1);
                int index2 = distance(update.begin(), it2);

                if (index1 > index2) {
                    valid = false;
                    break;
                }
            }
        }

        if (valid) {
            int length = update.size();
            count += update[length / 2];
        }
    }

    cout << count << endl;

    return 0;
}
