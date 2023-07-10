'''w fukncji nucleotides, znajduje się tabela kodu geneytcznego (sekwencji trójek nukleotydowych, które będą transkrybowane z podanej nici DNA). 
Jeśli trójka nie znajduje się w tabeli, to w jej miejsce wpisuje się "?".
Funkcja plik_fasta natomiast otwiera dwa pilki w formacie FASTA, wejściowy i wyjściowy, 
plik wejściowy odczytuje sekwencje nukleotydów, a zapisuje ją w pliku wyjściowym jako sekwencje aminkowasową.
W celu transkrypcji sekwencji nukleotydów, stosujemy warunek if,  
który do zmiennej codons przypisuje listę złożoną z wycinków sekwencji - sekwencja, zaczynający się od indeksu i i kończący na indeksie i+3.
W pętli range, 3 argument oznacza, że i ma się zwiększać o krok równy 3.
Jeśli sekwencja rozpoczyna się od kodonu START (TAC - Met), to rozpoczynamy pętlę for.
W pętli sprawdzamy wszystkie następujące sekwencje, jeśli zgadzają się z tabelą kodu genetycznego, przypisujemy je do zmiennej - protein.
Jeśli kodon oznacza sekwencję STOP, przerywamy pracę pętli.
Następnie do plików wyjściowego i wejściowego przypisujemy odpowiednie nagłówki.
'''

def nucleotides(codon):

    genetic_code = {
        'TTT': 'Lys', 'TAA': 'Ile', 'CAT': 'Val', 'TCA': 'Ser', 'TGA': 'Thr', 'CGT': 'Ala',
        'TTC': 'Lys', 'TAG': 'Ile', 'CAC': 'Val', 'TCG': 'Ser', 'TGG': 'Thr', 'CGC': 'Ala',
        'AAA': 'Phe', 'TAT': 'Ile', 'AGA': 'Ser', 'GGA': 'Pro', 'TGT': 'Thr', 'ATA': 'Tyr',
        'AAG': 'Phe', 'TAC': 'Met', 'AGG': 'Ser', 'GGG': 'Pro', 'TGC': 'Thr', 'ATG': 'Tyr',
        'AAT': 'Leu', 'CAA': 'Val', 'AGT': 'Ser', 'GGT': 'Pro', 'CGA': 'Ala', 'GTA': 'His',
        'AAC': 'Leu', 'CAG': 'Val', 'AGC': 'Ser', 'Pro': 'GGC', 'CGG': 'Ala', 'GTG': 'His',
        'CTT': 'Gln', 'TTA': 'Asn', 'CTA': 'Asp', 'CTT': 'Glu', 'ACA': 'Cys', 'ACC': 'Trp',
        'GTC': 'Gln', 'TTG': 'Asn', 'CTG': 'Asp', 'CTC': 'Glu', 'ACG': 'Cys', 'GCA': 'Arg',
        'GCG': 'Arg', 'GCT': 'Arg', 'GCC': 'Arg', 'TCT': 'Arg', 'TCC': 'Arg', 'CCA': 'Gly',
        'CCG': 'Gly', 'CCT': 'Gly', 'CCC': 'Gly', 'ATT': 'STOP', 'ATC': 'STOP', 'ACT': 'STOP',
    }
    return genetic_code.get(codon, '?')

def fasta_file(input_path, output_path):
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        sequence = ''
        for line in input_file:
            if line.startswith('>'):
                headline = line.strip()
                if sequence:
                    transcript = ''
                    codons = []
                    for i in range(0, len(sequence), 3):
                        codon = sequence[i:i+3]
                        codons.append(codon)
                    if codons[0] == 'TAC':
                        for codon in codons:
                            protein = nucleotides(codon)
                            transcript += protein

                            if protein == 'STOP':
                                break

                        output_file.write(headline + ' (After transcription)\n')
                        output_file.write(transcript + '\n')
                    else:
                        output_file.write(headline + ' (Invalid codon - no start codon)\n')
                sequence = ''
            else:
                sequence += line.strip()



input_path = input('Specify the path to the input FASTA file: ')

output_path = input('Specify the path to the output FASTA file: ')

fasta_file(input_path, output_path)

print('You can see the transcription in the file:', output_path)
