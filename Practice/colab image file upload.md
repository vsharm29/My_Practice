After executing upload dailoug comes which set files in `uploaded`. `fn` in `for` loop give name of the file as output

``` 
images = []
from google.colab import files
uploaded = files.upload()
for i in range(2):
  for fn in uploaded.keys():
    images.append(img_to_array(load_img(fn, target_size=(224, 224))))
images = np.array(images, dtype=float)
```
