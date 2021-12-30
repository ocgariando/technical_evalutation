### DEVELOPED BY OSMARO GARIANDO
### SAMPLE PHASE

import sqlite3 as sql
import pandas as pd

conn = sql.connect('lifespark.sqlite')
sql = """SELECT a.member_id, a.first_name, a.last_name, sum(b.cost) member_cost
       FROM admissions a
LEFT JOIN codes b ON a.code = b.code
group by  a.member_id, a.first_name, a.last_name
order by member_cost desc limit 10;"""
frame1 = pd.read_sql_query(sql , conn)
print("User Stories 1 - List of 10 members that have had the highest cost of care from admissions")
print(frame1)
frame1.to_csv("top10_members_highest_cost.csv")


sql = """SELECT strftime('%w',substr(discharge_date,1,10)) week, sum(b.cost) total_cost_by_week
FROM admissions a
LEFT JOIN codes b ON a.code = b.code
group by  strftime('%w',substr(discharge_date,1,10)) 
order by week;"""
frame2 = pd.read_sql_query(sql , conn)
print("User Stories 2 - Total count of and cost of care for admissions broken down by week Sunday to Saturday (Sunday =0)")
print(frame2)
frame2.to_csv("total_weekly_admission.csv")


sql = """select * from (
SELECT a.member_id, a.first_name, a.last_name,date(substr(a.discharge_date,1,10))  discharge_date,Cast ((
    JulianDay(date('now')) - JulianDay(date(substr(a.discharge_date,1,10))) 
) As Integer) remitday_days
FROM admissions a
LEFT JOIN codes b ON a.code = b.code
) where remitday_days <= 1000
;"""
## -- DEFAULT to 1000

frame3 = pd.read_sql_query(sql , conn)
print("User Stories 3 - Report of members that have had a readmittance within the last 30 days - DEFAULT to 1000")
print(frame3)
frame3.to_csv("remittance_last_30days.csv")


sql = """select b.member_id, b.first_name, b.last_name, b.dob, b.gender,min(b.admission_date) first_admission_date ,max(b.discharge_date) last_discharge_date ,
sum(JulianDay(date(b.discharge_date)) - JulianDay(date(b.admission_date))) admission_days from (
SELECT a.member_id, a.first_name, a.last_name, a.dob, a.gender,
iif(a.admission_date is null or trim(a.admission_date)="", substr(a.discharge_date,1,10),
substr(admission_date,-4,LENGTH (admission_date)) || "-" ||
iif(LENGTH(admission_date)=10,substr(admission_date,1,2), iif(LENGTH(replace(substr(admission_date,1,2),"/",""))=2, replace(substr(admission_date,1,2),"/","") ,"0" || replace(substr(admission_date,1,2),"/",""))) || "-" ||
iif(LENGTH(admission_date)=10,substr(admission_date,4,2), iif(LENGTH(replace(substr(admission_date,3,2),"/",""))=2, replace(substr(admission_date,3,2),"/","") ,"0" || replace(substr(admission_date,3,2),"/","")))) admission_date,
substr(a.discharge_date,1,10) as discharge_date
FROM admissions a) 
b group by b.member_id, b.first_name, b.last_name, b.dob, b.gender order by  admission_days desc limit 10;
"""


frame4 = pd.read_sql_query(sql , conn)
print("User Stories 4 - Top 10 Longest Admission")
print(frame4)
frame4.to_csv("top_10_longest_admission.csv")
