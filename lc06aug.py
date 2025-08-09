#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int getLongestPrefix(string &s) {
        int n = (int)s.size();
        if (n <= 1) return -1;

        vector<int> lps(n, 0);
        int len = 0;
        for (int i = 1; i < n; ++i) {
            while (len > 0 && s[i] != s[len]) {
                len = lps[len - 1];
            }
            if (s[i] == s[len]) {
                ++len;
                lps[i] = len;
            } else {
                lps[i] = 0;
            }
        }

        int j = lps[n - 1];
        if (j == 0) return -1;

        int minBorder = INT_MAX;
        while (j > 0) {
            minBorder = min(minBorder, j);
            j = lps[j - 1];
        }

        if (minBorder == INT_MAX) return -1;

        int ans = n - minBorder;
        return (ans > 0 ? ans : -1);
    }
};
