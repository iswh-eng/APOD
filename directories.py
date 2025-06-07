import json

def create_directories(config_dir, root_dir, picture_path, home_dir, apod_dir, settings_file, WIDTH, HEIGHT):

        # Make directories if not available
    try: 
        if not config_dir.exists():
            print('Creating directory for config in root')
            try:
                config_dir.mkdir(parents=True, exist_ok=True)
                print(f'Config directory: {config_dir} created in Root')
            except Exception as e:
                print(f'Unable make directory {config_dir} in {root_dir}\n{e}')
                return

        if not picture_path.exists():
            print('Creating directory for Pictures')
            try:
                picture_path.mkdir(parents=True, exist_ok=True)
                print(f'Pictures directory {picture_path} created in {home_dir}')
            except Exception as e:
                print(f'Unable make directory {picture_path} in {home_dir}\n{e}')
                return

        if not apod_dir.exists():
            print("Creating directory for APOD")
            try:
                apod_dir.mkdir(parents=True, exist_ok=True)
                print(f'Apod directory {apod_dir} created in {home_dir}')
            except Exception as e:
                print(f'Unable make directory {apod_dir} in {home_dir}\n{e}')
                return
            
    except Exception as e:
        print('Unable to resolve directories creation:\n', e)
        return

    try:
        if not settings_file.exists():
            print("Creating settings.json")
            default_settings = {
                "WIDTH": WIDTH,
                "HEIGHT": HEIGHT,
                "IMAGE_DIR": str(apod_dir)
            }
            try:
                with open(settings_file, 'w') as f:
                    json.dump(default_settings, f, indent=4)
            except Exception as e:
                print(f"Unable to create 'settings.json':\n{e}")
                return
    except Exception as e:
        print('Unable to resolve settings.json\n', e)

