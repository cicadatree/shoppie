import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def choose_statistic(x, sampleStatText):
  # calculate mean if the text is "Mean"
  if sampleStatText == "Mean":
    return np.mean(x)
  # calculate minimum if the text is "Minimum"
  elif sampleStatText == "Minimum":
    return np.min(x)
  # calculate variance if the text is "Variance"
  elif sampleStatText == "Variance":
    return np.var(x, ddof=1)
  # raise error if sampleStatText is not "Mean", "Minimum", or "Variance"
  else:
    raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')

def population_distribution(populationData):
  # plot the population distribution
  sns.histplot(populationData, stat='density')
  # informative title for the distribution 
  plt.title(f"Population Distribution")
  # remove None label
  plt.xlabel('')
  plt.show()
  plt.clf()

def samplingDistribution(populationData, sampSize, stat):
  # list that will hold all the sample statistics
  sampleStats = []
  for i in range(2):
    # get a random sample from the population of size sampSize
    samp = np.random.choice(populationData, sampSize, replace = False)
    # calculate the chosen statistic (mean, minimum, or variance) of the sample
    sampleStat = choose_statistic(samp, stat)
    # add sampleStat to the sampleStats list
    sampleStats.append(sampleStat)
  
  popStatistic = round(choose_statistic(populationData, stat),2)
  # plot the sampling distribution
  sns.histplot(sampleStats, stat='density')
  # informative title for the sampling distribution
  plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sampleStats), 2)} \n Population {stat}: {popStatistic}")
  plt.axvline(popStatistic,color='g',linestyle='dashed', label=f'Population {stat}')
  # plot the mean of the chosen sample statistic for the sampling distribution
  plt.axvline(np.mean(sampleStats),color='orange',linestyle='dashed', label=f'Mean of the Sample {stat}s')
  plt.legend()
  plt.show()
  plt.clf()
  return sampleStat

# generate random list of 100 values between 1 and 10 (representing NPS scores), stored in scoreList
scoreList = []
numOfScores = 100
for i in range(0,numOfScores):
    n = random.randint(0,9)
    scoreList.append(n)

# df is a variable storing a pandas array of scoreList
df = pd.array(scoreList)

# create an empty list; container for sampDist Mean values
sampDistList = []

# main loop
while True:
    # generate a sampling distribution from the population set df
    # samplingDistribution() plots and displays a histogram of the data about the Mean (in this case sampling 50 observations from the population set)
    sampDist = samplingDistribution(df, 50, "Mean")

    # populate sampDistList with 10 sample distribution means
    if len(sampDistList) < 10:
        sampDistList.append(sampDist)
    elif len(sampDistList) >= 10:
        break

print(sampDistList)






