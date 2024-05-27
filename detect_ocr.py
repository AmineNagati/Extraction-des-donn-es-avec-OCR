import easyocr
import json

def detect_ocr(image_path, output_json):
    # Initialiser l'ocr (fr et it)
    reader = easyocr.Reader(['fr', 'it'])

    # Lire les textes dans l'image
    result = reader.readtext(image_path)

    # Mettre les resultats dans une liste
    output_list = []
    for item in result:
        bbox, text, confidence = item
        # Convert bounding box coordinates to lists of integers
        bbox = [[int(coord) for coord in point] for point in bbox]
        output_list.append({
            "text": text, "confidence": confidence , "bounding_box": bbox,
        })

    # Sauvgarder les résultats dans un fichier json
    with open(output_json, "w") as json_file:
        json.dump(output_list, json_file, indent=4)

    print(f"Les résultats ont été sauvgardés dans : {output_json}")

if __name__ == "__main__":
    image_path = input("Entrer le chemin de votre image : ")  
    output_json = "output.json"     
    detect_ocr(image_path, output_json)
