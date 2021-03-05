#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
const int MAX_N = 3010;
long double dp[MAX_N][MAX_N];
int main()
{
    int n;
    cin >> n;
    vector<long double> p(n);
    rep(i, n) cin>>p[i];
    dp[0][0] = 1;
    rep(i, n){
        dp[i+1][0] = dp[i][0]*(1-p[i]);
        rep(j, n){
            dp[i+1][j+1] = dp[i][j]*p[i] + dp[i][j+1]*(1-p[i]);
        }
    }
    long double ans = 0;
    repran(i, n/2+1, n+1) ans += dp[n][i];
    cout << fixed << setprecision(10) << ans << endl;

}