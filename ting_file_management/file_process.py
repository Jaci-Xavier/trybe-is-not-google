import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    file_dir = txt_importer(path_file)
    file_return = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_dir),
        'linhas_do_arquivo': file_dir
    }
    instance.enqueue(file_return)
    sys.stdout.write(f'{file_return}\n')
    return file_return


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
