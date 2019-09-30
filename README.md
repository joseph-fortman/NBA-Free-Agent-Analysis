# NBA-Free-Agent-Analysis

* This version is rudimentary, major updates coming *

## Abstract
Each summer, an interesting spectacle of business plays out with incredible visibility. Thanks to a limited scope, savage reporters, and an eager fan base, the NBA free agency provides a glimpse into corporate strategy, employee preference, and team building. However, every fan wants to state their opinion during decision reviews and objective feedback is hard to come by.
The following supervised learning model aims to provide a decision boundary to classify whether a general manager’s free agent signing was a good deal.

## Introduction
When playing stud poker [1], the proper bet does not depend on the outcome of the round. The player who becomes emotional and superstitious about certain hands or opponents is the patsy, bound to lose in the long-run.

As in stud poker, NBA general managers can see most of the cards their peers hold. As observers, so can we; however, it is hard to get a glimpse of the card faced down and the consequential gambles the executives make. Perhaps the best we can do is study history and model the difference between those which worked out and those that did not.

By decomposing at dataset of contract terms, player stats, and a subjective [-3, 3] tag to signify overall value, a classifier can be fit to analyze future free agents. Although the subjective decisions used to teach this classifier is concerning, the goal of this machine learning algorithm is not to make a final decision. The objective is to roughly evaluate NBA general managers decisions and avoid signing players with low odds to improve team success at the price point.

## Data
Player stats will be acquired from SportsReference [2] via the web scraping Python script included in this repository. Contract details come courtesy of Keith Smith [3]. He provides a great breakdown accessible on Google Sheets. The evaluations were done by myself; however, I have plans to survey fans on RealGM [4] to get more accurate evaluations.

Currently, only 2018-19 season data has been compiled. With so many features, 380 records is not enough for a good classifier. By the 2019 free agent market opening in July I hope to have a larger dataset ready.

### Subjective Player Valuations
Given the terms of a player’s contract, they are scored as follows:
```
  (-3) Exceptional negative impact on team success and outlook
  (-2) Harmful to team success and outlook
  (-1) Almost expiring contract, negative presence, only fair value based on team needs
  (0) Fair market value, replaceable, liquid as trade filler, select minimum contracts
  (1) Expiring contract, positive presence, young potential
  (2) Beneficial to team success
  (3) Exceptional contributions to team success given the terms of his contract
```
As the above are only guidelines, they are meant to be broken and stretched. Seven numbers cannot classify the value of NBA players, thus, the disregard for guidelines in various circumstances will blur the lines and provide for a better mathematical decision.

## Model
The current model uses a simple least squares minimization classifier. Much improvement can be made on this front, and will be with time. I will likely move from a classifier made from scratch to using an API like TPOT [5].

## Citations
[1] https://www.pagat.com/poker/variants/5stud.html

[2] https://www.basketball-reference.com/

[3] [Keith Smith - NBA Salaries & Rosters Sheets](https://docs.google.com/spreadsheets/d/1T2Eg_zvqNqQD_5TpE4Ns6xhElatXdLpYG1roZtRLyvE/edit?usp=sharing)

[4] https://forums.realgm.com/boards/viewforum.php?f=243

[5] https://github.com/EpistasisLab/tpot
