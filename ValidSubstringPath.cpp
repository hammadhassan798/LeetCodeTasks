#include <vector>

using namespace std;

class Solution {
    int m, n;
    int memo[100][100][101];

    bool dfs(vector<vector<char>>& grid, int r, int c, int bal) {
        // Balance cannot drop below 0
        if (bal < 0) return false;

        // Reached bottom-right cell
        if (r == m - 1 && c == n - 1) {
            return bal == 0;
        }

        // If state already calculated, return memoized result
        if (memo[r][c][bal] != -1) {
            return memo[r][c][bal];
        }

        bool result = false;

        // Move Down
        if (r + 1 < m) {
            int next_bal = bal + (grid[r + 1][c] == '(' ? 1 : -1);
            result = result || dfs(grid, r + 1, c, next_bal);
        }

        // Move Right
        if (c + 1 < n) {
            int next_bal = bal + (grid[r][c + 1] == '(' ? 1 : -1);
            result = result || dfs(grid, r, c + 1, next_bal);
        }

        return memo[r][c][bal] = result;
    }

public:
    bool hasValidPath(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();

        // Path length must be even
        if ((m + n - 1) % 2 != 0) return false;

        // Must start with '(' and end with ')'
        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;

        // Initialize memoization array with -1
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k <= (m + n) / 2; ++k) {
                    memo[i][j][k] = -1;
                }
            }
        }

        // Start DFS from (0, 0) with initial balance 1 for grid[0][0] == '('
        return dfs(grid, 0, 0, 1);
    }
};