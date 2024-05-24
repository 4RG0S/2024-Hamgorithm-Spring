#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	priority_queue<int> pq;

	cin >> n;

	vector<int> result;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;

		if (a == 0) {
			if (pq.size() == 0) {
				result.push_back(-1);
			} else {
				result.push_back(pq.top());
				pq.pop();
			}
		} else {
			int a2;

			for (int j = 0; j < a; j++) {
				cin >> a2;
				pq.push(a2);
			}
		}
	}

	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << endl;
	}
	return 0;
}