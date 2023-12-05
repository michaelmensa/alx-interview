#!/usr/bin/python3
'''
Module - lockboxes: alx interview question.
'''


def canUnlockAll(boxes):
    '''
    params: boxes - a list of lists

    a key with the same number as a box opens that box
    returns True if all boxes can be opened, otherwise False
    '''
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
