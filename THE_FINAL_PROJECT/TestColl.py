# Coded by Mushfiq Majal - 28290607

import math
import stddraw
import enemies 

score = 0

def check_collisions(bullets, enemy_list, bullet_radius=10, enemy_radius=30):

    global score

    new_bullets = []

    # makes sure we don't reuse collided bullets
    removed_bullets = set()
    
    # distance that defines a collision
    hit_zone = bullet_radius + enemy_radius

    for e in enemy_list:
        if not e["alive"]:
            continue # Skip enemies that have been hit already
            
        for i, b in enumerate(bullets):
            if i in removed_bullets:
                continue # This bullet already hit an enemy
        
            # distance formula:
            # b[0], b[1] are bullet's X and Y co-ords,  e["x"], e["y"] are enemy's X and Y co-ords
            dist = math.sqrt((b[0] - e["x"])**2 + (b[1] - e["y"])**2)
            
            if dist < hit_zone:
                e["alive"] = False    # remove the student
                score += 10           # Award 10 points when enemy is removed
                removed_bullets.add(i)  # add that bullet to removed_bullets
                break # Stop checking bullet collisions for this enemy

    # Only keep bullets that didn't hit an enemy
    for i, b in enumerate(bullets):
        if i not in removed_bullets:
            new_bullets.append(b)

    return new_bullets

# draws score on screen
def current_score():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(24)

    stddraw.text(100, 680, f"Score: {score}")




# This function checks whether the boss has been hit by a bullet. The boss has to be hit 10 times more than a normal enemies 
def check_boss_collisions(bullets, boss, bullet_radius=10):

    global score

    new_bullets = []
    removed_bullets = set()
    hit_zone = bullet_radius + enemies.BOSS_RADIUS

    if not boss["alive"]:
        return bullets

    for i, b in enumerate(bullets):
        if i in removed_bullets:
            continue

        dist = math.sqrt((b[0] - boss["x"])**2 + (b[1] - boss["y"])**2)

        if dist < hit_zone:
            enemies.boss_take_damage(boss, 1)   # 1 hit = 1 damage
            removed_bullets.add(i)

            if not boss["alive"]:
                score += 100   # boss bonus

    for i, b in enumerate(bullets):
        if i not in removed_bullets:
            new_bullets.append(b)

    return new_bullets

