arr = ["101", "0000", "1", "875425"]
def solve(s):
    final_string = ("(" * int(s[0])) + f"{s[0]}" + ")" * int(s[0])
    start = int(s[0])
    for i in range(1, len(s)):
        pos = int(s[i-1]) - int(s[i])
        if s[i] == "0":
            final_string += "0"
            start = len(final_string)
            continue
        if pos > 0:
            start += pos + 1
            final_string = final_string[:start] + f"{s[i]}" + final_string[start:]
        elif pos == 0:
            final_string = final_string[:start + 1] + f"{s[i]}" + final_string[start + 1:]
            start += 1
        else:
            compromise = abs(pos)
            insert = "("*compromise + f"{s[i]}" + ")"*compromise
            final_string = final_string[:start+1] + insert + final_string[start + 1:]
            start += compromise+1
        #print(f"fin start: {start}")
    return final_string
for ele in arr:
    print("For: ", ele)
    print(solve(ele))
