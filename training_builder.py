from training import Training, FastTraining, SavedTraining
from utils import NOW


class BasicTrainingBuilder():
    
    def set_name(self, name):
        self.training.name = name
        return self
    
    def return_training(self):
        return self.training
        

class FastTrainingBuilder(BasicTrainingBuilder):
    
    def __init__(self):
        self.training = FastTraining()
             
    def set_name(self):
        date = NOW
        self.training.name = f"Fast_Training_{date}"
        return self        
    
    def set_series(self, series):
        self.training.series = series
        return self

    def set_work_time(self, work_time):
        self.training.work_time = work_time
        return self
    
    def set_rest_time(self, rest_time):
        self.training.rest_time = rest_time
        return self    


class SavedTrainingBuilder(BasicTrainingBuilder):
    
    def __init__(self):
        self.training = SavedTraining()
    
    def add_exercises(self, dict):
        self.training.exercises = dict


class Director():
    def __init__(self):
        self._builder = None
        
    @property
    def builder(self):
        return self._builder
        
    @builder.setter
    def builder(self, builder):
        self._builder = builder
        
    def build_fast_training(self, series, work_time, rest_time):
        self.builder.set_name()
        self.builder.set_series(series)
        self.builder.set_work_time(work_time)
        self.builder.set_rest_time(rest_time)
        training = self.builder.return_training()
        Training.add_training(training)
        
        return training
    
    def build_saved_training(self, name, dict):
        self.builder.set_name(name)
        self.builder.add_exercises(dict)
        training = self.builder.return_training()
        Training.add_training(training)
        
        return training
    
    
