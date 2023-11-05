#!/usr/bin/python3

def divide_list_safe(list_1, list_2, list_len):
    result_list = []
    for i in range(list_len):
        result = 0
        try:
            # Check if the element is integer or float
            if not isinstance(list_1[i], (int, float)):
                print("wrong type")
                raise ValueError
            if not isinstance(list_2[i], (int, float)):
                print("wrong type")
                raise ValueError
            result = list_1[i] / list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except ValueError:
            pass
        finally:
            result_list.append(result)
    return result_list

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
