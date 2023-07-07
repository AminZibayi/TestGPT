import os
import shutil
import yaml

def migrateConfig():
    with open('./forestryCMS/config.yml', 'r') as f:
        config = yaml.safe_load(f)

    with open('./tinaCMS/config.yml', 'w') as f:
        yaml.safe_dump(config, f)

def migrateContent(content_type):
    src_dir = f'./forestryCMS/content/{content_type}'
    dest_dir = f'./tinaCMS/content/{content_type}'

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        shutil.copy(os.path.join(src_dir, filename), dest_dir)

def migrateStatic(static_type):
    src_dir = f'./forestryCMS/static/{static_type}'
    dest_dir = f'./tinaCMS/static/{static_type}'

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        shutil.copy(os.path.join(src_dir, filename), dest_dir)

def main():
    print("migration-start")

    migrateConfig()
    print("migration-progress: Config migrated")

    for content_type in ['posts', 'pages']:
        migrateContent(content_type)
        print(f"migration-progress: {content_type} migrated")

    for static_type in ['images', 'css', 'js']:
        migrateStatic(static_type)
        print(f"migration-progress: {static_type} migrated")

    print("migration-complete")

if __name__ == "__main__":
    main()