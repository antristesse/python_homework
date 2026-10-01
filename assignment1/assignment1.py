# task 1
def hello():
    return "Hello!"
print(hello())

# task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Ana"))

# task 3
def calc(a, b, action = "multiply"):
    try: 
        if action == "add":
            return a + b
        elif action == "subtract":
            return a - b
        elif action =="multiply":
            return a * b
        elif action =="divide":
            return a / b
        elif action =="modulo":
                return a % b
        elif action =="int_divide":
                return a // b
        elif action =="power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
         return "You can't multiply those values!"

# task 4
def data_type_conversion(value, type):
     try: 
        if type == "int":
            return int(value)
        elif type =="float":
            return float(value)
        elif type == "str":
            return str(value)
     except ValueError:
          return f"You can't convert {value} into a {type}."

print(data_type_conversion("nonsense", "float"))

# task 5
def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
         return "Invalid data was provided."
print(grade(56,67,"gddf"))
    
# task 6
def repeat(string,count):
    result = ""
    for i in range(count):
          result = result + string
    return result

print(repeat("cat", 5))

# task 7
def student_scores(action, **kwargs):
    if action == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif action == "best":
        best_score = 0
        best_student = ""

        for key, value in kwargs.items():
            if value > best_score:
                best_score = value
                best_student = key
        return best_student

print(student_scores("mean", Ana=90, Joe=80, Anna=70))
print(student_scores("best", Ana=90, Joe=98, Anna=85))

# task 8
def titleize(string):
    words = string.split()
    little = ["a", "on", "an", "the", "of", "and", "is", "in"]
    new = ""
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            word = word.capitalize()
        else:
            if word in little:
                pass
            else:
                word = word.capitalize()
        words[i] = word
    new = " ".join(words)
    return new
print(titleize("the lord of the rings"))

# task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result = result  + letter
        else:
            result = result + "_"
    return result
print(hangman("alphabet", "ab"))

# task 10
def pig_latin(string):
    vowel = "aeiou"
    words = string.split()
    result = []

    for word in words:
        for i, letter in enumerate(word):
            if word[i:i + 2] == "qu":
                word = word[i + 2:] + word[:i + 2] + "ay"
                break
            elif letter in vowel:
                if i == 0:
                    word = word + "ay"
                else:
                    word = word[i:] + word[:i] + "ay"
                break

        result.append(word)

    return " ".join(result)

print(pig_latin("apple"))   
print(pig_latin("pig"))    
print(pig_latin("square")) 