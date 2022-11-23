#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result = {1};
        for (int i = 1; i < rowIndex + 1; i++) {
            vector <int> level = {1};
            for (int j = 0; j < i / 2; j++) {
                level.push_back(*(result.begin() + j) + *(result.begin() + j + 1));
            }
            if (i % 2 == 0) {
                level.insert(level.end(), level.rbegin() + 1, level.rend());
            }
            else {
                level.insert(level.end(), level.rbegin(), level.rend());
            }
            result = level;
        }
        return result;
    }
};
