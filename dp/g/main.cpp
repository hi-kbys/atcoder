#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;
int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n);
    vector<int> deg(n, 0);
    vector<int> dist(n, 0);
    rep(i, m){
        int a, b;
        cin >> a >> b;
        a--;b--;
        g[a].push_back(b);
        deg[b]++;
    }
    queue<int> q;
    rep(i, n){
        if(deg[i] ==0 and g[i].size()!=0) q.push(i);
    }
    int ans = 0;
    while (not q.empty()){
        int v = q.front();q.pop();
        for (int nv : g[v]){
            deg[nv]--;
            if (deg[nv] == 0) {
                dist[nv] = dist[v]+1;
                q.push(nv);
            }
        }
    }
    rep(i, n) ans = max(ans, dist[i]);
    cout << ans << endl;
}