import PyTechBrain as Ptb
import random
import time

if __name__ == '__main__':
    board = Ptb.PyTechBrain()
    # r = 0
    # g = random.randrange(0, 255)
    # b = random.randrange(0, 255)
    b = 25

    while True:
        # x = board.potencjometr_raw()
        # b = int((x / 1023) * 255)
        #
        # if b < 25 and b >= 5:
        #     board.sygnalizator_zolty("on")
        #     board.sygnalizator_zielony("off")
        # elif b >= 25:

        #     board.sygnalizator_zielony("on")
        #     board.sygnalizator_zolty("off")
        # else:
        #     board.sygnalizator_zielony("off")
        #     board.sygnalizator_zolty("off")
        #
        # print(b)
        # board.sygnalizator_czerwony("on")
        # board.buzzer_sygnal("beep")
        # time.sleep(b/50)
        #
        # board.sygnalizator_czerwony("off")
        # time.sleep(b/50)

        if b < 15 and b >= 3:
            board.sygnalizator_zolty("on")
            board.sygnalizator_zielony("off")
        elif b >= 15:
            board.sygnalizator_zielony("on")
            board.sygnalizator_zolty("off")
        else:
            board.sygnalizator_zielony("off")
            board.sygnalizator_zolty("off")
        if b<=5:
            b-=0.2
        else:
            b-=1

        print(b)
        board.sygnalizator_czerwony("on")
        board.buzzer_sygnal("beep")
        time.sleep(b/50)

        board.sygnalizator_czerwony("off")
        time.sleep(b/50)

        if b < 0.2:
            board.buzzer_sygnal("demo")
            break



        # time.sleep(.001)
        # board.PWM_modulacja(b)
        # board.RGB_czerwona(x)
        # board.RGB_zielona(g)
        # board.RGB_niebieska(b)

        # board.sygnalizator_zielony("on")
        # time.sleep(1)
        # board.sygnalizator_zielony("off")
        # board.sygnalizator_zolty("on")
        # time.sleep(1)
        # board.sygnalizator_zolty("off")
        # board.sygnalizator_zielony("off")
        # board.sygnalizator_czerwony("on")
        # time.sleep(1)
        # board.sygnalizator_zielony("off")
        # board.sygnalizator_zolty("off")
        # board.sygnalizator_czerwony("off")

