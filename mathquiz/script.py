import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    # symbol = random.randint(0,3)
    # if symbol == 0:
    #     symbol = 'X'
    # elif symbol == 1:
    #     symbol = '/'
    # elif symbol == 2:
    #     symbol = '+'
    # elif symbol == 3:
    #     symbol = '-'
    symbol = 'X'
    prompt = f'{questionNumber}: {num1}{symbol}{num2}\n'
    try:
        pyip.inputStr(prompt,allowRegexes=[f'^{num1 * num2}$'],
                            blockRegexes=[('.*','Incorrect!')],
                            timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
        time.sleep(0.5)
        print(f'Score: {correctAnswers}/{numberOfQuestions}')
    