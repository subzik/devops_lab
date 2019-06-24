# import block
import subprocess
import json
import configparser
import os
import datetime
import time
import psutil

# install bash, packs
subprocess.call("./CPUmon/install.sh", shell=True)

# util data checker

cpu = psutil.getloadavg()
disc = psutil.disk_usage('/')
ram = psutil.virtual_memory()
io = psutil.disk_io_counters()
network = psutil.net_io_counters()


# int class


class CPUmon:
    """PC INFO app version.1.0"""

    cpu = psutil.getloadavg()

    @staticmethod
    def output():
        print('cpu average info checked')


print(CPUmon.__doc__)

end = CPUmon()

# settings parser file ini


def create_config(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "output", "json")
    config.set("Settings", "interval", "5")
    config.set("Settings", "settings_info",
               "You can set format %(output)s or time for %(interval)s")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )

    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    output = get_setting(path, 'Settings', 'output')
    interval = int(get_setting(path, 'Settings', 'interval'))

    update_setting(path, "Settings", "interval", "5")
    delete_setting(path, "Settings", "something")


pr = [['CPU load average: ', cpu],
      ['Disc status:', disc],
      ['RAM info:', ram],
      ['Disc IO status:', io],
      ['Network status:', network]]

# for exit file
timestamp = ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
file = open("log." + output, "w")

for i in range(1, int(interval) + 1):
    if output == "json":
        prints = json.dumps({
            "Status ": str(i),
            "Timestamp": timestamp,
            "CPU average": cpu,
            "Memory disc info": disc,
            "RAM info": ram,
            "Disc IO status": io,
            "Network status": network
        }, indent=4)
        file.write(prints)
        time.sleep(int(interval))
    elif output == "txt":
        prints = "\n" + "SNAPSHOT :" + str(i) + " " + \
                 timestamp + ":" + "\n" + \
                 "CPU average" + str(CPUmon.cpu) + " " + \
                 "Memory disc info:" + str(disc) + " " + \
                 "RAM info" + str(ram) + " " + \
                 "IO_info:" + str(io) + " " + \
                 "\n" + "Network_info:" + str(network) + "\n"
        file.write(prints)
        time.sleep(int(interval))

    end.output()
