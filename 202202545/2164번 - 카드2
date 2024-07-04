#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char**argv) {

	ios::sync_with_stdio(0);
	cin.tie(0);
		
	queue<int> Q;
	int N;
	
	cin >> N;
	
	for(int i=1;i<=N;i++){
		Q.push(i);
	}
	
	 
	while(Q.size()>1){
		Q.pop();
		Q.push(Q.front());
		Q.pop();	
	}

	cout << Q.front();
	
	return 0;
}