from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    queue_names = [item["nome_do_arquivo"] for item in instance.queue]
    if path_file not in queue_names:
        text_lines_list = txt_importer(path_file)
        archive_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_lines_list),
            "linhas_do_arquivo": text_lines_list,
        }
        instance.enqueue(archive_dict)
        print(archive_dict, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        archive = instance.dequeue()
        print(f'Arquivo {archive["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
