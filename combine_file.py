import os

def combine_files(output_path, input_parts):            #this function recombine the ipynb files in to 
    with open(output_path, 'wb') as output_file:        #main_combined.ipynb file by a for loop, in 
        for part in input_parts:                        #which all the parts are recombined in the order 
            with open(part, 'rb') as input_file:        #it was splited
                output_file.write(input_file.read())

if __name__ == "__main__":
    parts = [f"main.ipynb.part{i}" for i in range(3)]
    combine_files('main_combined.ipynb', parts)