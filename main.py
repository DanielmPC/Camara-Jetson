import cv2, time

video = cv2.VideoCapture(0)

while True: 
    
    check, frame = video.read()
    print(check)
    print(frame)    

    cv2.imshow('Capturing', frame)

    #cv2.waitKey(0)

    key = cv2.waitKey(1)

    if key == ord('q'):      # Al presionar q la ventana se cierra
        break 


# Apagar la camara
video.release()
cv2.destroyAllWindows()

