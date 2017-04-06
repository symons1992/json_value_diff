#-*- coding:utf-8 -*-
#
# bfs diff two json
#

import copy

j1 = {
        't1': 123,
        't2': [
            {
                'a1': 'abcd'
                },
            {
                'a2': 'efcgaaa'
                },
            ],
        't3': 345,
        }

j2 = {
        't1': 123,
        't2': [
            {
                'a1': 'abcd'
                },
            {
                'a2': 'efcg'
                },
            ],
        't3': 34,
        }


def get_value_by_key_list(key, j):

    if len(key) == 0:
        return None

    cnt = 0
    t = j
    while cnt < len(key):
        k = key[cnt]
        if isinstance(t, list):
            t = t[k]
        elif isinstance(t, dict):
            t = t[k]
        else:
            break
        cnt += 1
    return t


def bfs_search(key_list, aim, v_j2, res):

    if isinstance(aim, list):
        for i in range(len(aim)):
            v_key_list = copy.deepcopy(key_list)
            v_key_list.append(i)
            bfs_search(v_key_list, aim[i], v_j2, res)

    elif isinstance(aim, dict):
        for k, v in aim.items():
            if k in (
                    'v1',
                    ):
                continue
            v_key_list = copy.deepcopy(key_list)
            v_key_list.append(k)
            bfs_search(v_key_list, aim[k], v_j2, res)

    else:
        j2_value = get_value_by_key_list(key_list, v_j2)

        if aim == None:
            aim = ''
        if j2_value == None:
            j2_value = ''

        if aim != j2_value:
            key_list = map(str, key_list)
            key_list = '->'.join(key_list)
            res[key_list] = 'j1=%s,j2=%s'%(aim, j2_value)


if __name__ == '__main__':
    res = {}
    bfs_search([], j1, j2, res)
    print res

