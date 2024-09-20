def recherche_binaire(arr, target):
    min, max = 0, len(arr) - 1
    while min <= max:
        print(".", end="")
        pivot = (min + max) // 2
        if arr[pivot] == target:
            return pivot
        elif arr[pivot] < target:
            min = pivot + 1
        else:
            max = pivot - 1
    return -1  # Si la valeur n'est pas trouvée

tableau = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(recherche_binaire(tableau, 7))  # Sortie : 7
