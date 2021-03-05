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
    ll n, a, b;
    cin >> n >> a >> b;
    ll ans = n/(a+b)*a;
    ans += min(a, n%(a+b));
    cout << ans << endl;
}