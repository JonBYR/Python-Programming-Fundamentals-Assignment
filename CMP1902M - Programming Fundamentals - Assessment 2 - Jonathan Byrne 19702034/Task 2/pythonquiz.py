from datetime import datetime #imports the datetime function from the datetime module
def questionOne(score): #for the standard quiz there are ten questions, each needing the argument score when defined
    print(lines[0][0] + " " + lines[0][1] + " " +  lines[0][2] + " " + lines[0][3] + " " + lines[0][4]) #each question is stored in a 2d array array, which needs to be sliced to get the correct question, each row from index 0-9 and each coloum from index 0-4 for the question and answers (question 1-10 respectively). After slicing the question is then printed along with it's multiple choice answers
    answerOne = input() #asks the user for an input
    answerOne = answerOne.strip() #strips the answer so that any leading/trailing characters are removed
    if answerOne == "1955": #if the player gets the correct answer, this outcome will be executed
        print("Congratulations! You got it right!") #print statement acknowleging the user got the question right
        score = score + 1 #the score variable increases by 1 for each correct answer
        questionTwo(score) #the next question will be executed with the arguement score
    else: #if the player gets the question wrong, this piece of code will be executed
        print("I'm sorry, that's wrong. The correct answer is 1955.") #print statement telling the user they were incorrect, and given them the correct answer to compare 
        questionTwo(score) #the next question will be executed with the argument score
def questionTwo(score): #all functions follow roughly the same guidelines as the one above, with a few differences that I will explain when they come up
    print(lines[1][0] + " " + lines[1][1] + " " +  lines[1][2] + " " + lines[1][3] + " " + lines[1][4])
    answerTwo = input()
    answerTwo = answerTwo.strip()
    answerTwo = answerTwo.lower() #as the answer is a word/sentence instead of a number like question one, the answer is converted to lower case. This is the same for any answers that are a word/sentence instead of an integar
    if answerTwo == "jupiter": #as the answer is in lower case the if statement is looking for a lower case answer
        print("Congratulations! You got it right!")
        score = score + 1
        questionThree(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Jupiter.")
        questionThree(score)
def questionThree(score):
    print(lines[2][0] + " " + lines[2][1] + " " +  lines[2][2] + " " + lines[2][3] + " " + lines[2][4])
    answerThree = input()
    answerThree = answerThree.strip()
    answerThree = answerThree.lower()
    if answerThree == "pod":
        print("Congratulations! You got it right!")
        score = score + 1
        questionFour(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Pod.")
        questionFour(score)
def questionFour(score):
    print(lines[3][0] + " " + lines[3][1] + " " +  lines[3][2] + " " + lines[3][3] + " " + lines[3][4])
    answerFour = input()
    answerFour = answerFour.strip()
    answerFour = answerFour.lower()
    if answerFour == "alexander fleming":
        print("Congratulations! You got it right!")
        score = score + 1
        questionFive(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Alexander Fleming.")
        questionFive(score)
def questionFive(score):
    print(lines[4][0] + " " + lines[4][1] + " " +  lines[4][2] + " " + lines[4][3] + " " + lines[4][4])
    answerFive = input()
    answerFive = answerFive.strip()
    if answerFive == "12":
        print("Congratulations! You got it right!")
        score = score + 1
        questionSix(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is 12.")
        questionSix(score)
def questionSix(score):
    print(lines[5][0] + " " + lines[5][1] + " " +  lines[5][2] + " " + lines[5][3] + " " + lines[5][4])
    answerSix = input()
    answerSix = answerSix.strip()
    answerSix = answerSix.lower()
    if answerSix == "real":
        print("Congratulations! You got it right!")
        score = score + 1
        questionSeven(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Real.")
        questionSeven(score)
def questionSeven(score):
    print(lines[6][0] + " " + lines[6][1] + " " +  lines[6][2] + " " + lines[6][3] + " " + lines[6][4])
    answerSeven = input()
    answerSeven = answerSeven.strip()
    answerSeven = answerSeven.lower()
    if answerSeven == "copper and tin":
        print("Congratulations! You got it right!")
        score = score + 1
        questionEight(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Copper and tin.")
        questionEight(score)
def questionEight(score):
    print(lines[7][0] + " " + lines[7][1] + " " +  lines[7][2] + " " + lines[7][3] + " " + lines[7][4])
    answerEight = input()
    answerEight = answerEight.strip()
    answerEight = answerEight.lower()
    if answerEight == "fungi":
        print("Congratulations! You got it right!")
        score = score + 1
        questionNine(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Fungi.")
        questionNine(score)
def questionNine(score):
    print(lines[8][0] + " " + lines[8][1] + " " +  lines[8][2] + " " + lines[8][3] + " " + lines[8][4])
    answerNine = input()
    answerNine = answerNine.strip()
    answerNine = answerNine.lower()
    if answerNine == "no charge":
        print("Congratulations! You got it right!")
        score = score + 1
        questionTen(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is No charge.")
        questionTen(score)
def questionTen(score):
    print(lines[9][0] + " " + lines[9][1] + " " +  lines[9][2] + " " + lines[9][3] + " " + lines[9][4])
    answerTen = input()
    answerTen = answerTen.strip()
    answerTen = answerTen.lower()
    if answerTen == "nitrogen":
        print("Congratulations! You got it right!")
        score = score + 1
        finalScore(score)
    else:
        print("I'm sorry, that's wrong. The correct answer is Nitrogen.")
        finalScore(score)
def finalScore(score): #the finalScore function will display the final score the user recieved out of 10 for this quiz
    print ("Congratulations! You scored a total of",score,"/10 points!")
    global userScore #a new variable is created that will be assigned the player's score and is a global variable so it can be used outside the function. This is so that the variable can be used later for the Leaderboard class
    userScore = score

def customQuestionOne(customScore): #for my custom quiz, all the functions and variables related to it will have custom in front of them. The functionality of each function is the same of the standard quiz functions, but with different names (so questionOne() and customQuestionOne() preform similarly to each other but with different names, and so on)
    print(customLines[0][0] + " " + customLines[0][1] + " " +  customLines[0][2] + " " + customLines[0][3] + " " + customLines[0][4])
    customAnswerOne = input()
    customAnswerOne = customAnswerOne.strip()
    customAnswerOne = customAnswerOne.lower()
    if customAnswerOne == "bob dylan":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionTwo(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Bob Dylan.")
        customQuestionTwo(customScore)

def customQuestionTwo(customScore):
    print(customLines[1][0] + " " + customLines[1][1] + " " +  customLines[1][2] + " " + customLines[1][3] + " " + customLines[1][4])
    customAnswerTwo = input()
    customAnswerTwo = customAnswerTwo.strip()
    customAnswerTwo = customAnswerTwo.lower()
    if customAnswerTwo == "playstation two":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionThree(customScore)
    elif customAnswerTwo == "playstation 2": #as some answers might be typed differently by people, any answer that is reasonably correct will have a seperate if statement that adds to the score. As people say both "Playstation Two" and "Playstation 2", I will accept both answers" 
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionThree(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Playstation Two.")
        customQuestionThree(customScore)
def customQuestionThree(customScore):
    print(customLines[2][0] + " " + customLines[2][1] + " " +  customLines[2][2] + " " + customLines[2][3] + " " + customLines[2][4])
    customAnswerThree = input()
    customAnswerThree = customAnswerThree.strip()
    if customAnswerThree == "1932":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionFour(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is 1932.")
        customQuestionFour(customScore)
def customQuestionFour(customScore):
    print(customLines[3][0] + " " + customLines[3][1] + " " +  customLines[3][2] + " " + customLines[3][3] + " " + customLines[3][4])
    customAnswerFour = input()
    customAnswerFour = customAnswerFour.strip()
    customAnswerFour = customAnswerFour.lower()
    if customAnswerFour == "goldeneye":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionFive(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Goldeneye.")
        customQuestionFive(customScore)
def customQuestionFive(customScore):
    print(customLines[4][0] + " " + customLines[4][1] + " " +  customLines[4][2] + " " + customLines[4][3] + " " + customLines[4][4])
    customAnswerFive = input()
    customAnswerFive = customAnswerFive.strip()
    customAnswerFive = customAnswerFive.lower()
    if customAnswerFive == "green book":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionSix(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Green Book.")
        customQuestionSix(customScore)
def customQuestionSix(customScore):
    print(customLines[5][0] + " " + customLines[5][1] + " " +  customLines[5][2] + " " + customLines[5][3] + " " + customLines[5][4])
    customAnswerSix = input()
    customAnswerSix = customAnswerSix.strip()
    customAnswerSix = customAnswerSix.lower()
    if customAnswerSix == "pokemon":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionSeven(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Pokemon.")
        customQuestionSeven(customScore)
def customQuestionSeven(customScore):
    print(customLines[6][0] + " " + customLines[6][1] + " " +  customLines[6][2] + " " + customLines[6][3] + " " + customLines[6][4])
    customAnswerSeven = input()
    customAnswerSeven = customAnswerSeven.strip()
    customAnswerSeven = customAnswerSeven.lower()
    if customAnswerSeven == "shrek":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionEight(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Shrek.")
        customQuestionEight(customScore)
def customQuestionEight(customScore):
    print(customLines[7][0] + " " + customLines[7][1] + " " +  customLines[7][2] + " " + customLines[7][3] + " " + customLines[7][4])
    customAnswerEight = input()
    customAnswerEight = customAnswerEight.strip()
    customAnswerEight = customAnswerEight.lower()
    if customAnswerEight == "electric light orchestra":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionNine(customScore)
    elif customAnswerEight == "elo": #as the band electric light orechestra is also referred to as elo I will accept that answer
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionNine(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Electric Light Orchestra.")
        customQuestionNine(customScore)
def customQuestionNine(customScore):
    print(customLines[8][0] + " " + customLines[8][1] + " " +  customLines[8][2] + " " + customLines[8][3] + " " + customLines[8][4])
    customAnswerNine = input()
    customAnswerNine = customAnswerNine.strip()
    customAnswerNine = customAnswerNine.lower()
    if customAnswerNine == "tyler, the creator":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionTen(customScore)
    elif customAnswerNine == "tyler the creator": #as tyler, the creator is also refered to as tyler the creator I will accept that answer
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customQuestionTen(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Tyler, the Creator.")
        customQuestionTen(customScore)
def customQuestionTen(customScore):
    print(customLines[9][0] + " " + customLines[9][1] + " " +  customLines[9][2] + " " + customLines[9][3] + " " + customLines[9][4])
    customAnswerTen = input()
    customAnswerTen = customAnswerTen.strip()
    customAnswerTen = customAnswerTen.lower()
    if customAnswerTen == "hideo kojima":
        print("Congratulations! You got it right!")
        customScore = customScore + 1
        customFinalScore(customScore)
    else:
        print("I'm sorry, that's wrong. The correct answer is Hideo Kojima.")
        customFinalScore(customScore)
def customFinalScore(customScore): #same functionality as the function finalScore() but for my custom quiz
    print("Congratulations! You scored a total of",customScore,"/10 points!")
    global customUserScore #this variable has the same functionality as the userScore variable, but will be used in the customLeaderboard class instead. As a result it also needs to be global
    customUserScore = customScore
class Leaderboard(): #class made for the standard quiz
    def __init__(self,file,score,name,time,date): #requires the attributes score, name, time and date to be initialised
        self.file = file
        self.score = score
        self.name = name
        self.time = time
        self.date = date
    def update(self,score,name,time,date): #after initialising the file will write the users score, name, time and date to the file everytime it is played
        try:
            self.file.write(str(self.score) + " " + self.name + " " + self.time + " " + self.date) #score has to be converted to string in order to be written to the file, else a type error is returned as the other variables are strings
            self.file.write("\n") #creates a new line for each person's score
        except TypeError: #If a type error still occurs, then this error clause is printed to alert the user something has gone wrong above. Else the score, name, time and date will be appended onto the leaderboard file, and then a new line is written
            print("Incorrect variable type used. Type Error occured")
    
    
    
class Customleaderboard(): #class made for the custom quiz, which functions the same as the Leaderboard class for the standard quiz
    def __init__(self,file,score,name,time,date): 
        self.file = file
        self.score = score
        self.name = name
        self.time = time
        self.date = date
    def update(self,score,name,time,date):
        try:
            self.file.write(str(self.score) + " " + self.name + " " + self.time + " " + self.date) 
            self.file.write("\n")
        except TypeError: 
            print("Incorrect variable type used. Type Error occured")
    

def startQuiz():
    chosenQuiz = input("Which quiz would you like to try " + name + "? Type 1 for the standard quiz, or 2 for my custom quiz!") #using the name in a string and asking what quiz they'd like to play
    chosenQuiz = chosenQuiz.strip() #stripping any leading/trailing characters
    if chosenQuiz == "1": #if the user chose the first quiz, this code will preform the steps needed to initiate that quiz
        print("Welcome to the standard quiz! Please type your answer after the question is displayed. Be sure to spell your answers correctly or it won't count!") #Instructions for the user before playing
        score = 0 #score assigned to 0, which will potentially increase in each question function
        global lines #global variable created so it can be referred to in each of the standard quiz's functions
        with open("quiz.txt") as file: #for the quiz.txt file, a 2d array is being created by splitting each line in the file (method shown below). The variable lines will then be refered to in each function to recieve it's corresponding question.
            lines = [line.split(",") for line in file]
        questionOne(score) #the first question is executed
        currentTime = datetime.time(datetime.now()) #prints the exact hour, minute, second and microsecond the quiz was completed
        currentDate = datetime.date(datetime.now()) #prints datetime.date(year, month, date)
        currentDate = currentDate.strftime("%a %d %B 20%y") #formats the date to the current day, date, month and year the quiz was completed
        currentTime = currentTime.strftime("%H" + ":" +  "%M") #formats the time to only include the hour and the minute it was completed in
        leaderboardList = [] #creates an empty list
        try:
            leaderboardAppendFile = open("leaderboard.txt", "a") #creates a variable that will open the txt file leaderboard and append the score for the standard quiz as well as the name of the user and the time and date it was completed
            quizResult = Leaderboard(leaderboardAppendFile,userScore,name,currentTime,currentDate) #the result of the quiz is used to initialise the class, which requires the file, score, name, time and date
            leaderboardResult = quizResult.update(userScore,name,currentTime,currentDate) #the leaderboard is updated with the result by calling the update method of the class, with the variables it needs
            leaderboardAppendFile.close() #closes the file
        except NameError: #if a name error exists in the code as a variable is not defined, the following error clause is printed. Else, the score, name, time and date will be appended to the leaderboard file
            print("Variable not defined. Name Error occured")
        with open("leaderboard.txt") as leaderboardFile: #opens the leaderboard file again but only to read it
            for line in leaderboardFile.readlines(): #reads each line individually so it will create a list of lists
                leaderboardList.append(line.split()) #creates a list from each line by using line.split() which will make each word a seperate entity, thus creating a list for each person that has played. The list created is then appended to the empty list leaderboardList
        leaderboardList.sort(reverse = True) #sorts the list of lists in descending order
        print(leaderboardList) #prints the sorted list for the leaderboard
        input("Press enter to quit: ") #done so the sorted leaderboard is seen before quitting
        quit() #program is terminated
    elif chosenQuiz == "2": #if the user choses the second quiz, this code will preform the steps needed to initiate that quiz
        print("Welcome to the custom quiz! Please type your answer after the question is displayed. Be sure to spell your answers correctly or it won't count!") #Instructions for the user before playing
        customScore = 0 #customScore assigned as 0 as it is a different quiz, so the variables are named differently to avoid confusion
        global customLines #global variable created so it can be referred to in each of the custom quiz's functions
        with open("myquiz.txt") as customFile: #for the myquiz.txt file (the custom quiz), a 2d array is being created by splitting each line in the file (method shown below). The variable lines will then be refered to in each function to recieve it's corresponding question
            customLines = [line.split(",") for line in customFile]
        customQuestionOne(customScore) #the first question of my quiz is then executed
        currentTime = datetime.time(datetime.now()) #prints the exact hour, minute, second and microsecond the quiz was completed
        currentDate = datetime.date(datetime.now()) #prints datetime.date(year, month, date)
        currentDate = currentDate.strftime("%a %d %B 20%y") #formats the date to the current day, date, month and year the quiz was completed
        currentTime = currentTime.strftime("%H" + ":" +  "%M") #formats the time to only include the hour and the minute it was completed in
        customLeaderboardList = [] #creates an empty list
        try:
            customLeaderboardAppendFile = open("myleaderboard.txt", "a") #creates a variable that will open the txt file myleaderboard (the custom leaderboard) and preform the same funcion as the leaderboardAppendFile variable, but for my custom quiz
            customQuizResult = Customleaderboard(customLeaderboardAppendFile,customUserScore,name,currentTime,currentDate) #the result of the quiz is used to initialise the class, which requires the file, score, name, time and date
            customLeaderboardResult = customQuizResult.update(customUserScore,name,currentTime,currentDate) #the leaderboard is updated with the result by calling the update method of the class, with the variables it needs
            customLeaderboardAppendFile.close() #closes the file
        except NameError: #if a name error exists in the code as a variable is not defined, the following error clause is printed. Else, the score, name, time and date will be appended to the leaderboard file
            print("Variable not defined. Name Error occured")
        with open("myleaderboard.txt") as customLeaderboardFile: #opens the custom leaderboard file myleaderboard.txt again but only to read it
            for line in customLeaderboardFile.readlines(): #reads each line individually so that it will create a list of lists
                customLeaderboardList.append(line.split()) #creates a list from each line by using line.split() which will make each word a seperate entity for that list, thus creating a list for each person that has played. The list created is then appended to the empty list customLeaderboardList
        customLeaderboardList.sort(reverse = True) #sorts the list of lists in descending order
        print(customLeaderboardList) #prints the sorted list for the custom leaderboard
        input("Press enter to quit: ") #done so the sorted custom leaderboard is seen before quitting
        quit() #program is terminated
    else:
        startQuiz() #if the number 1 or 2 isn't recieved, then the function will be executed again so the user can try again and choose the quiz they want to play
name = input("Hello and welcome to the python quiz! What is your name? ") #asking the user for their name   
startQuiz() #function is executed to start either one of the quizzes





    





