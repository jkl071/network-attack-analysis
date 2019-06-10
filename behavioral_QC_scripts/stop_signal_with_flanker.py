#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:22:16 2018

@author: jamie

stop_signal_with_flanker

SS: go, go, stop
Flanker: ['H_congruent','H_incongruent','F_congruent','F_incongruent']

240 total trials, 48 trials per block, 5 blocks
12 minimum trials
full counterbalancing 
"""

import pandas as pd

input_path = "~/Desktop/network_tasks_output_files/stop_signal_with_flanker/"
input_path = "/Users/jamie/Desktop/network_output/final/A11S8IAAVDXCUS/modified_for_analysis/"
task = 'stop_signal_with_flanker_A11S8IAAVDXCUS.csv'

df = pd.read_csv(input_path + task) 

test_trials = df[(df.trial_id == "test_trial")] #practice_trial for practice
                 
SS_stop__H_congruent = 0
SS_stop__H_incongruent = 0
SS_stop__F_congruent = 0
SS_stop__F_incongruent = 0

SS_go__H_congruent = 0
SS_go__H_incongruent = 0
SS_go__F_congruent = 0
SS_go__F_incongruent = 0

for row in range(0,len(test_trials)):
    if test_trials.iloc[row].flanker_condition == "H_congruent" and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__H_congruent += 1
    elif test_trials.iloc[row].flanker_condition == "H_congruent" and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__H_congruent += 1
        
    elif test_trials.iloc[row].flanker_condition == "H_incongruent" and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__H_incongruent += 1
    elif test_trials.iloc[row].flanker_condition == "H_incongruent" and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__H_incongruent += 1
        
        
    elif test_trials.iloc[row].flanker_condition == "F_congruent" and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__F_congruent += 1
    elif test_trials.iloc[row].flanker_condition == "F_congruent" and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__F_congruent += 1
       
    elif test_trials.iloc[row].flanker_condition == "F_incongruent" and test_trials.iloc[row].stop_signal_condition == 'stop':
        SS_stop__F_incongruent += 1
    elif test_trials.iloc[row].flanker_condition == "F_incongruent" and test_trials.iloc[row].stop_signal_condition == 'go':
        SS_go__F_incongruent += 1
        
print("SS_stop__H_congruent = " + str(SS_stop__H_congruent) + " / " + str(len(test_trials)))
print("SS_stop__H_incongruent = " + str(SS_stop__H_incongruent) + " / " + str(len(test_trials))) 
print("SS_stop__F_congruent = " + str(SS_stop__F_congruent) + " / " + str(len(test_trials)))
print("SS_stop__F_incongruent = " + str(SS_stop__F_incongruent) + " / " + str(len(test_trials))) 

print("SS_go__H_congruent = " + str(SS_go__H_congruent) + " / " + str(len(test_trials)))
print("SS_go__H_incongruent = " + str(SS_go__H_incongruent) + " / " + str(len(test_trials))) 
print("SS_go__F_congruent = " + str(SS_go__F_congruent) + " / " + str(len(test_trials)))
print("SS_go__F_incongruent = " + str(SS_go__F_incongruent) + " / " + str(len(test_trials))) 
    

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