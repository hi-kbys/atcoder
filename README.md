# 概要
Atcoderのpythonによる実行環境をGithub Codespacesで展開するためのリポジトリ。

# 使い方
## 初期設定
`/workspaces/atcoder/`以下に`mkdir contests`でフォルダを作成する。
Github Codespaces以外の環境で作成している場合は`{workspacefolder}/contests`となるようにフォルダを作成し、
`atcodettools.toml`を以下のように書き換える。
```toml
[codestyle]
indent_type='space' # 'tab' or 'space'
indent_width=4
workspace_dir='{workspacefolder}/contests'
```

## 問題のダウンロード
以下のコードを実行すればOK
```
atcodertools gen {contestname} --config /path/to.atcodertools.toml
```

## 問題の提出
参考に書いてあるリンクの指示にしたがって提出すれば大丈夫（なはず）
# 参考
- [ac-library-python](https://github.com/not522/ac-library-python)
- [atcoder-tools](https://github.com/kyuridenamida/atcoder-tools)
