#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:36:25 2018

@author: jamie

stop signal single task network


12 total conditions
- 4 shapes by 3 SS type (go go stop)

144 total trials, 48/block, 3 blocks

full counterbalance
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_single_task_network_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

stop_signal_conditions = ['go','stop']
#shapes = circle, square, triangle, pentagon

go_shape1 = 0
go_shape2 = 0
go_shape3 = 0
go_shape4 = 0

stop_shape1 = 0
stop_shape2 = 0
stop_shape3 = 0
stop_shape4 = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].stop_signal_condition == 'go' and test_trials.iloc[row].stim == 'circle':
        go_shape1 += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'go' and test_trials.iloc[row].stim == 'pentagon':
        go_shape2 += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'go' and test_trials.iloc[row].stim == 'square':
        go_shape3 += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'go' and test_trials.iloc[row].stim == 'triangle':
        go_shape4 += 1
        
    
    elif test_trials.iloc[row].stop_signal_condition == 'stop' and test_trials.iloc[row].stim == 'circle':
        stop_shape1 += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'stop' and test_trials.iloc[row].stim == 'pentagon':
        stop_shape2 += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'stop' and test_trials.iloc[row].stim == 'square':
        stop_shape3 += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'stop' and test_trials.iloc[row].stim == 'triangle':
        stop_shape4 += 1
   
        
        

        
        
print("go_shape1 = " + str(go_shape1) + " / " + str(len(test_trials)))
print("go_shape2 = " + str(go_shape2) + " / " + str(len(test_trials)))
print("go_shape3 = " + str(go_shape3) + " / " + str(len(test_trials)))
print("go_shape4 = " + str(go_shape4) + " / " + str(len(test_trials)))


print("stop_shape1 = " + str(stop_shape1) + " / " + str(len(test_trials)))
print("stop_shape2 = " + str(stop_shape2) + " / " + str(len(test_trials)))
print("stop_shape3 = " + str(stop_shape3) + " / " + str(len(test_trials)))
print("stop_shape4 = " + str(stop_shape4) + " / " + str(len(test_trials)))




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