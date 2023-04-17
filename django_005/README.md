# Model Relationships (N:1)
Tue Apr 11 13:53:47 KST 2023
--- 
## 실습 목표
- N:1 관계의 개념을 이해한다.
- 연관 관계가 있는 두 모델의 N:1 관계를 설정할 수 있다.
- 관계가 설정된 다른 모델의 객체를 검색할 수 있다.

## 제출 안내
프로젝트 및 앱 폴더를 압축하여 실라버스 과제 제출란에 제출
> 가상환경 폴더(venv)는 제출하지 않습니다.


## 참고 문서
- [Django Many-to-one relationships](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/) 

---
--- 
--- 

## 개발 명세서
 
### ```Subject```
> 댓글, 영화, 리뷰, 사용자가 N:1 관계 설정된 웹 서비스 개발

### ```Environment```
- django 버전 : 3.2.18
- Database : SQLite

### ```App & Model```

**ERD(Entity Relationship Diagram)**

>User
- 앱 이름 : accounts
- 모델 이름 : User
- AbstractUser 클래스 상속

>Review
- 앱 이름 : reviews
- 모델 이름 : Review
- 필수 필드

| 필드 이름 | 역할 |
|---|---|
| user | 리뷰 작성자 |
| title | 리뷰 제목 |
| content | 리뷰 내용 |
| movie | 영화 제목 |

>Comment
- 앱 이름 : reviews
- 모델 이름 : Comment

| 필드 이름 | 역할 |
|---|---|
| user* | 댓글 작성자 |
| review** | 댓글 작성 리뷰 |
| content | 댓글 내용 |

*ForeignKey, 
** on_delete=models.CASCADE

**Django Form**

>Review
- 폼 이름 : ReviewForm
- 폼 모델 : Review
- 입력 필드
```
title
content
movie
```

>Comment
- 폼 이름 : CommentForm
- 폼 모델 : Comment
- 입력 필드
```
content
```

**skeleton code**
아래 기능이 구현된 스켈레톤 코드를 다운로드 받아서 실습 진행 다운로드
회원가입 / 로그인 / 로그아웃
리뷰 생성, 조회
댓글 생성, 조회, 삭제
**리뷰 생성**
- POST reviews/create/
```
ReviewForm 유효성 검사 통과시 데이터 생성
```
- GET reviews/create/
```
리뷰 생성 폼 렌더링
```


**리뷰 전체 조회**
- GET reviews/


**리뷰 단일 조회 & 댓글 전체 조회**
- GET reviews/<int:review_pk>/
```
pk가 review_pk인 리뷰 데이터 단일 조회
  - 단일 조회 템플릿 렌더링
  - 댓글 생성 폼(CommentForm) 렌더링
  - 해당 리뷰를 참조하는 댓글 전체 조회
```
    
    
**댓글 생성**
- POST reviews/<int:review_pk>/comments/
```
댓글 생성 과정
  - 사용자 입력 데이터로 CommentForm 인스턴스 생성
  - 유효성 검사
  - Comment 인스턴스만 생성
  - Comment 인스턴스에 참조하는 review 할당
  - Comment 인스턴스 저장
  - redirect GET reviews/<int:review_pk>/
```
    
    
**댓글 삭제**
- POST reviews/<int:review_pk>/comments/<int:comment_pk>/delete/
```
pk가 comment_pk인 댓글 삭제
  - redirect GET reviews/<int:review_pk>/
```

**예시 이미지**
댓글 조회, 생성, 삭제



### Try. 댓글 개수 출력
- 각 리뷰 단일 조회 페이지에서 해당 리뷰에 작성된 댓글 개수 출력
- 참고 문서 : [querysets count()](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#count)

### Try. 리뷰 영화 이미지 업로드
- 사용자가 리뷰 생성시 해당 영화와 관련된 이미지를 업로드할 수 있도록 개선
- 업로드 한 이미지를 조회 페이지에서 출력