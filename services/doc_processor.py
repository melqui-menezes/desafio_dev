import csv


def read_file_txt(file_txt):

    with open(file_txt, "r") as file_txt:

        read_file = csv.reader(file_txt, dialect=csv.excel_tab)
        file = [row for row in read_file]
        file.remove(file[0])
        lote_value = 0
        for index, row in enumerate(file):
            file[index] = {
                "comprador": row[0],
                "descricao": row[1],
                "preco_und": float(row[2]),
                "quantidade": int(row[3]),
                "endereco": row[4],
                "fornecedor": row[5],
                "total_venda": float(row[2]) * int(row[3]),
            }
            lote_value += file[index]["total_venda"]
        return {
            "vendas": file,
            "total_vendas": lote_value,
        }
