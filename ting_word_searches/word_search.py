def search_word(word, item):
    text_lines = item["linhas_do_arquivo"]
    occurrences = list()

    for index in range(len(text_lines)):
        if word in text_lines[index].lower():
            occurrences.append({"linha": index + 1})

    return occurrences


def exists_word(word, instance):
    queue_items = [item for item in instance.queue]
    response = []
    for item in queue_items:
        item_search_data = {
            "palavra": word,
            "arquivo": item["nome_do_arquivo"],
            "ocorrencias": search_word(word, item)
        }
        if len(item_search_data["ocorrencias"]) > 0:
            response.append(item_search_data)
    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
