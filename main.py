from user_choices import fast_training, saved_training, trainings_history, start_training


def main():
    
    while True:
        start_choice = input("""
            TIMER APP
            1 - Fast training
            2 - Create training
            3 - Start saved training
            4 - History
            5 - Exit
            """)

        if start_choice == "1":
            fast_training()

        elif start_choice == "2":
            saved_training()

        elif start_choice == "3":
            start_training()
            
        elif start_choice == "4":  
            trainings_history()
            
        elif start_choice == "5":
            break

        else:
            print("Incorrect choice")         
        

if __name__ == "__main__":
    
    main()



