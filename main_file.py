import numpy as np
import matplotlib.pyplot as plt

import warnings
from outputs import outputs
from outputs import results
from intervals import intervals
from figures import figures
import random
warnings.filterwarnings("ignore")

Tmax = 100

# randomize parameters
num = 1000
betas = [1 / np.random.uniform(20, 30) for i in range(0, num)]
gammas = [1 / np.random.uniform(8, 12) for i in range(0, num)]
# randomize age group of the first infectious person
first_inf = [random.randint(0, 15) for i in range(0, num)]

# populate 16-compartment model for first infectious person
i_16s = []
for i in range(0, num):
    i_16_initial = []
    for k in range(0, 16):
        if k == first_inf[i]:
            i_16_initial.append(1)
        else:
            i_16_initial.append(0)
    i_16s.append(i_16_initial)

# populate 3-compartment models for first infectious person
i_3s = []
for i in range(0, num):
    i_3_initial = []
    if first_inf[i] < 4:
        first_inf_3 = 0
    elif first_inf[i] < 13:
        first_inf_3 = 1
    else:
        first_inf_3 = 2
    for k in range(0, 3):
        if k == first_inf_3:
            i_3_initial.append(1)
        else:
            i_3_initial.append(0)
    i_3s.append(i_3_initial)

# models, age groups, cum or not
models = ['prem',  "choi", "griette_hilton", "oraby", "rost", "yang", "new"]
ages = ['all', 'kid', 'adult', 'elderly']
cums = ['', 'cum']

# create empty lists to hold simulation results later
for model in models:
    for age in ages:
        for cum in cums:
            exec('I' + '_' + model + '_' + age + '_' + cum + '=[]')

# run model and insert simulation results into lists (1000 simulations separately)
for k in range(0, num):
    in_one_simulation = []
    beta = betas[k]
    gamma = gammas[k]
    i_16 = i_16s[k]
    i_3 = i_3s[k]
    for model in models:
        model_output = outputs(Tmax, beta, gamma).insert_output(model, i_16, i_3)
        for age in ages:
            for cum in cums:
                result = results(model_output).insert_results(age, cum)
                name = 'I' + '_' + model + '_' + age + '_' + cum
                exec(name + '.append(result)')


# getting the mean number after 1000 simulations, produce and save figures
figures(Tmax).tot(datas = [intervals(I_prem_all_).get()[0], intervals(I_choi_all_).get()[0], intervals(I_griette_hilton_all_).get()[0],
                           intervals(I_oraby_all_).get()[0],intervals(I_rost_all_).get()[0],intervals(I_yang_all_).get()[0],intervals(I_new_all_).get()[0],
                           intervals(I_prem_all_).get()[1], intervals(I_choi_all_).get()[1], intervals(I_griette_hilton_all_).get()[1],
                           intervals(I_oraby_all_).get()[1],intervals(I_rost_all_).get()[1],intervals(I_yang_all_).get()[1],intervals(I_new_all_).get()[1],
                           intervals(I_prem_all_).get()[2], intervals(I_choi_all_).get()[2], intervals(I_griette_hilton_all_).get()[2],
                           intervals(I_oraby_all_).get()[2],intervals(I_rost_all_).get()[2],intervals(I_yang_all_).get()[2],intervals(I_new_all_).get()[2]
                           ], title = 'Cases')

figures(Tmax).tot(datas = [intervals(I_prem_all_cum).get()[0], intervals(I_choi_all_cum).get()[0], intervals(I_griette_hilton_all_cum).get()[0],
                           intervals(I_oraby_all_cum).get()[0], intervals(I_rost_all_cum).get()[0], intervals(I_yang_all_cum).get()[0], intervals(I_new_all_cum).get()[0],
                           intervals(I_prem_all_cum).get()[1], intervals(I_choi_all_cum).get()[1], intervals(I_griette_hilton_all_cum).get()[1],
                           intervals(I_oraby_all_cum).get()[1], intervals(I_rost_all_cum).get()[1], intervals(I_yang_all_cum).get()[1], intervals(I_new_all_cum).get()[1],
                           intervals(I_prem_all_cum).get()[2], intervals(I_choi_all_cum).get()[2], intervals(I_griette_hilton_all_cum).get()[2],
                           intervals(I_oraby_all_cum).get()[2], intervals(I_rost_all_cum).get()[2], intervals(I_yang_all_cum).get()[2],intervals(I_new_all_cum).get()[2]
                           ], title = 'Cumulative Cases')


figures(Tmax).age(datas = [intervals(I_prem_kid_).get()[0], intervals(I_choi_kid_).get()[0], intervals(I_griette_hilton_kid_).get()[0],
                           intervals(I_oraby_kid_).get()[0],intervals(I_rost_kid_).get()[0],intervals(I_yang_kid_).get()[0],intervals(I_new_kid_).get()[0],
                           intervals(I_prem_adult_).get()[0], intervals(I_choi_adult_).get()[0], intervals(I_griette_hilton_adult_).get()[0],
                           intervals(I_oraby_adult_).get()[0],intervals(I_rost_adult_).get()[0],intervals(I_yang_adult_).get()[0],intervals(I_new_adult_).get()[0],
                           intervals(I_prem_elderly_).get()[0], intervals(I_choi_elderly_).get()[0], intervals(I_griette_hilton_elderly_).get()[0],
                           intervals(I_oraby_elderly_).get()[0],intervals(I_rost_elderly_).get()[0],intervals(I_yang_elderly_).get()[0],intervals(I_new_elderly_).get()[0]
                           ],  title = 'Cases by Age')
figures(Tmax).age(datas = [intervals(I_prem_kid_cum).get()[0], intervals(I_choi_kid_cum).get()[0], intervals(I_griette_hilton_kid_cum).get()[0],
                           intervals(I_oraby_kid_cum).get()[0],intervals(I_rost_kid_cum).get()[0],intervals(I_yang_kid_cum).get()[0],intervals(I_new_kid_cum).get()[0],
                           intervals(I_prem_adult_cum).get()[0], intervals(I_choi_adult_cum).get()[0], intervals(I_griette_hilton_adult_cum).get()[0],
                           intervals(I_oraby_adult_cum).get()[0],intervals(I_rost_adult_cum).get()[0],intervals(I_yang_adult_cum).get()[0],intervals(I_new_adult_cum).get()[0],
                           intervals(I_prem_elderly_cum).get()[0], intervals(I_choi_elderly_cum).get()[0], intervals(I_griette_hilton_elderly_cum).get()[0],
                           intervals(I_oraby_elderly_cum).get()[0],intervals(I_rost_elderly_cum).get()[0],intervals(I_yang_elderly_cum).get()[0],intervals(I_new_elderly_cum).get()[0]
                           ], title = 'Cumulative Cases by Age')


figures(Tmax).age(datas = [np.array(intervals(I_prem_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),
                           np.array(intervals(I_choi_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),
                           np.array(intervals(I_griette_hilton_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),
                           np.array(intervals(I_oraby_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),
                           np.array(intervals(I_rost_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),
                           np.array(intervals(I_yang_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),
                           np.array(intervals(I_new_kid_).get()[0]) - np.array(intervals(I_prem_kid_).get()[0]),

                           np.array(intervals(I_prem_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),
                           np.array(intervals(I_choi_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),
                           np.array(intervals(I_griette_hilton_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),
                           np.array(intervals(I_oraby_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),
                           np.array(intervals(I_rost_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),
                           np.array(intervals(I_yang_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),
                           np.array(intervals(I_new_adult_).get()[0]) - np.array(intervals(I_prem_adult_).get()[0]),

                           np.array(intervals(I_prem_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0]),
                           np.array(intervals(I_choi_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0]),
                           np.array(intervals(I_griette_hilton_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0]),
                           np.array(intervals(I_oraby_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0]),
                           np.array(intervals(I_rost_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0]),
                           np.array(intervals(I_yang_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0]),
                           np.array(intervals(I_new_elderly_).get()[0]) - np.array(intervals(I_prem_elderly_).get()[0])
                           ],  title = 'Errors by Age')


figures(Tmax).err(datas = [np.array(intervals(I_prem_all_).get()[0])-np.array(intervals(I_prem_all_).get()[0]),
                           np.array(intervals(I_choi_all_).get()[0])-np.array(intervals(I_prem_all_).get()[0]),
                           np.array(intervals(I_griette_hilton_all_).get()[0])-np.array(intervals(I_prem_all_).get()[0]),
                           np.array(intervals(I_oraby_all_).get()[0])-np.array(intervals(I_prem_all_).get()[0]),
                           np.array(intervals(I_rost_all_).get()[0])-np.array(intervals(I_prem_all_).get()[0]),
                           np.array(intervals(I_yang_all_).get()[0])-np.array(intervals(I_prem_all_).get()[0]),
                           np.array(intervals(I_new_all_).get()[0]) - np.array(intervals(I_prem_all_).get()[0]),

                           np.array(intervals(I_choi_all_).get()[1])-np.array(intervals(I_prem_all_).get()[1]),
                           np.array(intervals(I_griette_hilton_all_).get()[1])-np.array(intervals(I_prem_all_).get()[1]),
                           np.array(intervals(I_oraby_all_).get()[1])-np.array(intervals(I_prem_all_).get()[1]),
                           np.array(intervals(I_rost_all_).get()[1])-np.array(intervals(I_prem_all_).get()[1]),
                           np.array(intervals(I_yang_all_).get()[1])-np.array(intervals(I_prem_all_).get()[1]),
                           np.array(intervals(I_new_all_).get()[1]) - np.array(intervals(I_prem_all_).get()[1]),

                           np.array(intervals(I_choi_all_).get()[2])-np.array(intervals(I_prem_all_).get()[2]),
                           np.array(intervals(I_griette_hilton_all_).get()[2])-np.array(intervals(I_prem_all_).get()[2]),
                           np.array(intervals(I_oraby_all_).get()[2])-np.array(intervals(I_prem_all_).get()[2]),
                           np.array(intervals(I_rost_all_).get()[2])-np.array(intervals(I_prem_all_).get()[2]),
                           np.array(intervals(I_yang_all_).get()[2])-np.array(intervals(I_prem_all_).get()[2]),
                           np.array(intervals(I_new_all_).get()[2]) - np.array(intervals(I_prem_all_).get()[2])
                           ], title = 'Errors')

figures(Tmax).err(datas = [np.array(intervals(I_prem_all_cum).get()[0])-np.array(intervals(I_prem_all_cum).get()[0]),
                           np.array(intervals(I_choi_all_cum).get()[0])-np.array(intervals(I_prem_all_cum).get()[0]),
                           np.array(intervals(I_griette_hilton_all_cum).get()[0])-np.array(intervals(I_prem_all_cum).get()[0]),
                           np.array(intervals(I_oraby_all_cum).get()[0])-np.array(intervals(I_prem_all_cum).get()[0]),
                           np.array(intervals(I_rost_all_cum).get()[0])-np.array(intervals(I_prem_all_cum).get()[0]),
                           np.array(intervals(I_yang_all_cum).get()[0])-np.array(intervals(I_prem_all_cum).get()[0]),
                           np.array(intervals(I_new_all_cum).get()[0]) - np.array(intervals(I_prem_all_cum).get()[0]),

                           np.array(intervals(I_choi_all_cum).get()[1])-np.array(intervals(I_prem_all_cum).get()[1]),
                           np.array(intervals(I_griette_hilton_all_cum).get()[1])-np.array(intervals(I_prem_all_cum).get()[1]),
                           np.array(intervals(I_oraby_all_cum).get()[1])-np.array(intervals(I_prem_all_cum).get()[1]),
                           np.array(intervals(I_rost_all_cum).get()[1])-np.array(intervals(I_prem_all_cum).get()[1]),
                           np.array(intervals(I_yang_all_cum).get()[1])-np.array(intervals(I_prem_all_cum).get()[1]),
                           np.array(intervals(I_new_all_cum).get()[1]) - np.array(intervals(I_prem_all_cum).get()[1]),

                           np.array(intervals(I_choi_all_cum).get()[2])-np.array(intervals(I_prem_all_cum).get()[2]),
                           np.array(intervals(I_griette_hilton_all_cum).get()[2])-np.array(intervals(I_prem_all_cum).get()[2]),
                           np.array(intervals(I_oraby_all_cum).get()[2])-np.array(intervals(I_prem_all_cum).get()[2]),
                           np.array(intervals(I_rost_all_cum).get()[2])-np.array(intervals(I_prem_all_cum).get()[2]),
                           np.array(intervals(I_yang_all_cum).get()[2])-np.array(intervals(I_prem_all_cum).get()[2]),
                           np.array(intervals(I_new_all_cum).get()[2]) - np.array(intervals(I_prem_all_cum).get()[2])
                           ], title = 'Cumulative Errors')

figures(Tmax).age(datas = [np.array(intervals(I_prem_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),
                           np.array(intervals(I_choi_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),
                           np.array(intervals(I_griette_hilton_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),
                           np.array(intervals(I_oraby_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),
                           np.array(intervals(I_rost_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),
                           np.array(intervals(I_yang_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),
                           np.array(intervals(I_new_kid_cum).get()[0]) - np.array(intervals(I_prem_kid_cum).get()[0]),

                           np.array(intervals(I_prem_adult_cum).get()[0]) -  np.array(intervals(I_prem_adult_cum).get()[0]),
                           np.array(intervals(I_choi_adult_cum).get()[0]) -  np.array(intervals(I_prem_adult_cum).get()[0]),
                           np.array(intervals(I_griette_hilton_adult_cum).get()[0]) -  np.array(intervals(I_prem_adult_cum).get()[0]),
                           np.array( intervals(I_oraby_adult_cum).get()[0]) -  np.array(intervals(I_prem_adult_cum).get()[0]),
                           np.array(intervals(I_rost_adult_cum).get()[0]) -  np.array(intervals(I_prem_adult_cum).get()[0]),
                           np.array(intervals(I_yang_adult_cum).get()[0]) -  np.array(intervals(I_prem_adult_cum).get()[0]),
                           np.array(intervals(I_new_adult_cum).get()[0]) - np.array( intervals(I_prem_adult_cum).get()[0]),

                           np.array(intervals(I_prem_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0]),
                           np.array(intervals(I_choi_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0]),
                           np.array(intervals(I_griette_hilton_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0]),
                           np.array(intervals(I_oraby_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0]),
                           np.array(intervals(I_rost_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0]),
                           np.array(intervals(I_yang_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0]),
                           np.array(intervals(I_new_elderly_cum).get()[0]) - np.array(intervals(I_prem_elderly_cum).get()[0])
                           ], title = 'Cumulative Errors by Age')















