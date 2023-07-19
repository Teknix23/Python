def calculate_results():
    team_a_totals = []
    team_b_totals = []

    for _ in range(5):
        score = input("Enter score for team A and team B separated by '+' sign: ")
        scores = score.split("+")

        team_a_score = int(scores[0])
        team_b_score = int(scores[1])

        team_a_totals.append(team_a_score)
        team_b_totals.append(team_b_score)

    team_a_total = sum(team_a_totals)
    team_b_total = sum(team_b_totals)

    overall_total = team_a_total + team_b_total
    average_total = overall_total / 5

    pick_for_this_match = average_total - 5

    print("Team A Totals:", team_a_totals)
    print("Team B Totals:", team_b_totals)
    print("Overall Total:", overall_total)
    print("Average Total:", average_total)
    print("Pick for this match:", pick_for_this_match)

calculate_results()