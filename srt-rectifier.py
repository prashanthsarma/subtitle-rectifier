input_file = "subtitle3.srt"
output_file = "subtitle4.srt"
def replace_values():
    input_file = "subtitle.srt"
    output_file = "subtitle1.srt"
    with open(input_file, 'r') as f:
        lines = f.readlines()

    count = 62
    for i in range(2, len(lines), 1):
        if '1\n' == lines[i]:
            lines[i] = lines[i].replace('1\n', str(count)+'\n')
            count += 1

    with open(output_file, 'w') as f:
        f.writelines(lines)

##replace_values()

def process_file():
    with open(input_file, 'r') as f:
        lines = f.readlines()

    processed_lines = []
    for i, line in enumerate(lines):
        # Check if the line contains only numerical value
        if line.strip().isdigit():
            # If previous line is not empty, insert a blank line
            if i > 0 and lines[i - 1].strip() != '':
                processed_lines.append('\n')
        processed_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(processed_lines)
process_file()

from datetime import datetime, timedelta

def adjust_timestamps():
    with open(input_file, 'r') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        if '-->' in line:
            from_time_str, to_time_str = line.strip().split(' --> ')
            from_time = datetime.strptime(from_time_str, '%H:%M:%S,%f')
            to_time = datetime.strptime(to_time_str, '%H:%M:%S,%f')

            # Ensure to_time is at least 3 seconds after from_time
            if to_time <= from_time + timedelta(seconds=3):
                to_time = from_time + timedelta(seconds=3)

            processed_lines.append(f"{from_time_str} --> {to_time.strftime('%H:%M:%S,%f')[:-3]}\n")
        else:
            processed_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(processed_lines)


def fix_serial_numbers():
    with open(input_file, 'r') as f:
        lines = f.readlines()

    corrected_lines = []
    expected_serial_number = 1

    for line in lines:
        line = line.strip()

        # If line is empty, skip
        if not line:
            corrected_lines.append('\n')
            continue

        # If line is a serial number
        if line.isdigit():
            corrected_lines.append(str(expected_serial_number) + '\n')
            expected_serial_number += 1
        else:
            corrected_lines.append(line + '\n')

    with open(output_file, 'w') as f:
        f.writelines(corrected_lines)


fix_serial_numbers()
