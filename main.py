from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
print("1-Текст внизу")
print("2-Текст и внизу и вверху")
user_answer = input()
top_text = ""
bottom_text = ""
if user_answer == "1":
    bottom_text = input("Введите нижний текст:")
elif user_answer == "2":
    top_text = input("Введите верхний текст:")
    bottom_text = input("Введите нижний текст:")
else:
    print("Неправильный ввод.")
memes = ["Cat_in_the_restarant.png", "Cat_with_glasses.png", "unnamed.jpg", "mkfred.png", "under.png"]
for i in range(len(memes)):
    print(i, memes[i])

image = Image.open(memes[int(input("Введите номер картинки"))])
width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size = 100)
text = draw.textbbox((0, 0),top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font,fill="black")
draw.text(((width - text[2]) / 2,(height - text[3]) - 10), bottom_text, font=font,fill="black")
image.save("new_meme.jpg")
