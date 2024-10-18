class LinQingLionCat:
    def __init__(my, Arm_length: float, Leg_length: float, Number_of_eye: int, has_tail: bool, is_furry: bool):
        my. Arm_length = Arm_length
        my.Leg_length = Leg_length
        my.Number_of_eye = Number_of_eye
        my.has_tail = has_tail
        my.is_furry = is_furry
    def describe(my):
            print("LinQing Lion Cat Physical Characteristics:")
            print(f"Arm length: {my.Arm_length} cm")
            print(f"Leg length: {my.Leg_length} cm")
            print(f"Number of eyes: {my.Number_of_eye}")
            print(f"Has a tail: {'Yes' if my.has_tail else 'No'}")
            print(f"Is furry: {'Yes' if my.is_furry else 'No'}")
myLinQing_Lion_Cat = LinQingLionCat(Arm_length=33.5, Leg_length=35.0, Number_of_eye=2, has_tail=True, is_furry=True)
myLinQing_Lion_Cat.describe()