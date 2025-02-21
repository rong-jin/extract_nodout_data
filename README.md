# extract_nodout_data
This python code is to read the LS-DYNA simulation result nodout file.

Extracts data for a specified field from a nodout file and returns the extracted data as a list of blocks.
Each block corresponds to a group of 'range_length' lines.
  
Args:
    file_path (str): Path to the nodout file.
    output_file_path (str): Path to the output text file.
    start_line (int): The starting line number.
    line_offset (int): The line offset for each increment.
    range_length (int): The number of lines in each block.
    field (str): The field to extract. Valid values include:
                  "nodal_point", "x_disp", "y_disp", "z_disp", 
                  "x_vel", "y_vel", "z_vel", "x_accl", "y_accl", "z_accl",
                  "x_coor", "y_coor", "z_coor".
  
Returns:
    list: A list of blocks, where each block is a list of extracted data strings.
