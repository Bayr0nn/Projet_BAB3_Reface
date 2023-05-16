import cv2 #Import de la librairie OpenCV


img = cv2.imread('input_path') #Lecture du fichier en mettant le chemin d'acces en parametres

# 1) Contours

blurred_image = cv2.medianBlur(img,105) # Reduire le bruit dans l'image de base 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Conversion en nuances de gris
gray = cv2.medianBlur(gray,7) # Reduire le bruit dans l'image
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,9) # Binerisation de l'image

# 2) Cartoon 
cartoon = cv2.bitwise_and(blurred_image,blurred_image,mask=edges)


cv2.imshow("Image",edges) # Afficher les contours
cv2.imshow("Cartoon",cartoon) # Afficher l'image Cartoon
cv2.waitKey(0) # Attendre une action
cv2.destroyAllWindows()
cv2.imwrite("output_path",cartoon) # Ecriture de l'image
