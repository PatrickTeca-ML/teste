from Alpha2 import df2
# Função para formatar os nomes dos países


def format_country_name(country_name):
    """
    Formata o nome dos países para o formato esperado pelas URLs:
    - Minúsculas
    - Substitui espaços por hífens
    - Remove caracteres especiais (opcional)
    """
    formatted_name = country_name.lower().replace(" ", "-")
    return formatted_name


# Aplicar a formatação aos nomes dos países
df2['Formatted_Name'] = df2['Area'].apply(format_country_name)

# Exibir os primeiros resultados para validação
print(df2[['Area', 'Formatted_Name']])
