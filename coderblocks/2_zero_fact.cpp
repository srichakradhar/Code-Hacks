#include <iostream>

using namespace std;

/*

factz = no. of occurences of 5, 5^2, 5^3... in n! = no. of trailing zeroes
because no. of even no.s >>> no. of 5's

*/

int main() {

    int n;
    cin >> n;
    int f = 5;
    int z = 0;
    while (n / f > 0) {
        z += n / f;
        f *= f;
    }

    cout << n << "! has " << z << " trailing zeroes!";

    return 0;
}