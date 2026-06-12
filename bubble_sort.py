def bubble_sort(arr):
    """
    冒泡排序算法

    每次遍历比较相邻元素，将较大的元素向后移动，
    重复这个过程直到数组有序。

    时间复杂度: O(n²)
    空间复杂度: O(1)
    稳定排序
    """
    n = len(arr)
    for i in range(n):
        # 优化：如果某轮没有发生交换，说明已经有序，提前退出
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    # 测试
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],  # 已有序
        [5, 4, 3, 2, 1],  # 逆序
        [],               # 空数组
        [42],             # 单元素
    ]

    for case in test_cases:
        original = case.copy()
        sorted_case = bubble_sort(case)
        print(f"{original} -> {sorted_case}")
