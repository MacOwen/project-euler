ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

two_digit_words = []
for i in range(10):
    two_digit_words.append(ones[i])
for i in range(10):
    two_digit_words.append(teens[i])
for i in range(1,9):
    for j in range(10):
        two_digit_words.append(tens[i]+ones[j])

three_digit_words = []
three_digit_words += two_digit_words
for i in range(1,10):
    for j in range(100):
        word = ones[i]+"hundred"
        if j > 0:
            word += "and"+two_digit_words[j]
        three_digit_words.append(word)

three_digit_words.append("one"+"thousand")

ans = 0

three_digit_words.remove("")
for word in three_digit_words:
    ans += len(word.replace(' ',''))

print(ans)
