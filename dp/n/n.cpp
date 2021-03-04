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

const ll inf = 1e18;
ll dp[405][405], s[405][405];
int a[405];
ll dfs(int l, int r){
    if (r-l == 1) {
        dp[l][r] = 0;
        return dp[l][r];
    }
    if (dp[l][r] != inf) return dp[l][r];
    repran(i, l+1, r){
        dp[l][r] = min(dp[l][r], dfs(l, i)+dfs(i, r)+s[l][i]+s[i][r]);
    }
    return dp[l][r];
}
int main()
{
    int n;
    cin >> n;
    rep(i, n) cin >> a[i];
    rep(i, n) {
        repran(j, i+1, n+1){
            dp[i][j] = inf;
            s[i][j] = s[i][j-1]+a[j-1];

        }
    }
    dfs(0, n);
    cout << dp[0][n] << endl;
}   