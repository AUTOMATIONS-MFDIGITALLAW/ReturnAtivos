import pyautogui as pya

from function.imgPath import get_resource_path

img_path = get_resource_path('img/incluir_processo.png')

print(f"Tentando localizar a imagem: {img_path}")
image_dimension = pya.locateOnScreen(img_path, confidence=0.8)

if image_dimension:
    print(f"✅ Imagem encontrada: {image_dimension}")
    pya.click(image_dimension)
else:
    print("❌ Imagem não encontrada!")
