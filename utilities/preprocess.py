import os
import errno
import json
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm

from utilities.midi_io import MIDI


def mkdir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def get_maestro_midi_list(split):
    maestro_json = pd.read_json('./dataset/maestro-v3.0.0/maestro-v3.0.0.json')
    midi_list = maestro_json.loc[maestro_json['split'] == split]['midi_filename'].values.tolist()
    return midi_list


def preprocess(style, aug):
    if style == "CSQ":
        time_set = [0, 1 / 32, 1 / 16, 1 / 12, 1 / 8, 1 / 6, 3 / 16, 1 / 4, 1 / 3, 3 / 8, 1 / 2, 2 / 3, 3 / 4, 1]
        index_filename = "aimgef-assets/CSQ/fast_first/index.json"
        with open(index_filename, mode="r") as f:
            midi_list = json.load(f)
        for midi in tqdm(midi_list):
            valid_set = [1211, 1219, 1240, 1827, 1893, 2322, 2368]  # 1207, 1227, 1836, 1901, 1908, 2340, 2325
            split = "train" if midi["ID"] not in valid_set else "validation"
            if aug:
                ps = [-3, -2, -1, 0, 1, 2, 3]
                ts = [0.95, 0.975, 1.0, 1.025, 1.05]
            else:
                ps = [0]
                ts = [1.0]
            for p in ps:
                for t in ts:
                    excerpt = MIDI(os.path.join("aimgef-assets/CSQ/fast_first/midi", f'{midi["ID"]}.mid'), None, time_set).get_events(True, p, t)
                    filename = os.path.join("datasets", style, split, f'{midi["ID"]}_p{p}_t{t}.npy')
                    mkdir(filename)
                    np.save(filename, np.array(excerpt, dtype=int))

    elif style == "CPI":
        for split in ["test", "validation", "train"]:
            fi = 0
            midi_list = get_maestro_midi_list(split)
            for midi in tqdm(midi_list):
                mid = MusicBox(f"./datasets/maestro-v3.0.0/{midi}", None)
                if mid.num_tracks != 1:
                    continue
                if aug:
                    ps = [-3, -2, -1, 0, 1, 2, 3]
                    ts = [0.95, 0.975, 1.0, 1.025, 1.05]
                else:
                    ps = [0]
                    ts = [1.0]
                for p in ps:
                    for t in ts:
                        excerpt = mid.get_events(True, p, t)
                        filename = f"./datasets/{style}/{representation}/{split}/{fi // 1000}/{fi}.npy"
                        mkdir(filename)
                        np.save(filename, np.array(excerpt))
                        fi += 1
