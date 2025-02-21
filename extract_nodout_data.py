"""
Author: Rong Jin, University of Kentucky
Date: 02-21-2025
Description: Extract data from the nodout file and save it to a text file.
"""

import os
def extract_nodout_field_data(file_path, output_file_path, start_line, line_offset, range_length, field):
    """
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
    """
    # Define the fields and their corresponding byte widths:
    # "nodal_point" occupies the first 10 bytes, and all other fields occupy 12 bytes each.
    fields = ["nodal_point", "x_disp", "y_disp", "z_disp", 
              "x_vel", "y_vel", "z_vel", 
              "x_accl", "y_accl", "z_accl", 
              "x_coor", "y_coor", "z_coor"]
    if field not in fields:
        raise ValueError(f"Field '{field}' is invalid. Valid fields are: {fields}")

    # Calculate the starting and ending indices for substring extraction.
    # Python slicing is end-exclusive.
    if field == "nodal_point":
        start_idx, end_idx = 0, 10  # Extract bytes 0-9 (10 characters)
    else:
        idx = fields.index(field)
        # For fields other than "nodal_point", the first field starts at byte 10 (index 10)
        start_idx = 10 + (idx - 1) * 12
        end_idx = start_idx + 12  # Extract 12 characters

    try:
        # Read the nodout file.
        with open(file_path, 'r') as file:
            lines = file.readlines()

        max_lines = len(lines)  # Total number of lines in the file.
        result_blocks = []      # List to store blocks of extracted data.

        # Process blocks of lines based on the provided start_line, range_length, and line_offset.
        while start_line + range_length - 1 <= max_lines:
            block_data = []  # List to store extracted data for the current block.
            end_line = start_line + range_length - 1

            # Extract data for the specified field in each line of the current block.
            for i in range(start_line - 1, end_line):
                if i < len(lines):
                    line = lines[i]
                    # Extract the substring using the calculated byte positions and strip whitespace.
                    extracted_str = line[start_idx:end_idx].strip()

                    # If the string does not contain 'e' (scientific notation), try to insert 'e' at the appropriate position.
                    if 'e' not in extracted_str.lower():
                        for j in range(1, len(extracted_str)):
                            if extracted_str[j] in ['+', '-']:
                                extracted_str = f"{extracted_str[:j]}e{extracted_str[j:]}"
                                break

                    try:
                        extracted_value = float(extracted_str)
                        # Append formatted value to the current block.
                        block_data.append(f"{extracted_value:.6e}")
                    except ValueError:
                        print(f"Warning: Could not parse data at line {i + 1}: '{extracted_str}'")
                        continue

            result_blocks.append(block_data)
            start_line += line_offset  # Move to the next block's starting line.

        # Write the extracted data to the output file.
        with open(output_file_path, 'w') as output_file:
            for block in result_blocks:
                # Join each block's data with newlines and add an extra newline between blocks.
                output_file.write("\n".join(block) + "\n\n")

        print(f"{field} data successfully saved to {output_file_path}!")
        return result_blocks

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# if __name__ == "__main__":
#     # Get the current directory
#     current_dir = os.path.dirname(os.path.abspath(__file__))
    
#     # Define file paths
#     file_path = os.path.join(current_dir, 'nodout')
#     output_file_path = os.path.join(current_dir, 'z_disp.txt')
    
#     # Set the parameters for extraction
#     start_line = 68
#     line_offset = 60
#     range_length = 54
#     field = "z_disp"
    
#     # Call the extraction function and capture the returned data
#     data_blocks = extract_nodout_field_data(file_path, output_file_path, start_line, line_offset, range_length, field)
    
#     # Debug: Print the returned data blocks
#     print("Returned data blocks:")
#     for idx, block in enumerate(data_blocks, start=1):
#         print(f"Block {idx}:")
#         for line in block:
#             print(line)
#         print("-" * 40)
