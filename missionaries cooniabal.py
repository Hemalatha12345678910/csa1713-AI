from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    # No negative values, and missionaries not outnumbered on either side
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_successors(state):
    successors = []
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1),  # 1 missionary and 1 cannibal
    ]

    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, 'right')
        else:
            new_state = (m_left + m, c_left + c, 'left')

        new_m_left, new_c_left, new_boat = new_state
        new_m_right = 3 - new_m_left
        new_c_right = 3 - new_c_left

        if is_valid(new_m_left, new_c_left, new_m_right, new_c_right):
            successors.append(new_state)

    return successors

def solve():
    start = (3, 3, 'left')
    goal = (0, 0, 'right')
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state == goal:
            return path

        for successor in get_successors(current_state):
            queue.append((successor, path + [successor]))

    return None

# Run and print solution
solution = solve()
if solution:
    for step in solution:
        m_left, c_left, boat = step
        print(f"Left -> M: {m_left}, C: {c_left}, Boat: {boat}")
else:
    print("No solution found.")
