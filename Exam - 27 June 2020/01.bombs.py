from collections import deque

bomb_effects = deque([int(el) for el in input().split(', ')])
bomb_casings = deque([int(el) for el in input().split(', ')])

datura = 40
cherry = 60
smoke_decoy = 120

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

flag = False

while True:
    if not bomb_casings or not bomb_effects:
        break
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        flag = True
        break
    first_effect = bomb_effects[0]
    last_casing = bomb_casings[-1]

    if first_effect + last_casing == datura:
        datura_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif first_effect + last_casing == cherry:
        cherry_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif first_effect + last_casing == smoke_decoy:
        smoke_decoy_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if flag:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    bomb_effects = [str(el) for el in bomb_effects]
    print(f"Bomb Effects: {', '.join(bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    bomb_casings = [str(el) for el in bomb_casings]
    print(f"Bomb Casings: {', '.join(bomb_casings)}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")