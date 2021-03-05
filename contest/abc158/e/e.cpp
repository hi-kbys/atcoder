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
    int n, p;
    cin >> n>> p;
    string s;
    cin >> s;
    vector<ll> div(p, 0);
    ll k = 0, base = 1;
    ll ans = 0;
    if (p == 2 or p==5){
        rep(i, n){
            if (stoi(s.substr(i, 1))%p==0){
                ans += i+1;
            }
        }
        cout << ans << endl;
        return 0;
    }
    repd(i, n){
        k += stoll(s.substr(i, 1))*base;
        k%=p;
        div[k]++;
        base *= 10;
        base %= p;
    }
    ans = div[0];
    rep(i, p){
        if (div[i]==0) continue;
        ans += (div[i]*(div[i]-1))/2;
    }
    cout << ans << endl;
    return 0;
}