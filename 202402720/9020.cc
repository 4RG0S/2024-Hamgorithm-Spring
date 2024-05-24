#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int n;
		cin >> n;

		int arr[n];

		for (int j = 0; j < n; j++) {
			arr[j] = 1;
		}

		for (int j = 2; j < n; j++) {
			for (int k = j + j; k < n; k += j) {
				arr[k] = 0;
			}
		}

		int h = n / 2;

		for (int j = h; j >= 2; j--) {
			if (arr[j] == 1 && arr[n - j] == 1) {
				cout << j << " " << n - j << endl;
				break;
			}
		}
	}

	return 0;
}