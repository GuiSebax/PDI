import numpy as np
import cv2

def gerar_fatia_rgb(face, i):
    # Criação do cubo RGB de 256x256x256
    cubo_rgb = np.zeros((256, 256, 256, 3), dtype=np.uint8)
    cubo_rgb[:, :, :, 0] = np.arange(256).reshape(1, 1, 256)
    cubo_rgb[:, :, :, 1] = np.arange(256).reshape(1, 256, 1)
    cubo_rgb[:, :, :, 2] = np.arange(256).reshape(256, 1, 1)

    if face == 1:
        # Face 1: R = 0, fatia ao longo de R
        fatia = cubo_rgb[i, :, :, :]
    elif face == 2:
        # Face 2: R = 255, fatia ao longo de R
        fatia = cubo_rgb[255 - i, :, :, :]
    elif face == 3:
        # Face 3: G = 0, fatia ao longo de G
        fatia = cubo_rgb[:, i, :, :]
    elif face == 4:
        # Face 4: G = 255, fatia ao longo de G
        fatia = cubo_rgb[:, 255 - i, :, :]
    elif face == 5:
        # Face 5: B = 0, fatia ao longo de B
        fatia = cubo_rgb[:, :, i, :]
    elif face == 6:
        # Face 6: B = 255, fatia ao longo de B
        fatia = cubo_rgb[:, :, 255 - i, :]
    else:
        raise ValueError("Face deve estar no intervalo de 1 a 6")
    
    return fatia

def main():
   
   face = int(input("Digite o numero da face (1 a 6): "))
   i = int(input("Digite o valor de i (0 a 255): "))

   if face < 1 or face > 6:
       print("Erro: A face deve estar no intervalo de 1 a 6.")
       return

   if i < 0 or i > 255:
       print("Erro: O valor de i deve estar no intervalo de 0 a 255.")
       return
   

   fatia = gerar_fatia_rgb(face, i)
   cv2.imshow("Fatia RGB", fatia)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
       

if __name__ == '__main__':
    main()