#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:21:14 2018

@author: jamie

go_nogo_with_flanker

GNG: ['go','go','go','go','stop']
Flanker: ['H_congruent','H_incongruent','F_congruent','F_incongruent']

20 minimum trials
240 total trials, 60 per block, 4 blocks total
full counterbalancing

"""

import pandas as pd

input_path = "/Users/jamie/Desktop/network_tasks_output_files/go_nogo_with_flanker/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'go_nogo_with_flanker_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice

gng_go__F_congruent = 0
gng_go__H_congruent = 0
gng_go__F_incongruent = 0
gng_go__H_incongruent = 0


gng_nogo__F_congruent = 0
gng_nogo__H_congruent = 0
gng_nogo__F_incongruent= 0
gng_nogo__H_incongruent = 0



for row in range(0,len(test_trials)):
    if test_trials.iloc[row].flanker_condition == 'F_congruent' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__F_congruent += 1
    
    elif test_trials.iloc[row].flanker_condition == 'H_congruent' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__H_congruent += 1
        
    elif test_trials.iloc[row].flanker_condition == 'F_incongruent' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__F_incongruent += 1
        
    elif test_trials.iloc[row].flanker_condition == 'H_incongruent' and test_trials.iloc[row].go_nogo_condition == 'go':
        gng_go__H_incongruent += 1
        
        
        
    
    elif test_trials.iloc[row].flanker_condition == 'F_congruent' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__F_congruent += 1
    
    elif test_trials.iloc[row].flanker_condition == 'H_congruent' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__H_congruent += 1
        
    elif test_trials.iloc[row].flanker_condition == 'F_incongruent' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__F_incongruent += 1
        
    elif test_trials.iloc[row].flanker_condition == 'H_incongruent' and test_trials.iloc[row].go_nogo_condition == 'nogo':
        gng_nogo__H_incongruent += 1
        
        

        
        
print("gng_go__F_congruent = " + str(gng_go__F_congruent) + " / " + str(len(test_trials)))
print("gng_go__H_congruent = " + str(gng_go__H_congruent) + " / " + str(len(test_trials)))
print("gng_go__F_incongruent = " + str(gng_go__F_incongruent) + " / " + str(len(test_trials)))
print("gng_go__H_incongruent = " + str(gng_go__H_incongruent) + " / " + str(len(test_trials)))



print("gng_nogo__F_congruent = " + str(gng_nogo__F_congruent) + " / " + str(len(test_trials)))
print("gng_nogo__H_congruent = " + str(gng_nogo__H_congruent) + " / " + str(len(test_trials)))
print("gng_nogo__F_incongruent = " + str(gng_nogo__F_incongruent) + " / " + str(len(test_trials)))
print("gng_nogo__H_incongruent = " + str(gng_nogo__H_incongruent) + " / " + str(len(test_trials)))




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
