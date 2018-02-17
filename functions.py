from collections import defaultdict


def count(text, pattern):
    '''
        Input:
                text:String(example:ABCABCABC)
                pattern:String(example:ABC)
        Output:
                Integer(3)
    '''
    count = 0
    for i in range(0, len(text) - len(pattern)):
        subs = text[i:i + len(pattern)]
        if subs == pattern:
            count += 1
    return count


def get_frequent_pattern(text, length):
    '''
        Input:
            text:String(example:ABCABCABC)
            length:Integer(example:3)
        Output:
            String:(example:ABC)
    '''
    leaderboard = defaultdict(lambda: 0)
    most_frequent_patterns = []
    largest_frequency_count = 0
    for i in range(0, len(text) - length):
        subs = text[i:i + length]
        leaderboard[subs] += 1
        if leaderboard[subs] > largest_frequency_count:
            largest_frequency_count = leaderboard[subs]
            most_frequent_patterns = [subs]
        elif leaderboard[subs] == largest_frequency_count:
            most_frequent_patterns.append(subs)
    return ' '.join(most_frequent_patterns)
