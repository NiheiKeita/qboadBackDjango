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
https://meetup-jp.toast.com/931

#### Windows で API たたき方

```bash
curl.exe -XPOST -d 'email=nihei2@example.com&password=nihei&user_name=nihei&unique_user_id=eeeeee' 'http://localhost:8000/api/users/'
```

#### API の認証

ライブラリインストール

```bash
pip install "djangorestframework-api-key==2.\*"
```

DB 反映

```bash
python manage.py migrate
```

APIKEY 作成

```bash
python manage.py shell
Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from rest_framework_api_key.models import APIKey
>>> api_key, key = APIKey.objects.create_key(name="qlitre-api-key")
>>> key
'FFltOiuF.JfVmZk3FoDHUDinkBUT3DYfwLbq5xnuA'
>>> exit()
```
