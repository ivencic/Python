import re


def remove_leading_zeros(ip_add):
    # Создаем регулярное выражение для поиска всех ведущих нулей в октетах IP-адреса
    pattern = r'\b0+(\d+)'

    # Заменяем ведущие нули в каждом октете на найденные цифры
    cleaned_ip_address = re.sub(pattern, r'\1', ip_add)

    return cleaned_ip_address


# Пример использования
ip_address = "192.101.001.1"
cleaned_ip = remove_leading_zeros(ip_address)
print(cleaned_ip)
