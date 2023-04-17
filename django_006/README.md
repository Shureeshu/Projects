# Django 15 - Model Relationships (N:M)


## 게시글 좋아요

articles/urls, views.like

- POST articles/<int:article_pk>/likes/
    1. article_pk에 해당하는 article을 조회
    1. 해당 article의 like_users 필드에 사용자가 존재하면exists 삭제remove
    1. 해당 article의 like_users 필드에 사용자가 존재하지 않으면 추가add

- 비로그인 사용자는 게시글 좋아요 버튼이 비활성화(disabled) 상태입니다.

- 로그인 사용자는 게시글 좋아요 버튼이 활성화 상태여야 하며 버튼을 눌려 좋아요를 남길 수 있습니다.

- 사용자는 각 게시글의 좋아요를 취소할 수 있습니다.

- 각 게시글에 해당 게시글의 총 좋아요 수를 출력합니다.