#include<bits/stdc++.h>
#define rep(i, n) for (int i=0; i < n; i++)
typedef long long ll;
using namespace std;
using LP = pair<ll, int>;
const ll inf = 1e18;
const int di[] = {-1, 0, 1, 0};
const int dj[] = {0, 1, 0, -1};
int main()
{
    int h, w, k;
    cin >> h >> w >> k;
    int si, sj, gi, gj;
    cin >> si >> sj >> gi >> gj;
    si--; sj--; gi--; gj--;
    vector<string> g(h);
    rep(i, h) cin >> g[i];
    auto toId = [&](int i, int j, int v){
        return (i*w+j)*4+v;
    };
    auto modCeil = [&](ll x){
        return (x + k-1)/k*k;
    };
    //ここからダイクストラ
    vector<ll> dist(h*w*4, inf);
    priority_queue<LP, vector<LP>,greater<LP>> que;
    auto push = [&](int i, int j, int v, ll cost){
        int idx = toId(i, j, v);
        if (dist[idx] <= cost) return;
        dist[idx] = cost;
        que.emplace(cost, idx);
    };
    //初期化
    rep(v, 4) push(si, sj, v, 0);
    while(!que.empty()){
        ll cost = que.top().first;
        int id = que.top().second;
        int i = id/4/w;
        int j = id/4%w;
        int v = id%4;
        que.pop();
        if (cost > dist[id]) continue;
        //方向替え
        
        rep(nv, 4){
            int ni = i + di[nv];
            int nj = j + dj[nv];
            if (0 <= ni && ni < h && 0 <= nj && nj < w){
                if (g[ni][nj] == '.') {
                    if (nv != v){
                        //方向替え
                        push(ni, nj, nv, modCeil(cost)+1);
                    }else{
                        //直進
                        push(ni, nj, nv, cost+1);
                    }
                }
            }
           
            
        } 
            
        
    }
    ll ans = inf;
    rep(i, 4) ans = min(ans, dist[toId(gi, gj, i)]);
    if (ans == inf) {
        cout << -1 << endl;
    }else
    {
        cout << modCeil(ans)/k << endl;
    }
    return 0;
}

