import launch
import os

path = os.path.dirname(os.path.realpath(__file__))

launch.git_clone("https://github.com/WuZongWei6/Pixelization.git", os.path.join(path, "pixelization"), "pixelization", "b7142536da3a9348794bce260c10e465b8bebcb8")

# we remove __init__ because it breaks BLIP - takes over the directory named models which BLIP also uses.
try:
    os.remove(os.path.join(path, "pixelization", "models", "__init__.py"))
except OSError as e:
    pass
#install older gdown version to avoid download error:
!pip install gdown==4.5.4 --no-cache-dir
#download the shared files by copypasting the file identifier that comes after "https://drive.google.com/file/d/" into "https://drive.google.com/uc?id="
!gdown https://drive.google.com/uc?id=1VRYKQOsNlE1w1LXje3yTRU5THN2MGdMM
!gdown https://drive.google.com/uc?id=17f2rKnZOpnO9ATwRXgqLz5u5AZsyDvq_
!gdown https://drive.google.com/uc?id=1i_8xL3stbLWNF4kdQJ50ZhnRFhSDh3Az
