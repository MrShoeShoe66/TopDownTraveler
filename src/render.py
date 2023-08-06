from copy import deepcopy

def render(map, player, color):
    if color:
        internalrendersprites = [
            ' ',
            "z",
            "W",
            "P"
        ]
    else:
        internalrendersprites = [
            ' ',
            '#',
            'W',
            'P'
        ]
    internalmap = deepcopy(map)
    output = ''
    output2 = ''
    internalmap[player[1]][player[0]] = 3
    for row in internalmap:
        for location in row:
            output2 = f'{output2}{internalrendersprites[location]} '
        output = f'{output}{output2}\n'
        output2 = ''
    internalmap[player[1]][player[0]] = 0
    return output[:-1]

''' kept in incase of later use '''

# def levelselectrender(selected, max, page):
#     output = ''

#     topbot = ''
#     midpad = ''
#     mid = ''

#     for i1 in [1,2,3,4,5]:
#         i = i1 + 5 * page
#         if i <= max:

#             if i == selected:
#                 topbot = f'{topbot}# # # # #   '
#             else:
#                 topbot = f'{topbot}- - - - -   '

#             if i == selected:
#                 midpad = f'{midpad}#       #   '
#             else:
#                 midpad = f'{midpad}-       -   '

#             if i > 99:
#                 if i == selected:
#                     mid = f'{mid}#  {i}  #   '
#                 else:
#                     mid = f'{mid}-  {i}  -   '
#             elif i > 9:
#                 if i == selected:
#                     mid = f'{mid}#   {i}  #   '
#                 else:
#                     mid = f'{mid}-   {i}  -   '
#             else:
#                 if i == selected:
#                     mid = f'{mid}#   {i}   #   '
#                 else:
#                     mid = f'{mid}-   {i}   -   '

#     output = f'{topbot}\n{midpad}\n{mid}\n{midpad}\n{topbot}'

#     return output