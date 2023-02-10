def game(heap, moves, to):
    if heap >= 165:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap + 1, moves + 1, to),
         game(heap + 4, moves + 1, to),
         game(heap * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'19: {[s for s in range(1, 165) if game(s, 0, 2) and not game(s, 0, 1)]}')
print(f'20: {[s for s in range(1, 165) if game(s, 0, 3) and not game(s, 0, 1)]}')
print(f'21: {min(s for s in range(1, 165) if game(s, 0, 4) and not game(s, 0, 2))}')
