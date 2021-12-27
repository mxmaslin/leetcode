class Solution:
    def firstBadVersion(self, n):
        left, middle, right = 1, n // 2, n
        for _ in range(0, n):
            righter = not (isBadVersion(middle-1) or isBadVersion(middle) or isBadVersion(middle+1))
            lefter = isBadVersion(middle-1) and isBadVersion(middle) and isBadVersion(middle+1)
            if righter:
                left = middle
                middle += max((right - left) // 2, 1)
            elif lefter:
                right = middle
                middle -= max((right - left) // 2, 1)
            else:
                found = [
                     x[0] for x in ((middle-1, isBadVersion(middle-1)), (middle, isBadVersion(middle)), (middle+1, isBadVersion(middle+1))) if x[1]
                ][0]
                return found
