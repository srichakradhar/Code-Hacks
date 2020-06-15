#include <iostream>

using namespace std;

/*
while b > 0

b | a 
    a % b | b

*/

int gcd(int a, int b){
    if(b == 0) return a;
    return gcd(b, a % b);
}


int main() {

    int a, b;
    cin >> a >> b;
    cout << gcd(a, b);

}