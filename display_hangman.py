def display(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
             ---------
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
             ---------
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
             ---------
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
             ---------
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
             ---------
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
             ---------
                """,
                # hardmode empty state (6 lives)
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
             ---------
                """,
                # medium empty state (7 lives)
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
             ---------
                """,
                # easy empty state (8 lives)
                """
                   -
                   |      
                   |      
                   |    
                   |      
                   |     
             ---------
                """,
                # baby empty state (9 lives)
                """
                   
                         
                         
                       
                         
                        
             ---------
                """
    ]
    return stages[tries]