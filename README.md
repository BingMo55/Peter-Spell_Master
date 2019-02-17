# Peter The SpelL Master - 
    It's a type-based game coded in Python using Pygame library. In this project, Peter, the Aneater, is a magcal being who has the power     to destroy zombies using magical words! Only with his words of wisdom he can save the world?!
    
    How to use:
          1.) First, you must make sure to run at least Python 3.0 and you must have the library needed to run the game.
                    Library:
                      a.) Pygame Library -  Instructions for installation  can be seen here ->                                                                                             https://www.webucator.com/blog/2015/03/installing-the-windows-64-bit-version-of-pygame/
          
          2.) There are two things you must know in order to run the code!
                      b.) Everything is seperated to different classes. Each one may be linked to some other file in the project.
                      Files in the project:
                          1.) DefenseGameUI.py = is a file that holds the GUI and runs the whole game. You can run this file only by                                                        having Pygame in the library.
                          2.) DefenseGameState.py = is a file holds the game logic for the game and utilized most of the objects and                                                           classes in the game. It runs manipulates most of the object behind the scene.
                          3.) WordProblem.py = it holds the the word needed to solve as a string type. This class has many attributes and                                                methods that keeps track if the word that is randomly generated is solved.
                          4.) Zombie.py = is an object class that holds the the Class WordProblems which is used as a part of the Zombie                                             attribute. Each zombie holds unique "word" that is used to keep track if the zombie should exist                                           or not.
                          
                          
          3.) How to play the game? What are the controls?
              Controls:
                      Keyboard Inputs: (a-z input, Enter, ESC, Space Bar)
                      1.) a-z key- this keyboard input is accepted in the input buffer. The game analyzes if each characters is following                           the path to answer the word. If not it will automatically clear it and leave the input buffer as an emoty                                 string
                      2.) Enter key- this input is used to accept the input buffer written by the player. It checks if it matches the word                           and will clear the zombie if do so else the input buffer will revert back to empty string.
                      3.) Space Bar - this input is utilized for the start and end menu in order to start the game or reset the game.
                      4.) ESC - this input is used to shutdown and force quit program.
              
              Goal of the Game:
                     Type the word that matches the current zombie and get the highest score for fighting the zombies.
