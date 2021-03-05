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
    int n, k;
    cin >> n >> k;
    vector<int> x, y, c;
    rep(i, n) cin >> x[i] >> y[i] >> c[i];
    double X, Y;
    rep(i, n){
        X+= c[i]*x[i];
        Y += c[i]*y[i];
    }
    X /= n, Y/= n;
    
}