from inventory_report.inventory.product import Product


def test_relatorio_produto():
    p1 = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )

    assert p1.id == 1
    assert p1.nome_do_produto == "Nicotine Polacrilex"
    assert p1.nome_da_empresa == "Target Corporation"
    assert p1.data_de_fabricacao == "2021-02-18"
    assert p1.data_de_validade == "2023-09-17"
    assert p1.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    assert p1.instrucoes_de_armazenamento == "instrucao 1"