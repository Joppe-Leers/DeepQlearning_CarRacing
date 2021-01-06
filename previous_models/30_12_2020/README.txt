input_DQN = 3 opeenvolgende schermen (één observatie)
output_DQN = integer van 0 tot 6 dat overeenkomt met één van de volgende action space
action_space    = [
            (0, 0, 0), 
            (-1, 0.5, 0), 
            (1, 0.5, 0),
            (0, 1,   0), 
            (0, 0,   0.5), 
            (-1, 0, 0.2), 
            (1, 0, 0.2)
        ],

STARTING_EPISODE              = 1
ENDING_EPISODE                = 1000
SKIP_FRAMES                   = 2
TRAINING_BATCH_SIZE           = 64
SAVE_TRAINING_FREQUENCY       = 25
UPDATE_TARGET_MODEL_FREQUENCY = 5

episode eindigen wanneer de agent 100 negative rewards op een rij krijgt
reward *= 1.5 wanneer een actie koos waar de voledige gas is ingedrukt
