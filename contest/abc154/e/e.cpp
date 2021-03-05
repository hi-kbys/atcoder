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

int dp[1000][4][2];
int main()
{
    string s;
    cin >> s;
    int n = s.size();
    int k; cin >> k;
    dp[0][0][0] = 1;
    rep(i, n){
        int num = s[i]-'0';
        rep(j, k+1) rep(v, 2){
            rep(d, 10){
                int nj = j, nk = k;
                if (d!= 0) nj++;
                if (nj > k) continue;
                if (k==0) {
                    if (d > num) continue;
                    else if (d < num) nk++;
                }
                dp[i+1][nj][nk] += dp[i][j][k];
            }

        }
    }
    cout << dp[n][k][0]+dp[n][k][1] << endl;
}

