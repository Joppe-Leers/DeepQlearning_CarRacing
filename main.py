from DQLalgorithm import DQLalgotirhm

if __name__ == '__main__':
    dql = DQLalgotirhm()
    dql.trainModel(episodes=2, render=True, skipFrames=2, trainingBatchSize=64, updateTargetModelFreq=5, saveModelFreq=25)
    # dql.continueTraining(fileName='trial_1000.h5', episodeOffset=1000, episodes=1, render=True, skipFrames=2, trainingBatchSize=64, updateTargetModelFreq=5, saveModelFreq=1, epsilon=0.01)
