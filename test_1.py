def check_relation(net, first, second):
    # first = first
    name_list = []
    net_in_list = list(net)
    while len(net_in_list) > 0:
        for index, item_tuple in enumerate(net_in_list):
            if name_friend := parse_name(item_tuple, first):
                name_list.append(name_friend)
                net_in_list[index] = None
        if second in set(name_list):
            return True
        else:
            try:
                net_in_list = list(filter(lambda x: x is not None, net_in_list))
                first = name_list.pop()
            except IndexError:
                return False
    return name_list

def parse_name(value: tuple, first: str):
    match value:
        case (name1, name2) if name1 == first:
            return name2
        case (name1, name2) if name2 == first:
            return name1
        case _:
            return None


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"),
        ("Лёша", "Катя"),
        ("Ваня", "Катя"),
        ("Вова", "Катя"),
        ("Лёша", "Лена"),
        ("Оля", "Петя"),
        ("Стёпа", "Оля"),
        ("Оля", "Настя"),
        ("Настя", "Дима"),
        ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
