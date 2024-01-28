import sys

def analyze_cat_shelter_log(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{filename}"!')
        return None

    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        cat_type, entry_time, exit_time = parts

        entry_time = int(entry_time)
        exit_time = int(exit_time)
        duration = exit_time - entry_time

        if cat_type == 'OURS':
            cat_visits += 1
            total_time_in_house += duration
            durations.append(duration)
        elif cat_type == 'THEIRS':
            other_cats += 1

    if cat_visits == 0:
        print('No cat visits found in the log.')
        return None

    average_duration = sum(durations) / len(durations)
    longest_duration = max(durations)
    shortest_duration = min(durations)

    return cat_visits, other_cats, total_time_in_house, average_duration, longest_duration, shortest_duration

def format_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f'{hours} Hours, {minutes} Minutes'

def main():
    if len(sys.argv) != 2:
        print('Missing command line argument!')
        sys.exit(1)

    filename = sys.argv[1]
    analysis_result = analyze_cat_shelter_log(filename)

    if analysis_result is not None:
        cat_visits, other_cats, total_time_in_house, average_duration, longest_duration, shortest_duration = analysis_result

        print('\nLog File Analysis')
        print('=' * 18 + '\n')
        print(f'Cat Visits: {cat_visits}')
        print(f'Other Cats: {other_cats}\n')
        print(f'Total Time in House: {format_time(total_time_in_house)}\n')
        print(f'Average Visit Length: {int(average_duration)} Minutes')
        print(f'Longest Visit: {int(longest_duration)} Minutes')
        print(f'Shortest Visit: {int(shortest_duration)} Minutes')

if __name__ == "__main__":
    main()
