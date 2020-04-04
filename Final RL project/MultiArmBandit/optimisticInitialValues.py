
# Premable
import numpy as np
import matplotlib.pyplot as plt
from ComparingEpsilons import run_experiment as run_experiment_eps # Needed from previous problem


class Bandit:
  def __init__(self, m, upper_limit):
    self.m = m
    self.mean = upper_limit
    self.N = 1

  def pull(self):
    return np.random.randn() + self.m

  def update(self, x):
    self.N += 1 # Use N as a counter
    self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N*x


def run_experiment(m1, m2, m3, N, upper_limit=10):
  bandits = [Bandit(m1, upper_limit), Bandit(m2, upper_limit), Bandit(m3, upper_limit)]

  data = np.empty(N)
  
  for i in range(N):
    # optimistic initial values
    j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)

    # for the plot
    data[i] = x
  cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

  # plot moving average ctr
  plt.plot(cumulative_average)
  plt.plot(np.ones(N)*m1)
  plt.plot(np.ones(N)*m2)
  plt.plot(np.ones(N)*m3)
  plt.xscale('log')
  plt.show()

  for b in bandits:
    print(b.mean)

  return cumulative_average

if __name__ == '__main__':
  c_1 = run_experiment_eps(1.0, 2.0, 3.0, 0.1, 100000)
  oiv = run_experiment(1.0, 2.0, 3.0, 100000)

  # Run the experiments and get the linear plot and log plot 
  # Plot 1
  plt.title("Multi-arm Bandit", fontsize=20)
  plt.xticks(rotation=45,fontsize=12,c='black')
  plt.yticks(fontsize=12,c='black')
  plt.plot(c_1, label='Realistic , $\epsilon$-greedy $Q_{1}=0$ $\epsilon = 0.1$',color="blue",lw=2)
  plt.plot(oiv, label='Optimistic  , greedy $Q_{1}=10$  $\epsilon = 0$',color="red",lw=2)
  plt.xlabel("Steps", fontsize=15)
  plt.ylabel("Average Reward", fontsize=15)
  plt.legend(loc="best", fontsize=15)
  plt.xscale('log')
  plt.show()


  # Plot 2
  plt.title("Log Multi-arm Bandit", fontsize=20)
  plt.xticks(rotation=45,fontsize=12,c='black')
  plt.yticks(fontsize=12,c='black')
  plt.plot(c_1, label='Realistic $Q_{1}=0$, $\epsilon$-greedy $\epsilon = 0.1$',color="blue",lw=2)
  plt.plot(oiv, label='Optimistic $Q_{1}=10$, greedy $\epsilon = 0$',color="red",lw=2)
  plt.xlabel("Steps", fontsize=15)
  plt.ylabel("Average Reward", fontsize=15)
  plt.legend(loc="best", fontsize=15)
  plt.show()

