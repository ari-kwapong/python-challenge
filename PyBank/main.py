import csv

data = csv.reader(open('Resources/budget_data.csv'))
my_report = open('analysis/Election_Analysis.txt','w')

next(data)

months = 0
total = 0
pre_rev = 0
total_ch = 0
gIv = 0
gDv = 0

for row in data:
    # Months
    months += 1 # months = months + 1

    # Total revenue
    rev = int(row[1])
    total += rev

    # Average Change
    ch = rev - pre_rev

    if pre_rev == 0:
        ch = 0

    total_ch += ch

    # Greatest Increase
    if ch > gIv:
        gIv = ch
        gIm = row[0]

    # Greatest Decrease
    if ch < gDv:
        gDv = ch
        gDm = row[0]

    # reset area
    pre_rev = rev


output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months - 1):,.2f}
Greatest Increase in Profits: {gIm} (${gIv:,})
Greatest Decrease in Profits: {gDm} (${gDv:,})
'''

print(output)
my_report.write(output)