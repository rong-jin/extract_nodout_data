"""
Author: Rong Jin, University of Kentucky
Date: 02-24-2025
Description: Extracts data from a file based on time.
"""

def extract_data_by_time(file_path, node_num, total_time, start_rt_value, rt_step, num_time_steps, n_extract):
    """
    Extracts data from a file based on time.

    Parameters:
      file_path (str): The file path.
      node_num (int): The number of valid data lines in each time step.
      total_time (float): The total time span of the data.
      start_rt_value (float): The starting time value for extraction.
      rt_step (float): The sampling time step.
      num_time_steps (int): The number of time steps to extract.
      n_extract (int): The number of lines to extract from the beginning of each time step.
      
    Returns:
      list: A list where each element is a list of extracted floating-point numbers for one time step.
    """
    # Read all lines from the file
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Assume each time step consists of node_num lines of valid data plus one blank line,
    # i.e., each data block occupies (node_num + 1) lines.
    group_size = node_num + 1
    num_groups_in_file = len(lines) // group_size
    if num_groups_in_file < 2:
        dt = total_time
    else:
        dt = total_time / (num_groups_in_file - 1)
    print(f"Total time steps in file: {num_groups_in_file}, dt = {dt:e}")

    # Calculate the starting time step index (0-indexed), using rounding.
    start_group_index = int(round(start_rt_value / dt))
    print(f"start_rt_value = {start_rt_value:e} corresponds to time step index: {start_group_index}")

    # Calculate the step between two sampling time steps (in terms of time step count)
    group_step = int(round(rt_step / dt))
    print(f"rt_step = {rt_step:e} corresponds to a time step interval of: {group_step}")

    # Each data block occupies group_size lines in the file.
    line_offset = group_step * group_size
    # Calculate the corresponding starting line in the file (1-indexed)
    start_line = start_group_index * group_size + 1
    print(f"Starting line in file: {start_line}, line offset per step: {line_offset}")

    extracted_groups = []
    # Loop to extract data for the specified number of time steps.
    for group in range(num_time_steps):
        current_start = start_line + group * line_offset
        current_end = current_start + n_extract - 1
        group_data = []
        # Note: file line indices are 0-indexed.
        if current_start - 1 < len(lines):
            for i in range(current_start - 1, min(current_end, len(lines))):
                try:
                    group_data.append(float(lines[i].strip()))
                except ValueError:
                    print(f"Warning: Line {i+1} could not be converted to a float.")
        else:
            print(f"Warning: Current starting line {current_start} exceeds total number of lines {len(lines)}")
        extracted_groups.append(group_data)

    # If n_extract is 1, convert single-element lists to scalars.
    if n_extract == 1:
        extracted_groups = [grp[0] if len(grp) == 1 else grp for grp in extracted_groups]
    return extracted_groups
