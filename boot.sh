#! /bin/bash

read -p "Would you like to play rock, paper, scissors? 'Yes' or 'No' " answer

if [ $answer == "Yes" ]
then
    python3 rock_paper_scissors.py
else
    echo "That's too bad, maybe next time!"
fi