 # GUI Application for Text Extraction from Images
GUI application in python which can extract texts from an image using OCR (optical character recognition). Along with image texts, the application can also recognize vehicle registration plates accurately to a certain extent.
An extra function is added to convert the extracted texts into audio files (text to speech conversion). The path of the image is needed as the input.

## Libraries Needed for Running the Script 
### Tkinter for GUI creation 
```
pip install tkinter
```
### Pytesseract for reading the text from the images
```
pip install pytesseract
```
Pytesseract needs PIL or Pillow as a prerequisite and you need to install [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract) first. 
### NumPy, cv2, imutils and Image(from PIL) for image manipulation
```
pip install numpy
```
```
pip install opencv-python
```
```
pip install imutils
```
```
pip install pillow
```
### Gtts and os for text to speech conversion.
```
pip install gTTS
```

os is a standard Python module, so you don't have to install it 

