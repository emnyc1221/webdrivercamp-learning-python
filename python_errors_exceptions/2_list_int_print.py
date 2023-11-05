#!/usr/bin/python3

def list_int_print(lst=[], i=0):
    count = 0
    for x in range(i):
        try:
            print(f"{lst[x]:d}", end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            if isinstance(lst[x], int):
                pass
            elif isinstance(lst[x], IndexError):
                raise
    print()
    return count

if __name__=="__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_int_print(list_, 4)
    print(f"Count: {count:d}")

    list_ = [1, 2, "Camp", 5, [3, 4]]
    count = list_int_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_int_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
