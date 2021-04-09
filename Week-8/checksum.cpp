#include <iostream>
#include <string>
#include <vector>

using namespace std;

string add(string a, string b) {
    int i = a.length() - 1;
    int j = b.length() - 1;
    int carry = 0, sum;
    string result = "";

    while (i >= 0 || j >= 0) {
        sum = carry + (i >= 0 ? a[i] - '0' : 0) + (j >= 0 ? b[j] - '0' : 0);

        switch (sum) {
            case 0:
            case 1:
                carry = 0;
                break;
            case 2:
                carry = 1;
                sum = 0;
                break;
            case 3:
                carry = 1;
                sum = 1;
                break;
            default:
                break;
        }

        result = char(sum + '0') + result;
        i--;
        j--;
    }

    if (carry == 1) result = '1' + result;

    return result;
}

char flipBit(char c) { return (c == '0') ? '1' : '0'; }

string onesComplement(string a) {
    string comp = "";
    for (int i = 0; i < a.length(); i++) comp += flipBit(a[i]);

    return comp;
}

int main(int argc, char const *argv[]) {
    int n;
    cout << "Enter the no. of data: ";
    cin >> n;

    cout << "Enter " << n << " data: " << endl;

    // string data[100];
    vector<string> data;
    string temp;
    string sum = "";
    for (int i = 0; i < n; i++) {
        // cin >> data[i];
        cin >> temp;
        data.push_back(temp);
        sum = add(sum, data[i]);
    }

    cout << "Checksum: " << onesComplement(sum);
}
