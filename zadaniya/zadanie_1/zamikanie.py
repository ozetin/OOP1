def umnozhit(a, b):
    return a * b


def sozdat_zamikanie(f):
    def vnutri(a, b):
        result = f(a, b)

        return (
            f"Для значений {a}, {b} произведение = {result} "
        )

    return vnutri