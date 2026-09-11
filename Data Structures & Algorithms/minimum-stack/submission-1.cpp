class MinStack {
    static constexpr int kCap = 30000;
    int vals[kCap];
    int mins[kCap];
    int n = 0;

public:
    void push(int val) {
        vals[n] = val;
        mins[n] = n == 0 ? val : std::min(mins[n-1], val);
        ++n;
    }
    
    void pop() {
        --n;
    }
    
    int top() {
        return vals[n-1];
    }
    
    int getMin() {
        return mins[n-1];
    }
};
