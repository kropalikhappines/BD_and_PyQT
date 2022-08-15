from task_2 import host_range_ping
from tabulate import tabulate


def host_range_ping_tab():
    dict_ip = host_range_ping()

    print(tabulate(dict_ip, headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == '__main__':
    host_range_ping_tab()
