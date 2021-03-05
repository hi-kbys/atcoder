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
    string n;
    cin >> n;
    int m = n.size();
    int tmp = 0;
    rep(i, m) tmp += (int) n[i]-'0', tmp %= 9;
    if (tmp==0) cout << "Yes" << endl;
    else cout << "No" << endl;
}