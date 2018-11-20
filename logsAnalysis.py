#!/usr/bin/env python3
# 
# Log Analysis project. 

import psycopg2

title1 = 'The Most Popular Three Articles of All Time'
query1 = """  
    SELECT a.title, COUNT(*) AS Views
    FROM articles a , log l
    WHERE l.path = '/article/' || a.slug
    GROUP BY a.title 
    ORDER BY Views DESC
    LIMIT 3; 
    """

title2 = 'The Most Popular author of All Time'
query2 = """
    SELECT a.name, COUNT(*) AS Views
    FROM authors a
    JOIN articles ar 
    ON ar.author = a.id
    JOIN log l 
    ON l.path = '/article/' || ar.slug
    GROUP BY a.name
    ORDER BY Views DESC

"""
title3 = 'The Day/s That Had More than 1% of Errors'
query3 = """
    WITH TotalRequestNumber AS (
    SELECT time::date AS day, count(*)
    FROM log
    GROUP BY day), 
    TotalErrorNumber AS (
    SELECT time::date AS day, count(*)
    FROM log
    WHERE status != '200 OK'
    GROUP BY day), 
    ErrorRateResult AS (
    SELECT requests.day,
    errors.count::float / requests.count::float * 100
    AS errorrate
    FROM TotalRequestNumber requests, TotalErrorNumber errors
    WHERE requests.day = errors.day)
    SELECT * FROM ErrorRateResult WHERE errorrate > 1;
"""
def GET_RESULT(query):
    db = psycopg2.connect("dbname=news")
    cu = db.cursor()  # Create a database cursor
    cu.execute(query)  # Execute the query
    result = cu.fetchall()  # Fetch all rows
    return result
    db.close()

def print_result (get_query):
    results = GET_RESULT(get_query)
    for result in results:
        print (str(result[0]) + ' - ' + str(result[1]) + ' views')

def print_result_error (get_query):
    results = GET_RESULT(get_query)
    for result in results:
        print ( str(result[0]) + ' - ' + str(result[1]) + ' %')

print (title1)
print('================================')
print_result(query1)
print ('\n')
print(title2)
print('================================')
print_result(query2)
print ('\n')
print(title3)
print('================================')
print_result_error(query3)
