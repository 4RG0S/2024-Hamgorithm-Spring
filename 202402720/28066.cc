#include <bits/stdc++.h>

using namespace std;

int main() {
	int N, K;
	cin >> N >> K;

	queue<int> q;

	for (int i = 1; i <= N; i++) {
		q.push(i);
	}

	while (true) {

		if (q.size() < K) {
			if (q.size() == 1) {
				break;
			} else {
				int x = q.front();
				q.pop();
				q.push(x);

				int y = q.size() - 1;

				for (int i = 0; i < y; i++) {
					q.pop();
				}
				break;
			}
		} else {
			int x = q.front();
			q.pop();
			q.push(x);

			for (int i = 0; i < K - 1; i++) {
				q.pop();
			}
		}
	}

	cout << q.front() << endl;
	return 0;
}