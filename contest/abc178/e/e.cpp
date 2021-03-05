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
const int inf = 1e9+5;
int main()
{
    int n;
    cin >> n;
    int a=-inf, b= inf, c= -inf, d = inf;
    rep(i, n) {
        int x, y;
        cin >> x >> y;
        a = max(a, x+y);
        b = min(b, x+y);
        c = max(c, x-y);
        d = min(d, x-y);
    }
    int ans = max(a-b, c-d);
    cout << ans << endl;

}

