# 프로그래머스 # 2개 이하로 다른 비트

# 풀이 1
'''
비트마스킹을 떠올리긴 했지만, 일단 어떻게든 해낸 풀이
'''
def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = bin(number)[2:]
        target = bin_number.rfind('0')
        if bin_number[-1] == '0':
            answer.append(int('0b' + bin_number[:-1]+'1', 2))
            continue
        if target == -1:
            answer.append(int('0b10' + '1' * (len(bin_number) -1), 2))
            # answer.append(1 << len(bin_number) | (1 << len(bin_number) - 1) - 1)
        else:
            answer.append(int('0b' + bin_number[:target] + '10' + '1' * len(bin_number[target+2:]), 2))
            # answer.append(number | (1 << (len(bin_number) - target + 1)) - 1)
    return answer

# 풀이 2
'''
number보다 큰 1번째 수는 (number + 1) 이다.
(number + 1) 과 number 간에 XOR 연산을 수행하면, 어디서부터 비트가 달라지는지 + 총 몇 비트가 다른지를 구할 수 있다.
한 비트가 달라지면 그 이후꺼도 다 달라지기 때문. ex) 숫자 23(10111)와 24(11000)에 대한 XOR을 수행하면, 1111 이 나온다. 
만약 XOR 결과가 1 혹은 11이라면, (number + 1)이 [2개 이하로 다른 비트]라는 조건을 만족한다. 따라서 정답은 (number + 1).
반면 XOR 결과가 111 이상이라면, 앞에꺼 두개 비트는 그대로 다르도록 유지하되, 나머지 비트는 같도록 조정해줘야 '2개 이하로 다른 비트'라는 문제 조건이 성립한다.
위의 23과 24의 예제를 다시 살펴보면, 24(11000)은 원래 숫자 23(10111)과 4개의 비트(XOR 결과가 1111)가 다르다.
하지만 문제 조건에 따라 최대 2개 비트까지만 다를 수 있다. 따라서 11000에 가장 오른쪽의 두 비트를 11을 더해 조정해주어야 한다.
이를 달리 표현하면, (1111 >> 2) == (11) 을 더해 조정해주어야 한다.
따라서 어떤 number에 대해 2개 이하로 다른 비트를 가진 최소 숫자를 구하려면,
(number + 1) 과 (number) 의 XOR 결과를 >> 2 해준 다음에, 이를 (number + 1)에 더해주면 되는 것이다 ! 

마지막으로 덧붙이자면, 짝수와 홀수를 구분할수도 있다.
만약 number 가 짝수라서 2의 0승에 해당하는 가장 오른쪽 자리가 1이라면, XOR 수행하면 1이 나온다. 1 >> 2 는 0이므로, 정답은 그냥 (number+1) + 0 = (number + 1) 이 된다.
'''
def solution(numbers):
    return [(((number + 1) ^ number) >> 2) + (number + 1) for number in numbers]
