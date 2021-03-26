#include <cstring>
#include <iostream>

using namespace std;

char evenParity(char msg[], int len) {
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (msg[i] == '1') count++;
    }

    return (count % 2 == 0) ? '0' : '1';
}

char oddParity(char msg[], int len) {
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (msg[i] == '1') count++;
    }

    return (count % 2 != 0) ? '0' : '1';
}

int main(int argc, char const *argv[]) {
    char msg[128];

    cout << "Enter the message: ";
    cin >> msg;
    int len = strlen(msg);

    int ch;
    cout << "1. Even parity \n2. Odd parity\nChoice: ";
    cin >> ch;

    char parityBit;
    switch (ch) {
        case 1:
            parityBit = evenParity(msg, len);
            break;
        case 2:
            parityBit = oddParity(msg, len);
            break;
        default:
            exit(0);
    }

    msg[len] = parityBit;
    msg[len + 1] = '\0';

    cout << endl << "Parity Bit: " << parityBit << endl;
    cout << "Message with Parity: " << msg << endl;

    return 0;
}
