import time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect(user="postgres",
                                  password="156632",
                                  host="localhost",
                                  port="8890")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    sql_create_database = 'create database postgres_db'
    cursor.execute(sql_create_database)

    print('for tiny data')
    sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
    first = 'SELECT "VendorID", count(*) FROM public.trips group by 1;'
    second = 'SELECT "passenger_count", avg(total_amount) FROM public.trips GROUP BY 1;'
    third = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM public.trips GROUP BY 1, 2;'
    fourth = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM public.trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'
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

    print('for big data')
    sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
    first = 'SELECT "VendorID", count(*) FROM public.taxi group by 1;'
    second = 'SELECT "passenger_count", avg(total_amount) FROM public.taxi GROUP BY 1;'
    third = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM public.taxi GROUP BY 1, 2;'
    fourth = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM public.taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'
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

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
