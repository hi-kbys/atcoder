#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;
const int mod = 1e9+7;

struct mint {
  ll x; // typedef long long ll;
  mint(ll x=0):x((x%mod+mod)%mod){}
  mint operator-() const { return mint(-x);}
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod-a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) { (x *= a.x) %= mod; return *this;}
  mint operator+(const mint a) const { return mint(*this) += a;}
  mint operator-(const mint a) const { return mint(*this) -= a;}
  mint operator*(const mint a) const { return mint(*this) *= a;}
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t>>1);
    a *= a;
    if (t&1) a *= *this;
    return a;
  }

  // for prime mod
  mint inv() const { return pow(mod-2);}
  mint& operator/=(const mint a) { return *this *= a.inv();}
  mint operator/(const mint a) const { return mint(*this) /= a;}
};
istream& operator>>(istream& is, mint& a) { return is >> a.x;}
ostream& operator<<(ostream& os, const mint& a) { return os << a.x;}

struct Combination {
    vector<mint> fact, ifact;
    Combination(int n) : fact(n+1), ifact(n+1) {
        fact[0] = 1;
        repran(i, 1, n+1){
            fact[i] = fact[i-1]*i;
        }
        ifact[n] = fact[n].inv();
        repd(i, n){
            ifact[i] = ifact[i+1]*(i+1);
        }
    };
    mint combination(int n, int i){
        return fact[n]*ifact[i]*ifact[n-i];
    }
    mint permutation(int n, int i){
        return fact[n]*ifact[i];
    }


};

int main()
{
    int n, k;
    cin >> n >> k;
    Combination c(n);
    k = min(k, n-1);
    mint ans;
    rep(i, k+1){
        ans += c.combination(n, i)*c.combination(n-1, i);
    }
    cout << ans.x << endl;

}