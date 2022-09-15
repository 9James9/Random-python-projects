import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
difficulty = pyip.inputNum('How high do you want the numbers to go?\n', greaterThan=3)
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(1,difficulty)
    num2 = random.randint(1,difficulty)
    symbol = random.randint(0,3)
    answer = ''
    if symbol == 0:
        symbol = 'X'
        answer = num1 * num2
    elif symbol == 1:
        symbol = '+'
        answer = num1 + num2
    elif symbol == 2:
        symbol = '-'
        answer = num1 - num2
    elif symbol == 3:
        if num1 % num2 == 0:
            symbol = '/'
            answer = int(num1 / num2)
        else:
            symbol = 'X'
            answer = num1 * num2

    prompt = f'{questionNumber}: {num1}{symbol}{num2}\n'
    try:
        pyip.inputStr(prompt,allowRegexes=[f'^{answer}$'],
                            blockRegexes=[('.*','Incorrect!')],
                            timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
        print(f'Answer was {answer}')
        break
    except pyip.RetryLimitException:
        print('Out of tries!')
        print(f'Answer was {answer}')
        break
    else:
        print('Correct!')
        correctAnswers += 1
        time.sleep(0.5)
        print(f'Score: {correctAnswers}/{numberOfQuestions}')