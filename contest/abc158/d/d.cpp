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
    string s;
    cin >> s;
    int q;
    cin >> q;
    int cnt = 0;
    rep(i, q){
        int t;
        cin >> t;
        if (t == 1){
            cnt += 1;
            cnt %=2;
        }else{
            int f;
            char c;
            cin >> f >> c;
            if ((cnt + f)%2 == 0){
                s += c;
            }else s = c + s;
        }

    }
    if (cnt%2 == 1) reverse(all(s));
    cout << s << endl;
}