N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
result_lst = []


for i in range(N):              # N까지의 숫자 중에서 i 고르고
    for j in range(i+1,N):      # i 이후부터 N까지 중에서 고르고
        for k in range(j+1, N): # j 이후부터 N까지 중에서 골라서 총 숫자 세 개 선택
            sum_n = num_lst[i] + num_lst[j] + num_lst[k]
            # 리스트에서 각 인덱스에 해당하는 숫자들 다 더해서 
            if sum_n <= M:                  # 만약 M보다 작거나 같은 경우에만 결과 리스트에 추가
                result_lst.append(sum_n)
print(max(result_lst))                      # 리스트 내부 값 중 최대값 출력