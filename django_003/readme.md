Django Staticfiles

## 실습 목표
Django Staticfiles를 사용하여 정적 파일을 웹 서비스에 적용할 수 있다.
Django Mediafiles를 사용하여 사용자가 업로드한 파일을 저장하고, 활용할 수 있다.

## 개발 명세서

### Environment
django 버전 : 3.2.18
Database : SQLite
필수 패키지
- Pillow


### App & Model
Album
- 앱 이름 : albums
- 모델 이름 : Album
- 모델 필드 및 속성
```
필드 이름	역할	django 필드	속성
content	내용	Char	max_length=20
image	이미지	Image	blank=True, upload_to='임의 경로'
```
Django Form
- 폼 이름 : AlbumForm
- 폼 모델 : Album
- 필드 : content, image
