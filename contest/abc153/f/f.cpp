#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
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

typedef pair<ll, ll> LP;
const ll inf = 1e18;
int main()
{
    int n;
    ll d, a;
    cin >> n >> d >> a;
    v(LP) p(n);
    rep(i, n) cin >> p[i].fi >> p[i].se;
    sort(all(p));
    ll ans = 0;
    ll tot = 0;
    queue<LP> q;
    rep(i, n){
        int x = p[i].fi;
        int h = p[i].se;
        while (q.size() && q.front().fi < x){
            tot -= q.front().se;
            q.pop();
        }
        h -= tot;
        if (h > 0){
            int num = (h+a-1)/a;
            ans += num;
            tot += a*num;
            q.emplace(x+2*d, a*num);
        }
    }
    cout << ans << endl;
}

