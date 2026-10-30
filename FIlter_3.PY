import cv2
import random
import time

cap = cv2.VideoCapture(0)
while True:
    ret,frames = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 0, 255)
    
    selection = random.randint(1,5)
    
    

    if selection == 1:

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        inv = 255 - gray 
        blur = cv2.GaussianBlur(inv, (25, 25), 0)
        div = cv2.divide(gray, 255 - blur, scale=256)
        skecth = cv2.cvtColor(div, cv2.COLOR_GRAY2BGR)
        skecth[:,:,0] = div
        skecth[:,:,1] = div
        skecth[:,:,2] = div

    black = edges * 0
    cycle = int(time.time() * 3) % 3
    if cycle == 0:
        neon_line = cv2.merge((black,edges,black))
    if cycle == 1:
        neon_line = cv2.merge((edges,black,edges))
    else:
        neon_line = cv2.merge((black,black,edges))

    neon_filter = frames
    neon_filter = cv2.add(neon_filter, neon_line)

    

    cv2.imshow("Sketch filter", neon_filter)

    key = cv2.waitKey(20) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    




