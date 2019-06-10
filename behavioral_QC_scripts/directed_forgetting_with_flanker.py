#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:44:48 2018

@author: jamie

directed_forgetting_with_flanker

directed: pos pos neg con
shape matching: congruent incongruent

8 = lowest number of trials
full counterbalancing
160 trials total, 32 per block, 5 blocks

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'directed_forgetting_with_flanker_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

directed_conditions = ['pos','pos','con','neg']

congruent__pos = 0
congruent__con = 0
congruent__neg = 0

incongruent__pos = 0
incongruent__con = 0
incongruent__neg = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__neg += 1
        
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'pos' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__pos += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'con' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__con += 1
        
    elif test_trials.iloc[row].directed_forgetting_condition == 'neg' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__neg += 1
        
    
        
        
print("congruent__pos = " + str(congruent__pos) + " / " + str(len(test_trials)))
print("congruent__con = " + str(congruent__con) + " / " + str(len(test_trials)))
print("congruent__neg = " + str(congruent__neg) + " / " + str(len(test_trials)))

print("incongruent__pos = " + str(incongruent__pos) + " / " + str(len(test_trials)))
print("incongruent__con = " + str(incongruent__con) + " / " + str(len(test_trials)))
print("incongruent__neg = " + str(incongruent__neg) + " / " + str(len(test_trials)))


suspect_trial_timing = []
for row in range(0,len(df)-1):
    actual_duration = df.iloc[row + 1].time_elapsed - df.iloc[row].time_elapsed
    expected_duration = df.iloc[row + 1].block_duration + df.iloc[row].timing_post_trial
    
    if df.iloc[row + 1].trial_type == 'poldrack-categorize':
            expected_duration += 500
    
    if abs(expected_duration - actual_duration) > 50:
        suspect_trial_timing.append(str(df.iloc[row + 1].trial_index) + '_' + 
                                    task + '_' + 
                                    str(abs(expected_duration - actual_duration)) + '_' + 
                                    str(actual_duration) + '_' + 
                                    df.iloc[row + 1].trial_id + '_' +
                                    df.iloc[row + 1].trial_type)
        
if len(suspect_trial_timing) == 0:
    print('no suspect timing issues')
else: 
    print('check suspect_trial_timing array')