/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
# include <vector>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector <vector <int>> res;
        if (root == nullptr) {
            return res;
        }
        // res.push_back(vector<int> {root -> val});
        zigzagLevelOrder_helper(root, res, 1);
        for (int i=0; i < res.size(); i++) {
            if (i % 2 != 0) {
                reverse(res[i].begin(), res[i].end());
            }
        }
        return res;
    }
    
    void zigzagLevelOrder_helper(TreeNode* node, vector<vector<int>> &res, int level) {
        if (node == nullptr) {
            return;
        }

        if (res.size() < level) {
            res.push_back(vector<int> {});
        }

        res[level - 1].push_back(node -> val);
        zigzagLevelOrder_helper(node -> left, res, level + 1);
        zigzagLevelOrder_helper(node -> right, res, level + 1);
    }
};


int main() {
    Solution s;
    TreeNode* t = new TreeNode(1, new TreeNode(2, new TreeNode(4), nullptr), new TreeNode(3, nullptr, new TreeNode(5)));
    s.zigzagLevelOrder(t);

}