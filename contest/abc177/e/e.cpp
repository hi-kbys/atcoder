#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i=0; i < n; i++)
#define repd(i, n) for (int i = n-1; i > -1; i--)
#define repran(i, a,b) for (int i = a; i<b;i++)
#define all(x) (x).begin(), (x).end()
typedef long long ll;
typedef pair<int, int> P;

// Sieve of Eratosthenes
// https://youtu.be/UTVg7wzMWQc?t=2774
struct Sieve {
  int n;
  vector<int> f, primes;
  Sieve(int n=1):n(n), f(n+1) {
    f[0] = f[1] = -1;
    for (ll i = 2; i <= n; ++i) {
      if (f[i]) continue;
      primes.push_back(i);
      f[i] = i;
      for (ll j = i*i; j <= n; j += i) {
        if (!f[j]) f[j] = i;
      }
    }
  }
  bool isPrime(int x) { return f[x] == x;}
  vector<int> factorList(int x) {
    vector<int> res;
    while (x != 1) {
      res.push_back(f[x]);
      x /= f[x];
    }
    return res;
  }
  vector<P> factor(int x) {
    vector<int> fl = factorList(x);
    if (fl.size() == 0) return {};
    vector<P> res(1, P(fl[0], 0));
    for (int p : fl) {
      if (res.back().first == p) {
        res.back().second++;
      } else {
        res.emplace_back(p, 1);
      }
    }
    return res;
  }
  vector<pair<ll,int>> factor(ll x) {
    vector<pair<ll,int>> res;
    for (int p : primes) {
      int y = 0;
      while (x%p == 0) x /= p, ++y;
      if (y != 0) res.emplace_back(p,y);
    }
    if (x != 1) res.emplace_back(x,1);
    return res;
  }
};


int main()
{
    int n;
    cin >> n;
    vector<int> a(n); // setだとgcdを正しく評価できていない。
    int gcd = 0;
    int m = 0;
    rep(i, n){
        cin >> a[i];
        gcd = __gcd(gcd, a[i]);
        m = max(m, a[i]);
    }
    Sieve s(m);
    vector<int> cnt(m+1);
    for (int x: a){
        auto p = s.factor(x);
        for (auto v: p){
            cnt[v.first]++;
        }
    }
    int mcnt = 0;
    repran(i, 2, m+1){
        mcnt = max(mcnt, cnt[i]);
    }
    if (mcnt == n){
        cout << "not coprime" << endl;
    }
    else if (mcnt > 1){
        cout << "setwise coprime" << endl;
    }
    else cout << "pairwise coprime" << endl;

}
