#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;
const int inf = 1e9;
const int di[4] = {-1, 0, 1, 0};
const int dj[4] = {0, 1, 0, -1};

int main()
{
    int h, w;
    cin >> h >> w;
    int si, sj;
    cin >> si >> sj;
    si--;sj--;
    int gi, gj;
    cin >> gi >> gj;
    gi--;gj--;
    vector<vector<char>> mp(h, vector<char>(w));
    rep(i, h) rep(j, w) cin>> mp[i][j];
    vector<vector<int>> dist(h, vector<int>(w, inf));
    deque<P> q;
    
    dist[si][sj] = 0;
    q.emplace_back(si, sj);
    while (not q.empty()){
        int i = q.front().first;
        int j = q.front().second;
        int x = dist[i][j];
        q.pop_front();
        rep(v, 4){
            int ni = i + di[v];
            int nj = j + dj[v];
            if (ni < 0 or ni >= h or nj < 0 or nj >= w) continue;
            if (mp[ni][nj]=='#') continue;
            if (dist[ni][nj] <= x) continue;
            dist[ni][nj] = x;
            q.emplace_front(ni, nj);
        }
        //一律emplace_backだと複数回書き直すこともあるのでTLEになるっぽい。
        repran(ei, -2, 3){
            repran(ej,-2, 3){
                int ni = i + ei;
                int nj = j + ej;
                // if (abs(ni-i)+abs(nj-j)<=1) continue;
                if (ni < 0 or ni >= h or nj < 0 or nj >= w) continue;
                if (mp[ni][nj]=='#') continue;
                if (dist[ni][nj] <= x+1) continue;
                dist[ni][nj] = x+1;
                q.emplace_back(ni, nj);
            }
        }
    }
       
    if (dist[gi][gj] == inf) cout << -1 << endl;
    else cout << dist[gi][gj] << endl;
}