#!/usr/bin/python3
"""
    A Function to check if a box can be unlocked by a key
"""


def canUnlockAll(boxes):
    """
        Arg: boxes is a list of list
    """

    if isinstance(boxes, list) and isinstance(boxes[0], list):
        locked_boxes = []
        unlock_boxes = set((boxes[0]))
        for i in range(1, len(boxes)):
            if i in unlock_boxes:
                if not isinstance(boxes[i], list):
                    return False
                unique = list(set(boxes[i]) - unlock_boxes)
                for j in range(0, len(unique)):
                    if unique[j] < len(boxes):
                        unlock_boxes.update(boxes[unique[j]])
                    if unique[j] in locked_boxes:
                        locked_boxes.remove(unique[j])
            else:
                locked_boxes.append(i)
        return not locked_boxes
    else:
        return False
