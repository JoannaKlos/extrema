def find_maxima(arr):
  """Returns the positions of the macimum values in the array arr.

  Example:
  find_maxima ([1, 2, 1])
  return [1, 2] → [1]
  find_maxima([2, 0, 0, -2, 2]) → [0, 4]
  """
 ans = []
 N = len(arr)
 for i in range(len(arr)):
     if (arr[i]>arr[i-1] and
     (i >= len(arr) or arr[i]> arr[i +1]):
     ans.append(i)
     return ans
