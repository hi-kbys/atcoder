# 概要
これは[yamatia](https://github.com/yamatia/atcoder_docker_sample)さんのコードを自分用に改変したものである。
詳しくはこの方のREADMを読んでください。

# 前提となる環境
1. dockerがインストールされていること。
1. vscode、及び拡張機能Remote Containerがインストールされていること。
# 改造点
* ac-libraryの導入
* [atcoder-cli](https://www.npmjs.com/package/atcoder-cli)の導入.自動でコンテストのファイルを作成してくれます。便利。
* online-judge-tools 及び　atcoder-cliへの自動ログイン
# 注意点
* 一応自分の環境でうまくいっているバージョンをrequirements.txtに記述しています。依存関係でエラーがでた場合は適宜変えてください。
* devcontainer.jsonでac-libraryへのパスをCPLUS_INCLUDE_PATHで指定しています。ac-libraryが読み込まれないなぁという場合はここのパスを変えてdocker imageをリビルドすると良いかもです。
* .devcontainer/devcontainer.envというファイルにatcoderへのログイン情報を記述するようにして下さい。一応gitignoreで排除してますが、絶対githubにはあげないようにしてください。もっと安全でいい感じのログイン自動化があれば教えて欲しいです。