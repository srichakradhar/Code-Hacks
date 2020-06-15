#include <iostream>

using namespace std;

/*

counting no. of set bits in a number

13 = 1101
    8,4,1

*/

int set_bit_count_slow(int n) {
    int n_bits = 0;
    while (n > 0) {
        n_bits += n & 1;
        n = n >> 1;
    }
    return n_bits;
}

int set_bit_count_fast(int n) {
    int n_bits = 0;
    while (n > 0) {
        n_bits += 1;
        n = n & (n -1);
    }
    return n_bits;
}


int main() {

    int n;
    cin >> n;
    cout << __builtin_popcount(n) << endl;
    cout << set_bit_count_slow(n) << endl;
    cout << set_bit_count_fast(n) << endl;
}