day02

crome - F12 - id값 copy selector
vscode 왼쪽 가장 아래 클릭 -> vscode 검색 -> vscode icons 다운

*typora
- 앞에 #
- 앞 뒤로 ** -> 볼드체 (ctrl + b)
- 앞뒤로 * -> 기울임 (ctrl + i)
- 앞뒤로 ` <- 1옆에 있음
- 코드 블록 ``` -> 무슨 언어로 할 지
- ![] () -> 이미지 입력 
- 테이블 작성 -> ctrl + t
- ctrl+ / 누르면 코드 보기
- 대쉬 + space, * + space
- [TOC]
- 링크걸기 []()

git
#SCM(소스코드매니저) #DVCS(분산형 버전 관리 시스템) #오픈소스
- (분산) 버전 관리 시스템
- 코드 히스토리 관리 도구 
- 개발 과정 볼 수 있음. 이전 버전 복원, 변경사항 비교, 분석 및 병합도 가능

git 작업흐름
- add : 커밋 목록에 추가
- commit : 커밋 만들기(코드를 저장)
- push : 현재까지의 역사(커밋)가 기록된 곳에 새로 생성한 커밋 반영

- 작업파일(Working directory)-> add -> 커밋 목록(INDEX, staging area) -> commit -> 쌓인 커밋들(HEAD) -> push -> Github

$ git add ______ 
$ git commit -m <- 필수
$ git config --global ______ ->  arguments 2개

**중요**
- 자리를 옮기게 되면 git 초기화를 해야함
1. git bash 실행 후 , 미리 설정되었을지 모를 계정 정보 삭제(처음 설치 시 생략 가능)
$ git config --global --unset credential.helper
$ git config --system --unset credential.helper
2. windows 자격 증명 관리자에서 git 관련 정보 삭제
3. git bash 실행 후 아래와 같이 입력
$ git credential reject
protocol=https
host=github.com

- 진행하고 있는 폴더 안에서만 git init 해야됨