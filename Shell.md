### shell 특수 문자 정리

## 특수 매개변수

특수 매개변수는 bash쉘이 linux또는 unix 시스템의 bash 스크립트에서 특별한 값을 처리하는 매개 변수입니다. 이 bash 스클비트 매개변수의 중요한점은 참조만 가능하고 값을 지정할 수 없다는 것입니다. 

| 문자  | 설명                                        |
| --- | ----------------------------------------- |
| $$  | 현재 쉘 스크립트의 PID                            |
| $?  | 프로그램의 종료값을 저장 (참과 거짓 반환코드 값)              |
| $!  | 마지막 작업의 PID (종료되지 않은 방금 전에 실행된 프로세스의 PID) |
| $-  | 현재 옵션의 플래그                                |
| $_  | 지난 명령의 마지막 인자로 설정된 특수 변수                  |

## 위치 매개 변수

위치 매개 변수는 쉘 프로그램 내의 변수입니다. 해당 값은 프로그램을 호출하는 명령 행에 지정된 인수에서 설정됩니다.  

위치 매개 변수는 번호가 매겨지며 $1, $2, $3 등과 같이 앞에 "$"로 표시됩니다.

| 문자  | 설명                                                                  |
| --- | ------------------------------------------------------------------- |
| $0  | 실행된 쉘 스크립트의 이름<br>                                                  |
| $*  | 위치 매개변수 (매개변수 인자의 모든 리스트)                                           |
| $@  | 위치 매개변수 ($*과 똑같지만 각 매개변수는 quiting 된 문자열로 취급)                        |
| $숫자 | 쉘 스크립트에 넘겨진 숫자에 따른 인자의 값 ($1, $2, $3 ... ${10} -> 10부터는 괄호로 묶음)<br> |
| $#  | 쉘 스크립트에 넘겨진 인자의 총 갯수                                                |

## 와일드 카드

와일드 카드는 검색에서 문자 클래스를 대체 할 수있는 문자로 검색의 유연성과 효율성을 크게 향상시킵니다.  

와일드 카드는 일반적으로 Linux 및 기타 Unix 계열 운영 체제의 쉘 명령에 사용됩니다.

| 문자  | 설명                                           |
| --- | -------------------------------------------- |
| *   | 매칭되는 모든 문자를 나타내는 특수 문자로 쉘에서 *는 0개 이상의 문자로 대체 |
| [ ] | 문자 범위 지정하는 특수 문자로 [] 괄호 안에 포함된 문자 중 하나를 나타냄  |
| ?   | 매칭되는 하나의 문자를 나타내는 특수 문자 (쉘에서 ?는 1개의 문자로 대체)  |

## 쿼팅 (인용 ) 관련

uoting은 특정 문자나 단어가 쉘에 특수한 의미를 제거하는데 사용됩니다.  

Quoting은 특수 문자에 대한 특수 처리를 비활성화하고 예약어가 인식되지 않도록하고, 매개 변수 확장을 방지하는 데 사용할 수 있습니다.

| 문자          | 설명                                                                                                        |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| ' '         | 뒤에 오는 모든 특수문자를 일반 문자로 인식 (모든 특수 문자 쿼팅)                                                                    |
| " "         | " " 사이에 들어있는 모든 특수 문자를 일반 문자로 인식하지만단, $()와  ` `(명령어 대체 특수문자),  $ (변수 값 대체 특수문자), \ (quotation 특수문자) 등은 예외 |
| \           | 특수문자 바로 앞에 사용되는데 해당 특수문자의 효과를 없애고 일반 문자처럼 처리 (뒤에 한 특수문자만 쿼팅)                                              |
| ` ` (역 따옴표) | 역 따옴표는 따옴표 안에 있는 명령문의 실행하여 실행결과를 대입                                                                       |

## 입출력 리다이렉션

리디렉션을 통해 명령의 파일 핸들을 복제, 열기, 닫기, 다른 파일을 참조 할 수 있으며 명령을 읽고 쓰는 파일을 변경할 수 있습니다.  

현재 쉘 실행 환경에서 파일 핸들을 수정하기 위해 리디렉션을 사용할 수도 있습니다.

| 문자  | 설명                              |
| --- | ------------------------------- |
| <   | 입력 재지정                          |
| >   | 출력 재지정 (표준 출력 파일을 바꿈)           |
| >>  | 출력 재지정 (파일의 내용을 추가하는 역할, 이어 쓰기) |

## 다중 명령 관련

다중 명령을 사용할 경우 연산자에 따라서 출력을 다른 명령으로 보내거나 다음 명령어의 실행 여부를 결정할 수 있습니다.

| 문자  | 설명                                            |
| --- | --------------------------------------------- |
| \|  | 명령과 명령을 연결 (왼쪽 명령의 실행결과를 오른쪽 명령어의 입력으로 전달)    |
| ;   | 명령과 명령을 연결 (연결된 명령을 왼쪽부터 차례로 실행)              |
| &&  | 이전 명령이 정상 종료인 0의 값을 반환할 경우, 다음 명령 실행 (AND 연산) |
| \|  | 이전 명령이 비정상 종료인 1의 값을 반환할 경우, 다음 명령 실행 (OR 연산) |