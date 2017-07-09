import numpy as np
from matplotlib import pyplot as plt

def plot_stepAvgReward(num_steps, line_data):
    x = np.linspace(0, num_steps, num=num_steps)
    plt.figure(figsize=(16, 8))
    for data,label in line_data:
        plt.plot(x, data, label=label)
    plt.title('Average reward vs steps')
    plt.legend(loc='lower right')
    plt.show()