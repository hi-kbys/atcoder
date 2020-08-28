#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
const int MAX = 100050;
const ll mod = 1e9+7;
ll dp[MAX];
int main()
{
    int n, k;
    cin >> n >> k;
    int a[n];
    rep(i, n) cin >> a[i];
    dp[0] = 1;
    repran(i, n){
        vector<ll> tmp = {0};
        
        repran(j, 1, k+1){

        }
    }
}