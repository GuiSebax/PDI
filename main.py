import cv2
import numpy as np

def apply_low_pass_filter(image, kernel_size):
    """
    Aplica um filtro passa-baixa utilizando uma média.
    Args:
        image (np.ndarray): Imagem de entrada em escala de cinza.
        kernel_size (int): Tamanho do kernel para o filtro passa-baixa.
    Returns:
        np.ndarray: Imagem suavizada.
    """
    return cv2.blur(image, (kernel_size, kernel_size))

def high_boost_filter(image, k, kernel_size=5):
    """
    Aplica o filtro high-boost em uma imagem.
    Args:
        image (np.ndarray): Imagem de entrada em escala de cinza.
        k (float): Fator de amplificação.
        kernel_size (int): Tamanho do kernel para o filtro passa-baixa.
    Returns:
        np.ndarray: Imagem com a filtragem high-boost aplicada.
    """
    # Converte a imagem para float32
    image = image.astype(np.float32)
    
    # Aplica o filtro passa-baixa
    low_pass = apply_low_pass_filter(image, kernel_size)
    
    # Calcula a imagem high-boost
    high_boost = image + k * (image - low_pass)
    
    # Converte de volta para uint8
    high_boost = np.clip(high_boost, 0, 255).astype(np.uint8)
    
    return high_boost

# Exemplo de uso
image_path = 'Fig0340(a)(dipxe_text).tif'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Solicita ao usuário o valor de k
k = float(input("Digite o valor de k para a filtragem high-boost: "))

# Aplica a filtragem high-boost com o valor de k fornecido pelo usuário
filtered_image = high_boost_filter(image, k)

result_path = 'Imagem2.png'
cv2.imwrite(result_path, filtered_image)

print(f"Imagem processada e salva em {result_path}")
