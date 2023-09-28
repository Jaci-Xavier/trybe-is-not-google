def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        occurrences = []
        file = instance.search(i)

        for line_num, line in enumerate(file
                                        ['linhas_do_arquivo'], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_num})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": occurrences
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
