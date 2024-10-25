import random

# Create dice 1-6
player_dice = random.randint(1,6)
player_dice_2 =random.randint(1,6)
player_dice_3 =random.randint(1,6)
cpu_dice = random.randint(1,6)
cpu_dice_2 = random.randint(1,6)
cpu_dice_3 = random.randint(1,6)
# Create Player and CPU
player_hand = []
cpu_hand = []
player_score = 0
cpu_score = 0
# Compare rolls

# Award winner
# Add number needed to win
# num_to_win = int(input('How many do you need to win ?: '))
num_to_win = 10
# Make it dynamic
def dice_game():
    global player_dice,player_dice_2,player_dice_3,cpu_dice,cpu_dice_2,cpu_dice_3,player_hand,cpu_hand,player_score,cpu_score,num_to_win
    # while cpu_score < num_to_win and player_score < num_to_win:
    # 3 Rolls
    player_hand.append(player_dice)
    player_hand.append(player_dice_2)
    player_hand.append(player_dice_3)

    print('Player rolls are: ')

    # Loop rolls into player score
    for rolls in player_hand:
        print(rolls)
        player_score = player_score + rolls

    print(f'Players Score is {player_score}')
        # print(f'Player Score is: {player_score} and CPU Score is {cpu_score} ')

    # CPU Rolls
    cpu_hand.append(cpu_dice)
    cpu_hand.append(cpu_dice_2)
    cpu_hand.append(cpu_dice_3)

    print('CPU rolls are: ')

    for rolls in cpu_hand:
        print(rolls)
        cpu_score = cpu_score + rolls
    print(f'CPU Score is {cpu_score}')

    if player_score > cpu_score:
        print(f'Player Wins ! Player score: {player_score} is greater than CPU score: {cpu_score}')
    elif cpu_score > player_score:
        print(f'CPU Wins ! CPU score {cpu_score} is greater than Player Score: {player_score}')
    else: 
        print(f'It is tied at score {player_score} to {cpu_score}!')
dice_game()
