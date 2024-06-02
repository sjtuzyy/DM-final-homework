import numpy as np
import matplotlib.pyplot as plt
test = np.load(r"C:\Users\Steve12\Desktop\datamining\project\LTSF-Linear\LTSF-Linear\results\test_DLinear_university_ftS_sl96_ll48_pl400_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_test_0\real_prediction.npy")
test = test[-1:]
test = np.squeeze(test)
def expand(input,windowsize):
    tag = np.zeros(windowsize-1)
    tag.fill(np.infty)
    expanded_input = np.concatenate([tag,input])
    expanded_input = np.concatenate([expanded_input,tag])
    return expanded_input
def moving_average(input,windowsize):
    expand_input = expand(input,windowsize)
    result = []
    for i in range(len(expand_input)-windowsize):
        total = 0
        count = 0
        for j in range(windowsize):
            if expand_input[i+j] != np.infty:
                total += expand_input[i+j]
                count += 1
        ave = total/count
        result.append(ave)
    return result 
after = moving_average(test,7)
np.save('pred.npy',after)
plt.figure()
plt.plot(after, label='pred', linewidth=2)
plt.show()
print(after)