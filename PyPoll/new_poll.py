import os
import csv
poll_csv = os.path.join('..', '..', 'election_data.csv')
election_output = os.path.join('election_output.txt')
total_vote_count = 0
candidate_option = []
candidate_votes = {}
winning_candidate = ''
winning_count = 0
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for line in csvreader:
       total_vote_count += 1  
       candidate_name = line[2]
       if candidate_name not in candidate_option:
           candidate_option.append(candidate_name)   
           candidate_votes[candidate_name] = 0
       candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/ float(total_vote_count) * 100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        print(candidate_option)
        print(candidate_votes)
        with open(election_output, "w") as f:
            print("Election Results", file=f)
            print("-----------------------", file=f)
            print(f'{candidate_votes}', file=f)
            print("---------------------------------")
            print(f" And the winner is!!! {winning_candidate}", file=f)
    

     
print(voter_output)
print(winning_candidate)
print(total_vote_count)
