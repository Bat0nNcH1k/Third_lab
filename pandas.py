import time
import pandas as pd

t = pd.read_csv(r"D:\Second_Course\bd\third_lab\tiny.csv")
big = pd.read_csv(r"D:\Second_Course\bd\third_lab\big.csv")

print('for tiny data')
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for z in range(10):
    #first
    t_0 = time.perf_counter()
    first_result = t.groupby(["VendorID"]).size()
    t_1 = time.perf_counter()
    sum_1 += (t_1 - t_0)
    #second
    t_0 = time.perf_counter()
    second_result = t.groupby(["passenger_count"])["total_amount"].mean()
    t_1 = time.perf_counter()
    sum_2 += (t_1 - t_0)
    #third
    t_0 = time.perf_counter()
    t['Year'] = pd.to_datetime(t['tpep_pickup_datetime']).dt.year
    third_result = t.groupby(['passenger_count', 'Year']).size()
    t_1 = time.perf_counter()
    sum_3 += (t_1 - t_0)
    #fourth
    t_0 = time.perf_counter()
    t['Year'] = pd.to_datetime(t['tpep_pickup_datetime']).dt.year
    t['trip_distance'] = t['trip_distance'].round()
    fourth_result = t.groupby(['passenger_count', 'Year', 'trip_distance']).size().reset_index(name='count').sort_values(['Year', 'count'], ascending=[True, False])
    t_1 = time.perf_counter()
    sum_4 += (t_1 - t_0)
    if z == 9:
        print("First query")
        print("Result: ", first_result)
        print("Average time: ", sum_1 / 10)
        print()
        print("Second query")
        print("Result: ", second_result)
        print("Average time: ", sum_2 / 10)
        print()
        print("Third query")
        print("Result: ", third_result)
        print("Average time: ", sum_3 / 10)
        print()
        print("Fourth query")
        print("Result: ", fourth_result)
        print("Average time: ", sum_4 / 10)
        print()

print('for big data')
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for z in range(10):
    #first
    t_0 = time.perf_counter()
    first_result = big.groupby(["VendorID"]).size()
    t_1 = time.perf_counter()
    sum_1 += (t_1 - t_0)
    #second
    t_0 = time.perf_counter()
    second_result = big.groupby(["passenger_count"])["total_amount"].mean()
    t_1 = time.perf_counter()
    sum_2 += (t_1 - t_0)
    #third
    t_0 = time.perf_counter()
    big['Year'] = pd.to_datetime(big['tpep_pickup_datetime']).dt.year
    third_result = big.groupby(['passenger_count', 'Year']).size()
    t_1 = time.perf_counter()
    sum_3 += (t_1 - t_0)
    #fourth
    t_0 = time.perf_counter()
    big['Year'] = pd.to_datetime(big['tpep_pickup_datetime']).dt.year
    big['trip_distance'] = big['trip_distance'].round()
    fourth_result = big.groupby(['passenger_count', 'Year', 'trip_distance']).size().reset_index(name='count').sort_values(['Year', 'count'], ascending=[True, False])
    t_1 = time.perf_counter()
    sum_4 += (t_1 - t_0)
    if z == 9:
        print("First query")
        print("Result: ", first_result)
        print("Average time: ", sum_1 / 10)
        print()
        print("Second query")
        print("Result: ", second_result)
        print("Average time: ", sum_2 / 10)
        print()
        print("Third query")
        print("Result: ", third_result)
        print("Average time: ", sum_3 / 10)
        print()
        print("Fourth query")
        print("Result: ", fourth_result)
        print("Average time: ", sum_4 / 10)
