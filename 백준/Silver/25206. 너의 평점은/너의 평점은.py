rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0  # 학점 총합을 담을 변수
result = 0  # (학점 * 과목평점) 총합을 담을 변수
for _ in range(20) :
    i, j, k = input().split()  # 과목명, 학점, 등급
    j = float(j)  # 학점
    if k != 'P':  # P는 계산에서 제외
        total += j
        result += j * grade[rating.index(k)]

print('%.4f' % (result / total))