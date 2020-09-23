"""Create configuration envs.

What do you do need to config?
"""
import sys

config_file = f"app/configurations/envs/.env.{sys.argv[1]}"

# Read env
with open(config_file) as file_name:
    data = file_name.read()

# Write env file
with open(r".env", "w") as file_name:
    file_name.write(data)
