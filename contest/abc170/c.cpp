#include<bits/stdc++.h>
#define rep(i, n) for (int i=0; i < n; i++)
typedef long long ll;
using namespace std;
using P = pair<int, int>;


int main()
{
    int x, n;
    cin >> x >> n;
    vector<int> p(102);
    rep(i, n) {
        int id ;
        cin >> id;
        p[id] = 1;
    }
    P ans(102,-1);
    rep(i, 102){
        if (p[i] == 1) continue;
        int sub = abs(i-x);
        ans = min(ans, P(sub,i));
    }   
    cout << ans.second << endl;
}