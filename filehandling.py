def modify_file_content( input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        # Replace the old string with the new string
        modified_content = content.replace(old_string, new_string)

        with open(input_filename, 'w') as file:
            file.write(modified_content)

        print(f"Successfully replaced '{output_filename}' with '{new_string}' in {file_path}.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")