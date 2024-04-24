import csv

data = csv.reader(open('Resources/election_data.csv'))
my_report = open('analysis/Election_Analysis.txt','w')

next(data)

totalv = 0
maxvote = 0 
can_list = {}

for row in data:
    #Total Votes
    totalv += 1

    can = row[2]

    if can not in can_list.keys():
        can_list[can] = 0

    can_list[can] += 1


output = f'''Election Results
-------------------------
Total Votes: {totalv:,}
-------------------------
'''

for can in can_list.keys():
    votes = can_list[can]

    if votes > maxvote:
        maxvote = votes
        winner = can

    output += f'{can}: {votes/totalv*100:.3f}% ({votes:,})\n'

output += f'''-------------------------
Winner: {winner}
-------------------------
'''

print(output)
my_report.write(output)