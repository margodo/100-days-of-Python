enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemies


increase_enemies()
print(f"enemies outside function: {enemies}")
