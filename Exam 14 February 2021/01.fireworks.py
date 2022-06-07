from collections import deque

show = False
fireworks_effect = deque(int(el) for el in input().split(', ') if int(el) > 0)
explosive_power = deque(int(el) for el in input().split(', ') if int(el) > 0)
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while fireworks_effect and explosive_power:
    current_effect = fireworks_effect.popleft()
    current_power = explosive_power.pop()
    mix = current_power + current_effect
    if mix % 3 == 0 and mix % 5 != 0:
        palm_fireworks += 1
    elif mix % 5 == 0 and mix % 3 != 0:
        willow_fireworks += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        crossette_fireworks += 1
    else:
        current_effect -= 1
        if current_effect > 0:
            fireworks_effect.append(current_effect)
        explosive_power.append(current_power)
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        show = True
        break
if show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effect:
    print(f"Firework Effects left: {', '.join(str(el) for el in fireworks_effect)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
