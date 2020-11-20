print('''
        distance
speed = --------
          Time
''')

print("")

print('''
        distance
Time  = --------
         Speed

''')

print('''

distance = speed x Time

''')
print('''
--------------------------------------------------------------------------------
                                   |NOTE|

                         To open CMS again write CMS.
--------------------------------------------------------------------------------
''')
while True:
    a = input("What to find out? :")

    if "speed" in a or "s" in a or "Speed" in a:
        distance = int(input("Distance:"))
        time = int(input("Time:"))

        print("Speed = ", distance / time)

    elif "Time" in a or "t" in a or "time" in a:
        dis = int(input("Distance: "))
        spe = int(input("Speed: "))

        print("Time = ", dis / spe)

    elif "distance" in a or "d" in a or "Distance" in a:
        s = int(input("Speed: "))
        t = int(input("Time: "))

        print("Distance = ", s * t)

    elif "CMS." in a or "CMS" in a or "cms." in a or "cms" in a or "Cms" in a or "Cms." in a:
        from subprocess import *
        Popen('python Program.py')
        quit

    else:    
        print("Not, recognized.")