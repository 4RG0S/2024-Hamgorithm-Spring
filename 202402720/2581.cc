#include <bits/stdc++.h>

using namespace std;

bool isPrime(int num) {
	if (num == 1) {
		return false;
	}

	double r = sqrt(num);
	int d = (int)r;

	bool prime = true;

	for (int i = 2; i <= d; i++) {
		if (num % i == 0) {
			prime = false;
		}
	}

	return prime;
}

int main() {
	int M, N;
	int sum = 0;
	int min = 10000;

	cin >> M;
	cin >> N;

	for (int i = M; i <= N; i++) {
		if (isPrime(i)) {
			if (min > i) {
				min = i;
			}
			sum += i;
		}
	}

	if (sum == 0) {
		cout << "-1" << endl;
	} else {
		cout << sum << endl;
		cout << min << endl;
	}

	return 0;
}