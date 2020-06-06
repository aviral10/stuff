"""
Surprisingly it sticks around 0.3 everytime
"""

import random
from matplotlib import pyplot as plt


def simulate(n, prisoners):
    numbers = list(range(1, prisoners + 1))
    cases = []
    ratio = []
    for run in range(1, n + 1):
        random.shuffle(numbers)
        # print(numbers)
        successful = 0
        unsuccessful = 0
        for prisoner_number in range(1, prisoners + 1):
            choice = prisoner_number

            for j in range(1, prisoners // 2 + 1):
                if numbers[choice - 1] == prisoner_number:
                    successful += 1
                    break
                choice = numbers[choice - 1]
            else:
                unsuccessful += 1
        #  print(f"Trial {run} successful: {successful}   Unsuccessfull:{unsuccessful}")
        cases.append((successful, unsuccessful))
        ratio.append(successful / prisoners)
    return cases, ratio


# Tweak these parameters
value = 20
prisoners = value
total_runs = value
case = 100

pav = 0
p_list = []
p_avg = []
for _ in range(case):
    ans, ratios = simulate(total_runs, prisoners)
    # print(ans)
    # print(ratios)
    ones = ratios.count(1)
    # print(ones)
    p = ones / total_runs
    p_list.append(p)
    pav = sum(p_list)/(len(p_list))
    p_avg.append(pav)

# print(p_list)
# print(p_avg)

print("Probability of Prisoners Surviving: ", sum(p_list)/len(p_list))


x = range(1, len(p_list)+1)
y = p_list
plt.plot(x, y, color="green")
plt.plot(x, p_avg, color="red")
plt.ylabel('Success Probability')
plt.xlabel('Cases#')
plt.show()
