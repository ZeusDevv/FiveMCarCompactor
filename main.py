import os, shutil

base_path = os.getcwd()
processed_path = os.path.join(base_path, 'processed_files')

if not os.path.exists(processed_path):
    os.mkdir(processed_path)

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)

    if not os.path.isdir(folder_path):
        continue

    meta_files = [f for f in os.listdir(folder_path) if f.endswith(".meta")]
    if not meta_files:
        continue

    stream_path = os.path.join(folder_path, "stream")
    if os.path.isdir(stream_path):
        stream_files = [f for f in os.listdir(stream_path) if f.endswith('.yft')]
    else:
        stream_files = []

    new_folder_path = os.path.join(base_path, folder + "_processed")
    os.mkdir(new_folder_path)

    for meta_file in meta_files:
        meta_path = os.path.join(folder_path, meta_file)
        shutil.copy(meta_path, new_folder_path)

    if stream_files:
        stream_folder_path = os.path.join(new_folder_path, "stream")
        os.mkdir(stream_folder_path)
        for stream_file in stream_files:
            stream_file_path = os.path.join(stream_path, stream_file)
            shutil.copy(stream_file_path, stream_folder_path)

            lua_file_path = os.path.join(stream_folder_path, stream_file.replace('.yft', '.lua'))
            vehicle_name = stream_file.replace('.yft', '')
            with open(lua_file_path, 'w') as f:
                f.write("['"+ vehicle_name +"'] = {\n")
                f.write("   ['name'] = '"+vehicle_name+"',\n")
                f.write("   ['brand'] = '"+vehicle_name+"',\n")
                f.write("   ['model'] = '"+ vehicle_name +"',\n")
                f.write("   ['price'] = 9999999,\n")
                f.write("   ['category'] = 'Gwop',\n")
                f.write("   ['hash'] = '"+vehicle_name+"',\n")
                f.write("   ['shop'] = 'pdm',\n")
                f.write("}\n")
    if os.path.exists(new_folder_path):
        new_processed_path = os.path.join(processed_path, folder + "_processed")
        shutil.move(new_folder_path, new_processed_path)
