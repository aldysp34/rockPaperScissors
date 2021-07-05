"""
Permainan Batu, Gunting, Kertas
"""
from random import randint

#Masukkan komponen utama permainan ke dalam list
component = ['batu', 'gunting', 'kertas']

#Berapa kali main
batas = int(input('Mau berapa kali main? '))

#menentukan sedang bermain permainan yang ke berapa
main = 0

#menghitung berapa kali player menang
playerWins = 0

#menghitung berapa kali computer menang
computerWins = 0

#sebagai acuan apakah player menang atau tidak
menang = False
    
while main < batas:
    #komponen yang dipilih player
    player = input('Batu, Gunting, Kertas ? ')

    #memberikan komponen kepada computer secara random
    computer = component[randint(0,2)]
    computer = component.index(computer)
    
    #menjadikan pilihan player menjadi lowercase
    player = player.lower()

    #apabila pilihan player tidak ada pada list
    if player not in component:
        print('Pilihan gaada')
        continue
    
    #mencari index komponen berdasarkan pilihan player
    for word in component:
        if word == player:
            player = component.index(player)

    #jika Seri
    if player == computer:
        print('Seri')
        main+=1
        continue
    else:
        #kondisi jika player menang
        if player == 0 and computer == 1:
            print('Menang')
            menang = True
        elif player == 1 and computer == 2:
            print('menang')
            menang = True
        elif player == 2 and computer == 0:
            print('menang')
            menang = True

        #kondisi jika player kalah
        elif player == 0 and computer == 2:
            print('kalah')
            menang = False
        elif player == 1 and computer == 0:
            print('kalah')
            menang = False
        elif player == 2 and computer == 1:
            print('kalah')
            menang = False
    
    #jika player menang maka jumlah kemenangan player + 1
    if menang is True:
        playerWins+=1
        
    #jika player kalah maka jumlah kemenangan computer + 1    
    else:
        computerWins+=1

    main+=1

#string result
wordResult = 'Score Kamu = {} : Computer = {}'.format(playerWins, computerWins)

#jika jumlah menang player lebih sedikit dari computer
if playerWins < computerWins:
    print('Kamu Kalah')
    print(wordResult)

#jika jumlah menang player lebih banyak dari computer
elif playerWins > computerWins:
    print('Kamu Menang')
    print(wordResult)

#jika jumlah menang player dan computer sama
else:
    print('Kamu Seri')
    print(wordResult)