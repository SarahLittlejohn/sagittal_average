import numpy as np
import test_call_command

data_input = np.zeros((20, 20))
data_input[-1, :] = 20
data_input[-2, :] = 19
data_input[-3, :] = 18
data_input[-4, :] = 17
data_input[-5, :] = 16
data_input[-6, :] = 15
data_input[-7, :] = 14
data_input[-8, :] = 13
data_input[-9, :] = 12
data_input[-10, :] = 11
data_input[-11, :] = 10
data_input[-12, :] = 9
data_input[-13, :] = 8
data_input[-14, :] = 7
data_input[-15, :] = 6
data_input[-16, :] = 5
data_input[-17, :] = 4
data_input[-18, :] = 3
data_input[-19, :] = 2
data_input[-20, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')
expected = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

test_call_command.run_sagittal_brain()

actual = np.genfromtxt("brain_average.csv", delimiter=',')
print("Expected:", expected)
print("Actual:", actual)

assert np.array_equal(expected, actual)