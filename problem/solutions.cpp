#include <iostream>
using namespace std;
int findLastDigitOfFibonacci(int n) {
    if (n <= 1) {
        return n;
    }

    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = (a + b) % 10;
        a = b;
        b = temp;
    }

    return b;
}

int main() {
    cout<<"Enter the indexx number : ";
    int n;
    cin >> n;
    int result = findLastDigitOfFibonacci(n);
    cout << result << std::endl;
    return 0;
}
// F200 = 280 571 172 992 510 140 037 611 932 413 038 677 189 525