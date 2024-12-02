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

    int n1, n2, n3, n4, n5;

    vector<int> arr1, arr2, arr3, arr4, arr5;

    // Read each line and parse the numbers
    while (inputFile >> n1 >> n2 >> n3 >> n4 >> n5) {
        arr1.push_back(n1);
        arr2.push_back(n2);
        arr3.push_back(n3);
        arr4.push_back(n4);
        arr5.push_back(n5);
    }

    int count = 0;

    int len = arr1.size();
    for (int i = 0; i < len; i++) {
        int most_difference = 0;
        most_difference = max(most_difference, abs(arr1[i] - arr2[i]));
        most_difference = max(most_difference, abs(arr2[i] - arr3[i]));
        most_difference = max(most_difference, abs(arr3[i] - arr4[i]));
        most_difference = max(most_difference, abs(arr4[i] - arr5[i]));

        if (most_difference <= 3) {
            count++;
        }
    }

    cout << count << endl;
}