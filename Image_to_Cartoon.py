import cv2 #Import de la librairie OpenCV


img = cv2.imread("/Users/don_williams09/Downloads/Reface Project/hysacam.jpg") #Lecture du fichier en mettant le chemin d'acces en parametres

# 1) Contours

blurred_image = cv2.medianBlur(img,15) # Reduire le bruit dans l'image de base 


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Conversion en nuances de gris
gray = cv2.medianBlur(gray,5) # Reduire le bruit dans l'image
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3) # Detection des contours

# 2) Cartoon 
cartoon = cv2.bitwise_and(blurred_image,blurred_image,mask=edges)

cv2.imshow("Image",img)
cv2.imshow("Edges",edges)
cv2.imshow("Cartoon",cartoon) # Afficher l'image
cv2.waitKey(0) # Attendre une action
cv2.destroyAllWindows()
cv2.imwrite("/Users/don_williams09/Downloads/Reface Project/hysacam_cartoon.jpg",cartoon) # Ecriture image
cv2.imwrite("/Users/don_williams09/Downloads/Reface Project/hysacam_edges.jpg",edges)