# FIDE Chess Ratings Analysis

This project aims to analyzes FIDE chess ratings for the top ranked chess players in the world. This explores patterns in ELO scores, games played, and federations. This concurrently takes a look at basic EDA and manipulation of a csv data structure to extract specific information we want to analyze.

## Features
- Basic data cleaning using pandas.
- Visualizations of ELO, birth years and federation trends with the tools of Matplotlib and Seaborn
- Insights into top-performing players and federations.

## Skills Demonstrated
- Python (pandas, NumPy, seaborn, matplotlib)
- Data exploration and visualization

## How to Use
1. Clone this repository.
2. Place `FIDERanking.csv` in the project directory.
3. Run `chess_project.py` to generate insights and visualizations.

## Findings
- Larger federations such as the USA, Russia and India have the highest populations of players.
- There is an expected moderate negative correlation in the birth year of the player and the number of games played.
- There is little to no correlation to ELO (level of play) and birth year, which may seem surprising at first. However, as chess has grown there is an increasing number of young players competing at very high levels.
- There is an accutely moderate positive correlation to a player's ELO and the amount of games played. Thus, at this range of ELOs the more games played tends to show a larger ELO.

## Visualizations
### Correlation Heatmap
![Distribution of ELO](ChessELODistribution.png)
![Correlation Heatmap](ChessHeatmapCorrelation.png)

Feel free to explore and contribute! This is my first project so I am open to any constructive criticism!
