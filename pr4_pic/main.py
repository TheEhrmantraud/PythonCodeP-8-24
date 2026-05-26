import os
import time
import multiprocessing
from PIL import Image


INPUT_DIR = "C:/Users/12/Downloads/МПТфайлы/PROJECTbyMPT/my_projectPython/pr4_pic/test_images"
OUTPUT_DIR = "C:/Users/12/Downloads/МПТфайлы/PROJECTbyMPT/my_projectPython/pr4_pic/processed"



def create(num_images):
    #генерация изображений
    os.makedirs(INPUT_DIR, exist_ok=True)
    images = []
    for i in range(num_images):
        #цветное изображение
        img = Image.new('RGB', (1920, 1080), color=(i * 10 % 255, 150, 200))
        filepath = os.path.join(INPUT_DIR, f"img_{i}.jpg")
        img.save(filepath)
        images.append(filepath)
    return images



def process(filepath):
    #обработка изображения
    filename = os.path.basename(filepath)
    out_path = os.path.join(OUTPUT_DIR, f"out_{filename}")
    
    with Image.open(filepath) as img:
        img = img.transpose(Image.ROTATE_270)
        
        #изменение размера
        img = img.resize((800, 600), Image.LANCZOS)
        
        #в оттенки серого Luminous
        img = img.convert('L')
        
        #сохранение результата
        img.save(out_path)












def main():
    #папки и тестовые картинки
    print("Генер изображений")
    image_files = create(30)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    #очищаем папку processed перед тестам, если там чтото было
    for f in os.listdir(OUTPUT_DIR):
        os.remove(os.path.join(OUTPUT_DIR, f))





    print("Последовательная обработка")
    start_time = time.time()
    
    for img_path in image_files:
        process(img_path)
        
    time_end = time.time() - start_time
    print(f"Последовательная обработка заняла: {time_end:.2f} сек")






    print("Параллельная обработка")
    start_time_par = time.time()
    
    # pool использует количество процессов которое равное количеству ядер так что у нас по факту эффективный юз мощностей пк
    with multiprocessing.Pool() as pool:
        pool.map(process, image_files)
        
    par_time = time.time() - start_time_par
    print(f"Параллельная обработка заняла: {par_time:.2f} сек")






    if par_time < time_end:
        speedup = time_end / par_time
        print(f"\nПараллельная обработка оказалась быстрее в {speedup:.1f} раз")

if __name__ == "__main__":
    main()