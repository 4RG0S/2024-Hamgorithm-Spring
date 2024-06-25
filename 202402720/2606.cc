#include <bits/stdc++.h>

using namespace std;

vector<int> visited;

void dfs(vector<vector<int>> &v, int here) {
	visited[here] = 1;

	for (int next : v[here]) {
		if (visited[next] == 0) {
			dfs(v, next);
		}
	}
}

int main() {
	int n;
	cin >> n;
	int m;
	cin >> m;

	vector<vector<int>> v(n + 1);
	visited.resize(n + 1, 0);

	while (m > 0) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
		m--;
	}

	dfs(v, 1);

	int cnt = 0;

	for (int i = 1; i <= n; i++) {
		if (visited[i] == 1) {
			cnt += 1;
		}
	}

	cout << cnt - 1 << "\n";

	return 0;
}