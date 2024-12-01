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
    ifstream inputFile("input.txt"); // Open the file

    int n1, n2;

    vector<int> arr1, arr2;

    // Read each line and parse the numbers
    while (inputFile >> n1 >> n2) {
        arr1.push_back(n1);
        arr2.push_back(n2);
    }

    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());

    int diff = 0;

    int len = arr1.size();
    for (int i = 0; i < len; i++) {
        diff += abs(arr1[i] - arr2[i]);
    }

    cout << diff << endl;
}