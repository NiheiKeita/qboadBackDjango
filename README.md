# Django

起動コマンド

```bash
python manage.py runserver
```

# ローカル DB 接続

#### 1.APP の Model にテーブル作成

#### 2.migration ファイルを作成

```bash
python manage.py makemigrations
```

#### 3. DB に登録

```bash
python manage.py migrate
```

## ローカル DB（splite3）に接続

#### 1.PC のパスを通す

参照：https://chuna.tech/blog/web-application/Django/django-sqlite3-error-2/

#### 2.python manage.py dbshell で接続

.table で一覧見れるから、作成したテーブルができているか確認

### API

http://localhost:8000/api/choices.json
上のやつで choice の中身がとれるようになった

#### 論理削除ライブラリ

pip3 install django_boost

### API 参考

https://chigusa-web.com/blog/django-rest-framework/
