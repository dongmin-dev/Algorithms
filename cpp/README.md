# C++

C++ 알고리즘 풀이를 저장하는 공간입니다. 예를 들어 Programmers 문제는 `programmers/문제이름.cpp`처럼 플랫폼별로 정리할 수 있습니다.

단일 소스 파일은 저장소 루트에서 다음처럼 컴파일하고 실행합니다. 출력 파일은 저장소 밖에 두어 풀이 파일만 Git에 남깁니다.

```sh
g++ -std=c++17 -Wall -Wextra -O2 cpp/programmers/문제이름.cpp -o /tmp/algorithm
/tmp/algorithm
```

위 경로는 앞으로 해당 풀이 파일을 만들었을 때 사용할 예시입니다.
