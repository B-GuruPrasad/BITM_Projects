from collections import Counter
def min_steps_to_magic_string(s):
    if len(set(s))==1:
        return 0
    freq=Counter(s)
    max_freq=max(freq.values())
    return len(s)-max_freq
S=input()
result=min_steps_to_magic_string(S)
print(result)