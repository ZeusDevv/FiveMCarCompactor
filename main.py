import os
import shutil

# Get current directory
base_path = os.getcwd()

# Create processed_files directory if it doesn't exist
processed_path = os.path.join(base_path, 'processed_files')
if not os.path.exists(processed_path):
    os.mkdir(processed_path)

# Create stream folder in base_path
stream_path = os.path.join(base_path, 'stream')
if not os.path.exists(stream_path):
    os.mkdir(stream_path)

# Loop through directories in current directory
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    
    # Only operate on directories
    if not os.path.isdir(folder_path):
        continue
    
    # Find .meta files in directory
    meta_files = [f for f in os.listdir(folder_path) if f.endswith('.meta')]
    if not meta_files:
        continue

    # Find .ycd, .yft, and .ytd files in "stream" directory
    stream_dir_path = os.path.join(folder_path, 'stream')
    if os.path.isdir(stream_dir_path):
        stream_files = [f for f in os.listdir(stream_dir_path) if f.endswith(('.ycd', '.yft', '.ytd'))]
    else:
        stream_files = []

    # Create new directory with .meta contents
    new_folder_path = os.path.join(base_path, folder + '_data')
    os.mkdir(new_folder_path)
    for meta_file in meta_files:
        meta_path = os.path.join(folder_path, meta_file)
        shutil.copy(meta_path, new_folder_path)
    
    # Move stream files to stream folder in base_path
    if stream_files:
        for stream_file in stream_files:
            stream_file_path = os.path.join(stream_dir_path, stream_file)
            shutil.move(stream_file_path, stream_path)
        
    # Move newly created folder to processed_files directory
    if os.path.exists(new_folder_path):
        new_processed_path = os.path.join(processed_path, folder + '_data')
        shutil.move(new_folder_path, new_processed_path)
