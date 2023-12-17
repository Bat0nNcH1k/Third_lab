import time
import sqlite3
import pandas as pd

t = sqlite3.connect('tiny.db')
big = sqlite3.connect('big.db')

tdata = pd.read_csv(r"D:\Second_Course\bd\third_lab\tiny.csv")
tdata.to_sql('trips', t, if_exists='replace', index=False)
bdata = pd.read_csv(r"D:\Second_Course\bd\third_lab\big.csv")
bdata.to_sql('trips', big, if_exists='replace', index=False)

cursor = t.cursor()
first = 'SELECT VendorID, count(*) FROM trips GROUP BY 1;'
second = 'SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;'
third = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;'''
fourth = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'''

print('for tiny data')
cursor = t.cursor()
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for z in range(10):
    #first
    t_0 = time.perf_counter()
    cursor.execute(first)
    first_result = cursor.fetchall()
    t_1 = time.perf_counter()
    sum_1 += (t_1 - t_0)
    #second
    t_0 = time.perf_counter()
    cursor.execute(second)
    second_result = cursor.fetchall()
    t_1 = time.perf_counter()
    sum_2 += (t_1 - t_0)
    #third
    t_0 = time.perf_counter()
    cursor.execute(third)
    third_result = cursor.fetchall()
    t_1 = time.perf_counter()
    sum_3 += (t_1 - t_0)
    #fourth
    t_0 = time.perf_counter()
    cursor.execute(fourth)
    fourth_result = cursor.fetchall()
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
cursor.close()
t.close()

print('for big data')
cursor = big.cursor()
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for z in range(10):
    #first
    t_0 = time.perf_counter()
    cursor.execute(first)
    first_result = cursor.fetchall()
    t_1 = time.perf_counter()
    sum_1 += (t_1 - t_0)
    #second
    t_0 = time.perf_counter()
    cursor.execute(second)
    second_result = cursor.fetchall()
    t_1 = time.perf_counter()
    sum_2 += (t_1 - t_0)
    #third
    t_0 = time.perf_counter()
    cursor.execute(third)
    third_result = cursor.fetchall()
    t_1 = time.perf_counter()
    sum_3 += (t_1 - t_0)
    #fourth
    t_0 = time.perf_counter()
    cursor.execute(fourth)
    fourth_result = cursor.fetchall()
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
cursor.close()
big.close()
