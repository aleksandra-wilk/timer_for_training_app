from training_builder import FastTrainingBuilder, SavedTrainingBuilder, Director
from training import Training
from time_counter import TimeCounter
from history import History
from datetime import datetime

director = Director()
time_counter = TimeCounter()
history = History()
history2 = History()

def fast_training():
    fast_training_builder = FastTrainingBuilder()
    director.builder = fast_training_builder
    
    series = input("Select number of sets:\n")
    work_time = input("Enter set duration (in seconds):\n")
    rest_time = input("Enter rest duration (in seconds):\n")
    fast_start = input(f"""
                        * Fast Training - Summary *
                        Sets: {series}
                        Set duration: {work_time} seconds
                        Rest duration: {rest_time} seconds

                        Start fast training? yes/no\n""")
    
    fast_training = director.build_fast_training(series=series, work_time=work_time, rest_time=rest_time)
    Training.print_trainings()
    
    if fast_start == "yes":
        time_counter.fast_training_countdown(series=series, work_time=work_time, rest_time=rest_time)
        
def saved_training():
    n = 1
    exercises_dict = {}
    
    training_name = input("Enter training name:\n")
    
    while True:
        
        saved_training_builder = SavedTrainingBuilder()
        director.builder = saved_training_builder
        
        print(f"Exercise {n}")
        exercise_title = input("Enter exercise title:\n")
        series = input("Enter number of sets:\n")
        work_time = input("Enter set duration (in seconds):\n")
        rest_time = input("Enter rest duration (in seconds):\n")
        
        exercise = saved_training_builder.training.add_exercise(exercise_title, series, work_time, rest_time)

        exercises_dict[n] = exercise
        
        n += 1

        next_exercise = input("Do you want to add another exercise? Y/N\n")
        
        if next_exercise == "N":
            saved_training = director.build_saved_training(name=training_name, dict=exercises_dict)
            print(f"Training {training_name} saved -> {saved_training}")
            break
        
def trainings_history():
    print("Training history")
    day_input = input("Enter the date of the training: YYYY-MM-DD\n")
    history.display_training_by_day(str(day_input))
    
def start_training():
    print("Starting training")
