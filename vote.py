# Function to determine the winner
def determine_winner(votes):
    # Initialize winners and their respective vote counts
    winners = []
    max_votes = 0
    
    # Iterate through candidates
    for candidate, candidate_votes in votes.items():
        # Check if the candidate has at least 7 wins
        if len([vote for vote in candidate_votes if vote == "Win"]) >= 7:
            # Check if the candidate has the highest total votes
            total_votes = sum([1 for vote in candidate_votes if vote == "Win" or vote == "Lost"])
            if total_votes > max_votes:
                winner = [candidate]
                max_votes = total_votes
            elif total_votes == max_votes:
                winner.append(candidate)
    
    return winner


# votes for Tinubu, Atiku, and Obi from 10 local governments
votes = {
    "Tinubu": ["Win", "Lose", "Win", "Win", "Lost", "Win", "Lost", "Win", "Win", "Win"],
    "Atiku": ["Lost", "Lost", "Lost", "Win", "Win", "Lost", "Win", "Win", "Win", "Win"],
    "Obi": ["Win", "Lost", "Win", "Win", "Win", "Lost", "Lost", "Lost", "Win", "Lost"]
}

# Determine the winner(s)
winner = determine_winner(votes)

# Print the winner(s)
if winner:
    print(f'Winnar {winner}')
else:
    print("No clear winner.")

