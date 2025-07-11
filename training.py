from abc import ABC, abstractmethod
from utils import WrongState


class Training():
    
    trainings = []
    
    def __init__(self):
        self.name = None
        self.series = None
        self.work_time = None
        self.rest_time = None
        self.date = None
        self.state = "Inactive"
        self.type = None
        self._observers = [] 
    

    @classmethod
    def add_training(cls, training):
        cls.trainings.append(training)
    
    @classmethod
    def print_trainings(cls):
        for training in cls.trainings:
            print(training)
            
    def print_one_fast_training(self):
        print(f"Training name: {self.name}")
        print(f"Number of sets: {self.series}")
        print(f"Set time: {self.work_time} seconds")
        print(f"Rest between sets: {self.rest_time} seconds")
        print(f"Training name: {self.name}")
        print(f"Training name: {self.name}")
        
    def print_one_saved_training(self):
        print(f"Training name: {self.name}")
        print(f"Number of exercises: {len(self.exercises)}")
        for key, value in self.exercises.items():
            print(f"Exercise {key}")
            print(f"Exercise name: {value['exercise_title']}")
            print(f"Number of sets: {value['series']}")
            print(f"Set duration: {value['work_time']}")
            print(f"Rest between sets: {value['rest_time']}")


class TrainingInterface(ABC):
    
    @abstractmethod
    def execute(self):
        raise NotImplemented(Exception)
    
    def set_state(self, state):
        if state == "Active" or state == "Inactive":
            self.state = state
        else:
            raise WrongState('State can be "Active" or "Inactive"')


class FastTraining(Training, TrainingInterface):
                   
    def __init__(self):
        super().__init__()
        self.type = "fast_training"
    
    def execute(self):
        print("Fast training executing...")
        
        
class SavedTraining(Training, TrainingInterface):
    
    def __init__(self):
        super().__init__()
        self.type = "saved_training"
        self.exercises = {}
        
    def add_exercise(self, exercise_title, series, work_time, rest_time):
        self.exercise = {
        "exercise_title": exercise_title,
        "series": series,
        "work_time": work_time,
        "rest_time": rest_time
        }
        return self.exercise
    
    def execute(self, name):
        print(f"{name} training executing...")
