#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;
int main()
{
    string s, t;
    cin >> s >> t;
    int n = s.size();
    int m = t.size();
    int ans = 10000;
    rep(i, n-m+1){
        int tmp = 0;
        rep(j, m){
            if (s[i+j] != t[j]) tmp++;
        }
        ans = min(ans, tmp);
    }
    cout << ans << endl;
}