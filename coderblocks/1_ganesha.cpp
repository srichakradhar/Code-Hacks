#include <iostream>

using namespace std;

/*

*  ****
*  *
*  *
*******
   *  *
   *  *
****  * 

*/

void first_part(int n){
    cout << "*";
    for(int i = 0; i < n / 2 - 1; i++) cout << " ";
    for(int i = 0; i <= n / 2; i++) cout << "*";
    cout << "\n";
}

void top_middle(int n){
    int n_spaces = n / 2 - 1;
    for(int i = 0; i < n_spaces; i++)
    {
        cout << "*";
        for(int j = 0; j < n_spaces; j++) cout << " ";
        cout << "*\n";
    }
}

void bottom_middle(int n){
    int n_spaces = n / 2 - 1;
    for(int i = 0; i < n_spaces; i++)
    {
        for(int j = 0; j < n / 2; j++) cout << " ";
        cout << "*";
        for(int j = 0; j < n_spaces; j++) cout << " ";
        cout << "*\n";
    }
}

void last_part(int n){
    for(int i = 0; i <= n / 2; i++) cout << "*";
    for(int i = 0; i < n / 2 - 1; i++) cout << " ";
    cout << "*\n";
}

int main(){
    int n;
    cin >> n;
    int center_len = n % 2 ? n : n + 1;
    first_part(n);
    top_middle(n);
    for(int i = 0; i < center_len; i++) cout << "*";
    cout << "\n";
    bottom_middle(n);
    last_part(n);
}
