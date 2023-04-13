
def get_preffered_option(task1, task2):
    if task1.description == "wash dishes" and task2.description == "cook dinner":
        return task1 
    elif task1.description == "wash dishes" and task2.description == "clean window":
        return task2
    elif task1.description == "cook dinner" and task2.description == "clean window":
        return task1


   