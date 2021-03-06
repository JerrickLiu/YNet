import pandas as pd
import yaml
import argparse
import torch
from model import YNet


CONFIG_FILE_PATH = 'config/sdd_longterm.yaml'  # yaml config file containing all the hyperparameters
EXPERIMENT_NAME = 'sdd_longterm_with_TTST_CWS'  # arbitrary name for this experiment
DATASET_NAME = 'sdd'

CHECKPOINT_PATH = 'pretrained_models/' + EXPERIMENT_NAME + '_weights.pt'

TRAIN_DATA_PATH = 'data/SDD/train_longterm.pkl'
TRAIN_IMAGE_PATH = 'data/SDD/train'
VAL_DATA_PATH = 'data/SDD/test_longterm.pkl'
VAL_IMAGE_PATH = 'data/SDD/test'
OBS_LEN = 5  # in timesteps
PRED_LEN = 30  # in timesteps
NUM_GOALS = 20  # K_e
NUM_TRAJ = 1  # K_a

BATCH_SIZE = 8

with open(CONFIG_FILE_PATH) as file:
    params = yaml.load(file, Loader=yaml.FullLoader)
experiment_name = CONFIG_FILE_PATH.split('.yaml')[0].split('config/')[1]
print(params)


df_train = pd.read_pickle(TRAIN_DATA_PATH)
df_val = pd.read_pickle(VAL_DATA_PATH)
print(df_train.head)

model = YNet(obs_len=OBS_LEN, pred_len=PRED_LEN, params=params)

model.train(df_train, df_val, params, train_image_path=TRAIN_IMAGE_PATH, val_image_path=VAL_IMAGE_PATH,
            experiment_name=EXPERIMENT_NAME, batch_size=BATCH_SIZE, num_goals=NUM_GOALS, num_traj=NUM_TRAJ, 
            device=None, dataset_name=DATASET_NAME, checkpoint_path=CHECKPOINT_PATH, use_checkpoint=True)
