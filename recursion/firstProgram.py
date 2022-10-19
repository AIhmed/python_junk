def rec(value):
    if value==0:
        return value
    else:
        out=rec(value-1)
        print(f"getting out of call where value == {value} and output == {out}\n")
        return out
rec(10)
