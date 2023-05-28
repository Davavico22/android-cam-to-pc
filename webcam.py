import cv2
import numpy as np
import urllib.request


class Video:
    
    def  __init__(self, url, img_width=0, img_height=0):
        self.img_width = img_width
        self.img_height = img_height
        self.url = url

    def show(self):
        while True:
            frame = self.download()
            self.render(frame)

            if cv2.waitKey(1) == 27:
                break
            # if cv2.waitKey(1) & 0xFF == ord('|'):
                # break

        cv2.destroyAllWindows()

    def render(self, frame):
        frame = cv2.imdecode(frame, -1)
        if self.img_height != 0 and self.img_width != 0:
            frame = self.resize(frame)
        cv2.imshow('cam', frame)

    def download(self):
        frame = urllib.request.urlopen(self.url)
        return np.array(bytearray(frame.read()), dtype=np.uint8)

    def resize(self, frame):
        return cv2.resize(frame, dsize=(self.img_width, self.img_height), interpolation=cv2.INTER_CUBIC)


if __name__ == '__main__':

    # type in your cam ip
    # if you don't want to resize image leave
    # `img_width` and `img_height` at 0
    print("Selecciona un número:")
    print("1) 153  2) 140  3) otro a introducir")
    entrada = int(input())
    print(entrada)
    ip = 0
    if entrada == 1:
        ip = 153
    elif entrada == 2:
        ip = 128
    elif entrada == 3:
        ip = input("Introduce el endpoint: ")
    url = 'http://192.168.1.'+str(ip)+':8080/shot.jpg'
    print(url)
    img_width = 0
    img_height = 0

    video = Video(url, img_width, img_height)
    video.show()
