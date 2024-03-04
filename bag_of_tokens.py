def bag_of_tokens_score(tokens, power):
    """
    A greedy algorithm to maximize score.
    Time complexity O(nlogn)
    sorting, itereates over the tokens one (each iteration constant time)
    :type tokens: List[int]
    :type power: int
    :rtype: int
    """
    score = 0
    tokens.sort()  # Sort tokens from smallest to largest
    left, right = 0, len(tokens) - 1

    while left <= right:
        if power >= tokens[left]:
            score += 1
            power -= tokens[left]
            left += 1
        elif score > 0 and left + 1 <= right:  # Play face-down if score is positive and there
            # left enough future move such it will be worth it
            score -= 1
            power += tokens[right]
            right -= 1
        else:
            break  # No more moves possible

    return score

if __name__=='__main__':
    tokens_tests = [ [100], [200,100], [100, 300, 400, 200]]
    power_tests = [50, 150, 200]
    expected = [0, 1, 2]
    for i in range(3):
        print("expected: ", expected[i], " got: ", bag_of_tokens_score(tokens_tests[i], power_tests[i]))