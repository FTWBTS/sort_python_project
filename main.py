
import BubbleSort
import InsertionSort
import MergeSort
import QuickSort
import SelectionSort


def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('这是各类排序')
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", BubbleSort.bubble_sort(arr))
    print("Insertion Sort:", InsertionSort.insertion_sort(arr))
    print("Quick Sort:", QuickSort.quick_sort(arr))
    print("Selection Sort:", SelectionSort.selection_sort(arr))
    print("Merge Sort:", MergeSort.merge_sort(arr))
