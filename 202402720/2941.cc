// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>

using namespace std;

char table[8][4] = {
	{"c="}, {"c-"}, {"dz="}, {"d-"}, {"lj"}, {"nj"}, {"s="}, {"z="},
};

int main() {
	char input[200];
	char skip[200];
	memset(input, 0, sizeof(input));
	memset(skip, 0, sizeof(skip));
	cin >> input;

	int count = 0;
	for (int i = 0; i < sizeof(input) - 1; i++) {
		if (skip[i] == 0) {
			bool found = false;
			for (int j = 0; j < 8; j++) {
				if (input[i] == table[j][0] && input[i + 1] == table[j][1]) {
					if (j == 2 && i < sizeof(input) - 2) {
						if (input[i + 2] == table[j][2]) {
							found = true;
							skip[i] = 1;
							skip[i + 1] = 1;
							skip[i + 2] = 1;
							count++;
						}
					} else {
						found = true;
						skip[i] = 1;
						skip[i + 1] = 1;
						count++;
					}
				}
			}
			if (!found && input[i] != 0) {
				count++;
			}
		}
	}

	cout << count << endl;
	return 0;
}