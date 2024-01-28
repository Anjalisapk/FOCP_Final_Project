import sys

def read_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

def analyze_log(lines):
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    visit_lengths = []

    for line in lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        cat_type = parts[0]
        entry_time = int(parts[1])
        exit_time = int(parts[2])

        if cat_type == 'OURS':
            cat_visits += 1
            total_time_in_house += (exit_time - entry_time)
            visit_lengths.append(exit_time - entry_time)
        elif cat_type == 'THEIRS':
            other_cats += 1

    if cat_visits == 0:
        average_visit_length = longest_visit = shortest_visit = 0
    else:
        average_visit_length = sum(visit_lengths) / cat_visits
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)

    return cat_visits, other_cats, total_time_in_house, average_visit_length, longest_visit, shortest_visit

def format_time(minutes):
    hours = minutes // 60
    minutes %= 60
    return f"{hours} Hours, {minutes} Minutes"

def main():
    # if len(sys.argv) != 2:
    #     print('Missing command line argument!')
    #     sys.exit(1)

    file_path = "shelter_2023-08-25.log"
    lines = read_log_file(file_path)

    cat_visits, other_cats, total_time, avg_length, longest, shortest = analyze_log(lines)

    print(f'Log File Analysis\n{"=" * 18}\n')
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}\n')
    print(f'Total Time in House: {format_time(total_time)}\n')
    print(f'Average Visit Length: {format_time(avg_length)}')
    print(f'Longest Visit:        {format_time(longest)}')
    print(f'Shortest Visit:       {format_time(shortest)}')

if __name__ == "__main__":
    main()
