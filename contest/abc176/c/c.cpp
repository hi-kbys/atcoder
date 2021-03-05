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
    int n;
    ll ans = 0;
    ll m = 0;
    cin >> n;
    rep(i, n){
        ll a;
        cin >> a;
        m = max(m, a);
        ans += max((ll)0, m-a);
    }
    cout << ans << endl;

}