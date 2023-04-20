```bash
# 1. 가상환경 생성
$ python -m venv .venv
# 2. 가상환경 활성화
$ source .venv/bin/activate
# 3. django 설치
$ pip install django
# 4. 의존성 파일 생성
$ pip freeze > requirements.txt
# 4-1. 의존성 파일로 부터 동일한 환경 생성
$ pip install -r requirements.txt
# 5. .gitignore 파일 생성
https://www.toptal.com/developers/gitignore/
# 6. git 저장소 생성
```

```bash
# 7. django 프로젝트 생성
$ django-admin startproject config .
# 8. django 서버 실행
$ python manage.py runserver

# 9. 앱 생성 & 등록 (settings.py)
$ python manage.py startapp articles
```
# URLs -> Views -> Templates

```bash
# blueprint 작성
$ python manage.py makemigrations
# DBdp blueprint 전달
$ python manage.py migrate

# admin 계정 생성
$ python manage.py createsuperuser

# admin에 모델 클래스 등록
```
```python
# articles/admin.py
from .models import Article
admin.site.register(Article)
```
```bash
# cf
$ python manage.py showmigrations
$ python manage.py sqlmigrate articles 0001
```

```bash
# export requirements
$ pip freeze > requirements.txt
# import requirements
$ pip install -r requirements.txt

# shell_plus
$ pip install ipython
$ pip install django-extensions

$ python manage.py shell_plus

# seeder & fakerer
$ pip install django-seed
```



```



