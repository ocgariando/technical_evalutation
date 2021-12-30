 ===== Introduction =====
Since Lifespark is a Health Care company, we have created some fake data to support this
exercise. Don’t worry this data is completely made up, they aren’t real people it is not real PHI.
You can find these data sets attached in this email
Please submit your code via Github. It can be a public repo or you can be prepared share it with
one of our teammates as part of submission.
You can complete this exercise in any language of your choosing. Currently we have expertise
on the team in Ruby, Python, and Javascript. It will be fun if it is in a language that we are
unfamiliar with, just make sure we have the setup steps

 ===== Requirements =====
Here’s what we’ve gathered from conversations with our CFO and VP of Pop Health. We’ve
taken a stab at ranking them in order of importance, so if you don’t have time to get to all of
them, just start at the top.
1. As the VP of Population Health, I’d like to be able to see a list of 10 members that have
had the highest cost of care from admissions.
2. As the CFO I would like to be able to see the total count of and cost of care for
admissions broken down by week Sunday to Saturday.
3. As the VP of Life Management I would like to see a report of members that have had a
readmittance within the last 30 days.
4. As the VP of Life Management I would like to see a report of the top 10 longest
admissions.
5. As a data engineer I would like to be able to upload a new list of admissions.

=====  Recommended modules =====
Python version 3
Dependencies

backports.zoneinfo==0.2.1
click==7.1.2
csv-to-sqlite==2.1.1
dateparser==1.1.0
numpy==1.21.5
pandas==1.3.5
py-lru-cache==0.1.4
python-dateutil==2.8.2
pytz==2021.3
pytz-deprecation-shim==0.1.0.post0
regex==2021.11.10
six==1.16.0
tzdata==2021.5
tzlocal==4.1
=====  Installation ====
pip install -r requirements.txt

==== How to run ====
NOTE: Default Data loaded on sqlite - LOAD DATA

If data engineer I would like to be able to upload a new list of admissions
python run_ingest.py
NOTE: GENERATE REPORT
python run_cfo_vp_report.py

LIST OF REPORS
remittance_last_30days.csv
top10_members_highest_cost.csv
top_10_longest_admission.csv
total_weekly_admission.csv

 * Troubleshooting
 * FAQ
 * Maintainers