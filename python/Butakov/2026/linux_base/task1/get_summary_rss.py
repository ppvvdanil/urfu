def get_summary_rss(file_path):
    total_rss = 0

    with open(file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]

        for line in lines:
            columns = line.split()

            if len(columns) > 5:
                try:
                    rss = int(columns[5])
                    total_rss += rss
                except ValueError:
                    continue

    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    unit_index = 0
    size = float(total_rss)

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


if __name__ == "__main__":
    file_path = "/root/ps.log"

    result = get_summary_rss(file_path)
    print(result)
