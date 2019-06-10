#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:47:18 2018

@author: jamie

stop_signal_with_predictable_task_switching

SS: go, go, stop
Predictive: 2 (switch or stay) by 2 (mag or parity)

240 trials tota, 48 trials per block, 5 blocks
12 minimum trials
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_with_predictable_task_switching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_with_stop for practice

stop_signal_conditions = ['go','stop']
#shapes = circle, square, triangle, pentagon

go_stay = 0
go_switch = 0

stop_stay = 0
stop_switch = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].stop_signal_condition == 'go' and test_trials.iloc[row].predictive_condition == 'stay':
        go_stay += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'go' and test_trials.iloc[row].predictive_condition == 'switch':
        go_switch += 1
        
        
    
    elif test_trials.iloc[row].stop_signal_condition == 'stop' and test_trials.iloc[row].predictive_condition == 'stay':
        stop_stay += 1
        
    elif test_trials.iloc[row].stop_signal_condition == 'stop' and test_trials.iloc[row].predictive_condition == 'switch':
        stop_switch += 1
        
  
   
        
        

        
        
print("go_stay = " + str(go_stay) + " / " + str(len(test_trials)))
print("go_switch = " + str(go_switch) + " / " + str(len(test_trials)))

print("stop_stay = " + str(stop_stay) + " / " + str(len(test_trials)))
print("stop_switch = " + str(stop_switch) + " / " + str(len(test_trials)))





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



