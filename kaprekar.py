# ==============================================================================
# PROJETO: ROTINA DE KAPREKAR (CONSTANTES 6174 E 495)
# AUTOR: Leonardo Lima de Oliveira
# ==============================================================================

print("=== ROTINA DE KAPREKAR ===")
print("Escolha a quantidade de dígitos para testar:")
print("3 - Para números de 3 dígitos (Constante 495)")
print("4 - Para números de 4 dígitos (Constante 6174)")
opcao_digitos = int(input("Digite sua opção (3 ou 4): "))

if opcao_digitos != 3 and opcao_digitos != 4:
    print("Erro: Opção inválida. Escolha apenas 3 ou 4.")
else:
    # Captura da entrada do usuário
    numero_original = int(input(f"Informe um número de {opcao_digitos} dígitos: "))

    # 1. VALIDAÇÃO DE TIPO E SINAL (Inteiro e Positivo)
    # Nota: A conversão int(input()) garante o tipo inteiro.
    if numero_original < 0:
        print("Erro: O número informado deve ser positivo.")
    else:
        # 2. VALIDAÇÃO DE FAIXA
        limite_superior = 9999 if opcao_digitos == 4 else 999
        if numero_original > limite_superior:
            print("Erro: O número informado está fora da faixa permitida.")
        else:
            # Inicialização de variáveis para o laço iterativo
            numero_atual = numero_original
            constante_alvo = 6174 if opcao_digitos == 4 else 495
            iteracao = 0
            executar_rotina = True

            print(f"\nNúmero informado: {numero_atual}")

            # Se o número já for a própria constante, valida mas não precisa iterar
            if numero_atual == constante_alvo:
                print(f"Constante de Kaprekar ({constante_alvo}) atingida em 0 iterações.")
                executar_rotina = False

            while executar_rotina:
                # Extração dos dígitos puramente por matemática
                if opcao_digitos == 4:
                    d1 = numero_atual // 1000
                    d2 = (numero_atual // 100) % 10
                    d3 = (numero_atual // 10) % 10
                    d4 = numero_atual % 10
                else:  # 3 dígitos
                    d1 = numero_atual // 100
                    d2 = (numero_atual // 10) % 10
                    d3 = numero_atual % 10
                    d4 = -1 # Desativado para o caso de 3 dígitos

                # 3. VALIDAÇÃO DE REPETIÇÃO DE DÍGITOS
                # Proibido mais de 2 dígitos iguais. 
                # Se houver 3 ou mais iguais, o número é inválido.
                invalido = False
                if opcao_digitos == 4:
                    if ((d1 == d2 and d1 == d3) or (d1 == d2 and d1 == d4) or 
                        (d1 == d3 and d1 == d4) or (d2 == d3 and d2 == d4)):
                        invalido = True
                else: # 3 dígitos (repdigit completo: ex 111, 222)
                    if d1 == d2 and d1 == d3:
                        invalido = True

                if invalido:
                    print("Erro: O número possui muitos dígitos repetidos.")
                    break

                # ORDENAÇÃO DOS DÍGITOS (Algoritmo de Troca Simples sem Listas)
                # Para ordenar de forma crescente e decrescente usando apenas ifs aritméticos
                if opcao_digitos == 4:
                    # Garantir ordenação decrescente em variáveis temporárias (maior para o menor)
                    # Compara d1 com os outros
                    if d1 < d2: t = d1; d1 = d2; d2 = t
                    if d1 < d3: t = d1; d1 = d3; d3 = t
                    if d1 < d4: t = d1; d1 = d4; d4 = t
                    # Compara d2 com os restantes
                    if d2 < d3: t = d2; d2 = d3; d3 = t
                    if d2 < d4: t = d2; d2 = d4; d4 = t
                    # Compara d3 com d4
                    if d3 < d4: t = d3; d3 = d4; d4 = t

                    # Montagem do NDD (Número Dígitos Decrescentes) e NDC (Crescentes)
                    ndd = (d1 * 1000) + (d2 * 100) + (d3 * 10) + d4
                    ndc = (d4 * 1000) + (d3 * 100) + (d2 * 10) + d1
                else:
                    # Ordenação para 3 dígitos
                    if d1 < d2: t = d1; d1 = d2; d2 = t
                    if d1 < d3: t = d1; d1 = d3; d3 = t
                    if d2 < d3: t = d2; d2 = d3; d3 = t

                    ndd = (d1 * 100) + (d2 * 10) + d3
                    ndc = (d3 * 100) + (d2 * 10) + d1

                # 4. SUBTRAÇÃO
                resultado = ndd - ndc
                iteracao += 1

                # Exibição do passo atual conforme modelo do edital
                print(f"Iteração {iteracao}: {ndd} - {ndc} = {resultado}")

                # 5. CONDIÇÃO DE PARADA / ITERAÇÃO
                if resultado == constante_alvo:
                    print(f"\nConstante de Kaprekar ({constante_alvo}) atingida em {iteracao} iterações.")
                    executar_rotina = False
                else:
                    numero_atual = resultado
                    # Salvaguarda para evitar loops infinitos caso algo dê errado
                    if iteracao >= 7 and opcao_digitos == 4:
                        executar_rotina = False
                    elif iteracao >= 6 and opcao_digitos == 3:
                        executar_rotina = False
