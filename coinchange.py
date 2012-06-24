def change(amount, denomination):
    if sum(denomination) == 0:
        return [0]
    length = len(denomination)
    coins = [0] * length
    length = length - 1
    while amount > 0 and length >= 0:
        while denomination[length] <= amount:
            coins[length] += 1
            amount -= denomination[length]
        length -= 1
        
            
    return coins
