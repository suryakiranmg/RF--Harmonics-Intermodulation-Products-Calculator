'''
Author: Suryakiran Menachery George
Date: March-19-2018
Purpose: EE 544 Mini Project, Harmonics & Inter-modulation Products Calculator
'''

import sys

print('\033[1;34mEnter the first frequency in MHz\033[1;m')
val1 = sys.stdin.readline()
print('\033[1;34mEnter the second frequency in MHz\033[1;m')
val2 = sys.stdin.readline()
print('\033[1;34mEnter the third frequency in MHz\033[1;m')
val3 = sys.stdin.readline()
print('\033[1;34mEnter the desired frequency(for hit calculation) MHz\033[1;m')
val4 = sys.stdin.readline()

print("\033[1;31mHarmonics & IM Components for each Non-Linearity\033[1;m")

f1 = int(val1)
f2 = int(val2)
f3 = int(val3)
des_freq = int(val4)
IM_freq_list = []
IM_freq_list_2nd = []
IM_freq_list_3rd = []
IM_freq_list_4th = []
IM_freq_list_5th = []
IM_freq_list_6th = []
IM_freq_list_7th = []
Total_hits = 0
Har_hits = 0
print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")
'''---------------------------------------------------------------'''
''' 2nd Order Harmonics & Inter-modulation Components'''
hit_count = 0
# 2nd Harmonics
Har_freq_list_2nd = [2 * f1, 2 * f2, 2 * f3]
print("\033[1;33mThe 2nd Order Harmonic Freqs:\033[1;m", Har_freq_list_2nd)
for x in range(0, 3):
   if((Har_freq_list_2nd[x]) == des_freq):
       Har_hits += 1


# 2nd IM
print("\033[1;33mThe 2nd Order Inter-modulation Components:\033[1;m")
from itertools import permutations

list_1 = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
list_2 = [(-1, -1, 0), (-1, 0, -1), (0, -1, -1)]
list_3 = list(permutations([-1, 1, 0]))

IM2_order_list = list_1 + list_2 + list_3

for x in range(0, len(IM2_order_list)):
    m = IM2_order_list[x][0]
    n = IM2_order_list[x][1]
    k = IM2_order_list[x][2]
    Sum_Val = m * f1 + n * f2 + k * f3
    if abs(Sum_Val) == des_freq:
        hit_count += 1
        print("(m,n,k):", m, n, k)
    IM_freq_list_2nd.append(Sum_Val)

print("\033[1;34m\nNo of hits :\033[1;m", hit_count)
Total_hits += hit_count
# avoid -ve freqs
IM_freq_list_2nd = [abs(x) for x in IM_freq_list_2nd]
# convert to set to eliminate repeat values
IM_freq_set = set(IM_freq_list_2nd)
IM_freq_list_2nd = list(IM_freq_set)
IM_freq_list_2nd.sort()
print('\n',IM_freq_list_2nd)

print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")
'''---------------------------------------------------------------'''
''' 3rd Order Harmonics & Inter-modulation Components'''
# 3rd Harmonics
Har_freq_list_3rd = [3 * f1, 3 * f2, 3 * f3]
print("\033[1;33mThe 3rd Order Harmonic Freqs:\033[1;m", Har_freq_list_3rd)
for x in range(0, 3):
   if Har_freq_list_3rd[x] == des_freq:
       Har_hits += 1

# 3rd IM
print("\033[1;33mThe 3rd Order  Inter-modulation Components:\033[1;m")
hit_count = 0

list_1 = [(1, 1, 1),(-1,-1,-1)]
list_2 = [(-1, 1, 1), (1, -1, 1), (1, 1, -1)] + [(-1, -1, 1), (1, -1, -1), (-1, 1, -1)]

list_3 = list(permutations([-2, 1, 0])) + list(permutations([2, -1, 0]))
list_4 = list(permutations([2, 1, 0])) + list(permutations([-2, -1, 0]))

IM2_order_list = list_1 + list_2 + list_3 + list_4

for x in range(0, len(IM2_order_list)):
    m = IM2_order_list[x][0]
    n = IM2_order_list[x][1]
    k = IM2_order_list[x][2]
    Sum_Val = m * f1 + n * f2 + k * f3
    if abs(Sum_Val) == des_freq:
        hit_count += 1
        print("(m,n,k):", m, n, k)

    IM_freq_list_3rd.append(Sum_Val)

print("\033[1;34m\nNo of hits :\033[1;m", hit_count)
Total_hits += hit_count
# avoid -ve freqs
IM_freq_list_3rd = [abs(x) for x in IM_freq_list_3rd]
# convert to set to eliminate repeat values
IM_freq_set = set(IM_freq_list_3rd)
IM_freq_list_3rd = list(IM_freq_set)
IM_freq_list_3rd.sort()
print('\n',IM_freq_list_3rd)

print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")
'''---------------------------------------------------------------'''
''' 4th Order Harmonics & Inter-modulation Components'''
# 4th Harmonics
Har_freq_list_4th = [4 * f1, 4 * f2, 4 * f3]
print("\033[1;33mThe 4th Order Harmonic Freqs:\033[1;m", Har_freq_list_4th)
for x in range(0, 3):
   if((Har_freq_list_4th[x]) == des_freq):
       Har_hits += 1
       #print(Har_hits)

# 4th IM
print("\033[1;33mThe 4th Order Inter-modulation Components:\033[1;m")
hit_count = 0

list_1 = list(permutations([3, 1, 0])) + list(permutations([-3, -1, 0]))
list_2 = list(permutations([-3, 1, 0])) + list(permutations([3, -1, 0]))

list_3 = [(2, 2, 0), (2, 0, 2), (0, 2, 2)] + [(-2, -2, 0), (-2, 0, -2), (0, -2, -2)]
list_4 = list(permutations([-2, 2, 0]))

list_5 = [(2, 1, 1), (1, 2, 1), (1, 1, 2)] + [(-2, -1, -1), (-1, -2, -1), (-1, -1, -2)]
list_6 = [(-2, 1, 1), (1, -2, 1), (1, 1, -2)] + [(2, -1, -1), (-1, 2, -1), (-1, -1, 2)]
list_7 = list(permutations([2, -1, 1])) + list(permutations([-2, -1, 1]))


IM2_order_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7

for x in range(0, len(IM2_order_list)):
    m = IM2_order_list[x][0]
    n = IM2_order_list[x][1]
    k = IM2_order_list[x][2]
    Sum_Val = m * f1 + n * f2 + k * f3
    if (abs(Sum_Val) == des_freq):
        hit_count += 1
        print("(m,n,k):", m, n, k)

    IM_freq_list_4th.append(Sum_Val)

print("\033[1;34m\nNo of hits :\033[1;m", hit_count)
Total_hits += hit_count
# avoid -ve freqs
IM_freq_list_4th = [abs(x) for x in IM_freq_list_4th]
# convert to set to eliminate repeat values
IM_freq_set = set(IM_freq_list_4th)
IM_freq_list_4th = list(IM_freq_set)
IM_freq_list_4th.sort()
print('\n',IM_freq_list_4th)

print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")
'''---------------------------------------------------------------'''
''' 5th Order Harmonics & Inter-modulation Components'''
# 5th Harmonics
Har_freq_list_5th = [5 * f1, 5 * f2, 5 * f3]
print("\033[1;33mThe 5th Order Harmonic Freqs:\033[1;m", Har_freq_list_5th)
for x in range(0, 3):
   if((Har_freq_list_5th[x]) == des_freq):
       Har_hits += 1
       #print(Har_hits)

# 5th IM
print("\033[1;33mThe 5th Order Inter-modulation Components:\033[1;m")
hit_count = 0
list_1 = list(permutations([4, 1, 0])) + list(permutations([-4, -1, 0]))
list_2 = list(permutations([4, -1, 0])) + list(permutations([-4, 1, 0]))
list_3 = list(permutations([3, 2, 0])) + list(permutations([-3, -2, 0]))
list_4 = list(permutations([-3, 2, 0])) + list(permutations([3, -2, 0]))

list_5 = [(3, 1, 1),(1, 3, 1), (1, 1, 3)] + [(-3, -1, -1),(-1, -3, -1), (-1, -1, -3)]
list_6 = [(-3, 1, 1), (1, -3, 1), (1, 1, -3)] + [(3, -1, -1), (-1, 3, -1), (-1, -1, 3)]
list_7 = list(permutations([3, -1, 1])) + list(permutations([-3, -1, 1]))

list_8 = [(2, 2, 1), (2, 1, 2), (1, 2, 2)] + [(-2, -2, -1), (-2, -1, -2), (-1, -2, -2)]
list_9 = list(permutations([-2, 2, 1])) + list(permutations([-2, 2, -1]))
list_10 = [(-2, -2, 1), (-2, 1, -2), (1, -2, -2)] + [(2, 2, -1), (2, -1, 2), (-1, 2, 2)]


IM2_order_list = list_1 + list_2 + list_3 + list_4 + list_5 + \
                 list_6 + list_7 + list_8 + list_9 + list_10

for x in range(0, len(IM2_order_list)):
    m = IM2_order_list[x][0]
    n = IM2_order_list[x][1]
    k = IM2_order_list[x][2]
    Sum_Val = m * f1 + n * f2 + k * f3
    if abs(Sum_Val) == des_freq:
        hit_count += 1
        print("(m,n,k):", m, n, k)

    IM_freq_list_5th.append(Sum_Val)

print("\033[1;34m\nNo of hits :\033[1;m", hit_count)
Total_hits += hit_count
# avoid -ve freqs
IM_freq_list_5th = [abs(x) for x in IM_freq_list_5th]
# convert to set to eliminate repeat values
IM_freq_set = set(IM_freq_list_5th)
IM_freq_list_5th = list(IM_freq_set)
IM_freq_list_5th.sort()
print('\n',IM_freq_list_5th)


print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")

'''---------------------------------------------------------------'''
''' 6th Order Harmonics & Inter-modulation Components'''
# 6th Harmonics
Har_freq_list_6th = [6 * f1, 6 * f2, 6 * f3]
print("\033[1;33mThe 6th Order Harmonic Freqs:\033[1;m", Har_freq_list_6th)
for x in range(0, 3):
   if((Har_freq_list_6th[x]) == des_freq):
       Har_hits += 1
       #print(Har_hits)

# 6th IM
print("\033[1;33mThe 6th Order Inter-modulation Components:\033[1;m")
hit_count = 0
list_1 = list(permutations([5, 1, 0])) + list(permutations([-5, -1, 0]))
list_2 = list(permutations([-5, 1, 0])) + list(permutations([5, -1, 0]))

list_3 = list(permutations([4, 2, 0])) + list(permutations([-4, -2, 0]))
list_4 = list(permutations([-4, 2, 0])) + list(permutations([4, -2, 0]))

list_5 = [(3, 3, 0), (3, 0, 3), (0, 3, 3)] + [(-3, -3, 0), (-3, 0, -3), (0, -3, -3)]
list_6 = list(permutations([-3, 3, 0]))

list_7 = list(permutations([3, 2, 1])) + list(permutations([-3, -2, -1]))
list_8 = list(permutations([3, -2, 1])) + list(permutations([-3, 2, -1]))
list_9 = list(permutations([-3, 2, 1])) + list(permutations([3, -2, -1]))
list_10 = list(permutations([3, 2, -1])) + list(permutations([-3, -2, 1]))


list_11 = [(4, 1, 1), (1, 4, 1), (1, 1, 4)] + [(-4, -1, -1), (-1, -4, -1), (-1, -1, -4)]
list_12 = list(permutations([4, -1, 1])) + list(permutations([-4, -1, 1]))
list_13 = [(-4, 1, 1), (1, -4, 1), (1, 1, -4)] + [(4, -1, -1), (-1, 4, -1), (-1, -1, 4)]


IM2_order_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + \
                 list_8 + list_9 + list_10 + list_11 + list_12 + list_13
for x in range(0, len(IM2_order_list)):
    m = IM2_order_list[x][0]
    n = IM2_order_list[x][1]
    k = IM2_order_list[x][2]
    Sum_Val = m * f1 + n * f2 + k * f3
    if (abs(Sum_Val) == des_freq):
        hit_count += 1
        print("(m,n,k):", m, n, k)

    IM_freq_list_6th.append(Sum_Val)

print("\033[1;34m\nNo of hits :\033[1;m", hit_count)
Total_hits += hit_count
# avoid -ve freqs
IM_freq_list_6th = [abs(x) for x in IM_freq_list_6th]
# convert to set to eliminate repeat values
IM_freq_set = set(IM_freq_list_6th)
IM_freq_list_6th = list(IM_freq_set)
IM_freq_list_6th.sort()
print('\n',IM_freq_list_6th)

print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")
'''---------------------------------------------------------------'''
''' 7th Order Harmonics & Inter-modulation Components'''
# 7th Harmonics
Har_freq_list_7th = [7 * f1, 7 * f2, 7 * f3]
print("\033[1;33mThe 7th Order Harmonic Freqs:\033[1;m", Har_freq_list_7th)
for x in range(0, 3):
   if((Har_freq_list_7th[x]) == des_freq):
       Har_hits += 1
       #print(Har_hits)

# 7th IM
print("\033[1;33mThe 7th Order Inter-modulation Components:\033[1;m")
hit_count = 0
list_1 = list(permutations([6, 1, 0])) + list(permutations([-6, -1, 0]))
list_2 = list(permutations([-6, 1, 0])) + list(permutations([6, -1, 0]))

list_3 = list(permutations([5, 2, 0])) + list(permutations([-5, -2, 0]))
list_4 = list(permutations([-5, 2, 0])) + list(permutations([5, -2, 0]))

list_5 = list(permutations([4, 3, 0])) + list(permutations([-4, -3, 0]))
list_6 = list(permutations([-4, 3, 0])) + list(permutations([4, -3, 0]))

list_7 = [(3, 3, 1), (3, 1, 3), (1, 3, 3)] + [(-3, -3, -1), (-3, -1, -3), (-1, -3, -3)]
list_8 = list(permutations([3, -3, 1])) + list(permutations([3, -3, -1]))
list_9 = [(3, 3, -1), (3, -1, 3), (-1, 3, 3)] + [(-3, -3, 1), (-3, 1, -3), (1, -3, -3)]

list_10 = list(permutations([4, 2, 1])) + list(permutations([-4, -2, -1]))
list_11 = list(permutations([-4, 2, 1])) + list(permutations([4, -2, -1]))
list_12 = list(permutations([4, -2, 1])) + list(permutations([-4, 2, -1]))
list_13 = list(permutations([4, 2, -1])) + list(permutations([-4, -2, 1]))

list_14 = [(3, 2, 2), (2, 3, 2), (2, 2, 3)] + [(-3, -2, -2), (-2, -3, -2), (-2, -2, -3)]
list_15 = [(-3, 2, 2), (2, -3, 2), (2, 2, -3)] + [(3, -2, -2), (-2, 3, -2), (-2, -2, 3)]
list_16 = list(permutations([3, -2, 2])) + list(permutations([-3, -2, 2]))


list_17 = [(5, 1, 1), (1, 5, 1), (1, 1, 5)] + [(-5, -1, -1), (-1, -5, -1), (-1, -1, -5)]
list_18 = list(permutations([5, -1, 1])) + list(permutations([-5, -1, 1]))
list_19 = [(-5, 1, 1), (1, -5, 1), (1, 1, -5)] + [(5, -1, -1), (-1, 5, -1), (-1, -1, 5)]

IM2_order_list = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + \
                 list_8 + list_9 + list_10 + list_11 + list_12 + list_13 + list_14 + \
                 list_15 + list_16 + list_17 + list_18 + list_19
for x in range(0, len(IM2_order_list)):
    m = IM2_order_list[x][0]
    n = IM2_order_list[x][1]
    k = IM2_order_list[x][2]
    Sum_Val = m * f1 + n * f2 + k * f3
    if abs(Sum_Val) == des_freq:
        hit_count += 1
        print("(m,n,k):", m, n, k)

    IM_freq_list_7th.append(Sum_Val)

print("\033[1;34m\nNo of hits :\033[1;m", hit_count)
Total_hits += hit_count
# avoid -ve freqs
IM_freq_list_7th = [abs(x) for x in IM_freq_list_7th]
# convert to set to eliminate repeat values
IM_freq_set = set(IM_freq_list_7th)
IM_freq_list_7th = list(IM_freq_set)
IM_freq_list_7th.sort()
print('\n',IM_freq_list_7th)

print("\033[1;34m-------------------------------------------------------------------------------\033[1;m")
'''---------------------------------------------------------------'''
''' ------------ All Upto 7th NL Combined-------------------------'''
print("\033[1;31m\n---------   SUMMARY  -----------\033[1;m")
Har_freq_list = Har_freq_list_2nd + Har_freq_list_3rd + Har_freq_list_4th\
                + Har_freq_list_5th + Har_freq_list_6th + Har_freq_list_7th
print("\033[1;31m\nAll Harmonic Freqs up-to 7th Non Linearity\033[1;m")
Har_freq_set = set(Har_freq_list)
Har_freq_list_all = list(Har_freq_set)
Har_freq_list_all.sort()
print(Har_freq_list_all)

IM_freq_list = IM_freq_list_2nd + IM_freq_list_3rd + IM_freq_list_4th\
               + IM_freq_list_5th + IM_freq_list_6th + IM_freq_list_7th
IM_freq_set = set(IM_freq_list)
IM_freq_list_all = list(IM_freq_set)
IM_freq_list_all.sort()
print("\033[1;31m\nAll IM Freq Components up-to 7th Non Linearity\033[1;m")
print(IM_freq_list_all)
print("\033[1;31m\nTotal Hits at desired f due to Inter-Modulation:\033[1;m",Total_hits)
print("\033[1;31m\nTotal Hits at desired f due to Harmonics:\033[1;m",Har_hits)