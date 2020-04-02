# Premable
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")

class Bandit:
  def __init__(self, m):
    self.m = m
    self.mean = 0
    self.N = 0

  def pull(self):
    return np.random.randn() + self.m

  def update(self, x):
    self.N += 1
    self.mean = (1 - 1.0/self.N)*self.mean + 1.0/self.N*x


def run_experiment(m1, m2, m3, eps, N):
  bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

  data = np.empty(N)
  
  for i in range(N):
    # epsilon greedy
    p = np.random.random()
    if p < eps:
      j = np.random.choice(3)
    else:
      j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)

    # for the plot
    data[i] = x
  cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

  # plot moving average ctr
  plt.plot(cumulative_average)
  plt.plot(np.ones(N)*m1,ls='--')
  plt.plot(np.ones(N)*m2,ls='--')
  plt.plot(np.ones(N)*m3,ls='--')
  plt.xscale('log')
  plt.show()

  for b in bandits:
    print(b.mean)

  return cumulative_average # Return the cumulative Average reward

if __name__ == '__main__':
  c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000)
  c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000)
  c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)
  c_0 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000)

  # Run experiments and get the Linear plot and Log plot
  # We do this on a log scale too so that you can see the fluctuatuons in the
  # earlier rounds more clearly
  # Plot 1
  plt.title("Linear Multi-arm Bandit",fontsize=20)
  plt.xticks(rotation=45,fontsize=12,c='black')
  plt.yticks(fontsize=12,c='black')
  plt.plot(c_0,  label=' $\epsilon = 0,$ $ Greedy$',lw=2,c = 'black')
  plt.plot(c_1,  label=' $\epsilon-greedy $ $ \epsilon = 0.1$',lw=2,c = 'blue')
  plt.plot(c_05,  label='$\epsilon-greedy$ $  \epsilon = 0.05$',lw=2,c = 'red')
  plt.plot(c_01,  label='$\epsilon-greedy $ $ \epsilon = 0.01$',lw=2,c = 'green')
  plt.xlabel("Steps", fontsize=15)
  plt.ylabel("Average Reward", fontsize=15)
  plt.legend(loc="best", fontsize=15)
  plt.xscale('log')
  plt.show()


  # Plot 2
  plt.title("Log  Multi-arm Bandit",fontsize=20)
  plt.xticks(rotation=45,fontsize=12,c='black')
  plt.yticks(fontsize=12,c='black')
  plt.plot(c_0,  label=' $\epsilon = 0,$ $ Greedy$',lw=2, c = 'black')
  plt.plot(c_1,  label=' $\epsilon-greedy $ $ \epsilon = 0.1$',lw=2, c = 'blue')
  plt.plot(c_05,  label='$\epsilon-greedy$ $  \epsilon = 0.05$',lw=2,c = 'red')
  plt.plot(c_01, label='$\epsilon-greedy $ $ \epsilon = 0.01$',lw=2,c = 'green')
  plt.xlabel("Steps", fontsize=15)
  plt.ylabel("Average Reward", fontsize=15)
  plt.legend(loc="best", fontsize=15)
  plt.show()

#help(plt.plot)