#include <bits/stdc++.h>

using namespace std;

int main() {
	int N;
	cin >> N;

	int M = N * 2 - 1;

	for (int i = 0; i < M / 2; i++) {
		for (int j = 0; j < (M / 2) - i; j++) {
			cout << " ";
		}
		for (int j = 0; j < (i + 1) * 2 - 1; j++) {
			cout << "*";
		}
		cout << endl;
	}

	for (int i = 0; i < M; i++) {
		cout << "*";
	}
	cout << endl;

	for (int i = 0; i < M / 2; i++) {
		for (int j = 0; j < i + 1; j++) {
			cout << " ";
		}
		for (int j = 0; j < M - ((i + 1) * 2); j++) {
			cout << "*";
		}
		cout << endl;
	}

	return 0;
}