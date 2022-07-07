length = int(input())
width = int(input())
total_pieces = length * width
remaining_pieces = total_pieces
cake_is_finished = False

while remaining_pieces > 0:
    piece = input()
    if piece == "STOP":
        break
    remaining_pieces -= int(piece)

if remaining_pieces <= 0:
    cake_is_finished = True

if cake_is_finished:
    needed_pieces = total_pieces - (total_pieces + remaining_pieces)
    print(f"No more cake left! You need {needed_pieces} pieces more.")
else:
    print(f"{remaining_pieces} pieces are left.")
