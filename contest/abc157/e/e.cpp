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
    cin >> n;
    string s;
    cin >> s;
    vector<set<int>> p(26);
    rep(i, n){
        int v = s[i]-'a';
        p[v].insert(i);
    }
    int q;
    cin >> q;
    rep(i, q){
        int t;
        cin >> t;
        if (t == 1){
            int j;char c;
            cin >> j >> c;
            j--;
            p[s[j]-'a'].erase(j);
            p[c-'a'].insert(j);
            s[j] = c;
        }else{
            int l, r;
            cin >> l >> r;
            l--;r--;
            int ans = 0;
            
            rep(j, 26){
                auto it = p[j].lower_bound(l);//std::set::lower_boundを使うべし
                if (*it <= r && it != p[j].end()) ans++;
            }
            cout << ans << endl;
        }
    }
    return 0;

}