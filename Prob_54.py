import time
from collections import defaultdict

start =  time.time()

poker = [i.strip().split() for i in open("E:\Sharing\Data\p054_poker.txt").readlines()]

first_player, second_player = [], []
for i in poker:
    mid = (len(i) + 1) // 2
    first_player.append(i[:mid])
    second_player.append(i[mid:])


card_order = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}


def check_rank(n):
    num = ''.join(n)
    value = card_order[str(num)]
    return value


def check_flush(n):
    suit = [i[1] for i in n]
    if len(set(suit)) == 1:
        return True
    return False

def check_four_of_kind(n):
    values = [i[0] for i in n]
    value_count = defaultdict(lambda:0)
    for v in values:
        value_count[v] += 1
    if sorted(value_count.values()) == [1,4]:
        return True
    return False

def check_three_of_kind(n):
    values = [i[0] for i in n]
    value_count = defaultdict(lambda:0)
    for v in values:
        value_count[v] += 1
    if set(value_count.values()) == set([3,1]):
        return True
    return False
   
def check_two_pairs(n):
    values = [i[0] for i in n]
    value_count = defaultdict(lambda:0)
    for v in values:
        value_count[v] += 1
    rank_values = sorted([card_order[i] for i in values])
    keys = [key for key,value in value_count.items() if value == 2]
    val = []
    for key in keys:
        val.append(check_rank(key))    
    count = 0
    if sorted(value_count.values()) == [1,2,2]:
        return True, sorted(val)[1], sorted(val)[0], rank_values[0]
    return False

def check_one_pair(n):
    values = [i[0] for i in n]
    value_count = defaultdict(lambda:0)
    for v in values:
        value_count[v] += 1
    key1 = [key for key, value in value_count.items() if value == 2]
    rank_values = sorted([card_order[i] for i in values])
    if sorted(value_count.values()) == [1,1,1,2]:        
        return True, rank_values[-3], check_rank(key1)
    return False

def check_full_house(n):
    values = [i[0] for i in n]
    value_count = defaultdict(lambda:0)
    for v in values:
        value_count[v] += 1
    if sorted(value_count.values()) == [2,3]:
        return True
    return False

def check_straight(n):
    values = [i[0] for i in n]
    value_count = defaultdict(lambda:0)
    for v in values:
        value_count[v] += 1
    rank_values = [card_order[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_count.values())) == 1 and (value_range == 4):
        return True
    else:
        if set(values) == set(["A","2","3","4","5"]):
            return True
        return False

def check_straight_flush(n):
    if check_flush(n) and check_straight(n):
        return True
    return False

def check_royal_flush(n):
    if check_flush(n):
        values = [i[0] for i in n]
        value_count = defaultdict(lambda:0)
        for v in values:
            value_count[v] += 1
        rank_values = [card_order[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        for rank in rank_values:
            if rank < 10:
                return False
        if len(set(value_count.values())) == 1 and (value_range == 4):
            return True
        else:
            if set(values) == set(["A","2","3","4","5"]):
                return True
            return False
    
def check_high_card(n):
    values = [i[0] for i in n]  
    rank_values = [card_order[i] for i in values]
    return max(rank_values)

def check_hand(n):
    if check_royal_flush(n):
        return 10
    if check_straight_flush(n):
        return 9
    if check_four_of_kind(n):
        return 8
    if check_full_house(n):
        return 7
    if check_flush(n):
        return 6
    if check_straight(n):
        return 5
    if check_three_of_kind(n):
        return 4
    if check_two_pairs(n):
        return 3
    if check_one_pair(n):
        return 2
    return 1


   
first_player_hand, second_player_hand = [], []
for row in first_player:
    first_player_hand.append(check_hand(row))
for row in second_player:
    second_player_hand.append(check_hand(row))

count = 0

for i in range(1000):
    if first_player_hand[i] > second_player_hand[i]:
        count += 1
    if first_player_hand[i] == second_player_hand[i]:
        if check_one_pair(first_player[i]):
            bool1,val1,val2 = check_one_pair(first_player[i])
            bool2,val3,val4 = check_one_pair(second_player[i])
            if val2 > val4:
                count += 1
            if val2 == val4:
                if val1 > val3:
                    count += 1
        else:
            if check_high_card(first_player[i]) > check_high_card(second_player[i]):
                count += 1

print(count)

end = time.time()

print(end-start)

