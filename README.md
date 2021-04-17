# Numerical-Analysis

# 근 구하기 알고리즘

## 이분법(dichotomy)
  1) 주어진 구간 a<x<b 에서 중간점 c를 구한다. (c = (a+b)/2)
  2) 중간점의 함수값을 f(c)라고 하자.
  3) f(c)의 부호를 f(a) 또는 f(b)와 비교한다.
  4) 부호가 다른 구간에 해가 있으므로 새로운 구간을 정의한다. (f(a) = f(c) 또는 f(b) = f(c) )
  5) 위 과정을 반복하며 가장 근사한 해를 구한다.

    - 구간이 적절하다면 거의 확정적으로 해를 찾을 수 있다.
    - 하지만 모든 영역을 나누어 가면서 탐색해야 하므로 시간이 오래 걸릴 수 있다.
<img width="139" alt="스크린샷 2021-04-16 오후 5 19 37" src="https://user-images.githubusercontent.com/46489446/114994628-ed389e00-9ed7-11eb-8c0c-d7aec3d80c39.png">
<img width="606" alt="스크린샷 2021-04-16 오후 5 19 58" src="https://user-images.githubusercontent.com/46489446/114994667-f9bcf680-9ed7-11eb-9c16-0ee74f7ffb40.png">

## 고정점 반복법(fixed point iteration)

  연속함수 g(x)에 대해서 g(x) = x 를 만족하는 해를 고정점(fixed point)라고 할때
  1. f(x) = 0의 해 A를 구하는 문제
  - 함수 g(x) = x - f(x) 로 정의하면 g(A) = A 가 되므로 g(x)의 고정점을 찾는 문제이다.
  2. f(x) = g(x) - x 로 정의 했을때 f(x) = 0 의 해를 구하는 문제

  => f(x) = 0 과 g(x) = x 해를 찾는 문제들은 서로 동치다.
  적절한 반복함수 g(x)를 정의하면 고정점 반복법을 이용하여 f(x) = 0의 근사해를 구할 수 있다.

  - 그래프가 있을때 y=x그래프를 활용하여 y값의 위치를 통해 x값의 위치를 구하여 계산할 수 있다.
  - f(x) = -x^2 + 6x -5 가 있으면 좌변에 1차의 x가 오도록 수정
  6x = x^2 + 5
  x = 1/6(x^2 + 5)
  => x = g(x) 꼴의 형태

<img width="161" alt="스크린샷 2021-04-16 오후 5 22 13" src="https://user-images.githubusercontent.com/46489446/114994942-4accea80-9ed8-11eb-9452-f689bbd3c674.png">
<img width="582" alt="스크린샷 2021-04-16 오후 5 22 35" src="https://user-images.githubusercontent.com/46489446/114995014-58827000-9ed8-11eb-8cee-a49d0378978f.png">

