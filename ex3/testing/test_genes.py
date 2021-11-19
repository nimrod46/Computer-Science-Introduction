from ex3.genes import *


def test_main(monkeypatch, capfd):
    genes_path = str(__file__).replace("\\test_genes.py", "\\gene_files") + "\\genome"
    proteins_path = str(__file__).replace("\\test_genes.py", "\\proteins_files") + "\\genome"
    for i in range(1, 6):
        monkeypatch.setattr('builtins.input', lambda _: genes_path + str(i))
        main()
        with open(genes_path + str(i) + "_proteins.txt") as result:
            with open(proteins_path + str(i) + "_proteins.txt") as expect_result:
                assert result.read().replace("\n", "") == expect_result.read().replace("\n", "")
        # out, err = capfd.readouterr()
        # assert out == "Longest arithmetic sequence: 15, 13, 11, 9, 7, 5"
