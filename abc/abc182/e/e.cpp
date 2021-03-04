#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
#define v(T) vector<T>
#define vv(T) vector<v(T)>
typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
template<class T>bool chmax(T &a, const T &b){
    if (a < b) {a = b; return true;}
    return false;
}
template<class T>bool chmin(T &a, const T &b){
    if (a > b) {a = b; return true;}
    return false;
}

int main()
{
    int h, w, n, m;
    cin >> h >> w >> n >> m;
    vvi G(h, vi(w, 0));
    rep(i, n){
        int x, y;
        cin >> x >> y;
        x--;y--;
        G[x][y] = 1;
    } 
    rep(i, m){
        int x, y;
        cin >> x >> y;
        x--;y--;
        G[x][y] = -1;
    }
    rep(i, h) rep(j, w){
        if (i != 0){
            if (G[i-1][j] == 1 && G[i][j] != -1) G[i][j] = 1;  
        } 
        if (j!= 0){
            if (G[i][j-1] == 1 && G[i][j] != -1) G[i][j] = 1;  
        }
    }
    repd(i, h) repd(j, w){
        if (i != h-1){
            if (G[i+1][j] == 1 && G[i][j] != -1) G[i][j] = 1;  
        }
        if (j != w-1){
            if (G[i][j+1] == 1 && G[i][j] != -1) G[i][j] = 1;  
        }
    }
    int ans = 0;
    rep(i, h)rep(j, w){
        if (G[i][j] == 1) ans += G[i][j];
    }
    cout << ans << endl;
}

