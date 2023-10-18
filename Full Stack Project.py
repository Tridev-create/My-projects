import time
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import PoseModule as pm
import cv2
import socket
from datetime import date
from cvzone.FPS import FPS
from gtts import gTTS
import os
from playsound import playsound


URL = 'https://192.168.1.32:8080/video'
cap = cv2.VideoCapture('Videos/1.Knees push up - Copy.mp4')

Pose_Detector = pm.PoseDetector()
data_dict = 0

sss = 800 



Pose = ['HandStand', 'Pull up']

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ('127.0.0.1', 5052)

cred = credentials.Certificate('google-services.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://diabetes-ai-app-default-rtdb.asia-southeast1.firebasedatabase.app/', # Error 4.Low to High Plank - Copy.mp4
    # 'storageBucket': "realtimedatabaseface.appspot.com"
})
def main():
    Revolution_Reps = 0
    Revolution_Sets = 0
    re = 1
    time = 0
    time_Pose = 0
    time_count = 3000 # 10S
    count = 0
    sss = 800
    data = []
    height = 720
    data_final = []
    countz = 0
    dirs = 0
    week = 1
    i = 0
    Next_Poses = 0
    current = 1
    Current = 0
    count_week = 0
    Result_week = 7
    pull_up = True
    HandStand = True
    Generate = False
    Data_final = 0
    ranks = 0


    """    mytext = "Please Up"
    audio = gTTS(text=mytext, lang="en", slow=False)
    audio.save("Up.mp3")
    os.system("start Up.mp3")"""

    List_Poses = ['HandStand', 'Pull up']
    Firebase_DB = []
    Degree_Beginners = {'Burpee': '90, 170, 90, 170','Butt kick': '90, 150, 90, 150',
                        'Knees tap': '170, 55, 170, 55','Low To High Plank': '260, 180, 260, 180',
                        'Mountain Climber': '50, 150, 50, 150', 'Regular Push up': '250, 185, 250, 185',

                        'Knees Push up': '50, 160, 300, 230', 'Bench Dip': '160, 50, 230, 300',
                        'Hiqh Plank': '160, 50, 230, 300', 'Low to High Plank': '160, 50, 230, 300',
                        'Knee Triceps Extension': '160, 50, 230, 300',

                        'W Pull': '330, 280, 330, 280', 'Y Pull': '200, 190, 200, 190',
                        'Towel Pull to the chest': '37, 160, 310, 185','Reverse Plank': '160, 50, 160, 50',

                        'Bulqaian Squat': '280, 180, 260, 200', 'Lunqe': '180, 280, 180, 280',
                        'Regular Squat': '285, 170, 285, 170', 'Glutes Bridge': '225, 170, 225, 170'
                        }

    Straight = {'Low to High Plank' : 'Low to High Plank', 'Knees Triceps Extension' : 'Knees Triceps Extension',
                'W Pull' : 'W Pull', 'Y Pull' : 'Y Pull', 'Bulgarian Squat' : 'Bulgarian Squat', 'Lunge' : 'Lunge', 'Regular Squat' : 'Regular Squat',
                'Glutes Bridge' : 'Glutes Bridge', 'Regular Push Up' : 'Regular Push Up', 'Mountain Climber' : 'Mountain Climber', 'Knees Tap' : 'Knees Tap'}

    Leg = {'Butt kick' : 'Butt kick', 'Biceps' : 'Biceps', 'Mountain Climber' : 'Mountain Climber'}

    Seconds_Pose = {'Burpee' : 'Burpee', 'Butt Kick' : 'Butt Kick', 'Knees Tap' : 'Knees Taps', 'High Plank' : 'High Plank'}

    Iso_Pose = {'High Plank' : 'High Plank','Reverse Plank' : 'Reverse Plank'}
    Count_DB = 0

    User = db.reference(f'user/Login/Username').get()
    print(User)

    #BloodSugar = db.reference(f'{User}/Blood Sugar').get()
    #Weight = db.reference(f'{User}/Weight')

    today = date.today()

    Early_Day = today.day
    Early_Month = today.month
    print(today)

    todays = f'31-7-{today.year}'
    #Data = db.reference(f'{User}/{todays}/exercise posture').get()


    #First_Generate(User, week)

    First_Generate(User, week, re, count_week)

    Weight = db.reference(f'user/Login/Weight').get()
    Height = db.reference(f'user/Login/Height').get()

    BMI = int(Weight) / ((int(float(Height))/100) * (int(float(Height)) / 100))
    print(f'OverWeighttttttttttttttttttttttttttttttttttttttttt{BMI}')

    if BMI > 23:
        print('OverWeighttttttttttttttttttttttttttttttttttttttttt')
        Over_Weight(User, week, re, count_week)

    Data = db.reference(f'{User}/Week {week}/Day 3/Exercise posture').get()
    #Data = db.reference(f'Test').get()

    """    Register_Day = db.reference(f'Register/{User}/Registered').get()
    print(Register_Day)
    Register_Day = str(Register_Day)
    day, month, year = Register_Day.split('-')
    Result_Day = int(Early_Day) - int(day)
    Result_Month = int(Early_Month) - int(month)
    if Result_Month > 0:
        Result_Day = 30 - int(day)
        Result_Day += Early_Day
        print(f'Resultttttttttttttt {Result_Day}')"""


    while True:
        success, img = cap.read()
        img = cv2.imread('Gym-Image.jpg')
        img = cv2.flip(img, 1)
        #img = cv2.resize(img, (530, 830))
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Pose_Detector.findPose(img, False)
        Position, bbox = Pose_Detector.findPosition(img, False)
        # print(Position)

        """        if Result_Day <= Result_week:
            cv2.putText(img, str(f'Week {week}'), (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            # time.sleep(10)
        else:
            # Result_Day = (30 * Result_Month) - day + Early_Day
            # Result_Month = 0
            Result_week += 7
            week += 1"""

        if len(Position) != 0:
            # sock.sendto(str.encode(str(int(percentage_Right))), serverAddressPort)

            # Reps, Sets = convert(Data, 'HandStand')
            # Result_Handstand = int(Reps) * int(Sets)
            for i in Data:
                Firebase_DB.append(i)
                print(f'eeee {Firebase_DB[0:10]}')
                if Firebase_DB[Count_DB]:  # Pose Name
                    Reps, Sets = convert(Data, f'{Firebase_DB[Count_DB]}')
                    print(Reps, Sets)
                    Result = int(float(Reps)) * int(float(Sets))
                    if int(float(Reps)) > 0 and int(float(Sets)) > 0:
                        # Convert Degree
                        Right_Down, Right_Up, Left_Down, Left_Up = convert_degree(Degree_Beginners[Firebase_DB[Count_DB]])

                        # Calculate the percent
                        if Firebase_DB[Count_DB] in Straight:
                            print(f'{Firebase_DB[Count_DB]}')
                            percentage_Right, percentage_Left = Hand_Straight(img, Right_Down, Right_Up, Left_Down,
                                                                              Left_Up,
                                                                              Reps, Sets)
                        elif Firebase_DB[Count_DB] in Leg:
                            percentage_Right, percentage_Left = Legs(img, Right_Down, Right_Up, Left_Down, Left_Up,
                                                                     Reps, Sets)
                        elif Firebase_DB[Count_DB] in Seconds_Pose:
                            percentage_Right, percentage_Left = Seconds(img, Right_Down, Right_Up, Left_Down, Left_Up,
                                                                     Reps, Sets)

                            if time_Pose >= 10000: # 20 S
                                countz += int(float(Reps))
                                time_Pose = 0

                        elif Firebase_DB[Count_DB] in Iso_Pose:
                            percentage_Right, percentage_Left = Iso(img, Right_Down, Right_Up, Left_Down, Left_Up,
                                                                    Reps, Sets)

                            if percentage_Right >= 80 and percentage_Left >= 80:
                                time_Pose += 10
                                print(f'TIme_Pose {time_Pose}')
                                if time_Pose >= 10000:
                                    countz += int(float(Reps))
                                    time_Pose = 0
                                    current = 1



                        else:
                            percentage_Right, percentage_Left = Hand(img, Right_Down, Right_Up, Left_Down, Left_Up,
                                                                     Reps, Sets)

                        cv2.putText(img, str(f'{str(Firebase_DB[Count_DB])}'), (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                    1,
                                    (0, 0, 255),
                                    2)
                        cv2.putText(img, str(f'Count: {int(countz)}'), (50, 170), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255),
                                    2)
                        Percentage = (percentage_Right + percentage_Left) / 2
                        Data_final = ((int(float(Percentage)),int(float(Reps)), int(float(Sets))), int(countz), str(ranks))
                        print(f'Dataaaaa {Data_final}')
                        sock.sendto(str.encode(str(int(Percentage))), serverAddressPort)
                        sock.sendto(str.encode(str(Data_final)), serverAddressPort)
                        if percentage_Right < 10 and percentage_Left < 10:
                            if dirs == 0:
                                countz += 0.5
                                dirs = 1
                        if percentage_Right > 95 and percentage_Left > 95:
                            if dirs == 1:
                                countz += 0.5
                                dirs = 0
                                time = 0
                                time_count = 3000

                        if countz == Result:
                            countz = 0
                            Count_DB += 1
                            ranks += 1

                        if percentage_Right <= 50 and percentage_Left <= 50 and time >= time_count:
                            time_count += 750
                            # playsound('Sounds/Warming.mp3')
                        elif 80 < percentage_Right > 50 and 80 < percentage_Right > 50 and time >= time_count:
                            print('Please Up')
                            # playsound('Sounds/Warming.mp3')
                            time_count += 750

                        """tts = gTTS('ท่าของคุณผิดองศาเล็กน้อย กรุณาปรับตามเทรนเนอร์', lang='th')
                        tts.save('hello.mp3')
                        #print('Please Down')"""

                    else:
                        Count_DB += 1
                        print('Nexttt')
                        current = 1
                        ranks += 1

                    time_Pose += 10
                    time += 10
                    print(f'TImesss: {time_Pose}')
                    # Check(img)

        cv2.imshow('Diabetes-Ai', img)
        key = cv2.waitKey(1)
        if key == 27:
            break





    cap.release()
    cv2.destroyAllWindows()

# bucket = storage.bucket()

# count = db.reference(f'user/Email').get() # Get the data from database
# print(count)
# convert(count)


ref = db.reference(f'user')  # Send the data
ref.child('count').set(sss)


def convert(data, Pose):
    Data = dict(data)
    Data = Data[Pose]
    data = str(Data)
    data = data.replace(",", "")
    data = data.replace('{', "")
    data = data.replace('}', "")
    _, Reps, _, Sets = data.split(' ')
    #print(f'Easyy{Reps} {Sets}')
    return Reps, Sets

def Hand(img, Left_Down, Left_Up, Right_Down, Right_Up, Reps, Sets, countz=0, dirs=0):
    for _ in range(len(Reps)):
        for _ in range(len(Sets)):
            Angle_Left = Pose_Detector.findAngle(img, 12, 14, 16)
            Angle_Right = Pose_Detector.findAngle(img, 11, 13, 15)

            percentage_Left = np.interp(Angle_Left, (Left_Down, Left_Up), (100, 0)) # Less to More
            percentage_Right = np.interp(Angle_Right, (Right_Up, Right_Down), (0, 100))

            percentage_Right = int(percentage_Right)
            percentage_Left = int(percentage_Left)

            #print(f'eeeeeeeee{percentage_Left}')

            cv2.putText(img, str(f'{int(percentage_Right)} %'), (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            cv2.putText(img, str(f'{int(percentage_Left)} %'), (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            fps = FPS.update(img)
            #cv2.putText(img, str(f'{int(fps)} fps'), (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)



            return percentage_Right, percentage_Left

            #print(f'Count: {countz}')
            #print(f'Dir: {dirs}')
            #print('percentage_Rightsssssssssssssssssssssssssssssssssssssssssssssssss')

def Hand_Straight(img, Left_Down, Left_Up, Right_Down, Right_Up, Reps, Sets, countz=0, dirs=0):
    for _ in range(len(Reps)):
        for _ in range(len(Sets)):
            Angle_Left = Pose_Detector.findAngle(img, 12, 14, 16)
            Angle_Right = Pose_Detector.findAngle(img, 11, 13, 15)

            percentage_Left = np.interp(Angle_Left, (Left_Up, Left_Down), (0, 100)) # Less to More
            percentage_Right = np.interp(Angle_Right, (Right_Up, Right_Down), (0, 100))

            percentage_Right = int(percentage_Right)
            percentage_Left = int(percentage_Left)

            #print(f'eeeeeeeee{percentage_Left}')

            cv2.putText(img, str(f'{int(percentage_Right)} %'), (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            cv2.putText(img, str(f'{int(percentage_Left)} %'), (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            fps = FPS.update(img)
            #cv2.putText(img, str(f'{int(fps)} fps'), (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)



            return percentage_Right, percentage_Left

            #print(f'Count: {countz}')
            #print(f'Dir: {dirs}')
            #print('percentage_Rightsssssssssssssssssssssssssssssssssssssssssssssssss')


def Legs(img, Left_Down, Left_Up, Right_Down, Right_Up, Reps, Sets, countz=0, dirs=0):
    for _ in range(len(Reps)):
        for _ in range(len(Sets)):
            Angle_Left = Pose_Detector.findAngle(img, 24, 26, 28)
            Angle_Right = Pose_Detector.findAngle(img, 23, 25, 27)

            percentage_Left = np.interp(Angle_Left, (Left_Down, Left_Up), (0, 100)) # Less to More
            percentage_Right = np.interp(Angle_Right, (Right_Down, Right_Up), (0, 100))

            percentage_Right = int(percentage_Right)
            percentage_Left = int(percentage_Left)

            #print(f'eeeeeeeee{percentage_Left}')

            cv2.putText(img, str(f'{int(percentage_Right)} %'), (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            cv2.putText(img, str(f'{int(percentage_Left)} %'), (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            fps = FPS.update(img)
            #cv2.putText(img, str(f'{int(fps)} fps'), (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)



            return percentage_Right, percentage_Left

            #print(f'Count: {countz}')
            #print(f'Dir: {dirs}')
            #print('percentage_Rightsssssssssssssssssssssssssssssssssssssssssssssssss')


def Seconds(img, Left_Down, Left_Up, Right_Down, Right_Up, Reps, Sets, countz=0, dirs=0):
    for _ in range(len(Reps)):
        for _ in range(len(Sets)):
            Angle_Left = Pose_Detector.findAngle(img, 12, 24, 26)
            Angle_Right = Pose_Detector.findAngle(img, 11, 23, 25)

            percentage_Left = np.interp(Angle_Left, (Left_Down, Left_Up), (0, 100)) # Less to More
            percentage_Right = np.interp(Angle_Right, (Right_Down, Right_Up), (0, 100))

            percentage_Right = int(percentage_Right)
            percentage_Left = int(percentage_Left)

            #print(f'eeeeeeeee{percentage_Left}')

            cv2.putText(img, str(f'{int(percentage_Right)} %'), (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            cv2.putText(img, str(f'{int(percentage_Left)} %'), (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            fps = FPS.update(img)
            #cv2.putText(img, str(f'{int(fps)} fps'), (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)



            return percentage_Right, percentage_Left

def Iso(img, Left_Down, Left_Up, Right_Down, Right_Up, Reps, Sets, countz=0, dirs=0):
    for _ in range(len(Reps)):
        for _ in range(len(Sets)):
            Angle_Left = Pose_Detector.findAngle(img, 12, 14, 16)
            Angle_Right = Pose_Detector.findAngle(img, 11, 13, 15)

            percentage_Left = np.interp(Angle_Left, (Left_Up, Left_Down), (0, 100)) # Less to More
            percentage_Right = np.interp(Angle_Right, (Right_Up, Right_Down), (0, 100))

            percentage_Right = int(percentage_Right)
            percentage_Left = int(percentage_Left)

            #print(f'eeeeeeeee{percentage_Left}')

            cv2.putText(img, str(f'{int(percentage_Right)} %'), (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            cv2.putText(img, str(f'{int(percentage_Left)} %'), (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)
            fps = FPS.update(img)
            #cv2.putText(img, str(f'{int(fps)} fps'), (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)



            return percentage_Right, percentage_Left



def convert_degree(List):
    List = str(List)
    Right_Down, Right_Up, Left_Down, Left_Up = List.split(',')

    return Right_Down, Right_Up, Left_Down, Left_Up


def Check(img):
    Angle_Right = Pose_Detector.findAngle(img, 11, 13, 15)
    Angle_Left = Pose_Detector.findAngle(img, 12, 14, 16)
    print(f'Left: {Angle_Right}')
    print(f'Left: {Angle_Left}')


def First_Generate(User, week, re, count_week):
    if re == 1:
        print(f'repoioptieroiorieotttttttttttttttttttttttttttipoiropeioptiro {re}')
        Revolution_Reps = (week / 2) * 0
        Revolution_Sets = (week / 2) * 0
        # Recently_Days = (Result_Day + 8) - (7 * week)
        ref = db.reference(User)

        refs = db.reference('user')
        # refs.child('Recently_Weeks').set(f'Week {week}')  # Set the early week
        # refs.child('Recently_Days').set(f'Days {Recently_Days}')

        for _ in range(4):
            data = {

                # 'Registered': f'{Register_Day}',

                f"Week {int(week) + count_week}":
                    {
                        'Day 1':
                            {
                                "Blood Sugar": {
                                    "Sleep": { "Sleep": 100},
                                    "Before_Workout": {"Before_Workout" : 100},
                                    "After_Workout": {"After_Workout" : 0},
                                },
                                "Exercise posture": {
                                    "Burpee": {
                                        "Reps": 10 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Regular Push Up": {
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Low to High Plank": {
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "Mountain Climber": {  # นับเป็นวินาที
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Butt kick": { # นับเป็นวินาที
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Knees Tap": { # นับเป็นวินาที
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },

                                    }
                                },
                        'Day 2' : {
                            "Blood Sugar": {
                                "Sleep": {"Sleep": 0},
                                "Before_Workout": {"Before_Workout": 0},
                                "After_Workout": {"After_Workout": 0},
                            },
                        },

                        'Day 3':
                            {
                                "Blood Sugar": {
                                    "Sleep": { "Sleep": 0},
                                    "Before_Workout": {"Before_Workout" : 0},
                                    "After_Workout": {"After_Workout" : 0},
                                },
                                "Exercise posture": {
                                    "Knees Push up": {
                                        "Reps": 1 + Revolution_Reps,
                                        "Sets": 2 + Revolution_Sets,
                                    },
                                    "Bench Dip": {
                                        "Reps": 0 + Revolution_Reps,
                                        "Sets": 0 + Revolution_Sets,
                                    },
                                    "High Plank": {  # ท่าค้างไม่จับจำนวนครั้งเเต่จับเป็นวินาที เเขนต้องตรงตลอดเวลา
                                        "Reps": 0 + Revolution_Reps,
                                        "Sets": 0 + Revolution_Sets,
                                    },
                                    "Low To High Plank": {  # ขึ้น 2 ข้างนับหนึ่ง Reps
                                        "Reps": 3 + Revolution_Reps,
                                        "Sets": 2 + Revolution_Sets,
                                    },
                                    "Knee Triceps Extension": {
                                        "Reps":2 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },

                                }
                            },
                        'Day 4':
                            {
                                "Blood Sugar": {
                                    "Sleep": { "Sleep": 0},
                                    "Before_Workout": {"Before_Workout" : 0},
                                    "After_Workout": {"After_Workout" : 0},
                                },
                                "Exercise posture": {
                                    "W Pull": {
                                        "Reps": 0 + Revolution_Reps,
                                        "Sets": 0 + Revolution_Sets,
                                    },
                                    "Y Pull": {
                                        "Reps": 12 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Towel pull up": {
                                        "Reps": 0 + Revolution_Reps,
                                        "Sets": 0 + Revolution_Sets,
                                    },
                                    "Reverse Plank": {  # ท่าค้างไม่จับจำนวนครั้งเเต่จับเป็นวินาที เเขนต้องตรงตลอดเวลา
                                        "Reps": 0 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                }
                            },
                        'Day 5':
                            {
                            "Blood Sugar": {
                                    "Sleep": { "Sleep": 0},
                                    "Before_Workout": {"Before_Workout" : 0},
                                    "After_Workout": {"After_Workout" : 0},
                            },
                                "Exercise posture": {
                                    "Bulgarain Squat": {  # 5 ครั้งต่อข้าง
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Lunge": {  # 5 ครั้งต่อข้าง
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Regular Squat": {
                                        "Reps": 10 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Glutes Bridge": {
                                        "Reps": 8 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    }
                                }
                            },
                        'Day 6': {
                            "Blood Sugar": {
                                "Sleep": 0,
                                "Before Workout": 0,
                                "After Workout": 0,
                            },
                        },
                        'Day 7': {
                            "Blood Sugar": {
                                "Sleep": 0,
                                "Before Workout": 0,
                                "After Workout": 0,
                            },
                        },
                    }
            }


            for key, value in data.items():
                ref.child(key).set(value)

            count_week += 1
        re = 100


def Over_Weight(User, week, re, count_week):
    if re == 1:
        print(f'repoioptieroiorieotttttttttttttttttttttttttttipoiropeioptiro {re}')
        Revolution_Reps = (week / 2) * 2
        Revolution_Sets = (week / 2) * 2
        # Recently_Days = (Result_Day + 8) - (7 * week)
        ref = db.reference(User)

        refs = db.reference('user')
        # refs.child('Recently_Weeks').set(f'Week {week}')  # Set the early week
        # refs.child('Recently_Days').set(f'Days {Recently_Days}')

        for _ in range(4):
            data = {

                # 'Registered': f'{Register_Day}',

                f"Week {int(week) + count_week}":
                    {
                        'Day 1':
                            {
                                "Exercise posture": {
                                    "Regular Push Up": {
                                        "Reps": 3 + Revolution_Reps,
                                        "Sets": 2 + Revolution_Sets,
                                    },
                                    "Low to High Plank": {
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "Mountain Climber": {  # นับเป็นวินาที
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Butt kick": { # นับเป็นวินาที
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "Knees Tap": { # นับเป็นวินาที
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    }
                                }
                            },
                        'Day 3':
                            {
                                "Exercise posture": {
                                    "Knees Push up": {
                                        "Reps": 10 + Revolution_Reps,
                                        "Sets": 2 + Revolution_Sets,
                                    },
                                    "Bench Dip": {
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "High Plank": {  # ท่าค้างไม่จับจำนวนครั้งเเต่จับเป็นวินาที เเขนต้องตรงตลอดเวลา
                                        "Reps": 20 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "Low To High Plank": {  # ขึ้น 2 ข้างนับหนึ่ง Reps
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "Knee Triceps Extension": {
                                        "Reps":10 + Revolution_Reps,
                                        "Sets": 2 + Revolution_Sets,
                                    }
                                }
                            },
                        'Day 4':
                            {
                                "Exercise posture": {
                                    "W Pull": {
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    },
                                    "Y Pull": {
                                        "Reps": 12 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Towel pull up": {
                                        "Reps": 15 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Reverse Plank": {  # ท่าค้างไม่จับจำนวนครั้งเเต่จับเป็นวินาที เเขนต้องตรงตลอดเวลา
                                        "Reps": 10 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    }
                                }
                            },
                        'Day 5':
                            {
                                "Exercise posture": {
                                    "Bulgarain Squat": {  # 5 ครั้งต่อข้าง
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Lunge": {  # 5 ครั้งต่อข้าง
                                        "Reps": 5 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Regular Squat": {
                                        "Reps": 10 + Revolution_Reps,
                                        "Sets": 4 + Revolution_Sets,
                                    },
                                    "Glutes Bridge": {
                                        "Reps": 8 + Revolution_Reps,
                                        "Sets": 3 + Revolution_Sets,
                                    }
                                }
                            },
                    }
            }

            for key, value in data.items():
                ref.child(key).set(value)

            count_week += 1
        re = 100

main()



Diabetes_AI-2.txt
34 KB
