#include <stack>

class MinStack {
private:
  std::stack<int> stack;
  std::stack<int> minStack;

public:
  MinStack() : stack(), minStack() {}

  void push(int val) {
    stack.push(val);
    if (minStack.empty()) {
      minStack.push(val);
      return;
    }
    int prevMin = minStack.top();
    if (val < prevMin) {
      minStack.push(val);
    } else {
      minStack.push(prevMin);
    }
  }

  void pop() {
    stack.pop();
    minStack.pop();
  }

  int top() { return stack.top(); }

  int getMin() { return minStack.top(); }
};