#include <iostream>

#define ll long long

using namespace std;

void soe(int *primes, int n)
{
    // for all odd numbers
    for (int i = 1; i < n; i += 2) primes[i] = 1;

    primes[1] = 0; // 1 is neither prime nor composite

    for (int i = 3; i < n; i += 2)
    {
        // if the given odd number is still prime (after few markings / runs)
        if (primes[i])
        {
            // mark it's multiples as not prime starting from it's square
            for (int j = i * i; j < n; j += i)
            {
                // if not yet marked as not prime
                if (primes[j])
                {
                    primes[j] = 0;
                }
            }
        }
    }
}

int main(void)
{
    int a, b;
    const int n = 1000;
    cin >> a >> b;
    int primes[n] = {0};

    int cummulative_sum[n] = {0};
    soe(primes, n);

    // all the primes till n
    // for (int i = 1; i < 100; i++)
    // {
    //     if (primes[i])
    //     {
    //         cout << i << ", ";
    //     }
    // }

    for (int i = 0; i < n; i++)
    {
        cummulative_sum[i] = cummulative_sum[i - 1] + primes[i];
    }
    
    cout << cummulative_sum[b] - cummulative_sum[a - 1] << endl;
}