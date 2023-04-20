# Django Authentication 2

# 개발 명세서

## Environment
- django 버전 : 3.2.18
- Database : SQLite

## 🌟Custom User Model 대체
0. AbstractUser 모델을 상속 받는 커스텀 User 모델 작성(models.py)
0. 참조 하는 사용자 정의 모델 설정(settings.py)
0. 커스텀 User 모델 관리자 페이지 등록(admin.py)

## App & Model
아래 정보를 기반으로 앱 생성 및 모델 작성
- 앱 이름 : accounts
- 모델 이름 : User
- AbstractUser 클래스 상속

## Django Form

회원가입 폼 CustomUserCreationForm
- 폼 이름 : CustomUserCreationForm
- 클래스 상속 : UserCreationForm
- 입력 필드
    - username
    - email
    - first_name
    - last_name
    - password1
    - password2

회원 정보 수정 폼 CustomUserChangeForm
- 폼 이름 : CustomUserChangeForm
- 클래스 상속 : UserChangeForm
- 수정 필드
    - email
    - first_name
    - last_name

## 회원 정보

GET accounts/
- 비로그인 상태
    - AnonymousUser 출력
    - 로그인 버튼
    - 회원가입 버튼
- 로그인 상태
    - 로그인 사용자 정보 출력
    - 로그아웃 버튼
    - 회원 정보 수정 버튼
    - 회원 탈퇴 버튼

## 로그인

POST accounts/login/
- AuthenticationForm 유효성 검사 후 로그인
- redirect GET accounts/

GET accounts/login/
- AuthenticationForm 전달한 로그인 템플릿 렌더링
- 로그인 사용자의 경우 redirect GET accounts/
- Django Form 변수를 활용하여 로그인 폼 출력

## 회원가입

POST accounts/signup/
- CustomUserCreationForm 유효성 검사 후 회원가입
- redirect GET accounts/

GET accounts/signup/
- 로그인 사용자의 경우 redirect GET accounts/
- Django Form을 활용하여 회원가입 폼 출력


## 회원 탈퇴

[login_required] POST accounts/delete/
- 계정 삭제 후 로그아웃


## 회원 정보 수정

[login_required] POST accounts/update/
- CustomUserChangeForm 유효성 검사 후 회원 정보 수정
- redirect GET accounts/

[login_required] GET accounts/update/
- Django Form을 활용하여 회원 정보 수정 폼 출력


## 비밀번호 수정

[login_required] POST accounts/password/
- PasswordChangeForm 유효성 검사 후 비밀번호 수정

[login_required] GET accounts/password/
- Django Form을 활용하여 비밀번호 수정 폼 출력