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
    int a, b;
    cin >> a >> b;
    rep(i, 1001){
        int aa = i*0.08;
        int bb = i*0.1;
        if (aa == a and bb == b){
            cout << i << endl;
            return 0;
        }
    }
    cout << -1 << endl;
}