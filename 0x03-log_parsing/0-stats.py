#!/usr/bin/python3
"""
This module reads output line by line from stdin
get status code and print the total size
status codes and their num of occurrence in every
10 count
"""
from sys import stdin
import re
from datetime import datetime


def validate_ip(ip4_address):
    """
    Args:
        ip4_address: ip4_address passes
        return: True if ip is valid
    """
    if not ip4_address:
        return False

    pattern = r"^\d{1,3}$"
    octects = ip4_address.split(".")
    return all(re.match(pattern, octect) for octect in octects)


def validate_time(date, time):
    """
    checks if date and time are valid
    Args:
        date: current date
        time: current time
    """
    if not date and not time:
        return False

    date_time = str(date + " " + time).strip("[]")
    try:
        datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f")
        return True
    except ValueError:
        return False


def update_status_code(status_list, code):
    """
    Args:
        status_list: list of status codes
        code: status code
    """
    if not isinstance(status_list, list) or not code:
        return

    for status in status_list:
        if code in status:
            status[code] += 1
            return

    status_list.append({code: 1})
    status_list.sort(key=lambda x: int(next(iter(x.keys()))))


def print_data(total_size, status_list):
    """
    Args:
        total_size: Print total size of input
        status_list: list of status code (dict)
    """
    if status_list and total_size:
        print(f"File size: {total_size}")

        for data in status_list:
            for key, value in data.items():
                print(f"{key}: {value}")


def parse_line():
    """
        This function parse all lines and handle all error
        for smooth flow of program
    """
    count = 0
    status_codes = ("200", "301", "400", "401", "403", "404", "405", "500")

    data = {
            "total_size": 0,
            "status_codes": []
            }

    try:
        for line in stdin:
            line = line.split()
            count += 1

            if (validate_ip(line[0]) and
                validate_time(line[2], line[3]) and
                    line[-1].isdigit()):
                if line[-2] in status_codes:
                    data["total_size"] += int(line[-1])
                    update_status_code(data["status_codes"], line[-2])

            if count == 10:
                count = 0
                print_data(data['total_size'], data['status_codes'])

    except (TypeError, ValueError, IndexError):
        pass
    except KeyboardInterrupt:
        print_data(data['total_size'], data['status_codes'])
        raise


if __name__ == "__main__":
    parse_line()
