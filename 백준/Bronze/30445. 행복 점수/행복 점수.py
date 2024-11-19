message = input().strip()
# print(message)

h_count = 0
g_count = 0

for char in message:
    if char in "HAPPY":
        h_count += 1
    if char in "SAD":
        g_count += 1

if h_count == 0 and g_count == 0:
    happiness = 0.5
else:
    happiness = h_count / (h_count + g_count)

happiness_percentage = "{:.2f}".format(happiness * 100 + 1e-12)

print(happiness_percentage)