# Prototype for Data Integration between Python and Notion Using Flask


This is a prototype module that retrieves information from a Notion database using Python. The framework used here is Flask.


The structure of the database includes the following properties:

 - Title
 - Category (Multi-select)
 - Public (Checkbox)
 - Creation Date (Creation Time)
 - Last Updated (Last Update Time)

The core module is located in my_package/notion.py.

As long as you install notion-client, this module should be ready to use.










# (JP)pythonを用いたnotionとのデータ連携の試作 


notionのデータデース内の情報をpythonから取得するモジュール（ここではフレームワークとしてflaskを使用）


使用するデータベースの構成はプロパティ

 - Title
 - Category（マルチセレクト）
 - public（チェックボックス）
 - Creation date（作成日時）
 - Last updated（最終更新日）

モジュールの本体はmy_package内のnotion.py

notion-clientさえインストールしてもらえれば使えると思います

