#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result = {{1}};
        for (int i = 1; i < numRows; i++) {
            vector <int> level = {1};
            for (int j = 0; j < i / 2; j++) {
                level.push_back(*(result[i - 1].begin() + j) + *(result[i - 1].begin() + j + 1));
            }
            if (i % 2 == 0) {
                level.insert(level.end(), level.rbegin() + 1, level.rend());
            }
            else {
                level.insert(level.end(), level.rbegin(), level.rend());
            }
            result.push_back(level);
        }
        return result;
    }
};


int main() {
    Solution s;
    s.generate(5);
}