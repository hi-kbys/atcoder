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
    int h, w, m;
    cin >> h >> w >> m;
    set<P> c;
    map<int,int> mph, mpw;
    int hmax = 0, wmax = 0;
    rep(i, m){
        int a, b;
        cin >> a >> b;
        --a;--b;
        c.emplace(a,b);
        mph[a]++;mpw[b]++;
        hmax = max(hmax, mph[a]);
        wmax = max(wmax, mpw[b]);
    }
    vector<int> hidx, widx;
    for (auto p : mph){
        if (p.second==hmax) hidx.push_back(p.first);
    }
    for (auto p : mpw){
        if (p.second==wmax) widx.push_back(p.first);
    }
    int ans = hmax+wmax-1;
    for (int i: hidx){
        for (int j : widx){
            if (c.find({i,j})==c.end()) {
                ans++;
                cout << ans << endl;
                return 0;
            }
        }
    }
    cout << ans << endl;
    return 0;
}