workoutList = []

while True:
    addOrDone = input("Enter DONE if finished, otherwise enter ADD to add another exercise to the list ")
    newExercise = input("Enter a new exercise (enter DONE when finished): ")
    if newExercise == "DONE":
            composeList()
            break       
    newSets = input(f"How many sets of {newExercise}? ")
    newReps = input("How many reps in each set? ")
    newWeight = input("What weight? ")

    def addExercise(addOrDone, xrcs, sets, reps, weight):
        workoutList.append([addOrDone, xrcs, sets, reps, weight])

    def composeList():
        for i in workoutList:
            print("")
            print("Excercise: " + str(i[0]))
            print("Sets: " + str(i[1]))
            print("Reps: " + str(i[2]))
            print("Weight: " + str(i[3]))
            print("")

    addExercise(addOrDone, newExercise, newSets, newReps, newWeight)

 