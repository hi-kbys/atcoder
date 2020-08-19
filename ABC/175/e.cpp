#include<bits/stdc++.h>
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
typedef long long ll;
using namespace std;
const int MAX_R = 3010, MAX_C=3010;
ll item[MAX_R][MAX_C], dp[MAX_R][MAX_C][4];
int main()
{
    int r, c, k;
    cin >> r >> c >> k;
    rep(i, r+1)rep(j, c+1) {
        item[i][j] = 0;
        rep(v, 4) dp[i][j][v] = 0;
    }
    rep(i, k){
        int a, b;
        ll c;
        cin >> a >> b >> c;
        item[a][b] = c;
    }
    repran(i, 1, r+1) repran(j, 1, c+1){
        rep(v, 4){
            dp[i][j][v] = max(dp[i][j-1][v], dp[i-1][j][3]);
        }
        if (item[i][j] > 0){
            repd(v, 3){
                dp[i][j][v+1] = max(dp[i][j][v+1], dp[i][j][v]+item[i][j]);
            }
        }
    }
    cout << dp[r][c][3] << endl;
}