#!/bin/sh

gnome-terminal -e "python3 daemon.py router1_config"
gnome-terminal -e "python3 daemon.py router2_config"
gnome-terminal -e "python3 daemon.py router3_config"
gnome-terminal -e "python3 daemon.py router4_config"
gnome-terminal -e "python3 daemon.py router5_config"
gnome-terminal -e "python3 daemon.py router6_config"
gnome-terminal -e "python3 daemon.py router7_config"


# pantheon-terminal -e "python3 daemon.py router1_config"
# pantheon-terminal -e "python3 daemon.py router2_config"
# pantheon-terminal -e "python3 daemon.py router3_config"
# pantheon-terminal -e "python3 daemon.py router4_config"
# pantheon-terminal -e "python3 daemon.py router5_config"
# pantheon-terminal -e "python3 daemon.py router6_config"
# pantheon-terminal -e "python3 daemon.py router7_config"

# terminator  -e "python3 daemon.py router1_config"
# terminator  -e "python3 daemon.py router2_config"
# terminator  -e "python3 daemon.py router3_config"
# terminator  -e "python3 daemon.py router4_config"
# terminator  -e "python3 daemon.py router5_config"
# terminator  -e "python3 daemon.py router6_config"
# terminator  -e "python3 daemon.py router7_config"
