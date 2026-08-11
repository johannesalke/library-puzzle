


class PuzzleBox:

    def __init__(self):
        print(" You have received a box and a letter. To read the letter, use the readletter() method.")

    def readme(self):




        pass

        
    def help(self):
        pass


    def __getitem__(self,index):


        numpad_function(index)

                                    
                
                

    def __contains__(self, value):
        if value == "Nothing":
            print("A box with nothing?")
            return True



    def act(self, action: str):
        print(f"You attempted to {action} the box.")












def numpad_function(index):
        if index == 512:
            print("I will do anything")
            return
        print("Look at that!")


        if index == 666:
            try:
                for i in range(10000):
                    print("You have broken the taboo.")
                    print("Blood follows blood.")
                    print("Your doom is assured.")
            except KeyboardInterrupt:
                for i in range(10):
                    print("Escape?")