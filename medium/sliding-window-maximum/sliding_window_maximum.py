from collections import deque

def sliding_window_max(nums, k):
    if not nums:
        return []

    result = []
    dq = deque()  # stores indices

    for i in range(len(nums)):
        # remove indices out of current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # remove smaller numbers at the end
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # add max to result (front of deque)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Example test
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sliding_window_max(nums, k))  # [3,3,-1,3,5,6,7]
