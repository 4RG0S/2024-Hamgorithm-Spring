#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int m, n, h, ans, dist[102][102][102];
int dx[] = {0,0,1,-1,0,0};
int dy[] = {1,-1,0,0,0,0};
int dz[] = {0,0,0,0,1,-1};
queue<pair<pair<int,int>, int>> q;

void bfs(){
    while(!q.empty()){
        int xx = q.front().first.first;
        int yy = q.front().first.second;
        int zz = q.front().second;
        q.pop();
        for(int i=0;i<6;i++){
            int nx = xx+dx[i];
            int ny = yy+dy[i];
            int nz = zz+dz[i];
            
            if(nx>=0&&ny>=0&&nz>=0&&nx<n&&ny<m&&nz<h&&dist[nx][ny][nz] == 0){
                dist[nx][ny][nz] = dist[xx][yy][zz] + 1;
                q.push(make_pair(make_pair(nx,ny),nz));
            }
        }
    }
    
}
int main()
{
    cin >> m >> n >> h;
    for(int k=0;k<h;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin >> dist[i][j][k];
                if(dist[i][j][k] == 1){
                    q.push(make_pair(make_pair(i,j),k));
                }
            }
        }
    }
    
    bfs();
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for(int k=0;k<h;k++){
                if (dist[i][j][k] == 0) {
                    cout << -1;
                    return 0;
                }else {
                    ans = max(dist[i][j][k], ans);
                }
            }
            
        }
    }

    cout << ans-1;

    return 0;
}