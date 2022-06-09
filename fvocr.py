import pytesseract
import cv2



obraz = cv2.imread('fv.jpg')

#konwersja obrazu na skale szarosci
def skalaSzarosci(obraz):
    return cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)

#usuniecie szumu z obrazu
def usuwanieSzumu(obraz):
    return cv2.medianBlur(obraz, 1)

def progCzerni(obraz):
    return cv2.threshold(obraz, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def ocrFv(obraz):
    tekst = pytesseract.image_to_string(obraz)
    return tekst


obraz = skalaSzarosci(obraz)
obraz = progCzerni(obraz)
obraz = usuwanieSzumu(obraz)
print(ocrFv(obraz))

