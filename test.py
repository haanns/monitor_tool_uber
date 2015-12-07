
import psycopg2
import csv

try:
    conn = psycopg2.connect("dbname='ziqiu_li' user='ziqiu_li' host='localhost' password='dbpass'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

Station_List = ["Harry Bridges Plaza (Ferry Building)", "Townsend at 7th",
"San Francisco Caltrain 2 (330 Townsend)", "Embarcadero at Sansome",
"2nd at Townsend", "2nd at South Park", "Harry Bridges Plaza (Ferry Building)",
"Market at 10th", "Steuart at Market", "San Francisco Caltrain (Townsend at 4th)", "Market at Sansome",
"San Francisco Caltrain (Townsend at 4th)", "Steuart at Market", "Embarcadero at Folsom", "San Francisco Caltrain 2 (330 Townsend)"]


"""
for i in range(len(Station_List)):
    if i < len(Station_List)-1:
        print Station_List[i], "+", Station_List[i+1]
    else:
        print Station_List[i]

"""


result_array = []
for i in range(len(Station_List)):
    for j in range(len(Station_List)):
        cur = conn.cursor()
        cur.execute("""select "Count" from pair_values where "Start Station" = '""" + Station_List[i] + """'and "End Station" = '""" + Station_List[j] + """'""")
        rows = cur.fetchall()
        for row in rows:
            result_array.append(row[0])
            print Station_List[i], "+", Station_List[j], "+", row[0]
            result = Station_List[i], "+", Station_List[j], "+", row[0]
            writer = csv.writer(open("/Users/ziqiu_li/Desktop/result_file.csv", 'w'))
            writer.writerow(result)

print result_array
print sum(result_array)
"""
for i in range (0, len(result_array), 15):
    for j in range (0, 14, 1):
        new_array = []
        new_array.append(result_array[i+j])
    print new_array
"""
for i in range (0, len(result_array), 15):
    new_array = []
    for j in range (0, 15, 1):
        number = result_array[i+j]/82522.00*100
        new_array.append(number)
    print new_array
    print sum(new_array)