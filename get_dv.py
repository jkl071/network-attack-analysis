#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:46:28 2019

@author: jamie


Intended to be a script where all functions that are utilized in 36 experiments are

"""
import pandas as pd


path = '/Users/jamie/Desktop/network_output/second_round_of_subs_9assignment_HIT/'
worker_id = 'A17MUS17DFQZ4P'
task = 'n_back_with_predictable_task_switching'


full_path = path + worker_id + '/' + task + '_' + worker_id + '.csv'

df = pd.read_csv(full_path)

def getAvgRT():
    

