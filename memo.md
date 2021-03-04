# 競技プログラミングメモ
覚えておいた方が良いことをメモ。
## いもす法（累積和）

問題例は[Lamps](https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c)をみること。ソースは[いもすさんの記事](https://imoz.jp/algorithms/imos_method.html)を見るべし。

足すべき区間[l, r]のlに+1、r+1に-1して累積和をとるとOK!
提出は[これ](https://atcoder.jp/contests/tokiomarine2020/submissions/16541559)


## Rerooting(全方位木DP)
ある根を起点にDFSしたのち、BFSで各頂点ごとの値を求める。
BFSの際、splitの操作によっては累積和による管理が必要。（０で割る操作など）
```math
dp[v] = merge(dp[u], dp[v]);
```

## 154e(けたDP と数え上げ)
単純な数え上げだと
1001
3
でWAをはくけど、
[この提出例](https://atcoder.jp/contests/abc154/submissions/16570782)
みたいにIDX==Kで+1としてやれば数え上げでもok!

けたDPだと思考停止で
DP[i][j][v] := i桁まで決めているときの0でないものがj個あるときの数。

として書いたものが
この[提出例](https://atcoder.jp/contests/abc154/submissions/16572277)



