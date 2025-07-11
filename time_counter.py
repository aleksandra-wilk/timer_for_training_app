import time
import sys
from utils import NOW, TODAY, clearing_line
from history import History

#TODO: Template method
class TimeCounter():
    
    @staticmethod
    def countdown(t):
        t = int(t)
        while t>=0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
            
    def fast_training_countdown(self, series, work_time, rest_time):
        for i in range(int(series)):
            clearing_line()
            print(f"Serie: {i+1}")             
            self.countdown(work_time)
            if i+1 != int(series): 
                clearing_line()
                print(f"Rest: {i+1}")
                self.countdown(rest_time)

    
