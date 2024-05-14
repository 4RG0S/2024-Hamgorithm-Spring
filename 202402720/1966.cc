#include <bits/stdc++.h>

using namespace std;

int main() {
	int caseNum;

	cin >> caseNum;

	vector<int> result;

	for (int i = 0; i < caseNum; i++) {
		int N, M;
		queue<int> q;
		vector<int> v;

		cin >> N >> M;

		for (int j = 0; j < N; j++) {
			int x;
			cin >> x;
			q.push(x);
			v.push_back(x);
		}

		sort(v.begin(), v.end());

		int currentIndex = M;
		int count = 1;

		while (true) {
			int x = q.front();
			if (x == v.back()) {
				if (currentIndex == 0) {
					break;
				} else {
					count += 1;
					q.pop();
					v.pop_back();
					currentIndex -= 1;
				}
			} else {
				q.pop();
				q.push(x);

				if (currentIndex == 0) {
					currentIndex = q.size() - 1;
				} else {
					currentIndex -= 1;
				}
			}
		}

		result.push_back(count);
	}

	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << endl;
	}

	return 0;
}