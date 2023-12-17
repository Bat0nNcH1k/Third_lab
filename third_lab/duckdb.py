import time
import duckdb

t = duckdb.connect('tiny.duckdb')
big = duckdb.connect('big.duckdb')

first = 'SELECT VendorID, count(*) FROM trips GROUP BY 1;'
second = 'SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;'
third = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;'''
fourth = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'''

print('for tiny data')
cursor = t.cursor()
cursor.execute("CREATE TABLE trips AS SELECT * FROM read_csv_auto('tiny.csv');")
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for z in range(10):
    #first
    t_0 = time.perf_counter()
    first_result = cursor.execute(first).fetchall()
    t_1 = time.perf_counter()
    sum_1 += (t_1 - t_0)
    #second
    t_0 = time.perf_counter()
    second_result = cursor.execute(second).fetchall()
    t_1 = time.perf_counter()
    sum_2 += (t_1 - t_0)
    #third
    t_0 = time.perf_counter()
    third_result = cursor.execute(third).fetchall()
    t_1 = time.perf_counter()
    sum_3 += (t_1 - t_0)
    #fourth
    t_0 = time.perf_counter()
    fourth_result = cursor.execute(fourth).fetchall()
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
cursor.execute("CREATE TABLE trips AS SELECT * FROM read_csv_auto('big.csv');")
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
for z in range(10):
    #first
    t_0 = time.perf_counter()
    first_result = cursor.execute(first).fetchall()
    t_1 = time.perf_counter()
    sum_1 += (t_1 - t_0)
    #second
    t_0 = time.perf_counter()
    second_result = cursor.execute(second).fetchall()
    t_1 = time.perf_counter()
    sum_2 += (t_1 - t_0)
    #third
    t_0 = time.perf_counter()
    third_result = cursor.execute(third).fetchall()
    t_1 = time.perf_counter()
    sum_3 += (t_1 - t_0)
    #fourth
    t_0 = time.perf_counter()
    fourth_result = cursor.execute(fourth).fetchall()
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
