def check_methods(dct: dict) -> None:

    if "__slots__" not in dct:
        raise ValueError("Class must have __slots__ attribute...")
    
    if "dimension" not in dct:
        raise ValueError("Class must have dimension class attribute...")