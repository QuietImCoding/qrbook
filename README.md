# qrbook
Break files up into multiple parts and then create qr codes for these parts. The idea is to see how much information can be printed on a single page. Makes for cool gifs.

## Setup ##

  * Check the Pipfile for dependencies, since they might grow a bit.
  Right now, they are
      * pypng
      * pyqrcode
      * progress
  * Pyqrcode is sort of an old package and has been known to get a little bit crazy with breaking. As such, I read most of their source code and realized that something's wrong with the way it chooses a size for the QR code. I added a small patch so you can just copy pyqrcode_init.py over the __init__.py file in the package... Don't blame me blame the package?
  * You want to make a directory called qrcodes/ in the same directory as your file. This is where the qrcodes go before they get stitched together
  * Get imagemagick installed, it's referenced by a system() command and I didn't want to use PIL(low?). You can do this on MacOS with homebrew. If you're on Windows... good luck!!
