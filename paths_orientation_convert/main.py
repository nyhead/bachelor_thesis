import random

orientations = {"S" : 0, "E":1, "N":2, "W":-1}
# actions = ["CW", "CCW", "F", "W"]
num_rows = num_cols = 32
num_agents = 100



def get_random_orientation():
    return random.choice(list(orientations.keys()))

def get_actions(curr_info, next_info):
    curr_o, curr_l = curr_info  # Current orientation and location
    next_o, next_l = next_info  # Target orientation and location

    # Define orientation order and map each orientation to an index
    orientations = ['N', 'E', 'S', 'W']
    orientation_index = {orientation: idx for idx, orientation in enumerate(orientations)}

    # Calculate the target orientation based on movement direction
    direction = (next_l[0] - curr_l[0], next_l[1] - curr_l[1])
    direction_to_orientation = {
        (-1, 0): 'W',  # Moving left
        (1, 0): 'E',   # Moving right
        (0, 1): 'S',  # Moving down
        (0, -1): 'N'    # Moving up
    }

    next_o = direction_to_orientation.get(direction, curr_o)  # Update target orientation

    # Calculate rotations needed
    curr_idx = orientation_index[curr_o]
    next_idx = orientation_index[next_o]
    rotation_steps = (next_idx - curr_idx) % 4  # Calculate rotation steps in a circular manner

    # Determine actions based on rotation direction
    if rotation_steps == 0:
        actions = ["F"]  # No rotation needed, just move forward
    else:
        if rotation_steps == 2:
            actions = ["CW", "CW", "F"]  # Opposite direction, two turns
        else:
            action = "CW" if rotation_steps == 1 else "CCW"
            actions = [action, "F"]

    return actions, next_o
# def run_simulation(paths):
#     timestep = 0
#     for id,path in enumerate(paths):
#         orientation = get_random_orientation()
#         print(f'Agent {id}: \t{path}')
#         for i in range(len(path)-1):
#             curr = path[i]
#             next = path[i+1]
#             prev_orientation = orientation
#             actions, orientation = get_actions([orientation, curr],['', next])

#             print(i, prev_orientation, curr, actions, orientation, next)
#         # break
def run_simulation(paths):
    timestep = 0
    # Dictionary to store agent positions at each timestep
    positions_at_time = {}  # Format: {timestep: set of (position, agent_id)}

    for id, path in enumerate(paths):
        orientation = get_random_orientation()
        print(f'Agent {id}: \t{path}')
        for i in range(len(path) - 1):
            curr = path[i]
            next = path[i + 1]
            prev_orientation = orientation
            actions, orientation = get_actions([orientation, curr], ['', next])

            # Check for conflicts at the next position
            if timestep not in positions_at_time:
                positions_at_time[timestep] = set()

            if next in positions_at_time[timestep]:
                print(f"Conflict detected at timestep {timestep} for Agent {id} at position {next}")
            else:
                # No conflict; register this position
                positions_at_time[timestep].add(next)

            print(i, prev_orientation, curr, actions, orientation, next)
            timestep += 1  # Advance timestep after each move for each agent
        timestep = 0  # Reset timestep for each agent
def main():
    paths = []
    with open("paths.txt", "r") as f:
        for line in f:
            # agent = []
            id, path = line.split(':')
            # id = id.remove('Agent')
            path = [eval(x) for x in path.split('->')[:-1]]
            # print(f'{id}\t{path}')
            paths.append(path)
            # break
    run_simulation(paths)

if __name__ == '__main__':
    main()
    o = get_random_orientation()
    print(o)
    print(get_actions([o,(8, 14)], ['',(7, 14)]))