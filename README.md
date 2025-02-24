# Nodout Data Extraction and Time-Based Processing

This project contains Python scripts designed to extract and process data from nodout files with fixed-width formatting. It consists of two primary modules:

1. **Nodout Field Data Extraction:**  
   The `extract_nodout_field_data` function extracts specific field data (e.g., `z_disp`, `x_disp`, etc.) from a nodout file. The function is configurable with parameters such as starting line, block length, and line offset, and it outputs both a text file and a list of data blocks.

2. **Time-Step Based Data Extraction:**  
   The `extract_data_by_time` function processes an already extracted data file (such as the one produced for `z_disp`) and extracts data based on time steps. Parameters include the number of valid lines per time step, total time span, starting time value, sampling time step, number of time steps, and the number of lines to extract per time step. This function returns a list where each element corresponds to one time step's data.

A debugging script (`main.py`) demonstrates how to use both functions in sequence.

## Features

- **Configurable Field Extraction:**  
  Extract data from a nodout file by specifying the starting line, block length, and line offset. Supports multiple fields such as `nodal_point`, `x_disp`, `y_disp`, `z_disp`, `x_vel`, `y_vel`, `z_vel`, `x_accl`, `y_accl`, `z_accl`, `x_coor`, `y_coor`, and `z_coor`.

- **Time-Step Data Processing:**  
  Process the extracted data file further by sampling it based on time steps. This is useful for background data extraction in time-dependent analyses.

- **Output Files and Debugging:**  
  The scripts output processed data into text files. The debugging script prints detailed information about the extracted blocks and time-step groups for easier troubleshooting.

## Getting Started

### Prerequisites

- Python 3.x  
- Ensure that the nodout file (named `nodout` in the example) is present in the project directory and follows the expected fixed-width format.

### Usage

#### Nodout Field Data Extraction

The function `extract_nodout_field_data` is defined in `extract_nodout_data.py` and requires the following parameters:

- `file_path` (str): Path to the nodout file.
- `output_file_path` (str): Path to the output text file.
- `start_line` (int): The starting line number.
- `line_offset` (int): The offset (in lines) between successive data blocks.
- `range_length` (int): The number of lines in each block.
- `field` (str): The field to extract (e.g., `"z_disp"`).

#### Time-Step Based Data Extraction

The function `extract_data_by_time` is defined in `extract_data_by_time.py` and extracts data from the previously generated text file. Its parameters are:

- `file_path` (str): The file path to the extracted data file.
- `node_num` (int): The number of valid data lines in each time step.
- `total_time` (float): The total time span of the data.
- `start_rt_value` (float): The starting time value for extraction.
- `rt_step` (float): The sampling time step.
- `num_time_steps` (int): The number of time steps to extract.
- `n_extract` (int): The number of lines to extract from the beginning of each time step.

#### Debugging Script

A debugging script (`main.py`) is provided. It demonstrates how to call both functions sequentially:

- First, it extracts the nodout field data and writes it to a file.
- Next, it processes that file using the time-step extraction function.
- Finally, it prints the extracted data blocks and writes the time-step groups to a new output file.

### Running the Script

To run the debugging script, ensure that the nodout file is in the proper format and located in the project directory, then execute:

```bash
python main.py
```

## Code Explanation

- **Nodout Extraction (`extract_nodout_field_data`):**  
  - Reads the nodout file line by line.
  - Processes the file in blocks based on `start_line`, `line_offset`, and `range_length`.
  - Extracts the specified field using fixed-width slicing.
  - Converts the extracted string to a floating-point number (formatted in scientific notation).
  - Outputs the data to a text file and returns a list of blocks.

- **Time-Step Extraction (`extract_data_by_time`):**  
  - Reads the previously generated text file.
  - Divides the data into groups corresponding to time steps based on `node_num` and group size.
  - Computes the correct time step indices using `total_time`, `start_rt_value`, and `rt_step`.
  - Extracts a specified number of lines (`n_extract`) from each time step.
  - Returns a list where each element is the extracted data for one time step.

- **Debugging:**  
  The `main.py` script integrates both modules, prints detailed debug information, and saves the final processed data into a separate file.
