#include <bits/stdc++.h>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	set<string> nSet;

	string s1;

	int sum = 0;

	for (int i = 0; i < N; i++) {
		cin >> s1;
		nSet.insert(s1);
	}

	for (int i = 0; i < M; i++) {
		cin >> s1;
		sum += nSet.count(s1);
	}

	cout << sum << endl;

	return 0;
}