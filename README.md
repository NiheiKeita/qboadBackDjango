# qboadBackDjango

起動コマンド
python manage.py runserver

# ローカル DB 接続

1.APP の Model にテーブル作成
2.python manage.py makemigrations apiapp を流して migration ファイルを作成
3.python manage.py migrate を流して DB に登録

##ローカル DB（splite3）に接続
1.PC のパスを通す
参照：https://chuna.tech/blog/web-application/Django/django-sqlite3-error-2/
2.python manage.py dbshell で接続
.table で一覧見れるから、作成したテーブルができているか確認
