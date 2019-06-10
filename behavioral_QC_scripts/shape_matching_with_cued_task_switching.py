#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:41:31 2018

@author: jamie

shape_matching_with_two_by_two
shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']
task_conditions = switch vs stay
cue_conditions = switch vs stay


5 blocks of 112 trials, 560 total.  
lowest counterbalance = 28
full counterbalancing


"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'shape_matching_with_cued_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

task_stay__cue_stay_DDD = 0
task_stay__cue_stay_SDD = 0
task_stay__cue_stay_DSD = 0
task_stay__cue_stay_DDS = 0
task_stay__cue_stay_SSS = 0
task_stay__cue_stay_SNN = 0
task_stay__cue_stay_DNN = 0


task_stay__cue_switch_DDD = 0
task_stay__cue_switch_SDD = 0
task_stay__cue_switch_DSD = 0
task_stay__cue_switch_DDS = 0
task_stay__cue_switch_SSS = 0
task_stay__cue_switch_SNN = 0
task_stay__cue_switch_DNN = 0

task_switch__cue_stay_DDD = 0
task_switch__cue_stay_SDD = 0
task_switch__cue_stay_DSD = 0
task_switch__cue_stay_DDS = 0
task_switch__cue_stay_SSS = 0
task_switch__cue_stay_SNN = 0
task_switch__cue_stay_DNN = 0

task_switch__cue_switch_DDD = 0
task_switch__cue_switch_SDD = 0
task_switch__cue_switch_DSD = 0
task_switch__cue_switch_DDS = 0
task_switch__cue_switch_SSS = 0
task_switch__cue_switch_SNN = 0
task_switch__cue_switch_DNN = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DDD':
        task_stay__cue_stay_DDD += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'SDD':
        task_stay__cue_stay_SDD += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DSD':
        task_stay__cue_stay_DSD += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DDS':
        task_stay__cue_stay_DDS += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'SSS':
        task_stay__cue_stay_SSS += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'SNN':
        task_stay__cue_stay_SNN += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DNN':
        task_stay__cue_stay_DNN += 1
        
        
        
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DDD':
        task_stay__cue_switch_DDD += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'SDD':
        task_stay__cue_switch_SDD += 1
    
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DSD':
        task_stay__cue_switch_DSD += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DDS':
        task_stay__cue_switch_DDS += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'SSS':
        task_stay__cue_switch_SSS += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'SNN':
        task_stay__cue_switch_SNN += 1
        
    elif test_trials.iloc[row].task_condition == "stay" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DNN':
        task_stay__cue_switch_DNN += 1
        
        
        
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DDD':
        task_switch__cue_stay_DDD += 1
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'SDD':
        task_switch__cue_stay_SDD += 1
        
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DSD':
        task_switch__cue_stay_DSD += 1
        
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DDS':
        task_switch__cue_stay_DDS += 1
        
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'SSS':
        task_switch__cue_stay_SSS += 1
        
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'SNN':
        task_switch__cue_stay_SNN += 1
        
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "stay" and test_trials.iloc[row].shape_matching_condition == 'DNN':
        task_switch__cue_stay_DNN += 1
              
              
        
    
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DDD':
        task_switch__cue_switch_DDD += 1
        
    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'SDD':
        task_switch__cue_switch_SDD += 1

    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DSD':
        task_switch__cue_switch_DSD += 1

    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DDS':
        task_switch__cue_switch_DDS += 1

    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'SSS':
        task_switch__cue_switch_SSS += 1

    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'SNN':
        task_switch__cue_switch_SNN += 1

    elif test_trials.iloc[row].task_condition == "switch_new" and test_trials.iloc[row].cue_condition == "switch" and test_trials.iloc[row].shape_matching_condition == 'DNN':
        task_switch__cue_switch_DNN += 1


        
        
print("task_stay__cue_stay_DDD = " + str(task_stay__cue_stay_DDD) + " / " + str(len(test_trials)))
print("task_stay__cue_stay_SDD = " + str(task_stay__cue_stay_SDD) + " / " + str(len(test_trials)))
print("task_stay__cue_stay_DSD = " + str(task_stay__cue_stay_DSD) + " / " + str(len(test_trials)))
print("task_stay__cue_stay_DDS = " + str(task_stay__cue_stay_DDS) + " / " + str(len(test_trials)))
print("task_stay__cue_stay_SSS = " + str(task_stay__cue_stay_SSS) + " / " + str(len(test_trials)))
print("task_stay__cue_stay_SNN = " + str(task_stay__cue_stay_SNN) + " / " + str(len(test_trials)))
print("task_stay__cue_stay_DNN = " + str(task_stay__cue_stay_DNN) + " / " + str(len(test_trials)))


print("task_stay__cue_switch_DDD = " + str(task_stay__cue_switch_DDD) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch_SDD = " + str(task_stay__cue_switch_SDD) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch_DSD = " + str(task_stay__cue_switch_DSD) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch_DDS = " + str(task_stay__cue_switch_DDS) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch_SSS = " + str(task_stay__cue_switch_SSS) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch_SNN = " + str(task_stay__cue_switch_SNN) + " / " + str(len(test_trials))) 
print("task_stay__cue_switch_DNN = " + str(task_stay__cue_switch_DNN) + " / " + str(len(test_trials))) 


print("task_switch__cue_stay_DDD = " + str(task_switch__cue_stay_DDD) + " / " + str(len(test_trials)))
print("task_switch__cue_stay_SDD = " + str(task_switch__cue_stay_SDD) + " / " + str(len(test_trials)))
print("task_switch__cue_stay_DSD = " + str(task_switch__cue_stay_DSD) + " / " + str(len(test_trials)))
print("task_switch__cue_stay_DDS = " + str(task_switch__cue_stay_DDS) + " / " + str(len(test_trials)))
print("task_switch__cue_stay_SSS = " + str(task_switch__cue_stay_SSS) + " / " + str(len(test_trials)))
print("task_switch__cue_stay_SNN = " + str(task_switch__cue_stay_SNN) + " / " + str(len(test_trials)))
print("task_switch__cue_stay_DNN = " + str(task_switch__cue_stay_DNN) + " / " + str(len(test_trials)))


print("task_switch__cue_switch_DDD = " + str(task_switch__cue_switch_DDD) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch_SDD = " + str(task_switch__cue_switch_SDD) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch_DSD = " + str(task_switch__cue_switch_DSD) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch_DDS = " + str(task_switch__cue_switch_DDS) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch_SSS = " + str(task_switch__cue_switch_SSS) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch_SNN = " + str(task_switch__cue_switch_SNN) + " / " + str(len(test_trials))) 
print("task_switch__cue_switch_DNN = " + str(task_switch__cue_switch_DNN) + " / " + str(len(test_trials))) 


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