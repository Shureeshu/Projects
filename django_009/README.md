# Django 16 - Model Relationships (N:M)

## 개발 명세서

Subject
- 사용자간 팔로우 기능이 구현된 웹 서비스 개발

Environment
- django 버전 : 3.2.18
- Database : SQLite

skeleton code
- 아래 기능이 구현된 스켈레톤 코드를 다운로드 받아서 실습 진행 다운로드
- 사용자 프로필 조회
- 회원가입 / 로그인 / 로그아웃
- 게시글 생성, 조회
- 댓글 생성, 조회


## App & Model

User
- 앱 이름 : accounts
- 모델 이름 : User
- AbstractUser 클래스 상속

Article
- 앱 이름 : articles
- 모델 이름 : Article
- 필수 필드
    - 필드 이름	역할	django 필드	속성
    - user	작성자		
    - like_users	좋아요를 누른 사용자	ManyToManyField	settings.AUTH_USER_MODEL, related_name='like_articles'
    - title	제목		
    - content	내용	

Comment
- 앱 이름 : articles
- 모델 이름 : Comment
- 필수 필드
    - 필드 이름	역할	django 필드	속성
    - user	댓글 작성자		
    - like_users	좋아요를 누른 사용자	ManyToManyField	settings.AUTH_USER_MODEL, related_name='like_comments'
    - article	댓글 작성 게시글		
    - content	내용		

## 요구사항

사용자 프로필 조회
- GET accounts/profile/<str:username>/
- [스켈레톤 코드] index 페이지에서 자신의 아이디를 클릭하면 사용자 프로필을 조회할 수 있습니다.
- 게시글 작성자의 아이디를 클릭하면 사용자 프로필을 조회할 수 있습니다.
- 댓글 작성자의 아이디를 클릭하면 사용자 프로필을 조회할 수 있습니다.

사용자 팔로우
- POST accounts/<int:user_pk>/follow/
- 비로그인 사용자는 팔로우 버튼이 비활성화(disabled) 상태입니다.
- 로그인 한 사용자는 다른 사용자 프로필 페이지에서 해당 사용자를 팔로우 할 수 있습니다.
- 자기 자신을 팔로우 할 수 없습니다.

사용자 팔로우 목록 조회
- 프로필 페이지에 해당 사용자의 팔로워 / 팔로잉 목록을 출력합니다.
- 프로필 페이지에 해당 사용자의 팔로워 / 팔로잉 수를 출력합니다.

Try. 페이지네이션
처음, 마지막 이동 버튼 - 위 기본 코드에서 처음, 마지막 페이지로 이동하는 버튼 구현
구현 힌트 - [View] paginator.num_pages : 해당 페이지네이션의 페이지 수(마지막 페이지 번호)를 저장한 값