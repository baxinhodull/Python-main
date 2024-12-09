while True:
    
    fruta = input("Digite o nome de uma fruta").strip().lower()

    
    if not fruta:
        print("Por favor, digite o nome de uma fruta válida.")
        continue

   
    if fruta == "sair":
        print("Você escolheu sair. Até a próxima!")
        break

   
    if fruta == "uva":
        print(f"Parabéns! Você acertou a fruta. Você digitou '{fruta}'!")
        break  

   
    else:
        print(f"A fruta '{fruta}' não é a correta. Tente novamente!")
