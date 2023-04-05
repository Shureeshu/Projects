# Django 10 - Django Authentication 1

Django Authentication 1
=======================

실습 목표
-----

*   Django Authentication 기능을 활용한 로그인 기능을 구현할 수 있다.
*   쿠키와 세션을 활용한 사용자 인증 과정을 설명할 수 있다.
*   쿠키와 세션을 활용한 사용자 인증 과정을 그림으로 그릴 수 있다.

제출 안내
-----

프로젝트 및 앱 폴더를 압축하여 실라버스 과제 제출란에 제출

> 가상환경 폴더(venv)는 제출하지 않습니다.

* * *

개발 명세서
------

### Environment

*   django 버전 : 3.2.18
*   Database : SQLite

### 🌟Custom User Model 대체

> [참고 문서 - Substituting a custom User model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)

1.  AbstractUser 모델을 상속 받는 커스텀 User 모델 작성(models.py)
2.  참조 하는 사용자 정의 모델 설정(settings.py)
3.  커스텀 User 모델 관리자 페이지 등록(admin.py)

### App & Model

*   앱 이름 : accounts
*   모델 이름 : User
*   `AbstractUser` 클래스 상속

### Superuser(관리자 계정) 생성

> 로그인 테스트용 계정 생성

1.  관리자 계정(superuser) 생성
2.  생성한 관리자 계정으로 로그인 테스트

* * *

### 회원 정보

*   `GET` accounts/
    *   비로그인 상태
        *   AnonymousUser 출력
        *   로그인 페이지 이동 버튼
    *   로그인 상태
        *   로그인 사용자의 username 출력
        *   로그아웃 버튼

* * *

### 로그인

> built-in form `AuthenticationForm` 활용

*   `POST` accounts/login/
    *   AuthenticationForm 유효성 검사 통과 시 로그인
    *   redirect `GET` accounts/
*   `GET` accounts/login/
    *   AuthenticationForm 전달한 로그인 템플릿 렌더링
    *   로그인 사용자의 경우 redirect `GET` accounts/
    *   Django Form 변수를 활용하여 로그인 폼 출력

* * *

### 로그아웃

*   `POST` accounts/logout/
    *   사용자 로그아웃
    *   redirect `GET` accounts/

* * *

### 예시 이미지

*   로그인 & 로그아웃 ![](https://user-images.githubusercontent.com/109528419/229655036-3c1eab0e-98b7-46ab-876a-c0d737f48b34.gif)

* * *

### Cookie & Session 정리 및 내용 공유

> 아래 주제에 대해 내용 정리 후 코드 리뷰 시간에 내용 공유

1.  쿠키(Cookie) 특징
2.  세션(Session) 특징
3.  쿠키(Cookie)와 세션(Session) 차이
4.  쿠키 & 세션 활용 로그인 과정

* * *

### Django ModelForm 복습

*   \[참고\] django form 활용 이유
    1.  유효성 검사
    2.  생성 & 수정 로직 간소화
    3.  HTML Form 렌더링 간소화

1.  \[forms\] django form 작성 방법
2.  \[view\] django form 활용 방법
3.  \[template\] django form 렌더링 방법