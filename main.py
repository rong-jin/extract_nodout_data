import os
from extract_nodout_data import extract_nodout_field_data
from extract_data_by_time import extract_data_by_time

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths for the input nodout file and the output file for z_disp field extraction
    file_path = os.path.join(current_dir, 'nodout')
    output_file_path = os.path.join(current_dir, 'z_disp.txt')
    
    # Set parameters for nodout extraction
    start_line = 68         # Starting line number for extraction
    line_offset = 60        # Line offset between successive data blocks
    range_length = 54       # Number of lines in each data block
    field = "z_disp"        # Field to extract (e.g., "z_disp")
    
    # Call the nodout extraction function and capture the returned data blocks
    try:
        data_blocks = extract_nodout_field_data(file_path, output_file_path, start_line, line_offset, range_length, field)
    except Exception as e:
        print(f"Error during nodout extraction: {e}")
        exit(1)
    
    # Debug: Print the returned data blocks
    print("Returned data blocks from extract_nodout_field_data:")
    for idx, block in enumerate(data_blocks, start=1):
        print(f"Block {idx}:")
        for line in block:
            print(line)
        print("-" * 40)
    
    # Set parameters for time-based extraction from the z_disp data file
    node_num = 54           # Number of valid data lines in each time step (should match the block length from nodout extraction)
    total_time = 1e-5       # Total time span of the data
    start_rt_value = 0.3e-5 # Starting time value for extraction
    rt_step = 0.05e-5       # Sampling time step
    num_time_steps = 15     # Number of time steps to extract
    n_extract = 15          # Number of lines to extract from the beginning of each time step

    try:
        true_measurement_groups = extract_data_by_time(
            output_file_path, node_num, total_time, start_rt_value, rt_step, num_time_steps, n_extract)
    except Exception as e:
        print(f"Error during time-step extraction: {e}")
        exit(1)
    
    # Debug: Print the groups extracted based on time steps
    print("Extracted true measurement groups:")
    for idx, group in enumerate(true_measurement_groups, start=1):
        print(f"Group {idx}: {group}")
    
    # Save the true measurement groups to a file (each line contains n_extract data values separated by commas)
    z_displ_true_file = os.path.join(current_dir, "z_displ_true.txt")
    try:
        with open(z_displ_true_file, 'w') as file:
            for group in true_measurement_groups:
                file.write(",".join(f"{val:.6e}" for val in group) + "\n")
        print(f"True values saved to {z_displ_true_file}")
    except Exception as e:
        print(f"Error writing true measurement groups to file: {e}")

