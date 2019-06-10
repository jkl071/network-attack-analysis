#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:07:55 2018

@author: jamie

stop_signal_with_shape_matching

SS: go, go, stop
Shape: ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

420 total trials, 84 per block, 5 blocks total
21 minimum trials
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'stop_signal_with_shape_matching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

SS_go__DDD = 0
SS_go__SDD = 0
SS_go__DSD = 0
SS_go__DDS = 0
SS_go__SSS = 0
SS_go__SNN = 0
SS_go__DNN = 0

SS_stop__DDD = 0
SS_stop__SDD = 0
SS_stop__DSD = 0
SS_stop__DDS = 0
SS_stop__SSS = 0
SS_stop__SNN = 0
SS_stop__DNN = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__DNN += 1
        
        
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__DNN += 1
        
        
        
        

        
        
print("SS_go__DDD = " + str(SS_go__DDD) + " / " + str(len(test_trials)))
print("SS_go__SDD = " + str(SS_go__SDD) + " / " + str(len(test_trials)))
print("SS_go__DSD = " + str(SS_go__DSD) + " / " + str(len(test_trials)))
print("SS_go__DDS = " + str(SS_go__DDS) + " / " + str(len(test_trials)))
print("SS_go__SSS = " + str(SS_go__SSS) + " / " + str(len(test_trials)))
print("SS_go__SNN = " + str(SS_go__SNN) + " / " + str(len(test_trials)))
print("SS_go__DNN = " + str(SS_go__DNN) + " / " + str(len(test_trials)))


print("SS_stop__DDD = " + str(SS_stop__DDD) + " / " + str(len(test_trials)))
print("SS_stop__SDD = " + str(SS_stop__SDD) + " / " + str(len(test_trials)))
print("SS_stop__DSD = " + str(SS_stop__DSD) + " / " + str(len(test_trials)))
print("SS_stop__DDS = " + str(SS_stop__DDS) + " / " + str(len(test_trials)))
print("SS_stop__SSS = " + str(SS_stop__SSS) + " / " + str(len(test_trials)))
print("SS_stop__SNN = " + str(SS_stop__SNN) + " / " + str(len(test_trials)))
print("SS_stop__DNN = " + str(SS_stop__DNN) + " / " + str(len(test_trials)))




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