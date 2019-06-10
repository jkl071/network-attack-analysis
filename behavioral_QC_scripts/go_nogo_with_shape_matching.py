#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:58:46 2018

@author: jamie

go_nogo_with_shape_matching

GNG: ['go','go','go','go','nogo']
Shape: ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

700 total trials, 140 per block, 5 blocks total
35 minimum trials
full counterbalancing
"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_output/final/A3NNB4LWIKA3BQ/modified_for_analysis/"
task = 'go_nogo_with_shape_matching_A3NNB4LWIKA3BQ.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

shape_matching_conditions = ['DDD','SDD','DSD','DDS','SSS','SNN','DNN']

gng_go__DDD = 0
gng_go__SDD = 0
gng_go__DSD = 0
gng_go__DDS = 0
gng_go__SSS = 0
gng_go__SNN = 0
gng_go__DNN = 0

gng_nogo__DDD = 0
gng_nogo__SDD = 0
gng_nogo__DSD = 0
gng_nogo__DDS = 0
gng_nogo__SSS = 0
gng_nogo__SNN = 0
gng_nogo__DNN = 0


for row in range(0,len(test_trials)):
    if test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__DNN += 1
        
        
    
    elif test_trials.iloc[row].shape_matching_condition == 'DDD' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__DDD += 1
    
    elif test_trials.iloc[row].shape_matching_condition == 'SDD' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__SDD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DSD' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__DSD += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DDS' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__DDS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SSS' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__SSS += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'SNN' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__SNN += 1
        
    elif test_trials.iloc[row].shape_matching_condition == 'DNN' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__DNN += 1
        

        
        
print("gng_go__DDD = " + str(gng_go__DDD) + " / " + str(len(test_trials)))
print("gng_go__SDD = " + str(gng_go__SDD) + " / " + str(len(test_trials)))
print("gng_go__DSD = " + str(gng_go__DSD) + " / " + str(len(test_trials)))
print("gng_go__DDS = " + str(gng_go__DDS) + " / " + str(len(test_trials)))
print("gng_go__SSS = " + str(gng_go__SSS) + " / " + str(len(test_trials)))
print("gng_go__SNN = " + str(gng_go__SNN) + " / " + str(len(test_trials)))
print("gng_go__DNN = " + str(gng_go__DNN) + " / " + str(len(test_trials)))


print("gng_nogo__DDD = " + str(gng_nogo__DDD) + " / " + str(len(test_trials)))
print("gng_nogo__SDD = " + str(gng_nogo__SDD) + " / " + str(len(test_trials)))
print("gng_nogo__DSD = " + str(gng_nogo__DSD) + " / " + str(len(test_trials)))
print("gng_nogo__DDS = " + str(gng_nogo__DDS) + " / " + str(len(test_trials)))
print("gng_nogo__SSS = " + str(gng_nogo__SSS) + " / " + str(len(test_trials)))
print("gng_nogo__SNN = " + str(gng_nogo__SNN) + " / " + str(len(test_trials)))
print("gng_nogo__DNN = " + str(gng_nogo__DNN) + " / " + str(len(test_trials)))



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