# Cartoon

import cv2


def cartoon(image):
    blurred_image = cv2.medianBlur(image,5) # Reduire le bruit dans l'image de base 

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Conversion en nuances de gris
    gray = cv2.medianBlur(gray,3) # Reduire le bruit dans l'image
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,3) #Ressortir les bordures des objets
    cartoon = cv2.bitwise_and(blurred_image,blurred_image,mask=edges) # Utiliser l'operation de table "ET" sur les pixels de l'image et du masque
    return cartoon

def edges(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,3) # Reduire le bruit dans l'image
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,3)
    return edges

# Via la webcam 
video_capture = cv2.VideoCapture(0) # Creation d'un objet video_capture qui permet de gérer les flux vidéos

if (video_capture.isOpened() == False): #check si l'ouverture se fait correctement
      print("Error opening the video file")
      
while True:
    _, frame = video_capture.read() # read() renvoie un bool et le frame à un instant donné
    canvas = cartoon(frame)
    cv2.imshow('Video', canvas) # Afficher l'image
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
video_capture.release() # Fermeture de la webcam

cv2.destroyAllWindows()

# Pour une vidéo externe
vid_capture = cv2.VideoCapture("/Users/don_williams09/Downloads/Reface Project/IMG_7968.MOV")
 
if (vid_capture.isOpened() == False):
  print("Error opening the video file")
 
while(vid_capture.isOpened()):
    
  ret, frame = vid_capture.read()
  if ret == True:
    cart = cartoon(frame)
    cv2.imshow('Frame',cart)
    key = cv2.waitKey(20) # 
    if key == ord('q'):
      break
  else:
    break