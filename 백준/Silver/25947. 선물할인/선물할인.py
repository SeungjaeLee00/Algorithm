n, b, a = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
# print(nums)

right = 0
left = 0

while right < n:
    if right - left < a:
        b -= nums[right] // 2
        if b < 0:
            break
        right += 1
    else:
        if a > 0:
            b -= nums[left] // 2
            left += 1
        else:
            b -= nums[right]
            if b < 0:
                break
            right += 1

print(right)