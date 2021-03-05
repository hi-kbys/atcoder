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
// auto mod int
// https://youtu.be/L8grWxBlIZ4?t=9858
// https://youtu.be/ERZuLAxZffQ?t=4807 : optimize
// https://youtu.be/8uowVvQ_-Mo?t=1329 : division
const int mod = 1000000007;
const int MX = 200005;
struct mint {
  ll x; // typedef long long ll;
  mint(ll x=0):x((x%mod+mod)%mod){}
  mint operator-() const { return mint(-x);}
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod-a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) { (x *= a.x) %= mod; return *this;}
  mint operator+(const mint a) const { return mint(*this) += a;}
  mint operator-(const mint a) const { return mint(*this) -= a;}
  mint operator*(const mint a) const { return mint(*this) *= a;}
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t>>1);
    a *= a;
    if (t&1) a *= *this;
    return a;
  }

  // for prime mod
  mint inv() const { return pow(mod-2);}
  mint& operator/=(const mint a) { return *this *= a.inv();}
  mint operator/(const mint a) const { return mint(*this) /= a;}
};
istream& operator>>(istream& is, mint& a) { return is >> a.x;}
ostream& operator<<(ostream& os, const mint& a) { return os << a.x;}

// combination mod prime
// https://www.youtube.com/watch?v=8uowVvQ_-Mo&feature=youtu.be&t=1619
struct combination {
    vector<mint> fact, ifact;
    combination(int n):fact(n+1),ifact(n+1) {
        assert(n < mod);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i-1]*i;
        ifact[n] = fact[n].inv();
        for (int i = n; i >= 1; --i) ifact[i-1] = ifact[i]*i;
    }
    mint operator()(int n, int k) {
        if (k < 0 || k > n) return 0;
        return fact[n]*ifact[k]*ifact[n-k];
    }
};

combination comb(MX);
// Rerooting
// https://youtu.be/zG1L4vYuGrg?t=7092
// TODO: vertex info, edge info
struct Rerooting {
    struct DP {
        mint x;
        int t;
        DP(mint x=1, int t=0):x(x), t(t) {};
        DP operator+(const DP& a) const {
            DP ret(*this);
            ret.x *= a.x;
            ret.x *= comb(ret.t+a.t, ret.t);
            ret.t += a.t;
            return ret;
        }
        DP addRoot() const {
            DP ret(*this);
            ret.t++;
            return ret;
        }
    };
    
    int n;
    vector<vector<int>> to;
    vector<vector<DP>> dp;
    vector<DP> ans;
    Rerooting(int n=0):n(n),to(n),dp(n),ans(n) {}
    void addEdge(int a, int b) {
        to[a].push_back(b);
        to[b].push_back(a);
    }
    void init() {
        dfs(0);
        bfs(0);
    }

    DP dfs(int v, int p=-1) {
        DP dpSum;
        dp[v] = vector<DP>(to[v].size());
        rep(i,to[v].size()) {
            int u = to[v][i];
            if (u == p) continue;
            dp[v][i] = dfs(u,v);
            dpSum = dpSum + dp[v][i];
        }
        return dpSum.addRoot();
    }
    //累積和を利用したbfs：
    void bfs(int v, const DP& dpP=DP(), int p=-1) {
        int deg = to[v].size();
        rep(i,deg) if (to[v][i] == p) dp[v][i] = dpP;

        vector<DP> dpSumL(deg+1);
        rep(i,deg) dpSumL[i+1] = dpSumL[i] + dp[v][i];
        vector<DP> dpSumR(deg+1);
        for (int i = deg-1; i >= 0; --i){
            dpSumR[i] = dpSumR[i+1] + dp[v][i];
        }
        ans[v] = dpSumL[deg].addRoot();

        rep(i,deg) {
            int u = to[v][i];
            if (u == p) continue;
            DP d = dpSumL[i] + dpSumR[i+1];
            bfs(u, d.addRoot(), v);
        }
    }
};

int main()
{
    int n;
    cin >> n;
    Rerooting r(n);
    rep(i, n-1){
        int a, b;
        cin >> a >>b;
        a--;b--;
        r.addEdge(a, b);
    }
    r.init();
    rep(i, n){
        cout << r.ans[i].x << endl;
    }
}

