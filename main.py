from PIL import Image
import os
from tkinter import filedialog, Tk, messagebox


def resize_and_crop(image_path, output_folder):
    try:
        with Image.open(image_path) as img:
            width, height = img.size

            if width > height:
                new_width = height
                new_height = height
                left = (width - new_width) / 2
                top = 0
                right = left + new_width
                bottom = new_height
            else:
                new_width = width
                new_height = width
                left = 0
                top = (height - new_height) / 2
                right = new_width
                bottom = top + new_height

            img = img.crop((left, top, right, bottom))
            img = img.resize((1080, 1080), Image.LANCZOS)

            base_name = os.path.basename(image_path)
            output_path = os.path.join(output_folder, base_name)
            img.save(output_path, "PNG")
            print(f"Imagem processada: {output_path}")
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")

def main():
    root = Tk()
    root.withdraw()

    image_files = filedialog.askopenfilenames(title="Selecione as imagens PNG", filetypes=[("PNG files", "*.png")])
    if not image_files:
        messagebox.showinfo("Nenhuma imagem selecionada", "Selecione ao menos uma imagem.")
        return

    output_folder = filedialog.askdirectory(title="Selecione a pasta de saída")
    if not output_folder:
        messagebox.showinfo("Pasta de saída não selecionada", "Selecione uma pasta de saída para as imagens.")
        return

    for image_file in image_files:
        resize_and_crop(image_file, output_folder)

    messagebox.showinfo("Processo concluído", "Todas as imagens foram redimensionadas e cortadas para 1080x1080.")


if __name__ == "__main__":
    main()
