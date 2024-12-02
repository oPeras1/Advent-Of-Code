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

        bool increasing = true;
        bool decreasing = true;
        for (int j = 0; j < allVectors[i].size()-1; j++) {
            int diff = allVectors[i][j + 1] - allVectors[i][j];

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

        if (increasing || decreasing) {
            count++;
        }
    }

    cout << count << endl;
}