from cvzone.HandTrackingModule import HandDetector
import cv2
import Mode as m
import asyncio
import time
import keyboard

detector = HandDetector()
cap = cv2.VideoCapture(0)
mode = m.Mode()


class Block:
    def __init__(self,  hand1_position, hand1_1_position, result_hand):
        self.hand1_position = hand1_position
        self.hand1_1_position = hand1_1_position
        self.result_hand = result_hand
        self.status = False
        self.Button_Status = 1
        self.count_button = 1
        self.button = 0
        self.block1 = 0
        self.org1 = 0
        self.org2 = 0
        self.status_expand = 0

    def Create(self, img, block1, color, p2):
        org1 = (block1[0], block1[1])
        org2 = (block1[2], block1[3])
        # จุดทั้งหมดสี่จุดแบบออริจินอล
        org1_position = (int(org1[0]) - int(org1[1]) // 2)

        org2_position = (int(org2[0]) - int(org1[1]) // 2)
        org3_position = (int(org1[0]) - int(org2[1]) // 2)

        org4_position = (int(org2[0]) - int(org2[1]) // 2)
        cv2.rectangle(img, org1, org2, (250, color, 100), cv2.FILLED)

        if ((
                org1_position < self.hand1_position < org4_position and org3_position < self.hand1_position < org2_position) or (
                org3_position < self.hand1_position < org2_position and
                org1_position < self.hand1_1_position < org4_position)):
            cv2.rectangle(img, org1, org2, (0, 250, 0), cv2.FILLED)
            if -40 < self.result_hand < 40:
                org1 = ((int(p2[0]) - org1_position) - 50, (int(p2[1]) - org1_position) - 50)
                org2 = ((int(p2[0]) + org2_position) + 50, (int(p2[1]) + org2_position) + 50)


        button1 = (org1[0], org1[1], org2[0], org2[1])

        return button1



    def Zoom(self, img, button, color, p2, result_hand):
        org1 = (button[0], button[1])
        org2 = (button[2], button[3])
        # จุดทั้งหมดสี่จุดแบบออริจินอล
        org1_position = (int(org1[0]) - int(org1[1]) // 2)

        org2_position = (int(org2[0]) - int(org1[1]) // 2)
        org3_position = (int(org1[0]) - int(org2[1]) // 2)

        org4_position = (int(org2[0]) - int(org2[1]) // 2)
        cv2.rectangle(img, org1, org2, color, cv2.FILLED)

        async def timers():
            t1 = time.time()
            t1 = tuple(str(int(t1)))

            return t1

        if ((
                org1_position < self.hand1_position < org4_position and org3_position < self.hand1_position < org2_position) or (
                org3_position < self.hand1_position < org2_position and
                org1_position < self.hand1_1_position < org4_position)):
            cv2.rectangle(img, org1, org2, (0, 250, 0), cv2.FILLED)
            if keyboard.is_pressed('esc'):
                self.status_expand = 1
            elif self.Button_Status == 1 and self.status_expand == 0:
                cv2.rectangle(img, org1, org2, (250, 0, 0), cv2.FILLED)
                org1 = (int(p2[0]) - (result_hand + 50), int(p2[1]) - (result_hand + 50))
                org2 = (int(p2[0]) + (result_hand + 50), int(p2[1]) + (result_hand + 50))

                # org1 = ((int(p2[0]) - (result_hand - 50)) // 2, ((int(p2[1]) - (result_hand - 50))) // 2)
                # org2 = ((int(p2[0]) - (result_hand + 50)) // 2, ((int(p2[1]) - (result_hand + 50))) // 2)

            if self.Button_Status == 2 and self.count_button == 2:
                print('Heyyy')
                self.Button_Status = 1
                self.count_button = 1


        elif ((
                org1_position > self.hand1_position > org4_position and org3_position > self.hand1_position > org2_position) or (
                org3_position > self.hand1_position > org2_position and
                org1_position > self.hand1_1_position > org4_position)) and self.status_expand == 1:
            self.status_expand = 0

        print(org1[0], org1[1])
        button = (org1[0], org1[1], org2[0], org2[1])
        return button




    # def Show_Position(self, img, hand1_position):
    #
    #     cv2.putText(img, f'{hand1_position}', (100, 100), 3, 2, (255, 0, 255))
    #
    #     cv2.putText(img, f'Up : {self.status}', (10, 300), 3, 2, (255, 0, 255))
    #     cv2.putText(img, f'Down : {org4_position}', (10, 400), 3, 2, (255, 0, 255))
    #
    #     cv2.imshow('First', img)
    #     cv2.waitKey(1)

