from untested_nn import sentences, predict
import random
n_test_cases = 0
n_succ_cases = 0
n_fail_cases = 0

for s in sentences:
    if len(s) > 2:
        n_test_cases += 1
        item_we_need = s.pop(random.randint(0, len(s) - 1))
        predictions = [i[0] for i in predict(s)]
        if item_we_need in predictions:
                n_succ_cases += 1
        else:
                n_fail_cases += 1


print("All cases: {}".format(n_test_cases))
print("Success cases: {}".format(n_succ_cases))
print("Failed cases: {}".format(n_fail_cases))
