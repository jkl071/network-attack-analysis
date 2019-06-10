#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:39:18 2018

@author: jamie

flanker with shape matching

280 total trials, 56 trials per block, 5 blocks

flanker: congruent vs incongruent
shape matching : ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']
full counterbalancing
14 = lowest number of trials 

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/flanker_with_shape_matching/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'flanker_with_shape_matching_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

congruent__DDD = 0
congruent__SDD = 0
congruent__DSD = 0
congruent__DDS = 0
congruent__SSS = 0
congruent__SNN = 0
congruent__DNN = 0

incongruent__DDD = 0
incongruent__SDD = 0
incongruent__DSD = 0
incongruent__DDS = 0
incongruent__SSS = 0
incongruent__SNN = 0
incongruent__DNN = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].flanker_condition == 'congruent' :
        congruent__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].flanker_condition == 'congruent':
        congruent__DNN += 1
        
    
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].flanker_condition == 'incongruent':
        incongruent__DNN += 1
        

        
        
print("congruent__DDD = " + str(congruent__DDD) + " / " + str(len(test_trials)))
print("congruent__SDD = " + str(congruent__SDD) + " / " + str(len(test_trials)))
print("congruent__DSD = " + str(congruent__DSD) + " / " + str(len(test_trials)))
print("congruent__DDS = " + str(congruent__DDS) + " / " + str(len(test_trials)))
print("congruent__SSS = " + str(congruent__SSS) + " / " + str(len(test_trials)))
print("congruent__SNN = " + str(congruent__SNN) + " / " + str(len(test_trials)))
print("congruent__DNN = " + str(congruent__DNN) + " / " + str(len(test_trials)))

print("incongruent__DDD = " + str(incongruent__DDD) + " / " + str(len(test_trials)))
print("incongruent__SDD = " + str(incongruent__SDD) + " / " + str(len(test_trials)))
print("incongruent__DSD = " + str(incongruent__DSD) + " / " + str(len(test_trials)))
print("incongruent__DDS = " + str(incongruent__DDS) + " / " + str(len(test_trials)))
print("incongruent__SSS = " + str(incongruent__SSS) + " / " + str(len(test_trials)))
print("incongruent__SNN = " + str(incongruent__SNN) + " / " + str(len(test_trials)))
print("incongruent__DNN = " + str(incongruent__DNN) + " / " + str(len(test_trials)))




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