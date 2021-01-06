# DeepQlearning_CarRacing
Deep Q-learning algorithm for my thesis. It should learn to drive a car

You have two options to train the model:

1) start from zero:
  Add these two lines in main.py and change the parameters to what you want

  dql = DQLalgotirhm()
  dql.trainModel(episodes=2, render=True, skipFrames=2, trainingBatchSize=64, updateTargetModelFreq=5, saveModelFreq=25)

2) start from a previously trained model:
  place the trained model (.h5 file) where you want to start from in the main repository
  use the folowing two lines in main.py and change the parameters to what you want

  dql = DQLalgotirhm()
  dql.continueTraining(fileName='trial_1000.h5', episodeOffset=1000, episodes=1, render=True, skipFrames=2, trainingBatchSize=64, updateTargetModelFreq=5, saveModelFreq=1, epsilon=0.01)
  
  episodeOffset is the amount of episodes the model had to train before.
  
  
