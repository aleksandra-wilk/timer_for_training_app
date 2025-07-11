# from observer import Observer
from utils import TODAY 


#TODO: Singleton, Observer


class History():

    def __init__(self):
        self.trainings_history = {}

    def update(self, training):
        self.trainings_history[str(TODAY)] = training
        print(f"[History] Saved training with date {TODAY}")

    def display_training_by_day(self, day):
        training = self.trainings_history[day]
        print("Training name: " + training.name)
        print("Number of sets: " + training.series)
        print("Set duration: " + training.work_time)
        print("Rest time: " + training.rest_time)
        print("Training execution date: " + training.date)

            
