## 좋은 커밋 메세지를 작성하기 위한 규칙들
***
### Github commit 메세지 규칙의 필요성 
* 팀원과의 소통
* 편리한 과거의 기록 추적
* 프로젝트 진행 사항을 확인가능

### 커밋 메세지의 7가지 규칙 
* 제목과 본문을 빈 행으로 구분한다.
* 제목을 50글자 이내로 제한한다.
* 제목의 첫글자는 대문자로 작성한다.
* 제목의 끝에는 마침표를 넣지 않는다.
* 제목은 명령문으로! 과거형을 사용하지 않는다
* 본문에서 어떻게 변경했는지보다 무엇을 왜 변경했는지 설명한다.
* 푸터는 선택상이며 관련된 이슈만 짧게 언급 보통 issue tracker ID를 명시하고 싶은경우 작성
* ex) Fixes:#1~#20 (Closes,Fixes,Resolves,Ref,Related to)

### Commit 메시지의 구조 
* 제목 (subject)

* 본문 (body)

* 푸터 (footer)

### 예시
* fix: CardList 컴포넌트 클릭 시 공백으로 나오는 오류 수정


* 모바일 버전에서 CardList의 img 부분 클릭 시 공백으로 나오는 오류 수정.
PC버전은 이상없음.


* Resolves: #232

### 자주 사용하는 단어
* 설명
  * Feat 새로운 기능을 추가할 경우 
  * Fix 버그를 고친 경우 
  * Design CSS 등 사용자 UI 디자인 변경 
  * !BREAKING CHANGE 커다란 API 변경의 경우 !HOTFIX 급하게 치명적인 버그를 고쳐야하는 경우 
  * Style 코드 포맷 변경, 세미 콜론 누락, 코드 수정이 없는 경우 
  * Refactor 프로덕션 코드 리팩토링 
  * Comment 필요한 주석 추가 및 변경 
  * Docs 문서를 수정한 경우 
  * Test 테스트 추가, 테스트 리팩토링(프로덕션 코드 변경 X) 
  * Chore 빌드 태스트 업데이트, 패키지 매니저를 설정하는 경우(프로덕션 코드 변경 X) 
  * Rename 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우 
  * Remove 파일을 삭제하는 작업만 수행한 경우

