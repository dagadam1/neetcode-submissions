
#include <algorithm>
#include <vector>
class Solution {
  std::vector<int> minPrefix;
  std::vector<int> maxPostfix;

public:
  int maxProfit(std::vector<int> &prices) {
    for (int p : prices) {
      if (minPrefix.empty()) {
        minPrefix.push_back(p);
        continue;
      }
      minPrefix.push_back(std::min(p, minPrefix.back()));
    }

    for (int i = prices.size() - 1; i >= 0; --i) {
      if (maxPostfix.empty()) {
        maxPostfix.push_back(prices[i]);
        continue;
      }
      maxPostfix.push_back(std::max(prices[i], maxPostfix.back()));
    }

    int max = 0;
    for (int i = 0; i < maxPostfix.size(); ++i) {
      if (maxPostfix[maxPostfix.size() - 1 - i] - minPrefix[i] > max) {
        max = maxPostfix[maxPostfix.size() - 1 - i] - minPrefix[i];
      }
    }

    return max;
  }
};