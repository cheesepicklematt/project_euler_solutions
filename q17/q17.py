def number_to_words(number):
    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    teens = [
        "ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    if number == 1000:
        return "one thousand"
    if number < 10:
        return ones[number]

    if number < 20:
        return teens[number - 10]

    if number < 100:
        return tens[(number // 10) - 1] + (" " + ones[number % 10] if (number % 10) != 0 else "")
    else:
        hundreds = ones[int(str(number)[0])] + "hundred"
        tensNum = str(number)[1:]
        if 10<int(tensNum)<20:
            p1 = 'and'+teens[int(tensNum) - 10]
        else:
            tenWord = '' if int(tensNum[0])==0 else tens[int(tensNum[0])-1]
            oneWord = '' if int(tensNum[1])==0 else ones[int(tensNum[1])]
            p1 = 'and'+tenWord + oneWord if tenWord + oneWord !='' else ''

        return hundreds+p1

totalChar = 0
tmpList = []
for n in range(1,1001):
    tmpStr = number_to_words(n).replace(' ','').replace('-','')
    totalChar += len(tmpStr)

    tmpList.append(tmpStr)
