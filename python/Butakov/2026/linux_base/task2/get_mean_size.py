import sys


def get_mean_size(lines):
    total_size = 0
    file_count = 0

    for line in lines:
        columns = line.split()

        if len(columns) >= 9:
            try:
                size = int(columns[4])
                total_size += size
                file_count += 1
            except ValueError:
                continue

    if file_count > 0:
        return total_size / file_count
    else:
        return 0


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    lines = lines[1:]

    mean_size = get_mean_size(lines)
    print(mean_size)
