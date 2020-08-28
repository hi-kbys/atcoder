#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;
typedef pair<ll, ll> LP;
const ll mod = 998244353;
const int N = 200050;
const ll inf = 1e18;
vector<vector<int>> g(N);

ll dfs(int s){
    if (g[s].empty()) return 2;
    ll tmp = 1;
    for (int v: g[s]){
        tmp *= dfs(v);
        tmp%= mod;
    }
    tmp++;
    tmp %= mod;
    return tmp;
}

int main()
{
    int n;
    cin >> n;
    vector<P> p(n);
    rep(i,n) cin >> p[i].first >> p[i].second;
    sort(all(p));
    set<P> s;
    repd(i, n){
        int x = p[i].first;
        int d = p[i].second;
        while (s.size() and s.begin()->first < x+d){
            g[i].push_back(s.begin()->second);
            s.erase(s.begin());
        }
        s.emplace(x, i);
    }

    ll ans = 1;
    for (auto& u : s) {
        ans *= dfs(u.second);
        ans %= mod;
    }
    cout << ans << endl;
    
}