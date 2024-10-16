# 概要
python3.11でのatcoder実行環境

# 使い方

## 環境構築
### Dev Containerを使用する場合
1. vscodeでReopen in Containerを選択
### ローカルで使用する場合
1. プロジェクトルートで `uv sync` を実行する

## 初期設定
`atcodettools.toml`を以下のように書き換える。
```toml
[codestyle]
indent_type='space' # 'tab' or 'space'
indent_width=4
workspace_dir='{workspacefolder}/contests'
```

## 問題のダウンロード
以下のコマンドを実行する
```
atcodertools gen {contestname} --config /path/to/atcodertools.toml
```

## 問題の提出
参考に書いてあるリンクの指示にしたがって提出すれば大丈夫（なはず）
# 参考
- [ac-library-python](https://github.com/not522/ac-library-python)
- [atcoder-tools](https://github.com/kyuridenamida/atcoder-tools)
