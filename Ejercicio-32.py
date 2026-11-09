frase = "A quien madruga Dios ayuda."
for palabra in ["madruga", "Dios", "dios"]:
    if palabra.lower() in frase.lower():
        print(f"La palabra está en la frase y está en el índice {frase.lower().find(palabra.lower())}")
    else:
        print("La palabra no está en la frase")
