class Clock:
    def __init__(self):  # initialising the clock time with hours, minutes and seconds set to None
        self.hours = None
        self.minutes = None
        self.seconds = None

    def setHours(self):
        self.hours = int(input('Set hour(s) on clock: '))  
        while self.hours > 23:  
            print('Hour(s) cannot be more than 23!')
            self.hours = int(input('Set hour(s) on clock: '))
        return

    def setMinutes(self):
        self.minutes = int(input('Set minute(s) on clock: '))  # getting user input for minutes
        while self.minutes > 59:  # if hours more than 59, print error message and prompt for minute
            print('Minute(s) cannot be more than 59!')
            self.minutes = int(input('Set minute(s) on clock: '))
        return

    def setSeconds(self):
        self.seconds = int(input('Set second(s) on clock: '))  # getting user input for seconds
        while self.seconds > 59:  # if hours more than 59, print error message and prompt for second
            print('Second(s) cannot be more than 59!')
            self.seconds = int(input('Set second(s) on clock: '))
        return

    def setTime(self):  # setTime method that calls setHours, setMinutes and setSeconds methods
        print('Please set clock values in 24-Hour format.')
        self.setHours()
        self.setMinutes()
        self.setSeconds()
        return

    def showTime(self):  # showTime method that prints time that was set
        print('Time set is: ' + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))
        return


print('Creating new ClockTime object...')
Clock = Clock()
Clock.setTime()
Clock.showTime()
