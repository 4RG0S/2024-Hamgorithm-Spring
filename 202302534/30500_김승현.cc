#include <iostream>
#include <vector>
#include <set>
#include <stack>
using namespace std;

vector<vector<int>> graph, graph2;
vector<bool> visited;
stack<int> Stack;

void dfs(int v) {
    visited[v] = true;
    for (int i : graph[v]) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    Stack.push(v);
}

void dfs2(int v, set<int>& tmp) {
    visited[v] = true;
    tmp.insert(v);
    for (int i : graph2[v]) {
        if (!visited[i]) {
            dfs2(i, tmp);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int V, E;
    cin >> V >> E;
    
    graph.resize(V + 1);
    graph2.resize(V + 1);
    visited.assign(V + 1, false);
    
    for (int i = 0; i < E; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph2[b].push_back(a);
    }

    for (int k = 1; k <= V; ++k) {
        if (!visited[k]) {
            dfs(k);
        }
    }

    vector<set<int>> scc;
    visited.assign(V + 1, false);
    while (!Stack.empty()) {
        int k = Stack.top();
        Stack.pop();
        if (visited[k]) continue;
        set<int> tmp;
        dfs2(k, tmp);
        scc.push_back(tmp);
    }

    vector<set<int>> ans;
    for (auto& i : scc) {
        int cnt = 0;
        for (int j : i) {
            for (int k : graph2[j]) {
                if (i.find(k) == i.end()) {
                    ++cnt;
                }
            }
        }
        if (cnt == 0) {
            ans.push_back(i);
        }
    }

    cout << ans.size() << endl;

    return 0;
}
