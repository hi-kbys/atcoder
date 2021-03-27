# 概要
これは[yamatia](https://github.com/yamatia/atcoder_docker_sample)さんのコードを自分用に改変したものである。
詳しくはこの方のREADMを読んでください。
# 改造点
* ac-libraryの導入
* [atcoder-cli](https://www.npmjs.com/package/atcoder-cli)の導入。使い方はリンクから見て下さい。
* online-judge-tools 及び　atcoder-cliへの自動ログイン
# 注意点
* 基本的にバージョン管理が面倒だったのでrequirements.txtでバージョン指定はしていません。悪しからず。
* devcontainer.jsonでac-libraryへのパスをCPLUS_INCLUDE_PATHで指定しています。ac-libraryが読み込まれないなぁという場合はここのパスを変えてdocker imageをリビルドすると良いかもです。
* .devcontainer/devcontainer.envというファイルにatcoderへのユーザ情報を記述するようにして下さい。