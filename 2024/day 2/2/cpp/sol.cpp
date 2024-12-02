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

using namespace std;

int isSafe(vector<int> &v) {
    bool increasing = true;
    bool decreasing = true;
    for (int j = 0; j < v.size()-1; j++) {
        int diff = v[j + 1] - v[j];

        if (abs(diff) < 1 || abs(diff) > 3) {
            decreasing = false;
            increasing = false;
            break;
        }
        
        if (diff > 0) {
            decreasing = false;
        } else if (diff < 0) {
            increasing = false;
        } else {
            decreasing = false;
            increasing = false;
            break;
        }
    }

    return increasing || decreasing;
}

int canBeSafe(vector<int> &v) {
    if (v.size() < 3) {
        return false;
    }

    for (int i = 0; i < v.size(); i++) {
        vector<int> copy = v;
        copy.erase(copy.begin() + i);
        if (isSafe(copy)) {
            return true;
        }
    }

    return false;
}

int main() {
    ifstream inputFile("../../input.txt");

    vector<vector<int>> allVectors;

    string line;

    while (getline(inputFile, line)) { // Read file line by line
        istringstream iss(line);
        vector<int> currentVector;
        int number;

        while (iss >> number) { // Extract integers from the line
            currentVector.push_back(number);
        }
        allVectors.push_back(currentVector);
    }

    inputFile.close();

    int count = 0;

    for (int i = 0; i < allVectors.size(); i++) {
        bool safe = isSafe(allVectors[i]);
        bool BeSafe = canBeSafe(allVectors[i]);
        
        if (safe || BeSafe) {
            count++;
        }
    }

    cout << count << endl;
}