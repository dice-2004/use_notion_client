# pythonを用いたnotionとのデータ連携の試作 
## (ぜひ参考に使ってください）

notionのデータデース内の情報をpythonから取得するモジュールを作りました。（ここではフレームワークとしてflaskを使っています）


使用するデータベースの構成はプロパティ

 - Title
 - Category（マルチセレクト）
 - public（チェックボックス）
 - Creation date（作成日時）
 - Last updated（最終更新日）

モジュールの本体はmy_package内のnotion.pyにあります。

notion-clientさえインストールしてもらえれば使えると思います。

時刻を日本に変えたいならばpython-dateutilもインストールしてください。
