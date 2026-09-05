class DynamicArray {
public:
    int* _data;
    int _capacity;
    int _curr;

    DynamicArray(int capacity) {
        _capacity = capacity;
        _curr = -1;
        _data = new int[capacity]();
    }

    int get(int i) {
        return _data[i];
    }

    void set(int i, int n) {
        _data[i] = n;
    }

    void pushback(int n) {
        if (!(_curr < _capacity-1)) {
            resize();
        }
        _data[++_curr] = n;
    }

    int popback() {
        return _data[_curr--];
    }

    void resize() {
        int* newData = new int[_capacity*2]();
        for (int i = 0; i <= _curr; i++) {
            newData[i] = _data[i];
        }
        delete[] _data;
        _data = newData;
        _capacity = _capacity*2;
    }

    int getSize() {
        return _curr + 1;
    }

    int getCapacity() {
        return _capacity;
    }
};
