from task_1 import host_ping


def host_range_ping():
    while True:
        address_ip = input('Введите аддрес начала сети: ')
        try:
            octet = int(address_ip.split('.')[3])
            break
        except IndexError:
            print(f'Не корректный аддрес')
        except ValueError:
            pass
    while True:
        count_address = input('Сколько аддресов проверить: ')
        if not count_address.isnumeric():
            print('Введите число!')
        else:
            if int(count_address) + octet > 254:
                print(f'Максимальное количество хостов не должно превышать 254,'
                      f'в вашем случае максимально допустимое {254 - octet}')
            else:
                break
    list_address = []
    for last_octet in range(octet, octet + int(count_address)):
        address = address_ip.split('.')[:3]
        address.append(str(last_octet))
        list_address.append('.'.join(address))
    return host_ping(list_address)


if __name__ == '__main__':
    host_range_ping()
