from ipaddress import ip_address
from subprocess import PIPE, call


def host_ping(list_ip_address, timeout=3, requests=1):
    result = {'Узел доступен: ': [], 'Узел не доступен: ': []}
    for address in list_ip_address:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        args = ['ping', '-n', str(requests), '-w', str(timeout), str(address)]
        proc = call(args, shell=False, stdout=PIPE)  # По какой-то причине call работает быстрее Popen
        if proc == 0:
            result['Узел доступен: '].append(str(address))
            print(f'Узел доступен: {str(address)}')
        else:
            result['Узел не доступен: '].append(str(address))
            print(f'Узел не доступен: {str(address)}')
    return result


if __name__ == '__main__':
    lst = ['yandex.ru', '192.168.0.1', '192.168.0.10', '192.168.1.71',
           '192.168.1.1', '81.5.125.165', '2.2.2.2', '192.168.1.36']
    host_ping(lst)
