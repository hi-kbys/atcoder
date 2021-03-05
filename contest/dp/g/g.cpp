#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
#define v(T) vector<T>
#define vv(T) vector<v(T)>
typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
template<class T>bool chmax(T &a, const T &b){
    if (a < b) {a = b; return true;}
    return false;
}
template<class T>bool chmin(T &a, const T &b){
    if (a > b) {a = b; return true;}
    return false;
}

int n, m;
vvi g(100005);
int memo[100005];
int dp(int s){
    if (g[s].size()==0) {return memo[s] = 0;}
    if (memo[s] > 0) return memo[s];
    int ret = 0;
    for (int v : g[s]){
        chmax(ret, dp(v)+1);
    }
    return memo[s] = ret;
}

int main()
{
    cin >> n >> m;
    rep(i, m){
        int a, b;
        cin >> a >> b;
        a--;b--;
        g[a].push_back(b);
    }
    int ans = 0;
    rep(i, n) chmax(ans, dp(i));
    cout << ans << endl;
}