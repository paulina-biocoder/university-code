# PL: Translator nukleotydów na aminokwasy

W programie na początku została stworzona funkcja nucleotides, w której znajduje się tabela kodu geneytcznego (sekwencji trójek nukleotydowych, które będą transkrybowane z podanej nici DNA). 
Jeśli trójka nie znajduje się w tabeli, to w jej miejsce wpisuje się "?".
Funkcja plik_fasta natomiast otwiera dwa pilki w formacie FASTA, wejściowy i wyjściowy, 
plik wejściowy odczytuje sekwencje nukleotydów, a zapisuje ją w pliku wyjściowym jako sekwencje aminkowasową.
W celu transkrypcji sekwencji nukleotydów, stosujemy warunek if,  
który do zmiennej codons przypisuje listę złożoną z wycinków sekwencji - sekwencja, zaczynający się od indeksu i-tego i kończący na indeksie i-tym powiększonym o 3.
W pętli range, 3 argument oznacza, że i ma się zwiększać o krok równy 3.
Jeśli sekwencja rozpoczyna się od kodonu START (TAC - Met), to rozpoczynamy pętlę for.
W pętli sprawdzamy wszystkie następujące sekwencje, jeśli zgadzają się z tabelą kodu genetycznego, przypisujemy je do zmiennej - protein.
Jeśli kodon oznacza sekwencję STOP, przerywamy pracę pętli.
Następnie do plików wyjściowego i wejściowego przypisujemy odpowiednie nagłówki.

# EN: Nucleotide to amino acid translator

In the program, the nucleotides function was created at the beginning, where there is a table of the genitive code (the sequence of nucleotide triplets that will be transcribed from the given DNA strand). 
If the triplet is not in the table, a "?" is entered in its place.
The file_fasta function, on the other hand, opens two FASTA-formatted files, an input file and an output file, 
the input file reads the nucleotide sequence, and writes it in the output file as an amino acid sequence.
To transcribe the nucleotide sequence, we use the if condition,  
which assigns to the variable codons a list consisting of slices of the sequence - sequence, starting at the i-th index and ending at the i-th index incremented by 3.
In a range loop, the 3 argument means that i is to increment by a step equal to 3.
If the sequence starts with the START codon (TAC - Met), we start the for loop.
In the loop we check all the following sequences, if they agree with the genetic code table, we assign them to the variable - protein.
If the codon indicates a STOP sequence, we stop the loop.
Then we assign the corresponding headers to the output and input files.
