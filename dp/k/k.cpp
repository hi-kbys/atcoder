#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;
const int inf = 100000000;
int main()
{
    int n, k;
    cin >> n>> k;
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    vector<int> dp(k+1, 0);
    dp[0] = 0;
    repran(i, 1, k+1){
        rep(j, n){
            if (i>=a[j] and dp[i-a[j]]==0) dp[i] = 1;
        }
    }
    if (dp[k]) cout << "First" << endl;
    else cout << "Second" << endl;
}