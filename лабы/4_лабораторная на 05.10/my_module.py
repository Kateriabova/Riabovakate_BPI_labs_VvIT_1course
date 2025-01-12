def the_best_function(name):
    print(f'You are the best person I know, {name}')

def count_points_cybernitic(name, datetime, sqrt, luck):
    count = len(name) + int(datetime.split('.')[1]) + sqrt ** luck
    count = count ** 0.7
    return count