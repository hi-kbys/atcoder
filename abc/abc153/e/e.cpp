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
const int inf = 10000;
int dp[10050];
int main()
{
    int h, n;
    cin >> h >> n;
    memset(dp, inf, sizeof(dp));
    dp[0] = 0;
    vi a(n), b(n);
    rep(i, n) cin >> a[i] >> b[i];
    rep(i, n){
        for(int j = 0; j<=h;j++){
            int nj = min(j+a[i], h);
            dp[nj] = min(dp[nj], dp[j]+b[i]);
        }
    }
    cout << dp[h] << endl;
}

