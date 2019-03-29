from untested_nn import *
import random
n_test_cases = 0
n_succ_cases = 0
n_fail_cases = 0

for s in sentences[:5]:
    if len(s) > 2:
        n_test_cases += 1
        item_we_need = s.pop(random.randint(0, len(s) - 1))
        print(item_we_need)
        print(predict(s))
